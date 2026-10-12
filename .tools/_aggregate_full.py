import json, os, glob, re

WORK = r"E:\WKB-OB\.tools\_enum_work"
OUT  = r"E:\WKB-OB\.tools\_ima_enum_full_20261011.json"
ROOT = "001a693ee6c0644e"

# ---- collect all entries from shards (dedupe by media_id) ----
by_id = {}
folder_by_id = {}   # folder_id -> {name, parent_folder_id}
raw_total = 0
for fp in glob.glob(os.path.join(WORK, "*.json")):
    if os.path.basename(fp).startswith("_"):
        continue
    try:
        data = json.load(open(fp, encoding="utf-8"))
    except Exception as e:
        print("ERR", fp, e)
        continue
    if isinstance(data, dict):
        data = data.get("items") or data.get("root") or []
    for it in data:
        raw_total += 1
        mid = it.get("media_id")
        if not mid:
            continue
        if mid not in by_id:
            by_id[mid] = it
        if it.get("media_type") == 99:
            fi = it.get("folder_info") or {}
            fid = fi.get("folder_id") or mid
            folder_by_id[fid] = {
                "name": fi.get("name") or it.get("title") or "",
                "parent_folder_id": fi.get("parent_folder_id") or "",
                "file_number": fi.get("file_number"),
                "folder_number": fi.get("folder_number"),
            }

print("shard entries (raw):", raw_total)
print("unique media_id:", len(by_id))
print("folders found:", len(folder_by_id))

# ---- guard: every folder's parent must be known ----
missing_parents = set()
for fid, info in folder_by_id.items():
    p = info["parent_folder_id"]
    if p and p != ROOT and p not in folder_by_id:
        missing_parents.add(p)
if missing_parents:
    print("!! UNRESOLVED PARENT FOLDERS:", missing_parents)

# ---- build folder kb_path ----
def safe_name(s):
    return (s or "").replace("/", "_")

fpath = {ROOT: ""}
def f_path(fid, seen=None):
    if fid in fpath:
        return fpath[fid]
    seen = seen or set()
    if fid in seen:
        return safe_name(folder_by_id.get(fid, {}).get("name", fid))
    seen.add(fid)
    info = folder_by_id.get(fid)
    if not info:
        fpath[fid] = ""
        return ""
    p = info["parent_folder_id"]
    pbase = "" if (not p or p == ROOT) else f_path(p, seen)
    nm = safe_name(info["name"])
    fpath[fid] = (pbase + "/" + nm) if pbase else nm
    return fpath[fid]

for fid in list(folder_by_id.keys()):
    f_path(fid)

# ---- folders[] ----
folders = []
for fid, info in folder_by_id.items():
    folders.append({
        "kb_path": fpath.get(fid, safe_name(info["name"])),
        "folder_id": fid,
        "total_size": None,  # not tracked per-folder in shards
        "file_number": info.get("file_number"),
        "folder_number": info.get("folder_number"),
    })
folders.sort(key=lambda x: ((x["kb_path"] or "").count("/"), x["kb_path"] or ""))
# ---- items[] : media_state==2 and not folder ----
items = []
skipped_non2 = 0
seen_item = set()
for mid, it in by_id.items():
    if it.get("media_type") == 99:
        continue
    st = it.get("media_state")
    if st != 2:
        skipped_non2 += 1
        continue
    if mid in seen_item:
        continue
    seen_item.add(mid)
    # find parent folder path
    p = it.get("parent_folder_id") or ""
    base = fpath.get(p, "")
    title = safe_name(it.get("title") or "")
    kb_path = (base + "/" + title) if base else title
    items.append({
        "kb_path": kb_path,
        "media_id": mid,
        "media_type": it.get("media_type"),
        "title": it.get("title"),
        "media_state": st,
        "create_time": it.get("create_time"),
        "parent_folder_id": p,
    })

items.sort(key=lambda x: x["kb_path"])

result = {
    "root": [ROOT],
    "items": items,
    "folders": folders,
    "_meta": {
        "enumerated_at": "2026-10-11",
        "folders_visited": len(folder_by_id),
        "raw_total": raw_total,
        "items_count": len(items),
        "skipped_non2": skipped_non2,
        "folders_count": len(folders),
        "collected_entries": len(items) + len(folders) + skipped_non2,
        "total_size_reported": 1382,
        "note": "total_size_reported (1382) is IMA's KB-level metric; recursive enumeration yields more entries (folders are counted separately / metric is approximate).",
    },
}

json.dump(result, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("=== WROTE", OUT)
print("root", len(result["root"]), "items", len(items), "folders", len(folders))
print("skipped_non2", skipped_non2, "folders_visited", len(folder_by_id))
