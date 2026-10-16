---
type: source
title: "MFR _ MFI（以及 MI、MVR）辨析"
source_type: 会议纪要
source_path: RAW/ima_sync/个人知识库/WKB/Areas/Test Method/MFR _ MFI（以及 MI、MVR）辨析.md
original_link: ""
date_published: 2026-10-11
date_processed: 2026-10-11
credibility: 中
knowledge_update_status: pending
key_claims: []
pages_linked: []
compile_mode: extractive
---

# MFR _ MFI（以及 MI、MVR）辨析

## Positioning 定位

本文为 IMA 知识库条目的抽取式源摘要页（`source_type: 会议纪要`）。
正文直接摘录自镜像层 `RAW_FULL/ima_sync/个人知识库/WKB/Areas/Test Method/MFR _ MFI（以及 MI、MVR）辨析.md`，未做语义改写；
待后续深度编译时补全 `key_claims` 与实体链接。

## Extracted Content 原文摘录

# MFR _ MFI（以及 MI、MVR）辨析

# 


# MFR / MFI（以及 MI、MVR）辨析


先说明："FDI" 在聚合物表征中没有对应的标准缩写，您可能想问的是 MFI 或 MVR，下面一并覆盖；如果 FDI 另有所指（比如外汇 FDInvest 之类），告诉我再查。


## 一、本质：同一种测试，不同叫法


MFR 和 MFI 指的是同一个测试（ASTM D1238 / ISO 1133 毛细管熔体流动仪）：恒定温度、恒定负荷下，10 分钟内从标准口模挤出的熔体克数，单位 g/10min。


MFR（Melt Flow Rate，熔体流动速率）：现代标准用语，PE/PP Handbook 和 ISO 体系的主流叫法


MFI（Melt Flow Index，熔融指数）：老叫法，纺织纤维行业仍大量沿用（如 Manufactured Fibre Technology 中熔喷章节）


MI（Melt Index，熔指）：PE 行业惯用，严格定义是 190°C / 2.16kg（303 kPa）这个特定条件下的挤出量——只有该条件才叫 MI；其他负荷下的流量称为 flow index，如 I₂（2.16kg）、I₅（5kg）


测试条件按树脂区分：PP 用 230°C / 2.16kg（MFI 定义出处）；PE 用 190°C / 2.16kg 。


## 二、它到底表征什么


MFR 是重均分子量 Mw 的反比单点指标：分子量越大、熔体黏度越高、流出量越少。典型 HPP 产品 MFR 0.2–45 对应 Mw 从约 100 万降到 10 万，两者严格反比 。PP 市场销售就是按 "MFR + 助剂配方" 定牌号的 。


关键局限——它是单点测试：MFR 只反映低剪切速率下的黏度，无法描述整个剪切速率谱。MWD 越宽，剪切变稀越强，单点 MFR 完全看不到这个信息 。这正是文献批评的"用单点 MFR 替代完整流变曲线"是常见错误的原因 。对纺粘/熔喷这类高剪切、高牵伸工艺，MFR 只是入场券，MWD（PDI）才是决定性指标：窄 MWD → 低熔体弹性 → 稳定细旦牵伸；宽 MWD → 牵伸共振 → 断丝 。


## 三、卫材场景的 MFR 窗口速查


|工艺/应用|MFR (g/10min)|来源|
|---|---|---|

|纺粘 Spunbond|30–80（典型 ~35，CR 均聚）||

|熔喷 Meltblown|30–1500（典型 ≥500，窄 MWD）||

|短纤 Staple|10–30||

|单丝 Monofilament|1–4||

|PP 注塑（一般）|≥5；TWIM 薄壁 ~75||

|PE 吹膜|0.5–2||

|PE 流延膜|2–6||

|PE 挤出涂布|5–12||


## 四、MFR 之外的两个补充概念


MVR（Melt Volume Rate，熔体体积流动速率）：ISO 1133 的体积版，单位 cm³/10min，活塞位移法测量，可避开称重、直接数字化；MFR = MVR × 熔体密度。（此条为通用标准常识，知识库未直接覆盖 ISO 1133 MVR 细节）


CR 树脂（Controlled Rheology）：通过过氧化物控释降解把 MWD 收窄的树脂——纺粘/熔喷指定的 MFR 窗口默认搭配 CR 工艺；代价是过氧化物分解副产物影响气味（organoleptics），这也是注塑领域反应器料反而更受欢迎的原因


采购一句话：规格书上要的不只是 MFR 单点值——PP 纤维级要同时锁定 MFR 窗口 + CR 工艺 + PDI，膜级 PE 要注明负荷条件（I₂ 还是 I₅），否则同一牌号不同测试条件数值不可比。

## Original 原文

- 本地路径：`RAW/ima_sync/个人知识库/WKB/Areas/Test Method/MFR _ MFI（以及 MI、MVR）辨析.md`
- 镜像正文：`RAW_FULL/ima_sync/个人知识库/WKB/Areas/Test Method/MFR _ MFI（以及 MI、MVR）辨析.md`

## 关联页面

- [[熔喷 Meltblown]]　[[纺粘 Spunbond]]
