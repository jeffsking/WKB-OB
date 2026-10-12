---
type: source
title: "US 20250064649A1 Intelligent Monitoring Diaper with Enhanced Features (Wu Guohui)"
source_type: 专利
source_path: RAW/ima_sync/个人知识库/WKB/Areas/IP/六-1_Intelligent_Monitoring_Diaper_with_Enhanced_Features.pdf.md
original_link: ""
date_published: 2025-02-27
date_processed: 2026-09-29
credibility: 中
knowledge_update_status: done
key_claims:
  - "US patent APPLICATION publication (US 2025/0064649 A1, published Feb. 27, 2025; Appl. No. 18/455,603, filed Aug. 24, 2023) by Wu Guohui, Kowloon (CN), claiming priority from Chinese Patent Application Ser. No. 2023216251165 filed Jun. 6, 2023: an intelligent monitoring diaper with a REUSABLE, DETACHABLE monitor clipped onto a disposable diaper body."
  - "Urine detection is ELECTRICAL, not optical: the diaper body carries a conductive layer with conductive cables in a GRID of vertical and horizontal stripes; urine permeating the cable CHANGES ITS RESISTANCE, and the main control board judges the presence of urine from that resistance change."
  - "The reusable-monitor architecture is the economic core: an elastic clip on the back of the monitor presses the conductive POGO PIN against the cable; a hole in the waterproof layer exposes the cable at the contact point. The monitor is reused across diapers, which the document says 'reduces costs while promoting environmental sustainability'."
  - "Sensor stack on the single monitor: body temperature sensor, humidity sensor, odor sensor (H2S, NH3, C8H7N, C9H9N, CH3COOH, C4H8O2, H2 or CH4), motion sensor (three- or six-axis acceleration), warning device (loudspeaker and/or LED), communication module (Bluetooth or WIFI), GPS locator, and an enzyme detection module."
  - "The enzyme test piece sits on the water-absorbing layer and is electrically connected to the conductive cable; urine infiltration changes its resistance, and the module derives uric acid content. The document states other strips may be substituted, e.g. total cholesterol or HDL cholesterol test strips."
  - "8 claims (claims 1–8; claim 1 is the sole independent claim). The document contains three drafting defects: claim 4 depends on 'claim 4', claim 7 depends on 'claim 7', and paragraph [0044] refers to transmitting 'blood sugar readings' although no blood-glucose sensor is described anywhere in the disclosure."
pages_linked: ["[[Sensor-Equipped Absorbent Article（含传感器吸收性物品）]]", "[[Wetness Indicator Ladder（尿湿指示阶梯）]]", "[[智能尿裤功能层]]"]
---

# US 20250064649A1 Intelligent Monitoring Diaper with Enhanced Features (Wu Guohui)

## One-line positioning 一句话定位

**一件美国发明申请公开**（US 2025/0064649 A1，2025-02-27 公开；申请人/发明人均为 **Wu Guohui，Kowloon (CN)**，中国优先权 2023216251165）。它把"智能尿裤"的成本难题用**结构拆分**解决：**昂贵的多传感器监控器做成可拆可复用的夹子**，一次性尿裤本体上只留**一层导电线缆（栅格状）**作为耗材。尿液检测走**电阻法**（尿渗入导电线缆 → **电阻变化** → 主控板判定），而不是本库常见的光学/变色法。

## Abstract 摘要（逐字摘录）

(54) **INTELLIGENT MONITORING DIAPER WITH ENHANCED FEATURES**。
(57) 逐字要点：一种具有增强功能的智能监测尿裤，具有：尿裤本体；监控器，其配备**电池、主控板、体温传感器、湿度传感器、气味传感器、运动传感器与报警装置**；电池与主控板电连接；体温、湿度、气味、运动传感器与报警模块**各自独立**地与主控板电连接；**湿度传感器与导电弹簧针（conductive pogo pin）电连接**；**尿裤本体具有导电线缆（conductive cable）**；监控器**可拆卸地**安装在尿裤本体上，且**导电弹簧针与导电线缆接触**。

## Extracted numbers and conclusions 提炼的数字与结论

### Bibliographic data 著录数据（逐字照抄）

| Item 项目 | Value / Conclusion 数值 / 结论 | Note 备注 |
|---|---|---|
| 公开号 / 文献种类 | **US 2025/0064649 A1**；**(12) Patent Application Publication**（**申请公开，非授权公告**） | 扉页 (10)(12)，逐字照抄 |
| 公开日 | **Feb. 27, 2025** | (43) |
| 申请号 / 申请日 | **18/455,603**；**Aug. 24, 2023** | (21)(22) |
| 优先权 | 35 U.S.C. §119(a) 主张 **Chinese Patent Application Ser. No. 2023216251165**（**2023-06-06**） | [0001] |
| 申请人 / 发明人 | **Wu Guohui, Kowloon (CN)**（**个人申请人**，申请人与发明人同一人） | (71)(72)，逐字照抄 |
| IPC / CPC | **A61F 13/49**、**A61F 13/84**；CPC **A61F 13/49003**、**A61F 13/84**、**A61F 2013/8479**、**A61F 2013/8488** | (51)(52)，逐字照抄 |
| 附图 | Sheet 1–3 of 3（FIG. 1 系统示意、FIG. 2 爆炸图、FIG. 3 监控器电路功能框图） | 扉页 |
| 权利要求数 | **8 项**（1–8；**仅权 1 为独立权利要求**） | 权利要求书 |

### Sensor stack and architecture 传感器栈与架构

| Module 模块 | Content 内容 | Note 备注 |
|---|---|---|
| 主控板（3） | 连接并接收全部传感器信号；触发报警装置；管理通信模块与智能设备的通信 | [0041] |
| 电池（31） | 与主控板电连接，为板、传感器及其他电子元件供电 | [0040] |
| 体温传感器（35） | 监测体温；异常（如发热）时报警并向智能设备发送读数 | [0045] |
| 湿度传感器（36） | 连接监控器背面的**导电弹簧针（361）** | [0046] |
| 气味传感器（37） | 用于**检测粪便**；可选传感器列举：**H2S、NH3、C8H7N、C9H9N、CH3COOH、C4H8O2、H2、CH4** | [0047]，逐字照抄 |
| 运动传感器（38） | **三轴或六轴加速度传感器**，监测运动状态尤其是**睡姿** | [0048] |
| 报警装置（32） | **扬声器 + LED 灯**（声音与闪光），原文称可向监护者主动报警 | [0026][0042] |
| 通信模块（34） | **Bluetooth 或 WIFI**，近距离或远距离与智能设备（智能手机、平板电脑）通信 | [0044] |
| GPS 定位器（39） | 追踪行走活动与位置信息 | [0049] |
| 酶检测模块（340） | 连接主控板与导电弹簧针；尿裤本体上设有**酶试纸（4）** | [0050] |
| 控制按键（33） | 控制电源开关、报警装置启停、通信模块连接 | [0043] |
| 弹性夹（21） | 位于监控器背面，用于**可拆卸夹紧**在尿裤上，保证弹簧针与线缆紧密接触 | [0033][0038] |

### Diaper-body construction 尿裤本体结构

| Layer 层 | Content 内容 |
|---|---|
| 防水层（11） | 最外层；在对应弹簧针处**开孔**，露出导电线缆 |
| 导电层（12） | 内含**导电线缆（121）**，呈**纵横交错的栅格状**（grid-like pattern of intersecting vertical and horizontal stripes） |
| 吸水层（13） | 承载**酶试纸（4）**，试纸与导电线缆电连接 |

**尿液检测原理（[0046]）**：监控器装上后，防水层开孔对准导电弹簧针 → 弹簧针接触导电线缆 → 构成回路；**当尿裤本体有尿液时，尿液渗入导电线缆，改变其电阻**；主控板**检测到电阻变化**即判定有尿，触发报警并经通信模块上报智能设备。

**酶检测原理（[0050]）**：酶试纸置于吸水层并与导电线缆电连接；尿液渗入试纸 → **电阻变化** → 电流经导电线缆传至酶检测模块 → 分析电阻值判定**尿酸含量**。原文称可按需更换为**总胆固醇试纸或高密度脂蛋白胆固醇试纸**。

## Drafting defects 撰写缺陷（客观记录）

> 以下三处为原文自身的文本问题，逐条记录，**不作任何法律效力推断**。

| # | Defect 问题 | Location 位置 |
|---|---|---|
| 1 | 权 4 记载为"**The intelligent monitoring diaper of claim 4**"——自我引用（应为 claim 3 或 claim 1） | 权利要求 4 |
| 2 | 权 7 记载为"**The intelligent monitoring diaper of claim 7**"——自我引用（应为 claim 6） | 权利要求 7 |
| 3 | [0044] 称异常状态下向智能设备传送"**blood sugar readings**（血糖读数）"，但**全文未记载任何血糖/葡萄糖传感器** | [0044] |
| 4 | 权 8 称"**conductive spring needle**"，而摘要、权 1 与 [0046] 均用"**conductive pogo pin**"——同一元件的两种称谓 | 权 8 vs 权 1/[0046] |

## Key claims 关键论断

- **"可复用监控器 + 耗材导电层"是本件对智能尿裤成本问题的答案**：弹性夹 + 弹簧针实现"反复拆装"，一次投入的传感器栈在多片尿裤间复用。原文明确其益处为"**reduces costs while promoting environmental sustainability**"。这与本库 [[智能尿裤功能层]] 讨论的"功能层成本与一次性化矛盾"是同一问题的两种解法。→ [[Sensor-Equipped Absorbent Article（含传感器吸收性物品）]]
- **检测走电阻法而非光学法**：尿渗入 → 导电线缆**电阻变化**。相较本库的光散射/变色路线（[[Light-Scattering Masking Wetness Indicator（光散射遮蔽型尿湿指示）]]、[[Wetness Indicator Ladder（尿湿指示阶梯）]]），优点是可**量化并数字化上报**，代价是需在尿裤内**增设导电层与栅格线缆**。
- **气味传感器被用来判定"是否有粪便"**：原文列举 8 种可测气体（H2S、NH3、吲哚 C8H7N、粪臭素相关 C9H9N、乙酸、丁酸相关 C4H8O2、H2、CH4）。这是本库 [[BM Urine Indicator Concept（尿+便双指示概念）]] 之外的一条**电子鼻式**路径。
- **酶试纸被电气化**：试纸电阻变化经导电线缆回传，可测尿酸；原文还提到可换为胆固醇类试纸。属于"**把生化检测并入同一电气接口**"的扩展设计。

> 🔴 **manual_review（2026-09-29）**：**本页仅为美国发明申请公开文本的客观摘录，不构成 FTO（自由实施）或侵权判断。**
> - **法律状态记录（2026-09-29）**：本件为 **A1 申请公开**（公开日 2025-02-27，申请号 18/455,603，申请日 2023-08-24）。**是否已被授权、审查过程、是否存在延续案/分案、期限调整（35 U.S.C. §154(b)）情况 → 来源未记载，一律标 `[待验证]`**。
> - **上方"撰写缺陷"四点为客观文本记录，不构成对本件有效性或可实施性的任何结论**；其法律后果须由专利代理或法务独立评估。
> - **AI 不得判断我方智能尿裤/传感方案是否落入本件保护范围**，须由中美专利代理或法务独立评估。
> - **credibility 定为「中」**：文件为个人申请人的申请公开文本，**全部为书面披露，无实施例数据、无试验验证、无第三方验证**；且含上述自我引用与体内不一致之处。

## Related pages 关联页面

- Concept 概念：[[Sensor-Equipped Absorbent Article（含传感器吸收性物品）]]、[[智能尿裤功能层]]、[[Wetness Indicator Ladder（尿湿指示阶梯）]]、[[Light-Scattering Masking Wetness Indicator（光散射遮蔽型尿湿指示）]]、[[BM Urine Indicator Concept（尿+便双指示概念）]]、[[Diaper Microclimate]]

## Original 原文

- Local path 本地路径：`RAW/ima_sync/个人知识库/WKB/Areas/IP/六-1_Intelligent_Monitoring_Diaper_with_Enhanced_Features.pdf.md`
- Original link 原文链接：（无；专利文献）
- Note 备注：原文 FIG. 3 为图片，其 OCR 文字块被压缩为一行（含 `Enzymne test piece`、`Conductive cables`、`warning device`、`Humidity sensor`、`conductive pogo pin`、`Enzyme detection`、`Main control board`、`Odor sensor`、`Communication module`、`Battery`、`Motion sensor`、`GPS locator` 等标签）。本页的模块编号与连接关系以**说明书正文 [0038]–[0050]** 为准，图中标签仅作旁证。
- Note 备注（实体页）：申请人为**个人（Wu Guohui）**而非企业，本库**不为其单建实体页**（与本批次 [[US20220125319A1 Moisture and Fever Sensing Apparatus (Farnaz Zand)]] 的处理一致），仅在源页逐字记录其姓名与地址。
