import json, sys, os
# usage: python _mk_shard.py <folder_id> <raw_json_file>
# normalizes full objects to slim objects
fid = sys.argv[1]
rawf = sys.argv[2]
raw = json.load(open(rawf, encoding="utf-8"))
lst = raw.get("knowledge_list", [])
def slim(it):
    return {
        "media_id": it.get("media_id"),
        "media_type": it.get("media_type"),
        "title": it.get("title"),
        "media_state": it.get("media_state"),
        "create_time": it.get("create_time"),
        "folder_info": it.get("folder_info"),
        "parent_folder_id": it.get("parent_folder_id"),
    }
out = [slim(x) for x in lst]
json.dump(out, open(f"E:/WKB-OB/.tools/_enum_work/{fid}.json","w",encoding="utf-8"), ensure_ascii=False, indent=1)
print(fid, "saved", len(out), "is_end=", raw.get("is_end"), "total_size=", raw.get("total_size"))
