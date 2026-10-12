# WKB-OB Seed 页补齐报告 · 2026-09-30

## 起点与首个纠正

断链清零后 `status: seed` 共 **447 页**。原以为它们全是空壳 —— **错**。

**`status: seed` 不等于没有内容。** S1–S7 收官批建的 161 页里，大量页面已有完整正文，只是 status 没改：

| 页面 | 实际内容 |
|---|---|
| `Residual Fluid & Pore Stranding（残液与孔隙滞留）` | 9 条机理（Young-LaPlace / PSD / 层间空隙 / 包裹层…） |
| `Changeover Four-Layer Architecture` | 四层划分完整表 + 第一原则原文 |
| `Repitch（鼓距与产品节距解耦）` | 定义表 + `P = πD/n` 推导 |

→ 批量改标 `status: growing`，**161 页**，未动一个字的正文。

### 第二个纠正：我的"空白"统计写错了

首版脚本算内容量时把 `^[#>|\-*]` 开头的行全删 —— **把表格行和列表项一起删了**。表格密集型的 legacy 页因此被误判成"空白"，虚报出 355 个缺口。改版只去掉 seed 横幅和纯链接行后：

| 口径 | 真空白数 |
|---|---|
| 首版（错误） | 355 |
| 修正后 | **174** |

---

## 本轮成果

### ① 填充 104 页（严格"只引库内实证、禁编造"）

**引用 ≥2 的 92 页 100% 完成**：

| 页面 | 原引用 | 页面 | 原引用 |
|---|---|---|---|
| 吸收芯体 | 23 | 液晶 Liquid Crystal | 8 |
| 光致变色 Photochromic | 14 | 智能织物 Smart Textile | 8 |
| 回渗 Rewet | 13 | GB-T 28004-2011 | 7 |
| 机械变色 Mechanochromic | 13 | SAM Distribution Test | 7 |
| 刺激响应聚合物 | 11 | 芯体通道花型设计 | 7 |
| 达西定律 Darcy's Law | 10 | 交联密度 Crosslink Density | 6 |
| Nonwoven 非织造布 | 10 | 水刺 / 熔喷 / 纺粘 | 6 |
| Co-extruded Elastic Film | 10 | 结构色 Structural Color | 6 |
| 83 Changeover 四层架构 | 10 | Daehyun / Shin-Etsu | 6 |

另补 12 页引用=1 的高价值概念（聚合物刷、中空纤维、爆裂纤维、鸡毛纤维、自由体积、导电无纺布、热风非织造、Nonwoven Lamination、过滤材料、植物基材料、变色材料、Polyolefin Absorbent Materials）。

**每页统一结构**：Definition 定义 / Key Parameters（逐值带 `（源：[[…]]）`）/ Method·Mechanism / Hygiene Relevance / Open Questions 待补 / Related Sources。

举例 —— `回渗 Rewet` 携 11 行带源数据（加液压力跨方法 0–0.53 psi、单亲 vs 多亲面层 3.89–6.17 g vs 0.84–1.32 g、AD 面层互换 0.51→0.15 g、五项目实测战绩），并诚实标出「U Rewet 压块质量未知」「HPR <0.3 g 机理未确认」。

### ② 重复页处理（**未删任何页**）

**合并 6 对**（一方为真 stub）—— 全库入链改写为 canonical（涉及 19 个文件），stub 转为 `status: merged` **指针页** + manual_review 提示：

| Stub | Canonical |
|---|---|
| `热致变色` | `热致变色 Thermochromic` |
| `Contact Angle` | `接触角 Contact Angle` |
| `Hot Melt Adhesive` | `热熔胶 Hot Melt Adhesive` |
| `毛细管压力 Capillary Pressure` | `毛细压力 Capillary Pressure` |
| `2025.06.25 - Learning Cycle Check In` | `GRIFFIN Learning Cycle Check In` |
| `SymDeo™ XPP 抑臭聚合物` | `Symrise SymDeo™ XPP 抑臭聚合物（中文版）` |

**标记 2 对双方均有内容的重复**（不自动合并，交人工裁决）：`Changeover Four-Layer Architecture` ↔ `83 Changeover …`；`Repitch（鼓距与产品节距解耦）` ↔ `82 鼓距与产品节距解耦 repitch 选型`。

### ③ 三处已记录的方法论问题

1. **`status: seed` 不可信** → 必须先测内容量（见上）。
2. **digest 关键词匹配会跑偏** —— `过滤材料` 命中液晶/热电摘录、`爆裂纤维` 命中通用纤维表征。已要求代理回 cited-by 来源页核对原文、弃用跑偏摘录；**根治需给 digest 加主题词白名单**。
3. **统计口径会自欺** —— 剔除表格行导致 355 vs 174 的错误缺口。

---

## 终态

| 指标 | 值 |
|---|---|
| WIKI 页数 | **1589**（sources 836 / concepts 530 / entities 143 / comparisons 80） |
| **断链** | **0** ✅ |
| front matter | **1589 / 1589 通过** |
| index.md 对齐 | **1589 / 1589** |
| seed 页 | 447 → **176**（已补 104 + 重标 161 + 合并 6） |

## 工具链

| 文件 | 用途 |
|---|---|
| `.tools/_seed_inventory.py` | 盘点 seed 页 + 引用频次 |
| `.tools/_seed_classify2.py` | **精确**测内容量（保留表格/列表行） |
| `.tools/_gen_seed_digests.py` | 为每页生成原文摘录 → `.tools/_seed_ctx/`（447 份） |
| `.tools/_seed_dupes.py` | 检测重复 seed（Jaccard） |
| `.tools/_consolidate_seed_dupes.py` | 合并（改写入链 + stub 转指针页，不删） |

备份：`.tools/_page_backup_dupes/`

## 待办

- **176 个真 seed 页**按 `.tools/_seed_ctx/` digest 继续补齐（按 digest 内容丰富度排序即可）
- 4 页重复待人工裁决
- P0 工业干燥 40 章未编译
- 261 条 manual_review 待集中裁决
