import json, os, re
MIDS = ["01a162b62dff7dbcaed0855d0b90a280","01a162b5e6017d5d938b55d238339fc0",
        "01a162b49b01773995ca0f3c60a7e32000","01a162b3c01a7f08b4e7cda51ad15652",
        "01a162b36c8c7e51a178d839cfd68bad","5d9bbd4465f535eb0f873c570d397830",
        "910cc7726e3b79b9729c5536a6d86c5c","903428b49d13679de587398ab07212eb","7518874194940520"]
hits = {m: [] for m in MIDS}
for base in ("RAW",):
    for dp, dn, fn in os.walk(base):
        for f in fn:
            p = os.path.join(dp, f)
            try:
                head = open(p, encoding="utf-8", errors="ignore").read(1200)
            except Exception:
                continue
            for m in MIDS:
                if m in head:
                    hits[m].append(p.replace("\\","/"))
for m, ps in hits.items():
    print(m, "->", len(ps))
    for p in ps: print("   ", p)
