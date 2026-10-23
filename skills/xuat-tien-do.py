# Xuất tiến độ sprint cho progress-report.md: bảng trạng thái (đọc từ Project) và bảng SWP còn lại theo ngày giả lập
# (tính từ kịch bản, vì GitHub chỉ ghi ngày thật lúc áp kịch bản). Kiểm trạng thái cuối trên Project khớp kịch bản.
#   python3 skills/xuat-tien-do.py > /tmp/tien-do.md
import json, subprocess, sys
from collections import Counter
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent.parent
SCENARIO = ROOT / "skills" / "kich-ban-sprint-1.yaml"
STATUS_NAME = {"todo": "Todo", "in-progress": "In Progress", "done": "Done"}


def vn(x):
    s = f"{x:,.1f}".rstrip("0").rstrip(".")
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def main():
    k = yaml.safe_load(SCENARIO.read_text(encoding="utf-8"))
    out = subprocess.run(["gh", "project", "item-list", "1", "--owner", "mytcn-1511", "--format", "json", "--limit", "1000"],
                         capture_output=True, text=True, check=True).stdout
    items = [i for i in json.loads(out)["items"] if (i.get("iteration") or {}).get("title") == k["sprint"]["iteration"]]
    swp = {i["content"]["number"]: i["sWP"] for i in items}
    hours = {i["content"]["number"]: i["giờ ước lượng"] for i in items}
    status = {i["content"]["number"]: i.get("status") for i in items}

    # Trạng thái cuối theo kịch bản phải khớp Project
    final, stuck = {}, set()
    for d in k["ngay"]:
        for ev in d["su_kien"]:
            final[ev["issue"]] = ev["status"]
            if ev.get("ket"):
                stuck.add(ev["issue"])
    mismatch = [n for n in swp if STATUS_NAME[final.get(n, "todo")] != status[n]]
    if mismatch:
        sys.exit(f"Project lệch kịch bản ở: {mismatch}")

    total = sum(swp.values())
    print(f"Sprint: {k['sprint']['iteration']} · {k['sprint']['bat_dau']:%d/%m/%Y}–{k['sprint']['ket_thuc']:%d/%m/%Y} · "
          f"{len(swp)} issue · {total} SWP · {vn(sum(hours.values()))} giờ\n")
    print("| Trạng thái | Số issue | Tổng SWP | Giờ ước lượng | Issue |\n|---|---|---|---|---|")
    for st in ("Done", "In Progress", "Todo"):
        ns = sorted(n for n in swp if status[n] == st)
        print(f"| {st} | {len(ns)} | {sum(swp[n] for n in ns)} | {vn(sum(hours[n] for n in ns))} | "
              + ", ".join(f"#{n}" + (" (kẹt)" if n in stuck and st != 'Done' else "") for n in ns) + " |")
    print(f"| **Tổng** | **{len(swp)}** | **{total}** | **{vn(sum(hours.values()))}** | |\n")

    # SWP còn lại theo ngày: issue chỉ trừ vào ngày nó chuyển Done
    state = {n: "todo" for n in swp}
    rows, days = [], len(k["ngay"])
    for idx, d in enumerate(k["ngay"], 1):
        done_today = []
        for ev in d["su_kien"]:
            state[ev["issue"]] = ev["status"]
            if ev["status"] == "done":
                done_today.append(ev["issue"])
        remaining = sum(swp[n] for n, s in state.items() if s != "done")
        plan = total * (1 - idx / days)
        rows.append((d["ngay"], plan, remaining, done_today))
    print("| Ngày giả lập | Kế hoạch còn lại (SWP) | Thực tế còn lại (SWP) | Chênh | Issue xong trong ngày |\n|---|---|---|---|---|")
    for day, plan, rem, dn in rows:
        print(f"| {day:%d/%m} | {vn(plan)} | {rem} | +{vn(rem - plan)} | " + (", ".join(f"#{n}" for n in dn) or "—") + " |")
    labels = ", ".join(f'"{d:%d/%m}"' for d, *_ in rows)
    print("\n```mermaid\nxychart-beta\n    title \"SWP còn lại — Iteration 1\"\n"
          f"    x-axis [{labels}]\n    y-axis \"SWP\" 0 --> {total}\n"
          f"    line [{', '.join(f'{p:.1f}' for _, p, _, _ in rows)}]\n"
          f"    line [{', '.join(str(r) for _, _, r, _ in rows)}]\n```")
    done_swp = sum(swp[n] for n in swp if status[n] == "Done")
    print(f"\nHoàn thành {done_swp}/{total} SWP ({round(done_swp / total * 100)}%); còn {total - done_swp} SWP chuyển sang sprint sau.")


if __name__ == "__main__":
    main()
