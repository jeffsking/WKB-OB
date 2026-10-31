import json
def load(p):
    return json.load(open(p, encoding="utf-8"))
new = load(".tools/_ima_enum_20261022.json")
old = load(".tools/_ima_enum_20261021.json")
led = load(".tools/_ima_sync_state.json")
def s(d):
    return {e["media_id"] for e in d["items"]}
n, o, l = s(new), s(old), set(led["items"].keys())
print("new enum files:", len(n), "| 10-21 enum files:", len(o), "| ledger:", len(l))
print("新增(vs 10-21):", len(n - o))
print("消失(vs 10-21):", len(o - n))
print("新增(vs 账本):", len(n - l))
print("账本多登(vs 本轮枚举):", len(l - n))
byid = {e["media_id"]: e for e in new["items"]}
oid = {e["media_id"]: e for e in old["items"]}
print("\n--- 新增明细 ---")
for mid in sorted(n - o):
    e = byid[mid]
    print(f"{mid} | type={e.get('media_type')} | {e.get('title')} | kb_path={e.get('kb_path')}")
print("\n--- 消失明细 ---")
for mid in sorted(o - n):
    e = oid[mid]
    print(f"{mid} | type={e.get('media_type')} | {e.get('title')}")
