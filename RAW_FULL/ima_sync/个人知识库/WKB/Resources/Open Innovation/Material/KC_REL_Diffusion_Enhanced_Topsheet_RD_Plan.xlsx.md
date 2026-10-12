---
media_id: "excel_3867e2b60070d7dc3f413086d0b0036e_41e957fd81a6e760ea130eafb514a220001a693ee6c0644e"
source_file: "KC_REL_Diffusion_Enhanced_Topsheet_RD_Plan.xlsx.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Resources/Open Innovation/Material/KC_REL_Diffusion_Enhanced_Topsheet_RD_Plan.xlsx.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# KC_REL_Diffusion_Enhanced_Topsheet_RD_Plan.xlsx.md

[Notes_Assumptions:Diffusion-Enhanced Topsheet (REL Ultra-Thin Core) - Notes &amp; Assumptions]
|Deliverable 1/2 foundation sheet. All assumptions are explicitly traced to source; items marked [TBD] require meeting confirmation. Prepared 2026-08-14.|Deliverable 1/2 foundation sheet. All assumptions are explicitly traced to source; items marked [TBD] require meeting confirmation. Prepared 2026-08-14.|Deliverable 1/2 foundation sheet. All assumptions are explicitly traced to source; items marked [TBD] require meeting confirmation. Prepared 2026-08-14.|Deliverable 1/2 foundation sheet. All assumptions are explicitly traced to source; items marked [TBD] require meeting confirmation. Prepared 2026-08-14.|Deliverable 1/2 foundation sheet. All assumptions are explicitly traced to source; items marked [TBD] require meeting confirmation. Prepared 2026-08-14.|
|---|---|---|---|---|
|Note: This workbook is output in English per instruction (full-English). Chinese sheet names map to: 说明与假设 / 试验方案_概述 / 试验方案_DOE矩阵 / 试验方案_表征指标 / 试验计划_排程 / 风险与资源.|Note: This workbook is output in English per instruction (full-English). Chinese sheet names map to: 说明与假设 / 试验方案_概述 / 试验方案_DOE矩阵 / 试验方案_表征指标 / 试验计划_排程 / 风险与资源.|Note: This workbook is output in English per instruction (full-English). Chinese sheet names map to: 说明与假设 / 试验方案_概述 / 试验方案_DOE矩阵 / 试验方案_表征指标 / 试验计划_排程 / 风险与资源.|Note: This workbook is output in English per instruction (full-English). Chinese sheet names map to: 说明与假设 / 试验方案_概述 / 试验方案_DOE矩阵 / 试验方案_表征指标 / 试验计划_排程 / 风险与资源.|Note: This workbook is output in English per instruction (full-English). Chinese sheet names map to: 说明与假设 / 试验方案_概述 / 试验方案_DOE矩阵 / 试验方案_表征指标 / 试验计划_排程 / 风险与资源.|
||||||
|1. SCOPE &amp; PRODUCT DEFINITION|1. SCOPE &amp; PRODUCT DEFINITION|1. SCOPE &amp; PRODUCT DEFINITION|1. SCOPE &amp; PRODUCT DEFINITION|1. SCOPE &amp; PRODUCT DEFINITION|
|S1|Product|Diffusion-enhanced topsheet = functional layer at topsheet-to-core interface responsible for fast acquisition (下渗) + in-plane lateral distribution (面内扩散), for REL ultra-thin core diaper.|Defined in task brief|Confirmed|
|S2|Layer architecture|Dual-card system: (a) skin-side card = 2D ES + optional Lyocell (softness/hydrophilicity); (b) core-side card = profiled fiber + ES (acquisition/distribution). Whether this replaces the current ADL or sits as an integrated topsheet+ADL is pending.|Meeting minutes + task brief|TBD - confirm|
|S3|Anchor formula (最优解)|Top card: 2D 10% Lenzing Lyocell (trilobal) + 90% ES fiber. Bottom card (diffusion layer): 50% Fudi ES + 50% base ES. Best theoretical surface area + soft hand; highest cost.|Meeting 2026-08-13|Confirmed|
|S4|Backup formula (过渡/备选)|Top card: 3D 10% Fudi trilobal ES + 2D 90% ES. Bottom card: 50% 3D Fudi trilobal ES + 50% 4D base ES. Fallback: top 10% 3D spindle monocomponent PET + 90% 2D ES (subject to Suzhou supply).|Meeting 2026-08-13|Confirmed|
|S5|Cross fiber (十字)|Cross-section PET fiber kept PENDING - reported skin roughness; marginal overall benefit.|Meeting 2026-08-13|Confirmed|
|2. KEY TECHNICAL FACTS CARRIED INTO DESIGN|2. KEY TECHNICAL FACTS CARRIED INTO DESIGN|2. KEY TECHNICAL FACTS CARRIED INTO DESIGN|2. KEY TECHNICAL FACTS CARRIED INTO DESIGN|2. KEY TECHNICAL FACTS CARRIED INTO DESIGN|
|F1|PE vs PET melt behavior|PE sheath melts ~130C; over-temp (e.g. 135C oven) causes trilobal to flow/round and lose surface-area benefit. PET melts ~220C, stable profile, but bonding strength relies entirely on ES -&gt; may drop. Goal: balance strength vs. flow.|Meeting 2026-08-13|Confirmed|
|F2|Oven Delta-T validation|Must run at Yanjiang (岩浆) base line: take samples at normal set-temp, then step down 2-5C (130/128/126C batches); measure tensile + flow via microscope. Adopt lowest temp that still meets bonding strength.|Meeting 2026-08-13|Confirmed|
|F3|Profiled fiber loading|Recommended primary 10% (3D profiled PET in core-side card only); DOE 0/5/10/15/20%; launch zone 5-12%; early cap &lt;=15%, 20% stress-only. &gt;~15% risks fuzz/tensile loss/coarse hand/rewet.|KB: pentagram_PET liner|From KB|
|F4|CoPET/PET vs PE/PET ADL|CoPET/PET gives -24% 3rd-insult rewet (0.26g vs 0.34g) and +17% core utilization, but +16% price (8,900 vs 7,650 RMB/t). Recommended 30% CoPET / 70% PE blend. If caliper loss &gt;=8%, rewet benefit is zeroed.|KB: CoPET_ADL blueprint|From KB|
|F5|Simulation anchor|v11 2D sim: SAP utilization 63.6% (vs 48.1% uniform), MD spread 34.9% (D_aniso=3, theoretical limit 36.7%); ADL permeability 5e-11 m2 (~50x core). ML+Xdiff is best stable scenario.|KB: v11 simulation report|From KB|
|F6|REL layer targets|REL wet tensile currently 58 N/m, target &gt;75 N/m; 1st strike-through ~0.9s, target &lt;0.8s; rewet 0.04g, target &lt;0.03g (0.5kPa/5min).|KB: REL simulation|From KB|
|F7|Test protocol preference|Enterprise low-load multi-insult standard is PRIMARY judge; high-load short-interval protocol can mask true wearing performance (prior &#39;all-511 optimal&#39; was an artifact).|KB: SAP selection strategy|From KB|
|F8|Diffusion theory|Core total mass-transfer resistance = sum of layer resistances; SAP layer non-linear (concentration-dependent D). Improve by lowering SAP-layer resistance + raising ADL permeability + reducing interlayer contact resistance.|KB: ch12 diffusion|From KB|
|3. ASSUMPTIONS REQUIRING CONFIRMATION  [TBD]|3. ASSUMPTIONS REQUIRING CONFIRMATION  [TBD]|3. ASSUMPTIONS REQUIRING CONFIRMATION  [TBD]|3. ASSUMPTIONS REQUIRING CONFIRMATION  [TBD]|3. ASSUMPTIONS REQUIRING CONFIRMATION  [TBD]|
|A1|Final basis weight|Total dual-card basis weight assumed 25 gsm (12.5 + 12.5). Confirm target gsm and whether ADL is a separate layer or integrated card.|Proposed|TBD - confirm|
|A2|Lyocell grade|Lyocell assumed Lenzing 1.7 dtex trilobal, staple. Denier/length to be fixed with supplier.|Proposed|TBD - confirm|
|A3|Monocomponent PET source|Suzhou supplier mass-production schedule uncertain; keep Fudi trilobal ES as parallel path.|Meeting 2026-08-13|TBD - confirm|
|A4|Primary rewet threshold|Two candidate gates: material-level &lt;0.03g (0.5kPa/5min, [KB REL]) vs diaper enterprise &lt;5.9g (low-load multi-insult). Kickoff must lock the PRIMARY gate.|KB + prior project|TBD - confirm|
|A5|Budget figures|All cost figures are engineering estimates (RMB) pending procurement quotation.|Proposed|TBD - confirm|
|A6|Timeline anchors|QQV6 material validation ~end-Sep; Angela meeting Nov. Schedule is back-planned from these.|Meeting 2026-08-13|Confirmed|
|4. REFERENCE LEGEND|4. REFERENCE LEGEND|4. REFERENCE LEGEND|4. REFERENCE LEGEND|4. REFERENCE LEGEND|
|[M1]|Meeting minutes 2026-08-13 - 纤维加工工艺验证及材料研发规划研讨会|Meeting minutes 2026-08-13 - 纤维加工工艺验证及材料研发规划研讨会|Meeting minutes 2026-08-13 - 纤维加工工艺验证及材料研发规划研讨会|Meeting minutes 2026-08-13 - 纤维加工工艺验证及材料研发规划研讨会|
|[K1]|KB: v11_simulation_report_20260708.pdf|KB: v11_simulation_report_20260708.pdf|KB: v11_simulation_report_20260708.pdf|KB: v11_simulation_report_20260708.pdf|
|[K2]|KB: CoPET_ADL_Strategic_Blueprint.pptx|KB: CoPET_ADL_Strategic_Blueprint.pptx|KB: CoPET_ADL_Strategic_Blueprint.pptx|KB: CoPET_ADL_Strategic_Blueprint.pptx|
|[K3]|KB: pentagram_PET_diaper_liner_deep_dive.pptx|KB: pentagram_PET_diaper_liner_deep_dive.pptx|KB: pentagram_PET_diaper_liner_deep_dive.pptx|KB: pentagram_PET_diaper_liner_deep_dive.pptx|
|[K4]|KB: REL_Simulation_Baby_Diaper_Core.pptx|KB: REL_Simulation_Baby_Diaper_Core.pptx|KB: REL_Simulation_Baby_Diaper_Core.pptx|KB: REL_Simulation_Baby_Diaper_Core.pptx|
|[K5]|KB: ch12_DIFFUSION_IN_HETEROGENEOUS_MEDIA_report.md|KB: ch12_DIFFUSION_IN_HETEROGENEOUS_MEDIA_report.md|KB: ch12_DIFFUSION_IN_HETEROGENEOUS_MEDIA_report.md|KB: ch12_DIFFUSION_IN_HETEROGENEOUS_MEDIA_report.md|
|[K6]|KB: 纸尿裤结构与技术全景 / 核心技术与应用材料 (ADL funnel holes, density gradient)|KB: 纸尿裤结构与技术全景 / 核心技术与应用材料 (ADL funnel holes, density gradient)|KB: 纸尿裤结构与技术全景 / 核心技术与应用材料 (ADL funnel holes, density gradient)|KB: 纸尿裤结构与技术全景 / 核心技术与应用材料 (ADL funnel holes, density gradient)|
|[K7]|KB: NW 原始引用索引 (EDANA/INDA definitions + nonwoven test standards)|KB: NW 原始引用索引 (EDANA/INDA definitions + nonwoven test standards)|KB: NW 原始引用索引 (EDANA/INDA definitions + nonwoven test standards)|KB: NW 原始引用索引 (EDANA/INDA definitions + nonwoven test standards)|
|[K8]|KB: SAP选型策略与实验数据综合分析 (enterprise vs high-load protocol, rewet &lt;5.9g)|KB: SAP选型策略与实验数据综合分析 (enterprise vs high-load protocol, rewet &lt;5.9g)|KB: SAP选型策略与实验数据综合分析 (enterprise vs high-load protocol, rewet &lt;5.9g)|KB: SAP选型策略与实验数据综合分析 (enterprise vs high-load protocol, rewet &lt;5.9g)|

[Protocol_Overview:Diffusion-Enhanced Topsheet - Experiment Protocol (Overview)]
|试验方案_概述. Quantified targets, factors, architecture and acceptance summary. References: [M1][K1]-[K8].|试验方案_概述. Quantified targets, factors, architecture and acceptance summary. References: [M1][K1]-[K8].|试验方案_概述. Quantified targets, factors, architecture and acceptance summary. References: [M1][K1]-[K8].|试验方案_概述. Quantified targets, factors, architecture and acceptance summary. References: [M1][K1]-[K8].|
|---|---|---|---|
|1. OBJECTIVE|1. OBJECTIVE|1. OBJECTIVE|1. OBJECTIVE|
|Primary|Develop a diffusion-enhanced topsheet (acquisition + distribution) that improves SAP utilization and reduces rewet while keeping surface softness/handle for REL ultra-thin core diapers.|Develop a diffusion-enhanced topsheet (acquisition + distribution) that improves SAP utilization and reduces rewet while keeping surface softness/handle for REL ultra-thin core diapers.|Develop a diffusion-enhanced topsheet (acquisition + distribution) that improves SAP utilization and reduces rewet while keeping surface softness/handle for REL ultra-thin core diapers.|
|Secondary|Quantify the effect of profiled fibers, Lyocell, 3D emboss/perforation, mono-PET and CoPET/PET on acquisition-distribution, and lock a production-feasible, cost-viable formula + process window.|Quantify the effect of profiled fibers, Lyocell, 3D emboss/perforation, mono-PET and CoPET/PET on acquisition-distribution, and lock a production-feasible, cost-viable formula + process window.|Quantify the effect of profiled fibers, Lyocell, 3D emboss/perforation, mono-PET and CoPET/PET on acquisition-distribution, and lock a production-feasible, cost-viable formula + process window.|
|Validation|Confirm sim-to-real translation (v11 predicts SAP util 63.6%, MD spread 34.9% [K1]) on pilot line and finished-diaper bench.|Confirm sim-to-real translation (v11 predicts SAP util 63.6%, MD spread 34.9% [K1]) on pilot line and finished-diaper bench.|Confirm sim-to-real translation (v11 predicts SAP util 63.6%, MD spread 34.9% [K1]) on pilot line and finished-diaper bench.|
|2. CORE PERFORMANCE TARGETS (proposed acceptance thresholds)|2. CORE PERFORMANCE TARGETS (proposed acceptance thresholds)|2. CORE PERFORMANCE TARGETS (proposed acceptance thresholds)|2. CORE PERFORMANCE TARGETS (proposed acceptance thresholds)|
|KPI|Target|Direction|Rationale / Source|
|Strike-Through Time, 1st insult|&lt; 0.8 s|Minimize (down)|Current ~0.9s, target &lt;0.8s [K4]. Faster acquisition = higher SAP utilization.|
|Repeated STT, 3rd insult|&lt;= 2.5 s (no penalty vs control)|Minimize (down)|Repeat-insult robustness; CoPET shows -24% on 3rd insult [K2].|
|Rewet under load (0.5 kPa / 5 min)|&lt; 0.03 g|Minimize (down)|Current 0.04g -&gt; target &lt;0.03g [K4].|
|Diaper rewet, enterprise standard|&lt; 5.9 g|Minimize (down)|Prior project decision gate [K8].|
|MD lateral spread / fluid distribution|&gt;= 30% (target 34.9%)|Maximize (up)|v11 ML+Xdiff = 34.9% [K1]; P10 profiled fiber gives +15-25% MD spread [K3].|
|SAP utilization|&gt;= 63%|Maximize (up)|v11 ML+Xdiff = 63.6% [K1].|
|Wet tensile strength, MD|&gt;= 75 N/m|Maximize (up)|REL target [K4]; bonding must survive with ES only.|
|Caliper retention vs control|loss &lt; 8% (recovery &gt;= PE/PET baseline)|Maintain (flat)|&gt;=8% caliper loss zeroes CoPET rewet benefit [K2].|
|Softness / Handle|No degradation vs control|Maintain (flat)|P10 must show no tactile downgrade [K3]; cross fiber flagged rough [M1].|
|Fuzz / Lint|No visible shedding|Maintain (flat)|Profiled fiber cap &lt;=15% to avoid fuzz [K3].|
|3. TEST ARCHITECTURE (dual-layer functional system)|3. TEST ARCHITECTURE (dual-layer functional system)|3. TEST ARCHITECTURE (dual-layer functional system)|3. TEST ARCHITECTURE (dual-layer functional system)|
|Layer 1 - Skin-side card|2D PE/PET ES + 0-10% Lyocell (trilobal). Softness, hydrophilicity, surface area. [M1]|2D PE/PET ES + 0-10% Lyocell (trilobal). Softness, hydrophilicity, surface area. [M1]|2D PE/PET ES + 0-10% Lyocell (trilobal). Softness, hydrophilicity, surface area. [M1]|
|Layer 2 - Core-side / diffusion card|Profiled fiber (trilobal / pentagram / mono-PET spindle) + ES (2D/4D). Acquisition + in-plane distribution. 50/50 Fudi ES as anchor. [M1]|Profiled fiber (trilobal / pentagram / mono-PET spindle) + ES (2D/4D). Acquisition + in-plane distribution. 50/50 Fudi ES as anchor. [M1]|Profiled fiber (trilobal / pentagram / mono-PET spindle) + ES (2D/4D). Acquisition + in-plane distribution. 50/50 Fudi ES as anchor. [M1]|
|Optional under-layer|PET-composite ADL with 30% CoPET / 70% PE blend (3rd-insult rewet -24%, +17% core util) [K2].|PET-composite ADL with 30% CoPET / 70% PE blend (3rd-insult rewet -24%, +17% core util) [K2].|PET-composite ADL with 30% CoPET / 70% PE blend (3rd-insult rewet -24%, +17% core util) [K2].|
|Surface structuring|Plain vs 3D emboss vs perforation (funnel-shaped through-holes to promote one-way flow + anti-rewet) [K6].|Plain vs 3D emboss vs perforation (funnel-shaped through-holes to promote one-way flow + anti-rewet) [K6].|Plain vs 3D emboss vs perforation (funnel-shaped through-holes to promote one-way flow + anti-rewet) [K6].|
|4. FACTORS vs RESPONSES (mapping)|4. FACTORS vs RESPONSES (mapping)|4. FACTORS vs RESPONSES (mapping)|4. FACTORS vs RESPONSES (mapping)|
|Factor (X)|Levels (screening)|Primary responses (Y)|Reference|
|X1 Profiled fiber type|Trilobal PET / Pentagram PET|STT, MD spread, wet tensile, softness|[M1][K3]|
|X2 Profiled fiber loading|5% / 15% (center 10%)|Rewet, fuzz, softness, STT|[K3]|
|X3 Bonding sheath|PE/PET ES / PET ES|Wet tensile, caliper, STT|[M1]|
|X4 Lyocell in skin card|0% / 10%|Softness, STT, hydrophilicity|[M1]|
|X5 Surface structure|Plain / 3D emboss + perforation|Rewet, STT, MD spread|[K6]|
|5. ACCEPTANCE SUMMARY|5. ACCEPTANCE SUMMARY|5. ACCEPTANCE SUMMARY|5. ACCEPTANCE SUMMARY|
|Gate 1 (screening)|Pass if STT &lt;0.8s, rewet &lt;0.03g, wet tensile &gt;=75 N/m, no fuzz, no softness downgrade on &gt;=1 factor combination vs control.|Pass if STT &lt;0.8s, rewet &lt;0.03g, wet tensile &gt;=75 N/m, no fuzz, no softness downgrade on &gt;=1 factor combination vs control.|Pass if STT &lt;0.8s, rewet &lt;0.03g, wet tensile &gt;=75 N/m, no fuzz, no softness downgrade on &gt;=1 factor combination vs control.|
|Gate 2 (optimization)|Best candidate must beat control on &gt;=3 of 5 KPIs with zero critical failures (wet tensile &lt;60 N/m or caliper loss &gt;=8% = reject).|Best candidate must beat control on &gt;=3 of 5 KPIs with zero critical failures (wet tensile &lt;60 N/m or caliper loss &gt;=8% = reject).|Best candidate must beat control on &gt;=3 of 5 KPIs with zero critical failures (wet tensile &lt;60 N/m or caliper loss &gt;=8% = reject).|
|Gate 3 (confirm)|Top-2 candidates reproduced on pilot line + diaper bench; enterprise rewet &lt;5.9g; SAP utilization &gt;=63% verified.|Top-2 candidates reproduced on pilot line + diaper bench; enterprise rewet &lt;5.9g; SAP utilization &gt;=63% verified.|Top-2 candidates reproduced on pilot line + diaper bench; enterprise rewet &lt;5.9g; SAP utilization &gt;=63% verified.|

[Protocol_DOE_Matrix:Diffusion-Enhanced Topsheet - DOE Matrix]
|试验方案_DOE矩阵. Stage 1 screening = 2^(5-1) fractional factorial (Res V, 16 runs) + 3 center points. Stage 2 optimization = full factorial 2^3 + 3 centers. Stage 3 confirmation = control + top-2. Output columns are pre-formatted for direct data entry.|试验方案_DOE矩阵. Stage 1 screening = 2^(5-1) fractional factorial (Res V, 16 runs) + 3 center points. Stage 2 optimization = full factorial 2^3 + 3 centers. Stage 3 confirmation = control + top-2. Output columns are pre-formatted for direct data entry.|试验方案_DOE矩阵. Stage 1 screening = 2^(5-1) fractional factorial (Res V, 16 runs) + 3 center points. Stage 2 optimization = full factorial 2^3 + 3 centers. Stage 3 confirmation = control + top-2. Output columns are pre-formatted for direct data entry.|试验方案_DOE矩阵. Stage 1 screening = 2^(5-1) fractional factorial (Res V, 16 runs) + 3 center points. Stage 2 optimization = full factorial 2^3 + 3 centers. Stage 3 confirmation = control + top-2. Output columns are pre-formatted for direct data entry.|试验方案_DOE矩阵. Stage 1 screening = 2^(5-1) fractional factorial (Res V, 16 runs) + 3 center points. Stage 2 optimization = full factorial 2^3 + 3 centers. Stage 3 confirmation = control + top-2. Output columns are pre-formatted for direct data entry.|试验方案_DOE矩阵. Stage 1 screening = 2^(5-1) fractional factorial (Res V, 16 runs) + 3 center points. Stage 2 optimization = full factorial 2^3 + 3 centers. Stage 3 confirmation = control + top-2. Output columns are pre-formatted for direct data entry.|试验方案_DOE矩阵. Stage 1 screening = 2^(5-1) fractional factorial (Res V, 16 runs) + 3 center points. Stage 2 optimization = full factorial 2^3 + 3 centers. Stage 3 confirmation = control + top-2. Output columns are pre-formatted for direct data entry.|试验方案_DOE矩阵. Stage 1 screening = 2^(5-1) fractional factorial (Res V, 16 runs) + 3 center points. Stage 2 optimization = full factorial 2^3 + 3 centers. Stage 3 confirmation = control + top-2. Output columns are pre-formatted for direct data entry.|试验方案_DOE矩阵. Stage 1 screening = 2^(5-1) fractional factorial (Res V, 16 runs) + 3 center points. Stage 2 optimization = full factorial 2^3 + 3 centers. Stage 3 confirmation = control + top-2. Output columns are pre-formatted for direct data entry.|试验方案_DOE矩阵. Stage 1 screening = 2^(5-1) fractional factorial (Res V, 16 runs) + 3 center points. Stage 2 optimization = full factorial 2^3 + 3 centers. Stage 3 confirmation = control + top-2. Output columns are pre-formatted for direct data entry.|试验方案_DOE矩阵. Stage 1 screening = 2^(5-1) fractional factorial (Res V, 16 runs) + 3 center points. Stage 2 optimization = full factorial 2^3 + 3 centers. Stage 3 confirmation = control + top-2. Output columns are pre-formatted for direct data entry.|试验方案_DOE矩阵. Stage 1 screening = 2^(5-1) fractional factorial (Res V, 16 runs) + 3 center points. Stage 2 optimization = full factorial 2^3 + 3 centers. Stage 3 confirmation = control + top-2. Output columns are pre-formatted for direct data entry.|试验方案_DOE矩阵. Stage 1 screening = 2^(5-1) fractional factorial (Res V, 16 runs) + 3 center points. Stage 2 optimization = full factorial 2^3 + 3 centers. Stage 3 confirmation = control + top-2. Output columns are pre-formatted for direct data entry.|试验方案_DOE矩阵. Stage 1 screening = 2^(5-1) fractional factorial (Res V, 16 runs) + 3 center points. Stage 2 optimization = full factorial 2^3 + 3 centers. Stage 3 confirmation = control + top-2. Output columns are pre-formatted for direct data entry.|试验方案_DOE矩阵. Stage 1 screening = 2^(5-1) fractional factorial (Res V, 16 runs) + 3 center points. Stage 2 optimization = full factorial 2^3 + 3 centers. Stage 3 confirmation = control + top-2. Output columns are pre-formatted for direct data entry.|试验方案_DOE矩阵. Stage 1 screening = 2^(5-1) fractional factorial (Res V, 16 runs) + 3 center points. Stage 2 optimization = full factorial 2^3 + 3 centers. Stage 3 confirmation = control + top-2. Output columns are pre-formatted for direct data entry.|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Fixed parameters (all runs): total basis weight 25 gsm (12.5 skin + 12.5 core); profiled fiber 3.0D, cut 38-51mm, 3D crimp; ES 2D/4D; durable hydrophilic finish; ATB bonding (NO oven temp increase for PET bonding [K3]).|Fixed parameters (all runs): total basis weight 25 gsm (12.5 skin + 12.5 core); profiled fiber 3.0D, cut 38-51mm, 3D crimp; ES 2D/4D; durable hydrophilic finish; ATB bonding (NO oven temp increase for PET bonding [K3]).|Fixed parameters (all runs): total basis weight 25 gsm (12.5 skin + 12.5 core); profiled fiber 3.0D, cut 38-51mm, 3D crimp; ES 2D/4D; durable hydrophilic finish; ATB bonding (NO oven temp increase for PET bonding [K3]).|Fixed parameters (all runs): total basis weight 25 gsm (12.5 skin + 12.5 core); profiled fiber 3.0D, cut 38-51mm, 3D crimp; ES 2D/4D; durable hydrophilic finish; ATB bonding (NO oven temp increase for PET bonding [K3]).|Fixed parameters (all runs): total basis weight 25 gsm (12.5 skin + 12.5 core); profiled fiber 3.0D, cut 38-51mm, 3D crimp; ES 2D/4D; durable hydrophilic finish; ATB bonding (NO oven temp increase for PET bonding [K3]).|Fixed parameters (all runs): total basis weight 25 gsm (12.5 skin + 12.5 core); profiled fiber 3.0D, cut 38-51mm, 3D crimp; ES 2D/4D; durable hydrophilic finish; ATB bonding (NO oven temp increase for PET bonding [K3]).|Fixed parameters (all runs): total basis weight 25 gsm (12.5 skin + 12.5 core); profiled fiber 3.0D, cut 38-51mm, 3D crimp; ES 2D/4D; durable hydrophilic finish; ATB bonding (NO oven temp increase for PET bonding [K3]).|Fixed parameters (all runs): total basis weight 25 gsm (12.5 skin + 12.5 core); profiled fiber 3.0D, cut 38-51mm, 3D crimp; ES 2D/4D; durable hydrophilic finish; ATB bonding (NO oven temp increase for PET bonding [K3]).|Fixed parameters (all runs): total basis weight 25 gsm (12.5 skin + 12.5 core); profiled fiber 3.0D, cut 38-51mm, 3D crimp; ES 2D/4D; durable hydrophilic finish; ATB bonding (NO oven temp increase for PET bonding [K3]).|Fixed parameters (all runs): total basis weight 25 gsm (12.5 skin + 12.5 core); profiled fiber 3.0D, cut 38-51mm, 3D crimp; ES 2D/4D; durable hydrophilic finish; ATB bonding (NO oven temp increase for PET bonding [K3]).|Fixed parameters (all runs): total basis weight 25 gsm (12.5 skin + 12.5 core); profiled fiber 3.0D, cut 38-51mm, 3D crimp; ES 2D/4D; durable hydrophilic finish; ATB bonding (NO oven temp increase for PET bonding [K3]).|Fixed parameters (all runs): total basis weight 25 gsm (12.5 skin + 12.5 core); profiled fiber 3.0D, cut 38-51mm, 3D crimp; ES 2D/4D; durable hydrophilic finish; ATB bonding (NO oven temp increase for PET bonding [K3]).|Fixed parameters (all runs): total basis weight 25 gsm (12.5 skin + 12.5 core); profiled fiber 3.0D, cut 38-51mm, 3D crimp; ES 2D/4D; durable hydrophilic finish; ATB bonding (NO oven temp increase for PET bonding [K3]).|Fixed parameters (all runs): total basis weight 25 gsm (12.5 skin + 12.5 core); profiled fiber 3.0D, cut 38-51mm, 3D crimp; ES 2D/4D; durable hydrophilic finish; ATB bonding (NO oven temp increase for PET bonding [K3]).|Fixed parameters (all runs): total basis weight 25 gsm (12.5 skin + 12.5 core); profiled fiber 3.0D, cut 38-51mm, 3D crimp; ES 2D/4D; durable hydrophilic finish; ATB bonding (NO oven temp increase for PET bonding [K3]).|Fixed parameters (all runs): total basis weight 25 gsm (12.5 skin + 12.5 core); profiled fiber 3.0D, cut 38-51mm, 3D crimp; ES 2D/4D; durable hydrophilic finish; ATB bonding (NO oven temp increase for PET bonding [K3]).|
|Run ID|Stage|X1 Profile type|X2 Load %|X3 Sheath|X4 Lyocell %|X5 Surface|Basis wt (gsm)|STT 1st (s)|Rewet (g)|MD spread (%)|Wet tensile (N/m)|Caliper (mm)|Softness (TS7)|Fuzz (0-3)|Notes|
|A00|Anchor|Trilobal (Lyocell)|50/50 Fudi|PE/PET ES|10% (top)|Plain|25||||||||Meeting 最优解 [M1]: top 10% Lyocell+90% ES; bottom 50% Fudi+50% base ES|
|S01|1-Screen|Trilobal PET|5%|PE/PET ES|0%|3D emboss+perf|25|||||||||
|S02|1-Screen|Trilobal PET|5%|PE/PET ES|10%|Plain|25|||||||||
|S03|1-Screen|Trilobal PET|5%|PET ES|0%|Plain|25|||||||||
|S04|1-Screen|Trilobal PET|5%|PET ES|10%|3D emboss+perf|25|||||||||
|S05|1-Screen|Trilobal PET|15%|PE/PET ES|0%|Plain|25|||||||||
|S06|1-Screen|Trilobal PET|15%|PE/PET ES|10%|3D emboss+perf|25|||||||||
|S07|1-Screen|Trilobal PET|15%|PET ES|0%|3D emboss+perf|25|||||||||
|S08|1-Screen|Trilobal PET|15%|PET ES|10%|Plain|25|||||||||
|S09|1-Screen|Pentagram PET|5%|PE/PET ES|0%|Plain|25|||||||||
|S10|1-Screen|Pentagram PET|5%|PE/PET ES|10%|3D emboss+perf|25|||||||||
|S11|1-Screen|Pentagram PET|5%|PET ES|0%|3D emboss+perf|25|||||||||
|S12|1-Screen|Pentagram PET|5%|PET ES|10%|Plain|25|||||||||
|S13|1-Screen|Pentagram PET|15%|PE/PET ES|0%|3D emboss+perf|25|||||||||
|S14|1-Screen|Pentagram PET|15%|PE/PET ES|10%|Plain|25|||||||||
|S15|1-Screen|Pentagram PET|15%|PET ES|0%|Plain|25|||||||||
|S16|1-Screen|Pentagram PET|15%|PET ES|10%|3D emboss+perf|25|||||||||
|C01|1-Screen|Trilobal PET|10%|PE/PET ES|5%|Light emboss|25||||||||Center point replicate 1|
|C02|1-Screen|Trilobal PET|10%|PE/PET ES|5%|Light emboss|25||||||||Center point replicate 2|
|C03|1-Screen|Trilobal PET|10%|PE/PET ES|5%|Light emboss|25||||||||Center point replicate 3|
|Stage 2 - Optimization (full factorial 2^3 on X2/X3/X5; X1 &amp; X4 fixed at Stage-1 optimum).|Stage 2 - Optimization (full factorial 2^3 on X2/X3/X5; X1 &amp; X4 fixed at Stage-1 optimum).|Stage 2 - Optimization (full factorial 2^3 on X2/X3/X5; X1 &amp; X4 fixed at Stage-1 optimum).|Stage 2 - Optimization (full factorial 2^3 on X2/X3/X5; X1 &amp; X4 fixed at Stage-1 optimum).|Stage 2 - Optimization (full factorial 2^3 on X2/X3/X5; X1 &amp; X4 fixed at Stage-1 optimum).|Stage 2 - Optimization (full factorial 2^3 on X2/X3/X5; X1 &amp; X4 fixed at Stage-1 optimum).|Stage 2 - Optimization (full factorial 2^3 on X2/X3/X5; X1 &amp; X4 fixed at Stage-1 optimum).|Stage 2 - Optimization (full factorial 2^3 on X2/X3/X5; X1 &amp; X4 fixed at Stage-1 optimum).|Stage 2 - Optimization (full factorial 2^3 on X2/X3/X5; X1 &amp; X4 fixed at Stage-1 optimum).|Stage 2 - Optimization (full factorial 2^3 on X2/X3/X5; X1 &amp; X4 fixed at Stage-1 optimum).|Stage 2 - Optimization (full factorial 2^3 on X2/X3/X5; X1 &amp; X4 fixed at Stage-1 optimum).|Stage 2 - Optimization (full factorial 2^3 on X2/X3/X5; X1 &amp; X4 fixed at Stage-1 optimum).|Stage 2 - Optimization (full factorial 2^3 on X2/X3/X5; X1 &amp; X4 fixed at Stage-1 optimum).|Stage 2 - Optimization (full factorial 2^3 on X2/X3/X5; X1 &amp; X4 fixed at Stage-1 optimum).|Stage 2 - Optimization (full factorial 2^3 on X2/X3/X5; X1 &amp; X4 fixed at Stage-1 optimum).|Stage 2 - Optimization (full factorial 2^3 on X2/X3/X5; X1 &amp; X4 fixed at Stage-1 optimum).|
|O01|2-Opt|Best from S1 (assume Trilobal)|5%|PE/PET ES|10% (fix)|Plain|25||||||||X1/X4 provisional until Stage 1 completes|
|O02|2-Opt|Best from S1 (assume Trilobal)|5%|PE/PET ES|10% (fix)|3D emboss+perf|25||||||||X1/X4 provisional until Stage 1 completes|
|O03|2-Opt|Best from S1 (assume Trilobal)|5%|PET ES|10% (fix)|Plain|25||||||||X1/X4 provisional until Stage 1 completes|
|O04|2-Opt|Best from S1 (assume Trilobal)|5%|PET ES|10% (fix)|3D emboss+perf|25||||||||X1/X4 provisional until Stage 1 completes|
|O05|2-Opt|Best from S1 (assume Trilobal)|15%|PE/PET ES|10% (fix)|Plain|25||||||||X1/X4 provisional until Stage 1 completes|
|O06|2-Opt|Best from S1 (assume Trilobal)|15%|PE/PET ES|10% (fix)|3D emboss+perf|25||||||||X1/X4 provisional until Stage 1 completes|
|O07|2-Opt|Best from S1 (assume Trilobal)|15%|PET ES|10% (fix)|Plain|25||||||||X1/X4 provisional until Stage 1 completes|
|O08|2-Opt|Best from S1 (assume Trilobal)|15%|PET ES|10% (fix)|3D emboss+perf|25||||||||X1/X4 provisional until Stage 1 completes|
|OC1|2-Opt|Trilobal PET|10%|PE/PET ES|10%|Light emboss|25||||||||Optimization center 1|
|OC2|2-Opt|Trilobal PET|10%|PE/PET ES|10%|Light emboss|25||||||||Optimization center 2|
|OC3|2-Opt|Trilobal PET|10%|PE/PET ES|10%|Light emboss|25||||||||Optimization center 3|
|Stage 3 - Confirmation (control + top-2 candidates, full characterization + diaper bench).|Stage 3 - Confirmation (control + top-2 candidates, full characterization + diaper bench).|Stage 3 - Confirmation (control + top-2 candidates, full characterization + diaper bench).|Stage 3 - Confirmation (control + top-2 candidates, full characterization + diaper bench).|Stage 3 - Confirmation (control + top-2 candidates, full characterization + diaper bench).|Stage 3 - Confirmation (control + top-2 candidates, full characterization + diaper bench).|Stage 3 - Confirmation (control + top-2 candidates, full characterization + diaper bench).|Stage 3 - Confirmation (control + top-2 candidates, full characterization + diaper bench).|Stage 3 - Confirmation (control + top-2 candidates, full characterization + diaper bench).|Stage 3 - Confirmation (control + top-2 candidates, full characterization + diaper bench).|Stage 3 - Confirmation (control + top-2 candidates, full characterization + diaper bench).|Stage 3 - Confirmation (control + top-2 candidates, full characterization + diaper bench).|Stage 3 - Confirmation (control + top-2 candidates, full characterization + diaper bench).|Stage 3 - Confirmation (control + top-2 candidates, full characterization + diaper bench).|Stage 3 - Confirmation (control + top-2 candidates, full characterization + diaper bench).|Stage 3 - Confirmation (control + top-2 candidates, full characterization + diaper bench).|
|F01|3-Confirm|None (control)|0%|PE/PET ES|0%|Plain|25||||||||Baseline control|
|F02|3-Confirm|TBD|TBD|TBD|TBD|TBD|25||||||||Top candidate #1 from Stage 2|
|F03|3-Confirm|TBD|TBD|TBD|TBD|TBD|25||||||||Top candidate #2 from Stage 2|

[Protocol_Characterization:Diffusion-Enhanced Topsheet - Characterization &amp; Acceptance Metrics]
|试验方案_表征指标. Columns: Unit / Target or Threshold / Direction / Test Method (GB/T, INDA/EDANA, ISO).|试验方案_表征指标. Columns: Unit / Target or Threshold / Direction / Test Method (GB/T, INDA/EDANA, ISO).|试验方案_表征指标. Columns: Unit / Target or Threshold / Direction / Test Method (GB/T, INDA/EDANA, ISO).|试验方案_表征指标. Columns: Unit / Target or Threshold / Direction / Test Method (GB/T, INDA/EDANA, ISO).|试验方案_表征指标. Columns: Unit / Target or Threshold / Direction / Test Method (GB/T, INDA/EDANA, ISO).|试验方案_表征指标. Columns: Unit / Target or Threshold / Direction / Test Method (GB/T, INDA/EDANA, ISO).|试验方案_表征指标. Columns: Unit / Target or Threshold / Direction / Test Method (GB/T, INDA/EDANA, ISO).|
|---|---|---|---|---|---|---|
|#|Metric|Unit|Target / Threshold|Direction|Test Method / Standard|Sample / Notes|
|1|Basis weight|gsm|25 +/- 1 (per card 12.5)|Target|ISO 9073-1 / GB/T 24218.1|n&gt;=5, cut 100x100mm|
|2|Thickness / Caliper|mm|Loss &lt; 8% vs control; recovery &gt;= PE/PET baseline|Maintain (flat)|ISO 9073-2 / GB/T 24218.2 (0.5 kPa foot)|CoPET: &gt;=8% loss zeroes benefit [K2]|
|3|Strike-Through Time, 1st insult|s|&lt; 0.8|Minimize (down)|EDANA/INDA WSP 70.3 / GB/T 24218.8|9 mL saline (0.9%), n&gt;=5|
|4|Repeated STT, 3rd insult|s|&lt;= 2.5, no penalty vs control|Minimize (down)|WSP 70.8 (repeat strike-through)|3 insults, same pad|
|5|Acquisition rate / Runoff|g or mL|Runoff minimized vs control|Minimize (down)|WSP 70.5 (acquisition &amp; rewet)|fixed volume, timed|
|6|Rewet under load|g|&lt; 0.03 (0.5 kPa / 5 min)|Minimize (down)|WSP 70.8 / in-house load wetback|current 0.04g [K4]|
|7|Diaper rewet (enterprise)|g|&lt; 5.9|Minimize (down)|Enterprise low-load multi-insult std [K8]|finished diaper bench|
|8|MD lateral wicking length|mm (10 min)|+15-25% vs control|Maximize (up)|WSP 10.1 / ISO 9073-6|P10 target [K3]|
|9|MD spread ratio (fluid distribution)|%|&gt;= 30 (target 34.9)|Maximize (up)|Core stain-map image analysis (after insult)|v11 sim 34.9% [K1]|
|10|SAP utilization|%|&gt;= 63|Maximize (up)|Gravimetric absorbed / theoretical capacity|v11 sim 63.6% [K1]|
|11|Wet tensile strength, MD|N/m|&gt;= 75|Maximize (up)|ISO 9073-3 / GB/T 24218.3 (wet strip)|current 58 N/m [K4]|
|12|Dry tensile strength, MD/CD|N/m|No major CD loss vs control|Maintain (flat)|ISO 9073-3 / GB/T 24218.3|watch PET bonding drop|
|13|Softness / Handle|TS7 (or H-O-M mN)|No degradation vs control|Maintain (flat)|Tissue Softness Analyzer (TSA/TS7) / WSP 90.3|P10 no tactile downgrade [K3]|
|14|Fuzz / Lint|grade 0-3|0 (no visible shedding)|Maintain (flat)|Visual + tape lift, after rub|cap loading &lt;=15% [K3]|
|15|Air permeability|mm/s or L/m2/s|No regression vs control|Maintain (flat)|ISO 9237 / GB/T 5453|breathe/comfort|
|16|Wettability / contact angle|deg or s|Wet-out &lt; 3 s|Minimize (down)|ISO 15989 / drop test|durable hydrophilic finish|
|17|Trilobal profile retention (flow check)|qualitative|Profile intact (not rounded)|Maintain (flat)|Optical/SEM microscopy of bonded web|oven Delta-T study [M1]|
|18|Fiber surface area (specific)|m2/g|Increase vs round control|Maximize (up)|BET or calculated (geometric)|profiled fiber benefit|

[Plan_Schedule:Diffusion-Enhanced Topsheet - Project Plan &amp; Weekly Schedule]
|试验计划_排程. 14 weeks back-planned from QQV6 (end-Sep) and Angela meeting (Nov). Owner roles from meeting minutes [M1].|试验计划_排程. 14 weeks back-planned from QQV6 (end-Sep) and Angela meeting (Nov). Owner roles from meeting minutes [M1].|试验计划_排程. 14 weeks back-planned from QQV6 (end-Sep) and Angela meeting (Nov). Owner roles from meeting minutes [M1].|试验计划_排程. 14 weeks back-planned from QQV6 (end-Sep) and Angela meeting (Nov). Owner roles from meeting minutes [M1].|试验计划_排程. 14 weeks back-planned from QQV6 (end-Sep) and Angela meeting (Nov). Owner roles from meeting minutes [M1].|试验计划_排程. 14 weeks back-planned from QQV6 (end-Sep) and Angela meeting (Nov). Owner roles from meeting minutes [M1].|试验计划_排程. 14 weeks back-planned from QQV6 (end-Sep) and Angela meeting (Nov). Owner roles from meeting minutes [M1].|
|---|---|---|---|---|---|---|
|Week|Start (Mon)|Phase|Activity / Task|Milestone / Deliverable|Owner|Support|
|W1|2026-08-17|P0 Kickoff|Freeze spec + basis weight; issue fiber RFQ (Lenzing Lyocell, Fudi ES, mono-PET, CoPET). Build control (25 gsm).|M1: DOE frozen + fibers sourced|Materials Engineer (徒弟)|R&amp;D Lead (负责人)|
|W2|2026-08-24|P0 Kickoff|Characterize control baseline (STT, rewet, tensile, caliper, softness). Draft DOE run list. Confirm assumptions [TBD].|Baseline dataset done|Materials Engineer|R&amp;D Lead, Clea (docs)|
|W3|2026-08-31|P1 Screening|Lab carding + ATB of screening runs S01-S08; 24h fiber conditioning, pre-mix CV&lt;5%.||Materials Engineer|Lab Technician|
|W4|2026-09-07|P1 Screening|Runs S09-S16; quick characterization (STT, tensile, caliper, fuzz).||Materials Engineer|Lab Technician|
|W5|2026-09-14|P1 Screening|Center points C01-C03; full characterization of top candidates; ANOVA / effects analysis.|M2: 3 factors shortlisted|Materials Engineer|R&amp;D Lead review|
|W6|2026-09-21|P1/P2|Shortlist factors; launch Stage-2 optimization carding (O01-O11). Oven Delta-T study at Yanjiang base (130/128/126C).|M3: QQV6 material validation (end-Sep)|Materials Engineer + 沿江 Cai Jixiang|R&amp;D Lead|
|W7|2026-09-28|P2 Optimization|Optimization runs O01-O11; full characterization; response surface fit.||Materials Engineer|Lab Technician|
|W8|2026-10-05|P2 Optimization|Microscope flow check of trilobal (Delta-T); refine process window (oven temp, suction, tension).|M4: oven temp window validated|Materials Engineer|沿江 Cai Jixiang|
|W9|2026-10-12|P2 Optimization|Select top-2 candidates + cost analysis (10% Lyocell vs 50/50 Fudi ES vs CoPET 30% blend).|M5: top-2 locked|Materials Engineer|Procurement|
|W10|2026-10-19|P3 Confirm|Pilot-line conversion of top-2 + control into finished diaper; bench test (repeat insult, loaded rewet, core stain map).||Materials Engineer|Line team, SAP supplier (Nuoer)|
|W11|2026-10-26|P3 Confirm|Diaper bench full run; SAP utilization verification; fuzz/softness panel.|M6: bench validation done|Materials Engineer|R&amp;D Lead|
|W12|2026-11-02|P4 Wrap|Patent drafting (Jerry) - profiled-fiber nonwoven in diaper system; broaden claims to wet-diaper diffusion web.|Patent draft submitted|Jerry (patent)|Materials Engineer|
|W13|2026-11-09|P4 Wrap|Final selection + spec sheet; risk closeout; cost sign-off.|Final formula + spec frozen|R&amp;D Lead|Materials Engineer, Clea|
|W14|2026-11-16|P4 Wrap|Angela-meeting package (泡泡/highlight) for REL + Liner QQV6.|M7: Angela meeting ready|R&amp;D Lead|Materials Engineer, Clea|

[Risk_Resources:Diffusion-Enhanced Topsheet - Risk Register &amp; Resource/Budget]
|风险与资源. Risk likelihood/impact = H/M/L. Budget in RMB (engineering estimate, [TBD]).|风险与资源. Risk likelihood/impact = H/M/L. Budget in RMB (engineering estimate, [TBD]).|风险与资源. Risk likelihood/impact = H/M/L. Budget in RMB (engineering estimate, [TBD]).|风险与资源. Risk likelihood/impact = H/M/L. Budget in RMB (engineering estimate, [TBD]).|风险与资源. Risk likelihood/impact = H/M/L. Budget in RMB (engineering estimate, [TBD]).|风险与资源. Risk likelihood/impact = H/M/L. Budget in RMB (engineering estimate, [TBD]).|风险与资源. Risk likelihood/impact = H/M/L. Budget in RMB (engineering estimate, [TBD]).|
|---|---|---|---|---|---|---|
|1. RISK REGISTER|1. RISK REGISTER|1. RISK REGISTER|1. RISK REGISTER|1. RISK REGISTER|1. RISK REGISTER|1. RISK REGISTER|
|ID|Risk|Likelihood|Impact|Mitigation / Control|Owner|Source|
|R1|PE sheath flows at oven temp -&gt; trilobal rounds, loses surface-area benefit|H|H|Yanjiang low-temp trial (130/128/126C); find Delta-T; microscope flow check; adopt lowest temp meeting bonding &gt;=75 N/m|Materials Engineer|[M1]|
|R2|PET / monocomponent PET bonding strength drop (bonding relies on ES)|M|H|Cap profiled loading &lt;=15%; maintain ES balance; wet tensile &gt;=75 N/m gate|Materials Engineer|[M1]|
|R3|CoPET/PET caliper loss &gt;=8% -&gt; -24% rewet benefit zeroed|M|H|Caliper recovery &gt;= PE/PET baseline; re-tune oven temp/suction/winding tension|Materials Engineer|[K2]|
|R4|Cross-section (十字) fiber skin roughness|M|M|Keep PENDING; place profiled fiber only in core-side card; handle panel gate|Materials Engineer|[M1]|
|R5|Lyocell cost premium (optimal formula highest cost)|M|M|Cost analysis 10% Lyocell vs 50/50 Fudi ES vs CoPET 30% blend; 10% cap|Procurement|[M1]|
|R6|Fuzz / lint from profiled fiber|M|M|Loading &lt;=15%; pre-mix weight CV &lt;5%; gentle carding|Materials Engineer|[K3]|
|R7|Supplier lead time (Suzhou mono-PET / Fudi mass-production schedule)|M|H|Parallel sourcing; Fudi trilobal ES as fallback path|Procurement|[M1]|
|R8|Test-protocol bias (high-load vs enterprise low-load)|M|H|Use enterprise low-load multi-insult as PRIMARY gate [K8]|Materials Engineer|[K8]|
|R9|Sim-to-real gap (SAP util 63.6% may not translate)|M|M|Mandatory diaper-bench validation (Stage 3)|Materials Engineer|[K1]|
|R10|Rewet threshold ambiguity (0.03g vs 5.9g)|L|M|Lock PRIMARY gate in kickoff [TBD A4]|R&amp;D Lead|[TBD]|
|2. RESOURCE &amp; BUDGET ESTIMATE (RMB)|2. RESOURCE &amp; BUDGET ESTIMATE (RMB)|2. RESOURCE &amp; BUDGET ESTIMATE (RMB)|2. RESOURCE &amp; BUDGET ESTIMATE (RMB)|2. RESOURCE &amp; BUDGET ESTIMATE (RMB)|2. RESOURCE &amp; BUDGET ESTIMATE (RMB)|2. RESOURCE &amp; BUDGET ESTIMATE (RMB)|
|Item|Category|Qty|Unit|Unit cost (RMB)|Total (RMB)|Notes|
|Fiber samples (Lyocell, ES, mono-PET, CoPET, profiled ES)|Material|33|run x 10 kg|25|8,250|Screening+opt+confirm trials|
|Yanjiang base line trial (3 temp-gradient batches)|Line|3|batch|16,667|50,000|Oven Delta-T + pilot conversion|
|Lab characterization consumables|Lab|1|lot|15,000|15,000|STT/rewet/tensile reagents &amp; pads|
|Diaper conversion materials (ADL/core/SAP/backsheet/chassis)|Material|1|lot|20,000|20,000|Bench + finished-diaper tests|
|Diaper bench testing|Lab|1|lot|10,000|10,000|Repeat insult, loaded rewet, stain map|
|Patent drafting + agency filing|IP|1|lot|40,000|40,000|Jerry drafts; broaden to wet-diaper diffusion web|
|Contingency (10%)|Buffer|1|lot|14,325|14,325|~10% of subtotal|
|TOTAL|TOTAL|TOTAL|TOTAL|TOTAL|157575|Excl. internal labor (man-days)|
||||||||
|3. PERSONNEL (internal, not billed in budget)|3. PERSONNEL (internal, not billed in budget)|3. PERSONNEL (internal, not billed in budget)|3. PERSONNEL (internal, not billed in budget)|3. PERSONNEL (internal, not billed in budget)|3. PERSONNEL (internal, not billed in budget)|3. PERSONNEL (internal, not billed in budget)|
|Role|Owner (meeting)|Commitment|Scope|||||
|Materials Engineer|徒弟|100% x 14 wk (~70 md)|DOE execution, characterization, cost, spec|||||
|R&amp;D Lead|负责人|20% (~10 md)|Direction, gates, approvals|||||
|Lab Technician|N/A|50% (~40 md)|Carding, ATB, standard tests|||||
|Yanjiang base|蔡吉祥 (Cai Jixiang)|3 line days|Oven Delta-T + pilot conversion|||||
|Patent|杰瑞 (Jerry)|draft (W12)|Patent write-up, broad claims|||||
|Documentation|克雷亚 (Clea)|as-needed|Paperwork, IP/project list, DB|||||
|SAP supplier|诺尔 (Nuoer)|sample support|SAP small samples for bench (supporting)||||
