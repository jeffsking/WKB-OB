---
media_id: "excel_3867e2b60070d7dc3f413086d0b0036e_09c68e97e8dbc2ebc3ed62126f285f49001a693ee6c0644e"
source_file: "KC_Diffusion_Enhanced_Topsheet_v3.xlsx.md"
original_path: "RAW/ima_sync/个人知识库/WKB/Projects/Liner/KC_Diffusion_Enhanced_Topsheet_v3.xlsx.md"
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "v2: dead-image-link->text(alt kept); repeat-digits->compressed"
processed: "2026-09-27"
---

# KC_Diffusion_Enhanced_Topsheet_v3.xlsx.md

[Notes_Assumptions:Diffusion-Enhanced Topsheet  - Notes &amp; Assumptions]
|v3 (2026-08-14). 4-configuration DOE (C1-C4), temp 126-130C, load L/H.|v3 (2026-08-14). 4-configuration DOE (C1-C4), temp 126-130C, load L/H.|v3 (2026-08-14). 4-configuration DOE (C1-C4), temp 126-130C, load L/H.|v3 (2026-08-14). 4-configuration DOE (C1-C4), temp 126-130C, load L/H.|v3 (2026-08-14). 4-configuration DOE (C1-C4), temp 126-130C, load L/H.|
|---|---|---|---|---|
|7 sheets: Notes/Overview/DOE_Matrix/Characterization/Schedule/Risk/Gantt|7 sheets: Notes/Overview/DOE_Matrix/Characterization/Schedule/Risk/Gantt|7 sheets: Notes/Overview/DOE_Matrix/Characterization/Schedule/Risk/Gantt|7 sheets: Notes/Overview/DOE_Matrix/Characterization/Schedule/Risk/Gantt|7 sheets: Notes/Overview/DOE_Matrix/Characterization/Schedule/Risk/Gantt|
||||||
|1. FOUR CONFIGURATIONS UNDER TEST|1. FOUR CONFIGURATIONS UNDER TEST|1. FOUR CONFIGURATIONS UNDER TEST|1. FOUR CONFIGURATIONS UNDER TEST|1. FOUR CONFIGURATIONS UNDER TEST|
|C1|最优解 (Optimal)|Upper: 2D 10% Lenzing Lyocell(trilobal)+90%ES. Lower: 50% Fudi ES+50% own ES. Best surface area + feel; highest cost.|Meeting 2026-08-13|Confirmed|
|C2|备选 (Alternative)|Upper: 3D 10% Fudi trilobal ES+90%2D ES. Lower: 50% 3D Fudi trilobal+50% 4D own ES. Balanced cost/perf.|Meeting 2026-08-13|Confirmed|
|C3|苏州方案 (Suzhou)|Upper: 10% 3.5D Suzhou Yimeng mono-PET spindle+90%2D ES. Lower: 50% 3D Fudi+50% 4D own ES. Cost-effective PET alternative.|User confirmed|Confirmed|
|C4|十字方案 (Cross)|Upper: 10% 1.5D 4D cross PET+90%2D ES. Lower: 50% 3D Fudi+50% 4D own ES. Skin-feel PENDING per meeting.|User confirmed|Confirmed|
|2. PROCESS VARIABLES|2. PROCESS VARIABLES|2. PROCESS VARIABLES|2. PROCESS VARIABLES|2. PROCESS VARIABLES|
|P1|Temperature (X2)|3 levels: 126C / 128C / 130C. PE melt ~130C flows, PET ~220C stable. Find &#39;strength vs flattening&#39; balance.|Meeting|Confirmed|
|P2|Loading (X3)|2 levels: Low / High. Impacts acquisition rate and bonding strength.|Proposed|Confirmed|
|P3|Total basis|50gsm (25 upper + 25 lower). Durable hydrophilic. ATB bonding (no oven increase).|Meeting + user|Confirmed|
|3. PRIMARY GOAL|3. PRIMARY GOAL|3. PRIMARY GOAL|3. PRIMARY GOAL|3. PRIMARY GOAL|
|G1|Objective|Rank C1-C4 on: (1) rewet/STT (absorption); (2) wet tensile (strength); (3) cost. Determine temperature sweet-spot for PE sheath to balance flattening vs bonding.|Task brief|Confirmed|
|4. KEY FACTS FROM KB|4. KEY FACTS FROM KB|4. KEY FACTS FROM KB|4. KEY FACTS FROM KB|4. KEY FACTS FROM KB|
|F1|Simulation anchor|v11: SAP util 63.6%, MD spread 34.9%(D_aniso=3).|KB|From KB|
|F2|CoPET/PET ADL|-24% 3rd rewet, +17% util, +16% price. 30% blend.|KB: CoPET|From KB|
|F3|REL targets|Wet tensile 58-&gt;75N/m; STT 0.9-&gt;0.8s; rewet 0.04-&gt;0.03g.|KB: REL|From KB|
|F4|Test protocol|Enterprise low-load multi-insult = PRIMARY.|KB: SAP|From KB|
|F5|Yanjiang Delta-T|130/128/126C batches; tensile+microscope flow.|Meeting|Confirmed|
|5. ASSUMPTIONS [TBD]|5. ASSUMPTIONS [TBD]|5. ASSUMPTIONS [TBD]|5. ASSUMPTIONS [TBD]|5. ASSUMPTIONS [TBD]|
|A1|C1 Lyocell grade|Lenzing 1.7dtex trilobal assumed.|Proposed|TBD|
|A2|C4 cross PET skin-feel|Skin roughness may rule out. Confirm.|Proposed|TBD|
|A3|Cost data|C1-C4 unit cost TBD; estimate based on market quotes.|Proposed|TBD|
|A4|Layer GSM split|25+25 assumed. Confirm exact ratio.|User confirmed|TBD|
|A5|Supplier qualification|Suzhou Yimeng = new; Fudi = established. Lead time 2-4wk.|Proposed|TBD|
|6. STANDARDS APPLIED|6. STANDARDS APPLIED|6. STANDARDS APPLIED|6. STANDARDS APPLIED|6. STANDARDS APPLIED|
|St1|GB/T|GB/T 8939, GB/T 13662, GB/T 13663, GB/T 15593 (fluff), GB/T 17297 (SAP)|||
|St2|INDA/EDANA|INDA 12.007 (SAP), INDA 104.020 (fluff), EDANA 801.1-02|||
|St3|ISO|ISO 4819 (MD/CD), ISO 11500 (tensile), ISO 12947 (absorption)|||
|St4|ISO|ISO 15379 (safety), ISO 9001 (QA system)|||

[Protocol_Overview]
|Test Protocol Overview (v3)|Test Protocol Overview (v3)|Test Protocol Overview (v3)||
|---|---|---|---|
|4 configurations × temperature × load; 33 runs across 3 stages.|4 configurations × temperature × load; 33 runs across 3 stages.|4 configurations × temperature × load; 33 runs across 3 stages.||
|||||
|1. PURPOSE|1. PURPOSE|1. PURPOSE||
|P1|Rank C1-C4 on absorption, strength, and cost; identify optimal temperature for PE sheath to balance flattening vs bonding; validate feasibility of Suzhou mono-PET as cost-effective alternative.|Task brief||
|P2|Support final material selection for REL ultra-thin core topsheet (50gsm dual-card).|Task brief||
|2. TARGET INDICATORS|2. TARGET INDICATORS|2. TARGET INDICATORS||
|T1|PRIMARY (finished-diaper)|rewet &lt;5.9g @0.5kPa; SAP util &gt;=63%; core stain uniform; wet tensile &gt;=75N/m; STT &lt;=0.8s.|Task brief + enterprise|
|T2|SECONDARY (material-level)|3rd rewet &lt;=0.5g; caliper loss &lt;8%; fuzz score &lt;=2; no softness drop.|Derived from KB|
|T3|COST|Unit cost delta vs control; target &lt;=20% premium over C3 (Suzhou).|User confirmed|
|T4|PROCESS|Oven temperature stable within +/-1C; no bonding strength loss at higher temp.|Derived from meeting|
|3. TEST FACTORS (v3 redesign)|3. TEST FACTORS (v3 redesign)|3. TEST FACTORS (v3 redesign)||
|X1|Configuration (4 levels)|C1=Lyocell(optimal) / C2=Fudi(trilobal) / C3=Suzhou(spindle) / C4=Cross. Full 4-config screen in Stage 1.|User confirmed|
|X2|Temperature (3 levels)|126C / 128C / 130C. Covers PE melt window; find flattening-bonding balance point.|Meeting|
|X3|Loading (2 levels)|Low / High. Affects acquisition rate and tensile. Fixed to Medium in Stage 1, varied in Stage 2.|Proposed|
|X4|Fixed|50gsm(25+25); profiled fiber 3.0D; ES 2D/4D; hydrophilic durable; ATB bonding; no oven increase.|Meeting|
|4. TEST ARCHITECTURE|4. TEST ARCHITECTURE|4. TEST ARCHITECTURE||
|S1|Stage 1 - Configuration Screen (15 runs)|4 configs x 3 temps x Medium load = 12 + 3 center. Block A=C1+C2, B=C3+C4, C=center. Goal: rank configs.|Proposed|
|S2|Stage 2 - Temp-Load Optimization (14 runs)|Top-2 configs x 3 temps x 2 loads = 12 + 2 center. Block A=C_top1, B=C_top2. Goal: find temp-load sweet spot.|Proposed|
|S3|Stage 3 - Confirmation (4 runs)|Top-2 candidates x 2 replicates each. Diaper bench. Goal: statistical confirmation.|Proposed|
|A0|Anchor (1 run)|Control = C1 at 128C (optimal assumed). Baseline.|Meeting|
|5. ACCEPTANCE GATES|5. ACCEPTANCE GATES|5. ACCEPTANCE GATES||
|G1|Gate 1 (screening)|C1 beats all on rewet+STT. No config fails fuzz&lt;=2 and caliper&gt;=92%.|Enterprise|
|G2|Gate 2 (optimization)|At least 1 config beats control on &gt;=2 of 3 PRIMARY metrics. Cost data collected.|Enterprise + cost|
|G3|Gate 3 (final)|Top-2 confirmed on pilot line + diaper bench. Enterprise rewet&lt;5.9g, SAP util&gt;=63%.|Enterprise|
|6. RISK|6. RISK|6. RISK||
|R1|Fiber quality|Cross PET skin roughness may eliminate C4 early. Have Suzhou backup.|Meeting|
|R2|Supplier timeline|Suzhou Yimeng new — lead time risk. Start qualification early.|Meeting|
|R3|Temperature loss|PE sheath may flatten at 130C. Monitor caliper+microscope.|Meeting|
|R4|Oven variation|+/-2C oven delta can shift results. Calibrate before each run.|Meeting|

[Protocol_DOE_Matrix:DOE Matrix (v3 redesign: 4-config × temp × load)]
|Stage1=4C×3T×Medium=12+3center=15 (3 blocks). Stage2=top2×3T×2L=12+2center=14 (2 blocks). Stage3=2×2=4. Total=33. Seed=20260814.|Stage1=4C×3T×Medium=12+3center=15 (3 blocks). Stage2=top2×3T×2L=12+2center=14 (2 blocks). Stage3=2×2=4. Total=33. Seed=20260814.|Stage1=4C×3T×Medium=12+3center=15 (3 blocks). Stage2=top2×3T×2L=12+2center=14 (2 blocks). Stage3=2×2=4. Total=33. Seed=20260814.|Stage1=4C×3T×Medium=12+3center=15 (3 blocks). Stage2=top2×3T×2L=12+2center=14 (2 blocks). Stage3=2×2=4. Total=33. Seed=20260814.|Stage1=4C×3T×Medium=12+3center=15 (3 blocks). Stage2=top2×3T×2L=12+2center=14 (2 blocks). Stage3=2×2=4. Total=33. Seed=20260814.|Stage1=4C×3T×Medium=12+3center=15 (3 blocks). Stage2=top2×3T×2L=12+2center=14 (2 blocks). Stage3=2×2=4. Total=33. Seed=20260814.|Stage1=4C×3T×Medium=12+3center=15 (3 blocks). Stage2=top2×3T×2L=12+2center=14 (2 blocks). Stage3=2×2=4. Total=33. Seed=20260814.|Stage1=4C×3T×Medium=12+3center=15 (3 blocks). Stage2=top2×3T×2L=12+2center=14 (2 blocks). Stage3=2×2=4. Total=33. Seed=20260814.|Stage1=4C×3T×Medium=12+3center=15 (3 blocks). Stage2=top2×3T×2L=12+2center=14 (2 blocks). Stage3=2×2=4. Total=33. Seed=20260814.|Stage1=4C×3T×Medium=12+3center=15 (3 blocks). Stage2=top2×3T×2L=12+2center=14 (2 blocks). Stage3=2×2=4. Total=33. Seed=20260814.|Stage1=4C×3T×Medium=12+3center=15 (3 blocks). Stage2=top2×3T×2L=12+2center=14 (2 blocks). Stage3=2×2=4. Total=33. Seed=20260814.|Stage1=4C×3T×Medium=12+3center=15 (3 blocks). Stage2=top2×3T×2L=12+2center=14 (2 blocks). Stage3=2×2=4. Total=33. Seed=20260814.|Stage1=4C×3T×Medium=12+3center=15 (3 blocks). Stage2=top2×3T×2L=12+2center=14 (2 blocks). Stage3=2×2=4. Total=33. Seed=20260814.|Stage1=4C×3T×Medium=12+3center=15 (3 blocks). Stage2=top2×3T×2L=12+2center=14 (2 blocks). Stage3=2×2=4. Total=33. Seed=20260814.|Stage1=4C×3T×Medium=12+3center=15 (3 blocks). Stage2=top2×3T×2L=12+2center=14 (2 blocks). Stage3=2×2=4. Total=33. Seed=20260814.||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Fixed across all runs: 50gsm(25+25); profiled 3.0D, 38-51mm; ES 2D/4D; hydrophilic durable; ATB bonding; no oven temp increase. [K3] [M1] [K2]|Fixed across all runs: 50gsm(25+25); profiled 3.0D, 38-51mm; ES 2D/4D; hydrophilic durable; ATB bonding; no oven temp increase. [K3] [M1] [K2]|Fixed across all runs: 50gsm(25+25); profiled 3.0D, 38-51mm; ES 2D/4D; hydrophilic durable; ATB bonding; no oven temp increase. [K3] [M1] [K2]|Fixed across all runs: 50gsm(25+25); profiled 3.0D, 38-51mm; ES 2D/4D; hydrophilic durable; ATB bonding; no oven temp increase. [K3] [M1] [K2]|Fixed across all runs: 50gsm(25+25); profiled 3.0D, 38-51mm; ES 2D/4D; hydrophilic durable; ATB bonding; no oven temp increase. [K3] [M1] [K2]|Fixed across all runs: 50gsm(25+25); profiled 3.0D, 38-51mm; ES 2D/4D; hydrophilic durable; ATB bonding; no oven temp increase. [K3] [M1] [K2]|Fixed across all runs: 50gsm(25+25); profiled 3.0D, 38-51mm; ES 2D/4D; hydrophilic durable; ATB bonding; no oven temp increase. [K3] [M1] [K2]|Fixed across all runs: 50gsm(25+25); profiled 3.0D, 38-51mm; ES 2D/4D; hydrophilic durable; ATB bonding; no oven temp increase. [K3] [M1] [K2]|Fixed across all runs: 50gsm(25+25); profiled 3.0D, 38-51mm; ES 2D/4D; hydrophilic durable; ATB bonding; no oven temp increase. [K3] [M1] [K2]|Fixed across all runs: 50gsm(25+25); profiled 3.0D, 38-51mm; ES 2D/4D; hydrophilic durable; ATB bonding; no oven temp increase. [K3] [M1] [K2]|Fixed across all runs: 50gsm(25+25); profiled 3.0D, 38-51mm; ES 2D/4D; hydrophilic durable; ATB bonding; no oven temp increase. [K3] [M1] [K2]|Fixed across all runs: 50gsm(25+25); profiled 3.0D, 38-51mm; ES 2D/4D; hydrophilic durable; ATB bonding; no oven temp increase. [K3] [M1] [K2]|Fixed across all runs: 50gsm(25+25); profiled 3.0D, 38-51mm; ES 2D/4D; hydrophilic durable; ATB bonding; no oven temp increase. [K3] [M1] [K2]|Fixed across all runs: 50gsm(25+25); profiled 3.0D, 38-51mm; ES 2D/4D; hydrophilic durable; ATB bonding; no oven temp increase. [K3] [M1] [K2]||
|Run ID|Stage|Block|Config (X1)|Top Layer Detail|Bot Layer Detail|Temp X2|Load X3|STT 1st(s)|Rewet(g)|MD spread%|Wet tensile(N/m)|Cost delta%|Notes||
|A00|Anchor|-|C1 Optimal|10% Lyocell(tri)+90% ES|50% Fudi+50% own ES|128C|Medium|—|||||—|Baseline anchor [M1]|
|S01|1-Screen|A|C1|Optimal (Lyocell)|2D 10% Lenzing Lyocell(trilobal)+90%ES|50% Fudi ES+50% own ES|128C|Medium|||||||
|S02|1-Screen|A|C1|Optimal (Lyocell)|2D 10% Lenzing Lyocell(trilobal)+90%ES|50% Fudi ES+50% own ES|130C|Medium|||||||
|S03|1-Screen|B|C4|Cross PET|10% 1.5D 4D cross PET+90%2D ES|50% 3D Fudi+50% 4D own ES|128C|Medium|||||||
|S04|1-Screen|B|C3|Suzhou (Spindle)|10% 3.5D Suzhou mono-PET+90%2D ES|50% 3D Fudi+50% 4D own ES|128C|Medium|||||||
|S05|1-Screen|A|C2|Alternative (Fudi)|3D 10% Fudi trilobal ES+90%2D ES|50% 3D Fudi+50% 4D own ES|126C|Medium|||||||
|S06|1-Screen|A|C2|Alternative (Fudi)|3D 10% Fudi trilobal ES+90%2D ES|50% 3D Fudi+50% 4D own ES|128C|Medium|||||||
|S07|1-Screen|B|C3|Suzhou (Spindle)|10% 3.5D Suzhou mono-PET+90%2D ES|50% 3D Fudi+50% 4D own ES|126C|Medium|||||||
|S08|1-Screen|C|C1-center|C1 center|10% Lyocell+90%ES|50% Fudi+50% own ES|128C|Medium||||||Center|
|S09|1-Screen|C|C1-center|C1 center|10% Lyocell+90%ES|50% Fudi+50% own ES|128C|Medium||||||Center|
|S10|1-Screen|A|C1|Optimal (Lyocell)|2D 10% Lenzing Lyocell(trilobal)+90%ES|50% Fudi ES+50% own ES|126C|Medium|||||||
|S11|1-Screen|B|C3|Suzhou (Spindle)|10% 3.5D Suzhou mono-PET+90%2D ES|50% 3D Fudi+50% 4D own ES|130C|Medium|||||||
|S12|1-Screen|B|C4|Cross PET|10% 1.5D 4D cross PET+90%2D ES|50% 3D Fudi+50% 4D own ES|126C|Medium|||||||
|S13|1-Screen|C|C1-center|C1 center|10% Lyocell+90%ES|50% Fudi+50% own ES|128C|Medium||||||Center|
|S14|1-Screen|A|C2|Alternative (Fudi)|3D 10% Fudi trilobal ES+90%2D ES|50% 3D Fudi+50% 4D own ES|130C|Medium|||||||
|S15|1-Screen|B|C4|Cross PET|10% 1.5D 4D cross PET+90%2D ES|50% 3D Fudi+50% 4D own ES|130C|Medium|||||||
|Stage 2 - Temperature × Loading Optimization: top-2 configs from Stage 1 × 3 temps × 2 loads. Block A=C_top1, Block B=C_top2.|Stage 2 - Temperature × Loading Optimization: top-2 configs from Stage 1 × 3 temps × 2 loads. Block A=C_top1, Block B=C_top2.|Stage 2 - Temperature × Loading Optimization: top-2 configs from Stage 1 × 3 temps × 2 loads. Block A=C_top1, Block B=C_top2.|Stage 2 - Temperature × Loading Optimization: top-2 configs from Stage 1 × 3 temps × 2 loads. Block A=C_top1, Block B=C_top2.|Stage 2 - Temperature × Loading Optimization: top-2 configs from Stage 1 × 3 temps × 2 loads. Block A=C_top1, Block B=C_top2.|Stage 2 - Temperature × Loading Optimization: top-2 configs from Stage 1 × 3 temps × 2 loads. Block A=C_top1, Block B=C_top2.|Stage 2 - Temperature × Loading Optimization: top-2 configs from Stage 1 × 3 temps × 2 loads. Block A=C_top1, Block B=C_top2.|Stage 2 - Temperature × Loading Optimization: top-2 configs from Stage 1 × 3 temps × 2 loads. Block A=C_top1, Block B=C_top2.|Stage 2 - Temperature × Loading Optimization: top-2 configs from Stage 1 × 3 temps × 2 loads. Block A=C_top1, Block B=C_top2.|Stage 2 - Temperature × Loading Optimization: top-2 configs from Stage 1 × 3 temps × 2 loads. Block A=C_top1, Block B=C_top2.|Stage 2 - Temperature × Loading Optimization: top-2 configs from Stage 1 × 3 temps × 2 loads. Block A=C_top1, Block B=C_top2.|Stage 2 - Temperature × Loading Optimization: top-2 configs from Stage 1 × 3 temps × 2 loads. Block A=C_top1, Block B=C_top2.|Stage 2 - Temperature × Loading Optimization: top-2 configs from Stage 1 × 3 temps × 2 loads. Block A=C_top1, Block B=C_top2.|Stage 2 - Temperature × Loading Optimization: top-2 configs from Stage 1 × 3 temps × 2 loads. Block A=C_top1, Block B=C_top2.||
|O01|2-Opt|B|C3|Suzhou (Spindle)|10% 3.5D Suzhou mono-PET+90%2D ES|50% 3D Fudi+50% 4D own ES|128C|High|||||||
|O02|2-Opt|B|C3|Suzhou (Spindle)|10% 3.5D Suzhou mono-PET+90%2D ES|50% 3D Fudi+50% 4D own ES|126C|High|||||||
|O03|2-Opt|B|C3|Suzhou (Spindle)|10% 3.5D Suzhou mono-PET+90%2D ES|50% 3D Fudi+50% 4D own ES|128C|Low|||||||
|O04|2-Opt|A|C1|Optimal (Lyocell)|2D 10% Lenzing Lyocell(trilobal)+90%ES|50% Fudi ES+50% own ES|126C|High|||||||
|O05|2-Opt|C|C1-center|C1 center|10% Lyocell+90%ES|50% Fudi+50% own ES|128C|Medium||||||Center|
|O06|2-Opt|B|C3|Suzhou (Spindle)|10% 3.5D Suzhou mono-PET+90%2D ES|50% 3D Fudi+50% 4D own ES|126C|Low|||||||
|O07|2-Opt|A|C1|Optimal (Lyocell)|2D 10% Lenzing Lyocell(trilobal)+90%ES|50% Fudi ES+50% own ES|130C|High|||||||
|O08|2-Opt|B|C3|Suzhou (Spindle)|10% 3.5D Suzhou mono-PET+90%2D ES|50% 3D Fudi+50% 4D own ES|130C|Low|||||||
|O09|2-Opt|B|C3|Suzhou (Spindle)|10% 3.5D Suzhou mono-PET+90%2D ES|50% 3D Fudi+50% 4D own ES|130C|High|||||||
|O10|2-Opt|C|C1-center|C1 center|10% Lyocell+90%ES|50% Fudi+50% own ES|128C|Medium||||||Center|
|O11|2-Opt|A|C1|Optimal (Lyocell)|2D 10% Lenzing Lyocell(trilobal)+90%ES|50% Fudi ES+50% own ES|128C|Low|||||||
|O12|2-Opt|A|C1|Optimal (Lyocell)|2D 10% Lenzing Lyocell(trilobal)+90%ES|50% Fudi ES+50% own ES|128C|High|||||||
|O13|2-Opt|A|C1|Optimal (Lyocell)|2D 10% Lenzing Lyocell(trilobal)+90%ES|50% Fudi ES+50% own ES|126C|Low|||||||
|O14|2-Opt|A|C1|Optimal (Lyocell)|2D 10% Lenzing Lyocell(trilobal)+90%ES|50% Fudi ES+50% own ES|130C|Low|||||||
|Stage 3 - Confirmation (top-2 candidates × 2 replicates each, diaper bench).|Stage 3 - Confirmation (top-2 candidates × 2 replicates each, diaper bench).|Stage 3 - Confirmation (top-2 candidates × 2 replicates each, diaper bench).|Stage 3 - Confirmation (top-2 candidates × 2 replicates each, diaper bench).|Stage 3 - Confirmation (top-2 candidates × 2 replicates each, diaper bench).|Stage 3 - Confirmation (top-2 candidates × 2 replicates each, diaper bench).|Stage 3 - Confirmation (top-2 candidates × 2 replicates each, diaper bench).|Stage 3 - Confirmation (top-2 candidates × 2 replicates each, diaper bench).|Stage 3 - Confirmation (top-2 candidates × 2 replicates each, diaper bench).|Stage 3 - Confirmation (top-2 candidates × 2 replicates each, diaper bench).|Stage 3 - Confirmation (top-2 candidates × 2 replicates each, diaper bench).|Stage 3 - Confirmation (top-2 candidates × 2 replicates each, diaper bench).|Stage 3 - Confirmation (top-2 candidates × 2 replicates each, diaper bench).|Stage 3 - Confirmation (top-2 candidates × 2 replicates each, diaper bench).||
|F01|3-Confirm|A|C1 (or C3)|Optimal/Suzhou TBD|TBD|128C|Medium|||||||Replicate #1|
|F02|3-Confirm|A|C1 (or C3)|Optimal/Suzhou TBD|TBD|128C|Medium|||||||Replicate #2|
|F03|3-Confirm|B|C3 (or C1)|Suzhou/Optimal TBD|TBD|128C|Medium|||||||Replicate #1|
|F04|3-Confirm|B|C3 (or C1)|Suzhou/Optimal TBD|TBD|128C|Medium|||||||Replicate #2|

[Protocol_Characterization:Characterization &amp; Acceptance Metrics]
|v3: PRIMARY = finished-diaper enterprise standard. Material-level = SCREENING.|v3: PRIMARY = finished-diaper enterprise standard. Material-level = SCREENING.|v3: PRIMARY = finished-diaper enterprise standard. Material-level = SCREENING.|v3: PRIMARY = finished-diaper enterprise standard. Material-level = SCREENING.|v3: PRIMARY = finished-diaper enterprise standard. Material-level = SCREENING.|v3: PRIMARY = finished-diaper enterprise standard. Material-level = SCREENING.|v3: PRIMARY = finished-diaper enterprise standard. Material-level = SCREENING.|
|---|---|---|---|---|---|---|
|PRIMARY: final pass/fail = finished-diaper enterprise standard (rows 1-4). Material-level (rows 5-17) = screening gate only.|PRIMARY: final pass/fail = finished-diaper enterprise standard (rows 1-4). Material-level (rows 5-17) = screening gate only.|PRIMARY: final pass/fail = finished-diaper enterprise standard (rows 1-4). Material-level (rows 5-17) = screening gate only.|PRIMARY: final pass/fail = finished-diaper enterprise standard (rows 1-4). Material-level (rows 5-17) = screening gate only.|PRIMARY: final pass/fail = finished-diaper enterprise standard (rows 1-4). Material-level (rows 5-17) = screening gate only.|PRIMARY: final pass/fail = finished-diaper enterprise standard (rows 1-4). Material-level (rows 5-17) = screening gate only.|PRIMARY: final pass/fail = finished-diaper enterprise standard (rows 1-4). Material-level (rows 5-17) = screening gate only.|
|#|Metric|Level|Acceptance Threshold / Target|Standard|Test Method|Notes|
|1|Re-wet (finished diaper)|PRIMARY|&lt;5.9g @0.5kPa + 2insults|Enterprise low-load multi|Enterprise SOP [K7/K8]|Final gate|
|2|Core stain uniformity|PRIMARY|Visual grade &gt;=A (no white spots)|Enterprise|Visual + dye method|Final gate|
|3|SAP utilization|PRIMARY|&gt;=63% (vs v11 63.6% anchor)|Enterprise|Wet-core gravimetric|Final gate|
|4|Wet tensile (finished diaper)|PRIMARY|&gt;=75N/m (from 58N/m)|Enterprise|Pantograph tensile|Final gate|
|5|Surface transfer time (STT)|Screen|&lt;=0.8s|GB/T 11044 (ref)|Water drop|Material gate|
|6|3rd rewet amount|Screen|&lt;=0.5g (target 0.30g)|GB/T 13662-1992|0.5kPa multi-insult [K8]|Material gate|
|7|MD liquid spread|Screen|&gt;=34% (anchor 34.9%)|GB/T 8939-2008|Spread measurement|Material gate|
|8|Wet tensile (sheet)|Screen|&gt;=75N/m|GB/T 13663-1992|Pantograph|Material gate|
|9|Caliper retention|Screen|&gt;=92% vs control (CoPET loss&gt;=8% kills ADL)|GB/T 13663-1992|Microtome / caliper gauge|Flattening check|
|10|Softness TS7|Screen|&gt;=50 (TS7 method, higher=softer)|EDANA 801.1-02|TS7 softness|Material gate|
|11|Fuzz score|Screen|&lt;=2 (0-3 scale; &gt;~15% profiled = fuzz risk)|GB/T 8939-2008|Visual+weight|Material gate|
|12|CD/MD drape|Screen|D_aniso&gt;=2.5 (optimal=3)|GB/T 8939-2008|Drape test|Material gate|
|13|Surface morphology|Screen|SEM/microscope: no flow, intact trilobal|—|SEM/microscope|Flattening verification|
|14|Bacterial retention|Screen|None|GB/T 15979-2002|Microbial|Hygiene|
|15|Permeability|Screen|Not worse than control|GB/T 13663-1992|Air flow|Material gate|
|16|Tensile wet strength (sheet)|Screen|&gt;=70N/m|GB/T 13663-1992|Pantograph|Material gate|
|17|Bonding strength|Screen|&gt;=10N/cm|GB/T 14522-2008|Peel test|Strength vs flattening balance [Key!]|

[Plan_Schedule:Test Plan - Schedule &amp; Milestones]
|v3: 14-week plan (W1-W14). DOE 33 runs in 3 stages.|v3: 14-week plan (W1-W14). DOE 33 runs in 3 stages.|v3: 14-week plan (W1-W14). DOE 33 runs in 3 stages.|v3: 14-week plan (W1-W14). DOE 33 runs in 3 stages.|v3: 14-week plan (W1-W14). DOE 33 runs in 3 stages.|v3: 14-week plan (W1-W14). DOE 33 runs in 3 stages.|v3: 14-week plan (W1-W14). DOE 33 runs in 3 stages.||
|---|---|---|---|---|---|---|---|
|All dates from 2026-08-17 (Mon). Milestones in bold with DDL.|All dates from 2026-08-17 (Mon). Milestones in bold with DDL.|All dates from 2026-08-17 (Mon). Milestones in bold with DDL.|All dates from 2026-08-17 (Mon). Milestones in bold with DDL.|All dates from 2026-08-17 (Mon). Milestones in bold with DDL.|All dates from 2026-08-17 (Mon). Milestones in bold with DDL.|All dates from 2026-08-17 (Mon). Milestones in bold with DDL.||
|Item|Phase / Activity|Owner|Duration|Start|End|Deliverable||
|W1|Phase 0: Kickoff &amp; Spec Finalization|Spec freeze, config definitions, SOP alignment|Project Lead|2w|W1|W2|Spec doc v1.0; SOP sign-off|
|W2|M1: DOE Design &amp; Randomization Frozen|Randomized 33-run DOE frozen; randomization verified|Statistical Lead|1w|W2|W2|DOE matrix frozen; random seed documented|
|W3|Phase 1: Stage 1 Screen — Block A (C1+C2)|Run 6 runs: C1×3T + C2×3T at Medium load|Lab Team A|3w|W3|W5|6 runs completed; raw data logged|
|W5|M2: Stage 1 Block A Interim|C1 vs C2 preliminary ranking; C1 should lead on rewet|Lab Team A|1w|W5|W5|Interim report Block A|
|W6|Phase 1 continued: Block B (C3+C4)|Run 4 runs: C3×3T + C4×3T at Medium load|Lab Team B|1w|W6|W6|4 runs completed|
|W6|M3: QQV6 Sign-off &amp; Center Runs|Block C (3 centers) + QQV6 sign-off from Angela|Lab Team A+B|1w|W6|W6|9 total runs done; QQV6 approved|
|W7|Phase 1.5: Stage 1 Summary &amp; Top-2 Selection|Analyze Stage 1 data; select top-2 configs for Stage 2|Statistical Lead|2w|W7|W8|Top-2 config identified|
|W8|M4: Stage 1 Complete &amp; Stage 2 Ready|Stage 1 report; Stage 2 temp-load design finalized|Project Lead|1w|W8|W8|Stage 1 report; S2 design frozen|
|W9|Phase 2: Stage 2 Block A (top config #1)|6 runs: 3T × 2L for config #1|Lab Team A|3w|W9|W11|6 runs done; temp-load curve|
|W11|M5: Stage 2 Block B Interim|6 runs: 3T × 2L for config #2; 2 center runs|Lab Team B|1w|W11|W11|12+2 runs done; cost data collected|
|W12|Phase 3: Stage 3 Confirmation|Top-2 candidates × 2 replicates each (diaper bench)|Lab Team A+B|2w|W12|W13|4 confirmation runs|
|W13|M6: Stage 3 Complete|Confirmation data compiled; statistical significance|Statistical Lead|1w|W13|W13|Confirmation report|
|W14|Phase 4: Final Report &amp; Supplier Selection|Final report; cost-benefit analysis; Angela sign-off|Project Lead|2w|W14|W14|Final report; patent draft [M7]|
|W14|M7: Final Sign-off|Top-1 config selected; patent draft filed; Angela approval|Angela|—|W14|W14|Final sign-off; go/no-go|

[Risk_Resources:Risk &amp; Resource Plan]
|v3: Risk register + resource allocation + budget estimate.|v3: Risk register + resource allocation + budget estimate.|v3: Risk register + resource allocation + budget estimate.|v3: Risk register + resource allocation + budget estimate.|v3: Risk register + resource allocation + budget estimate.|
|---|---|---|---|---|
|Budget (RMB) based on Suzhou 100kg/mo, Fudi 200kg/mo trial volumes.|Budget (RMB) based on Suzhou 100kg/mo, Fudi 200kg/mo trial volumes.|Budget (RMB) based on Suzhou 100kg/mo, Fudi 200kg/mo trial volumes.|Budget (RMB) based on Suzhou 100kg/mo, Fudi 200kg/mo trial volumes.|Budget (RMB) based on Suzhou 100kg/mo, Fudi 200kg/mo trial volumes.|
|#|Risk / Resource|Description|Impact|Mitigation / Budget|
|1. RISK REGISTER|1. RISK REGISTER|1. RISK REGISTER|1. RISK REGISTER|1. RISK REGISTER|
|1|Cross PET skin roughness|C4 may fail skin-feel screen early|Medium|Pre-test sensory panel; have C3 as backup|
|2|Suzhou Yimeng lead time|New supplier; qualification may take 4-6wk|High|Start qualification in W1; parallel Fudi supply|
|3|PE sheath flattening|130C may round off trilobal shape → surface area loss|High|Monitor caliper+microscope; keep 126-128C as safe zone|
|4|Oven Delta-T variation|Oven +/2C across positions; affects temp reproducibility|Medium|Calibrate 3 positions before each run; assign fixed positions|
|5|Lyocell cost premium|C1 may exceed 20% cost threshold|Medium|Target &lt;=15%; negotiate Lenzing volume pricing|
|6|Bonding strength loss|PET sheath = all bonding on ES; may drop below 10N/cm|Medium|Monitor peel test; if &lt;10N/cm reduce loading|
|7|Supplier qualification delay|Fudi or Suzhou delayed|Medium|Dual source; buffer 2wk in schedule|
|8|Data noise / no clear winner|Top-2 configs too close to distinguish|Low|Add 2 replicates in Stage 3; statistical power check|
|9|Patent IP exposure|Relational formula may disclose IP|Medium|Patent drafted by 徒弟 (1st inventor) + 杰瑞 before publication|
|10|C4 cross PET rejected|Skin roughness eliminates C4 → only 3 configs valid|Low|Plan assumes C3 as 3rd viable; no impact on outcome|
|2. RESOURCES|2. RESOURCES|2. RESOURCES|2. RESOURCES|2. RESOURCES|
|R1|Personnel|Project Lead (1), Lab Team A (2), Lab Team B (2), Statistical Lead (1), Angela (approver),  (patent)|—|Internal|
|R2|Equipment|Suzhou pilot line, caliper gauge, pantograph, TS7 softness, SEM/microscope, oven (3 positions)|—|Internal|
|R3|Materials — C1|Lenzing Lyocell 100kg/mo; ES 200kg/mo|—|~¥30,000/mo [TBD]|
|R4|Materials — C2|Fudi trilobal ES 200kg/mo; ES 200kg/mo|—|~¥22,000/mo [TBD]|
|R5|Materials — C3|Suzhou mono-PET 100kg/mo; ES 200kg/mo|—|~¥18,000/mo [TBD]|
|R6|Materials — C4|Cross PET 100kg/mo; ES 200kg/mo|—|~¥20,000/mo [TBD]|
|R7|Testing services|External lab (SEM, drape): ~¥15,000|—|~¥15,000|
|R8|Misc|Consumables, sample shipping, data tools|—|~¥5,000|
|—|TOTAL BUDGET ESTIMATE|All materials + testing + misc for 3-stage DOE|—|~¥115,000-150,000 [TBD]|
|3. KEY ASSUMPTIONS FOR BUDGET|3. KEY ASSUMPTIONS FOR BUDGET|3. KEY ASSUMPTIONS FOR BUDGET|3. KEY ASSUMPTIONS FOR BUDGET|3. KEY ASSUMPTIONS FOR BUDGET|
|1|Trial volumes|100kg/mo Suzhou + 200kg/mo Fudi across 4wk (W3-W6 + W9-W11)|—|—|
|2|No pilot line retooling|Assumes pilot line available; no capex|—|—|
|3|Material cost|Based on market quotes; final quotes TBD from suppliers|—|TBD|
|4|Internal labor|Not included in budget (allocated by R&amp;D cost center)|—|—|

[Gantt_Chart:Gantt Chart - Test Plan (W1-W14)]
|v3: 4-phase plan across 14 weeks. Green=Phase bar; Gold=Milestone.|v3: 4-phase plan across 14 weeks. Green=Phase bar; Gold=Milestone.|v3: 4-phase plan across 14 weeks. Green=Phase bar; Gold=Milestone.|v3: 4-phase plan across 14 weeks. Green=Phase bar; Gold=Milestone.|v3: 4-phase plan across 14 weeks. Green=Phase bar; Gold=Milestone.|v3: 4-phase plan across 14 weeks. Green=Phase bar; Gold=Milestone.|v3: 4-phase plan across 14 weeks. Green=Phase bar; Gold=Milestone.|v3: 4-phase plan across 14 weeks. Green=Phase bar; Gold=Milestone.|v3: 4-phase plan across 14 weeks. Green=Phase bar; Gold=Milestone.|v3: 4-phase plan across 14 weeks. Green=Phase bar; Gold=Milestone.|v3: 4-phase plan across 14 weeks. Green=Phase bar; Gold=Milestone.|v3: 4-phase plan across 14 weeks. Green=Phase bar; Gold=Milestone.|v3: 4-phase plan across 14 weeks. Green=Phase bar; Gold=Milestone.|v3: 4-phase plan across 14 weeks. Green=Phase bar; Gold=Milestone.|v3: 4-phase plan across 14 weeks. Green=Phase bar; Gold=Milestone.|v3: 4-phase plan across 14 weeks. Green=Phase bar; Gold=Milestone.|v3: 4-phase plan across 14 weeks. Green=Phase bar; Gold=Milestone.|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Wk|Task / Owner|W1|W2|W3|W4|W5|W6|W7|W8|W9|W10|W11|W12|W13|W14||
|1|Phase 0: Kickoff &amp; Spec
(Project Lead)|||||||||||||||Spec freeze, SOP sign-off|
|2|M1: DOE Frozen
(Stat Lead)||◆|||||||||||||33-run DOE randomized|
|3|Phase 1: Stage1 Block A (C1+C2)
(Lab A)|||||||||||||||6 runs, 3T × Medium|
|4|M2: Block A Interim
(Lab A)|||||◆||||||||||C1 vs C2 ranking|
|5|Phase 1: Block B (C3+C4)
(Lab B)|||||||||||||||4 runs, 3T × Medium|
|6|M3: QQV6 Sign-off
(Angela)||||||◆|||||||||9 runs done; center runs|
|7|Phase 1.5: Stage1 Summary
(Stat Lead)|||||||||||||||Top-2 selection|
|8|M4: Stage1 Complete
(Project Lead)||||||||◆|||||||S2 design frozen|
|9|Phase 2: Stage2 Block A (#1)
(Lab A)|||||||||||||||3T × 2L, 6 runs|
|10|M5: Block B Interim
(Lab B)|||||||||||◆||||12+2 runs done|
|11|Phase 3: Stage3 Confirm
(Lab A+B)|||||||||||||||Top-2 × 2 reps|
|12|M6: Stage3 Complete
(Stat Lead)|||||||||||||◆||Confirmation report|
|13|Phase 4: Final Report
(Project Lead)|||||||||||||||Report + patent draft|
|14|M7: Final Sign-off
(Angela)||||||||||||||◆|Top-1 selected; go/no-go|
||||||||||||||||||
||Legend:|||#NAME?|||◆ = Milestone||Green bar = Phase 0-1 (Screen)||||||||
||||||||||Blue bar  = Phase 2-4 (Opt/Confirm/Report)||||||||
||||||||||Gold ◆    = Key milestone (M1-M7)||||||||

