---
schema: comparison_provenance.v3
draft_card: ../cards/llm-wiki-mcp-design-boundary-mechanics-not-content.md
draft_provenance: ../provenance/llm-wiki-mcp-design-boundary-mechanics-not-content.md
similarity_result: ../similarity/llm-wiki-mcp-design-boundary-mechanics-not-content.json
existing_cards:
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.25
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.2
  - card_id: llm-wiki-health-checks
    card_path: llm_wiki/kb/cards/llm-wiki-health-checks.md
    score: 0.125
decision: new_card
audit_required: false
created_time: 2026-05-26T12:35:00+08:00
edited_time: 2026-05-26T12:35:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

top 1 `llm-wiki-schema-configuration-document` 与 draft 有部分语义连接：

- 两者都谈到"schema 应该住在用户的 `CLAUDE.md` / `AGENTS.md`"；
- draft 引用 Karpathy gist 的"刻意把 schema 留给用户"作为 server 不做 Layer 3 校验的设计理由。

但这一连接是**作为论据被引用**，draft 的主题是 `llm-wiki-mcp` 这个 MCP server 包的设计边界，不是 schema 概念本身的定义。

top 2 / top 3 是 token 误中（仅 `llm / wiki / 的`、`llm / wiki`）。

## 2. draft 与候选在哪里不同

- **对象不同**：v2 候选讲的是 Karpathy gist 抽象的 schema 概念；本 draft 讲的是一个具体软件包 `llm-wiki-mcp`（PyPI 包，v0.1.1 alpha）的 server-side 设计边界。
- **抽象层不同**：v2 是概念定义；draft 是软件实现的契约描述（atomic write / etag / path containment / CVE-2025-53109 / WikiStorage Protocol）。
- **覆盖维度全新**：原子写、etag 乐观并发、CVE 编号、Protocol 扩展点、log line 格式锁定——v2 任何卡片都不涉及。
- **scope 不同**：v2 scope 仅限对 Karpathy gist 段落的事实描述；draft scope 是 `llm-wiki-mcp` 包 README 对自身边界的描述。
- 不是 v2 卡片的扩展，也不是同主题不同视角——是**关于另一个工件（软件包）的全新事实卡**，只在论证 server 为何不做 Layer 3 校验时引用了 Karpathy 原意。

## 3. 下一步的核心依据

- 不是 `merge_candidate` / `provenance_delta`：draft 关于 `llm-wiki-mcp` server 的事实在 v2 schema 卡片中完全没有，没有可合并 / 可补强的对应内容。draft 引用 Karpathy gist "刻意留给 schema" 只是论据，不构成对 v2 schema 卡的新证据补充。
- 不是 `duplicate_skip`：v2 没有 MCP server 实现层的任何卡片。
- 不是 `revise_before_gate`：draft 证据完整（所有原文行号都给出）、scope 清晰、边界（用户不写 schema 时 server 不拦截 / alpha 阶段 backend 限制）都标注。
- 是 `new_card`：是关于一个独立软件工件（`llm-wiki-mcp` 包）的全新事实，与 v2 任何卡片不构成事实重叠。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：走 publication_gate；接受后建议在 v2 拓扑上挂到"LLM Wiki 工程实现 / MCP 工具"类目下；与同源的兄弟 draft `llm-wiki-mcp-skills-vs-tools-workflow`、`llm-wiki-mcp-four-tools` 形成簇。

## 5. 备注

- top 1 的 0.25 分主要来自 `schema` token——draft 因为论证里出现 "schema lives in CLAUDE.md" 而带上该 token，并不意味着 draft 主题是 schema。
- draft 与 v2 schema 卡之间的关系是"引用关系"而非"事实重叠关系"——可在 audit 阶段加 related 链接，但不构成 provenance_delta。
