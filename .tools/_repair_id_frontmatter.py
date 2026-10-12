"""Repair AGENTS.md §2.0 mandatory front matter on the 13 Industrial Drying
chapter pages compiled 2026-09-29.

Missing fields per verify_wiki.py: date_published, date_processed,
credibility, knowledge_update_status, key_claims, pages_linked.

key_claims are transcribed from each page's own verbatim quotes / H2-H3
structure (see .tools/_id_digest.py) -- no fabricated claims.
"""
import glob
import os
import re

DATE_PUBLISHED = "2014"
DATE_PROCESSED = "2026-09-29"
CREDIBILITY = "高"
STATUS = "done"

# key_claims transcribed from each page's own content (verified quotes)
KEY_CLAIMS = {
    "Industrial Drying Ch1 Principles and Classification": [
        "Drying = two coupled subprocesses: external heat supply to evaporate surface water + internal moisture transport to the surface; internal transport is rate-limiting at low final moisture (p.1)",
        "Over 85% of industrial dryers are convective (hot air / direct combustion gas) and over 99% of applications remove water (p.3)",
        "Bound vs unbound moisture dichotomy sets the residual-moisture floor -- maps to fluff pulp (hygroscopic) vs SAP (colloidal)",
        "Characteristic drying curve: constant-rate period (surface evaporation controlled) -> critical moisture content -> falling-rate period (internal diffusion controlled)",
        "Dryer selection is multi-criteria; 'a wrong dryer for a given application is still a poor dryer, regardless of how well it is designed'",
    ],
    "Industrial Drying Ch15 Impingement Drying": [
        "Impinging jets are recommended ONLY if a major fraction of the moisture to be removed is unbound; if drying is internal-diffusion controlled, jets add nothing",
        "Evaporative cooling in the constant-rate period holds product surface well below its degradation temperature -- a genuine safety lever for thermolabile webs",
        "Extremely high drying rates at high jet velocity can cause case hardening or cracking; very high shear can railroading-ink/coatings (streaks)",
        "Through-air / jet benchmarks cited at ~3100 kJ/kg with jet velocities up to 100 m/s and air temperatures to 350 degC",
    ],
    "Industrial Drying Ch17 Conveyor Dryers": [
        "Conveyor (through-air) dryers suit bulky, permeable, porous products -- the mechanism for TAD / through-air tissue and absorbent web lines",
        "Bed uniformity is the core design rule: 'if the feeding or spreading is not right, the dryer will not be able to dry the product uniformly'",
        "Volumetric heat-transfer coefficient h_v (kW/m3 degC) with volume V is the practical design formulation, not per-area h",
        "Evaporative cooling keeps product far below air temperature; chilling below ambient is required when a coating must be set below its glass-transition temperature",
    ],
    "Industrial Drying Ch28 Osmotic Dehydration and SAP Physics": [
        "Osmotic pressure rises as solute molar mass falls; electrolyte ion effects govern the water activity driving force (Pi = RT ln a_w)",
        "Plasmalemma is a 7.5-10 nm protein-lipid layer, water-permeable and selectively permeable -- the direct structural analogue of a superabsorbent polymer gel network",
        "Microbial proliferation ceilings: most bacteria P > 12.7 MPa, yeasts P > 17.3 MPa, moulds P > 30.1 MPa",
        "Osmotic dehydration removes water WITHOUT a phase change, so it avoids the latent-heat penalty of thermal drying",
        "0.5 h of osmotic dehydration gave a sixfold decrease in water-binding forces at the apple surface",
    ],
    "Industrial Drying Ch33 Drying of Fibrous Materials": [
        "Wood fibre water is held by cell-wall bonding; the differential heat of sorption for most woods is about half the heat of vaporization, falling to about one quarter at complete dryness",
        "Loose fibres do NOT constitute a simple capillary-porous body -- constant-rate behaviour needs a different mechanism than neat porous media",
        "Single-fibre diffusion is fast (wool ~1e-11 m2/s); macroscopic drying is controlled by the bed, not the fibre",
        "Press drying bonds fibres when held 25 to 50 degC above the lignin glass-transition temperature",
        "Critical moisture content X_cr and superheated-steam inversion temperature govern whether a fibre bed shrinks or case-hardens",
    ],
    "Industrial Drying Ch34 Drying of Textile Products": [
        "'Textile' explicitly includes nonwoven fabrics, knits, and terry products -- the chapter covers the whole web family",
        "Mechanical dewatering is far cheaper than thermal drying, so as much water as possible is removed mechanically first",
        "Heat-set structures are predried to about 30% moisture regain, transported, then final-dried",
        "Hydrophilic fibres (cotton) can be dewatered from about 150% regain down to 60-100%; hydrophobic fibres behave very differently",
        "Through-air drying wins as permeability rises; IR is predry-only with scorch risk and is NOT used for final drying",
    ],
    "Industrial Drying Ch35 Drying of Pulp and Paper": [
        "THE lower-moisture bound is critical: overheating below it causes thermal cross-linking (hornification) that makes reconstitution of the original fibre impossible",
        "A paper-machine dryer section has up to 70 cast-iron/steel cylinders and is conduction-limited, not convection-limited",
        "Pocket ventilation can raise drying efficiency by up to 20% depending on prior conditions",
        "Press, impulse and Condebelt drying combine mechanical + thermal + interactive effects -- thermomechanical web consolidation",
        "Drying strategy sets the final strength-bulk balance; pulp drying energy is quoted in the thousands of kJ/kg range",
    ],
    "Industrial Drying Ch40 Drying of Coated Webs": [
        "The drying curve controls coating morphology: water-based latex has a LONGER constant-rate period than solvent-based coatings; paper dries fastest and shortest",
        "Over-drying or too-rapid drying causes brittleness, blistering, curl and wrinkles, and reduces brightness, ink receptivity and varnishability",
        "High-velocity impingement dries the coating surface and accelerates binder migration -> railroading",
        "UV-curable coatings are 100% solids and need no solvent-removal equipment; cure/cross-linking generally improves adhesion and durability",
    ],
    "Industrial Drying Ch41 Drying of Polymers": [
        "Most polymers leave the reactor carrying unreacted monomer, solvents, water and/or other volatiles that must be removed",
        "ABS needs BOTH surface and bound moisture removal, so a two-stage drying system is recommended",
        "PET, nylon, ABS and PC are hygroscopic resins that collect moisture INSIDE the pellet -- drying by air is insufficient alone",
        "Devolatilization must be done above the glass transition temperature for effective bound-moisture removal -- directly relevant to SAP / SAP-composite processing",
    ],
    "Industrial Drying Ch46 Energy Aspects": [
        "Industrial dryers consume a significant share of manufacturing energy, 12% on average",
        "Thermodynamic minimum for evaporating 1 kg of water at standard conditions is 2200 to 2700 kJ/kg; typical practical values run far above that",
        "Cheap retrofits (plug leaks, insulation, air control) save 13-50%; heat recovery can reach 64-71%",
        "Typical heat-pump SMER is about 3 kg/kWh, favourable against conventional convective drying",
    ],
    "Industrial Drying Ch48 Safety Aspects": [
        "Drying is a potentially hazardous operation: roughly 8-9% of food-industry dust explosions are related to drying",
        "Fire/explosion needs three simultaneous conditions: fuel, oxidizer, ignition source",
        "Most incidents involve spark ignition energies BELOW 25 mJ; the very high resistance of synthetic-fibre bag filters is a major static-discharge hazard",
        "Safety is far more economical when built in at the design stage than added later",
    ],
    "Industrial Drying Ch50 Solid-Liquid Separation": [
        "Solid-liquid separation and drying are complementary operations, and the dry-cake cost must be balanced against the dryer's thermal requirement",
        "Energy gap is the central economic rule: mechanical dewatering ~58 kJ/kg vs convective thermal drying ~7000 kJ/kg",
        "Ruth filtration equation: for most industrial slurries n lies between 0.1 and 0.8",
        "Decreased particle size lowers filtration rate and raises cake moisture content, though it can improve washing efficiency",
    ],
    "Industrial Drying Ch53 Cost Estimation": [
        "A dryer is only one component of the whole drying system, which may include preprocessing, conveyors, dust collection, controls and utilities",
        "Capacity scaling: if n is not given, n = 0.6 can be taken for rough estimation",
        "Total direct installation cost is roughly 2.25x the equipment FOB cost",
        "304 stainless construction costs 1.5-1.7x carbon steel, and 2-3x more if built of other alloys",
    ],
}

BOOK_LINK = "[[Handbook of Industrial Drying]]"


def pages_linked(body):
    """Extract [[...]] targets from the Related Sources section, add book index."""
    links = []
    m = re.search(r"##\s*\d*\.?\s*Related Sources[\s\S]*", body)
    scope = m.group(0) if m else body
    for x in re.findall(r"\[\[([^\]|#]+)", scope):
        x = x.strip()
        if x and x not in links:
            links.append(x)
    if "Handbook of Industrial Drying" not in links:
        links.insert(0, "Handbook of Industrial Drying")
    return links


def inline(lst):
    return "[" + ", ".join('"' + x + '"' for x in lst) + "]"


def block(lst):
    return "key_claims:\n" + "\n".join("  - " + json_q(x) for x in lst)


def json_q(s):
    return '"' + s.replace('"', "'") + '"'


def repair(path):
    name = os.path.basename(path).rsplit(".md", 1)[0]
    if name not in KEY_CLAIMS:
        return None
    t = open(path, encoding="utf-8").read()
    i = t.index("---", 3)  # closing fence of front matter
    fm, body = t[:i], t[i:]

    # dedupe: drop any already-present mandatory fields
    for key in (
        "date_published",
        "date_processed",
        "credibility",
        "knowledge_update_status",
        "key_claims",
        "pages_linked",
    ):
        fm = re.sub(r"^" + key + r":[\s\S]*?(?=\n[A-Za-z_]+:|\Z)", "", fm, flags=re.M)
        fm = fm.rstrip("\n") + "\n"

    add = []
    add.append("date_published: " + DATE_PUBLISHED)
    add.append("date_processed: " + DATE_PROCESSED)
    add.append("credibility: " + CREDIBILITY)
    add.append("knowledge_update_status: " + STATUS)
    add.append(block(KEY_CLAIMS[name]))
    add.append("pages_linked: " + inline(pages_linked(body)))
    fm = fm.rstrip("\n") + "\n" + "\n".join(add) + "\n"

    out = fm + body
    if out == t:
        return "unchanged"
    open(path, "w", encoding="utf-8", newline="\n").write(out)
    return "fixed"


n = 0
for f in sorted(glob.glob("WIKI/sources/Industrial Drying Ch*.md")):
    name = os.path.basename(f).rsplit(".md", 1)[0]
    if name not in KEY_CLAIMS:
        continue
    print(repair(f), name)
    n += 1
print("processed:", n)
