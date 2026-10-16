---
type: source
title: "REL 结构优化与选材技术方案"
source_type: 会议纪要
source_path: RAW/ima_sync/个人知识库/WKB/Projects/REL/REL 结构优化与选材技术方案.md
original_link: ""
date_published: 2026-10-11
date_processed: 2026-10-11
credibility: 中
knowledge_update_status: pending
key_claims: []
pages_linked: []
compile_mode: extractive
---

# REL 结构优化与选材技术方案

## Positioning 定位

本文为 IMA 知识库条目的抽取式源摘要页（`source_type: 会议纪要`）。
正文直接摘录自镜像层 `RAW_FULL/ima_sync/个人知识库/WKB/Projects/REL/REL 结构优化与选材技术方案.md`，未做语义改写；
待后续深度编译时补全 `key_claims` 与实体链接。

## Extracted Content 原文摘录

# REL 结构优化与选材技术方案

REL 结构优化与选材技术方案


# REL 结构优化与选材技术方案


目标：实现 Void Volume 80–117 cm³/g @ 0.5 kPa


## 一、当前方案（Variant C）诊断


PPT 中 Variant C 是一个重要起点，但在结构上仍有明确的优化空间。


|维度|现状|瓶颈|
|---|---|---|

|结构|四组分均匀混合单层|各纤维功能无法独立优化|

|密度|35–45 gsm 均匀|吸液区与扩散区无法分区优化|

|PTT 含量|28%|弹性恢复有余，但MD输运不足|

|Hollow 含量|14%|已接近均匀混合上限，不宜再提高|

|PVA 含量|8%|Z向支撑足够，但分散均匀性难控|


## 六、实施路线图建议


Phase 1（2–3周）：梯度密度 REL 验证   → 现有 ATB 线最小改造（双头feed改造）   → 验证 Void Volume 目标达成度   → 成本增量 ~+RMB 500/ton  Phase 2（4–6周）：双层 REL 中试   → 需要 air-lay head 双层改造（资本支出 ~$80K–120K）   → 全面 KPI 验证（Slide 10 全部指标）   → 成本增量 ~+RMB 1,400/ton vs Variant C  Phase 3（8–12周）：量产锁定   → 供应商资格认证（重点关注 PVA 不溶性验证）   → 全过程 CPK 监控（bW CV <5%, thickness CV <8%）


总结：从当前 Variant C 出发，梯度密度方案是低风险、中等收益的过渡路径；双层 REL 方案是达成 108–117 cm³/g void volume 的最优解，核心是将"快输运"和"强支撑"两个互相矛盾的需求解耦到两个独立层中。


王总，以上是完整的技术方案。需要我进一步展开某个具体部分（比如双层 ATB 的工艺细节，或者 PVA 不溶性验证的实验方案）吗？


双层结构关键技术参数：


|参数|Layer A (Intake)|Layer B (Scaffold)|
|---|---|---|

|目标克重|20–22 gsm|16–18 gsm|

|ES 2.2D/38mm|38%|60%|

|PTT 4D/51mm|35%|20%|

|Hollow 6D/51mm|20%|8%|

|PVA 1.5D/38mm|7%|12%|

|预期孔隙率|~92%|~88%|

|功能目标|快输运、高弹性恢复|Z向抗压缩、尺寸稳定|


## 三、选材精细优化参数


### 3.1 ES 纤维（PE/PET 2.2D/38mm）


当前 PPT 中已使用"durable hydrophilic"finish，但未指定接触角指标。


|参数|当前|优化后|备注|
|---|---|---|---|

|Finish 类型|Durable hydrophilic|双组分 finish：尖端亲水 + 根部耐久|第一次 void 接触角 <20°，第4次后仍 <35°|

|亲水持久性测试|未指定|4× void 循环后接触角变化 <15°|用 OWRK 方法测 Fiber Bundle|

|供应商二次开发|ES FiberVisions / Huvis|指定 Type B finish（耐尿液级）|普通亲水 finish 在离子强度 ~0.15M 时会失效|


### 3.2 PTT/PET 侧-by-侧纤维（4.0D/51mm）


这是弹性恢复的核心，但 PPT 对其卷曲激活曲线的描述较模糊。


|参数|当前|优化后|测试方法|
|---|---|---|---|

|预粘合卷曲数|<15 crimps/25mm|8–12 crimps/25mm（预）|确保 opening 不损伤卷曲|

|激活后卷曲数|>50 crimps/25mm|55–70 crimps/25mm|ATB 145–155°C 后测|

|卷曲激活温度窗|~145°C|143–150°C 可控窗口|TMA 测试，要求 ΔL/L0 > 15%|

|弹性模量|未指定|3.5–4.2 GPa（PET芯）|确保弹簧常数足够|

|供应商规格确认|未明确|Toray T-620 系列 或 同级|要求提供 Crimp Activation Curve|


### 3.4 水不溶性 PVA 纤维（1.5D/38mm）


这是 Z 向支撑的关键，但也是最敏感的组分——用错 PVA 类型是灾难性的（见 Slide 15 的失败案例）。


|参数|当前|优化后|验证方法|
|---|---|---|---|

|PVA 类型|水不溶性（acetalized）|Kuraray KURALON™ K-II INSOLUBLE（确认型号）|要求供应商提供 insoluble cert|

|不溶验证|80°C 水 30min 不溶|追加：人工尿液模拟液，37°C，4h 不溶|尿液离子强度更高，需专项验证|

|乙酰化度|未指定|≥99.5% acetylization|低于此值会在高温高湿下部分溶解|

|拉伸强度|高tenacity（未量化）|≥8 cN/dtex|确保 Z 向抗压能力|

|在 REL 中的分散均匀性|未指定|CV of PVA area fraction < 12%（SEM 横截面）|分散不均会导致局部 Z 向弱点|


## 五、ATB 工艺窗口精细化


PPT Slide 6 已给出 148–155°C 的推荐范围，这里补充更精细的工艺窗口：


|参数|Variant C|双层 REL 优化值|理由|
|---|---|---|---|

|烤箱顶区温度|148–155°C|150–153°C（双层同步）|Layer A/B 界面需要足够 PE 熔合|

|烤箱底区温度|未指定|145–148°C|底部温度过低会导致 B 层 bonding 不足|

|风压（through-air）|2.5–3.2 m/s|3.0–3.2 m/s|双层 web 较厚（~5.5mm 冷态），需要更高穿透力|

|Web overfeed|8–12%|10–13%|双层收缩更复杂，PTT 在两层中都存在|

|冷却区温度|<60°C|<50°C|确保 PTT 卷曲"锁定"在膨胀状态|

|线速度|15–22 m/min|12–18 m/min|双层需要更长烤箱停留时间（目标 8–10s）|


核心问题：单层均匀混合架构中，快的纤维（Hollow，输运）和强的纤维（PVA，支撑）在同一层互相牵制，无法独立调优。


## 二、结构优化方案


### 方案 A：梯度密度 REL（Gradient Density）


核心思路：沿 MD 方向做密度梯度——intake 端 48 gsm，rear 端 32 gsm。


Intake Zone (48 gsm)          MD Center          Rear Zone (32 gsm) ES 45%  PTT 32%  Hollow 16%  →  ES 52%  PTT 26%  Hollow 12% [PVA 7%]                        [PVA 10%] ← 高蓬松、快输运                均匀过渡            高 Recovery、低成本


技术参数：


Intake 区 Hollow 提升至 16–18%，PTT 保持 30%+，确保第一次 void 的 STT < 2.0s


Rear 区 PVA 提升至 10–12%，ES 提升至 55%，确保多次压缩后厚度恢复


梯度通过 ATB 生产时双头feed控制实现（前段 feeder 多投 Hollow+PTT，后段多投 PVA+ES）


过渡区长度 ≥ 80mm，避免突变导致 web 分层


预期效果：


1st void STT 从 <2.5s 降至 <2.0s


3rd void 后 void volume 剩余从 ~82% 提升至 ~87%


成本增加约 +RMB 500/ton（Hollow 多用 2–4%）


### 方案 B：双层 REL（Dual-Layer REL）← 推荐


核心思路：将 REL 拆分为功能解耦的两层，分别在 ATB 线上通过双头喂入同时热风粘合。


Top REL-A (Intake Layer, ~20 gsm):   PTT 35% + Hollow 20% + ES 38% + PVA 7%   → 高输运、高弹性、快吸收  Bottom REL-B (Scaffold Layer, ~18 gsm):   PVA 12% + ES 60% + PTT 20% + Hollow 8%   → 高Z向支撑、高bond密度、尺寸稳定


双层同步 ATB 工艺路径（无需两次通过烤箱）：


两台独立 opener 分别处理 Layer A 和 Layer B 的纤维


双层 air-lay head：先铺 Layer B（底部 scaffold），再叠加 Layer A（顶部 intake）


单层通过 ATB 烤箱：PE sheath 同时粘合两层


关键：Layer A 和 B 的 ES 纤维在界面处熔融互联，形成整体


关键：如果 PTT 卷曲在 ATB 烤箱中激活不足（温度偏低），弹性恢复损失；过度激活（>155°C 过久）则卷曲"锁定"，失去弹簧效应。需要在 ATB 线上做激活温度扫描（Slide 13 的 Stage 3 已部分覆盖，需补充量化标准）。


### 3.3 偏心 Hollow PE/PET 纤维（6.0D/51mm）


PPT 中指定了 hollow ratio ≥25%，这是对的，但坍塌压力测试未定义。


|Hollow Ratio|≥25%|28–32%|SEM 横截面上测，取 n=50|

|坍塌压力（Lumen collapse）|未测|>2.0 kPa（保压10min后 lumen 保留 >80%）|模拟 body weight 1.5× 安全系数|

|偏心度（Eccentricity）|未指定|偏心率 1.8–2.5×|确保 crimp 不对称，纤维互相推开|

|耐用亲水 finish|Durable hydrophilic|尿液耐受级（离子强度 0.15M 下接触角 <30°）|同 ES fiber 的 finish 要求|


预期效果（基于 Darcy + 弹性梁理论估算）：


|KPI|Variant C|双层REL（预测）|提升幅度|
|---|---|---|---|

|Void Volume @0.5kPa|95–105 cm³/g|108–117 cm³/g|+12~17%|

|Compression Recovery (4×)|85–88%|91–94%|+4~6pt|

|1st STT|<2.5s|<1.8s|-28%|

|3rd STT|<6.0s|<4.5s|-25%|

|MD Permeability (k)|6,000–9,000 D|9,000–13,000 D|+30~50%|


## 四、Void Volume 80–117 cm³/g @ 0.5 kPa 的参数映射


基于 Darcy's Law 和毛细管压力理论，void volume 与各参数的关系如下：


VV ∝ (1 - ρ_rel/ρ_fiber) × ε × f(compression)  其中： ρ_rel = REL 堆密度（gsm / thickness） ρ_fiber ≈ 1.38 g/cm³（PET基纤维平均） ε = 孔隙率 ≈ 1 - (局部纤维体积 / 总体积) f(compression) = 压缩修正（PTT弹性恢复 × PVA抗塌）


空隙率 ε 的目标值：


当前 Variant C：ε ≈ 92–94%（对应 VV ~95–105 cm³/g）


目标 117 cm³/g：需要 ε ≈ 96–97%


实现路径：降低堆密度——即相同 gsm 下做出更大厚度


|参数调节|对 VV 的影响|方向|
|---|---|---|

|提高 PTT 含量（28%→32%）|弹性恢复↑ → 压缩后厚度↑ → VV↑|+8~12 cm³/g|

|双层结构（功能解耦）|每层独立优化 → 整体蓬松度↑|+10~15 cm³/g|

|Hollow ratio 28%→32%|Lumen 体积直接贡献 VV|+5~8 cm³/g|

|PVA 细旦化（1.5D→1.2D）|相同质量下纤维根数↑ → 分散支撑更均匀|+3~5 cm³/g|

|ATB 风压优化（2.8→3.2 m/s）|Web 蓬松度↑（但需防 web lift）|+5~10 cm³/g|

## Original 原文

- 本地路径：`RAW/ima_sync/个人知识库/WKB/Projects/REL/REL 结构优化与选材技术方案.md`
- 镜像正文：`RAW_FULL/ima_sync/个人知识库/WKB/Projects/REL/REL 结构优化与选材技术方案.md`

## 关联页面

- [[Kuraray（可乐丽）]]　[[PET（聚酯）]]　[[PTT（聚对苯二甲酸丙二醇酯）]]　[[REL Splice Tensile Test（REL 拼接拉断力测试）]]　[[双物理交联网络水凝胶（PVA-壳聚糖-TOCNF）]]　[[尿液模拟液（Urine Analog）]]
