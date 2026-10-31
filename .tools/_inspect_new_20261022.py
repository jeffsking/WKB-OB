import json, os
led = json.load(open(".tools/_ima_sync_state.json", encoding="utf-8"))
enum = json.load(open(".tools/_ima_enum_20261022.json", encoding="utf-8"))
old = json.load(open(".tools/_ima_enum_20261021.json", encoding="utf-8"))
o = {e["media_id"] for e in old["items"]}
new = [e["media_id"] for e in enum["items"] if e["media_id"] not in o]
for mid in new:
    it = led["items"][mid]
    print("-"*100)
    print(mid)
    for k in ("title","media_type","status","raw_path","full_path","kb_path","source_page_hint","create_time"):
        print(f"  {k}: {it.get(k)}")
    rp = it.get("raw_path")
    if rp:
        p = os.path.join(".", rp)
        print("  RAW exists:", os.path.exists(p), "size:", os.path.getsize(p) if os.path.exists(p) else "-")
