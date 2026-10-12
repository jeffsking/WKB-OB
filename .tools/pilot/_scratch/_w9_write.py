import json, sys, os, io

tmp, media_id, name, dst = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

raw = io.open(tmp, "r", encoding="utf-8", errors="replace").read()
raw = raw.strip()
try:
    obj = json.loads(raw)
    content = obj.get("content", "") if isinstance(obj, dict) else str(obj)
except Exception:
    content = raw

dst_path = os.path.join("E:/WKB-OB", dst)
os.makedirs(os.path.dirname(dst_path), exist_ok=True)

rel = dst
for p in ("RAW_FULL/ima_sync/WKB/",):
    if rel.startswith(p):
        rel = rel[len(p):]

fm = (
    "---\n"
    'media_id: "%s"\n'
    'source_file: "%s"\n'
    'original_path: "RAW/ima_sync/WKB/%s"\n'
    'extracted: "2026-09-27"\n'
    'extract_method: "ima-mcp fetch_media_content"\n'
    'extract_status: "ok"\n'
    'clean_rules: ""\n'
    'processed: ""\n'
    "---\n\n# %s\n\n%s" % (media_id, name, rel, name, content)
)

with io.open(dst_path, "w", encoding="utf-8", newline="\n") as f:
    f.write(fm)

sys.stdout.write("WROTE %d chars %s" % (len(content), dst_path))
