# SEED 去重（第二轮）+ concepts 库分类审计 · 2026-10-12

**触发**：王总 22:08 批评 —— 不该靠名字猜，应**读库内 concept 定义**做语义判断；并要求继续过完剩余 SEED、回顾库内 concepts 分类。
**方法论纠正**：先建 **concept 语义档案**（title + domain + status + 定义首句，673 页），再做语义判断。

---

## 一、结论

| 事项 | 结果 |
|---|---|
| 剩余 SEED 逐条核对 | **111 条** → **19 条改指既有页** + **3 条占位符** + **89 条保留待建** |
| 断链 | 111 → **89 种**（本轮 −22；今日累计 **129 → 89**） |
| **concepts 库结构** | ⚠️ **133 个 domain 变体**，其中 `hygiene-materials` 一档塞 **261 页（49%）** → **分类体系崩坏** |
| **疑似重复 concept** | **35 对高相似**（ratio≥0.72），其中 **≥14 对为同一概念两页** |

---

## 二、本轮 19 条改指（SEED → 既有页）

| SEED | → 既有页 |
|---|---|
| `无纺布` | `Nonwoven 非织造布` |
| `SMS无纺布` | `SMS 复合无纺布` |
| `水刺` | `水刺 Hydroentanglement` |
| `TBCW在线超声波复合工艺` | `TBCW结构` |
| `SAP 表面交联` | `表面交联 Surface Cross-linking` |
| `水变油墨` | `Water-Activated Ink（水变／湿变油墨）` |
| `裤型纸尿裤` | `Pant-Type Disposable Absorbent Article（裤型一次性吸收物品）` |
| `Liner（面层）` | `Topsheet（面层）` |
| `气味管理` | `Odour Management Routes（气味管理技术路线）` |
| `Open Innovation` | `Material Open Innovation Function（材料开放创新职能）` |
| `纳米纤维素` | `纳米纤维素（CNC、CNF、BNC）` |
| `PTT` | `PTT（聚对苯二甲酸丙二醇酯）` |
| `PVA` | `PVA纤维（湿强骨架）` |
| `莱赛尔` | `莱赛尔 Lyocell` |
| `华峰集团` | `华峰集团（Huafon Group）` |
| `诺尔` | `诺尔（Nuoer）` |
| `紫华公司` | `紫华公司（Zihua, Zijiang Group）` |
| `维盛集团` | `新维盛集团（Xinweisheng Group）` |
| `Huayi集团` | `Huayi Group（待核中文名）` |

**占位符 → 纯文本（3）**：`推断`、`实体`、`对比页`（均引用自会议纪要，是**页面类型名/动作词**被误当链接）。

> 上一轮已处理 11 条 + `图片类条目`。**两轮合计：30 条 SEED 实为重复/占位符**，占优先项 20 条的 60% + 其余批次的对应项。

---

## 三、concepts 库结构审计

### 3.1 domain 分类崩坏

- **133 个 domain 变体**，其中 **261 页（49%）** 共用最笼统的 `hygiene-materials`。
- 其余 267 页散在 **132 个细碎 domain**，风格不统一：
  - 英文单值：`hygiene-materials`、`供应商`
  - 中文数组：`[卫材研发, 芯体结构]`（20）、`[卫材研发, 测试与验收]`（18）
  - 占位：`[待补]`（7）、`[卫材研发]`（18，无二级）
  - 过度细分：`[卫材研发, 智能功能化, 高吸水树脂, 测试方法]`（1 页独占一档）等

### 3.2 架构问题

| 问题 | 表现 |
|---|---|
| **大杂烩 domain** | `hygiene-materials` 261 页 —— 从 `Nanoparticle` 到 `83 换型要素` 全塞一起，失去分类意义 |
| **同概念多 domain** | `热致变色 Thermochromic` 在 `hygiene-materials`；`热致变色` 在 `[待补]` |
| **一页一 domain** | 大量 domain 仅 1 个成员 → 等于没分类 |
| **命名风格混用** | 中/英、单值/数组、有「待补」 |

---

## 四、疑似重复 concept（35 对高相似，摘录）

### 4.1 同一概念两页（**建议合并**，≥14 对）

| 相似 | 页 A | 页 B |
|---|---|---|
| 0.98 | `毛细压力 Capillary Pressure` | `毛细管压力 Capillary Pressure` |
| 0.97 | `83 Changeover Four-Layer Architecture（…）` | `Changeover Four-Layer Architecture（…）` |
| 0.91 | `干燥角质化 Hornification` | `角化 Hornification` |
| 0.91 | `Hot Melt Adhesive` | `热熔胶 Hot Melt Adhesive` |
| 0.89 | `Contact Angle` | `接触角 Contact Angle` |
| 0.88 | `Silane Coupling Agent` | `硅烷偶联剂 Silane Coupling Agent` |
| 0.86 | `Stimuli-Responsive Polymers` | `刺激响应聚合物 Stimuli-Responsive Polymer` |
| 0.83 | `热风无纺布` | `热风粘合无纺布` |
| 0.80 | `胶乳 Latex` | `胶乳胶黏剂 Latex` |
| — | `热致变色 Thermochromic` | `热致变色`（英中对照差异，未入 35 对） |
| — | `芯体通道花型设计` | `Core Channel Pattern（芯体通道花型设计）` |
| — | `SMS 复合无纺布` / `SMS 纺粘熔喷复合` / `SMS复合结构` / `纺粘熔喷 Spunbond-Meltblown` | **4 页同族** |
| — | `摩擦电自供电 TENG` | `摩擦纳米发电机 TENG` |
| — | `PSA` | `压敏胶 PSA` |

### 4.2 上下位关系（**不可合并**，应互链）

`吸收芯体` ⊃ `复合吸收芯体`｜`胶黏剂 Adhesive` ⊃ `生物胶黏剂`｜`机械变色` ⊃ `Mechanochromic变色纤维`｜`纳米纤维素` ⊃ `细菌纳米纤维素`｜`热风无纺布` ⊃ `热粘合热风无纺布 Airlaid`

### 4.3 同族/相邻（**不可合并**）

`Motion/Static/Mannequin BM Test`（三种假人法）｜`光致变色` / `光致变色油墨`（材料 vs 应用）｜`热致变色` / `电致变色`｜`CoPET` / `PET`｜`湿强剂` / `湿态强度`

---

## 五、验证

| 项 | 结果 |
|---|---|
| guard `check` 断链 | **89** ✅ |
| front matter | **2155 / 2155** ✅ |
| index 对齐 | 2155 / 2155 漏收 0 ✅ |
| apply | 改指 **20 处**；占位符转文本 **3**；seed 新建 **0**（纪律） |
| 白名单 | redirects **91** / block **30** / plain_text **6** |

---

## 六、建议（待裁决）

1. **合并 ≥14 对重复 concept**（§4.1）—— 用同一套 `source_paths` 合并纪律（AGENTS §1.1.4）。
2. **重构 domain 分类**：把 `hygiene-materials` 261 页按 MOC 的 11 域重新归类；废弃「一页一 domain」。
3. **89 条 SEED** 待建（已过语义去重，确认无既有页）。

---

_报告版本：v1（2026-10-12）。_
