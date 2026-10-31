---
type: source
title: "Cellulose-Based LCE with Salt-Tuned Hydrogen Bonding（盐调控氢键网络 · 纤维素液晶弹性体 · NC 2026）"
source_type: 公众号
source_path: RAW/ima_sync/个人知识库/WKB/NC｜盐调控氢键网络：纤维素液晶弹性体实现可视化力致变色.md
original_link: "https://mp.weixin.qq.com/s/q86180nPIeEb6z_ZGKhrPg"
date_published: 2026-05-05
date_processed: 2026-10-31
credibility: 中
credibility_note: "学术论文导读类公众号（二手转述，非原文全文）。原文可回溯：Nat. Commun. 17, 6058 (2026), DOI 10.1038/s41467-026-72725-w。页内数值均转自导读，未经原文/补充材料复核 → 关键数值引用前须回溯 DOI。"
knowledge_update_status: done
key_claims:
  - "**盐调控（Hofmeister 效应）是解开纤维素 LCE「刚性 ↔ 可拉伸」死结的钥匙**：HPC 的刚性主链与链间氢键限制延展性，1 M Na₂SO₄ 处理把断裂伸长率从纯水的 155% 提到 **590%**、拉伸强度从 0.01 MPa 提到 **0.26 MPa**，手性向列相结构色同时保留"
  - "**同一阳离子下换阴离子就能调力学谱**：NaCl 得 0.13 MPa / 590–700%（更软更韧），Na₂SO₄ 得 0.26 MPa / 590%（更强），Na₂CO₃ 则过度溶胀破坏网络 —— 阴离子的 kosmotrope/chaotrope 定位直接决定水合状态与强/中/弱氢键配比"
  - "**颜色来自螺距而非染料，因此应变即波长**：拉伸 200/400/600% 依次红→橙→绿→蓝，反射峰 **717 → 455 nm**（拉伸）/ 450 nm（压缩）；AA 含量 10→15% 使初始反射峰 484 → 816 nm 线性红移（即配方端可预制任意基色）"
  - "**可拉伸 + 可自修复 + 可降解三者同时成立，但都有前置条件**：自修复须 70 °C + 1 M Na₂SO₄ 浸泡 60 min（强度恢复约 65%，0.17 MPa / 伸长 ~500%）；降解须室外暴露于铁网上方，10–20 天开始收缩、**30 天近完全降解**；L929 存活率 91%（NaCl）/ 94%（Na₂SO₄）"
  - "**与卫材应变区间存在量级错位（本库研判）**：材料要到 100–600% 应变才走完全色域，而纸尿裤腰围/腿围工作应变约 25–40% → 直接移植不可行；可用路径是把初始反射峰预置在长波端并利用低应变段的窄带位移，或改作**拉伸量超限指示**而非连续读数"
  - "**自修复条件在成品端不可实现（本库研判）**：70 °C 盐溶液浸泡 60 min 属实验室条件，一次性卫生用品既无此工况也无此必要 → 该性能对卫材价值为零，不应作为选型加分项"
pages_linked: ["[[胆甾相液晶弹性体 CLCE]]", "[[Structural Colour Mechanochromism（结构色力致变色）]]", "[[结构色 Structural Color]]", "[[液晶 Liquid Crystal]]", "[[变色材料 Chromic Materials]]", "[[Mechanochromic Strain Regime Transition（力致变色 25–27% 应变区间转型）]]", "[[Mechanochromic变色纤维]]"]
compile_mode: semantic
---

# Cellulose-Based LCE with Salt-Tuned Hydrogen Bonding（盐调控氢键网络 · 纤维素液晶弹性体 · NC 2026）

## Positioning 一句话定位

A bio-derived, fully degradable cholesteric liquid crystal elastomer that trades the usual petrochemical precursor for hydroxypropyl cellulose, and uses **salt (Hofmeister) chemistry — not molecular design — as the knob that buys stretchability** while keeping structural colour intact.

一种以羟丙基纤维素（HPC）替代石油基前驱体的手性向列相液晶弹性体：**用盐（Hofmeister 效应）而不是分子设计**来换取可拉伸性，同时完整保留结构色，且可室外降解。

## Source Facts 来源事实

| 项 | 内容 |
|---|---|
| 原文 | Guo, L.; Sun, J.; Wan, Z.; et al. *Cellulose-based liquid crystal elastomer with tunable mechanochromic response*. **Nature Communications 17, 6058 (2026)** |
| DOI | 10.1038/s41467-026-72725-w（2026-05-05 在线） |
| 通讯作者 | Guang Chu（东南大学）、Jiaqi Guo（南京林业大学） |
| 转载载体 | 微信公众号「学术论文导读 · 前沿速递」类文章，含 Figure 1–6 图注转述 |
| 抓取通道 | `get_media_info` → 微信原文 → Chrome UA + Referer 取 `#js_content`（不吃 REST 配额） |

## Summary 摘要

HPC self-assembles into a right-handed cholesteric nematic phase and selectively reflects right-circularly polarised light, giving structural colour without any dye. Its dense inter-chain hydrogen bonding, however, locks the chains: in pure water the material reaches only 0.01 MPa and 155% elongation. The authors copolymerise HPC with acrylic acid (AA) using PEGDA as crosslinker and LAP as photoinitiator, UV-cure the film to freeze the chiral nematic order, then soak it in salt solutions. The salt ions re-specify the hydration state of the network — kosmotropic SO₄²⁻ strips free water and rebuilds a strong/medium/weak hydrogen-bond hierarchy — and the same material jumps to 0.26 MPa and 590% elongation while the photonic structure survives.

HPC 自组装成右手性向列相，选择性反射右旋圆偏振光 —— 无需染料即有结构色。但其致密的链间氢键锁死了链段：纯水中强度仅 0.01 MPa、伸长 155%。作者让 HPC 与丙烯酸（AA）共聚（PEGDA 交联、LAP 光引发），紫外固化把手性向列序冻结成膜，再用盐溶液处理。盐离子重新指定网络的水合状态 —— kosmotropic 的 SO₄²⁻ 夺走自由水、重建强/中/弱氢键层级 —— 同一材料跃升到 0.26 MPa / 590%，而光子结构完好保留。

Mechanochromically, deformation reduces the cholesteric pitch and blue-shifts the reflection: 200/400/600% strain walks the film red → orange → green → blue, with the peak travelling 717 → 455 nm in tension and to 450 nm in compression. Formulation-side tuning is equally linear — raising AA from 10% to 15% moves the as-made reflection from 484 nm to 816 nm — which means the base colour can be pre-set at compounding rather than by mechanical pre-strain.

力致变色层面，形变压缩螺距使反射蓝移：200/400/600% 应变依次走红→橙→绿→蓝，峰值 717 → 455 nm（拉伸）、450 nm（压缩）。配方侧同样线性 —— AA 从 10% 提到 15% 使初始反射峰 484 → 816 nm —— 意味着基色可在配料端预设，而不必靠机械预拉伸。

## Numbers 提炼的数字与结论

| 项目 | 数值 | 口径 / 备注 |
|---|---|---|
| 纯水浸泡（对照） | 0.01 MPa / 155% | 氢键未调控的基线 |
| **1 M Na₂SO₄** | **0.26 MPa / 590%** | 后续试验选用体系 |
| 1 M NaCl | 0.13 MPa / 590–700% | 更软更韧 |
| 1 M Na₂CO₃ | — | 过度溶胀、网络破坏（不可用） |
| AA 10% → 15% | 反射峰 484 → 816 nm | 线性，可预制基色 |
| 拉伸 200/400/600% | 红 → 橙 → 绿 → 蓝 | 反射峰 717 → 455 nm |
| 压缩 | 717 → 450 nm | 与拉伸同向蓝移 |
| 手指关节 0/90/135° | 700 / 580 / 470 nm | 无需电信号的可视化运动检测 |
| 自修复（70 °C，1 M Na₂SO₄） | 30 min → 40%；**60 min → 0.17 MPa（约 65%）、伸长 ~500%** | 实验室条件 |
| 细胞相容性（L929） | 91%（NaCl）/ 94%（Na₂SO₄） | 存活率 |
| 室外降解 | 10–20 天收缩，**30 天近完全降解** | 样品置于土壤上方铁网 |
| MD 相互作用能 HPC–PAA | −270.1±13.4（水）/ −330.5±11.9（NaCl）/ −307.3±11.1（Na₂SO₄） kcal/mol | 盐体系更负 = 聚合物间作用更强 |
| 自由水/溶剂化水比 R | **3.6（Na₂SO₄） vs 8.4（NaCl）** | 解释两者性能排序不同源 |

## Key Mechanism 机理要点

1. **结构色不是染料**：色彩来自手性向列相的螺距对圆偏振光的选择性布拉格反射 → 颜色 = 螺距的读数，天然抗漂白。
2. **盐调控的三层作用**：① 离子水合减少可直接作用于聚合物的自由水；② 改变强/中/弱氢键的相对面积比（FTIR 二维相关 + 分峰拟合证实）；③ 提高 HPC–PAA 相互作用能（MD 模拟）。三者叠加把脆性凝胶变成弹性体。
3. **阴阳离子正交**：固定 Na⁺ 换阴离子（Cl⁻ / SO₄²⁻ / CO₃²⁻）呈现 0.13 / 0.26 / 破坏 三档 → 阴离子是主调节杆；固定阴离子换阳离子（Ca²⁺ / K⁺ / Na⁺）为次级调节。
4. **应变读数靠 SAXS/WAXS 佐证**：拉伸后散射图样由圆变椭圆或取向弧，说明宏观形变对应微观取向，颜色位移不是假象。

## Engineering Appraisal 卫材适配性研判（本库判断，非原文结论）

| 维度 | 原文事实 | 对卫材的含义 |
|---|---|---|
| 应变区间 | 全色域需 100–600% 应变 | 纸尿裤腰围/腿围工作应变约 25–40% → **量级错位**；直接移植不可行 |
| 可用的替代路径 | AA 10→15% 可把基色预置到 484–816 nm | 把初始峰预置长波端 + 只取低应变段窄带位移，或改作**超限报警**（一次性色变）而非连续读数 |
| 自修复 | 需 70 °C + 1 M 盐溶液 60 min | 成品端无此工况 → **该性能对卫材价值为零**，不作选型加分项 |
| 降解 | 室外 30 天近完全降解 | 一次性用品场景的 ESG 卖点；但意味着**货架期须控湿**，且"可冲散"仍不成立 |
| 生物相容 | L929 91–94% | 仅细胞级，未做皮肤刺激/致敏 → 若接触皮肤仍是 `[待验证]` |
| 盐敏感 | 性能依赖离子环境 | 遇尿（高离子强度、多价离子）行为**未测** → 尿液环境下的色域与力学需重新标定 `[待验证]` |

**结论（工程侧）**：这是一条「材料学上漂亮、卫材上错位」的路线。真正可迁移的不是它的应变范围，而是两个方法论：① **用离子环境调氢键网络**来同时拿到拉伸性与结构色（可用于本库其它纤维素基体系）；② **基色在配料端预制**而非机械预拉伸（工程上更可控）。若要往卫材走，应先解决 25–40% 应变段的色分辨力，而不是提高最大伸长率。

## 关联页面

- 概念：[[胆甾相液晶弹性体 CLCE]] · [[Structural Colour Mechanochromism（结构色力致变色）]] · [[结构色 Structural Color]] · [[液晶 Liquid Crystal]] · [[Mechanochromic Strain Regime Transition（力致变色 25–27% 应变区间转型）]] · [[Mechanochromic变色纤维]] · [[变色材料 Chromic Materials]]
- 同域源页：[[Self-Powered Photonic Sensor CLCE Sandwich]] · [[跨界科技早读 _ 一拉变色、可机洗！Nature Materials突破：可机洗的液晶弹性体变色纤维，让布料自带应变可视化]]

## 原文 Anchors 锚点状态

- 本地路径：`RAW/ima_sync/个人知识库/WKB/NC｜盐调控氢键网络：纤维素液晶弹性体实现可视化力致变色.md`（**预期路径**：原题含 ASCII `|` 非法文件名字符，按库内 4 条 NC 系列惯例转全角 `｜`；IMA 插件自 2026-10-20 起零落盘，正文已落 `RAW_FULL/` 同相对路径）
- 原文链接：https://mp.weixin.qq.com/s/q86180nPIeEb6z_ZGKhrPg
- 论文 DOI：https://doi.org/10.1038/s41467-026-72725-w
- **待办**：次日复核插件实落名，不符则按「三处同步」修正（RAW_FULL 镜像 + 账本 raw_path/full_path + 本页 source_path），**禁建重复页**。
