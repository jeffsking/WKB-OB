# -*- coding: utf-8 -*-
"""REST get_doc_content 单次试探（日配额≈1次，先落盘再读，禁管道预览）。"""
import json, os, urllib.request
CRED = os.path.join(os.path.expanduser("~"), ".config", "ima")
def rd(n):
    with open(os.path.join(CRED, n), encoding="utf-8") as f: return f.read().strip()
CID, KEY = rd("client_id"), rd("api_key")
def post(path, payload):
    req = urllib.request.Request("https://ima.qq.com/" + path,
        data=json.dumps(payload).encode(), headers={"ima-openapi-clientid": CID,
        "ima-openapi-apikey": KEY, "Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=90) as r:
        return json.loads(r.read().decode("utf-8"))
TARGET = {
  "聚合芯能拜访纪要": ("note_3867e2b60070d7dc3f413086d0b0036e_7518291224433921", "7518291224433921"),
}
out = {}
for name, (mid, nid) in TARGET.items():
    try:
        out[name] = {"media_id": mid, "note_id": nid,
                     "resp": post("openapi/note/v1/get_doc_content", {"note_id": nid})}
    except Exception as e:
        out[name] = {"media_id": mid, "note_id": nid, "err": str(e)}
json.dump(out, open(".tools/_doc_content_20261022.json", "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
for k, v in out.items():
    r = v.get("resp") or {}
    print(k, "| code", r.get("code"), "| msg", str(r.get("msg"))[:60], "| err", v.get("err"))
