# WKB-OB 断链修复报告 · 2026-09-30

**结论：302 处断链 → 0**

---

## 修复前基线

| 指标 | 值 |
|---|---|
| WIKI 页数 | 1333（sources 836 / concepts 280 / entities 137 / comparisons 80） |
| 断链 | **302 种目标 / 650 处引用** |
| 来源 | S1–S7 收官后的存量 seed 缺口 + Wave 2/3（工业干燥、P1）新页引入 |

## 三段式修复

### ① 改指 46 种（182 处引用）—— 仅同名变体

| 类别 | 示例 |
|---|---|
| 归一化命中 | `SAP`→`SAP（高吸水树脂）`(45)、`导流层 ADL`→`ADL（导流层）`(22)、`绒毛浆 Fluff Pulp`→`绒毛浆（Fluff Pulp）`(17)、`面层 Topsheet`→`Topsheet（面层）`(7)、`Kimberly-Clark`→`Kimberly-Clark（金佰利）` |
| 家族收敛 | SAP 四变体（`SAP Superabsorbent Polymer` / `Superabsorbent Polymer 高吸水树脂` / `Synthetic Superabsorbent Polymers` / `SAP Composites`）→ 统一指向 `SAP（高吸水树脂）` |
| 分册改名 | `Adhesive Handbook Part 2 Adhesion Science`→`Part 2 Fundamental Aspects`；`Part 3 Polymer Chemistry`→`Part 3 Adhesive Classes` |
| 温致变色 | `热致变色 Thermochromic` / `温致变色 Thermochromic` → 既有 `热致变色` |
| 同义组合并（9 组） | Nonwoven×3→`Nonwoven 非织造布`；`水刺 Spunlace`→`水刺 Hydroentanglement`；`热熔胶 Hot Melt`→`热熔胶 Hot Melt Adhesive`；`气流成网 Airlaid`→`气铺 Airlaid`；`交联密度 Cross-link`→`Crosslink`；`光致变色 Photochromism`→`Photochromic`；`保水值 WRV`→`WRV 水保留值`；`刺激响应材料`→`刺激响应聚合物 Stimuli-Responsive Polymer`；`双组分纤维 Bicomponent Fiber`→`Bicomponent` |

### ② 建 seed 页 256 个（概念 247 / 实体 9）

模板固定，**未填任何数据**：

```yaml
type: concept | entity
title: "<= 文件名>"
domain/category: [待补]
status: seed          # entity 用 relationship: 待核
updated: 2026-09-30
tags: [seed, 待补]
```

正文仅含：Seed 声明（明示「未填数据、须回来源核对、禁止编造」）+ 引用来源清单（去重，≤12 条）+ 待补维度 + 关联来源。

**引用频次 Top 12**

| 目标 | 引用 | 目标 | 引用 |
|---|---|---|---|
| 吸收芯体 | 23 | 液晶 Liquid Crystal | 8 |
| 光致变色 Photochromic | 14 | 智能织物 Smart Textile | 8 |
| 回渗 Rewet | 13 | 双组分纤维 Bicomponent | 7 |
| 机械变色 Mechanochromic | 13 | 熔喷 Meltblown | 6 |
| 达西定律 Darcy's Law | 10 | 纺粘 Spunbond | 6 |
| 热致变色 Thermochromic | 9 | 非织造布 Nonwoven | 6 |
| Fick 定律 | 9 | 结构色 Structural Color | 6 |

新建实体页（9 → 修正后 6）：BASF、OxyChem、Henkel、Sun Chemical、PPG Industries、Koch Industries。
（3 个误判为 entity 的已改回 concept：`超分子 Host-Guest Chemistry`、`变色材料 Chromic Materials`、`Polyolefin Absorbent Materials`）

### ③ 手工收尾 2 处

- `Handbook of Adhesive Technology Full Report.md` 的 `pages_linked` 写成畸形 `[[[X]], ...`（缺引号）→ 修正为合法引号列表
- `[[每克厚度 T/W]]` 半角 `/` 不可作文件名 → 页面落地为全角 `每克厚度 T／W.md`，改写源页链接匹配

---

## ⚠️ 记录在案的方法论错误（已写入 skill 铁律）

首轮尝试用 **token-overlap 重合度自动匹配** 做改指，产出把**上位概念窄化到下位页**的错误：

| 错误改指 | 问题 |
|---|---|
| `光致变色 Photochromic` → 某供应商调研报告 | 概念 → 具体报告 |
| `BASF` → `BASF Biomass Balanced Superabsorbents 产品页` | 公司 → 单一产品页 |
| `Sun Chemical` → `Chemical bonding` | 完全无关 |
| `热熔胶 Hot Melt` → `Polyolefin Hot Melt Adhesive` | 泛称 → 特定品类 |
| `湿巾 Wet Wipes` → `GB-T 27728-2011 Wipes` | 品类 → 某标准 |
| `非织造布 Nonwoven` → `Meltblown Nonwoven` | 上位 → 下位 |

→ **改指只允许「同名变体」；语义近似一律建 seed 页。**

---

## 终态

| 指标 | 值 |
|---|---|
| WIKI 页数 | **1589**（sources 836 / concepts 530 / entities 143 / comparisons 80） |
| **断链** | **0** ✅ |
| front matter | **1589 / 1589 通过** |
| index.md 对齐 | **1589 / 1589** |

备份：`.tools/_wiki_backup_20260930/`（修复前全量 WIKI）

## 工具

| 文件 | 用途 |
|---|---|
| `.tools/_link_triage.py` / `_link_triage2.py` | 断链分级（改指 / 待裁决 / 需建页）+ 候选评分 |
| `.tools/_fix_links_all.py` | 改指 + seed 生成，幂等，支持 `--apply` |
| `.tools/_link_fix_plan.json` | 修复计划（改指表 / seed 清单） |
| `.tools/_link_fix_result.json` | 修复结果（新建页全清单） |

## 遗留

- **530 个 seed 页待按引用来源补齐真实内容**（优先：吸收芯体、回渗 Rewet、达西定律、Fick 定律）
- 261 条 manual_review 待集中裁决
- P0 工业干燥 40 章未编译
