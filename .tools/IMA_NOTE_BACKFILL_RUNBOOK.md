# IMA 条目正文回填 · 运行手册（方案 C）

> 配套根因报告：`.tools/IMA_NOTE_SYNC_ROOTCAUSE_2026-10-10.md`
> 建立日期：2026-10-10

## 为什么需要这条流水线

Obsidian 插件 `ima-copilot-sync v6.6.0` 取笔记正文只走 `openapi/note/v1/get_doc_content`：
- 该接口受**当日配额**限制，超量返回 `200005 请求超量，请明日再试`
- 插件把配额错误误判为永久失败（错误码白名单写的是 `20005`，少一位），且占位符写入后
  因 `if (a.has(i.media_id)) continue` **永不重试**

结论：**不要指望插件自愈**，正文必须由本流水线外部回填。

## 通道优先级

| 通道 | 命令 | 配额 | 用在哪 |
|---|---|---|---|
| **MCP**（首选） | `mcp__ima-mcp__fetch_media_content` | 无日配额（实测有效） | WorkBuddy **交互式会话** |
| REST（兜底） | `ima_api.cjs openapi/note/v1/get_doc_content` | 受日配额 | 会话未挂载 MCP 时 |
| REST 原件 | `get_media_info` → 签名 URL → curl | 宽松 | 附件类（需下载原件而非取文本） |

## 三条命令（清单 → 切片 → 验收）

```bash
PY="C:/Users/Chris Wang/.workbuddy/binaries/python/versions/3.13.12/python.exe"
cd "E:/WKB-OB"

# 1) 生成缺口清单 → .tools/_ima_note_gap.json
"$PY" .tools/ima_note_backfill.py --scan --kinds unsupported,attach_stub
#   只看"暂不支持"家族（笔记/录音/session/html/网页）：
"$PY" .tools/ima_note_backfill.py --scan --kinds unsupported

# 2) 按片切分给子代理 → .tools/_ima_note_slices/batch_NN.json
"$PY" .tools/ima_note_backfill.py --slices 14 --kinds unsupported,attach_stub

# 3) 覆盖率验收
"$PY" .tools/ima_note_backfill.py --verify
"$PY" .tools/ima_note_backfill.py --status --kinds unsupported,attach_stub
```

## 回填执行单元：子代理

正文可达数万字符（录音转写 40KB+、PDF 100KB+），**不要在主会话逐条调用**，会撑爆上下文。
派 `general-purpose` 子代理，每个 13~14 条，2~3 个并行。

子代理契约（照抄给代理）：

1. 读 `.tools/_ima_note_gap.json`，取 `items` 下标区间 `[a, b]`
2. `ToolSearch` → `tool_names: ["mcp__ima-mcp__fetch_media_content"]`
3. 逐条 `DeferExecuteTool`：`{"media_id": "<item.media_id>"}`，正文在返回的 `content` 字段
4. `Write` 到**绝对路径** `E:/WKB-OB/<item.full_path>`，front matter **严格固定**：

```
---
media_id: "<item.media_id>"
source_file: "<item.title>"
original_path: "<item.raw_path>"
extracted: "YYYY-MM-DD"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
---

<content 原文，原样保留，不改写/不翻译/不截断>
```

5. 无正文（无文字层图片、扫描件、空录音、数据文件）→ 仍写同路径，`extract_status: "empty"`，
   正文处写 `（IMA 侧无可用正文：<原因>）`。**empty 也算已处理，脚本会据此跳过，不会反复重跑。**
6. 硬约束：**绝不修改 `RAW/` 下任何文件**；不改其它文件；不复述正文
7. 回执只要表格：`序号 | 标题 | extract_status | 字节数` + 合计

## 落盘位置与幂等

- RAW 侧是占位壳（AI 只读红线），正文一律写 **`RAW_FULL/` 同相对路径**
- 幂等键 = 占位文件 front matter 的 `media_id`；脚本以 RAW_FULL 侧是否存在
  `extract_status: ok|empty` 判定"已处理"

## 通道 B：原件下载（图片/扫描件/Office 文件）

有些条目 IMA 侧**没有可提取文字层**（图纸类图片、扫描件 PDF、pptx/docx），
`fetch_media_content` 只能拿到空壳 —— 这时必须走**原件下载**。

```bash
PY="C:/Users/Chris Wang/.workbuddy/binaries/python/versions/3.13.12/python.exe"

"$PY" .tools/ima_fetch_originals.py --list        # 列出待下载原件
"$PY" .tools/ima_fetch_originals.py --run         # 执行下载（幂等，已存在则 SKIP）
"$PY" .tools/ima_fetch_originals.py --fix-ext     # 归一化：去 hash 后缀 + 按魔数纠正扩展名
"$PY" .tools/ima_fetch_originals.py --manifest    # 生成「原件 ↔ stub」配对清单
```

原理：REST `openapi/wiki/v1/get_media_info` → `data.url_info.url` + 签名 headers → GET 保存。
`url_info.url` 为 `chrome://...` 或为空时无法下载，脚本会 SKIP 并记录。

- **落盘位置**：`RAW_FULL/<原条目目录>/attachments/<原始文件名>`
  （用回原名而非 hash 后缀，便于 Obsidian 直接引用；`--fix-ext` 负责把扩展名纠正为真实类型）
- **幂等**：目标路径已存在即 SKIP
- **凭证**：读 `~/.config/ima/client_id` 与 `api_key`（REST 通道，不受 MCP 凭证加密限制）

### 取得原件后还要做「本地识读」

原件到手不等于内容可检索。清单生成后用**子代理**读原件、把内容写回 stub：

1. 图片 → Read 工具多模态读图；转录图中全部文字/编号/尺寸，再描述结构；区分「图中文字」与「推断」
2. 扫描件 PDF → Read 工具逐页读（支持 PDF 双通道：文字 + 视觉）
3. Office → `python-pptx` / `python-docx` 抽文字；DRM 加密的（如 `EncryptedPackage`）标记 `extract_status: "original-only"`
4. CSV → 直读，表头 + 行数 + 前若干行以 Markdown 表格内联

stub 的 front matter 增加 `original_file: "attachments/<文件名>"`，正文加：
- 图片：`![](attachments/<文件名>)`（Obsidian 内联渲染）
- 其它：`[打开原件](<attachments/<文件名>>)`（相对链接，尖括号可容纳空格与括号）

`extract_status` 取值：`ok`（已取得内容）/ `empty`（IMA 与原件均无内容）/ `original-only`（仅原件可看，内容需人工）。

## 已知边界（不必反复尝试）

| 现象 | 说明 |
|---|---|
| 图片仅返回单字符噪声（如 `8`） | 图纸类无可提取文字层（如 `Code *.jpg`），需改走原件下载通道 |
| `code 220030 文件获取失败` | IMA 侧该条目本身异常（如 `飞书` 笔记），需到 IMA 客户端处理 |
| `code 200005 请求超量` | REST 当日额度耗尽，**不要循环重试**，等交互式会话用 MCP |
| 录音无转写 | IMA 侧未生成转写文本，MCP 也取不到，需原件 + 本地 ASR |

## 与既有文档的关系

- 执行后按 `AGENTS.md` §3 编译入 `WIKI/`
- 操作留痕追加 `log.md`（追加式，勿覆盖）

## 2026-10-10 首次执行结果

- **通道 A（正文回填）**：「暂不支持」家族 **17 条**（12 取到正文 / 5 无正文）+ 附件类缺口 **40 条**（15 取到正文 / 25 无文字层）
- **通道 B（原件下载）**：**24 条**待下载原件全部成功（4 扫描件 PDF、14 图片、1 pptx、1 docx、4 CSV），已归一化命名
- **本地识读**：24 条 stub 全部回填 —— 3 份美国专利扫描件取得实质内容、1 份 `CN111134966A` 源文件截断（已在 stub 标注）、`1780441413150.jpg` 为幻灯片截图取得约 1100 字、4 个 CSV 内联 400 行数据、`NOTE.docx` 含手写图已识读、`REL_Optimized_PTT_PVA_Composition.pptx` 为 DRM 加密（`original-only`）
- **最终验收**：`--verify` 12 个类型**全部 0 缺口**；`RAW_FULL` 侧 **1240** 条有正文（原 1182）；`extract_status` 分布 = ok 1233 / original-only 1 / empty 6
