import json, os

base = "E:/WKB-OB"

def w(dst, ce):
    full = os.path.join(base, dst)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    content = json.loads('"' + ce + '"')
    with open(full, "w", encoding="utf-8", newline="") as f:
        f.write(content)
    print(f"OK: {os.path.basename(dst)[:30]} ({len(content)} chars)")

# Item 5: 温变湿变微胶囊
w(
    "RAW_FULL/ima_sync/WKB/Resources/Open Innovation/Material/X-Chromic/温变湿变微胶囊技术参数对比表.xlsx.md",
    r'''[温变 vs 湿变微胶囊对比:温变 / 湿变油墨微胶囊 — 核心技术参数对比表]
|数据来源：公开技术文献、厂商Datasheet、行业报告  |  编制日期：2026-06-18||||
|---|---|---|---|
|序号|参数维度|温变油墨微胶囊 (Thermochromic)|湿变油墨微胶囊 (Hydrochromic)|
|1|触发条件|温度变化（-10°C ~ 150°C 可选）
常用：15°C / 31°C / 37°C / 45°C / 65°C
可定制 ±0.5°C 精度|水分 / 湿气接触（遇水、遇尿即刻变色）
对高环境湿度（>85% RH）敏感|
|2|反应机理|隐色染料（Leuco Dye）+ 显色剂 + 相变溶剂
温度改变 → 溶剂熔融/凝固 → 电子转移
或晶体结构变化 → 颜色可逆变化|微胶囊内含遇水变色染料或光学活性物质
水分穿透/破坏胶囊壁或引发化学反应
导致颜色变化（多为 Yellow→Blue 体系）|
|3|微胶囊粒径|丝印/移印级：1 ~ 10 μm
凹印/柔版级：< 5 μm（需窄分布）
粒径 CV（变异系数）：国际 ≤ 15%，国内 ~ 30%|主流：2 ~ 15 μm
更小粒径挑战包覆率
粒径均匀性直接影响响应一致性|
|4|壁材类型 (Shell)|三聚氰胺-甲醛树脂（MF）✅ 主流
聚脲（Polyurea）✅ 高端
聚氨酯、聚丙烯酸酯
蜜胺树脂|三聚氰胺-甲醛树脂（MF）
聚脲（Polyurea）
聚丙烯酸酯
壁材亲水性需精确调控|
|5|芯材类型 (Core)|隐色染料（CVL/荧光烷类）+ 双酚A类显色剂
+ 脂肪醇/酯类相变溶剂
高端染料依赖进口（日本NCB、山田化学）|遇水变色染料（pH敏感染料/络合物）
或光学变化材料
配方相对单一，专利壁垒集中|
|6|可逆性|✅ 可逆（主流，数千至数万次循环）
❌ 不可逆（一次性高温指示/消毒标签）|✅ 可逆（干燥恢复原色，Ledio 宣称 >5000次）
❌ 不可逆（一次性尿显指示为主流）|
|7|响应时间|0.5 ~ 5 秒（取决于温差和基材导热）
金属/玻璃 < 1 秒
纸张/塑料 2 ~ 5 秒|0.1 ~ 1 秒（遇水即刻变色）
对微量 urine 也有快速响应|
|8|循环寿命|标准 1,000 ~ 5,000 次
高端（Matsui/CTI）> 10,000 次
最高可达 50,000 次（聚脲壁材）|可逆型：数千次（Ledio 宣称 >5,000次）
不可逆型：一次性
壁材疲劳是寿命瓶颈|
|9|变色温度/条件精度|±0.5 ~ 1°C（医用/高端）
±2 ~ 3°C（常规）
±5 ~ 8°C（超高温 80°C+）|不适用
（湿度阈值控制，无温度参数）
对环境湿度敏感需密封包装|
|10|颜色变化模式|有色 ↔ 无色（主流）
有色 A ↔ 有色 B
多色阶段变化（液晶型）
ΔE > 30 为清晰可见|黄色 → 蓝色（CTI 经典体系）
白色 → 透明
有色 ↔ 无色
可选颜色范围较窄|
|11|印刷工艺适配|丝印 ✅
移印 ✅
凹印 ⚠️（需专用分散液，<5μm）
柔印 ⚠️
最优涂布厚度：5~10μm|丝印 ✅
移印 ✅
凹印 ⚠️（粒径和粘度挑战大）
柔印 ⚠️
纸尿裤产线多采用溶剂型凹印|
|12|耐候性 / 储存寿命|中：需添加 UV 稳定剂
高温/强 UV 下寿命缩短
仓储：室温 1~3 月（国内）vs 12~24 月（CTI/Matsui）|低：对湿气/水分极其敏感
需严格密封储存（防潮包装）
生产过程中需避开水汽接触|
|13|包覆率 (Encapsulation)|行业平均 75~85%（国内）
高端 ≥ 92%（国际）
包覆率低 → 有效成分泄漏 → 批次报废|包覆率要求极高
水分提前渗入即失效
工艺难度高于温变|
|14|成本估算（元/kg）|200 ~ 800（国内常规）
800 ~ 1,500+（进口高端）
价格受染料成本波动影响大|300 ~ 800（国内，如广州乐迪）
800 ~ 2,000+（进口，CTI）
壁材/工艺要求更高，成本偏贵|
|15|全球标杆供应商|• CTI（美国）— 全球最大温变油墨商
• Matsui Shikiso Chemical（日本）— 高端
• LCR Hallcrest（英国）— 液晶温变
• Marabu（德国）— 油墨整体方案|• CTI（美国）— 湿变油墨全球霸主
  专利Yellow→Blue体系
• Microcapsule Pigment（韩国）
• SUNREE（中国）— 尿显胶方案|
|16|国内主要厂商|• 千色变（深圳）— 配方/应用
• 景艺姿 — 感温变色粉
• 侨盛新材料 — 温变/光变微胶囊
• 兴发集团（2023布局2200t/a）
⚠️ 多数以配方和应用为主，基础微胶囊技术仍落后|• 广州乐迪新材料 — 国内先行者
  可缓白遇水变透明/黄色变蓝色
• 心茉新材料（起步阶段）
• SUNREE — 尿显指示胶
⚠️ 起步阶段，尚无大规模量产能力|
|🔬 关键技术难点详解||||
|【温变微胶囊 — 三大核心壁垒】||||
||1. 粒径均匀性控制|||
||凹版/柔版印刷要求粒径 < 5 μm，且 > 90% 在目标区间内。需要高精度乳化+分级设备，批间 CV 需 ≤ 15%。
国内现状：大多落在 3~15 μm，批间 CV ~30%，导致印刷一致性差。|||
||2. 壁材强度 vs 薄度平衡|||
||壁材需足够坚韧抵抗印刷剪切力（丝印/凹印），同时要尽可能薄（100~200 nm）以保证灵敏传热。
高端路线：聚脲/聚氨酯体系 → 无甲醛 + 耐疲劳 + 薄壁高强。|||
||3. 耐候性 / UV稳定性|||
||核心隐色染料对 UV 和氧化敏感，需添加 UV 吸收剂和抗氧化剂。
保质期是区分国内外厂商的关键指标：国内 1~3 月 vs 国际 12~24 月。|||
|【湿变微胶囊 — 三大核心壁垒】||||
||1. 水分响应灵敏度与选择性|||
||需要在 0.1~0.5 秒内对微量水分（如尿液）做出明确显色响应，
但不能被环境高湿度（<85% RH）错误触发。壁材亲水性需精确到分子级调控。|||
||2. 包覆率与储存稳定性|||
||胶囊必须从生产→运输→储存→使用前始终保持绝对密封。
水分子极小（~0.28 nm），对壁材致密性要求远高于温变微胶囊。|||
||3. 应用场景局限|||
||遇水变色特性使其主要用于一次性尿显指示和防伪，市场规模远小于温变。
CTI 在此领域几乎垄断，国内厂商处于起步阶段。|||
|📋 典型应用场景||||
||温变微胶囊|湿变微胶囊|关键要求|
|纸尿裤/成人失禁裤|温度指示（体温联动）|✅ 尿显指示（核心应用）|响应快、无毒、耐摩擦|
|奶瓶/水杯温度指示|✅ 45°C 安全警示|—|食品接触安全认证|
|冷链物流标签|✅ -5°C / 0°C 指示|—|精度 ±1°C|
|防伪包装|✅ 触摸变色验证|✅ 水感变色验证|不可逆、颜色对比鲜明|
|智能纺织品|✅ 31°C 体感变色印花|—|耐水洗 > 50 次|
|医疗体温监测|✅ 37°C 发烧指示|—|精度 ±0.5°C|
|工业超温预警|✅ 65°C ~ 134°C|—|不可逆、耐高温|
|⚠️ 说明：以上数据基于公开技术文献、厂商Datasheet及行业报告整理，具体参数因品牌/型号/批次不同可能存在差异。||||


[供应商与成本对比:温变 / 湿变微胶囊 — 供应商与成本对比]
|序号|供应商|地区|品类|核心优势 / 备注|
|---|---|---|---|---|
|1|CTI (Chromatic Technologies Inc.)|美国 科罗拉多|温变 + 湿变|全球最大温变/湿变油墨生产商
ISO 9001 认证
自有专利水基分散体系
湿变 Y→B 体系全球垄断|
|2|Matsui Shikiso Chemical|日本 京都|温变（高端）|高端温变标杆
循环寿命 > 10,000 次
颜色鲜艳度行业第一|
|3|LCR Hallcrest|英国|温变（液晶型）|液晶温变领域领导者
精度 ±0.5°C
成本高，用于高端医疗/防伪|
|4|Marabu|德国|温变油墨方案|油墨整体方案供应商
印刷适配性优异
欧洲市场份额领先|
|5|Microcapsule Pigment (Daehyun)|韩国|温变 + 湿变|韩国本土微胶囊供应商
品类齐全（温变/光变/湿变/芳香）
中等价位|
|6|广州乐迪新材料|中国 广州|湿变 / 水溶油墨|国内湿变微胶囊先行者
可逆白色变透明系列
纸尿裤专用水溶油墨
宣称 >5000 次循环|
|7|千色变|中国 深圳|温变（配方/应用）|国内温变油墨应用层龙头
以色浆/成品油墨为主
基础微胶囊外购|
|8|景艺姿|中国|温变（感温变色粉）|感温变色粉/颜料供应商
价格优势明显
品质稳定性有待提升|
|9|侨盛新材料|中国|温变 + 光变微胶囊|兴发集团关联企业
布局 2200t/a 微胶囊项目
包括 200t/a 光变/温变胶囊粉|
|10|SUNREE|中国 福建|湿变（尿显胶）|尿显指示胶专业供应商
与卫品产线直接适配
性价比方案|
|💰 成本区间总结（元 / kg微胶囊粉）|||||
||品类|国内厂商|国际厂商|备注|
|1|温变微胶囊（常规）|200 ~ 500 元/kg|500 ~ 1,000 元/kg|品质差异主要在循环寿命和粒径分布|
|2|温变微胶囊（高端）|500 ~ 800 元/kg|1,000 ~ 1,500+ 元/kg|Matsui/CTI 品牌溢价|
|3|湿变微胶囊|300 ~ 800 元/kg|800 ~ 2,000+ 元/kg|工艺难度更高，CTI 垄断溢价|
|4|温变油墨（成品）|150 ~ 400 元/kg|300 ~ 800 元/kg|含溶剂/树脂载体|
'''
)

# Item 2: SAP_Three_Way_Design_Comparison
w(
    "RAW_FULL/ima_sync/WKB/Resources/Open Innovation/Material/SAM/SAP_Three_Way_Design_Comparison.pptx.md",
    r'''8
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
'''
)
