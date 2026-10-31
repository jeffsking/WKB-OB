import json, os, urllib.request
CRED = os.path.join(os.path.expanduser("~"), ".config", "ima")
def rd(n):
    with open(os.path.join(CRED, n), encoding="utf-8") as f:
        return f.read().strip()
CID, KEY = rd("client_id"), rd("api_key")
def post(path, payload):
    req = urllib.request.Request("https://ima.qq.com/" + path,
        data=json.dumps(payload).encode(), headers={"ima-openapi-clientid": CID,
        "ima-openapi-apikey": KEY, "Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))
out = {}
out["addable"] = post("openapi/wiki/v1/get_addable_knowledge_base_list", {"limit": 49, "cursor": ""})
with open(".tools/_kb_check_20261022.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
print("code", out["addable"].get("code"))
