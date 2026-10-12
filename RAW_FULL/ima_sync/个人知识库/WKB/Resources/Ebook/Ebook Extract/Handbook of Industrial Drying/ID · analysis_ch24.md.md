---
media_id: "markdown_3867e2b60070d7dc3f413086d0b0036e_4b8c41bc0b51cfc0ef08e7d1e3919f28001a693ee6c0644e"
source_file: "ID · analysis_ch24.md.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch24.md.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# ID · analysis_ch24.md.md

# Chapter 24 — Grain Property Values and Their Measurement

## 1. Chapter Overview (范围、对象与定位)

Chapter 24 (Jayas & Cenkowski) is the measurement-and-property handbook for grains and oilseeds: physical (bulk/particle density, porosity, shape, angles of repose, friction), hygroscopic (moisture measurement, equilibrium moisture content EMC, equilibrium relative humidity ERH, sorption/desorption, hysteresis, five isotherm equations), thermal (specific heat, conductivity/diffusivity, convective h, latent heat of vaporization, heat of respiration), electrical (dielectric, moisture meters), optical (NIR/reflectance), and aerodynamic (drag, terminal velocity) properties, closing with a full List of Symbols. For the hygiene-materials reader this is the single strongest method-transfer chapter of the batch (★★★★★): EMC, ERH (i.e. water activity a_w), sorption/desorption isotherms, hysteresis, and the thin-layer drying equation are precisely the tools used to set residual-moisture specs and predict warehouse moisture pickup for fluff pulp and SAP. The chapter never mentions hygiene products, but its hygroscopic section is substrate-agnostic — it applies to any hydrophilic porous solid. Sections 5 and 11 state plainly where the numbers (grain cultivars, ASAE standards) differ from pulp/SAP, but the methods transfer directly.

Page numbers derived from PDF-page − 21; offset anchored on Ch.1 = p.1 and should be spot-checked against the print edition.

Print-page span: p.573–p.598 (PDF p.594–619; references p.598+).

## 2. Key Viewpoints (核心观点 + 原文逐句引证)

V2.1 — EMC is defined by equilibrating a sample at fixed RH and temperature.
> "In the static method, a sample of known mass is allowed to reach equilibrium with air maintained at a constant relative humidity and temperature. The moisture content of the sample at equilibrium is measured and is defined as the EMC. The constant relative humidity environments are usually created using saturated salt solutions in containers." (p.579)
Interpretation: This is the operational definition of EMC — the residual moisture a material settles at for a given ambient RH/T. For pulp/SAP, the same saturated-salt method (Rockland, ref. [13]) gives the desorption isotherm that sets warehouse RH targets.

V2.2 — Sorption EMC < desorption EMC at the same RH (hysteresis).
> "The sorption EMC is lower than the desorption EMC at the same relative humidity because of the hysteresis phenomenon that is exhibited by biological materials." (p.580)
Interpretation: A hydrophilic material re-adsorbs water at a higher moisture than it desorbs to at the same RH. Critical for pulp/SAP: a bale dried to 8% will re-pick-up moisture faster on humid warehouse air than the desorption curve predicts — design the spec on the desorption branch.

V2.3 — Five isotherm equations; GAB is the preferred theoretical model.
> "The modified Henderson [15,16] and modified Chung–Pfost... equations have been adopted as standard equations by the American Society of Agricultural Engineers... The G.A.B. equation has recently been recognized as the most satisfactory theoretical isotherm equation, but it does not incorporate the effect of temperature on the EMC–ERH relationship." (p.580)
Interpretation: The GAB (Guggenheim–Anderson–deBoer) multilayer-sorption model is the workhorse for fitting a_w-vs-moisture data — the same model used to characterise moisture sorption of cellulose/SAP/hydrophilic biopolymers (see PoP crossref).

V2.4 — Thin-layer drying/wetting is an exponential approach to EMC.
> "The variation is that it is not necessary to bring the sample to equilibrium, and the EMC is determined as M_e by nonlinear regression of the equation: M = M_e + (M_i − M_e) exp(−K t^N) (24:5)" (p.580)
Interpretation: Equation 24.5 is THE thin-layer model: moisture approaches equilibrium exponentially with drying constant K (1/s) and shape coefficient N. This is the quantitative core for modelling fluff-pulp bale/roll conditioning and SAP particle drying kinetics (cf. Ch.23 thin-layer premise).

V2.5 — Wet vs dry basis must be stated explicitly.
> "In theories of grain drying, the moisture contents of samples are usually expressed on a dry mass basis (db)... it is suggested that the scientific community adopt a convention to report moisture contents on wet basis in percentage and moisture contents on dry basis in decimal fraction." (p.578)
Interpretation: A discipline rule the hygiene engineer must enforce: always declare wb% vs db decimal when specifying pulp/SAP residual moisture, or numbers become ambiguous.

V2.6 — Latent heat of vaporization rises as moisture falls (last points cost more).
> "To overcome the attractive forces between the adsorbed water molecules and the internal surfaces of grain kernels extra energy is needed... As the moisture content is lowered, there is an increase in the amount of energy required to evaporate the water molecules in seeds." (p.589)
Interpretation: Bound water is energetically harder to remove than free water — the physical reason the "last few moisture percentage points are especially difficult to remove" (Ch.23, p.563). Directly sets the energy cost of hitting a low pulp/SAP spec.

## 3. Research Method (研究方法)

This is a measurement-methods and property-data compilation [纯理论/综述章节，未使用实证方法]. Method:
- Standardised measurement protocols (ASAE standards) for each property class; e.g. bulk density via 500-mL container + funnel (p.574), porosity from bulk/particle density (Eq 24.1), EMC via static (saturated salts) or dynamic (recirculating air) method (p.579–580), specific heat via method of mixtures or DSC (p.582–584), thermal conductivity via guarded hot-plate / line-heat-source probe (p.585–587), dielectric via Q-meter (p.592–593).
- Isotherm fitting: nonlinear regression of EMC–ERH data to Henderson / Chung–Pfost / Halsey / Oswin / GAB (Table 24.8), constants tabulated (Table 24.9).
- Tabulated representative values (bulk density Table 24.1; porosity/particle density Table 24.2; thermal conductivity Table 24.12; diffusivity Table 24.13; latent-heat coefficients Table 24.14; terminal velocity Table 24.15).
- Full List of Symbols (p.598) — defines M, M_e, M_i, RH, T, K, N, etc.

Value: the method (how to measure EMC/ERH and fit isotherms) is directly reusable for fluff pulp / SAP; the grain numbers are not.

## 4. Argumentation (论证逻辑)

- Premise A: Engineering design of handling/storage/drying needs quantitative property values for individual seeds and bulk (p.573).
- Premise B: Hygroscopic properties (EMC/ERH, hysteresis) govern safe storage moisture and drying endpoint (p.579–580).
- Step: Measure EMC by static (saturated salts) or dynamic (recirculating air) method; fit to one of five isotherm equations; the GAB is preferred theoretically (p.580). Use EMC + thin-layer Eq 24.5 to model drying; use latent-heat Eq 24.32 to cost the last moisture points (p.589).
- Resolution: Report every property with full sample description (cultivar, moisture, pretreatment) because values are sample-dependent (p.584). The argument is rigorous and metrology-focused — appropriate for a "property values and measurement" chapter.
## 5. Role of This Chapter in the Book (在全书中的角色)

Ch.24 is the property-and-measurement backbone that makes every other drying chapter quantitative. It is the direct methodological home of the thin-layer premise introduced in Ch.23 (p.569) and the empirical basis for Chs. 25–27 (fruit/veg, herbal, roots). For hygiene it is the bridge from "dry it" to "spec it and predict warehouse pickup": EMC/ERH/isotherm/GAB are the exact toolkit for fluff-pulp and SAP moisture specification. It complements Ch.4 (property tables) and Ch.15 (web drying) with the measurable, modellable hygroscopic foundation.

## 6. Strengths and Weaknesses (贡献与局限)

Strengths
- Operational EMC/ERH definitions + two measurement methods (static/dynamic) — directly reusable (p.579–580).
- Five isotherm equations with constants; GAB flagged as best theoretical (p.580, Table 24.9).
- Thin-layer Eq 24.5 with defined K, N — the quantitative drying-kinetics entry point (p.580).
- Explicit wb/db discipline rule (p.578) and full symbol list (p.598).
- Latent-heat-of-vaporization-rises-with-drying Eq 24.32 + coefficients (p.589, Table 24.14) — energy-cost rationale.

Weaknesses
- All data are grain/oilseed cultivars under ASAE standards; no pulp/SAP/nonwoven numbers — transfer is by method, not value.
- Hysteresis modelled descriptively, not quantified with a dedicted hysteresis equation.
- OCR heavily garbles the isotherm equations in Table 24.8 (see §9) — re-verify against print before use.
- No explicit water-activity (a_w) terminology (uses ERH); the hygiene reader must equate a_w = ERH (decimal).

## 7. Key Terms (关键术语)

|||
|---|---|
|EMC (equilibrium moisture content)|moisture at equilibrium with fixed RH/T; measured by static (saturated salts) or dynamic method (p.579)|
|ERH (equilibrium relative humidity)|RH of air in equilibrium with sample; = water activity a_w (decimal) (p.579)|
|Sorption vs desorption|uptake vs loss branch; sorption EMC < desorption EMC (hysteresis) (p.580)|
|Hysteresis|sorption/desorption EMC differ at same RH (p.580)|
|Isotherm equations|Modified Henderson, Chung–Pfost, Halsey, Oswin, GAB (p.580)|
|GAB|"most satisfactory theoretical isotherm equation" (p.580)|
|Thin-layer model (Eq 24.5)|M = M_e + (M_i − M_e) exp(−Kt^N); K = drying const (1/s), N = coeff. (p.580)|
|wb / db|wet basis % vs dry basis decimal — must be declared (p.578)|
|Latent heat rise (Eq 24.32)|h*_fg = h_fg[1 + a·exp(−bM)]; bound water costs more (p.589)|
|Heat of respiration|metabolic heat in storage; microbial/spoilage risk (p.590)|

## 8. Micro close-reading (微观精读)

8.1 — EMC measurement (p.579). "a sample of known mass is allowed to reach equilibrium with air maintained at a constant relative humidity and temperature. The moisture content of the sample at equilibrium is measured and is defined as the EMC. The constant relative humidity environments are usually created using saturated salt solutions in containers." This sentence is the transferable protocol: to set a fluff-pulp warehouse RH target, measure the pulp desorption isotherm the same way — saturated salt solutions at 25 °C give known ERH points (Rockland [13], 5–40 °C), dry samples to each, weigh at equilibrium (1–5 weeks, p.580), fit GAB. The resulting curve is the spec.

8.2 — Hysteresis (p.580). "The sorption EMC is lower than the desorption EMC at the same relative humidity because of the hysteresis phenomenon that is exhibited by biological materials." For a pulp bale, this means: if you dry to 8% (desorption branch) and store at 60% RH, the bale will creep up toward the higher sorption-branch value if it re-wets — but more importantly, the desorption curve is the conservative one for setting the outgoing spec. Ignore hysteresis and you under-spec the warehouse RH.

8.3 — Thin-layer Eq 24.5 (p.580). "M = M_e + (M_i − M_e) exp(−K t^N) (24:5)." The exponential approach to equilibrium is the simplest defensible model for a thin pulp layer or SAP particle. K and N are fitted from a single drying curve; once known, predict residence time to hit M_e. This is the quantitative payoff of Ch.23's thin-layer premise.

8.4 — Latent-heat rise (p.589). "As the moisture content is lowered, there is an increase in the amount of energy required to evaporate the water molecules in seeds." Equation 24.32 h*_fg = h_fg[1 + a·exp(−bM)] (Table 24.14) quantifies why the last moisture points dominate energy cost — the same physics behind Ch.23's "last few moisture percentage points are especially difficult to remove."

## 9. Concept deep-dive (概念深掘)

9.1 EMC / ERH measurement (§24.3.2, p.579–580). Two methods. Static (EMC method): sample equilibrates in a sealed jar over a saturated salt solution at fixed T; final moisture = EMC; 1–5 weeks; mold risk at high RH (propionic acid inhibitor). Dynamic (ERH method): 0.5–1.0 kg sample recirculates air in a sealed unit at ±0.1 °C; when air RH stabilises, that RH = ERH and the (average) moisture = EMC; 6–12 h. Both deliver the same EMC–ERH pair; the dynamic method is faster. Academic origin: ASAE standards; the saturated-salt static method traces to Rockland [13].

9.2 Sorption isotherm equations (Table 24.8, p.580). Five models relate M (db), RH (decimal), T (°C):
- Modified Henderson: RH = 1 − exp(−(A(T+C) + B)·M) — [equation garbled in source; standard form RH = 1 − exp(−(A·T+C)·M^B)].
- Modified Chung–Pfost: RH = exp[−A·exp(−B(T+C))·M] — [transcription uncertain; standard M = −(1/B)·ln((−(T+C)·lnRH)/A)].
- Modified Halsey: [garbled; standard RH = exp(−A/(T·(M+B)^C))].
- Modified Oswin: RH = 1 / (1 + (A + B·T)/M^C) (transcribed from p.580 lines 465–471).
- GAB: M = (A·C·B·RH) / [(1 − B·RH)(1 − B·RH + C·B·RH)] (p.580 lines 473–476) — multilayer BET-type model; "most satisfactory theoretical isotherm equation"; Jayas–Mazza adds C/T temperature dependence (p.581). Constants in Table 24.9. Symbols: A, B, C constants; M % water db; RH decimal; T °C (definitions p.482, 598).
The GAB is the one to use for hygiene (multilayer water on cellulose/SAP — see PoP crossref).

9.3 Thin-layer drying equation (Eq 24.5, p.580). M(t) = M_e + (M_i − M_e)·exp(−K·t^N). Symbols (List of Symbols, p.598): M = moisture db; M_e = equilibrium moisture content; M_i = initial moisture content; K = drying constant (1/s); N = drying coefficient; t = time. The form is the Page-type exponential approach; K and N absorb temperature/air-velocity effects empirically. Directly usable for pulp-layer / SAP-particle kinetics once fitted.

9.4 Moisture basis (§24.3.1, p.578). wb = mass water / total mass (×100%); db = mass water / dry mass (decimal). The chapter urges always reporting both. Hygiene action: declare wb% vs db on every pulp/SAP spec.

9.5 Latent heat of vaporization vs moisture (Eq 24.32, p.589). h*_fg = h_fg·[1 + a·exp(−b·M)], M on db; coefficients a,b per crop in Table 24.14 (e.g. wheat hard a=1.7, b=217.6). Quantifies rising energy cost at low moisture.

## 10. Critique (批判性评估)

- Method, not data, transfers. All tabulated constants are grain/oilseed; using them for pulp/SAP would be erroneous — re-measure EMC/ERH for the actual material.
- OCR corruption of Table 24.8. The five isotherm equations are heavily garbled (concatenated symbols, swapped indices); I transcribed Oswin and GAB faithfully and flagged Henderson/Chung–Pfost/Halsey as uncertain. Re-verify against print before fitting.
- No a_w terminology. The chapter uses ERH; equate a_w = ERH (decimal) when bridging to hygiene/ food-science literature.
- Hysteresis not modelled. Stated qualitatively; no explicit hysteresis equation — the hygiene engineer must account for it separately (use desorption branch for outgoing spec).
- GAB ignores temperature in its base form; use Jayas–Mazza C/T correction (p.581) for T-dependent specs.
## 11. Hygiene-Material Relevance & Action Cards (卫材相关性与行动卡)

Relevance rating: ★★★★★ (very high — method transfer). This chapter supplies the exact toolkit (EMC/ERH/sorption isotherm/GAB/thin-layer Eq 24.5/wb-db discipline/latent-heat rise) for setting fluff-pulp and SAP residual-moisture specs and predicting warehouse moisture pickup. Substrate is grain, but the hygroscopic method is substrate-agnostic. No diaper "application" is invented for grain — the transfer is to pulp/SAP measurement and specification.

H11.1 — Measure pulp/SAP desorption isotherm by the static salt method (★★★★★). Action: Dry fluff-pulp and SAP samples over saturated salt solutions (known ERH) at 25 °C to equilibrium (1–5 weeks), weigh, fit the GAB model (p.580) → obtain the a_w-vs-moisture curve that sets warehouse RH and the outgoing residual-moisture spec.

H11.2 — Set spec on the desorption branch, respect hysteresis (★★★★★). Action: Because sorption EMC < desorption EMC at equal RH (p.580), dry to the desorption isotherm value and treat re-wetting on humid air as creeping toward the higher sorption branch — choose warehouse RH so even the sorption branch stays under the microbial/quality limit.

H11.3 — Model bale/roll/SAP drying with thin-layer Eq 24.5 (★★★★★). Action: Fit M = M_e + (M_i − M_e)·exp(−Kt^N) (p.580) from one drying curve to get K, N; then predict residence time / through-air exposure to reach target M_e for fluff bales and SAP particles.

H11.4 — Always declare wb% vs db (★★★★). Action: Enforce the chapter's convention (p.578): report residual moisture as wb% and db decimal on every pulp/SAP spec and QC certificate to remove ambiguity.

H11.5 — Cost the last moisture points via latent-heat rise (★★★★). Action: Use h*_fg = h_fg[1 + a·exp(−bM)] (p.589) logic to justify staged/lower-temperature finishing (cf. Ch.23 tempering): the final moisture fraction is energetically expensive, so remove it with low-energy air after a temper hold.

H11.6 — Equate ERH = a_w for cross-literature work (★★★★). Action: Map the chapter's ERH (decimal) directly to water activity a_w when reading SAP/pulp stability and microbial-growth literature; the monolayer/oxidation window concept (Ch.22, p.553) then plugs into the same isotherm.

## 12. Book-Map Quotes (本书脉络引证)

- Ch.23 (p.569): thin-layer premise ( m, no gradient) — Ch.24 quantifies it via Eq 24.5.
- Ch.22 (p.554): glass-transition / monolayer (a_w≈0.3) stability — pairs with Ch.24's isotherm as the Tg+a_w stability map.
- Ch.4 (p.81): property tables / internal diffusion — Ch.24 supplies the measurable hygroscopic properties behind them.
- Ch.25 (p.603): fruit/vegetable drying — applies Ch.24's EMC/isotherm method to another substrate.
