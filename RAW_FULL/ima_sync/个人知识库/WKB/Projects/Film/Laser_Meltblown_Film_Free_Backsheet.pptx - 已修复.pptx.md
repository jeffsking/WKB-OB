---
media_id: "ppt_3867e2b60070d7dc3f413086d0b0036e_bcc1744f06c3499b5619b32ce9efa9b5001a693ee6c0644e"
source_file: "Laser_Meltblown_Film_Free_Backsheet.pptx - 已修复.pptx.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Projects/Film/Laser_Meltblown_Film_Free_Backsheet.pptx - 已修复.pptx.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# Laser_Meltblown_Film_Free_Backsheet.pptx - 已修复.pptx.md

8
MB

# Laser-Assisted Meltblown

## Can an all-PP SMMMMS structure replace the breathable backsheet film?

A physics-based feasibility study: die-tip thermal decoupling, polymer ageing, fibre attenuation limits, and formation-limited liquid barrier

1-D attenuation ODE

Cross rheology + scission kinetics

Extreme-value barrier model

EXECUTIVE VERDICT

2

# Three findings decide this

## 1

### The laser does not make finer fibres

Fibre diameter in the industrial window is drag-limited: it is set by throughput per hole and jet velocity, not by melt viscosity. Raising tip temperature 250 → 300 °C changes the simulated diameter by < 1 %. The stated premise — better melt flow at the nozzle giving finer fibres — does not hold.

## 2

## But the anti-ageing case is real and large

Capillary residence time is 4–20 ms against 480 s for the rest of the melt path. Heating only the tip lets the bulk run at 245 °C instead of 285 °C: simulated MFR drift falls from 1.67× to 1.08×, and the hot tip itself contributes 0.004 %. That headroom is what lets you run a 450 MFR resin at 130 holes/inch.

## 3

## The film-free backsheet works — outside the crotch

SMMMS at 30 gsm reaches 141 mbar hydrohead clean and 121 mbar against synthetic urine, against 88 mbar of sitting pressure from a 9 kg infant. It collapses to 55 mbar against runny stool and 14 mbar against barrier cream. Film holds > 1000 mbar regardless. Zone the backsheet; do not swap it wholesale.

LANDSCAPE

3

# Where meltblown technology actually stands

## $\blacksquare$ Capillary density is the live battleground

Production dies have moved from 35 hpi to 70–100 hpi, with multi-row cassette designs offered as a swap-in on composite lines. Sub-micron claims almost always come from low throughput per hole, not from a new attenuation mechanism.

## Die-tip air uniformity, not air volume

Recent die-tip patents target uniform high-velocity air around the tip and faster changeover rather than higher air rates. Fibre CV, not mean diameter, is what limits barrier performance.

## Laser drawing is real — but off-line

CO₂ laser supersonic drawing reliably makes 250–600 nm PP, PET, PA66 and PPS fibres at draw ratios above 10$^{5}$. It works on an already-spun filament in a vacuum chamber. It is a nanofibre lab route, not a web-forming process.

## $\blacksquare$ Barrier nonwovens are displacing film at the edges

SMS support layers specified above 150 mm H₂O already appear in breathable backsheet assemblies, and modular meltblown beams are being retrofitted between spunbond beams to add barrier to existing lines.

MODEL ARCHITECTURE

4

# What was simulated, and what it is anchored on

## A

### Melt rheology

Cross model with Arrhenius shift, $E_a = 42$ kJ/mol. Zero-shear viscosity from MFR: 1200 MFR → 55 Pa·s at 230 °C; 450 MFR → 136 Pa·s.

## B

### Capillary flow

Generalised Hagen–Poiseuille with a $6\tau_v$ Bagley entrance term. Gives die pressure, wall shear rate and residence time per hole.

### C

### Fibre attenuation

1-D filament ODE: dF/dz = $\dot{m}$ dv/dz - Λ f_drag, Matsui skin friction, Kase-Matsuo cooling, twin-slot jet decay. Solved by shooting on die-exit tension.

### D

### Chain scission

Random scission, $1/M_n$ linear in time, MFR $\propto M_v^{-3.4}$. $E_a = 120$ kJ/mol, anchored so a 480 s path at 285 °C gives $1.67 \times$ MFR rise.

### E

### Liquid barrier

Formation-limited: breakthrough at the weakest local patch, not the mean pore. Gumbel minimum over $10^4$ patches per 100 cm$^{2}$, beam-to-beam averaging as 1/Vn.

## Three calibrations you should challenge

$$ \Lambda = 6 $$

Whipping amplification — fibre arc length per unit axial length. Without it a 1-D model under-attenuates by 4-5x. Set so 0.5 g/hole/min at 250 m/s gives 3.1 µm.

$$A = 24.5$$

Barrier constant, mbar-μm/gsm. Set so a 10 gsm / 2.4 μm single-beam meltblown gives 45 mbar, matching published SMS data.

$$ CV = 15\% $$

Local basis-weight CV of one meltblown beam at 1 mm $^{2}$ scale. This single number drives the entire multi-beam barrier argument.

FINDING 1 · ATTENUATION

5

# Fibre diameter is set by throughput, not by temperature

[图片: <table><tr><td>4</td><td>60</td><td>200</td><td></td></tr></table>]
## The three curves lie on top of each other

Once the filament reaches velocity-matching with the air jet, mass conservation fixes the diameter: $d \propto v(m / \Lambda v_a)$. Melt viscosity changes only how fast matching is reached — 2.4 mm from the tip at 285 °C, 2.7 mm at 250 °C.

## So how do you get to 1.5 µm?

● Cut g/hole/min

0.73 → 0.20 at fixed line output means 35 → 130 hpi

● Raise jet velocity

150 → 250 m/s buys 2.85 → 2.21 µm, then saturates

● Nothing else moves it

tip temperature, MFR and hole diameter do not

FINDING 2 · THE PRESSURE WALL

5

# The real constraint is die pressure, and it arrives fast

[图片: die pressure (bar) <table><tr><td>80</td><td></td><td>160</td><td>200</td><td></td></tr></table>]
## Read the middle curve first

A 450 MFR resin at conventional tip temperature crosses the die-tip pressure limit at about 160 hpi. That is the wall. The two conventional escapes both cost you something:

## Noise MFR to 1200

pressure drops, but $M_v$ falls, melt strength falls, breaks and shot rise, formation CV worsens — and barrier is formation-limited

## Noise bulk melt to 300 °C+

pressure drops, but thermal dose rises steeply (slide 8) and you degrade the resin you just paid for

## Heat only the tip

same pressure relief, 4-20 ms of exposure instead of 480 s

CONCEPT

7

# What a laser die tip is, and what it is not

[图片: hot air 290 °C both sides polymer distribution beam — 245 °C die tip nose — 300 °C diode array 976 nm DLC absorbing coating on the last 3 mm of the nose Residence time along the melt path extruder 180 s pump + screen 60 s distribution beam 240 s capillary 0.006 s ratio 1 : 80,000]
## It is a heat-delivery method, not new physics

The enthalpy to lift 192 kg/h of melt by 55 K is 13.3 kW whatever the heater. Cartridges, induction and a diode array all pay the same bill.

## Its edge is watt density and dynamics

You cannot fit a cartridge in the last 3 mm of a 60° nose. A diode array can put 4 kW/m there, and re-zone it in milliseconds for CD profile trim.

## Do not point it at the polymer

PP is transparent at 976 nm and you cannot get a beam down a 0.13 mm capillary. The beam heats an absorbing coating on the nose; the melt is heated by conduction over the last 2 mm.

## Recommended build is hybrid

Resistive or induction for the base tip load, laser only for the nose apex and ±10 K CD trim zones. That is roughly 2 kW of laser, not 13 kW.

FINDING 3 · POLYMER AGEING

8

# Thermal dose: the whole argument in one chart

[图片: <table><tr><td>2.4</td><td>]
1.67×

conventional bulk 285 °C

1.08×

laser tip
bulk 245 °C

0.004 %

of total drift from the 320 °C tip

## Why the tip is almost free

Degradation is a dose: rate × time. The capillary raises the rate by 8× at 320 °C but shortens the exposure by 80,000×. The product is negligible.

## What the saved thermal budget is worth

● Spend it on molecular weight

Run 450 MFR instead of 1200 MFR at the same die pressure. Higher $M_v$ means higher melt strength, fewer filament breaks, less shot and fly.

Spend it on antioxidant load

A 40 K cooler melt path lets you cut the phenolic/phosphate package roughly in half — fewer extractables and less yellowing on a skin-contact article.

Spend it on recycle content

Post-industrial edge trim tolerates one more heat history before it falls out of the barrier specification.

BARRIER PHYSICS

9

# Nonwoven barrier is formation-limited, not pore-limited

## An ideal-pore model over-predicts by 15×

Laplace on the median pore of a 1.5 µm web gives roughly 800 mbar. Real webs deliver 40–140. The gap is not pore size — it is that liquid finds the thinnest patch on the sheet and breaks through there.

$$ P \propto \text{weakest local gsm} \times \gamma |\cos \theta| \div \text{fibre diameter} $$

The weakest local basis weight is the lowest over the 100 cm $^{2}$ test area — a Gumbel minimum over 10$^{4}$ patches, about 3.74 standard deviations below the mean — not the sheet average.

## This is why splitting the meltblown matters

Independent beams average their formation noise as 1/Vn. One beam at 15 % CV retains 44 % of its weight at the weakest patch. Four beams retain 72 %. Same polymer, same grams, 64 % more barrier.

[图片: <table><tr><td>200</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>180</td><td></td><td></td><td></td><td>171</td><td>176</td></tr><tr><td>160</td><td></td><td>155</td><td></td><td></td><td></td></tr><tr><td>140</td><td>138</td><td></td><td></td><td></td><td></td></tr><tr><td>120</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>100</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>80</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>60</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>40</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>20</td><td>td>2 beams</td><td>3 beams</td><td>4 beams</td><td>5 beams</td><td>6 beams</td></tr></table>]
FINDING 4 · STRUCTURE COMPARISON

10

# SMMMS clears the bar. SMMSMMS adds 8 gsm and no barrier.

[图片: <table><tr><td></td]
## The inner S earns nothing

Barrier is carried entirely by meltblown grams and beam count. SMMSMMS has the same four beams and the same 12 gsm, so it lands on exactly the same number — for 8 more gsm and 27% more cost.

Choose it only where the web is mechanically activated — ring-rolled ears, pant side panels — where the inner sunbond anchors the meltblown against delamination.

## Breathability is not the issue

$$ \text{WVTR} = 18,000 \text{ vs } 3,000 \text{ g/m}^2/\text{day for film} $$

Air permeability

r permeability 52 L/m $^{2}$·s vs effectively zero

onsequence

conective drying, not just diffusive — the genuine consumer win

FINDING 5 · WHERE IT FAILS

# The kill chart: surface tension against in-use load

[图片: <table><tr><td>250</td><td>235</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>200</td><td>201</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>150</td><td>151</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>100</td><td>92</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>50</td><td>48</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>0</td><td>water</td><td>urine</td><td>urine +</td><td>runny</td><td>48</td><td>24</td></tr><tr><td>72 mN/m</td><td>66</td><td>sebum 58</td><td>stool 48</td><td>stool 48</td><td>residue 40</td><td>barrier cream 33</td></tr></table>]
## Where the curve crosses the load

Against clean urine the structure has a 2.3× margin on a sitting infant. Against runny stool the margin is gone. Against a barrier-cream-contaminated interface it is 3.7× under water.

A microporous film holds above 1000 mbar in every one of these columns, because its barrier is a solid wall, not a capillary.

## How contamination reaches the backsheet

Cream is applied to skin, so the core stands between it and the barrier — that helps. What does not help: bile salts in loose stool tracking around the core edge, and wipe-lotion carryover at the leg cuff, which is exactly where the seal matters most.

RECOMMENDATION

12

# Zone the backsheet — do not swap it wholesale

[图片: <table><tr><td>back</td><td colspan="3">SMMMS film-free</td></tr><tr><td>crotch</td><td>film strip</td><td></td><td></td></tr><tr><td>front</td><td colspan="3">SMMMS film-free</td></tr></table>]
Roughly 62 % of backsheet area goes film-free

## Chassis outside the core footprint

Go film-free now. No free liquid ever reaches it, breathability is a pure win, and the softness and drape gain is what the consumer actually notices.

## Pant side panels and ears

SMMSMMS here. The inner spunbond survives ring-rolling and mechanical activation; barrier demand is near zero.

## Crotch, core footprint

Keep the film for now. This is where free liquid, contamination and peak sitting pressure coincide.Revisit only if the contamination data on slide 11 comes back better than modelled.

## Leg cuff

Already meltblown-barrier today. Upgrade to the 1.2 µm grade — the same beams that serve the chassis — rather than treating it as a separate material.

DESIGN · MATERIAL

13

# Meltblown polymer composition

|Component|Specification|Level|Rationale|
|---|---|---|---|
|Base resin|Metallocene PP homopolymer, reactor-grade|450 g/10 min|Not peroxide-visbroken. Narrow PDI $2.2-2.6$ gives uniform attenuation; no peroxide residue to seed further session at the hot tip.|
|Callback resin|Same family, higher flow|900 g/10 min|Drops die pressure 22%. Use only if the laser tip is not yet commissioned — it costs melt strength and formation CV.|
|Hydrophobic additive|PFAS-free alkyl-modified polylefin masterbatch|2.0 wt %|Advancing water contact angle $105^\circ \rightarrow 118-122^\circ$. Worth about 35 % on hydrohead. No C6 fluorochemistry — assume it is going away.|
|Primary antioxidant|Hindered phenolic (Irganox 1010 type)|350 ppm|Halved from a conventional 700-800 ppm load because the melt path runs 40 K cooler. Fewer extractables on a skin-adjacent article.|
|Secondary antioxidant|Phosphite (Irgafos 168 type)|500 ppm|Protests during the short high-temperature excursion in the capillary. Phosphite is the right chemistry for a spike, phenolic for the long soak|
|Acid scavenger|Hydrotalcite (DHT-4A type)|250 ppm|Replaces calcium stearate. Ca-stearate is the single largest source of die drool and plate-out on a hot tip — unacceptable at $300^\circ$C|
|Nucleating agent|None in the meltblown beams|—|Nucleation raises crystallisation temperature and freezes the filament earlier, shortening the attenuation window. Nucleate the spunbond beams only.|
|Slip / antistat|None|—|Migratory amides destroy the hydrophobic surface you just paid for and contaminate the die tip.|

450 MFR

chosen over 1200

Melt strength, not flow, is what buys barrier — it lowers formation CV, and hydrohead scales on the weakest patch.

2.0 wt %

Moves the advancing contact angle from 105° to 118–122°, worth roughly 35 % on hydrohead for 3.5 EUR-c per kg of meltblown.

- 50 %

antioxidant load

Only affordable because the laser tip lets the bulk melt path run 40 K cooler. Fewer extractables next to skin.

DESIGN · HARDWARE

14

# Die tip design

[图片: coat-hanger manifold 60° included nose angle L/D = 15, land 1.95 mm capillary $\approx$ 0.13 mm air gap 0.65 mm / side positive setback 0.50 mm Section through one capillary]
Laser zones: 32 independently driven CD segments of 100 mm, 976 nm diode bars, absorbing DLC coating on the last 3 mm of the nose. Base tip load carried by induction; laser trims ±10 K.

|Parameter|Value|Basis|
|---|---|---|
|Capillary density|130 hpi|production point — 1.94 µm at 60 kg/h·m|
|Strength density|160 hpi|1.75 µm, 55 bar with the laser tip|
|Callback density|100 hpi|2.21 µm, safe on any existing beam|
|Capillary diameter|0.130 mm|hole $\alpha$ tracks density to hold land ratio|
|L/D ratio|15|$6 \times \tau_v$ entrance loss included in 51 bar|
|Throughput per hole|0.195 g/min|the variable that actually sets diameter|
|Wall shear rate|20,400 $s^{-1}$|inside the shear-thining plateau|
|Capillary residence|5.9 ms|why the hot tip costs almost no degradation|
|Tip temperature|300-320 °C|decoupled from a 245 °C distribution beam|
|Primary air|250 m/s at 290 °C|above 300 m/s the diameter gain saturates|
|Die-to-collector|180-220 mm|long enough to lay down without shot|

DESIGN · STRUCTURE

15

# SMMMS web architecture, 30 gsm

|S1 spunbond 9 gsm|1.8 dpf, 35 MFR mPP + nucleator|
|---|---|
|M1 meltblown 3.0 gsm|1.5 µm, 450 MFR mPP|
|M2 meltblown 3.0 gsm|1.5 µm|
|M3 meltblown 3.0 gsm|1.5 µm|
|M4 meltblown 3.0 gsm|1.5 µm|
|S2 spunbond 9 gsm|1.8 dpf, body side|

Calendar bond 16% area, 0.35 mm$^{2}$ dots, 148 / 150 °C

Low bond area is deliberate: every bond point is a stiff, non-porous island that contributes nothing to barrier and everything to harshness. 16% is the floor that still survives converting tension.

|Property|Target|Status|
|---|---|---|
|Hydrohead, clean|≥ 130 mbar|141 modelled|
|Hydrohead, synthetic urine|≥ 110 mbar|121 modelled|
|Air permeability|40-65 L/m²·s|52 modelled|
|WVTR|≥ 12,000 g/m²·d|≥ 18,000|
|Basis weight|30 ± 1.5 gsm|—|
|MD tensile|≥ 32 N / 50 mm|spunbond-carried|
|CD elongation|≥ 55%|spunbond-carried|
|Formation CV per beam|≤ 15 % at 1 mm²|gates everything above|
|Handle-o-meter|≤0.9 × film laminate|softness claim|
|Opacity|≥88%|no $TiO_{2}$ needed — melblown scatters|

COMMERCIAL REALITY

16

# Cost, sustainability and what it does to the line

[图片: <table><tr><td>12</td><td>11.02</td></tr><tr><td>10</td><td>8.26</td></tr><tr><td>8</td><td>6</td></tr><tr><td>4</td><td></td></tr><tr><td>2</td><td></td></tr><tr><td>0</td><td></td></tr><tr><td>0</td><td>Film laminate14 gsm film + 12 gsm SB</td></tr><tr><td>SMMMMS30 gsm</td><td>SMMMMS38 gsm</td></tr></table>]
SMMMS lands within 5 % of the incumbent — not cheaper, not a blocker.

The film route carries 1.8 EUR-cents of lamination adhesive that the all-nonwoven route does not. Strip that out and the gap closes to under 1 %.

## Mono-material PP

A PP-only backsheet removes the PE/PP split that blocks mechanical recycling of the chassis. This is the strategic prize, and it is worth more than the 0.4 cents.

## Two extra meltblown beams

Capital and floor space. On a new composite line it is a configuration choice; on an existing SMS line it is a rebuild. Modular beam inserts between spunbond beams are the realistic retrofit.

## Line speed exposure

Meltblown is the slowest beam on any composite line. Four beams at 3 gsm each means the meltblown section, not the spunbond, sets the ceiling. Model the line balance before the material.

## Odour is the unpriced risk

52 L/m $^{2}$-s of air permeability lets ammonia out as freely as it lets vapour out. No model predicts consumer response to this — it needs a panel, early.

ROADMAP

17

# Staged programme with explicit kill criteria

[图片: S1]
## Bench

0-3 mo

● Pilot 4-beam laydown at 3 gsm/beam,1.5 µm

· Measure formation CV at 1 mm$^{2}$ — the model's weakest input

· Hydrohead vs surface tension curve, 33-72 mN/m

[图片: S2]
## Die tip

3-9 mo

· Single-zone laser nose on a 400 mm lab die, 130 hpi

· Melt-path GPC and MFR before/after at 245 vs 285 °C

● Die drool and plate-out over 200 h at 320 °Ctip

[图片: S3]
## Product

9-18 mo

● Zoned backsheet on converting trial,film strip in crotch lane

● Contamination panel: BM, wipe residue, barrier cream

● Odour panel — run this before anything else in S3

[图片: S4]
## Scale

18-30 mo

● CD-zoned laser array, 32 segments over 3.2 m

● Line balance study — meltblown as the speed-limiting beam

· Mono-material recycling claim substantiation

KILL if formation CV > 20 % per beam, or if hydrohead at 66 mN/m is below 90 mbar

KILL if measured MFR drift reduction is under 30 %, or if drool forces cleaning more than weekly

KILL if the odour panel is negative against the film control. Nothing downstream recovers from that

GO/NO-GO on cost parity at full line speed, not at pilot speed

HONEST LIMITS

18

# What would change this answer

## $\blacksquare$ The whipping factor A is a fitted constant

Everything on slide 5 rests on $\Lambda = 6$. If your line's real arc-length ratio is 4 or 9, the absolute diameters move by $\pm 20\%$. The conclusion that temperature does not change diameter is robust to $\Lambda$ — the absolute numbers are not.

## $\blacksquare$ Formation CV is assumed, not measured

15 % per beam at 1 mm $^{2}$ drives the entire multi-beam barrier argument. Measure it on your own beams first. If it is 10 %, single-beam SMS looks far better than shown and the four-beam case weakens.

## $\blacksquare$ Contamination transport was not modelled

Slide 11 shows what hydrohead does at low surface tension. It does not model whether bile salts or lotion actually reach the backsheet in a real diaper. That is an experiment, not a calculation, and it decides the crotch zone.

## Fibre diameter distribution was collapsed to a mean

Real meltblown has a log-normal spread with CV around 0.5, and the coarse tail is where shot and large pores live. A mean-diameter model flatters barrier performance.

## $\blacksquare$ Laser coupling efficiency is a guess

55 % absorption into a coated nose is plausible but unvalidated. At 35 % the hybrid heating case still holds; at 20 % the laser stops being worth its capital against induction.

## $\blacksquare$ No creep or wet-collapse model

Under sustained sitting load a meltblown web compacts, solidity rises and pores shrink — which helps barrier — but bond points also concentrate stress. Neither effect is in these numbers.

