# Áp kịch bản giả lập sprint (skills/kich-ban-sprint-1.yaml) lên GitHub:
# - mỗi sự kiện thành một bình luận trên issue, ghi "Ngày giả lập", vai và việc đã làm;
# - trạng thái cuối của mỗi issue ghi vào trường Status của Project; issue Done thì đóng.
# Chạy lại an toàn: bình luận có dấu ẩn <!-- kich-ban:<ngày>:<issue>:<số thứ tự> -->, có rồi thì bỏ qua.
#   python3 skills/ap-kich-ban-sprint.py --dry-run
#   python3 skills/ap-kich-ban-sprint.py
import argparse, json, subprocess, sys, time
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent.parent
SCENARIO = ROOT / "skills" / "kich-ban-sprint-1.yaml"
REPO, OWNER, NUMBER = "mytcn-1511/product-a-lab5-backlog", "mytcn-1511", "1"
STATUS_NAME = {"todo": "Todo", "in-progress": "In Progress", "done": "Done"}


def gh(*args, payload=None):
    for attempt in range(3):  # GitHub đôi khi trả 422 khi đóng nhiều issue liên tiếp; thử lại có giãn cách
        r = subprocess.run(["gh", *args], input=json.dumps(payload) if payload else None, capture_output=True, text=True)
        if r.returncode == 0:
            break
        time.sleep(3 * (attempt + 1))
    else:
        sys.exit(f"gh {' '.join(args[:3])} lỗi: {r.stderr.strip()}")
    return json.loads(r.stdout) if r.stdout.strip() else None


def comment_body(day, ev, marker):
    head = f"**Ngày giả lập:** {day:%d/%m/%Y} · **Vai:** {ev['vai']} · **Trạng thái:** {STATUS_NAME[ev['status']]}"
    if ev.get("ket"):
        head += " · **Đang kẹt**"
    return f"{head}\n\n{ev['ghi']}\n\n_Sprint giả lập theo kịch bản `skills/kich-ban-sprint-1.yaml`; GitHub ghi ngày thật lúc áp kịch bản._\n<!-- {marker} -->"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    k = yaml.safe_load(SCENARIO.read_text(encoding="utf-8"))

    final, plan = {}, []
    for d in k["ngay"]:
        for i, ev in enumerate(d["su_kien"]):
            plan.append((d["ngay"], ev, f"kich-ban:{d['ngay']}:{ev['issue']}:{i}"))
            final[ev["issue"]] = ev["status"]

    # Bình luận đã có (đọc dấu ẩn) để không đăng trùng
    seen = set()
    for n in final:
        for c in gh("api", "--paginate", "--slurp", f"repos/{REPO}/issues/{n}/comments?per_page=100"):
            for cm in c:
                if "<!-- kich-ban:" in (cm["body"] or ""):
                    seen.add(cm["body"].rsplit("<!-- ", 1)[1].split(" -->")[0])

    posted = 0
    for day, ev, marker in plan:
        if marker in seen:
            continue
        print(f"+ #{ev['issue']} {day} {ev['status']}")
        posted += 1
        if not a.dry_run:
            gh("api", "-X", "POST", f"repos/{REPO}/issues/{ev['issue']}/comments", "--input", "-",
               payload={"body": comment_body(day, ev, marker)})
            time.sleep(1)

    project_id = gh("project", "view", NUMBER, "--owner", OWNER, "--format", "json")["id"]
    status = next(f for f in gh("project", "field-list", NUMBER, "--owner", OWNER, "--format", "json")["fields"] if f["name"] == "Status")
    opt = {o["name"]: o["id"] for o in status["options"]}
    items = {it["content"]["number"]: it for it in gh("project", "item-list", NUMBER, "--owner", OWNER, "--format", "json", "--limit", "1000")["items"]}
    changed = 0
    for n, st in final.items():
        want = STATUS_NAME[st]
        if items[n].get("status") != want:
            changed += 1
            print(f"~ #{n} Status: {items[n].get('status')} → {want}")
            if not a.dry_run:
                gh("project", "item-edit", "--id", items[n]["id"], "--project-id", project_id,
                   "--field-id", status["id"], "--single-select-option-id", opt[want])
        issue = gh("api", f"repos/{REPO}/issues/{n}")
        if st == "done" and issue["state"] == "open":
            changed += 1
            print(f"~ #{n} đóng issue")
            if not a.dry_run:
                gh("api", "-X", "PATCH", f"repos/{REPO}/issues/{n}", "--input", "-",
                   payload={"state": "closed", "state_reason": "completed"})
                time.sleep(1)
    print(f"Bình luận mới: {posted} · thay đổi trạng thái/đóng: {changed}" + (" (dry-run, chưa ghi)" if a.dry_run else ""))


if __name__ == "__main__":
    main()
