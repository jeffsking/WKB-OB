# 自动化「IMA 条目正文回填巡检」· 执行记忆

> 自动化 ID：8523233b-5eef-4997-95f8-c28f7977079f
> 流水线：方案 C `.tools/ima_note_backfill.py`；日报目录 `.tools/ima_backfill_daily/`

---

## 2026-10-10 09:40 · 首次自动化执行

**结果：缺口 0，12 类型 100% 覆盖，无需回填。**

- `--scan --kinds unsupported,attach_stub` → 缺口 **0** 条
- `--verify` → 12 个类型全部 0 缺口；RAW 带 media_id 条目 1346（attach_stub 1112 / unsupported 128 / has_body 106）；RAW_FULL 已处理 **1240** 条
- `--status` → 待回填 0 条（笔记 0 条）
- 磁盘交叉核验：RAW md 1752 / RAW_FULL md 1240；`extract_status` = ok 1233 / empty 6 / original-only 1
- 通道：**未使用**（缺口为 0，MCP 与 REST 均未触发）
- 落盘：**0 条**；`log.md` 未追加（无落盘，按约定不追加）
- 报告：`.tools/ima_backfill_daily/2026-10-10.md`

**背景备忘**：缺口为 0 的原因 —— 2026-10-10 首轮人工执行（方案 A 通道 A/B）已把「暂不支持」17 条 + 附件类 40 条 + 原件下载 24 条全部处理完毕，脚本幂等判据为 RAW_FULL 侧 `extract_status: ok|empty|original-only`。

**下次执行提示**：本巡检为幂等只读+按需回填。若插件 `ima-copilot-sync` 在两次运行之间又写入新占位符，缺口会重新 >0；此时按 runbook 步骤 2（MCP）→ 步骤 3（REST 兜底）处理。REST `get_doc_content` 遇 `code 200005` 立即停止、勿循环重试。

---

## 2026-10-11 09:37 · 第二次自动化执行

**结果：缺口 33 条，本轮落盘 0 条（通道均不可用），报告已出。**

- `--scan --kinds unsupported,attach_stub` → 缺口 **33 条**（PDF 17 / Word 6 / PPT 5 / Excel 2 / 图片 2 / 笔记 1）
- `--verify` → 12 类型合计 1271 占位 / 已回填 1238 / **缺口 33**（覆盖率 97.4%）；RAW 带 media_id **1380**（attach_stub 1142 / unsupported 129 / has_body 109）；RAW_FULL 有正文 1238
- `--status` → 待回填 33 条（笔记 1 条）
- **通道诊断（重要，会复用）**：
  - ❌ **MCP `ima-mcp` 在本自动化会话未挂载**。`ToolSearch` 全库检索无 `mcp__ima-mcp__*`；实际挂载的 MCP 为 teams / lighthouse-ops / agent-mail / sheetagent / genie-baas。**但 connector 侧状态正常**（`connector-states.json`: `ima-mcp {bound:true, enabled:true}`）→ 是会话未挂载，非凭证失效。**判定方法：ToolSearch 搜不到即未挂载，不要反复重试搜索。**
  - ✅ REST `openapi/wiki/v1/get_media_info` 可用（笔记 `7514131720577247` → `code:0`，notebook_ext_info 齐备）
  - ❌ REST `openapi/note/v1/get_doc_content` → `{"code":200005,"msg":"请求超量，请明日再试"}`，**当日额度耗尽，已按 runbook 立即停止、未重试**
- 落盘 **0 条**；未修改 `RAW/` 任何文件；未追加 `log.md`（无落盘，按约定不追加）
- 报告：`.tools/ima_backfill_daily/2026-10-11.md`
- 缺口构成：17 份供应商 PDF（`Areas/Supply Base/`）+ 6 份 BNC-SAP Word + 5 PPT（`Projects/Template/`）+ 2 Excel（Sensor China / COCO CI-06）+ 2 图片 + 1 笔记（`印刷技术总览（技术谱系）`）—— 均为 10-10 后新增占位符，属正常增量

**下次执行提示（更新）**：33 条中 **32 条是附件类（PDF/Word/PPT/Excel/图片）**，应走**通道 B 原件下载** `"$PY" .tools/ima_fetch_originals.py --run`（走 `get_media_info` 签名 URL，**不受 `get_doc_content` 日配额限制**）+ `--fix-ext` + 子代理本地识读；仅笔记 1 条需交互式会话 MCP `fetch_media_content`。若自动化会话仍无 MCP，附件类仍可用 REST 通道 B 闭环。
