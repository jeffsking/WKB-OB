---
type: source
title: "Industrial Drying Ch32 Drying of Peat and Biofuels"
source_type: book
source_path: "RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Handbook of Industrial Drying/ID · analysis_ch32.md.md"
date_published: 2014
date_processed: 2026-09-30
credibility: 高
knowledge_update_status: done
key_claims:
  - "Drying a moist fuel before firing is not obviously economical: 'It is not obvious that a moist fuel must be dried before firing. On the contrary, this is considered uneconomical in many cases.' (p.743)"
  - "Moisture dictates combustion performance: at 65/50/15% MC the higher calorific value stays 20.6 MJ/kg while adiabatic combustion temperature rises 900→1200→1800 °C and boiler efficiency (lower value) rises 0.85→0.89→0.93 (Table 32.1, p.741)"
  - "Flue-gas drying shows marginal returns past ~100 °C exhaust: 'Further drying leads to marginal savings only, due to the decrease in the amount of excess air.' (p.744)"
  - "Wood is a moderately hygroscopic material below about 0.3 MC, at which free water has been removed and the residue is cell-bound water; hygroscopicity is of rather limited importance for the drying process (p.750)"
  - "Biofuel-drying kinetics are largely empirical: 'Rather few papers deal with the kinetics of biofuel drying and most designs seem to be experience-based.' (p.751)"
  - "Storage biological threshold: to avoid significant microbiological degradation during storage, material should be dried to 20–25% MC (p.742)"
summary_cn: "把泥炭/生物质干燥作为燃烧前能源系统集成问题处理：阈值驱动、热力学三路线（烟气/过热蒸汽/双效）、四大干燥机族与经验型动力学，对卫材仅有'自由水vs结合水阈值'一座窄桥。"
tags: ["source/book", "drying/biofuels", "energy-integration", "moisture-threshold", "bulk-solids"]
tags_zh: ["书籍来源", "生物质干燥", "能源集成", "水分阈值", "散粒体"]
domain: "hygiene-materials"
priority: "P0"
pages_linked: ["[[Handbook of Industrial Drying]]", "[[Industrial Drying Ch28 Osmotic Dehydration and SAP Physics]]", "[[Industrial Drying Ch31 Drying of Ceramics]]", "[[Industrial Drying Ch33 Drying of Fibrous Materials]]", "[[Industrial Drying Ch35 Drying of Pulp and Paper]]"]
---

# Chapter 32 — Drying of Peat and Biofuels

> Source: Mujumdar (ed.), Handbook of Industrial Drying, 4th ed., CRC Press, 2014, Ch.32, pp.741–751 (span derived from quoted pages; to be verified against print).
> Author: Roland Wimmerstedt.
> 注：页码按 PDF 页 − 21 推算（锚定 Ch.1 = p.1），与印刷版核对前属推算值；源文件中版权年标注为 2015，本批统一按 2014 版处理。

## Scope & Position 范围与定位

Drying framed as a pre-combustion energy-systems problem, not materials science. Three drivers: (1) lower fuel moisture to raise boiler efficiency/capacity; (2) process thresholds (gasification ~15% MC, suspension firing, briquetting 10–20% MC); (3) storage degradation control.
"Peat produced directly from the bog contains 80 to 95% water (counted on the total mass), which is reduced to about 50% through natural drying on the bog during summer." (p.741) → 最便宜的脱水永远是机械/自然手段。
定位：与 Ch31/Ch33 相反的另一极 — 进料惰性、粗颗粒、相关尺度上无孔，干燥是净能量收益问题；"don't over-dry"由能量回报驱动，而非产品质量。

## Why / When / How 论证结构 (§1–4)

- **Why dry?** "It is not obvious that a moist fuel must be dried before firing. On the contrary, this is considered uneconomical in many cases." (p.743)
  Table 32.1 (p.741): 65/50/15% MC → 高位热值恒 20.6 MJ/kg，绝热燃烧温度 900→1200→1800 °C，锅炉效率（低位）0.85→0.89→0.93。
- **When?** 阈值驱动：气化 ~15% MC；储存防微生物降解 "the material should be dried to a moisture content of 20 to 25%" (p.742)。
- **How?** 三条热力学路线：
  - Flue-gas 干燥：降至 ~100 °C 排温即得主要收益，"Further drying leads to marginal savings only, due to the decrease in the amount of excess air." (p.744)；烟气 170 °C 显热可将 60% MC 燃料干至 ~55%（Fig. 32.2）。
  - 过热蒸汽干燥："The economy of the dryer is dependent on whether or not the low-pressure steam can be used in the process." (p.745)；4–5 bar 蒸汽压力下容量约为 12–25 bar 的两倍；无工艺用途时 MVR（如 270 kWh/t DS）。
  - 双效（Peco）：蒸汽 ~4 atm，比汽耗 0.65–0.70 kg 汽/kg 蒸发水。
- **Equipment?** rotary → cascade → pneumatic/flash → fluid-bed steam，按粒径与通量匹配。
- **Cost/risk?** VOC/萜烯排放；"The condensate in biofuel dryers is acidic and corrosive. All parts of the dryers, where condensation can take place, must be either lined or manufactured in stainless steel materials." (p.750)；可运行率：烟气型 80%+ vs 蒸汽型 35–90%。

## Equilibrium & Kinetics 平衡与动力学 (p.750–751)

"Wood is a moderately hygroscopic material at moisture contents below about 0.3, at which the free water has been removed and the residue can be regarded as cell-bound water." (p.750)
"The shapes of the isotherms are similar to those of wood and imply that most of the water is not strongly bound. It can be concluded that the hygroscopicity is of rather limited importance for the drying process." (p.750)
"Rather few papers deal with the kinetics of biofuel drying and most designs seem to be 'experience-based.'" (p.751)
→ 动力学：颗粒内阻力 ∝ 粒径；其余凭经验。滞后现象存在但结合弱。

## Limitations 局限

- 几乎无机理动力学模型；插图为低分辨率扫描、OCR 轴标受损。
- 北欧/泥炭偏重，普适性受限。
- 只讲热力干燥经济学，未正式化"先机械脱水再热力干燥"的能耗对比 — 对工艺工程师是最大缺憾。
- 与卫材的非迁移部分（明确排除）：锅炉集成、萜烯 VOC 治理、悬浮燃烧 MC 限值、Peco/MVR 经济性。

## Hygiene Implication 卫材关联

总评：★★☆☆☆（弱相关 — 能量/散粒体章节；仅一座真桥，诚实评估不拔高。）

- **★★★ 自由水 vs 结合水给浆板采购一个物理正确的词汇表**：木/浆在 MC≈0.3 以下才进入"细胞结合水"区（p.750）。审核绒毛浆供应商 MC 指标时，区分"表面自由水（压榨即可廉价脱除）"与"结合水（需能量）"，并据此设定来料 MC 验收线。
- **★★☆ 卷浆水分的阈值纪律**：干燥越过阈值后边际收益急剧下降（p.744 的 100 °C 悬崖）。绒毛浆卷浆 MC（典型 5–10%）由压榨+部分热干燥设定；不要用"越干越好"的笼统指标，先量化把 MC 压到自然平衡以下所需的蒸发能耗 — 避免为压榨+平衡已能实现的降水分支付蒸发能量。
- **★★☆ 冷凝水腐蚀审计迁移**：酸性冷凝水要求不锈钢/衬里（p.750）。若卫材转换线使用蒸汽/冷凝水回路烘纸幅，审计冷凝水酸性（添加剂/香精挥发分带入）— 预防烘缸腐蚀失效。
- 适用性边界：本章物理是散粒多孔体+重力/强制对流，无毛细压力模型、无结合水解吸能学、无聚合物/溶胀固体处理；唯一桥梁就是 p.750 那句细胞结合水。勿强行引用。

## Related Sources 关联来源

- [[Handbook of Industrial Drying]]
- [[Industrial Drying Ch28 Osmotic Dehydration and SAP Physics]]
- [[Industrial Drying Ch31 Drying of Ceramics]]
- [[Industrial Drying Ch33 Drying of Fibrous Materials]]
- [[Industrial Drying Ch35 Drying of Pulp and Paper]]
