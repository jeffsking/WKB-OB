---
media_id: "ppt_3867e2b60070d7dc3f413086d0b0036e_0b2413066e994dd56ba4bef3a149b8d1001a693ee6c0644e"
source_file: "Diaper_Microclimate_Visualization_Feasibility.pptx.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Projects/Thermal Comfort/Diaper_Microclimate_Visualization_Feasibility.pptx.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# Diaper_Microclimate_Visualization_Feasibility.pptx.md

8
# Microclimate Visualization:
## Feasibility Analysis

Application of Thermochromic & Hydrochromic
Materials in Diaper Design

[图片]
Technology
Routes

[图片]
MVP
Strategy

[图片]
Supplier
Matrices

[图片]
Implementation
Plan

GO (Conditional)

# Recommendation: A Conditional GO for a Dual-MVP Strategy

Implement a Low-Regret approach focusing on two separate visual signals (MVP A: Temperature, MVP B: Humidity) rather than a complex combined sensor.

[图片]
### The Philosophy

Simple visual signals, not precision instrumentation. We are providing a Reason to Believe (RTB) to help caregivers act, not a clinical thermometer.

[图片]
### The Priority

Do not replace the existing
Wetness Indicator (WI). Focus on
differentiation learning first.

[图片]
### The Hard Boundary

Zero compromise to core functions (absorbency, fit, cost, skin health, manufacturability).

# Technology Route: Reversible Thermochromic (Temperature)

Mechanism: Reversible phase change via microcapsules; applied as printed stripes or laminated label patches on the outer cover.

[图片: Heat Applied Leuco dye + developer + solvent Heat Applied Colored State (Activated) Color Intensity 30-37°C Threshold Temperature (°C) Activation Window: 30-37°C (Design targets: 32/34/36°C) Response Time: ≤120s to recognizable state Cyclic Stability: Readable after ≥10 thermal cycles]
Constraint: Dry-state thermal signaling is technically demanding; claim path requires stringent internal bench data validation.

# Technology Route: Hydrochromic (Humidity & Exposure)

Mechanism: Liquid/moisture triggers resin dissolution or complexation (transitions from invisible to visible blue/cyan).

[图片: Mainstream Path: Hot-Melt Wetness Glue - Dominates 84% of the market - Lowest technical risk; perfectly adapted to current converting lines Alternative Path: Water/Solvent-Based Ink - Printed directly on PE breathable film - Eco-friendly, simplifies process, high graphic customization]
### Alternative Path: Water/Solvent-Based Ink

[图片]
- Printed directly on PE breathable film

- Eco-friendly, simplifies process, high graphic customization

Bench Metrics: Response time ≤60s | Triggered by liquid exposure (5 / 10 / 20 mL bench tests)

# The Hard Boundaries: Safety and Chemical Compliance

[图片: Skin Contact Layer (Topsheet & Core) Outer Cover & Backsheet Window 2 Regulatory Framework Must meet ISO 10993 (Cytotoxicity/Irritation), REACH, FDA, and GB (GB/T 35613-2017) guidelines.]
1

[图片]
### Chemical Limits

100% BPA-Free, Zero Formaldehyde, Zero Heavy Metals.

2

[图片]
## Regulatory Framework

Must meet ISO 10993
(Cytotoxicity/Irritation), REACH, FDA, and GB (GB/T 35613-2017) guidelines.

[图片]
Caution: Some legacy technology contains trace formaldehyde—strict auditing required.

Mandatory Rule: Absolute zero back-transfer, visible color bleeding, or direct skin contact.

# The Low-Regret MVP Framework

[图片: Objective: Prioritize bench demos and consumer comprehension over full regulatory claims for Phase 1. ### Differentiation: Signals must be distinctly different from traditional wetness indicators (WI) to prevent semantic confusion. ### Step 1: Priority 1 (P1) ### MVP A: Separate Thermochromic Application ### MVP B: Separate Hydrochromic Application ### Step 2: Priority 2 (P2) ### MVP C: The Combined Indicator (High complexity, learning tool only) NotebookLM]
# MVP A: Temperature Indicator (Priority 1)

Function: Provides a visual Reason to Believe (RTB) for thermal comfort/cooling. Does not serve any structural function.

[图片: Blue = Cool Green = Comfort Red = Warm ☑ Verification Gates Stable color shifts in targeted zones (30-37°C) > >70% consumer comprehension of too hot/cold/comfort states]
### Verification Gates

$\bullet$ Stable color shifts in targeted zones (30-37°C)

$\bullet$ >70% consumer comprehension of too hot/cold/comfort states

### Core Risks

$\bullet$ The Trust Gap (exterior temperature vs. perceived skin-feel)

$\bullet$ UV stability and long-term drift

$\bullet$ Premature triggering during shelf storage or transport

# MVP B: Humidity / Wet Exposure Indicator (Priority 1)

Function: Visual cue for wet exposure, moisture accumulation, and wet-zone expansion.

[图片: Primary Wetness Indicator (Traditional yellow to blue) New Hydrochromic Indicator (Separate feature) Verification Gates Stable activation post-insult (≤60s) Distinct consumer differentiation from the traditional Wetness Indicator Core Risks Visual and semantic overlap with the primary WI Interference from urine pH, top-sheet lotions, or SAP dust Insufficient reaction speed (unnoticed) or excessive reaction speed (redundant) NotebookLM]
# MVP C: The Combined Indicator (Priority 2)

Goal: Determine if caregivers can decode two simultaneous, distinct signals (wetness vs heat) without semantic fighting.

[图片]
Color Strategy: Strict separation—Blue/Cyan tones for humidity, Red/Green for temperature.

Exit Condition: This is a learning prototype. If consumer comprehension fails or error rates are high during Phase 4, the combined approach is halted, and we revert to single-function MVPs (A or B).

# Strategic Supplier Landscape

[图片: Thermochromic Specialists Dual-Capability & Regional Partners Hydrochromic (Hot-Melt) Leaders #### Hydrochromic (Hot-Melt) Leaders]
## Thermochromic Specialists

$\bullet$ CTI (US): Full spectrum, requires diaper customization.

$\bullet$ Matsui (Japan): Legacy leader, safety checks required.

$\bullet$ OliKrom (France): Custom temperature bands.

## Hydrochromic (Hot-Melt) Leaders

$\bullet$ Bostik, Henkel, H.B. Fuller: Represent the mature 84% hot-melt market; lowest risk for MVP B.

## Dual-Capability & Regional Partners

$\bullet$ DaeHyun (Korea): Full material pool.

$\bullet$ Qianshebian / Guangzhou Ledi (China): Cost-effective, regional speed.

# Supplier Selection Matrix & Scoring

||Technical Maturity|Safety / Compliance|Diaper Experience|Capacity|Cost|
|---|---|---|---|---|---|
|Matsui|●|●|●|●|●|
|CTI|●|●|●|●|●|
|DaeHyun|●|●|●|●|●|
|Bostik|●|●|●|●|●|
|Henkel|●|●|●|●|●|

## Strategic Takeaway

- For MVP A (Temperature), engage CTI & Matsui for their advanced microencapsulation.

- For MVP B (Humidity), engage Bostik & Henkel to leverage existing hygiene hot-melt infrastructure.

# RFQ Strategy: Demanding Precision from Partners

[图片]
[图片]
Stop asking: Do you have a product?
– Demand exact constraints.

[图片]
Performance: Can you hit a visible 30-37°C reversible transition specifically on PE film or non-woven substrates?

[图片]
* Bleeding: Do you guarantee zero color bleeding for liquid-exposure hydrochromics?

[图片]
* Process: What are your exact converting constraints (drying temps, lamination pressure, coating methods)?

[图片]
Safety: Do you have proven, documented non-skin-contact hygiene migration data?

[图片]
Logistics: What are the exact MOQs and lead times for a diaper feasibility prototype?

# 12-Month Promotion Roadmap (Phases 0-2)

[图片: Month 0-1 (Phase 0) Month 2-3 (Phase 1) Upon Card Sampling (Film/Non-woven patches off-diaper) Outer Layer Dummy Build (Integrated into outer cover, no human testing) Gate: Commitments secured for 5+ supplier samples Gate: ≥2 stable color systems identified Gate: Legibility verified and converting machine compatibility confirmed (no curling/smudging) NotebookLM]
# 12-Month Promotion Roadmap (Phases 3-4 & Launch)

[图片: Month 5-7 (Phase 3) Month 7-9 (Phase 4) Consumer Comprehension Testing (Dry/Wet state comparisons) Gate: Response times (≤120s Temp, ≤60s Hydro) and contrast metrics met Month 7-9 (Phase 4) Consumer Comprehension Testing Month 11-12: Mass Production Feasibility Gate: Response times (≤120s Temp, ≤60s Hydro) and contrast metrics met Gate: ≥70% correct signal decoding (too hot/cold or wet exposure) without confusing the signals Final Gate: Go/No-Go Decision based on BOM, final cost, and compliance audit NotebookLM]
# Critical Success Factors: The Path to Mass Production

[图片]
### Data vs. Emotion

We are building a visual cue to help caregivers know when to act, not a precision clinical thermometer. Overpromising will kill the claim.

[图片]
## The Trust Gap

The biggest risk is not chemical—it is consumer perception (e.g., the diaper looks hot, but feels cool to the touch). Phase 4 comprehension testing is non-negotiable.

[图片]
## The Final Gate

If at any point the technology compromises absorbency, fit, cost, or skin safety, the MVP is immediately halted. Core function always wins.

