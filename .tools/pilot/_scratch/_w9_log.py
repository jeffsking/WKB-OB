import json, io, os, re, sys

LOG = r"C:/Users/Chris Wang/.workbuddy/projects/e-WorkBuddy-Workplace-Obsidian/7c5f96dd-83e0-4965-9cd5-4594fb238c9f/subagents/agent-e5c6979fa05043fd.jsonl"

# build callId -> arguments
calls = {}
results = {}
for line in io.open(LOG, encoding="utf-8"):
    line = line.strip()
    if not line:
        continue
    try:
        o = json.loads(line)
    except Exception:
        continue
    t = o.get("type")
    cid = o.get("callId")
    if t == "function_call" and cid:
        calls[cid] = o.get("arguments", "") or ""
    elif t == "function_call_result" and cid:
        results[cid] = o.get("output", "")

# map media_id -> result output
media_to_out = {}
for cid, args in calls.items():
    try:
        a = json.loads(args) if isinstance(args, str) else args
    except Exception:
        continue
    mid = None
    if isinstance(a, dict):
        mid = a.get("media_id") or (a.get("params") or {}).get("media_id") if isinstance(a.get("params"), dict) else a.get("media_id")
    if mid and cid in results:
        media_to_out[mid] = results[cid]

batch = json.load(io.open(r"E:/WKB-OB/.tools/pilot/W9_batch_1.json", encoding="utf-8"))

log_lines = []
ok = empty = failed = 0

for item in batch["items"]:
    mid, dst, name, typ = item["media_id"], item["dst"], item["name"], item["type"]

    def get_text():
        out = media_to_out.get(mid)
        if out is None:
            return None, "noresult"
        if isinstance(out, str):
            s = out
        elif isinstance(out, dict) and "text" in out:
            s = out["text"]
        elif isinstance(out, list):
            s = "".join(
                (b.get("text", "") if isinstance(b, dict) else str(b)) for b in out
            )
        else:
            s = json.dumps(out, ensure_ascii=False)
        m = re.search(r"saved to ([^\s]+\.txt)", s)
        if m:
            p = m.group(1)
            if os.path.exists(p):
                raw = io.open(p, encoding="utf-8", errors="replace").read().strip()
                try:
                    obj = json.loads(raw)
                    return (obj.get("content", "") if isinstance(obj, dict) else str(obj)), "ok"
                except Exception:
                    return raw, "ok"
            return None, "tmpmissing"
        try:
            obj = json.loads(s)
            if isinstance(obj, dict) and "content" in obj:
                return obj["content"], "ok"
        except Exception:
            pass
        return None, "error:" + s[:200]

    content, st = get_text()
    n = len(content) if content else 0

    if st != "ok":
        failed += 1
        log_lines.append("%s | 0 | failed(%s)" % (name, st[:80]))
        continue

    if content == "":
        empty += 1
        log_lines.append("%s | 0 | empty" % name)
        continue

    rel = dst
    pre = "RAW_FULL/ima_sync/WKB/"
    if rel.startswith(pre):
        rel = rel[len(pre):]
    dst_path = os.path.join("E:/WKB-OB", dst)
    os.makedirs(os.path.dirname(dst_path), exist_ok=True)
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
        "---\n\n# %s\n\n%s" % (mid, name, rel, name, content)
    )
    with io.open(dst_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(fm)
    ok += 1
    log_lines.append("%s | %d | ok" % (name, n))

print("\n".join(log_lines))
print("成功 %d / 源侧空 %d / 失败 %d" % (ok, empty, failed))
