---
type: source
title: Be Max Platform — Trilobal Fibre Ratio, Ultrasonic Bonding & MD Distribution Target（纤维加工温度与成本验证）
source_type: 会议纪要
source_path: RAW/ima_sync/个人知识库/WKB/Areas/Meeting Minutes/纤维加工温度与成本验证.md
original_link: ""
date_published: "[待验证]（ASR 未标注会议日期；锚点：初始样品「下个月 10 月」可拿、本月底供应商侧建 600 m 平台、巴西 2028 采用 → 推测 2026 年 9 月）"
date_processed: 2026-09-29
credibility: 内部一手（跨团队技术交流 ASR 转写，全英文但转写质量差、时间戳乱序，含供应商报价与项目代号）
knowledge_update_status: done
key_claims:
  - 会议围绕 **Be max（ASR 作 bay max / baby max）平台**：用**异形（三叶形 trilobal）纤维** + **超声波 bonding** 把 liner 与 surge 结合，目标提高 **MD 方向尿液分布长度约 15%**
  - 纤维配置：**第一梳理 10% 三叶形纤维**；**最多 30% 的 homo PET 三叶形纤维**；理论改善 **MD urine distribution 长度 +15%** → 进而**更好地利用 SAP**
  - **核心工艺未知**：三叶形纤维（尤其 homo PET）加得越多，**中间层的 bonding strength 未知**；不同聚合物的熔点不同（PP 与 PET 差异大）
  - **温度路线**：考虑**工程改性 PP，把加工温度降到接近 130 ℃（即 PE 的熔点）**，以与现有 TBCW / bicomponent 体系兼容 —— "仍在做，但近期应可行"
  - bonding 路线对比：**pressure bonding 试过、不工作**；目前**没有 LSE**；正在与中国供应商洽谈**类似 LSE 的方案**，但用**线性 horn（linear）而非旋转 horn**；报价约 **7 万美元**；速度可达 **500 m/min**，代价是**需要更多空间**
  - 另有一家**香港供应商复制德国 Herrmann 超声波模块**（"duplicate the whole material recipe"）→ 电气供电兼容，但**电压与频率不同**，会影响**寿命（振动）** → 必须选对频率与电压
  - 模块速度：目前 **380 m** 为可靠数据；目标验证 **500 m**
  - 离线验证计划：已订购 **pattern roll**，本月底在供应商侧搭建 **600 m 平台**跑离线，先验证 **pattern clearance**（高速下 3D 花型的清晰度），再用离线材料在 PC 机器线测性能
  - **成本动因**：目前从**延江（yanjiang）**大量采购较贵的面层 → 本项目可为**成本敏感国家**带来节约；巴西可能 **2028** 采用
  - **彩色印刷位置改变**：原考虑在 LSE 区域用不同颜色印刷；本次访问后改为主张在**被 TBCW 覆盖的区域**印刷 —— 认为高速下**不会有转移（transfer）或油墨堆积（build-up）问题**
  - 阶段：目前为 **FEI** 阶段；**初始样品（不含 kirigami 与印刷）预计 10 月**可得；**Kirigami（kiga）** 与对方 **BA 项目**的协同待讨论
pages_linked:
  - 三叶形截面纤维（Trilobal Fibre）
  - Ultrasonic Bonding of PET-Containing Topsheet
  - 延江（Yanjan）
  - TBCW结构
  - Kirigami Apertured Nonwoven（切割拉伸开孔工艺）
---

# Be Max Platform — Trilobal Fibre Ratio, Ultrasonic Bonding & MD Distribution Target（纤维加工温度与成本验证）

> ASR 转写讹字说明：本稿为跨团队技术交流的自动转写，**全英文但转写质量差**，时间戳乱序。已识别的还原与存疑：
> - **「bay max / baby max / waymas / be max」** = 项目名 **Be max**；「kiga / k 尔比 / k Bo Bo / k processor」= **Kirigami**
> - **「tri level fiber / high level fiber / five fiber」** = **三叶形（trilobal）异形纤维**；「homo PT / home PT fiber」= **homo PET（均聚 PET）纤维**
> - **「span ball / spend / by spa / byos bomb / TBCW / PVCW」** = **纺粘（spunbond）** / **TBCW（透过粘合梳理布）**
> - **「usonic / ul trust / the Duke without notation」** = **超声波（ultrasonic）**；「rotational horn / rotational home」= **旋转焊头**；「linear horn」= **线性焊头**
> - **「LSE」** = 一种既有的 bonding 工艺/设备（本方目前没有）；「pressure bonding / pressure on」= 压力 bonding
> - **「Herrmann / HERRMANI」** = 德国超声波厂商 **Herrmann**；"duplicate" = 香港供应商**复制其模块**
> - **「yanjiang / yenjiang」** = **延江（Yanjan）**；「JY」= 某供应商代号 [待验证]
> - **「PC machine line / TTJ twenty one / RS」** = 产线/设备代号 [待验证]；「FEI / FAI」= 项目阶段（**FEI** 为准）
> - **「pattern loan」** = **pattern roll（花型辊）** [待验证]；「pattern clearance」= 花型清晰度
> - 人名音转：Chris、Jerry、Anthony（doctor Anthony） —— 一律 **[待验证]**
>
> ⛔ 本页只记录**已决**事项与**待决**问题；讨论中的想法一律归入 `Open issues 待决问题` 或 `Background 背景`。

## Attendees / Date 参会与日期

- Date 日期：**[待验证]** —— 转写未标注；锚点为"初始样品下个月 10 月""本月底在供应商侧建平台""巴西 2028" → 推测 **2026 年 9 月**
- 场景：跨团队（FBI 团队 / 开放创新团队 / 产品与工艺）的技术交流，围绕 **Be max 平台**的纤维配置、bonding 工艺与验证计划
- 与会：Chris、Jerry、Anthony 及工艺/材料同事（均为音转）[待验证]
- ⚠️ 具体人名一律 **[待验证]**，不做实名指派

## Key decisions 决策要点

1. **平台目标（已定）**：Be max 平台用**异形（三叶形）纤维 + 超声波 bonding** 把 liner 与 surge 结合，**目标提高 MD 方向尿液分布长度约 15%**；更长的分布长度 → **更好地利用 SAP**。
2. **纤维配置（已排定）**：
   - **第一梳理：10% 三叶形纤维**；
   - **最多 30% 的 homo PET 三叶形纤维**；
   - 理论收益：**MD urine distribution 长度 +15%**（"theoretically 15% more on the MD distribution"）。
3. **核心工艺风险（已识别）**：**三叶形纤维（尤其 homo PET）加得越多，中间层的 bonding strength 越不确定** —— 这是本平台**尚未解决的关键未知**。
4. **温度路线（已提出，仍在做）**：不同聚合物熔点差异大（PP vs PET）；考虑**工程改性 PP，把加工温度降到接近 130 ℃（即 PE 的熔点）**，与现有 bicomponent / TBCW 体系兼容 —— 本方判断"近期应可行（feasible in the near future）"，但**仍在推进中**。
5. **bonding 路线的结论（已明确）**：
   - **pressure bonding 试过、不工作**；
   - 本方**目前没有 LSE**；
   - 正在与中国供应商洽谈**类似 LSE 的方案**，但采用**线性焊头（linear horn）而非旋转焊头**；报价约 **7 万美元**；**速度可达 500 m/min**，代价是**需要更多产线空间**。
6. **另一条超声波来源（已评估）**：一家**香港供应商复制德国 Herrmann 的超声波模块**（"duplicate the whole material recipe"）→ **供电兼容**，但**电压与频率不同**，会**影响寿命（因振动）** → 必须选对频率与电压。
7. **速度基线（已给出）**：模块目前 **380 m** 为**可靠数据**；目标验证 **500 m**。
8. **离线验证计划（已排定）**：已订购 **pattern roll**；**本月底**在供应商侧搭建 **600 m 平台**跑离线 → 先验证 **pattern clearance**（高速下 3D 花型是否清晰）→ 再用离线材料在 PC 机器线测性能。第二阶段为普通 TBCW + 非三叶形纤维。
9. **成本动因（已明确）**：目前**从延江大量采购较贵的面层** → 本项目可为**成本敏感国家**带来节约。
10. **彩色印刷位置（已改变）**：原考虑在 **LSE 区域**做不同颜色印刷；本次访问后改为主张在**被 TBCW 覆盖的区域**印刷 —— 因为被覆盖，**高速下不会有转移（transfer）或油墨堆积（build-up）问题**。
11. **阶段与里程碑（已给出）**：目前为 **FEI** 阶段；**初始样品（不含 Kirigami 与印刷）预计 10 月**可得；巴西预计 **2028** 采用。

## Open issues 待决问题

1. **中间层 bonding strength 未知**：三叶形（尤其 homo PET）比例提高后，中间层的**粘合强度**尚未知 —— 这是本平台的关键技术缺口。
2. **PP 低温改性尚未完成**：把 PP 加工温度降到接近 **130 ℃** 的改性"**仍在做**"，未落地。
3. **超声波 bonding 与材料的匹配性未验证**：pressure bonding 已确认不工作；bonding 效果"取决于材料、取决于 PP" → 具体匹配窗口未知。
4. **500 m 未验证**：380 m 可靠，**500 m 尚未验证**（"we haven't verified yet, we need more data to test online"）。
5. **Kirigami 与 BA 项目的协同未定**：本方提出"如果我们用这种方式做 Kirigami，你们 BA 项目的计划是什么" → 未获答复。
6. **Kirigami 用在纺粘上是否可行未试过**：会中讨论"能否在纺粘上做（切割+拉伸）"，结论是"**从未试过**（never tried）"，且推测**比 TBCW 更难**（纺粘纤维更长、更厚，拉伸更难、工位更少）。
7. **LSE 替代方案的供应商选择未定**：中国供应商的线性 horn 方案（约 7 万美元）vs. 香港复制 Herrmann 模块（频率/电压风险）→ 未定。
8. **打样排产受限**：会中提到 TTJ 21 的**利用率已很高**，可能需要在别处安排打样 → 未定。
9. **商业试产计划的时间点未给出**：会中问到"commercial trial plan 是什么时候"，**未获答复**。
10. **成本敏感的落地国家未定**：提到巴西，但"巴西可能 2028 才采用"；是否还有其他国家未定。

## Action items 行动项

| Task 任务 | Owner 负责人 | Due 截止 | Status 状态 |
| --- | --- | --- | --- |
| 本月底在供应商侧搭建 600 m 离线平台并跑通 | 供应商 + 本方（ASR 未指名） | 本月底 | Open |
| 用离线材料验证 pattern clearance（高速下 3D 花型清晰度） | 本方（ASR 未指名） | 离线阶段 | Open |
| 用离线材料在 PC 机器线测性能 | 本方（ASR 未指名） | 离线之后 | Open |
| 取得初始样品（不含 Kirigami 与印刷） | 本方 + 供应商（ASR 未指名） | 10 月 | Open |
| 在线验证模块速度从 380 m 提到 500 m | 本方（ASR 未指名） | [待验证] | Open |
| 推进 PP 低温改性（接近 130 ℃） | 本方 + 材料供应商（ASR 未指名） | 推进中 | Open |
| 验证高比例三叶形下的中间层 bonding strength | 本方（ASR 未指名） | [待验证] | Open |
| 评估中国供应商线性 horn 方案（约 7 万美元）与空间需求 | 本方 + 采购（ASR 未指名） | [待验证] | Open |
| 若采用香港复制 Herrmann 模块，确认频率与电压以保寿命 | 本方（ASR 未指名） | [待验证] | Open |
| 与对方就 Kirigami 与 BA 项目的协同给出计划 | 双方（ASR 未指名） | [待验证] | Open |
| 明确商业试产（commercial trial）的时间计划 | 本方（ASR 未指名） | [待验证] | Open |
| 评估在纺粘上做 Kirigami（切割+拉伸）的可行性（从未试过） | 双方（ASR 未指名） | [待验证] | Open |

## Background 背景

Be max 平台想解决的是"**不增加克重而提高尿液分布**"：用异形（三叶形）纤维改善 MD 方向的扩散，用超声波 bonding 把 liner 与 surge 结合，从而减少对**较贵的延江面层**的依赖，为成本敏感市场（如巴西）提供降本路径。本次交流是在 FEI 阶段，就纤维配比、bonding 工艺选型与离线验证计划做对齐。

## 提炼的数字与结论 Numbers & takeaways

| Item 项目 | Value 数值 | Note 备注 |
| --- | --- | --- |
| 三叶形纤维（第一梳理） | **10%** | — |
| homo PET 三叶形上限 | **30%** | — |
| 目标 | **MD urine distribution 长度 +15%** | **理论值**，待实测 |
| 逻辑链 | 分布更长 → **更好地利用 SAP** | — |
| 温度目标 | PP 改性至接近 **130 ℃**（= PE 熔点） | 仍在做，未落地 |
| 模块可靠速度 | **380 m** | 目标验证 **500 m** |
| 离线平台 | **600 m**（供应商侧，本月底） | 先验证 pattern clearance |
| 超声波方案（中国供应商） | **线性 horn**，约 **7 万美元**，可达 **500 m/min** | 需更多空间 |
| 超声波方案（香港） | 复制 **Herrmann** 模块，供电兼容但**电压/频率不同** | 影响寿命（振动） |
| 阶段 | **FEI** | 初始样品 **10 月** |
| 巴西采用 | 预计 **2028** | 成本敏感市场 |
| 成本动因 | 现从**延江**大量采购较贵面层 | 本项目用于降本 |

> 🔴 **manual_review（2026-09-29）**：本页涉及**供应商报价（约 7 万美元）、供应商能力评价（复制 Herrmann 模块）、采购依赖（延江）、项目阶段与商业化时间（巴西 2028）**。按 AGENTS.md §5，**报价与采购商务不得页面化**；此处只保留量级与决策门槛。请回原文核对：
> `RAW/ima_sync/个人知识库/WKB/Areas/Meeting Minutes/纤维加工温度与成本验证.md`
> 另：全文为**低质量英文 ASR**，多处音转无法确证（JY、PC machine line、TTJ 21、RS 等代号）；引用前须回溯。

## Sources 来源

- 原始记录：`RAW/ima_sync/个人知识库/WKB/Areas/Meeting Minutes/纤维加工温度与成本验证.md`（ASR 转写，会议日期 [待验证]）

## 关联页面 Related pages

- [[三叶形截面纤维（Trilobal Fibre）]]
- [[Ultrasonic Bonding of PET-Containing Topsheet]]
- [[延江（Yanjan）]]
- [[TBCW结构]]
- [[Kirigami Apertured Nonwoven（切割拉伸开孔工艺）]]
