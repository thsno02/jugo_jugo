---
schema: comparison_provenance.v3
draft_card: ../cards/llm-wiki-mcp-skills-vs-tools-workflow.md
draft_provenance: ../provenance/llm-wiki-mcp-skills-vs-tools-workflow.md
similarity_result: ../similarity/llm-wiki-mcp-skills-vs-tools-workflow.json
existing_cards:
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.2143
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.1875
  - card_id: llm-wiki-wiki-layer-generated-markdown-directory
    card_path: llm_wiki/kb/cards/llm-wiki-wiki-layer-generated-markdown-directory.md
    score: 0.1875
decision: new_card
audit_required: false
created_time: 2026-05-26T12:42:00+08:00
edited_time: 2026-05-26T12:42:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三张 v2 候选与 draft 共享 token 仅 `llm / wiki / 层 / 的`，纯属误中：

- 三张 v2 卡都是 Karpathy gist 抽取的概念定义；
- 本 draft 讲的是 `llm-wiki-mcp` 这个 PyPI 包提供的 4 个 Claude Code skills 与 4 个 MCP tools 的两层分工 + 每次重读 schema + plugin marketplace 分发。

主题与对象都不重叠。

## 2. draft 与候选在哪里不同

- **对象不同**：v2 候选讲 Karpathy gist 概念；draft 讲 `llm-wiki-mcp` 包的工程实现层（skills vs tools）。
- **抽象层不同**：v2 是概念定义；draft 是软件包契约描述。
- **覆盖维度全新**：4 个 skills 名称（wiki-init / wiki-ingest / wiki-query / wiki-lint）+ 每个 skill 是否需要 server + "每次运行重读 wiki/CLAUDE.md" + Claude Desktop/Cursor 无 skill 会跳过 bookkeeping + plugin marketplace 安装命令 + importlib.resources 非 Claude 用法 —— 都不在 v2 任何卡片中。
- **决策粒度不同**：draft 给出客户端选型规则（Claude Code 装 skills / Claude Desktop+Cursor 手动 prompt / 非 Claude importlib 取出 skill markdown）。

不是 v2 卡片的扩展，是**关于另一个工件（软件包 + Claude Code skills）的全新事实卡**。

## 3. 下一步的核心依据

- 不是 `merge_candidate` / `provenance_delta`：v2 没有任何 MCP server / Claude Code skills 内容。
- 不是 `duplicate_skip`：未被 v2 覆盖。
- 不是 `revise_before_gate`：draft 证据扎实（所有原文行号都给出）、scope 清晰、边界（无 skill 客户端的 fallback 路径）都标注。

正确决定是 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：走 publication_gate；与同源的 `llm-wiki-mcp-design-boundary-mechanics-not-content`、`llm-wiki-mcp-four-tools` 形成 `llm-wiki-mcp` 卡簇。

## 5. 备注

- draft 备注预测"与 v2 `llm-knowledge-base-five-stage-workflow` 邻近"——该卡未进入本 batch top-3，audit 阶段可在 related 中补建链接（五阶段抽象 workflow vs skill/tool 工程实现层，互补不重叠）。
- top 2 与 top 3 同分（0.1875）是 jaccard 在小集合上常见 tie，对决策无影响。
