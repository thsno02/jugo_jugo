---
id: llm-wiki-mcp-four-tools
title: llm-wiki-mcp 的四个 MCP 工具：read / write_page / log_append / inventory
status: accepted
card_type: operational_rule
tags: [#llm-wiki-mcp, #mcp, #tooling, #karpathy-llm-wiki]
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-28T14:18:00+08:00
edited_entity: llm
source_ids: [pypi-llm-wiki-mcp]
provenance_card: ../provenance/llm-wiki-mcp-four-tools.md
aliases: [wiki_read, wiki_write_page, wiki_log_append, wiki_inventory, four MCP tools]
related: [llm-wiki-mcp-design-boundary-mechanics-not-content, llm-wiki-mcp-skills-vs-tools-workflow, karpathy-llm-kb-three-operations, llm-wiki-ingest-vs-query-workflow, langgraph-tool-runtime-store-access, mem0-tool-call-add-update-delete-noop]
---

## 四个工具的契约

Steven Wu 的 `llm-wiki-mcp` 0.1.1（PyPI, 2026-04-08）把 Karpathy LLM Wiki 模式 [^v3-1] 的 MCP server 收敛到四个 tool，每个都明确标注 annotation（read-only / destructive / idempotent / not-idempotent） [^src1]：

| 工具 | Annotation | 作用 |
|---|---|---|
| `wiki_read` | read-only, idempotent | 读一页，返回 body、解析后的 frontmatter、outgoing links、etag |
| `wiki_write_page` | destructive, idempotent | 原子写入 [^src2]；`etag=null` 表示创建，已读 etag 表示更新（CAS） |
| `wiki_log_append` | not idempotent | 在 `log.md` 追加一条 Karpathy 格式 `## [YYYY-MM-DD] op | Title` 的条目 |
| `wiki_inventory` | read-only, idempotent | 全图快照：pages、frontmatter、link edges、log entries；可附加 plain-text mention 扫描做 backlink 审计 |

## 关键设计要点

- **`wiki_log_append` 是唯一非幂等的工具**——日志条目天然带语义"这件事发生过一次"，重复 append 会失真。LLM 必须意识到这一点，不能在重试逻辑里盲目重放。
- **`wiki_write_page` 用 etag CAS（compare-and-swap）实现乐观并发**：每个 page 的 etag 是 `sha256(body) || mtime_ns`；更新时不匹配会抛 `WikiConflictError`，agent 需要 **重读 → 合并 → 重写** [^src3]。
- **`wiki_inventory` 把整张图一次性给 agent**：不是为 production-scale 设计的接口，而是为"让 agent 在一次 Read 内审计所有 backlink 与 orphan"提供的便利接口。

## 故意不暴露的部分

- `index.md` 和 `raw/` **不**作为 MCP tool 暴露 [^src4]：
  - `index.md` 由 LLM 在 host 侧用 Read / Write 操作（属于"被 curate 的内容"，不应通过 server 自动化）。
  - `raw/` 在 server 视角是 immutable，不允许被 agent 通过 MCP 改动。
- 这种"主动留白"是设计选择——不是缺失功能。

## 操作含义

- agent 写一页之前必须先 `wiki_read` 拿 etag；这是 CAS 协议的硬要求。
- agent 完成 ingest / lint / contradiction-mark [^v3-2][^v3-3] 等操作后**必须**调一次 `wiki_log_append`，否则 log.md 失去"事情发生过"的可审计性。
- `wiki_inventory` 适合作为"会话开始时一次性建立 mental map"的工具调用，而非高频轮询。

## Footnotes

[^src1]: `data/raw/pypi/pypi-llm-wiki-mcp/text.txt` — 第 159–165 行，四个工具清单，每条配 annotation 与一句话功能描述。
[^src2]: `data/raw/pypi/pypi-llm-wiki-mcp/text.txt` — 第 180 行 verbatim："Atomic writes. tmp-file + fsync + rename for pages. O_APPEND single-write for log entries."
[^src3]: `data/raw/pypi/pypi-llm-wiki-mcp/text.txt` — 第 181 行 verbatim："Every page has an etag (sha256(body) || mtime_ns). Updates supply the etag they read; a mismatch raises WikiConflictError, and the agent re-reads, merges, and retries."
[^src4]: `data/raw/pypi/pypi-llm-wiki-mcp/text.txt` — 第 167 行，故意不暴露 index.md 与 raw/ 的设计说明。
[^v3-1]: [karpathy-gist-three-layers](karpathy-gist-three-layers.md) — Karpathy gist 的 raw / wiki / schema 三层是 llm-wiki-mcp 的设计原型。
[^v3-2]: [karpathy-llm-kb-three-operations](karpathy-llm-kb-three-operations.md) — Karpathy "LLM KB" 的三个操作 Ingest / Query / Lint，是 wiki_log_append 必须记录的 op 类型来源。
[^v3-3]: [llm-wiki-contradictions-are-assets](llm-wiki-contradictions-are-assets.md) — contradiction-mark 不是 bug 修复而是资产，正解释了为什么它是必须 log 的一类操作。
