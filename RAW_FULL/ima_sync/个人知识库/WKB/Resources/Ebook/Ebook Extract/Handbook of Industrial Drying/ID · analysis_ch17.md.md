---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_d1d524a725792b81c7b46ca7f41c175d001a693ee6c0644e"
source_file: "ID · analysis_ch17.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch17.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# ID · analysis_ch17.md.md

# Chapter 17 — Conveyor Dryers

## 1. Chapter Overview (范围、对象与定位)

Chapter 17 (Dan Poirier) is the handbook's treatment of the conveyor (through-circulation) dryer — a continuous unit in which product is carried on a perforated belt or mesh bed while hot process air is forced through the bed of product (p.409). The chapter's argument: although "conceptually very simple… a conveyor in a box with hot air" (p.409), it is "one of the most versatile dryers available" (p.409) precisely because forcing air through a permeable bed gives high, uniform heat/mass transfer. The logic flows from configuration choice (single-pass, single-pass/multiple-stage, multiple-pass — §17.2) → components (bed, enclosure, fans, heat source, feeder/spreader, accessories — §17.3) → selection & sizing via heat/mass balance and the volumetric heat-transfer coefficient (§17.4) → operation/control (air temperature, retention/bed depth, airflow, humidity — §17.5) → heat recovery (§17.6), sanitation (§17.7), economics (§17.8). For the hygiene reader this is a ★★★★★ chapter: the through-circulation conveyor is exactly the unit operation of through-air (TAD) bonding of airlaid nonwovens and thermobonding of bicomponent-fibre webs, and the chapter explicitly lists "super absorbent polymers" among products dried on single-pass/single-stage conveyors (p.411). It also names the glass transition temperature as the set/quench point for a coating (p.410) — the thermal-bonding window for PP/PET binder fibres.

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

Print-page span: p.409–p.420 (PDF p.430–441).

## 2. Key Viewpoints (核心观点 + 原文逐句引证)

V2.1 — Through-circulation conveyor forces air through a permeable bed; impermeable sheets are excluded.
> "Product is carried through the dryer on conveyors and hot air is forced through the bed of product… In general, the conveyor dryer is best suited for drying particulate material in the 1- to 50-mm diameter range. Drying in the conveyor dryer involves forcing air through the bed of product; therefore impermeable sheeted materials or slurries are not well suited to conveyor drying." (p.409–410)
Interpretation: The defining mechanism is air forced through a permeable bed. That is through-air drying/bonding. The chapter's one exclusion — impermeable sheeted materials — is the boundary that distinguishes conveyor/through-air from impingement (Ch.15) and Yankee (Ch.14-family). A porous airlaid or thermobond web is precisely the "permeable bed" this dryer was built for.

V2.2 — Super absorbent polymers are an explicitly named product.
> "Some examples of products that are often dried on single pass/single-stage dryers include expanded, non-coated snacks, baked snacks… nuts, charcoal, some synthetic rubbers, super absorbent polymers, etc." (p.411)
Interpretation: SAP powder is named verbatim as a conveyor-dried product — direct, unmistakable hygiene relevance, independent of any inference.

V2.3 — Glass transition temperature is the coating set/quench point.
> "If cooling to a temperature below ambient is required (for example to set a coating by getting it below its glass transition temperature), chilled air is used as the cooling medium." (p.410)
Interpretation: The chapter invokes Tg operationally as the quench window that fixes a coating. For nonwoven thermobonding this is the exact mechanism by which a low-Tg bicomponent sheath is cooled below Tg to lock fibre bonds — see POP trailer.

V2.4 — Uniform bed loading is the quality variable; clumps stay wet, shallow zones over-dry.
> "If the feeding or spreading is not right, the dryer will not be able to dry the product uniformly. The end result will be poor product quality, wasted energy, and reduced capacity… air will flow preferentially through the shallow areas… Therefore these shallow areas will be over dried… clumps… air will tend to flow around clumps rather than through them. This results in wet product inside the clumps." (p.415)
Interpretation: Cross-bed moisture uniformity is set at the feeder. For a nonwoven through-air oven this predicts exactly the streaks/shading defects the brief lists as web defects.

V2.5 — Volumetric heat-transfer coefficient is the sizing handle.
> "Since the product in a conveyor dryer is stacked, it is very difficult to determine the amount of product surface area exposed to the drying air… it is much easier to define the heat transfer in the form Q = h_v · V · ΔT where h_v is the volumetric heat transfer coefficient (kW/m³·°C) and V is the volume of the product bed (m³)." (p.416)
Interpretation: The engineering trick is to bypass the unknowable surface area and size from bed volume + h_v measured on a lab tray/belt sim — directly liftable to a nonwoven through-air line.

V2.6 — Evaporative cooling pins product below air temperature until near bone-dry.
> "the product in the dryer is typically at a much lower temperature than the air temperature due to evaporative cooling. If, however, the product is dried to a very low moisture content, near or approaching bone dry, the evaporation rate is reduced and the product may approach the air temperature." (p.418)
Interpretation: Same safety lever as Ch.15 — the latent sink protects heat-sensitive web until bound moisture is gone; past that, surface temperature climbs toward air temperature and the degradation/casehardening window opens.

## 3. Research Method & Data Sources

The chapter is a design-engineering practice manual (Poirier is a conveyor-dryer equipment author). Method:
- Configuration taxonomy (§17.2): single-pass/single-stage, single-pass/multiple-stage (deemed "most versatile", p.411), multiple-pass ("most popular", p.412).
- Sizing via heat & mass balance (§17.4): product, evaporated water, exhaust air, losses — Table 17.2 worked four-zone example.
- Volumetric h_v from lab sim (§17.4, p.416): static tray dryer simulates the continuous line; h_v then scales to other temperatures.
- Empirical databases (§17.4): "The most common way to size a conveyor dryer is to base the sizing on previous experience" (p.417); "theoretical modeling will never replace testing or previous experience" (p.415).
No new hygiene data; value is the balance procedure, Table 17.1 retention-time ranges, and the h_v method.

## 4. Argumentation Process

- Premise A: Forcing air through a permeable bed ⇒ high, uniform transfer; only permeable, non-clumping products fit (p.409–410).
- Premise B: Nonuniform bed loading breaks uniformity (over-dry shallow / wet clumps), so feeder/spreader is "one of the most critical components" (p.415).
- Step: Pick configuration by product; size bed volume from h_v and a heat balance; zone air temperature/flow; run first bed shallow, deepen after surface sets (p.420).
- Resolution: Control by air T (primary), retention/bed depth, humidity; recover >10 % energy via preheated make-up air (p.419); sanitary design for food; economics dominated by fuel + lost production, not capital (p.421).
The argument is candid that many effects (permeability vs depth, casehardening, clumping) are "very difficult to predict with a theoretical model" (p.416) — appropriate scope honesty.
## 5. Role in the Book

Ch.17 is the continuous permeable-bed convective dryer — the natural home of through-air (TAD) technology. It complements Ch.15 (impingement — air onto a sheet) and Ch.14-family Yankee (conductive), and it is the production-scale cousin of Ch.16's flash (dilute powder). Within the hygiene frame it is the bonding-oven chapter: airlaid through-air bonding and thermobond-oven lines are conveyor dryers forced-air-through-web, even when the handbook does not name nonwovens explicitly.

## 6. Strengths & Weaknesses

Strengths
- Names "super absorbent polymers" as a dried product (p.411) and "synthetic rubbers" repeatedly — direct polymer/hygiene relevance.
- Gives the full heat-balance procedure with a worked four-zone example (Table 17.2, p.417) and retention-time ranges (Table 17.1, p.417).
- Explicitly catalogs web-quality mechanisms: nonuniform loading → over-dry/wet-clump (p.415), casehardening at low humidity (p.419), and the evaporative-cooling safety lever (p.418).
- Concrete energy anchors: losses 10 % (p.419).

Weaknesses / contestable
- No nonwoven named. The chapter lists food/petfood/rubber/charcoal/SAP but never "nonwoven", "airlaid", or "through-air dryer"; the hygiene link is by mechanism, not by example. [inference]
- Permeability blind spot. "the permeability of a bed of product will often not change linearly with increasing bed depth… suddenly drop as the particles compress… and begin to blind over the bed" (p.416) — exactly what a consolidating wet-laid/airlaid web does, but the chapter gives no model for it.
- h_v is product-specific. The volumetric coefficient must be measured per product (p.416); no cross-material correlation supplied.

## 7. Key Terms / Concepts

- Conveyor / through-circulation dryer: hot air forced through a permeable product bed on a perforated/mesh belt (p.409).
- Single-pass/multiple-stage: deemed most versatile; allows bed-depth increase as product dries (p.411).
- Multiple-pass: most popular; stacked beds, smallest footprint, but hard to zone (p.412).
- Bedplate / mesh: perforated sheet (100–300 mm plates) or mesh; round holes vs slots; % open area critical; plugging kills uniformity (p.413).
- Volumetric heat-transfer coefficient h_v: kW/m³·°C; sizing handle from bed volume (p.416).
- Glass transition temperature (Tg): coating set/quench point via chilled air (p.410).
- Casehardening: can appear at too-low humidity (p.419).
- Optimal bed depth: first bed shallow, deepen after surface sets (p.420).
## 8. Micro close-reading (微观精读)

8.1 — The mechanism sentence (p.409–410). "hot air is forced through the bed of product… the conveyor dryer is best suited for drying particulate material in the 1- to 50-mm diameter range… impermeable sheeted materials or slurries are not well suited to conveyor drying." This is the load-bearing definition. "Forced through the bed" = through-air. The 1–50 mm particulate range is the food/rubber framing, but an airlaid nonwoven web is a permeable bed of fibres/bicomponent binder in exactly this size class; the only exclusion (impermeable sheet) is what pushes tissue to Yankee/impingement instead.

8.2 — SAP named (p.411). "some synthetic rubbers, super absorbent polymers, etc." One clause, huge relevance: SAP powder is a conveyor-dried product in industry. A hygiene engineer sizing an SAP post-polymerization dryer can lift Table 17.1 logic directly (though SAP retention time is not tabulated — gap).

8.3 — Tg quench (p.410). "to set a coating by getting it below its glass transition temperature" — the chapter states the polymer-physics quench rule without naming the polymer. For a thermobond oven this is the sheath-cool-below-Tg bond-lock step; see POP trailer.

8.4 — Uniformity mechanism (p.415). "air will flow preferentially through the shallow areas… over dried… clumps… air will tend to flow around clumps rather than through them. This results in wet product inside the clumps." The root cause of cross-web moisture shading in a through-air oven: feeder/spreader nonuniformity → preferential airflow → over-dry thin + wet clump. Fix is at the spreader, not the air temperature.

8.5 — Energy split (Table 17.2, p.417). Of 1831 kW total, evaporated water = 1263 kW (~69 %), exhaust air = 383 kW (~21 %), product = 145 kW (~8 %), losses = 40 kW (~2 %). Evaporative duty dominates; exhaust recovery is the lever (p.419, >10 %).

💡 Standout line: "super absorbent polymers" (p.411) — the single phrase that converts this from "a food/petfood dryer chapter" into a directly hygiene-relevant one.

## 9. Concept deep-dive (概念深掘)

9.1 Heat & mass balance (§17.4, Table 17.2). Four terms:
Q_Product = m_Product · C_pProduct · ΔT_Product  (p.418)
Q_Evaporation = m_Evaporation · (h_Vapor − h_Water)  (p.418; example uses h_Water = 105 kJ/kg, h_Vapor = 2650 kJ/kg → 1263 kW)
Q_Air = m_Air · C_pAir · ΔT_Air  (p.418–419; example 383 kW)
Losses < 7 % of total heat load (p.418). These four terms are the energy-cost/tonne backbone for a through-air bonding line.

9.2 Volumetric h_v method (p.416). Q = h_v · V · ΔT, h_v in kW/m³·°C. Measured on a lab static tray that simulates zoned air T/time; then scaled. For a nonwoven web, h_v is set by permeability (open area, fibre packing) — the chapter's "plugging/blinding" warning (p.416) is the web-consolidation risk.

9.3 Bed-depth progression (p.420). First bed shallow (contains light product, avoids clumping/deformation); deepen after surface is partially dry. Direct recipe for an airlaid mat: pre-dry surface, then compress/deepen to raise throughput.

9.4 Humidity control (p.419). Too high → lost capacity + corrosion; too low → excess energy + casehardening. Zone-exhaust dampers / VSD exhaust fan tie humidity to quality and energy simultaneously.

## 10. Academic critique & open questions

- Mechanism named, application not. Through-air bonding of nonwovens is never named, though it is the literal unit operation (p.409). The hygiene reader must map "permeable bed" → airlaid/thermobond web themselves.
- No permeability-vs-depth model. The chapter admits permeability "will often not change linearly with increasing bed depth… suddenly drop… blind over the bed" (p.416) but offers no predictive tool — the central difficulty for consolidating wet webs.
- SAP data gap. SAP is listed (p.411) but absent from Table 17.1 retention times; a hygiene engineer gets no SAP-specific T / airflow / retention anchor.
- Open question: How does h_v scale when the "bed" is a fibre web whose porosity collapses during bonding (sheath melt → pore closure)? The chapter's constant-h_v assumption (p.416) breaks exactly at the thermobond point.
- Open question: The Tg quench (p.410) is stated for "a coating" — is the same chilled-air-below-Tg rule the correct set step for a bicomponent sheath? PoP says yes (trailer).
## 11. Hygiene-material relevance & action cards

Relevance rating: ★★★★★ (strongest in this batch for airlaid/thermobond nonwovens and SAP).

H11.1 — Run the through-air oven as a conveyor forced-through-bed dryer (★★★★★). Action: Treat airlaid through-air bonding and thermobond ovens as Ch.17 conveyors: hot air through the permeable web (p.409); exclude impermeable sheets (p.410). Size from bed volume + h_v (p.416).

H11.2 — Spread uniformly or accept shading (★★★★★). Action: Engineer feeder/spreader to even web basis weight; nonuniform loading → preferential airflow → over-dry thin zones + wet clumps (p.415). This is the root cause of cross-web moisture streaks in nonwoven bonding.

H11.3 — Use the Tg quench to lock bonds (★★★★★). Action: After the bond zone, cool the web below the binder-fibre Tg (p.410, "set a coating by getting it below its glass transition temperature") with chilled air to freeze sheath bonds; see POP trailer for PP/PET Tg windows.

H11.4 — Progress bed depth: shallow first, deepen after surface set (★★★★). Action: Run first zone shallow to contain the light/web and avoid clumping; deepen after surface is partially dry (p.420) to maximize throughput without deformation.

H11.5 — Cost energy from the four-term balance (★★★★★). Action: Use Table 17.2 splits (evaporated water ~69 %, exhaust ~21 %, product ~8 %, losses 10 % heat-recovery lever (p.419) as the energy-cost/tonne baseline for a through-air bonding line.

H11.6 — Avoid casehardening via humidity floor (★★★★). Action: Keep zone humidity off the floor — too-low humidity causes casehardening (p.419); too-high loses capacity/corrodes. Tie exhaust dampers to humidity sensors (p.419).

H11.7 — Size an SAP dryer from conveyor logic (★★★). Action: SAP powder is a named conveyor product (p.411); apply the h_v + heat-balance method (§17.4) to size an SAP post-reaction dryer, measuring h_v on a lab tray first (p.416).

## 12. Book-map quotes (本书脉络引证)

- Ch.15 (p.383): impingement — air onto a sheet; Ch.17 is air through a permeable bed; the two are the convective pair.
- Ch.16 (p.395): flash — dilute powder, second-scale; Ch.17 is the continuous permeable-bed counterpart for larger/longer residence (5–240 min, p.410).
- Ch.19 (p.437): superheated steam — could be the "process air" forced through the bed here.
- Ch.41 (p.951): Drying of Polymers — the chapter that generalizes SAP/synthetic-rubber polymer drying named in Ch.17.

