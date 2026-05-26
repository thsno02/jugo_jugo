---
schema: comparison_provenance.v3
draft_card: ../cards/llm-wiki-mcp-four-tools.md
draft_provenance: ../provenance/llm-wiki-mcp-four-tools.md
similarity_result: ../similarity/llm-wiki-mcp-four-tools.json
existing_cards:
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.2
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.1765
  - card_id: llm-wiki-health-checks
    card_path: llm_wiki/kb/cards/llm-wiki-health-checks.md
    score: 0.125
decision: new_card
audit_required: false
created_time: 2026-05-26T12:04:00+08:00
edited_time: 2026-05-26T12:04:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三张候选共享 token `llm`、`wiki`、`的`——这些是 v2 卡片标题里的常见词。top1 (`three-layer-architecture`) jaccard 0.2 实际全部来自这三个功能词，没有任何与 MCP / tool / protocol 相关的概念共享。top3 (`health-checks`) 共享 `llm`、`wiki`，更弱。属于典型的"标题 token 频繁词撞分"。

## 2. draft 与候选在哪里不同

- **来源不同**：本 draft 取自 `pypi-llm-wiki-mcp`（Steven Wu 2026-04-08 在 PyPI 发布的具体 MCP server 实现）；v2 三张候选全部来自 `karpathy-gist-llm-wiki`（karpathy 自述 gist）。一个是某个第三方实现，一个是源头设计。
- **抽象层不同**：
  - top1 `three-layer-architecture` 谈 karpathy gist 内的概念三层（raw sources / wiki / schema），是**架构概念分层**；
  - 本 draft 谈某 MCP server 暴露的四个具体 tool 契约（read/write_page/log_append/inventory），含 annotation（read-only / destructive / idempotent / not-idempotent）、etag CAS 并发协议、`wiki_log_append` 唯一非幂等等。属**协议级 operational_rule**。
- top2 `schema-configuration-document` 讲 schema 作为配置文档约束 LLM 行为；本 draft 不触碰 schema 层。
- top3 `health-checks` 讲 LLM 健康检查；与 MCP tool 契约无关。
- 本 draft 显式排除了 skill 层和 server 设计哲学（属另外两张兄弟卡 `llm-wiki-mcp-skills-vs-tools-workflow`、`llm-wiki-mcp-design-boundary-mechanics-not-content`），范围严格收敛在"四个 tool 是什么 + 各自契约"。

## 3. 下一步的核心依据

(1) 三张候选都没有触及 MCP protocol 实现；(2) 来源是一个 v2 KB 完全没有的 PyPI 包；(3) 卡片是 operational_rule 而不是 known_fact——它锁定了 etag CAS、log 非幂等等运行时约束，这是 v2 三层架构概念卡覆盖不到的层次。结论是 `new_card`。

不是 `provenance_delta`：本 draft 不是补 v2 `three-layer-architecture` 的某个细节——它谈的是一个外部 MCP 实现，与 karpathy gist 的内部分层无直接对应。不是 `merge_candidate`：v2 没有任何 MCP/tool/protocol 卡可合并。不是 `revise_before_gate`：draft 已锁定 annotation、CAS 协议、log 格式，每条都有行号回引。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进入 publication_gate；建议同时引入 source_id `pypi-llm-wiki-mcp` 到 sources 索引；与两张兄弟 MCP 卡建立 related 互链。

## 5. 备注

- 这是一组 3 张 MCP 兄弟卡之一，本卡只覆盖 tool 契约；评估时不要要求它讨论 skill workflow 或设计哲学。
