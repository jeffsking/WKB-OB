import json
led = json.load(open(".tools/_ima_sync_state.json", encoding="utf-8"))
from collections import Counter
c = Counter()
for mid, it in led["items"].items():
    c[(mid.split("_")[0], it.get("status"))] += 1
for k,v in sorted(c.items(), key=lambda x:-x[1]): print(k, v)
print("\n--- 已落地 type15 样例 ---")
n=0
for mid, it in led["items"].items():
    if mid.startswith("soundrecording") and it.get("raw_path"):
        print(mid[:60], "|", it.get("raw_path"), "|", it.get("full_path"), "|", it.get("status"))
        n+=1
        if n>=4: break
print("\n--- 已落地 type7 markdown 样例 ---")
n=0
for mid, it in led["items"].items():
    if mid.startswith("markdown") and it.get("raw_path"):
        print(mid[:60], "|", it.get("raw_path"), "|", it.get("status"))
        n+=1
        if n>=4: break
