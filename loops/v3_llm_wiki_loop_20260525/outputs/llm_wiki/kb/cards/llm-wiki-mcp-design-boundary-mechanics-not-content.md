---
id: llm-wiki-mcp-design-boundary-mechanics-not-content
title: llm-wiki-mcp 的设计边界：server 只管 mechanics，schema 留给 wiki/CLAUDE.md
status: accepted
card_type: distinction
tags: [#llm-wiki-mcp, #design-philosophy, #karpathy-llm-wiki, #schema]
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-28T14:15:00+08:00
edited_entity: llm
source_ids: [pypi-llm-wiki-mcp]
provenance_card: ../provenance/llm-wiki-mcp-design-boundary-mechanics-not-content.md
aliases: [mechanics not content shape, no Layer 3 validation, schema lives in CLAUDE.md]
related: [karpathy-gist-three-layers, agents-md-as-schema-layer, llm-wiki-schema-is-most-important, llm-wiki-mcp-four-tools]
---

## 区分对象

`llm-wiki-mcp` 在 README 里**反复强调一条边界**：server 只负责"LLM 总是搞错的无聊机械层"（mechanics），而 wiki 的内容形态（schema）**完全留给用户的 `wiki/CLAUDE.md`** 来定义 [^src1]。这条边界把"协议层"和"语义层"切得很干净。

## Server 负责的（mechanics）

1. **Atomic writes**：page 用 tmp-file + fsync + rename；log entry 用 O_APPEND 单次写入。
2. **Optimistic concurrency**：每个 page 有 etag `sha256(body) || mtime_ns`；冲突时抛 `WikiConflictError`，agent 必须 re-read + merge + retry。
3. **Path containment**：slug 经正则校验；resolved path 与 root 的 realpath 比对，封堵 CVE-2025-53109 类的 symlink-escape [^src3]。
4. **Format-locked log line**：log 行必须是 `## [YYYY-MM-DD] operation | Title`；operation 名是自由字符串，但破坏行结构的字符会被拒。

## Server **不**负责的（content shape）

- **不**校验 frontmatter 字段是否合法。
- **不**校验 page category（concept / tool / person...）。
- **不**校验 link target 是否存在或正确。
- 这些都属于 "Layer 3 schema validation"，README 明确说 server 里**没有**这层。

## 为什么这样切边界

> "Karpathy's gist is deliberately silent on content shape; baking a schema into the server would defeat the point."
> —— `text.txt:187` [^src2]

Karpathy 原始 gist 把 schema 留给用户的 AGENTS.md / CLAUDE.md 是有意为之 [^v3-1][^v3-2]；如果把 schema 烧进 server，每个用户的 wiki 都要被同一个 schema 约束，gist 提倡的"每个领域自己长出 schema"就不成立。

## 实践含义

- **用户责任**：必须在 `wiki/CLAUDE.md` 里写出 frontmatter 字段、slug 规则、page 类型、link 约定、contradiction-resolution 协议。**没有这份文件**，wiki 在 2-3 个月内会退化成"a graveyard of abandoned notes"（呼应同源同主题的 openaitoolshub 经验文章 [^v3-3]）。
- **系统责任**：server 保证 `wiki_write_page` [^v3-4] 不会丢数据、不会被竞态破坏、不会被路径越权——这些是 LLM 自己写永远写不对的。
- **扩展责任**：想换存储后端（SQLite / Notion / GDrive）只需实现 `WikiStorage` Protocol 给 `build_server` 用，因为 mechanics 与 storage 解耦 [^src4]。

## 边界与限制

- 这个分工要求 user 真的会写 schema；如果用户不写，server 不会拦截"乱七八糟的 wiki"——server 的"安全网"覆盖不到内容质量层。
- alpha 阶段（v0.1.1）只支持 local filesystem backend；其他 backend 留给 Protocol 实现者。

## Footnotes

[^src1]: `data/raw/pypi/pypi-llm-wiki-mcp/text.txt` — 第 117 行 verbatim："The server handles the boring layer LLMs keep getting wrong: atomic writes, etag conflict checks, append-only log integrity, path containment. The skills give the agent a workflow to follow. The wiki schema lives in your own wiki/CLAUDE.md and grows with your domain. There is no Layer 3 schema validation in the server."
[^src2]: `data/raw/pypi/pypi-llm-wiki-mcp/text.txt` — 第 187 行 verbatim："The server does not validate frontmatter shape, page categories, or link targets. That layer lives in your wiki/CLAUDE.md schema doc and grows with the LLM. Karpathy's gist is deliberately silent on content shape; baking a schema into the server would defeat the point."
[^src3]: `data/raw/pypi/pypi-llm-wiki-mcp/text.txt` — 第 184 行 verbatim："Path containment. Slugs are regex-validated. Resolved paths are checked against the realpath of the root, blocking the CVE-2025-53109 symlink-escape class."
[^src4]: `data/raw/pypi/pypi-llm-wiki-mcp/text.txt` — 第 191–195 行，WikiStorage Protocol 扩展点描述。
[^v3-1]: [karpathy-gist-three-layers](karpathy-gist-three-layers.md) — Karpathy gist 把 raw / wiki / schema 三层所有权严格分离，正是 llm-wiki-mcp 不肯把 schema 烧进 server 的源头。
[^v3-2]: [agents-md-as-schema-layer](agents-md-as-schema-layer.md) — AGENTS.md / CLAUDE.md 作为 schema 层让多轮 ingest 不发散，是 llm-wiki-mcp 让用户自填 schema 的具体形态。
[^v3-3]: [llm-wiki-schema-is-most-important](llm-wiki-schema-is-most-important.md) — openaitoolshub 半年实战总结：schema.md 是 LLM Wiki 里最重要的文件，缺了就退化。
[^v3-4]: [llm-wiki-mcp-four-tools](llm-wiki-mcp-four-tools.md) — `wiki_write_page` 的 atomic write + etag CAS 在该卡有完整描述。
