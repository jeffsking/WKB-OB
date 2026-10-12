import json, os, glob, re

W = r"E:/WKB-OB/.tools/_enum_work"
visited = set()
allsub = {}  # folder_id -> {name, parent}
entries_total = 0

for fp in glob.glob(os.path.join(W, "*.json")):
    base = os.path.basename(fp)
    if base == "root.json" or base == "_root.json":
        # root shard: still scan children
        pass
    m = re.match(r"(folder_\d+)", base)
    if m:
        visited.add(m.group(1))
    try:
        data = json.load(open(fp, encoding="utf-8"))
    except Exception as e:
        print("ERR", base, e); continue
    if not isinstance(data, list):
        # could be dict with 'root'
        if isinstance(data, dict):
            data = data.get("root") or data.get("items") or []
        else:
            continue
    for it in data:
        if not isinstance(it, dict): continue
        entries_total += 1
        fi = it.get("folder_info") or {}
        fid = fi.get("folder_id") or ""
        if it.get("media_type") == 99 and fid:
            allsub[fid] = {"name": it.get("title",""), "parent": it.get("parent_folder_id","")}

print("visited folders:", len(visited))
print("known subfolders:", len(allsub))
print("entries scanned:", entries_total)

unvisited = {fid:v for fid,v in allsub.items() if fid not in visited}
print("=== UNVISITED:", len(unvisited), "===")
for fid,v in sorted(unvisited.items()):
    print(fid, "|", v["name"], "| parent=", v["parent"])

json.dump(unvisited, open("E:/WKB-OB/.tools/_unvisited.json","w",encoding="utf-8"), ensure_ascii=False, indent=1)
