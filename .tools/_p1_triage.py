"""Triage the P1 backlog: hygiene relevance tier + body-content availability."""
import json
import os
import re

VAULT = "E:/WKB-OB"
m = json.load(open(".tools/ebook_p1_manifest.json", encoding="utf-8"))

# Tier by relevance to Chris's work: REL 超薄芯体 / SAP / PP 无纺布改性 / 纳米纤维素 /
# 弹性纤维 / 胶黏剂 / 涂布复合 / 变色油墨
TIER1 = [  # 纤维-聚烯烃-ES 主键轴（直接命中 PP 无纺布与双组分纤维）
    "manufactured_fibre", "dual component", "pp handbook", "polypropylene",
    "es纤维", "双组分纤维", "涂布复合", "聚氨酯弹性体",
]
TIER2 = [  # 高分子基础与流变（打底 + 弹性体/粘合机理）
    "seymour", "ebewole", "physical_polymer", "principles_of_polymerization",
    "polymer_reaction", "viscoelastic", "rubber_elasticity", "plastic_films",
    "polymer_testing", "biodegradable_thermoplastic", "polymer-science",
    "polymer chemistry", "thermoplastic_poly",
]
TIER3 = [  # 智能/刺激响应 + 水凝胶 + 可穿戴（与变色油墨、智能胶黏剂相关）
    "smart_polymer", "smart_fabric", "smart_textiles", "intelligent_textile",
    "hydrogel", "flexible", "stretchable", "us_patents", "thermoelectric",
]
# 其余（液晶类、色谱、超分子等）= Tier4


def tier_of(name):
    low = name.lower()
    if any(k in low for k in TIER1):
        return 1
    if any(k in low for k in TIER2):
        return 2
    if any(k in low for k in TIER3):
        return 3
    return 4


def body_len(relp):
    """Readable body length: strip front matter, count non-empty chars."""
    p = os.path.join(VAULT, relp.replace("/", os.sep))
    if not os.path.exists(p):
        return -1
    t = open(p, encoding="utf-8", errors="ignore").read()
    if t.startswith("---"):
        i = t.find("\n---", 3)
        if i > 0:
            t = t[i + 4:]
    t = re.sub(r"^\s*#.*$", "", t, flags=re.M)
    return len(t.strip())


rows = []
for b in m["books"]:
    root = b["root_file_rel"]
    rl = body_len(root) if root else -1
    chs = b["chapter_source_paths"]
    chlen = [body_len(c) for c in chs] if chs else []
    tot = sum(x for x in chlen if x > 0)
    rows.append({
        "name": b["name"], "tier": tier_of(b["name"]),
        "n": b["n_chapters"], "root_len": rl, "ch_bytes": tot,
        "has_root": bool(root), "chs": chs, "chlen": chlen,
    })

rows.sort(key=lambda r: (r["tier"], -r["ch_bytes"], r["name"].lower()))

print("P1 分级（Tier1=纤维/聚烯烃主轴  Tier2=高分子基础  Tier3=智能响应  Tier4=液晶等）")
print("=" * 92)
cur = None
for r in rows:
    if r["tier"] != cur:
        cur = r["tier"]
        sub = [x for x in rows if x["tier"] == cur]
        print(f"\n### Tier {cur}  —  {len(sub)} 本  /  正文 {sum(x['ch_bytes'] for x in sub):,} 字符")
        print("-" * 88)
    flag = ""
    if r["root_len"] == 0:
        flag = "  ⚠root空"
    elif r["root_len"] < 0:
        flag = "  (无root)"
    elif r["root_len"] < 1500:
        flag = f"  ⚠root仅{r['root_len']}字符"
    print(f"  {r['name'][:56]:<56} {r['n']:>3}ch  正文 {r['ch_bytes']:>8,}{flag}")

print("\n" + "=" * 92)
print("Tier1 明细（建议首批执行）")
print("=" * 92)
for r in rows:
    if r["tier"] != 1:
        continue
    print(f"\n  {r['name']}")
    if r["root_file_rel"] if "root_file_rel" in r else False:
        pass
    if r["has_root"]:
        print(f"     root: {r['root_len']:,} 字符")
    for c, L in zip(r["chs"], r["chlen"]):
        print(f"     {L:>8,}  {os.path.basename(c)[:62]}")
