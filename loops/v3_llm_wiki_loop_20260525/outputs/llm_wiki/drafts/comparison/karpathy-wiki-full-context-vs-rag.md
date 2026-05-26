---
schema: comparison_provenance.v3
draft_card: ../cards/karpathy-wiki-full-context-vs-rag.md
draft_provenance: ../provenance/karpathy-wiki-full-context-vs-rag.md
similarity_result: ../similarity/karpathy-wiki-full-context-vs-rag.json
existing_cards:
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.1111
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.1
  - card_id: llm-wiki-persistent-compounding-artifact
    card_path: llm_wiki/kb/cards/llm-wiki-persistent-compounding-artifact.md
    score: 0.0588
decision: new_card
audit_required: false
created_time: 2026-05-26T16:05:00+08:00
edited_time: 2026-05-26T16:05:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

top 1/2 共享 `wiki`、`的`；top 3 仅 `wiki`。draft 标题的核心 token `full`、`context`、`RAG`、`retrieval`、`Karpathy`、`插件` 都不出现在任何候选标题，纯主题词撞分。

## 2. draft 与候选在哪里不同

- 候选 #1 `llm-wiki-three-layer-architecture`：Karpathy gist 的"raw/wiki/schema"三层静态架构。和"full context vs chunked RAG"立场无关。
- 候选 #2 `llm-wiki-schema-configuration-document`：schema 配置文档定义。无关。
- 候选 #3 `llm-wiki-persistent-compounding-artifact`：wiki 是持久复合产物的性质卡。也不在 full-context vs RAG 这条论点轴上。
- draft 来源是 `obsidian-community-plugin/text.txt` L343–375，是一张 distinction 卡，论点轴是"feed full wiki context, not chunked RAG retrieval"在 Obsidian 插件中的实际执行——含立场陈述、RAG vs Karpathy 模式对照表、长上下文模型选型表（Value Pick: DeepSeek V4-Flash / Gemini-3.5-Flash 等）、Ollama 本地局限与混合方案。v2 中没有任何 distinction 卡或模型选型卡覆盖这一立场。

## 3. 下一步的核心依据

- 不是 `merge_candidate`：v2 top 3 中无 RAG distinction 卡。
- 不是 `provenance_delta`：top 3 都是 wiki 性质 / schema 元事实卡，无法接收"长上下文模型选型表"的反向加挂。
- 不是 `duplicate_skip`：无任何覆盖。
- 不是 `revise_before_gate`：draft 已有立场 verbatim、对照表、模型选型表、边界（长上下文成本 / 注意力稀释 / wiki 触顶 / 混合策略）；门控可继续。
- 综合判 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：publication_gate；门控阶段可考虑模型选型表里的 2026 年模型（DeepSeek V4-Flash / Gemini-3.5-Flash / Qwen3.6-Plus / Grok-4 / Claude Sonnet 4.6 / Claude Opus 4.7）逐条与来源页面对齐。

## 5. 备注

- draft 自身 provenance 提到"v2 卡片 `auto-index-replaces-rag-at-small-scale` 概念近似"——该 v2 卡未在本次 top 3，无法直接判别；若 publication 阶段确认 v2 真的有此卡，可考虑互相 cross-link（属审计阶段）。
- top 1/2/3 在该 draft 上是典型的"v2 LLM Wiki 系列卡撞 wiki 主题词"案例。
