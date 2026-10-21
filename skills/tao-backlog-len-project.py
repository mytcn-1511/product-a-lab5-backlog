# Đọc skills/backlog.yaml, tạo epic → issue → issue con trên repo, nối cha–con bằng sub-issue và thêm mọi issue vào Project.
# Chạy lại an toàn: mỗi issue có dòng "key: <mã>" cuối thân; issue đã có thì không tạo lại, chỉ sửa thân nếu nội dung đổi.
# Cách chạy (cần gh đã đăng nhập, có scope project):
#   python3 skills/tao-backlog-len-project.py --dry-run            # chỉ in việc sẽ làm
#   python3 skills/tao-backlog-len-project.py --epic E-T10         # chạy một epic
#   python3 skills/tao-backlog-len-project.py                      # chạy toàn bộ (chạy 2 lần để mọi dòng "Làm sau" có số issue)
import argparse, json, re, subprocess, sys, time
from pathlib import Path
import yaml

YAML_PATH = Path(__file__).with_name("backlog.yaml")
KEY_RE = re.compile(r"(?m)^key: (\S+)$")
PAUSE = 1.5  # giây nghỉ sau mỗi lần ghi để GitHub không chặn vì tạo quá nhanh


def gh(*args, payload=None):
    """Gọi gh, trả JSON (hoặc None nếu không có đầu ra). Dừng hẳn nếu lỗi."""
    r = subprocess.run(["gh", *args], input=json.dumps(payload) if payload else None,
                       capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"gh {' '.join(args[:3])} lỗi: {r.stderr.strip()}")
    return json.loads(r.stdout) if r.stdout.strip() else None


def flatten(epics):
    """Trả danh sách (mục, khoá cha) theo thứ tự tạo: epic, rồi issue, rồi issue con."""
    out = []
    for e in epics:
        out.append(({**e, "_epic": True}, None))
        for i in e.get("issues", []):
            out.append((i, e["key"]))
            out += [(c, i["key"]) for c in i.get("con", [])]
    return out


def ref(key, existing, titles):
    """Dòng tham chiếu một issue khác: số issue nếu đã có, không thì mã khoá."""
    return f"#{existing[key]['number']}" if key in existing else f"{titles.get(key, key)} (chưa tạo, mã {key})"


def build_title(item):
    return f"[Epic] {item['title']}" if item.get("_epic") else item["title"]


def build_body(item, meta, existing, titles):
    if item.get("_epic"):
        parts = [item["body"].strip()]
    else:
        crit = "\n".join(f"- [ ] {c}" for c in item["tieu_chi_xong"])
        parts = [f"## Bối cảnh\n{item['boi_canh'].strip()}", f"## Việc\n{item['viec'].strip()}", f"## Tiêu chí xong\n{crit}"]
        if "doi:fe" in item["labels"]:
            parts.append("## Định nghĩa xong chung cho màn hình\n" + "\n".join(f"- [ ] {c}" for c in meta["dinh_nghia_xong_chung_man_hinh"]))
        parts.append("## File chạm (trong prototype)\n" + "\n".join(f"- `{f}`" for f in item["file_cham"]))
        if item.get("lam_sau"):
            parts.append("## Làm sau\n" + "\n".join(f"- {ref(k, existing, titles)}" for k in item["lam_sau"]))
    return "\n\n".join(parts) + f"\n\n---\nkey: {item['key']}\n"


def load_existing(repo):
    issues = [i for page in gh("api", "--paginate", "--slurp", f"repos/{repo}/issues?state=all&per_page=100") for i in page]
    found = {}
    for it in issues:
        m = KEY_RE.search(it.get("body") or "")
        if m and "pull_request" not in it:
            found[m.group(1)] = {k: it[k] for k in ("number", "id", "html_url", "body", "title")}
    return found


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--epic", action="append", help="chỉ chạy epic này (lặp lại được)")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    data = yaml.safe_load(YAML_PATH.read_text(encoding="utf-8"))
    meta, repo = data["meta"], data["meta"]["repo"]
    epics = [e for e in data["epics"] if not a.epic or e["key"] in a.epic]
    if a.epic and len(epics) != len(a.epic):
        sys.exit(f"Không thấy epic: {set(a.epic) - {e['key'] for e in epics}}")
    titles = {i["key"]: i["title"] for i, _ in flatten(data["epics"])}

    existing = load_existing(repo)
    project_urls = {it["content"]["url"] for it in gh("project", "item-list", str(meta["project_number"]),
                    "--owner", meta["project_owner"], "--format", "json", "--limit", "2000")["items"] if it.get("content")}
    counts = dict(tao=0, sua=0, giu=0, noi=0, project=0)

    for item, parent in flatten(epics):
        key, title = item["key"], build_title(item)
        body = build_body(item, meta, existing, titles)
        labels = item.get("labels") or []
        if key not in existing:
            print(f"+ tạo   {key}  ({len(labels)} nhãn{', cha ' + parent if parent else ''})")
            counts["tao"] += 1
            if a.dry_run:
                continue
            it = gh("api", "-X", "POST", f"repos/{repo}/issues", "--input", "-",
                    payload={"title": title, "body": body, "labels": labels, "assignees": [meta["assignee"]]})
            existing[key] = {k: it[k] for k in ("number", "id", "html_url", "body", "title")}
            time.sleep(PAUSE)
        elif existing[key]["body"] != body or existing[key]["title"] != title:
            print(f"~ sửa   {key}  #{existing[key]['number']}")
            counts["sua"] += 1
            if not a.dry_run:
                gh("api", "-X", "PATCH", f"repos/{repo}/issues/{existing[key]['number']}", "--input", "-",
                   payload={"title": title, "body": body})
                time.sleep(PAUSE)
        else:
            counts["giu"] += 1
        if a.dry_run:
            continue

        cur = existing[key]
        if parent:  # nối vào cha nếu chưa nối
            p = existing[parent]["number"]
            subs = {s["id"] for s in gh("api", f"repos/{repo}/issues/{p}/sub_issues?per_page=100") or []}
            if cur["id"] not in subs:
                gh("api", "-X", "POST", f"repos/{repo}/issues/{p}/sub_issues", "--input", "-", payload={"sub_issue_id": cur["id"]})
                counts["noi"] += 1
                time.sleep(PAUSE)
        if cur["html_url"] not in project_urls:
            gh("project", "item-add", str(meta["project_number"]), "--owner", meta["project_owner"], "--url", cur["html_url"])
            project_urls.add(cur["html_url"])
            counts["project"] += 1
            time.sleep(PAUSE)

    print(f"\nTạo {counts['tao']} · sửa {counts['sua']} · giữ nguyên {counts['giu']} · nối cha–con {counts['noi']} · thêm vào Project {counts['project']}"
          + ("  (dry-run, chưa ghi gì)" if a.dry_run else ""))


if __name__ == "__main__":
    main()
