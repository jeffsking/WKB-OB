8
R&D DESIGN + SIMULATION STUDY — UPDATE

#   Three-Way SAP Design Comparison

Zoned NR-610S/NR-950 blend · Zoned KC511/NR-950 blend · Mono KC511 (uniform)

385×110mm sandglass core · 6-month infant, 3 sequential urine insults · equal 15g total SAP add-on across all three designs

DESIGN SET

#   Same liner, same total mass — poly-side blend is the variable

#   Design A

Zoned · NR-610S / NR-950 blend

SAP1: KC 511 (liner)

Poly: 40% NR-610S + 60% NR-950

15.0g total add-on

#   Design C

Zoned · KC 511 / NR-950 blend (NEW)

SAP1: KC 511 (liner)

Poly: 40% KC 511 + 60% NR-950

15.0g total add-on

#   Design B

Mono KC 511 · uniform by area

Liner: KC 511

Poly: 100% KC 511

15.0g total add-on

Zoning: Designs A and C use the same insult-targeted zoning across the 385mm length (see prior deck). Design B spreads its 15g uniformly by area — no targeting. This isolates two questions at once: does zoning beat uniform spreading, and does swapping the blend's fast component (NR-610S $\rightarrow$ KC 511) change the outcome?

ADD-ON DETAIL

#   Per-zone add-on across the 385mm length

|Zone|A: SAP1|A: NR-610S|A: NR-950|C: SAP1|C: KC511|C: NR-950|B: liner|B: poly|
|---|---|---|---|---|---|---|---|---|
|Front|0.53|0.23|0.35|0.53|0.23|0.35|1.20|2.23|
|Front-Mid|1.84|0.87|1.31|1.84|0.87|1.31|1.00|1.86|
|Crotch|2.10|1.56|2.34|2.10|1.56|2.34|0.88|1.64|
|Back-Mid|0.63|0.94|1.40|0.63|0.94|1.40|1.00|1.86|
|Back|0.16|0.30|0.45|0.16|0.30|0.45|1.16|2.16|


All grams; A and C share the identical SAP1/liner allocation and zoning pattern — only the poly-side fast component changes (NR-610S $\rightarrow$ KC 511). B (mono) is spread by zone area, not by insult targeting.

SIMULATION RESULT

#   Zone saturation after insult 3 — all three designs

% of zone capacity used, after insult 3

![140\n\n120\n\n100\n\n80\n\n60\n\n40\n\n20\n\n0\n\nFront\n\n47\n\n43\n\n48\n\n45\n\n46\n\n53\n\n52\n\n64\n\n53\n\n67\n\n68\n\n69\n\n60\n\n40\n\n20\n\n0\n\n19\n\nDesign A (NR-610S/NR-950) Design C (KC511/NR-950) Design B (Mono KC511)\n\nDesign A (NR-610S/NR-950) Design C (KC511/NR-950) Design B (Mono KC511)\n\n47\n\n43\n\n44\n\n45\n\n46\n\n47\n\n48\n\n49\n\n100\n\n80\n\n60\n\n61\n\n129\n\n129\n\n76\n\n64\n\n68\n\n69\n\n67\n\n68\n\n67\n\n19\n\nBack\n\nDesign A (NR-610S/NR-950) Design C (KC511/NR-950) Design B (Mono KC511)\n\n47\n\n45\n\n46\n\n47\n\n48\n\n49\n\nDesign C leads\n\nDesign C's worst zone (Back) peaks at 67% — lower than Design A's 76%. Design B (mono) still overflows the Crotch zone at 129%. Why: KC511 beats NR-610S on both AUL (18.4 vs 12.1 g/g) and GBP (24 vs 6), so swapping it into the blend raises capacity margin everywhere.\n\nCaveat: this capacity-budget model doesn't score acquisition speed — NR-610S's faster vortex (19s vs KC511's 29s) is a real edge this chart can't see.
](1/parseimages/figuref225fc8ec3b4410cb545423bd32f31e9_0_3.png)
#   Design C leads

Design C's worst zone (Back) peaks at 67% — lower than Design A's 76%.

Design B (mono) still overflows the Crotch zone at 129%.

Why: KC511 beats NR-610S on both AUL (18.4 vs 12.1 g/g) and GBP (24 vs 6), so swapping it into the blend raises capacity margin everywhere.

Caveat: this capacity-budget model doesn't score acquisition speed — NR-610S's faster vortex (19s vs KC511's 29s) is a real edge this chart can't see.

TRADE-OFFS

#   Capacity, permeability, and speed pull in different directions

||Design A|Design C|Design B (mono)|
|---|---|---|---|
|Poly blend|40% NR-610S + 60% NR-950|40% KC511 + 60% NR-950|100% KC511|
|Peak zone saturation|76% (Back)|67% (Back)|129% (Crotch, overflow)|
|Blend AUL (0.7psi, g/g)|16.5|19.0|18.4|
|Blend GBP|7.2|14.4|24 (best-in-set)|
|Fast-component vortex|19s (fastest available)|29s|29s|
|SKUs to qualify|2 (KC511, NR-610S, NR-950)|2 (KC511, NR-950)|1 (KC511 only)|


Read: on this model, Design C dominates Design A on every capacity and permeability metric — dropping NR-610S for KC511 in the poly blend simplifies sourcing to 2 grades and improves both saturation margin and GBP. The one thing it gives up is initial acquisition speed (KC511's 29s vortex vs NR-610S's 19s), which this saturation-based model doesn't capture. If bench cGAM-LTD testing shows that speed gap matters in practice (surface wetness, strike-through), Design A remains the faster-acquisition option; if not, Design C is the stronger default.

NEXT STEPS

#   Resolving the speed-vs-capacity question

1

Bench cGAM-LTD acquisition timing on Design A vs Design C prototypes — this is the one variable the capacity model can't resolve.

2

If Design C's acquisition time stays within spec, prefer it: better capacity margin, better permeability, one fewer SKU to qualify.

3

Re-confirm blended AUL/GBP for KC511+NR-950 as mixed (not linearly averaged) — same caveat as the original NR-610S/NR-950 blend.

4

Carry Design B (mono KC511) forward only as a cost fallback — its crotch-zone overflow (129%) is a leak-risk signal at this insult schedule regardless of blend choice.

5

Re-run all three designs at 4-5 insults/wear (overnight case) before finalizing gsm.
