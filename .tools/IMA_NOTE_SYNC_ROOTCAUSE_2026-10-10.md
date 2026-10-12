# IMA 笔记无法同步进 Obsidian · 根因分析与解决方案

**日期**：2026-10-10
**范围**：`RAW/ima_sync/`（由 Obsidian 插件 `ima-copilot-sync v6.6.0` 维护）
**触发问题**：多数笔记显示「此条目为笔记，暂不支持自动同步内容」，但个别笔记（如 `会议纪要 Knight IV`）正文完整

---

## 0. 一句话结论

**这不是笔记本身的类型/位置/状态差异，而是插件唯一的「取正文」通道是一条受当日配额限制的 REST 接口。**
配额耗尽的调用会让插件写入占位符，而占位符一旦落盘就**永久不再重试**——所以只有极少数「配额尚存的幸运调用」拿到了正文。

---

## 1. 证据链

### 1.1 代码级（插件反混淆，`.obsidian/plugins/ima-copilot-sync/main.js`）

占位符文案由 `buildPlaceholder()` 用模板生成，类型名取自映射表 `Wr`：

```js
Wr = {1:"PDF",2:"网页",3:"Word 文档",4:"PPT",5:"Excel",6:"微信公众号文章",
      7:"Markdown",9:"图片",11:"笔记",13:"TXT",14:"Xmind"}

buildPlaceholder(l){
  let f = Wr[l.media_type] ?? `类型 ${l.media_type}`;
  return `---\nmedia_id: "${l.media_id}"\n---\n\n> 此条目为${f}，暂不支持自动同步内容。\n\n**标题**: ${l.title}`
}
```

知识库通道的完整分支（`syncKnowledgeItem`）：

```js
let info = await getMediaInfo(item.media_id);
if (info.media_type === 11 && info.notebook_ext_info?.notebook_id) {
    let md = await getNoteContentMarkdown(nid);   // = openapi/note/v1/get_doc_content
    return prependFrontmatterField(processContent(md, ...), "media_id", item.media_id);
}
if (info.url_info?.url) { ...下载网页/文件... }
if (Dn.has(info.media_type)) { ...重试 5 次... }
return this.buildPlaceholder(item);               // ← 占位符在这里产生
} catch(e) {
  if (er(e)) throw e;                             // 只有"限频类"错误才向上抛
  return this.buildPlaceholder(item);             // ← 其余错误一律降级为占位符
}
```

两个致命细节：

1. **占位符是永久性的**。知识库主循环里有：
   ```js
   if (a.has(i.media_id)) continue;   // 本地已有同 media_id 文件 → 整条跳过
   ```
   占位符文件的 front matter 里已写入 `media_id`，因此下一轮同步**直接跳过**，永远不会自愈。

2. **配额错误没被识别为"可重试"**。错误分类函数：
   ```js
   Di = new Set([200001, 20002, 110021, 20005]);      // 可重试错误码
   Oi = [/频率/,/限频/,/频控/,/限流/,/稍后重试/,/过于频繁/,/请求频繁/,
         /配额/,/每日/,/超限/,/rate\s*limit/i,/too many requests/i,
         /throttl/i,/quota/i,/daily/i,/retry later/i,/frequent/i];
   function er(e){ return e instanceof De ? (Di.has(e.code) || Oi.some(r=>r.test(e.message))) : false }
   ```
   实际配额错误是 **`200005` + 「请求超量，请明日再试」**：
   - `Di` 里写的是 `20005`（**少一位**，不匹配 `200005`）
   - 消息正则里有 `/超限/` 却没有 `/超量/`，有 `/稍后重试/` 没有 `/明日再试/`
   → `er()` 返回 false → 不重试、不中断，**直接写占位符继续下一条**。

### 1.2 API 级（今日实测）

调 REST `openapi/wiki/v1/get_media_info`：成功笔记与失败笔记的返回**完全同构**。

| 笔记 | media_id 尾号 | media_type | notebook_ext_info.notebook_id |
|---|---|---|---|
| 会议纪要 Knight IV（**成功**） | 7507100590678332 | 11 | 7507100590678332 ✓ |
| 会议纪要：V6产品开发技术研讨会（**失败**） | 7507101203046818 | 11 | 7507101203046818 ✓ |
| 会议纪要一（**失败**） | 7507092344697181 | 11 | 7507092344697181 ✓ |

→ 三条笔记类型相同、`notebook_ext_info` 均存在、创建时间仅相差 2~33 分钟、位于同一目录。
**可以排除「按条目属性区分」的解释。**

调 REST `openapi/note/v1/get_doc_content`（即插件的取正文接口）：

```
{"code":200005,"msg":"请求超量，请明日再试","data":{},...}
```
连续 4 次调用全部 200005 → 当日配额已耗尽（与 `log.md` 记录 10-02 起连续 6 天超量一致）。

### 1.3 数据级（本地落盘实况）

`RAW/ima_sync/` 中带 `media_id: note_` 的条目共 **84** 条：

| 状态 | 数量 | front matter 形态 | 来源 |
|---|---|---|---|
| 有正文 | **12** | 仅 `media_id` | 插件通道成功（11 条 09-28、1 条 10-02 Knight IV） |
| 占位符 | 72 | `media_id` + 提示语 | 插件通道失败 |

镜像侧 `RAW_FULL/ima_sync/` 另有 **61** 条 note 条目，**全部有正文** —— 这批是 09-30 人工 MCP 回填的结果，证明"内容取得到，只是插件取不到"。

`log.md` 记载 IMA 笔记区共 **127** 条 → 当前 vault 有 84 条 note 条目，**约 43 条从未进入知识库**（不出现即不参与同步）。

---

## 2. 失败家族全景（"暂不支持"不止笔记一类）

按占位文案精确统计 `RAW/` 侧：

| 占位文案 | 数量 | media_type | 含义 |
|---|---|---|---|
| 此条目为**笔记** | 71 | 11 | IMA 笔记（本次问题主体） |
| 此条目为**类型 15** | 41 | 15 | 录音 soundrecording（可经 MCP 取到转写全文，已实测） |
| 此条目为**类型 12** | 8 | 12 | session |
| 此条目为**类型 20** | 5 | 20 | html |
| 此条目为**网页** | 3 | 2 | 网页/剪藏 |

另有一类**无提示语**的占位（正文仅 `# 标题` + `[[标题]]`），共 **1109** 条：
`markdown 408 / pdf 316 / ppt 144 / word 127 / excel 80 / img 34 / note 1 / wechatarticle 1`。
这类属于"附件类条目"（`get_media_info` 未返回 `url_info` → 走 5 次重试后 `return null`），与笔记问题同源不同支。其中 145 条已于 10-01 回填。

---

## 3. 为什么偏偏是 Knight IV

不是它特殊，是**它那次调用恰好还在配额内**。

- Knight IV 与其 6 个同族笔记（`会议纪要一`、`维护V6技术研讨会` 等）均在 **10-02 22:57 同一轮**被写入；
- 6 个写成了占位符，只有 Knight IV 拿到正文 → 说明是**调用级/时序级**差异，不是条目级差异（1.2 节已从 API 侧证实三者同构）；
- 一旦写成占位符，`if (a.has(i.media_id)) continue` 就把它冻结在那里，**后续 12 轮重试全部无效**（10-02 → 10-08 连续 6 天各时段首调均 200005）。

---

## 4. 可行方案

### 方案 A（推荐·已验证可用于今日）：走 MCP 通道回填，绕开 REST 日配额

**实测证据（2026-10-10）**：对占位符条目 `会议纪要：V6产品开发技术研讨会` 与录音条目调用 MCP `fetch_media_content`，**两条均返回完整正文**，无 200005。

```
mcp__ima-mcp__fetch_media_content({ media_id: "note_3867e2b60070d7dc3f413086d0b0036e_7507101203046818" })
→ 返回完整会议纪要正文（Channel/SAP/材料实验/专利风险 全文）
```

要点：
1. **写入位置 = `RAW_FULL/` 同相对路径**。`RAW/` 是 AI 只读红线（AGENTS.md §0），正文镜像到 `RAW_FULL` 正是该目录的设计用途；存量 61 条已在 `RAW_FULL`。
2. **幂等键 = 占位符 front matter 里的 `media_id`**，已存在则跳过。
3. 优先级：MCP `fetch_media_content` > REST `get_doc_content`（配额恢复时）。
4. 覆盖范围：RAW 侧「暂不支持」占位共 **129 条**（笔记 72 + 类型15录音 41 + 类型12 session 8 + 类型20 html 5 + 网页 3）；其中 112 条在 `RAW_FULL` 早就有正文 → **实际缺口仅 17 条**。附件类 `attach_stub` 另有 40 条缺口（详见 §7）。

### 方案 B：给插件通道"松绑"（治本，二选一）

- **向 IMA 后台申请 OpenAPI 配额提额**——这是插件侧唯一能自愈的前提；
- **给插件作者提 issue**（两处一行代码的缺陷）：
  1. `Di` 集合里的 `20005` 应为 `200005`；
  2. `Oi` 正则补 `/超量/`、`/明日/`；
  3. 建议改为"占位符不写 `media_id`（或加 `placeholder: true` 标记）"，使其可被下轮重试覆盖——否则任何一次配额抖动都会造成永久空洞。

### 方案 C：自建"IMA → vault"补库流水线（推荐长期）

插件通道已连续 6 天不可用，不应再依赖它：
1. 每日定时任务，用 MCP `get_knowledge_list`（MCP 视角 `001a693ee6c0644e`）枚举知识库条目；
2. 对 `media_type ∈ {11,12,15,20,2}` 且本地无正文的条目，走 `fetch_media_content` 取正文；
3. 落 `RAW_FULL/`，登记回执；
4. 附件类（pdf/word/ppt/excel/markdown/img）走 `get_media_info` 签名 URL 下载原件；
5. 完成后按 AGENTS.md §3 编译入 `WIKI/`。

### 方案 D：补齐"从未入库"的约 43 条笔记

这批不出现于知识库列表，任何通道都取不到。需先在 IMA 客户端把笔记**「存入知识库」**，或改用 `openapi/note/v1/list_note_by_folder_id` 走"个人笔记"通道（注意：该通道产物以 `docid` 为键，写入 `RAW/ima_sync/notes/`，与知识库通道的 `media_id` 键不同，需分别判重）。

---

## 5. 风险与注意

1. **不要在 `RAW/` 原地改写占位符**——违反 AGENTS.md §0 红线；所有回填写 `RAW_FULL/`。
2. **占位符会被插件覆盖**：若人工回填写回 `RAW/` 侧但未保留插件要求的 `media_id` 键，下轮同步会重新覆盖为占位符（09-30 那批 61 条之所以安全，是因为写在 `RAW_FULL/`）。
3. **重复拉取无意义**：REST `get_doc_content` 命中配额后当天不会恢复，不要循环重试（已有 12 轮重试均为零产出）。
4. ⚠️ **`RAW/ima_sync/notes/飞书.md` 内含明文 App Secret / API Key**，且位于 Obsidian vault 内。建议移出 vault 或改为 `.env` 引用。

---

## 6. 附：核验命令

```bash
NODE="C:/Users/Chris Wang/.workbuddy/binaries/node/versions/22.22.2-6/node.exe"
cd "C:/Users/Chris Wang/.workbuddy/skills/ima-skill"

# 取条目元数据（判断 notebook_ext_info 是否存在）
"$NODE" ima_api.cjs openapi/wiki/v1/get_media_info '{"media_id":"note_..._7507101203046818"}'

# 取笔记正文（受日配额，超量返回 200005）
"$NODE" ima_api.cjs openapi/note/v1/get_doc_content '{"doc_id":"7507101203046818","target_content_format":1}'
```

MCP 通道（无配额限制）：
```
mcp__ima-mcp__fetch_media_content({ media_id: "<占位符文件 front matter 里的 media_id>" })
```

---

## 7. 执行记录（2026-10-10，方案 A + C 已落地）

### 方案 A 执行结果

以 3 + 3 个子代理（每个 13~14 条）走 MCP `fetch_media_content` 分批回填，正文写 `RAW_FULL/` 同相对路径：

| 批次 | 范围 | 取到正文 | IMA 侧无正文 |
|---|---|---|---|
| 「暂不支持」家族 | 17 条（笔记 10 / 录音 5 / session 2） | 12 | 5 |
| 附件类缺口 | 40 条 | 15 | 25 |
| **合计** | **57 条** | **27** | **30** |

**验收：12 个类型全部 0 缺口**，`RAW_FULL` 侧有正文条目 **1240** 条（执行前 1182）。

30 条"无正文"的根因分类（非通道故障）：

| 现象 | 条数 | 说明 |
|---|---|---|
| 图片无可提取文字层 | 16 | 图纸类（`Code *.jpg` 等），IMA 仅返回单字符噪声 → 需改走原件下载通道 |
| 空录音 / 未转写 | 2 | `录音纪要_*` session，IMA 侧无转写文本 |
| CSV/JMP 数据文件 | 7 | 纯数据表无文字层 |
| 扫描件 PDF | 4 | 无文字层 |
| `code 220030 文件获取失败` | 1 | `飞书` 笔记，IMA 侧条目本身异常，需在 IMA 客户端处理 |

### 方案 C 交付物

| 文件 | 作用 |
|---|---|
| `.tools/ima_note_backfill.py` | 清单生成 / 切片 / 覆盖率验收。`--scan`、`--slices N`、`--verify`、`--status`、`--kinds` |
| `.tools/ima_fetch_originals.py` | **通道 B**：原件下载（`get_media_info` 签名 URL）+ 文件名归一化 + 原件↔stub 配对清单。`--list`、`--run`、`--fix-ext`、`--manifest` |
| `.tools/IMA_NOTE_BACKFILL_RUNBOOK.md` | 运行手册：通道优先级、三条命令、子代理契约、边界与已知错误码 |
| `.tools/_ima_note_gap.json` | 当前缺口清单（幂等：`extract_status: ok\|empty` 即视为已处理） |
| 每日自动化「IMA 条目正文回填巡检」 | 每天 09:30 跑 scan/verify，缺口>0 时走 MCP（无 MCP 则 REST 兜底），报告落 `.tools/ima_backfill_daily/YYYY-MM-DD.md` 并追加 `log.md` |

### 遗留与建议

1. ~~**16 张图纸类图片**与 **4 个扫描件 PDF** 需走原件下载通道~~ → **已于 2026-10-10 完成**（见 §8）。同时补上 1 pptx + 1 docx + 4 CSV，共 24 条原件下载并完成本地识读。
2. **`RAW/ima_sync/notes/飞书.md` 仍含明文 App Secret / API Key**，且位于 vault 内，建议移出 vault 或改 `.env` 引用。
3. **建议向 IMA 后台申请 OpenAPI 提额**，并向插件作者提 issue（`20005`→`200005`、正则补「超量/明日」、占位符加标记以便重试）——否则插件通道每次配额抖动都会再制造一批永久空洞。
4. ~~旧的一次性重试链（`IMA笔记续跑-*`）~~ → **已于 2026-10-10 删除**（最后一个 `IMA笔记续跑-次日0930`）。
5. 约 43 条笔记仍未"存入知识库"，任何通道都取不到；需先在 IMA 客户端入库，或改走 `list_note_by_folder_id`（笔记通道，以 `docid` 为键，落 `RAW/ima_sync/notes/`）。

---

## 8. 扩展项执行记录（2026-10-10，通道 B 原件下载 + 本地识读）

**原件下载**：`.tools/ima_fetch_originals.py --run` → **24/24 成功**（幂等复跑 24 SKIP）。

| 类型 | 条数 | 落盘示例 |
|---|---|---|
| 扫描件 PDF | 4 | `Areas/IP/attachments/16_模块三：聚烯烃类热熔胶_US5266394A_….pdf`（748 KB） |
| 图纸图片 | 14 | `…/HSBL Trial - Oct 13 2025/attachments/Code 2.jpg`（142 KB） |
| pptx / docx | 1 / 1 | `Projects/REL/attachments/REL_Optimized_PTT_PVA_Composition.pptx`（233 KB） |
| CSV（书目索引） | 4 | `…/Seymour Polymer Chemistry/attachments/Seymour Polymer Chemistry_master_index.csv`（47 KB） |

**本地识读**（子代理读原件 → 写回 stub）：

- 3 份美国专利扫描件识读成功：`US20070203469A1`（SMMS 熔喷可弃式制品）、`US5266394A`（SBS 嵌段共聚物热熔胶，含受让人 Dow / Exxon）等
- `CN111134966A`（ω 型腿围橡筋）**源文件本身截断**（缺 xref/trailer），重新下载字节一致 → 已在 stub 如实标注
- `1780441413150.jpg` 为幻灯片截图，识读约 1100 字（含 20+ 中英双语散点标签）
- 13 张 `Code N.jpg` 为 UV 显色样品照，**确无文字层**，改为客观结构描述（不编造参数）
- 4 个 CSV 内联 400 行数据；`NOTE.docx` 内嵌手写图已识读
- `REL_Optimized_PTT_PVA_Composition.pptx` 为 **DRM 加密 OLE**（`EncryptedPackage`），无法抽文字 → `extract_status: "original-only"`

**最终验收**：`--verify` 12 类型 **0 缺口**；`extract_status` = ok 1233 / original-only 1 / empty 6（2 空录音 + 3 `.jmp` + 1 `飞书`）。

**通道 B 的工程要点**（已固化进脚本与手册）：

1. 原件扩展名必须按 **Content-Type → 魔数 → 前缀** 三级判定；早期只按前缀写死，导致图片丢扩展名、CSV 被写成 `.xlsx`
2. 落盘**用回原始文件名**而非 hash 后缀（便于 Obsidian `![](attachments/x.jpg)` 直接引用），幂等判据即"目标文件名是否已存在"
3. `url_info.url` 为 `chrome://…` 或空时无法下载 → 脚本 SKIP 并记录

**中间产物**：`.tools/_pdfpages/`（识读 PDF 时生成的 65 张页图 + 3 个诊断文件，约 17 MB）**已于 2026-10-10 清除**。清除前已确认：`D_text.txt` 为缺 ToUnicode 映射导致的乱码、`D_rebuilt.pdf` 为无效修复尝试，原件本身已存于 `attachments/`，无信息损失。
