---
type: comparison
title: "COCO 芯体成型质量判读方法对比（China-STM-03_04_05 vs TTM-02_03）"
subjects: ["[[COCO芯体平台]]", "[[芯体测试方法与验收基准（STM）]]"]
dimension: 综合
updated: 2026-09-29
tags: [COCO, 复合芯体, China-STM, TTM, 成型质量判读, 进厂检验, 内控标准]
---

# COCO 芯体成型质量判读方法对比（China-STM-03_04_05 vs TTM-02_03）

## 对比维度表 Comparison Matrix

> 必含「成本」与「供应链风险」两列。
> 两组方法同属 [[Nanjing South Plant BCC Finished Product STM Compendium WI-56234 Rev.8（南京南厂BCC成品标准测试方法汇编）]] 的「COCO 专属方法族」，但回答的问题不同：**China-STM-03/04/05 判「芯体看起来是否成型良好」（缺陷与尺寸）**，**TTM-02/03 判「材料分布是否均匀、量是否对」（密度与质量）**。

| 维度 Dimension | China-STM-03 / 04 / 05（缺陷与宽度判读） | TTM-02 / TTM-03（密度与质量判读） | 依据 Source |
|---|---|---|---|
| 回答的问题 Question | 芯体有没有 SAM 团聚、自由 SAM、REL 铺偏等**成型缺陷** | SAM 在芯体平面上**分布是否均匀**、REL 下层**量是否足够** | [[Nanjing South Plant BCC Finished Product STM Compendium WI-56234 Rev.8（南京南厂BCC成品标准测试方法汇编）]] |
| 输出量纲 Output | mm（宽度）、mm²（面积）、g（自由 SAM 质量 0.01 g）、%（存在比例） | g/cm³（分区密度 D）、g（SAM 质量） | 同上 |
| 判读性质 Nature | **定性 → 半定量**；目视识别 + 量具读数 | **定量**；称重 / 厚度计算 | 同上 |
| 试样与仪器 Sample & instrument | 整片芯体；标准量尺 + **灯箱**（[[China-STM-05 REL _ LSS _ PSS Width（COCO 芯体分层宽度测量 V4）]] 明列）、天平（0.01 g） | 圆形切刀 **r = 2.40 cm**；厚度精度 **0.01 mm**、重量精度 **0.01 g**（TTM-02 九点法） | 同上 |
| 关键口径 Key conditions | China-STM-03：SAM Island / Heavy Lane 判据为**纵向连续或累计长度 > 吸收体总长 1/2**；China-STM-05：宽度取 **（最宽 + 最窄）/ 2**，**PSS 与 LSS 各自单独备样** | TTM-02：**D = (W1i − W2i) / [π × 2.40² × (T1i − T2i)]**，九点取样；TTM-03：剥离后称重 | 同上、[[China-STM-05 REL _ LSS _ PSS Width（COCO 芯体分层宽度测量 V4）]] |
| 液体 / 压力口径 Liquid & pressure | **干态测量，不涉及液体与压力** | **干态测量，不涉及液体与压力** | 同上 |
| 主观性 Subjectivity | **高**——China-STM-05 原文明言 SAM 边缘确认「目前依赖检验员培训」 | **低**——切刀定位 + 称重/厚度读数，人为判读空间小 | [[China-STM-05 REL _ LSS _ PSS Width（COCO 芯体分层宽度测量 V4）]] |
| 版本敏感性 Version sensitivity | **高**——[[China-STM-05 REL _ LSS _ PSS Width（COCO 芯体分层宽度测量 V4）]] 为第 4 版（2020-02-26），而 WI-56234 收录为第 2 版（2019-06-20），**两版不可混用** | 未见多版本冲突记录 `[待验证]` | 两页同上 |
| 放行适用性 Release use | 成品过程判读 / 拆解分析，**非进厂放行项** | 成品过程判读 / 拆解分析，**非进厂放行项** | [[Raw Material Testing Method Summary（原材料测试方法汇总表）]] |
| **成本 Cost** | **低**——灯箱 + 量尺 + 0.01 g 天平即可；单样以分钟计；但**检验员培训成本与判读返工成本不可忽略**（边缘争议需复测、复样） | **中**——需定制圆形切刀（r = 2.40 cm）、0.01 mm 厚度计；九点法单样取样与读数工时约为宽度法的数倍；**试样破坏性更高**（切刀取样后芯体不可复原） | [[Nanjing South Plant BCC Finished Product STM Compendium WI-56234 Rev.8（南京南厂BCC成品标准测试方法汇编）]] |
| **供应链风险 Supply chain risk** | **中—高**：① 判据依赖检验员培训，**供应商侧与 KC 侧对同一片芯体可能给出不同宽度/缺陷结论**，构成来料争议点；② 灯箱识别法在供应商现场若无同等条件则**不可复现**；③ 第 2 版与第 4 版并存，对供应商下发检验规范时**易引错版本** | **中**：① 九点密度与 REL 下层 SAM 量直接反映**供应商布粉/复合工艺能力**，方法客观、争议小，但② 切刀半径 2.40 cm 为非标尺寸，**依赖特定工装，工装丢失或换型即断测**；③ 属厂内方法，供应商无对等标准时无法做联合比对 | 同上、[[Raw Material STM - Tianjin Mill WI-60632（原材料标准测试方法-TJ）]] |
| 适用场景 When to use | 新品导入、试产拆解、成型异常排查（SAM 团聚、REL 偏移、露胶颗粒） | 配方/工艺变更验证、SAM 分布均匀性量化、REL 下层 SAM 投料量核查 | [[COCO芯体平台]] |

> 尾注 Footnote：本表所有数字与判据均来自 [[Nanjing South Plant BCC Finished Product STM Compendium WI-56234 Rev.8（南京南厂BCC成品标准测试方法汇编）]]、[[China-STM-05 REL _ LSS _ PSS Width（COCO 芯体分层宽度测量 V4）]]、[[Raw Material STM - Tianjin Mill WI-60632（原材料标准测试方法-TJ）]]、[[Raw Material Testing Method Summary（原材料测试方法汇总表）]]；含 `[待验证]` 标记者为单一来源、库内无第二来源交叉印证。

## 各自适用场景 Application Scope

- **China-STM-03 / 04 / 05（缺陷与宽度）**：回答「芯体成型是否良好”——SAM Island / Heavy Lane（China-STM-03）、REL 下层自由 SAM（China-STM-04）、REL / LSS / PSS 分层宽度（China-STM-05）。适合**快速、低成本、可现场执行**的拆解判读，是试产与异常排查的第一道筛子。局限是输出为尺寸/面积/质量，**不能直接换算成吸收性能**，且边缘判定主观。
- **TTM-02 / TTM-03（密度与质量）**：回答「材料分布是否均匀、投放量是否到位」——九点分区密度（TTM-02）、REL 下层 SAM 质量（TTM-03）。输出可进入统计过程控制（SPC），**适合做工艺能力与供应商能力对比**。局限是破坏性取样、工时长、依赖非标切刀。

## 与进厂放行体系的落差 Gap to Incoming Release

> 关键结构性事实（2026-09-29）：以上六项均为**厂内成品/过程判读方法**，而复合芯体的**进厂放行**判读走的是另一套。

| 环节 Stage | 方法 Method | 编号体系 Numbering | 依据 Source |
|---|---|---|---|
| 成品 / 过程判读 | China-STM-03/04/05、TTM-02/03 | KC 中国区 China-STM / TTM 编号 | [[Nanjing South Plant BCC Finished Product STM Compendium WI-56234 Rev.8（南京南厂BCC成品标准测试方法汇编）]] |
| 复合芯体进厂判读 | 回渗 80 mL × 2 次（5 min + 5 min）+ φ100 mm / **1.20 kg** 压块压 1 min；滑渗 **30 ± 2°**、60 mL、7 条去极值取 5 条均值；厚度 5 片 × 10 点 = 50 点加权平均 | **RMS / 内控**，无 KC STM 编号 | [[Raw Material STM - Tianjin Mill WI-60632（原材料标准测试方法-TJ）]] |
| 原材料总表登记 | 复合芯体九项（基重、厚度、COV、尺寸、回渗、吸收性、滑渗、水分、白度、pH） | **全部 Inner Quality Testing Standard（内控）** | [[Raw Material Testing Method Summary（原材料测试方法汇总表）]] |

⚠️ **口径落差**：进厂复合芯体回渗用 **80 mL × 2 次 + 1.20 kg 压块**（[[Raw Material STM - Tianjin Mill WI-60632（原材料标准测试方法-TJ）]]），与成品端 FIFE / 回渗法（14 inH₂O ≈ 3.4 kPa、0.5 psi 回渗载荷）**口径完全不同，数值不可互比**。引用时必须标明「进厂 RMS 口径」或「成品 STM 口径」。

🔴 **manual_review（2026-09-29）**：复合芯体作为新兴材料，其进厂判读**尚未进入 KC 全球 STM 体系**（[[Raw Material Testing Method Summary（原材料测试方法汇总表）]] 明确记录九项全为内控）。在引入第二供应商或变更芯体供应商时，缺乏可对外引用的统一标准编号，属**对外谈判与来料争议的标准空白**。是否已有新版全球 STM 编号，需人工查 EtQ 方法主档确认——本页仅标记，不裁决。

## 结论 Conclusion

两组方法不是替代关系而是互补：**China-STM-03/04/05 用低成本目视判读筛出成型缺陷，TTM-02/03 用破坏性定量测出分布与投料量**；但两者都只覆盖成品/过程，**复合芯体的进厂放行仍停留在内控（RMS）层面**，这是 COCO 体系当前最大的标准缺口与供应链风险源。

## 来源 Sources

- [[Nanjing South Plant BCC Finished Product STM Compendium WI-56234 Rev.8（南京南厂BCC成品标准测试方法汇编）]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/BCC成品STM-南京南厂 1.pdf.md`
- [[China-STM-05 REL _ LSS _ PSS Width（COCO 芯体分层宽度测量 V4）]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/CoCo Product-REL Width, SAM Width in REL, LSS and PSS width China STM-05 20200303.pdf.md`
- [[Raw Material STM - Tianjin Mill WI-60632（原材料标准测试方法-TJ）]] —— 天津厂原材料 STM
- [[Raw Material Testing Method Summary（原材料测试方法汇总表）]] —— 原材料测试方法总索引

## 关联页面 Related

- 概念：[[COCO芯体平台]]、[[芯体测试方法与验收基准（STM）]]、[[REL增强层]]、[[MD Liquid Distribution]]、[[SAM Testing Methods（超级吸水材料测试方法）]]
- 实体：[[Kimberly-Clark（金佰利）]]、[[KC Nanjing Plant（金佰利南京厂）]]、[[KC Tianjin Mill（金佰利天津厂）]]
