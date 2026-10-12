---
type: source
title: "{{资料标题}}"
source_type: 研报 | 公众号 | 会议纪要 | 报价单 | 行业新闻 | 工作日志 | 专利 | book
source_path: raw/ima_sync/{{相对路径}}
original_link: "{{原文链接，无则留空}}"
date_published: {{YYYY-MM-DD}}
date_processed: {{YYYY-MM-DD}}
credibility: 高 | 中 | 低        # 仅限三档信任层级；来源/工序描述写入 credibility_note
knowledge_update_status: pending | done | manual_review
# —— 以下字段仅当 source_type: book（长文文档/电子书）时填写 ——
author: "{{作者/编者}}"
edition: "{{版次，如 3rd / 第2版}}"
publisher: "{{出版社}}"
year: {{YYYY}}
isbn: "{{ISBN，无则留空}}"
original_language: "EN | CN | 其他"
parent_book: "[[{{父书索引页标题}}]]"   # 章节页必填，指向该书索引页；整书索引页（book-index）留空
key_claims:
  - "{{核心论断1}}"
  - "{{核心论断2}}"
pages_linked: ["[[{{概念或实体页}}]]"]
---

# {{资料标题}}

## 一句话定位

{{这份资料解决什么问题、在库中的用途。1–2 句。}}

## 摘要

{{3–8 句，忠实于原文，不做外推。}}

## 提炼的数字与结论

| 项目 | 数值 / 结论 | 备注 |
|---|---|---|
| {{项}} | {{值}} | {{口径/日期}} |

## 关键论断（key_claims）

- {{论断}} —— 支撑页：[[{{页面}}]]

## 关联页面

- 概念：[[{{概念页}}]]
- 实体：[[{{实体页}}]]
- 对比：[[{{对比页}}]]

## 原文

- 本地路径：`{{source_path}}`
- 原文链接：{{original_link}}

---

## 附录：长文文档（电子书）编译约定

适用于 `RAW_FULL/.../Resources/Ebook/` 下的书籍、长篇论文、专利拆解、课件。蒸馏已分出两层：

- **整书文件**（Ebook 根目录，单文件可达 1.5MB / 数万行）→ **禁止当单页编译**（巨页不可用）。
- **章节提取**（`Ebook Extract/<书名>/`，已结构化带 Chapter Overview）→ 逐章编译为 source 页。

规则：

1. **章节页**：每章 = 1 个 `source_type: book` 的 source 页，`source_path` 指向该章节提取文件，`parent_book` 必填（指向该书索引页），`author/edition/publisher/year` 取自原书。
2. **父书索引页**：每本书 = 1 个 `source_type: book-index` 的 source 页（见 `TEMPLATES/book_index.md`），含 TOC（章节清单+链接）、书籍元数据、一句话综述，`pages_linked` 列全部章节页。
3. **整书独存（无章节提取）**：以单文档形式建 1 个 `source_type: book` 的 source 页（轻量，不当巨页展开）。
4. **重复整书**：若某书同时有整书文件与章节集，整书文件**跳过**，仅用作父书索引页的元数据来源。
5. `preview-` / `DeepRead` / `DeepBook` 等部分提取，编译前先核验完整性，节选内容需标注 `[节选/未全文]`。
6. 概念/实体页仅对高价值章节派生 1–2 个，不自动泛滥。
