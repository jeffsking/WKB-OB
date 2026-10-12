---
media_id: "ppt_3867e2b60070d7dc3f413086d0b0036e_a27ef180a0734b8e00a6c2004ed3ef9e001a693ee6c0644e"
source_file: "One_Drum_Two_Ups_11_Sizes_1000ppm.pptx.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Engineering/One_Drum_Two_Ups_11_Sizes_1000ppm.pptx.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# One_Drum_Two_Ups_11_Sizes_1000ppm.pptx.md

8
DEEP DIVE · 11 SIZES · 1,000 PPM

# One Drum, Two Ups

Skin-side and poly-side pattern-SAP printing for 6 open-diaper and 5 pants sizes, with registration held through every grade change

Ø882 mm

single drum body, both sides

6-up / 7-up

two sleeve families

1,000 ppm

396-462 m/min at the drum

≥ 99.99%

simulated in-spec registration

[图片]
3D model: 7-up M sleeves (358 mm fishbone), drum-to-drum nip, cut roll and servo repitch turret

# The size problem: a 140 mm spread in core length

From your Word file — 11 SAP-pattern sizes to run on one drum at a fixed 1,000 ppm

|Family|Size|MD × CD (mm)|
|---|---|---|
|Open diaper|NB|280 × 100|
|Open diaper|S|314 × 100|
|Open diaper|M|358 × 110|
|Open diaper|L|385 × 110|
|Open diaper|XL|420 × 110|
|Open diaper|XXL|420 × 110|
|Pants|L|355 × 110|
|Pants|XL|365 × 120|
|Pants|XXL|365 × 120|
|Pants|XXXL|365 × 120|
|Pants|XXXXL|420 × 120|

[图片]
280 → 420 mm

core length range: the longest is 1.5x the shortest

7 distinct lengths

355/358/365 and 420 cluster;
NB and S sit alone

3 widths

100, 110 and 120 mm –
handed in CD, not by ups

Why "ups" is the lever: with one drum diameter the only way to change drum pitch is the number of cores per revolution (P = πD / n). At fixed 1,000 ppm the drum then turns at 1,000/n rpm, and its surface speed equals the drum pitch in m/min. The chassis pitch is decoupled downstream by a repitch unit.

# Ups options simulated: one diameter, two ups

End zone = drum pitch – SAP pattern length (≥ 30 mm needed for end seal and cut); smaller means less core-wrap waste

## End zone per size (mm) — lower is better

[图片: 140 120 100 80 60 40 20 0 OpenNB Open S Open M Open L Open XL Open XXL Pant L Pant XL Pant XXL Pant XXXL Pant XXXXL $\blacksquare$ A - Ø882, 6/7-up $\blacksquare$ B - Ø889, 6/8-up $\blacksquare$ C - Ø1,014, 7/9-up]
## A · Ø882 mm, 6-up + 7-up

Mean 52 mm. 9 of 11 sizes ≤ 42 mm; only NB, S (and open L at 77) run long. Inside your 800–900 mm window

Recommended

## B·Ø889 mm, 6-up + 8-up

Mean 76 mm. Best for NB/S, but M and all pants waste 100-110 mm of core wrap every pad.

## C·Ø1,014 mm, 7-up + 9-up

Mean 69 mm, pants still ≥ 90 mm, and the drum is outside your window.

# Recommended: one Ø882 mm drum body, two sleeve families

Same drum, shell, sectors, motor and nip for all 11 sizes — only sleeves, recipe and two small change parts move

[图片]
# 6-up sleeve (shown: Open XL 420 mm)

[图片]
# 7-up sleeve (shown: Open M 358 mm)

|At 1,000 ppm|6-up|7-up|
|---|---|---|
|Drum pitch|461.8 mm|395.8 mm|
|Drum speed|166.7 rpm|142.9 rpm|
|Surface speed|462 m/min|396 m/min|
|Centrifugal field|13.7 g|10.1 g|
|Time per degree|1.00 ms|1.17 ms|
|Sizes|4|7|

# 6-up · Open L/XL/XXL, Pants XXXXL

[图片]
# 7-up · Open NB/S/M, Pants L-XXXL

[图片: $\blacksquare$]
Both drugs (skin and poly) always carry the same ups — the nip requires identical pitch and phase on each side.

# Size-by-size operating window at 1,000 ppm

Simulated per drum (skin side and poly side each); SAP at 160-230 gsm over the core footprint

|Size|Core mm|Ups|Drum pitch|End zone|Trim|Drum m/min|SAP g/pad/side|SAP kg/h/drum|Repitch ratio*|
|---|---|---|---|---|---|---|---|---|---|
|Open NB|280×100|7|395.8|116 mm|56 mm chip|396|4.5-6.4|269-386|0.99|
|Open S|314×100|7|395.8|82 mm|22 mm chip|396|5.0-7.2|301-433|1.07|
|Open M|358×110|7|395.8|38 mm|—|396|6.3-9.1|378-543|1.18|
|Open L|385×110|6|461.8|77 mm|—|462|6.8-9.7|407-584|1.07|
|Open XL|420×110|6|461.8|42 mm|—|462|7.4-10.6|444-638|1.15|
|Open XXL|420×110|6|461.8|42 mm|—|462|7.4-10.6|444-638|1.15|
|Pant L|355×110|7|395.8|41 mm|—|396|6.2-9.0|375-539|1.23|
|Pant XL|365×120|7|395.8|31 mm|—|396|7.0-10.1|420-604|1.25|
|Pant XXL|365×120|7|395.8|31 mm|—|396|7.0-10.1|420-604|1.25|
|Pant XXXL|365×120|7|395.8|31 mm|—|396|7.0-10.1|420-604|1.25|
|Pant XXXXL|420×120|6|461.8|42 mm|—|462|8.1-11.6|484-696|1.19|

# Decoupling drum pitch from product pitch

A servo repitch turret, not cut-and-slip — because NB needs the core slowed down

## Chassis pitch ÷ drum pitch (assumed chassis pitch)

[图片: <table><tr><td>1.3</td><td>]
## Cut-and-slip needs ratio ≥ ~1.03

It can only speed a core up. Open NB (0.99) would fail; open Land S sit at 1.07.

## Servo repitch turret: 0.85-1.40

Pucks on individual cam profiles take cores at 396 or 462 m/min and place at chassis pitch — one recipe per size.

## Chip trim only for NB (56 mm) and S (22 mm)

Double-knife cut roll with vacuum chip extraction; knife insert changed with those two sleeves only.

# Process architecture — 3D machine concept

Pattern set and bonded on the drugs; cut, trimmed and repitched below the nip

[图片: 1]
1. Servo rotary SAP valve + shaped chute phase-locked to pattern; width insert 100/110/120

2 Forming hood, high-vacuum sector65° = 65 ms (6-up) / 76 ms (7-up)

3. Air knife over blanked lands channels and end zones cleared

4. Fiberized HMA, segmented nozzle coated width follows core width

5 Skin/poly drum-to-drum nip raised lands bond channels in register

6 UV registration camera phase trim on poly-side drum only

7. Double-knife cut roll single cut; chip cut for NB and S

8. Servo repitch turret

drum pitch → chassis pitch, per recipe

# Forming drum — critical design criteria for two ups

Everything that defines phase is on the drum body; everything that defines size is on the sleeve

|Parameter|Specification|Why|
|---|---|---|
|Pitch diameter|882.0 mm at NW mid-plane (circ. 2,771 mm)|6-up 461.8 / 7-up 395.8 mm|
|Design speed|200 rpm; 6-up runs 166.7, 7-up 142.9|20% headroom on the faster ups|
|Runout / balance|TIR ≤ 0.03 mm; G1.0 per sleeve set|Re-balance check each sleeve family|
|Sleeve interface|Pinned to encoder zero ±0.02 mm, taper-locked|Grade change without re-registration|
|Sleeve pattern tolerance|±0.02 mm over 2,771 mm, all n pitches|Equal pitches = one phase fits all|
|Vacuum sectors|Fixed angular sectors, independent of ups|No sector change at grade change|
|CD centring|Pattern centred on drum face for all widths|Same axial setting for 100/110/120|
|Skin vs poly drum|Identical bodies, mirrored hand|Same pitch, inertia and runout class|
|Nip gap|Land-to-land 0.15-0.18 mm, stops + preload|Unchanged across sizes|

## At grade change

### Changes

· 2 sleeves (skin + poly)

· SAP chute width insert

· Recipe: ups, cams, fan, glue

· Knife insert (NB, S only)

### Stays

● Drum bodies, bearings, sectors

· Torque motors and encoders

● Nip gap and axial alignment

· Fans, ducts, glue modules

# Nichidai sleeve set — 22 sleeves, one construction

11 sizes × skin side + poly side; pocket-and-land relief, with end zones as blanked lands

[图片: 1 2 3 4]
Ask Nichidai for: sleeve-to-sleeve index repeatability ±0.02 mm, land edge radius ≤ 0.2 mm, wear-resistant land faces, and a sleeve ID tag the PLC reads to block a wrong-ups recipe.

## 1. Raised lands = channels + end zones

0.45 mm high; 30-116 mm end zones are lands too, so no SAP between cores

## 2 Pockets = SAP pattern

identical pitch on all n repeats, ±0.02 mm

## 3 Perforated screen

00.6-0.8 mm, 30-40% open, same on every sleeve

## 4 Sleeve carrier on drum body

pin + taper; ≤ 15 min swap per drum

Skin/poly pairing rule: patterns may differ, but every channel meant to bond must exist on both sleeves at the same position. Design the pair as one CAD file and fabricate both from it.

# Vacuum sectors — same angles, different dwell

Sectors are fixed in degrees; the 7-up runs 17% slower, so every zone gets 17% more time

[图片: SAP forming (VFD PID) -8... -12 kPa Land clean (air knife) lands blanked Glue + hold -4... -5 kPa NW wrap & cket forming -2... -3 kPa 0882 drum 60° 1° = 7.70 mm of screen 6-up 1.00 ms · 7-up 1.17 ms Return & screen cleaning 0 / air jet 18° Nip / transfer +1...+3 kPa (skin drum) 138°]
|Zone|Arc|6-up dwell|7-up dwell|Vacuum|
|---|---|---|---|---|
|NW wrap & pocket|$60^{\circ}$|60 ms|70 ms|$-2...-3$ kPa|
|SAP forming|$65^{\circ}$|65 ms|76 ms|$-8...-12$ kPa (receip)|
|Land clean|$25^{\circ}$|25 ms|29 ms|pockets only|
|Glue + hold|$54^{\circ}$|54 ms|63 ms|$-4...-5$ kPa|
|Nip / transfer|$18^{\circ}$|18 ms|21 ms|skin $+1...+3$ / poly $-4$|
|Return|$138^{\circ}$|138 ms|161 ms|0 / air jet|

Holding is never the limit: at 13.7 g a 230 gsm bed needs ~39 Pa; hold zones give ~4,000 Pa. The recipe changes forming vacuum (bed resistance) and the air-knife pressure, not the sector geometry.

# Forming fan power with inverter technology — per size

One blower per drum, VFD speed set by recipe and trimmed by plenum-pressure PID

## Forming-blower shaft power per drum (kW)

[图片: <table><tr><td>8</td><td>]
[图片: Flow per size 9-14 m³/min pattern area × 2.5 m/s + hold + 40% leakage Pressure 10-12 kPa screen/NW 3 + SAP bed 5-7 + duct 2 Design point 22 m³/min @ 15 kPa 8.5 kW shaft $\rightarrow$ 11 kW IE5 PM motor + VFD Energy vs damper -36% to -62% largest on NB/S at 160 gsm]
# Synchronized servo architecture with an ups-aware recipe

One virtual master at 1,000 ppm; every axis is geared or cammed to product count, not to m/min

[图片: Virtual master 1,000 products/min EtherCAT · 250 µs · DC sync Recipe (sleeve ID-checked) ups n, cams, fan, glue, chute UV camera + registration loop MA-10, ±0.1 mm deadband Skin drum torque motor 1/n rev per product Poly drum torque motor 1/n rev per product + trim SAP rotary valves (x2) e-cam, n pulses/rev NW unwinds (x2) speed = drum pitch Cut roll 1 or 2 knives by recipe Repitch turret cam per size phase trim → poly drum only]
|Drive (per drum)|6-up|7-up|
|---|---|---|
|Drum speed|166.7 rpm|142.9 rpm|
|J (est. 270 kg shell)|$\approx 52 \text{ kg}\cdot\text{m}^2$|$\approx 52 \text{ kg}\cdot\text{m}^2$|
|Run torque / power|180 Nm / 3.1 kW|180 Nm / 2.7 kW|
|Stop in 3 s|$\approx 455 \text{ Nm}$|$\approx 410 \text{ Nm}$|
|Following error|$\pm 38 \text{ µm}$|$\pm 33 \text{ µm}$|

One motor size covers both ups: direct-drive torque motor ≥ 250 Nm continuous, ≥ 600 Nm peak, ≥ 23-bit absolute encoder on the drum shaft. The 1/n gear ratio is the only thing the recipe changes.

# SAP dosing: re-set the chute speed with the ups

Drum surface speed drops from 7.70 to 6.60 m/s in 7-up — a chute tuned for 6-up then overshoots by 1.1 m/s

## SAP slide distance on NW (mm) vs speed mismatch $\Delta v$ (m/s)

[图片: <table><tr><td>35</td><td>]
## Chute velocity in the recipe

Eductor air set so SAP arrives at 6.6 or 7.7 m/s (±0.3). If left at the 6-up setting, the simulated in-spec rate drops from 99.996% to 92.7%.

## Servo rotary valve, not a curtain

Phase-locked pulses (n per revolution) put SAP only over pockets: ~90% lands on pattern vs ~50% for a continuous full-width curtain.

## Width inserts 100 / 110 / 120 mm

Shaped chute outlet per width family; strays from end zones and channels return via cyclone with fines removal.

# Registration simulation — skin vs poly pattern, both ups

200,000 products per case; spec |MD|≤1.0 mm, |CD|≤0.5 mm (keeps≥90% channel bond area)

## Relative misalignment, 3σ (mm)

[图片: <table><tr><td>1</td><td>]
## After a grade change: MD offset (mm) vs product #

[图片: Sleeve pinned (±0.05 mm) Recipe offset only (0.6 mm) No recipe offset (2.5 mm)]
## Cpk MD / CD

6-up 2.43 / 1.39 · 7-up 2.49 / 1.39

## In spec

≥ 99.99% both ups; 92.7% if chute not re-set

## Grade change

MD self-corrects in ~17 products (1 s); CD must be
pinned

# Skin-side and poly-side layers after the nip

Teal pins: channel nodes that must coincide through both SAP layers on every size

[图片: Skin side core wrap — SMS 10 gsm, hydrophilic Skin-side SAP (skin drum) Fiberized HMA, both drums Poly-side SAP (poly drum) Poly side core wrap — SMS10-12 gsm]
|Core-wrap NW|Target|
|---|---|
|Width|one width per core-width family|
|Pore size (max)|< 100 µm|
|MD strain @ 5 N/50 mm|≤ 1.5%|
|Heat shrink @ 140 °C|≤ 1%|
|Unwind speed|follows drum pitch (396/462)|

Skin and poly SAP gsm can differ (e.g. 230 skin / 160 poly); give each sleeve the land height of its own bed so the nip still meets land-to-land.

# SAP selection for pattern fidelity across 11 sizes

One SAP grade for all sizes keeps bed height, flow and chute settings recipe-only

|Property|Target|Reason (alignment / process)|
|---|---|---|
|Particle size|150–710 µm, D50 350–450 µm|Sharp edges at both 396 and 462 m/min|
|Fines < 150 µm|≤ 2%|Through NW, screen clogging, cling to end-zone lands|
|Shape|Irregular (gel-crushed)|Resists rolling after impact|
|Bulk density|0.62–0.70 g/cm³, lot CV ≤ 1%|Bed height matches land height: 0.31 mm @160, 0.44 mm @230 gsm|
|Flowability|≥ 10 g/s, anti-caking|Rotary valve fills cleanly at 16.7 pulses/s (1,000 ppm)|
|Moisture|3–6%|Less static — cleaner lands and end zones|
|CRC / AAP 0.7 psi|26–30 / ≥ 22 g/g|Fluff-free absorbency|
|Permeability|SFC ≥ 80 ×10⁻$^{7}$ cm³·s/g|No gel blocking; channels stay open wet|
|Throughput|270–700 kg/h per drum|NB 160 gsm → pants XXXXL 230 gsm|

# Hot-melt adhesive: tacky at the nip in both ups

Glue-to-nip time grows from 54 ms (6-up) to 63 ms (7-up) — pick the adhesive for the longer one

[图片: <table><tr><td>0 ms</td><td>10-20 ms</td><td>54 / 63 ms</td><td>&gt; 100 ms</td></tr><tr><td>Fiberized HMA hits SAP + lands</td><td>Fibers cool toward substrate temp</td><td>Nip: bond by PSA tack + land pressure</td><td>Cut, trim and repitch - bond must hold</td></tr></table>]
|Criterion|Recommendation|
|---|---|
|Chemistry|SBS-based pressure-sensitive; stays tacky ≥ 100 ms cold|
|Viscosity|2,500-6,000 mPa·s at 150 °C|
|Application temp|140-150 °C max (protects PP NW)|
|Add-on|3-5 gsm per drum incl. lands; ~175-240 g/min at 4 gsm|
|Softening point|85-95 °C, high cohesion for wet channels|
|Wet channel bond|≥ 1.5 N/25 mm after 2 saturations (validate)|

## Equipment for 11 sizes

· Segmented fiberizing nozzle: 100/110/120 mm core + 10 mm land margin by segment valves, no nozzle change.

● Pump speed follows drum surface speed(396 or 462 m/min), so gsm holds when the ups changes.

● Continuous over the pitch: the end-zone lands need glue to seal the core ends.

● UV tracer in skin-side glue only.

# Grade change in under 30 minutes — and the risks

## 1

### Stop & swap

Skin and poly sleeves in parallel, $\le 15$ min; chute insert; knife insert for NB/S

## 2

### Recipe load

Sleave IDs checked → ups n, cams, fan, glue segments, chute speed

[图片: 3]
## Auto-phase

Pins give ±0.05 mm; camera loop trims MD within ~17 products

[图片: 4]
## Verify

First-off channel overlay and wet bond; release to run

## Top risks and mitigations

Chute speed left at the other ups

Wrong sleeve for recipe

NB core longer than chassis

Skin/poly land heights differ with gsm

22 sleeves to store and maintain

recipe-locked edutor setpoint; alarm on SAP-edge camera metric

sleeve ID tags read by PLC; interlock on start

chip trim to 60 mm end zone; repitch turret (ratio 0.99)

design pairs together; nip set land-to-land per recipe

carrier racks, wear check of land faces per campaign
