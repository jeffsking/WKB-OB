"""Fix all broken wikilinks.

Strategy (conservative):
  1. malformed `[[[X]]` -> `[[X]]`
  2. curated rename-only redirects (hand-checked; same entity, name variant)
  3. every remaining missing target -> seed page (cites sources + pending
     dimensions ONLY; NEVER fabricated content)

Usage:
  python .tools/_fix_links_all.py            # dry-run
  python .tools/_fix_links_all.py --apply
"""
import glob
import os
import re
import sys
import json
from collections import defaultdict

VAULT = "E:/WKB-OB"
WIKI = os.path.join(VAULT, "WIKI")
APPLY = "--apply" in sys.argv
TODAY = "2026-09-30"

# ---------- curated redirects: name-variant only, never semantic narrowing ----------
CURATED = {
    "SAP": "SAP（高吸水树脂）",
    "导流层 ADL": "ADL（导流层）",
    "绒毛浆 Fluff Pulp": "绒毛浆（Fluff Pulp）",
    "面层 Topsheet": "Topsheet（面层）",
    "凝胶阻塞 Gel Blocking": "Gel Blocking（凝胶阻塞）",
    "Kimberly-Clark": "Kimberly-Clark（金佰利）",
    "非菲克扩散 Non-Fickian Diffusion": "Non-Fickian Diffusion (Crank Ch.11)",
    "Stimuli-Responsive Polymer Materials": "Stimuli-Responsive Polymer Materials (Nature Materials Review)",
    "SNF": "SNF（法国）",
    "LG Chem": "LG Chem（LG 化学）",
    "热粘 Thermal bonding": "Thermal bonding",
    "机械加固 Mechanical bonding": "Mechanical bonding",
    "微胶囊 Microencapsulation": "Microencapsulation",
    "NWSP and ISO Test Methods Comparison 11-10-2022 updated":
        "NWSP and ISO Test Methods Comparison 11-10-2022 updated.docx",
    "Procter & Gamble": "The Procter & Gamble Company（宝洁）",
    "Handbook of Adhesive Technology": "Handbook of Adhesive Technology Full Report",
    "Handbook of Industrial Drying 全书摘要": "Handbook of Industrial Drying",
    "Handbook of Industrial Drying 核心观点汇总": "Handbook of Industrial Drying",
    "可穿戴电子 Wearable Electronics": "Wearable Electronics (National Science Review 2023)",
    "Wearable Electronics": "Wearable Electronics (National Science Review 2023)",
    "柔性电子 Wearable Electronics": "Wearable Electronics (National Science Review 2023)",
    "Modern Chemistry of Ancient Dyes and Pigments":
        "Modern Chemistry of the Ancient Chemical Processing of Organic Dyes and Pigments",
    "Handbook of Adhesion": "Book Review Handbook of Adhesion by Packham",
    "SAP Research Advances": "Research Advances in Superabsorbent Polymers (Polymers 2024)",
    "Stimuli-Responsive Photonic Coatings": "Stimuli-Responsive Photonic Polymer Coatings (ChemComm 2014)",
    "Surface Energy": "Surface Tension and Surface Energy",
    "Surface Tension": "Surface Tension and Surface Energy",
    "表面能 Surface Energy": "Surface Tension and Surface Energy",
    # SAP family -> existing concept page (verified exists)
    "SAP Superabsorbent Polymer": "SAP（高吸水树脂）",
    "Superabsorbent Polymer 高吸水树脂": "SAP（高吸水树脂）",
    "Synthetic Superabsorbent Polymers": "SAP（高吸水树脂）",
    "SAP Composites": "SAP（高吸水树脂）",
    # Adhesive Handbook parts: real page names differ
    "Adhesive Handbook Part 2 Adhesion Science": "Adhesive Handbook Part 2 Fundamental Aspects",
    "Adhesive Handbook Part 3 Polymer Chemistry": "Adhesive Handbook Part 3 Adhesive Classes",
    # thermochromic: existing Chinese concept page
    "热致变色 Thermochromic": "热致变色",
    "温致变色 Thermochromic": "热致变色",
}

# canonical seed page <- variant names that should point at it
GROUPS = {
    "Nonwoven 非织造布": ["非织造布 Nonwoven", "非织造材料 Nonwoven", "无纺布 Nonwoven"],
    "双组分纤维 Bicomponent": ["双组分纤维 Bicomponent Fiber"],
    "水刺 Hydroentanglement": ["水刺 Spunlace"],
    "热熔胶 Hot Melt Adhesive": ["热熔胶 Hot Melt"],
    "气铺 Airlaid": ["气流成网 Airlaid"],
    "交联密度 Crosslink Density": ["交联密度 Cross-link Density"],
    "光致变色 Photochromic": ["光致变色 Photochromism"],
    "WRV 水保留值": ["保水值 WRV"],
    "刺激响应聚合物 Stimuli-Responsive Polymer": ["刺激响应材料"],
}
# semantic narrowing -> keep as seed instead
BLOCK = {"PNIPAAM", "SAP 干燥 SAP Drying",
         "光致变色 Photochromic", "热致变色 Thermochromic", "非织造布 Nonwoven", "湿巾 Wet Wipes",
         "BASF", "毛细压力 Capillary Pressure", "热风无纺布", "无纺布 Nonwoven", "热熔胶 Hot Melt",
         "Henkel", "水凝胶 Hydrogel", "Sun Chemical", "SMS 复合无纺布", "壳聚糖 Chitosan",
         "吸收芯体", "回渗 Rewet", "智能织物 Smart Textile", "纺粘 Spunbond", "熔喷 Meltblown",
         "结构色 Structural Color", "变色油墨 Color-Changing Ink", "变色材料 Chromic Materials",
         "SBS 弹性体", "Stimuli-Responsive PCM"}
BLOCK -= {v for vs in GROUPS.values() for v in vs}      # group variants are handled

# ---------- existing pages ----------
pages = {}
for d in ("sources", "concepts", "entities", "comparisons"):
    for f in glob.glob(os.path.join(WIKI, d, "*.md")):
        pages[os.path.basename(f)[:-3]] = d

# ---------- scan ----------
missing = defaultdict(list)
malformed = defaultdict(list)
for d in ("sources", "concepts", "entities", "comparisons"):
    for f in glob.glob(os.path.join(WIKI, d, "*.md")):
        src = os.path.basename(f)[:-3]
        t = open(f, encoding="utf-8", errors="ignore").read()
        for l in set(re.findall(r"\[\[\[([^\]|#]+)", t)):
            malformed[l.strip()].append(src)
        for l in set(re.findall(r"\[\[([^\]|#\[]+)", t)):
            l = l.strip()
            if l and l not in pages:
                missing[l].append(src)

redirect = {}
for tgt in list(missing):
    if tgt in BLOCK:
        continue
    if tgt in CURATED and CURATED[tgt] in pages:
        redirect[tgt] = CURATED[tgt]

# group variants -> canonical seed page
group_cited = {}
for canon, variants in GROUPS.items():
    agg = list(missing.get(canon, []))
    for v in variants:
        if v in missing:
            redirect[v] = canon
            agg += missing[v]
    if agg:
        group_cited[canon] = agg

seed = {}
for k, v in missing.items():
    if k in redirect:
        continue
    seed[k] = v
for canon, cited in group_cited.items():
    seed[canon] = cited

print(f"现有页面 {len(pages)}")
print(f"malformed [[[ : {len(malformed)} 种")
print(f"REDIRECT : {len(redirect)} 种 ({sum(len(missing.get(k, [])) for k in redirect)} 处)")
print(f"SEED     : {len(seed)} 种 ({sum(len(v) for v in seed.values())} 处)")

if not APPLY:
    print("\n(dry-run; add --apply)")
    json.dump({"redirect": redirect, "seed": seed, "malformed": dict(malformed)},
              open(os.path.join(VAULT, ".tools", "_link_fix_plan.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    sys.exit(0)

# ================= apply =================
stats = {"malformed": 0, "redirect": 0, "seed_pages": []}

for d in ("sources", "concepts", "entities", "comparisons"):
    for f in glob.glob(os.path.join(WIKI, d, "*.md")):
        t0 = open(f, encoding="utf-8").read()
        t = t0
        for l in malformed:
            if f"[[[{l}]]]" in t:
                t = t.replace(f"[[[{l}]]]", f"[[{l}]]")
                stats["malformed"] += 1
        for old, new in redirect.items():
            if f"[[{old}]]" in t or f"[[{old}|" in t:
                t = t.replace(f"[[{old}]]", f"[[{new}]]").replace(f"[[{old}|", f"[[{new}|")
                stats["redirect"] += 1
        if t != t0:
            open(f, "w", encoding="utf-8", newline="\n").write(t)

# ---- seed pages ----
UNSAFE = str.maketrans({"/": "／", "\\": "＼", ":": "：", "*": "＊", "?": "？",
                        '"': "”", "<": "＜", ">": "＞", "|": "｜"})
ENTITY_HINT = ["公司", "集团", "inc", "ltd", "llc", "gmbh", "corp", "co.", "industries",
               "chemical", "chem", "solutions", "technologies", "materials", "group",
               "basf", "henkel", "basf", "arkema", "evonik", "dow", "lg chem", "snf",
               "glatfelter", "bostik", "sumitomo", "toray", "positive", "supplier", "vendor"]


def classify(name):
    low = name.lower()
    if any(h in low for h in ENTITY_HINT):
        return "entity"
    return "concept"


def safe_name(n):
    n = n.translate(UNSAFE)
    n = n.strip().rstrip(". ")
    return n[:120] if len(n) > 120 else n


for target, cited in seed.items():
    typ = classify(target)
    fn = safe_name(target)
    if not fn:
        continue
    d = "entities" if typ == "entity" else "concepts"
    path = os.path.join(WIKI, d, fn + ".md")
    if os.path.exists(path):
        continue
    uniq = sorted(set(cited))
    shown = uniq[:12]
    if typ == "entity":
        fm = (f'---\ntype: entity\ntitle: "{fn}"\ncategory: 待补\n'
              f'relationship: 待核\nupdated: {TODAY}\ntags: [seed, 待补]\n---\n')
        meta = "| Category 类别 | 待补 |\n| Relationship 关系 | 待核 |"
    else:
        fm = (f'---\ntype: concept\ntitle: "{fn}"\ndomain: [待补]\nstatus: seed\n'
              f'updated: {TODAY}\ntags: [seed, 待补]\n---\n')
        meta = "| Domain 领域 | 待补 |\n| Status 状态 | seed |"

    body = [fm, f"\n# {fn}\n",
            f"\n> ⏳ **Seed page（{TODAY}）**：本页为断链收尾时按引用反查补建的占位页 —— "
            f"{len(uniq)} 处引用指向本标题，但此前未创建页面。**仅登记引用来源与待补维度，未填任何数据**；"
            f"补充内容时须回到下列来源页核对原文，禁止编造。\n",
            f"\n## Metadata 元数据\n\n| Item 项目 | Content 内容 |\n|---|---|\n{meta}\n",
            f"\n## Cited by 主要引用来源（{len(uniq)} 处{'' if len(uniq) <= 12 else '，取前 12'}）\n"]
    for c in shown:
        body.append(f"- [[{c}]]\n")
    body.append("\n## Pending 待补维度\n\n")
    if typ == "entity":
        body.append("- 公司全称 / 国别 / 主营产品（回引用来源核对后补齐）\n"
                    "- 与金佰利的既有关系（供应商 / 竞品 / 合作方）\n"
                    "- 相关产品牌号、产能、认证口径\n")
    else:
        body.append("- 定义 / 口径 / 关键参数（回引用来源核对原文后补齐）\n"
                    "- 与卫材（REL 芯体 / SAP / 无纺布 / 胶黏）的关联点\n"
                    "- 定量数据与来源页码\n")
    body.append("\n## Related Sources 关联来源\n\n")
    for c in shown[:5]:
        body.append(f"- [[{c}]]\n")

    open(path, "w", encoding="utf-8", newline="\n").write("".join(body))
    stats["seed_pages"].append(f"{d}/{fn}.md")

print(f"\nmalformed 修复: {stats['malformed']} 处")
print(f"redirect  改写: {stats['redirect']} 处")
print(f"seed 页新建  : {len(stats['seed_pages'])} 个")
json.dump(stats, open(os.path.join(VAULT, ".tools", "_link_fix_result.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=2)
