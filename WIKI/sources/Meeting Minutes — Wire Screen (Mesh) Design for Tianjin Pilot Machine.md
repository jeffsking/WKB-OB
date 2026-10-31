---
type: source
title: "Wire Screen (Mesh) Design for Tianjin Pilot Machine — Meeting Minutes 2026-10-16（天津中试机成型网屏设计定稿会）"
source_type: 会议纪要
source_path: RAW/ima_sync/个人知识库/WKB/Meeting Minutes — Wire Screen.md
original_link: ""
date_published: 2026-10-16
date_processed: 2026-10-18
credibility: 中
knowledge_update_status: pending
key_claims:
  - "Screen #1 must deliver uniform SAP density A→B across the 385 mm pad span on a flat mesh; only the large-hole layer is used (no fine top mesh), and all openings inside the channel must be fully plugged because the channel carries no SAP"
  - "Design basis: pad SAP density is currently 366 g/m² as a double layer; the acceptable window was widened to 340–400 g/m² (start at 400) — the screen must be sized for the HALVED single-layer value ≈170–200 g/m²"
  - "Hole sizing baseline is the blower maximum 5,300 CFM (~20–21 kW; controllable range 3,250–5,300 CFM); supplier is to back-calculate hole size and open area from flow + target density + PSD, i.e. the supplier does the simulation, the customer only states requirements"
  - "Plate thickness: host recommends 0.5 mm flat plate, 0.8 mm acceptable if the supplier judges it safer — supplier must validate 0.5 mm strength at 20 kW / 5,300 CFM (no support under the mesh, only the fluff web)"
  - "Hole shape: hexagonal honeycomb preferred over round 4×4 mm (better support, avoids excessive spacing that forms 'bumps/pockets'); fine mesh carries a real clogging risk — a clogged zone loses vacuum and forming becomes uneven"
  - "Screen #2 is a gradient design: MD segment length ratio 15:65:20 and wire/density ratio 10:75:15, supplier to compute the corresponding open area; the previous email is superseded"
  - "Channel width fixed at 8 mm (main bars and branch bars at the vertical compaction split also 8 mm); nonwoven is mandatory on the mesh because holes are ≥4×4 mm"
  - "SAP PSD (Nour reference): 300–600 μm ≈70% (76.2% cited), 90–300 μm 14.5%, overall ≈100–800 μm (no 45 μm, no 850 μm)"
pages_linked: ["[[Patterned SAP Core Forming Drum（印花SAP芯体成型鼓）]]", "[[SAP Dosing Speed Matching（SAP 落料速度匹配与容差）]]", "[[SAP性能指标（CRC AUL GBP Vortex）]]"]
---

# Wire Screen (Mesh) Design for Tianjin Pilot Machine — Meeting Minutes 2026-10-16（天津中试机成型网屏设计定稿会）

## Summary 摘要

A design-lock meeting with the wire-mesh supplier 徐总 to finalize the forming screen for the Tianjin pilot machine, following an email sent two weeks earlier. The drum is 385 mm with one circumference divided into 4 segments (four screens per revolution), and the pad is formed on a flat screen with large through-holes only. The two governing numbers are the target SAP density (340–400 g/m² combined, i.e. ≈170–200 g/m² per single layer) and the blower capacity (3,250–5,300 CFM at ~20 kW), and the supplier is expected to back-calculate hole size, open area and plate strength from these. Screen #2 is a separate gradient design (MD 15:65:20, density 10:75:15). 本次会议把天津中试机的成型网屏设计锁定：一块平网、只留大孔、通道区必须完全封孔；密度与风量是输入，孔径/开孔率/板厚由供应商反算。

## Key parameters 关键参数

| Item 项 | Value 值 | Note 备注 |
|---|---|---|
| Forming drum 成型鼓 | 385 mm, 4 segments/revolution | first trial drum 首试鼓 |
| Blower 风机 | ~20 kW (21 kW cited), 3,250–5,300 CFM | design baseline = 5,300 CFM (max) 以最大风量定孔径 |
| Current mesh 现用网 | flat screen, 4×4 mm round holes | reference only, not final 仅参考 |
| Pad SAP density 芯体SAP密度 | 366 g/m² double-layer now; 340–400 g/m² acceptable, start 400 | **screen sized to single layer ≈170–200 g/m²** |
| Plate thickness 板厚 | 0.5 mm recommended; 0.8 mm acceptable | supplier to validate strength 供应商验证强度 |
| Channel width 通道宽 | 8 mm (main + branch bars) | no SAP in channel 通道内无SAP |
| Line speed 车速 | 100 m/min | open area must be recomputed over 385×4 circumference |
| SAP PSD | 300–600 μm ≈70%; 90–300 μm 14.5%; 100–800 μm overall | Nour reference SAP |

## Design logic 设计逻辑

- **One hole size or several? 单一孔径能否覆盖全区间** — in principle yes if flow is tuned (3,250–5,300 CFM), but hole size must be matched to the air flow, so a single size is only valid over a bounded density window. Decision: size for the maximum curve (5,300 CFM) and re-measure actual flow at commissioning.
- **Flat plate, no fine top layer 只用大孔单层** — the fine top mesh is dropped; particles are held by a mandatory nonwoven placed on the mesh, otherwise ≥4×4 mm holes would let SAP through.
- **Frame attachment 边框固定** — drum vendor 传阅 asked to add two steps/landings; locating flat-head screws seat the screen on those steps; the gap between steps is deliberately left open to allow later testing of a 3D forming drum.
- **Clogging vs support 堵孔与支撑的取舍** — honeycomb hex holes give better support and tighter spacing than round holes; but小孔易堵 — 传阅's earlier equipment investment showed fine mesh clogging frequently, leading to manual re-opening of holes.

## Screen #2 (gradient) 第二块网（梯度）

- MD (length/pitch) segment ratio **15 : 65 : 20**.
- Wire/density ratio **10 : 75 : 15**; supplier computes the matching open area.
- Previous email instructions are withdrawn 旧邮件口径作废.

## Action items 行动项

| # | Owner | Task |
|---|---|---|
| 1 | 徐总 | Simulate hole size & open area for Screen #1 (5,300 CFM baseline; 340–400 g/m² combined, halved for single layer; uniform distribution); state whether one hole size covers the full range |
| 2 | 徐总 | Validate 0.5 mm thickness at 20 kW / 5,300 CFM; use 0.8 mm if safer |
| 3 | 徐总 | Fill in the PSD form (Japanese form) himself; customer states requirements only |
| 4 | 徐总 | Compute Screen #2 open area per 15:65:20 and 10:75:15 |
| 5 | 曼姐 | Provide SAP PSD (delivered in meeting) |
| 6 | 传阅 | Re-check 385 four-segment dimensions |
| 7 | Factory/process | Measure actual blower flow at new-machine commissioning |

## 来源 Source

- RAW: `RAW/ima_sync/个人知识库/WKB/Meeting Minutes — Wire Screen.md`（media_id `note_...7516856562776536`）
- 镜像正文: `RAW_FULL/ima_sync/个人知识库/WKB/Meeting Minutes — Wire Screen.md`
- 取证方式: MCP `fetch_media_content`（原始笔记为录音转写整理稿，人名/机名为音译，已在原文标注待核）
- 交叉参考: [[Patterned SAP Core Forming Drum（印花SAP芯体成型鼓）]]、[[SAP Dosing Speed Matching（SAP 落料速度匹配与容差）]]
