# -*- coding: utf-8 -*-
"""探测今日 9 条新条目的 get_media_info（不下载），落盘后读。"""
import json, os, urllib.request, time
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
MIDS = json.load(open(".tools/_new_mids_20261022.json", encoding="utf-8"))
out = {}
for mid in MIDS:
    try:
        out[mid] = post("openapi/wiki/v1/get_media_info", {"media_id": mid})
    except Exception as e:
        out[mid] = {"_err": str(e)}
    time.sleep(2.0)
json.dump(out, open(".tools/_media_probe_20261022.json","w",encoding="utf-8"), ensure_ascii=False, indent=1)
for mid, r in out.items():
    d = (r.get("data") or {})
    ui = d.get("url_info") or {}
    print(mid[:52], "| code", r.get("code"), "|",
          "url:", (ui.get("url") or "-")[:60], "|",
          "keys:", sorted(d.keys())[:8])
