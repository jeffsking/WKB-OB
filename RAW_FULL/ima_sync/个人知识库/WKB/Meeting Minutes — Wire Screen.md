---
media_id: "note_3867e2b60070d7dc3f413086d0b0036e_7516856562776536"
extract_status: "ok"
extract_channel: "A"
synced_at: "2026-10-18T09:17:19+08:00"
source_path: "RAW/ima_sync/个人知识库/WKB/Meeting Minutes — Wire Screen.md"
media_type: 11
extract_method: "MCP fetch_media_content (note)"
via: "agent session 2026-10-18"
---

# Meeting Minutes — Wire Screen ...

## 6. Screen #1 — Uniform Distribution

Requirement: strictly per the drawing dimensions; uniform SAP density from A to B across the 385 mm span (density at A = density at B; uniform throughout); flat mesh only .

Only the large-hole mesh is needed — no fine top mesh layer; the openings must be plugged where specified .

Current reference hole: 4 mm × 4 mm; blower 21 kW with max ~5,300 CFM on that machine .

SAP density (QQV6 basis): currently 366 g/m² double-layer; acceptable range widened to 340–400 g/m² (start with 400). This is the combined upper+lower density — the screen design must halve it (single layer ≈ 170–200 g/m²) .

Supplier to calculate via simulation: given flow, SAP density, and uniform distribution, determine the hole size (4×4 or other) and the open area .

PSD (particle size distribution) affects the calculation — different SAPs have different distributions. The form 徐总 previously sent was in Japanese, which the host could not read; 徐总 should fill it in himself, and the host will only state the requirements .

# 

# Meeting Minutes — Wire Screen (Mesh) Design for Tianjin Pilot Machine

Date: Friday, October 16, 2026 (afternoon)

Topic: Finalizing the wire screen design for the Tianjin experimental machine

Attendees: Host/presenter (screen design requester), 徐总 (wire mesh supplier), 李想, 腾哥, 何老板, 曼姐, 婷婷

Parties referenced: 传阅 (forming-drum vendor), 荷叶

Objective: Finalize the wire screen design for the Tianjin pilot machine, following up on the email sent two weeks ago (prior to the host's leave); this meeting was intended to lock the design completely .

## 3. Screen Thickness

There is no support under the mesh — it relies on the H (fluff pulp) web laid down layer by layer — so a slightly thicker plate is safer .

Host recommends 0.5 mm flat-plate thickness; 0.8 mm is acceptable if the supplier deems it safer. The supplier must validate whether 0.5 mm provides sufficient strength at 20 kW / up to 5,300 CFM .

Note: the domestic process for large-diameter screens differs from the supplier's layered process (0.1 mm cumulative build-up); the supplier's mesh is stronger .

## 9. Line Speed

Current line speed is 100 m/min — this is a speed, not an opening-rate parameter; amortized over the 385 × 4 circumference, the open area must be recalculated accordingly .

## 10. Screen #2 — Gradient Design

Ignore the previous email; new instructions per today's discussion :

Along the machine direction (length/pitch): segment ratio 15 : 65 : 20 .

Wire/density ratio: 10 : 75 : 15 — supplier to compute the correct open area accordingly .

(The transcript ends during the discussion of Screen #2.)

## Action Items

All items above are derived from the meeting transcript .

## 1. Background & Key Parameters

Forming drum: first trial drum measures 385; one drum circumference is divided into 4 segments (4 screens per drum revolution) .

Tianjin factory blower: ~20 kW; estimated flow 3,250–5,300 CFM .

Current Tianjin mesh: flat screen, 4 mm × 4 mm round holes — reference only, not final .

Key question: can 340–400 g/m² be achieved with a single hole size (adjusting only dosage/air flow), or does it require different hole sizes? In principle flow can be controlled internally (3,250–5,300); it is better to tune blower RPM to match the hole size, since a hole size designed for a maximum curve must match the air flow .

Decision: use max 5,300 CFM as the baseline for hole sizing (previous trials ran at maximum); when the new machine is commissioned, the factory process team should measure actual flow .

|#|Owner|Task|
|---|---|---|

|1|徐总|Simulate hole size & open area for Screen #1 (baseline 5,300 CFM; 340–400 g/m² combined density, halved for single layer; uniform distribution); answer whether one hole size covers the full 340–400 range|

|2|徐总|Validate 0.5 mm thickness strength at 20 kW / 5,300 CFM; use 0.8 mm if deemed safer|

|3|徐总|Fill in the PSD form himself (the Japanese form); host provides requirements only|

|4|徐总|Compute Screen #2 open area per 15:65:20 length ratio and 10:75:15 density ratio; ignore the previous email|

|5|曼姐|Provide SAP PSD data — delivered during the meeting (300–600 μm ≈ 70%, overall ≈ 100–800 μm)|

|6|传阅|Double-check the 385 four-segment dimensions|

|7|Factory/process|Measure actual blower flow when commissioning the new machine|

## 4. Basic Design Requirements per Screen (all 4 segments)

Blue area = pad forming shape; yellow area = channel. Channel width designed at 8 mm; main bars and branch bars (at the vertical compaction split) also 8 mm wide .

On each of the 4 continuous screens: blue outer frame + yellow inner channel. The channel contains NO SAP — air holes there must be completely blocked (most basic requirement) .

Frame thickness: to be finalized based on SAP density. Since two forming drums split upper/lower halves (top drum forms the top half, bottom drum forms the bottom half), thickness may need to be reduced by ~2; the average SAP density refers to the combined upper+lower density, which will be provided later .

Each "up" (segment) must carry the channel at this size .

## 5. Frame Attachment Method

Discussed whether the lower section can be left unopened; the host understood that only unopened sections allow forming such a frame — attach via spot welding (碰焊) or similar .

The hexagonal (open) part is what is needed; the upper air layer is not. The unopened section coincides with the frame location and can be fixed there .

徐总 agreed the proposal is workable, provided dimensions strictly follow the host's drawing .

## 8. Hole Shape & Clogging Risk

If hole spacing is too large, the product forms "bumps/pockets." Prior discussion concluded that hexagonal honeycomb holes are preferred — better support than round holes and avoids excessive spacing between round holes; honeycomb spacing should be as fine as possible .

Concern: if holes become very small, they clog easily. 传阅's past experiments during equipment investment showed fine mesh clogged frequently; a clogged zone loses vacuum and forming becomes uneven; the mesh was later manually opened up with larger holes .

Reference calculation is based on the existing 400 (per current 4×4 basis); at double-layer 366, single layer 170–200 g/m² is much easier; going straight to 340–400 would be more demanding .

## 2. Forming Drum Modification (Screen Mounting)

The drum vendor was asked to add two steps/landings to the drum; locating flat-head screws will fix the mesh onto these steps, with locating screw holes seated on the new steps .

The space between steps is deliberately left open, to allow future feasibility testing of a 3D forming drum .

## 7. SAP Particle Size Distribution (provided by 曼姐)

Use the standard Nour product as the reference .

300–600 μm: ~70% (one figure cited 76.2% within 300–600); 90–300 μm: 14.5% .

Minimum ~100 μm (45 μm virtually absent); maximum ~800 μm (850 μm does not exist); overall range ~100–800 μm .

Nonwoven is placed on the mesh, so particles will not be sucked away — nonwoven is mandatory since the holes are large (≥4×4 mm) .
