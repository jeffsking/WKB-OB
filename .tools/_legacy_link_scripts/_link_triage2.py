"""Improved link triage: catch EN/ZH alias pairs + substring matches.

Outputs .tools/_link_fix_plan.json with:
  redirect : {target -> real page name}
  seed     : {target -> [citing pages]}
  review   : {target -> [candidates]}
"""
import glob
import os
import re
import json
from collections import defaultdict

VAULT = "E:/WKB-OB"
WIKI = os.path.join(VAULT, "WIKI")

ZH = re.compile(r"[\u4e00-\u9fff]+")
EN = re.compile(r"[A-Za-z][A-Za-z0-9\-'&\.]{2,}")


def norm(s):
    s = re.sub(r"[（(][^）)]*[）)]", "", s)
    s = re.sub(r"[\s_\-–—×x·、，,。.:：;；\"'“”‘’/]", "", s)
    return s.strip().lower()


STOP = {"the", "and", "for", "with", "from", "book", "review", "ch", "ed", "of", "in", "on", "a"}


def tokens(s):
    out = set()
    for z in ZH.findall(s):
        if len(z) >= 2:
            out.add(z)
            if len(z) >= 4:
                out |= {z[i:i + 3] for i in range(len(z) - 2)}
    for e in EN.findall(s):
        e = e.lower()
        if len(e) >= 4 and e not in STOP:
            out.add(e)
    return out


# ---- existing pages ----
pages = {}
alias_map = defaultdict(list)
for d in ("sources", "concepts", "entities", "comparisons"):
    for f in glob.glob(os.path.join(WIKI, d, "*.md")):
        b = os.path.basename(f)[:-3]
        pages[b] = d
        alias_map[norm(b)].append(b)
        t = open(f, encoding="utf-8", errors="ignore").read(3000)
        m = re.search(r"^aliases:\s*\[(.*?)\]", t, re.M)
        if m:
            for a in re.findall(r'"([^"]+)"', m.group(1)):
                alias_map[norm(a)].append(b)

page_tokens = {b: tokens(b) for b in pages}

# ---- missing targets ----
missing = defaultdict(list)
for d in ("sources", "concepts", "entities", "comparisons"):
    for f in glob.glob(os.path.join(WIKI, d, "*.md")):
        src = os.path.basename(f)[:-3]
        t = open(f, encoding="utf-8", errors="ignore").read()
        for l in set(re.findall(r"\[\[([^\]|#]+)", t)):
            l = l.strip()
            if l and l not in pages:
                missing[l].append(src)

# curated redirects: safe conceptual duplicates only (hand-checked)
CURATED = {
    "SAP": "SAP（高吸水树脂）",
    "导流层 ADL": "ADL（导流层）",
    "绒毛浆 Fluff Pulp": "绒毛浆（Fluff Pulp）",
    "面层 Topsheet": "Topsheet（面层）",
    "Handbook of Adhesive Technology": "Handbook of Adhesive Technology Full Report",
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
    "Handbook of Industrial Drying 全书摘要": "Handbook of Industrial Drying",
    "Handbook of Industrial Drying 核心观点汇总": "Handbook of Industrial Drying",
    "可穿戴电子 Wearable Electronics": "Wearable Electronics (National Science Review 2023)",
    "Wearable Electronics": "Wearable Electronics (National Science Review 2023)",
    "柔性电子 Wearable Electronics": "Wearable Electronics (National Science Review 2023)",
}
# never auto-redirect these (semantically distinct / would be factually wrong)
BLOCK = {"PNIPAAM", "Hot Melt Adhesive", "SAP Composites", "SAP 干燥 SAP Drying"}

redirect, seed, review = {}, {}, {}
for target, cited in missing.items():
    if target in BLOCK:
        seed[target] = cited
        continue
    if target in CURATED:
        if CURATED[target] in pages:
            redirect[target] = CURATED[target]
            continue
    n = norm(target)
    hit = alias_map.get(n)
    if hit and len(set(hit)) == 1:
        redirect[target] = hit[0]
        continue
    # token overlap scoring
    tk = tokens(target)
    best, score = None, 0.0
    if tk:
        for b, bt in page_tokens.items():
            if not bt:
                continue
            inter = len(tk & bt)
            if inter == 0:
                continue
            s = inter / max(len(tk), 1)
            if s > score:
                best, score = b, s
    if best and score >= 0.75 and best != target:
        redirect[target] = best
    elif best and score >= 0.4:
        review[target] = (best, round(score, 2))
    else:
        seed[target] = cited

print(f"现有页面 {len(pages)} | 缺失目标 {len(missing)} | 引用 {sum(len(v) for v in missing.values())}")
print(f"REDIRECT {len(redirect)} | REVIEW {len(review)} | SEED {len(seed)}")

json.dump({"redirect": redirect,
           "review": {k: v[0] for k, v in review.items()},
           "review_score": {k: v[1] for k, v in review.items()},
           "seed": seed},
          open(os.path.join(VAULT, ".tools", "_link_fix_plan.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=2)

print("\n--- REDIRECT ---")
for k, v in sorted(redirect.items(), key=lambda kv: -len(missing[kv[0]])):
    print(f"  {len(missing[k]):>3}x [[{k}]] -> [[{v}]]")
print("\n--- REVIEW (低置信度候选，将转为 seed) ---")
for k, v in sorted(review.items(), key=lambda kv: -len(missing[kv[0]]))[:15]:
    print(f"  {len(missing[k]):>3}x [[{k}]]  ~ [[{v[0]}]] ({v[1]})")
print(f"\n--- SEED {len(seed)} 种，引用 {sum(len(v) for v in seed.values())} 处 ---")
