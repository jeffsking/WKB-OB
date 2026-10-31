import json, os, urllib.request
CRED = os.path.join(os.path.expanduser("~"), ".config", "ima")
def rd(n):
    with open(os.path.join(CRED, n), encoding="utf-8") as f: return f.read().strip()
CID, KEY = rd("client_id"), rd("api_key")
def post(path, payload):
    req = urllib.request.Request("https://ima.qq.com/" + path,
        data=json.dumps(payload).encode(), headers={"ima-openapi-clientid": CID,
        "ima-openapi-apikey": KEY, "Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))
res = {}
for kb in ["ima_kb_l24tiCGM", "001a693ee6c0644e", "F8DbmyEF1G8cO-4woYjmlpOs1dETfSgd8-mu6PSsPOI="]:
    res[kb] = post("openapi/wiki/v1/get_knowledge_list",
        {"knowledge_base_id": kb, "limit": 5, "cursor": "", "sort_type": "MEDIA_DESC_SORT_TYPE"})
with open(".tools/_kb_probe_list_20261022.json", "w", encoding="utf-8") as f:
    json.dump(res, f, ensure_ascii=False, indent=1)
for k, v in res.items():
    print(k, "->", v.get("code"), v.get("msg"),
          len(v.get("data", {}).get("knowledge_list", []) or []), "items")
