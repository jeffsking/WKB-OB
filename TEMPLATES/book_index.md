---
type: source
title: "{{书名}}"
source_type: book-index
author: "{{作者/编者}}"
edition: "{{版次}}"
publisher: "{{出版社}}"
year: {{YYYY}}
isbn: "{{ISBN，无则留空}}"
original_language: "EN | CN | 其他"
source_path: raw/ima_sync/{{整书文件相对路径，若无章节集则指向该文件；若有章节集可指向整书文件或留空}}
date_published: {{YYYY-MM-DD}}
date_processed: {{YYYY-MM-DD}}
credibility: 高 | 中 | 低
knowledge_update_status: done
summary_cn: "{{一句话中文综述}}"
key_claims:
  - "{{本书核心定位1}}"
pages_linked: ["[[{{章节页1}}]]", "[[{{相关概念页}}]]"]
---

# {{书名}} (Book Index 书籍索引)

> 父级索引页。本章节均链接到逐章编译的 source 页；禁止把整书正文塞入本页。

## Book Metadata 书籍元数据

| 项 | 值 |
|---|---|
| Author 作者/编者 | {{author}} |
| Edition 版次 | {{edition}} |
| Publisher 出版社 | {{publisher}} |
| Year 年份 | {{year}} |
| ISBN | {{isbn}} |
| Original Language 原文语种 | {{original_language}} |
| Relevance 相关性 | P0 / P1 / P2（对本库 REL/SAP/非织造/胶黏/变色材料主线） |

## One-line Summary 一句话综述

{{英文综述}}（中文：{{summary_cn}}）

## Table of Contents 章节目录

- [[{{章节页1标题}}]] — {{该章一句话}}
- [[{{章节页2标题}}]] — {{该章一句话}}
- …（按实际章节列出，全部内链到章节 source 页）

## Key Themes 核心主题

- {{主题1}}：见 [[{{章节页}}]]
- {{主题2}}：见 [[{{章节页}}]]

## Related Pages 关联页面

- 概念：[[{{概念页}}]]
- 实体：[[{{实体页}}]]
- 对比：[[{{对比页}}]]
