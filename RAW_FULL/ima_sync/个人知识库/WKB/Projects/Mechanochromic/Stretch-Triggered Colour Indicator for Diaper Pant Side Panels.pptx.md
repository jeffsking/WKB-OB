---
media_id: "ppt_3867e2b60070d7dc3f413086d0b0036e_d0e3d9f039a94740b86597962da1103d001a693ee6c0644e"
source_file: "Stretch-Triggered Colour Indicator for Diaper Pant Side Panels.pptx.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Projects/Mechanochromic/Stretch-Triggered Colour Indicator for Diaper Pant Side Panels.pptx.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# Stretch-Triggered Colour Indicator for Diaper Pant Side Panels.pptx.md

8
CONFIDENTIAL — R&D CONCEPT STUDY

# Stretch-Triggered Colour Indicator for Diaper Pant Side Panels

A single-pass, slot-coated fit meter that tells mom whether the pant is pulled to the right tension — deep dive on the mechanochromic technology landscape, the selected material composition, and the coating process window.

0 bars

too loose

2 bars

correct fit

red bar

size up

THE BRIEF

# Seven hard requirements behind the request

Each one eliminates part of the technology space before we even look at chemistry.

[图片: R1]
### Strain-keyed colour

Distinct visual states at distinct panel elongations — not a smooth fade.

[图片: R3]
### Existing HMA applicator

Slot die on the current hot-melt system: 140-170 °C, 20-70 bar, 2-8 k s⁻$^{1}$ shear.

[图片: R5]
### Force-relevant

The reading must map to what the baby actually feels, not just to geometry.

[图片: R7]
### Baby-safe, outer face

EN 71-3 Cat III, REACH, CPSIA. No new chemistry class if avoidable.

[图片: R2]
### One printing pass

A single application station. No second coater, no registration to a pre-print.

[图片: R4]
### Reversible & repeatable

Mom pulls, reads, releases, re-dons. Needs tens of cycles without drift.

[图片: R6]
#### Cost ≈ noise

Target < 0.2 C/pant all-in. It competes with the wetness indicator budget.

R3 + R4 together are the killer: they rule out every covalent mechanophore and every liquid-crystal route before cost is even discussed.

EXECUTIVE VERDICT

# Feasible — but not with the chemistry you would expect

The literature answer (mechanophores, photonic crystals) fails on the line. A geometry-gated optical mask succeeds.

[图片: FUNCTION Three separable states at 38 / 67 / 101 % panel strain, $\Delta$E\*ab > 18 between states. Fully reversible — the mechanism is geometric, not fracture. COST $\approx 0.09 \c/pant all-in (US$0.90 per 1,000). 60 mg of filled hot melt, one shim, no new station. SAFETY Zero new chemistry classes. Every raw material is already in diaper construction adhesives or printed back sheets. Garment-facing face only. IP / FTO The umbrella concept is K-C prior art (US770458982, expiring Oct-2026). Free to practise; the broad idea is not patentable. Novelty sits in the coating architecture. MECHANO-CHEMISTRY NO-GO Spiropyran-class mechanophores need ~240 pN per bond, covalent incorporation into a crosslinked network, and fade after ~3 cycles. Not compatible with a hot melt. 03]
PART ONE

# Does a stretch reading actually tell mom about force?

Before choosing a colour chemistry we have to prove the underlying claim: that panel elongation is a usable proxy for the tension the baby feels — and find where the real discomfort limit sits.

[图片]
1. Strain $\rightarrow$ force $\rightarrow$ skin pressure

[图片]
Where red marks come from

[图片]
Read the retraction curve

[图片]
The three-band target spec

THE PHYSICS

## Strain $\rightarrow$ force $\rightarrow$ skin pressure

For a given panel construction the elongation-to-force map is fixed, so reading elongation is reading force. This is the chain that justifies the feature.

### Step 1 — panel force at the three design points

|Panel strain|Retraction force (85 mm panel)|Band tension T|
|---|---|---|
|38 %|1.4 N|1.4 N|
|67 %|2.5 N|2.5 N|
|101 %|3.9 N|3.9 N|

Modelled for a 2.2×SEBS-meltblown / spunbond panel laminate. Industry design window for elasticised side panels is 250–500 gf at 6–19 mm extension.

### Step 2 — convert tension to skin pressure

$$P=T/(r\cdot w)$$

T band tension (N) · r hip radius, 76 mm at size 4 · w effective band width

A broad panel spreads the same tension over ~85 mm. A waist elastic spreads it over ~10 mm. Same newtons, 8.5× the pressure.

### Step 3 — the honest conclusion

1

Mean panel pressure never reaches the discomfort limit.

At 101 % strain the broad panel delivers ~4.3 mmHg. Capillary occlusion needs 20–30 mmHg sustained. The panel band itself is not the red-mark source.

2

The real risk is edge concentration and creep.

Narrow waist elastics under the same tension reach ~20 mmHg. Over-stretching the panel raises waist-elastic tension too — that is the mechanism the indicator actually protects against.

3

So the indicator is a fit and containment guide, not a pressure meter.

Claim it as 'pulled to the right stretch for a secure, comfortable fit' — never as a medical or pressure-safety claim.

COMFORT LIMIT

# Same tension, very different skin pressure

Contact pressure scales inversely with band width — which is why a broad indicator panel is safe to pull firm.

[图片: Modelled contact pressure at the hip, size-4 pant 29.4 mmHg mmHg 16 11 6 2.8 mmHg 4.3 mmHg Panel band 85 mm @ 2.5 N Panel band 85 mm @ 3.9 N Leg cuff 25 mm @ 2.5 N Waist elastic 10 mm @ 2.0 N Waist elastic 10 mm @ 3.0 N Discomfort threshold 20-30 mmHg sustained — the range where capillary perfusion is impaired and indentation marks persist after removal. What this buys the design The indicator can sit on the widest part of the panel with no comfort penalty. A 'too tight' warning at ~100% strain is really an over-tension warning for the waist elastic downstream. It also protects containment: under-stretched pants sag and leak before they ever feel tight.]
## Discomfort threshold

20-30

mmHg sustained — the range where capillary perfusion is impaired and indentation marks persist after removal.

## What this buys the design

$\bullet$ The indicator can sit on the widest part of the panel with no comfort penalty.

$\bullet$ A 'too tight' warning at ~100% strain is really an over-tension warning for the waist elastic downstream.

$\bullet$ It also protects containment: under-stretched pants sag and leak before they ever feel tight.

CALIBRATION

# Calibrate on the retraction curve, not the extension curve

Mom pulls the pant on, then lets go. What the baby feels for the next eight hours is the unloading branch.

[图片: Panel hysteresis — 85 mm laminate, 2nd cycle, 500 mm/min Force (N) 4 5 6 7 8 9 1 [重复数据串: 0 0 0 0 ×52] 0]
### Hysteresis is 35–55 % for an SEBS panel.

At 100% strain the pull force is 5.2 N but the sustained worn tension is 3.9 N. Publishing thresholds against the extension curve would overstate comfort by ~30%.

The indicator reads position, so it is hysteresis-blind — and that is a feature.

It reports where the panel sits, which is the same on both branches. We only have to choose which branch we calibrate the 'correct' band against.

### Set the band on the retraction curve.

Design point: 67% strain $\rightarrow$ 2.5 N sustained $\rightarrow$ ~2.8 mmHg mean. Comfortable, secure, and 5× below the marking threshold.

### Add a stress-relaxation correction.

SEBS panels lose 12-20% of tension in the first hour. The 'correct' band must be wide enough that an hour of relaxation does not drop the reading out of it — hence a 30-point-wide window, not a single line.

TARGET SPECIFICATION

# The read-out: a three-segment fit meter

Language-free, count-based, and legible at arm's length in a dim nursery.

[图片: <38 % panel strain TOO LOOSE Pull firmer, or size down. Sag and leak risk. 38 - 67 % panel strain ALMOST Acceptable. Slightly loose for an active toddler. 67 - 101 % panel strain CORRECT FIT Target state. 2.5-3.9 N sustained, ~3 mmHg. > 101 % panel strain TOO TIGHT Size up.�ist elastic is being over-tensioned.]
Design rule: target = two green, no red.

Counting beats hue-matching. A parent in a dark room at 3 a.m. cannot reliably distinguish purple from red-purple, but can always count bars. It also survives colour-vision deficiency and phone-camera photography for a support ticket.

PART TWO

# The mechanochromic technology landscape

Seven families can turn strain into colour. We score each against the applicator, the cycle life, the cost ceiling and the tox package — then keep the two that survive.

[图片]
1 Seven families, mapped

[图片]
Screening matrix

[图片]
Why mechanophores fail

[图片]
4 Why photonics is 'watch, not now'

LANDSCAPE

# Seven ways to turn strain into colour

Positioned by maturity and by delivered cost index. Bubble size = optical vividness.

[图片: Polymer opal / colloidal photonic Bragg shift, 127 nm Molecular mechanophore spirapyran, ~240 pN Cholesteric LCE helical pitch shift Interference pigment flake re-orientation Craze / cavitation whitening interfacial debond Geometric optical mask reveal by area]
SCREENING

# Screening matrix — the applicator does most of the eliminating

Green = passes. Amber = solvable with work. Red = disqualifying for this application.

|Family|Mechanism|Usable strain|Reversible|Slot-coatable|Cost idx|New tox pkg|TRL|Verdict|
|---|---|---|---|---|---|---|---|---|
|Geometric optical mask|Opaque print un-covers a printed under-colour by area|10-150 %|∞ cycles|Native|1.0x|None|8|SELECT|
|Craze / cavitation whitening|Interfacial debond at hard particles → Mie scatter|40-120 %|Thermal reset|Yes|1.4x|Minor|5|PHASE 2|
|Interference pigment|Mica-TiO2 flake re-orientation on stretch|30-200 %|Yes|Yes|3x|Minor|4|BACKUP|
|Polymer opal / colloidal PC|Bragg peak blue-shifts; 127 nm range demonstrated|0-60 %|>100 cyc|Needs shear ordering|25x|Minor|3|WATCH|
|Stretchable DBR|Multilayer Bragg stack, NIR → visible band shift|0-50 %|Yes|Co-extruded film|15x|Minor|3|REJECT|
|Cholesteric LCE|Helix pitch compression; red → blue|>100 % for full sweep|Yes|Alignment + UV cure|40x|Full package|2-3|REJECT|
|Molecular mechanophore|C-O scission → merocyanine, ~240 pN per bond|Network-dependent|~3 cycles|Must be covalent|60x|Full package|2|REJECT|

Cost index = delivered cost per pant relative to the geometric mask baseline. TRL assessed for a 1,200 ppm�变able-hygiene context, not for a laboratory demonstrator.

DEEP DIVE · REJECTED

# Why the obvious literature answer does not survive the line

Spiropyran-class mechanophores are the most-studied colorimetric strain probe — and the least compatible with a hot-melt applicator.

## Force must reach the bond

Single-molecule force spectroscopy puts spiropyran ring-opening at roughly 240 pN on a tens-of-millisecond timescale. That force only arrives if the mechanophore sits in a taut, load-bearing chain.

### Bulk activation is weak anyway

Conversion in bulk polymers is low enough that the field's recent work is about amplifying it — tethered di-mechanophore cross-linkers, force-focusing at nanoparticle interfaces, swelling pre-tension. All add cost and chemistry.

### And the threshold moves

Activation strain shifts with cross-link density, strain rate, temperature and pulling geometry. A parent pulls fast; a designer calibrates slow. The reading would not be trustworthy.

### Which means covalent incorporation

It has to be built in as a cross-linker inside a chemically cured network. A hot melt is an un-crosslinked thermoplastic — chains slide instead of loading, so almost nothing activates.

### It fades

Reported activation can be repeated about three times before the peak colour diminishes, because the over-strained chains carrying the mechanophore are damaged. A pant is donned and adjusted more than three times.

## Full tox package

A novel chromophore in a baby product means a complete toxicological dossier plus migration work — 18–30 months and six figures before a first shipment.

DEEP DIVE · DEFERRED

# Structural colour is beautiful, and two years too early

Photonic crystals and liquid-crystal elastomers give the most vivid strain response published — and cannot be made by a glue gun.

### Polymer opals / colloidal photonic crystals

$\bullet$ Core-shell PS/PEA particles ~200~300 nm shear-assemble into elastomeric opals with intense tunable colour.

$\bullet$ Silica-in-rubber photonic fibres on spandex shift red $\rightarrow$ blue across 127 nm and survive 100+ stretch cycles.

$\bullet$ Roll-to-roll is real: bending-induced oscillatory shear has produced >100 m opal film.

$\bullet$ But ordering needs oscillatory shear at ~300% strain amplitude between heated rollers — a dedicated line, not a slot die.

### Cholesteric liquid-crystal elastomers

$\bullet$ Helical pitch compresses under strain, blue-shifting the reflection band; 2025 work adds photo-switchable chiral dopants for imprinted patterns.

$\bullet$ Uniaxial red $\rightarrow$ blue typically needs >100% strain, and colour intensity drops as it shifts.

$\bullet$ Films need planar alignment and UV cure under nitrogen — two unit operations a hot-melt station does not have.

$\bullet$ Reactive mesogen toxicology for an infant product is unresolved.

### Two failure modes they share, and one thing worth stealing

#### Moisture and UV

Mechanochromic hydrogels take up moisture that changes both mechanical and optical behaviour; UV photodegrades chromogenic units. A diaper panel sees urine vapour, sweat and daylight.

### Angle dependence

Bragg colour travels with viewing angle. A parent tilting the pant would see a colour change that is not a strain change — the worst possible failure for a fit meter.

#### Worth stealing

The non-iridescent 'amorphous photonic' variants remove angle dependence, and silica-in-rubber costs are falling. Review at the 2028 platform gate.

PART THREE

# The selected design

One ink, one shim, one pass. The strain thresholds are written into the coating geometry, not into a molecule — which is why it is cheap, reversible, and already safe.

[图片]
1. Printed stack architecture

[图片]
The threshold equation

[图片]
Ink composition

[图片]
4. Property targets

ARCHITECTURE

# The printed stack: a rigid mask over a supplied under-print

The elastic laminate already arrives gathered. We use its own corrugations as the shutter.

[图片: Relaxed · panel strain 0 % Opaque mask caps the crowns; the printed valley is hidden. Panel reads plain white. Stretched · panel strain 67 %]
Stretched · panel strain 67 %

[图片]
Corrugation flattens, the rigid mask cannot follow, printed colour appears between the islands.

## 1 Elastic panel laminate

SEBS-meltblown or SBL, bonded at 2.2× pre-stretch.
Supplies both the elasticity and — for free — the
corrugation pitch that gates the read-out.

## 2 Under-print (supplied)

Three CD bands flexo-printed on the facing nonwoven by the panel supplier: green ✓ / green ✓ / red X. No registration to our coater is required — the bands are CD-continuous.

### 3

### Slot-coated opaque mask

Our single pass. A stiff, highly filled hot melt at 7.5-11 g/m$^{2}$ in three CD zones. Modulus ≈ 85 MPa, roughly 40x the panel — it acts as a rigid shutter, not a stretchy film.

THE MECHANISM

# One equation sets all three thresholds

Because the mask is rigid and the substrate is not, the exposed colour fraction is pure geometry.

[图片: $$ \phi(\varepsilon)=1-2a/\left[\lambda_0(1+\varepsilon)\right] $$ $$ \phi(\varepsilon)=1-2a/\left[\lambda_0(1+\varepsilon)\right] $$ $$ \phi(\varepsilon)$$ exposed under-print fraction at panel strain $\varepsilon$ $$2a$$ arc of the corrugation covered by ink — set by coat weight $$\lambda_0$$ relaxed corrugation pitch, 1.2 mm for a 2.2× laminate $$\Phi^*$$ visual threshold, set at 0.30 (validated by $\Delta E^*ab\geq 6$ )]
### Rearranged for design

$$2 a=\lambda_{0}\left(1-\varphi^{*}\right)\left(1+\varepsilon^{*}\right)$$

Pick the strain you want a bar to light up at, and the equation returns the ink arc — which the shim delivers as a coat weight. Three zones, three coat weights, one ink, one pass.

### Zone design — all three from one shim

|Zone|CD width|Target ε*|Required 2a|Arc coverage|Coat weight|Shim land length|Relative flow|
|---|---|---|---|---|---|---|---|
|A — first bar|18 mm|38 %|1.39 mm|53 %|7.5 g/m²|18.0 mm|1.00|
|B — second bar|18 mm|67 %|1.68 mm|64 %|9.0 g/m²|15.0 mm|1.20|
|C — red bar|18 mm|101 %|2.03 mm|77 %|11.0 g/m²|12.0 mm|1.47|

Flow through a slot scales as 1/land-length at constant manifold pressure, so land lengths of 18 / 15 / 12 mm give 1.00 : 1.20 : 1.50 — within 2 % of the required 1.00 : 1.20 : 1.47. The zoning is machined into the shim; nothing has to be controlled during production.

MATERIAL COMPOSITION

# Ink TB-A — the opaque masking hot melt

Every component is already qualified somewhere in a diaper. That is the point.

|#|Component|Grade / specification|Function in the mechanism|wt %|
|---|---|---|---|---|
|1|Amorphous poly-α-olefin (APAO)|Propene-rich, Mw ≈ 40 kDa, viscosity 8,000 mPa-s @ 190 °C|Film former; anchors to the PP spunbond facing without a primer|26.0|
|2|Hydrogenated C5 tackifier resin|R&B 100 °C, Mw ≈ 1,000, water-white, low volatiles|Wet-out onto the fibre crowns in the 0.4 s open time|16.0|
|3|Poly(α-methylstyrene) resin|R&B 140 °C, Tg 85 °C|Stiffener — raises film modulus to ≈ 85 MPa so the mask does not stretch with the panel. The key knob.|10.0|
|4|Fischer-Tropsch wax|mp 105 °C, narrow MWD, < 0.5 % oil|Cuts viscosity at the die; sets in < 0.5 s; prevents block on the roll|8.0|
|5|Rutile $TiO_{2}$|d50 0.28 µm, alumina/silica surface-treated, supplied as pre-dispersed masterbatch|Hiding power — the whole mask function. Never handled as free powder at the ink plant.|22.0|
|6|Precipitated $CaCO_{3}$|d50 0.8 µm, stearate-coated|Extender and matting agent; kills gloss so the mask reads flat white|17.0|
|7|Antioxidant package|Hindered phenol + phosphite, 1:1|Tank stability over a 48 h hold at 155 °C|1.0|
||TOTAL|Pigment volume concentration 14 %, well below CPVC — the film stays continuous and coherent||100.0|

Deliberately absent: optical brighteners (migration risk), azo pigments (aromatic amine cleavage), phthalate plasticisers, and any heavy-metal chromophore. The mask is white on purpose — all colour lives in the supplier's flexo under-print, where it is already tox-cleared.

MATERIAL COMPOSITION · PHASE 2

# Ink TB-B — a true strain-triggered whitening chemistry

If you want a colour change that comes from the material rather than from geometry, this is the only route that fits a hot melt.

## Mechanism

Glassy microspheres are dispersed in an elastomeric matrix with deliberately weak interfacial adhesion. Below the onset strain the film is translucent. Above it, the poles of each sphere debond, opening 0.3-1 µm voids. The refractive-index discontinuity turns the film opaque white — the same physics that whitens a stretched filled polyolefin, but engineered to happen at a chosen strain instead of at yield.

### Honest limitation

Cavitation onset is a stress criterion, so it is a bulk property of the ink. It cannot be zoned across the CD from a single formulation — coat weight barely moves it and shear-lag is irrelevant at millimetre stripe widths. TB-B therefore delivers ONE threshold, not three. Use it as a dedicated over-tension alarm layered on top of the TB-A meter, not as a replacement for it.

|Component|Specification|Role|wt %|
|---|---|---|---|
|SEBS block copolymer|30 % styrene, MFI 20, linear|Elastic continuous matrix; recovers fully so the voids close on release|30.0|
|Hydrogenated mid-block resin|C5 hydro, R&B 95 °C|Associates with the EB mid-block; drops melt viscosity into the window|20.0|
|Poly(α-methylstyrene)|R&B 140 °C, end-block associating|Reinforces the styrene domains so stress transfers to the sphere interface|8.0|
|Cross-linked PMMA microspheres|d50 3.0 µm, monodisperse, NO coupling agent|The void nucleators — sphere diameter sets void size, loading sets onset strain.|22.0|
|Hollow styrene-acrylic opacifier|0.4 µm internal void, 0.55 µm OD|Scatter floor and amplifier — sharpens the transition contrast|6.0|
|White mineral oil / PIB|Food-grade, low volatility|Onset tuner: softens the matrix, raises the debond strain. ±2 % moves onset by ~15 strain points.|6.0|
|Fischer-Tropsch wax + AO package|mp 105 °C; phenol/phosphite 1:1|Set speed and tank stability|8.0|

SPECIFICATION

# TB-A property targets and the viscosity window

The whole formulation exists to hit one number: 2,500–3,500 mPa·s at the die.

[图片: Brookfield Thermosel, SC4-27, 20 rpm Viscosity @ 160 °C 8000 6000 4000 2000 0 130 140 150 160 170 180 Operating window 158-164 °C Operating window 158-164 °C 158-164 °C 158-154 °C 158-154 °C 158-154 °C 158-154 °C 158-154 °C 158-154 °C 158-154 °C 158-154 °C 158-154 °C 158-154 °C 158-154 °C 158-154 °C 158-154 °C 158-154 °C 158-154 °C 158-154 °C 158-154 °C 158-154 °C 158-154 °C 158-154 °C 158-154 °C 158-154 °C 158-154 °C 158-154 °C 158-154 °C 158-154 °C 158-154 °C 158-154 °C 158-154 °C 158-15]
Modulus ratio is the specification that actually protects the read-out. If the mask softens toward the panel modulus, it stretches with the substrate and the bars stop appearing. That is why the α-methylstyrene resin level, not the pigment level, is the release-critical parameter.

|Property|Target|Method|
|---|---|---|
|Viscosity @ 160 °C|2,900 ± 400 mPa·s|ASTM D3236|
|Softening point (R&B)|112 ± 4 °C|ASTM E28|
|Melt density @ 160 °C|1.15 g/cm³|calculated|
|Solid density @ 23 °C|1.42 g/cm³|ASTM D792|
|Open time|0.8 s|in-house|
|Set time|< 0.5 s|in-house|
|Film tensile modulus|85 ± 15 MPa|ASTM D882, free film|
|Modulus ratio, ink : panel|≥ 35 : 1|derived|
|Contrast ratio @ 9 g/m²|≥ 0.86|ASTM D2805|
|Thermal stability, 48 h @ 155 °C|Δη ≤ 15 %, no char|ASTM D4499|
|Blocking, 40 °C / 48 h / 5 kPa|No transfer|in-house|

READ-OUT LOGIC

# What the panel looks like at each stage of donning

The under-print never moves. Only how much of it is uncovered changes.

[图片: Relaxed in the bag Plain white panel. Nothing to read, nothing to look broken. First green bar. Pant will stay up but is loose for an active toddler. Why the mask is white and the message is coloured: a white mask needs no colour matching between our hot melt and the supplier's flexo ink, survives lot-to-lot pigment drift, and photographs correctly under any nursery lighting. Colour accuracy becomes the panel supplier's existing problem, not a new one. Over-pulled 67% Two green bars. Sustained 2.5 N, ~3 mmHg. This is the target. Red bar appears. Size up — the waist elastic is being over-tensioned.]
Why the mask is white and the message is coloured: a white mask needs no colour matching between our hot melt and the supplier's flexo ink, survives lot-to-lot pigment drift, and photographs correctly under any nursery lighting. Colour accuracy becomes the panel supplier's existing problem, not a new one.

PART FOUR

# The coating process

Everything below runs on the hot-melt system already installed. One new shim, one new chill roll, no new station and no registration control.

[图片]
1 Line integration

[图片]
Die and shim design

[图片]
Full parameter table

[图片]
Rheology and pressure drop

LINE INTEGRATION

# Where the coater goes on the pant line

On the panel web, before cut-and-place. The web is relaxed and gathered at this point — which is exactly what the mechanism needs.

[图片: 1 Panel unwind Pre-printed elastic laminate, 2.2x bonded, 3 CD under-print bands 2 Tension control 25 N/m MD. Low, so the corrugation pitch is not pulled out before coating. 3 SLOT COATER Contact slot die, 3-zone shim, 54 mm coated width, 7.5-11 g/m² 4 Chill roll 12 °C, 180° wrap, 0.4 s dwell — sets the mask before any nip touches it 5 Vision check Line-scan camera, coat-weight proxy by reflectance, 100% inspection 6 Cut & place Existing panel applicator, unchanged 7 Side seam & fold Existing, unchanged]
## New hardware

$\bullet$ 3-zone slot shim + die body — US$14 k

$\bullet$ Chill roll & chiller — US$16 k

$\bullet$ Line-scan vision head — US$8 k

$\bullet$ Total capex — US$38 k

## Explicitly NOT needed

$\bullet$ No second applicator or tank

$\bullet$ No MD or CD registration control

$\bullet$ No tenter / CD pre-stretch frame

$\bullet$ No UV or thermal cure

$\bullet$ No solvent handling or LEL monitoring

TOOLING

# Shim design — the zoning is machined, not controlled

A single manifold pressure feeds three CD zones whose flows are fixed by land length.

[图片: 3-zone shim, 200 µm stainless, laser-cut — plan view coat-hanger manifold · single feed · 34.8 bar Zone A land 18.0 mm 7.5 g/m² 18 mm Zone B land 15.0 mm 9.0 g/m² 18 mm Zone C land 12.0 mm 11.0 g/m² longer land $\rightarrow$ more restriction $\rightarrow$ less flow 18 mm total coated width 54 mm · die lip exit · gap 200 µm]
### Why this works without control loops

$\bullet$ Flow through a rectangular land: $Q \propto \Delta P \cdot g^3 \cdot b / (12 \ \eta \ L)$. With $g, b$ and $\Delta P$ common to all three zones, the ratio is purely 1/L.

$\bullet$ Land lengths are machined to ±0.05 mm, so the coat-weight ratio is fixed to better than 1 % for the life of the shim.

$\bullet$ Absolute coat weight is set by pump rpm — one variable, one setpoint, one SPC chart.

$\bullet$ A viscosity excursion moves all three zones together, so the ratio (and therefore the thresholds) is self-compensating.

[图片: Pressure-drop check Shear rate $\dot{v}$ = 6Q/(w $g^{2}$) 8,000 $s^{-1}$ Wall shear stress $\Delta$P = 2tL/g, L = 15 mm Land pressure drop $\Delta$P = 2tL/g, L = 15 mm Typical HMA head limit A 100 µm shim would have driven 165 bar and stalled the pump — the 200 µm gap is the design decision that makes this run.]
PROCESS PARAMETERS

# Full setpoint table for the trial

Written against a 1,200 ppm pant line running the panel web at 400 m/min on the existing hot-melt system.

|Parameter|Setpoint / tolerance|Control note|
|---|---|---|
|THERMAL TRAIN|THERMAL TRAIN|THERMAL TRAIN|
|Melt tank|155 ± 3 °C|48 h max hold; auto-purge at stops > 90 s|
|Hose|158 ± 3 °C|Rising profile prevents cold slugs at the head|
|Applicator manifold|160 ± 2 °C|Sets the 2,900 mPa·s design viscosity|
|Die / shim|162 ± 2 °C|2 °C above manifold — kills edge streaking|
|DELIVERY|DELIVERY|DELIVERY|
|Gear pump|0.30 cc/rev|Keeps rpm in the low-pulsation band|
|Pump speed|576 rpm ± 2 %|The single coat-weight variable — SPC this|
|Volumetric delivery|173 cm²/min ± 3 %|= 199 g/min at melt density 1.15 g/cm³|
|Manifold pressure|34.8 ± 4 bar|Rising trend = filter blinding, not viscosity|
|Filter|100 mesh, dual|Swap on ΔP > 6 bar without a line stop|

|Parameter|Setpoint / tolerance|Control note|
|---|---|---|
|COATING GEOMETRY|COATING GEOMETRY|COATING GEOMETRY|
|Coated width|54 mm (3 × 18 mm) ± 0.5|Fixed by shim; centred on the panel|
|Coat weight by zone|7.5 / 9.0 / 11.0 g/m²|Ratio fixed by land length, ± 0.6 g/m²|
|Die gap (shim)|200 ± 5 µm|Pressure-drop driven, not film-thickness driven|
|Die-to-web|contact, 6 ± 1° wrap|Nonwoven roughness rules out precision slot mode|
|WEB & SETTING|WEB & SETTING|WEB & SETTING|
|Web speed|400 m/min (250-500)|Coat weight held by pump-to-line speed ratio|
|MD web tension|25 ± 3 N/m|Higher tension pulls out the corrugation|
|Web temp at die|22-28 °C|Above 32 °C the mask sinks too far down the flank|
|Chill roll|12 ± 2 °C, 180° wrap|0.4 s dwell; set before the first nip|
|Max downstream nip|0.5 bar|Above this the mask smears, thresholds shift low|

Every setpoint above is inside the normal operating envelope of a standard diaper hot-melt system. Nothing here asks the applicator to do something it was not built to do — which is why the trial risk sits in the incoming laminate, not in the coater.

CONTROL PLAN

# What actually moves the threshold — and what does not

Sensitivity analysis tells you where to spend control effort. Three variables matter; the rest are noise.

[图片: Panel lamination pre-stretch HIGH Coat weight Web tension at the die Melt viscosity Low Line speed Ambient humidity NEGLIGIBLE Pre-flattens the corrugation. Above 40 N/m the mask reaches too far down the flank and all thresholds shift late. Melt viscosity LOW Self-compensating — a viscosity shift moves all three zones together, so the ratio holds. Low Coat weight is held by the pump-to-line ratio; only extreme speeds change wet-out. Ambient humidity NEGLIGIBLE The mechanism is geometric. No hygroscopic component in the ink. Control conclusion: put the SPC on the incoming panel laminate, not on your own coater. Add lamination pre-stretch ratio and relaxed corrugation pitch to the panel purchase specification, with a Cpk ≥ 1.33 requirement and a certificate per lot.]
Control conclusion: put the SPC on the incoming panel laminate, not on your own coater.

Add lamination pre-stretch ratio and relaxed corrugation pitch to the panel purchase specification, with a Cpk ≥ 1.33 requirement and a certificate per lot.

PART FIVE

# Cost, safety, IP and the path to a trial

The commercial case is straightforward because nothing new is being introduced. The IP case is the one that needs attention before anyone drafts a claim.

[图片]
1 Cost model

[图片]
Safety and regulatory

[图片]
Freedom to operate

[图片]
Risk register and 24-week plan

COST

# Added cost model — US$0.90 per thousand pants

Basis: 441 M pants per year at 1,200 ppm and 70 % OEE; three-year capex amortisation.

|Cost element|Basis|US$ / 1,000 pants|% of add-on|
|---|---|---|---|
|Indicator hot melt TB-A|0.060 g/pant (2 panels × 54 × 60 mm at 9.2 g/m²) @ US$6.50/kg|0.39|43%|
|Under-print upcharge|3-colour flexo band on the elastic laminate, supplier upcharge|0.15|17%|
|Added waste & start-up scrap|0.10 % incremental scrap rate|0.20|22%|
|QC & lot-release testing|Coat weight, ΔE threshold check, 1 per shift|0.07|8%|
|Capex amortisation|US$38 k over 3 years / 1.32 bn pants|0.03|3%|
|Energy (chill roll + extra zone)|≈ 4 kW continuous|0.06|7%|

0.09 $

added cost per pant

US$38 k

total new capex

1: 4

vs a typical wetness indicator stripe

0

new raw material
classes introduced

Sensitivity: TiO₂ is 43 % of the ink cost. A TiO₂-free variant using hollow styrene-acrylic opacifier plus calcined kaolin lands at US$5.20/kg but drops contrast ratio to 0.79 — hold it as the regulatory hedge, not the base case.

SAFETY

# Safety case — the argument is 'nothing new', and it holds

Placement, binding and material provenance do most of the work; testing confirms rather than discovers.

### Placement

* Garment-facing outer surface only — never in contact with skin or mucosa.

$\bullet$ Outside the absorbent core; no pathway to urine or faeces contact in normal use.

$\bullet$ No component within 15 mm of the leg cuff or waist edge, where abrasion is highest.

## Composition

$\bullet$ APAO, hydrogenated resins, FT wax, rutile TiO₂ and coated CaCO₃ are all present today in diaper construction adhesives and printed backheets.

$\bullet$ No azo pigments, no phthalates, no optical brighteners, no heavy-metal chromophore, no CMR Cat 1A/1B.

$\bullet$ Pigment fully bound in the binder — the primary low-migration lever.

## Test programme

$\bullet$ EN 71-3 Category III (scraped coating) — migration of the 19 restricted elements.

$\bullet$ REACH Annex XVII: PAHs, phthalates, azo-amines. CPSIA lead and phthalates.

$\bullet$ OEKO-TEX Standard 100 Product Class I (baby).

$\bullet$ Specific migration into 3 % acetic acid and 50 % ethanol simulants.

$\bullet$ Sutherland rub 100 cycles / 4 lb, loose-particle count after 24 h wear simulation.

### One watch item: titanium dioxide

TiO₂'s regulatory status has moved more than once in recent years and the inhalation-hazard question concerns free powder, not pigment bound in a polymer film on an outer surface. Two controls follow: buy it only as a pre-dispersed masterbatch so no one at the ink plant handles powder, and keep the TiO₂-free formulation qualified in parallel. Re-verify the current classification before any launch decision.

FREEDOM TO OPERATE

# The umbrella concept is prior art — plan the claims accordingly

Kimberly-Clark filed the colour-changing fit indicator in 2004. That cuts both ways.

### US 7,704,589 B2 · 'Absorbent garment with color changing fit indicator'

|Assignee|Kimberly-Clark Worldwide, Inc.|
|---|---|
|Priority / filing|30 September 2004|
|Granted|27 April 2010|
|Status|Expired — fee related; adjusted expiration 4 October 2026|
|Family|CN 101031264 B · EP 1793778 B1 · BR · KR · AU · MX|

Its disclosure already covers: a stretchable panel changing colour beyond a set percentage; two- and three-colour schemes signalling too large / correct / too small; a gathered layer printed only at the peaks whose valleys reveal on stretch; and polyolefin films that craze or crystallise to white on stretch.

### Free to practise

The patent has lapsed and the adjusted term ends this October. Practising the concept in the US carries no infringement exposure from this family.

### Not patentable as a concept

Any claim to 'a pant panel that changes colour with stretch to indicate fit' reads straight onto this disclosure. Do not build the filing strategy around the idea.

### Where the white space is

The novelty is in the execution: a single-pass hot-melt slot coating whose three strain thresholds are set by CD-zoned coat weight against the laminate's own corrugation pitch; the TB-A stiffness-ratio specification; and the TB-B debond-onset formulation.

## Before anything is drafted or launched

$\bullet$ Confirm the legal status of every family member jurisdiction by jurisdiction — CN, EP, BR, KR, AU and MX lapse independently.

$\bullet$ Run a formal FTO search on hot-melt slot-coated indicator coatings and on stiff-mask-over-gathered-substrate architectures.

$\bullet$ Search P&G, Unicharm and Daio filings after 2015 for fit-indicator continuations that could be narrower but live.

RISK

# Risk register

Ranked by exposure. The top three are all about the incoming laminate, not about the ink.

|#|Risk|Likelihood|Impact|Mitigation|
|---|---|---|---|---|
|1|Threshold drift from panel lot-to-lot pre-stretch variation|HIGH|HIGH|Add pre-stretch ratio and relaxed corrugation pitch to the purchase spec with Cpk ≥ 1.33 and a per-lot certificate. Re-qualify the shim per supplier.|
|2|Corrugation pulled out by web tension before the die|MED|HIGH|Dancer-controlled tension at 25 N/m with a hard 40 N/m alarm; short unsupported span into the coater.|
|3|Consumer misreads or ignores the meter|MED|HIGH|Count-based read-out, on-pack legend, ✓ / X icons. Validate with n = 120 in-home use test before launch commitment.|
|4|Mask smears at a downstream nip and shifts thresholds low|MED|MED|Chill roll before the first nip; cap nip pressure at 0.5 bar; in-line vision on coat pattern.|
|5|Blocking on the wound roll in a hot warehouse|LOW|MED|FT wax level and R&B ≥ 112 °C; 40 °C / 48 h / 5 kPa block test as a lot-release criterion.|
|6|Soiled or wet panel changes the reading|MED|MED|Outer face is hydrophobic; verify with synthetic urine and BM simulant soak, ΔE change ≤ 3.|
|7|$TiO_{2}$ regulatory change|LOW|MED|Keep the $TiO_{2}-free$ variant qualified in parallel; masterbatch-only handling.|
|8|Claim challenge on fit or comfort language|LOW|HIGH|Position as a fit guide. No pressure, medical or safety claim. Substantiate with the use-test data, not with the pressure model.|

MEASUREMENT

# How to measure a threshold you cannot see with a ruler

The read-out is perceptual, so the test method has to be colorimetric and defined against a perception threshold.

### Primary method — $\Delta$Eab vs strain

$\bullet$ Mount a 25 mm panel strip in a tensile frame, D65 booth, 45*/0° geometry, calibrated camera.

$\bullet$ Extend at 500 mm/min to 130 %, hold 5 s at each 5 % step, image each zone.

$\bullet$ Compute CIE $\Delta Eab$ of each zone against its own relaxed state.

$\bullet$ Threshold $\epsilon^*$ is the strain at which $\Delta Eab$ first reaches 6 — roughly three just-noticeable differences, which is what a parent resolves at arm's length in poor light.

$\bullet$ Report on the second cycle, retraction branch.

### Why $\Delta E = 6$ and not $\Delta E = 2$

$\Delta$Eab ≈ 2 is the laboratory just-noticeable difference under controlled side-by-side viewing. A parent sees the panel alone, at arm's length, in a dim room, at an angle, possibly one-handed. Setting the acceptance at three JNDs is the difference between a specification that passes on a spectrophotometer and one that passes in a nursery — and it is also what forces the state separation of 18 rather than a marginal 8.

|Test|Condition|Acceptance|
|---|---|---|
|Threshold accuracy|ΔE*ab = 6 crossing, cycle 2 retraction|38 / 67 / 101 % ± 7 pts|
|State separation|ΔE*ab between adjacent bands|≥ 18|
|Cycle durability|20 don/doff cycles to 100 %|Threshold drift ≤ ±8 pts|
|Wear-condition hold|8 h at 33 °C / 85 % RH at 67 % strain|Drift ≤ ±5 pts|
|Wet robustness|4 h synthetic urine soak (0.9 % NaCl)|ΔE change ≤ 3|
|Adhesion|Sutherland rub, 100 cyc, 4 lb|No visible removal|
|Loose particles|24 h wear sim, tape lift|No detached mask|
|Coat weight|Solvent extraction, 5 positions × 3 zones|Cpk ≥ 1.33|
|Panel hysteresis|EDANA cyclic, 2 cyc to 100 %, 500 mm/min|Retraction 2.5 N at 67 %|
|Consumer read accuracy|n = 120 in-home, unaided first use|≥ 85 % correct band|

PLAN

# Twenty-four weeks from bench to launch decision

Four stages, four gates. Nothing after Stage 2 commits capital that Stage 1 cannot justify.

[图片: Stage 1 · Weeks 1-4 Bench formulation Compound TB-A at three α-methylstyrene levels (7 / 10 / 13 %) Hand drawdown onto three panel laminates at 1.8x / 2.2x / 2.6x Build the full $\Delta$E-vs-strain map for all nine combinations Measure real panel hysteresis and replace the modelled force numbers Pilot coating Cut shim v1; run pilot slot coater at 60 m/min Verify the 1.00 : 1.20 : 1.47 flow ratio from land length alone Coating window DOE: temperature × pump × tension × web temp 500 m of coated laminate for durability and wet-robustness testing GATE: shim v2 released; coat weight Cpk $\ge$ 1.33 at pilot speed Install die, chill roll and vision head on the pant line Speed ladder: 400 / 800 / 1,200 ppm 200 k pants; full process capability and start-up scrap quantification 24 h wear trial, n = 30 babies, instrumented for threshold hold GATE: capability demonstrated at 1,200 ppm; no OEE loss GATE: launch decision Stage 3 · Weeks 10-16 Compliance & consumer Full EN 71-3 / REACH / CPSIA / OEKO-TEX dossier n = 120 in-home use test on unaided read accuracy Formal FTO opinion and provisional filing on the coating architecture Costed launch case and pack-copy substantiation GATE: capability demonstrated at 1,200 ppm; no OEE loss GATE: launch decision]
Stage 1 costs about US$18 k and four weeks. It answers the only question that matters — whether the corrugation pitch of your actual panel supply is stable enough to key three thresholds off.

WHERE THIS LANDS

# Feasible, cheap, and safe — because it refuses to be clever.

The colour chemistry is a trap.

Every published strain-chromic material — spiropyran, cholesteric elastomer, polymer opal — fails on the same two constraints: it cannot go through a hot-melt applicator, and it cannot survive tens of don/doff cycles. Rejecting them is the finding, not a failure to find something.

The control point is upstream.

Threshold stability depends on the incoming laminate's pre-stretch ratio, not on anything the coater does. Put that number in the purchase specification before the first trial, or Stage 3 will fail for reasons that look like coating problems.

The panel already contains the mechanism.

A 2.2× elastic laminate arrives with a 1.2 mm corrugation pitch built in. That corrugation is a mechanical shutter that nobody is using. One rigid, opaque, CD-zoned hot-melt coating turns it into a three-state fit meter.

Do the FTO work first.

Kimberly-Clark disclosed the concept in 2004 and the patent lapses this October. You are free to build it and unable to own the idea — so file on the coating architecture and the ink specification, or file nothing.

Next action: release the Stage 1 bench protocol and add lamination pre-stretch ratio to the panel purchase specification.

