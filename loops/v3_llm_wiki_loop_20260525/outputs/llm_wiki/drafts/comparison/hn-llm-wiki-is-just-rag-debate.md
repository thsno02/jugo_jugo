---
schema: comparison_provenance.v3
draft_card: ../cards/hn-llm-wiki-is-just-rag-debate.md
draft_provenance: ../provenance/hn-llm-wiki-is-just-rag-debate.md
similarity_result: ../similarity/hn-llm-wiki-is-just-rag-debate.json
existing_cards:
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.2143
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.1875
  - card_id: llm-wiki-health-checks
    card_path: llm_wiki/kb/cards/llm-wiki-health-checks.md
    score: 0.1333
decision: new_card
audit_required: false
created_time: 2026-05-26T12:41:00+08:00
edited_time: 2026-05-26T12:41:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三张 v2 候选与 draft 共享 token 仅 `llm / wiki / 的`，纯属误中：

- v2 三张候选都是 Karpathy gist 抽取的事实定义卡（schema 配置 / 三层架构 / health checks 清理）；
- 本 draft 是 HN 原帖第 108–151 行围绕"This is just RAG"主题的多评论者综述（kenforthewin / panarky / darkhanakh / devmor / mememememememo 等）。

主题与来源都不重叠。

## 2. draft 与候选在哪里不同

- **事实类型不同**：v2 是 `known_fact`；draft 是 `distinction`（争论综述类）。
- **来源不同**：v2 来源 Karpathy gist；draft 来源 HN 原帖 thread。
- **覆盖维度全新**：kenforthewin 主帖 "This is just RAG" + panarky "RAG 不需要 embeddings" + darkhanakh "write loop 是关键差异 / vanilla RAG corpus is static" + devmor "persistent memory RAG" + mememememememo "compaction for RAG" —— 都不在 v2 任何卡片中。
- **决策粒度不同**：draft 给出"如果当 RAG 看 → 注意力落在 embedding/chunking/retriever / 如果当 write-loop+retrieval 看 → 注意力落在 schema/backlink/staleness/linting"的工程取向区分。
- **edges 不同**：draft 显式标注误用提示（把 LLM Wiki 当 RAG 实现会忽略 write-loop 循环不变量 / 反过来过度营销）。

不是 v2 卡片的扩展，是**全新的 distinction 类卡**。

## 3. 下一步的核心依据

- 不是 `merge_candidate` / `provenance_delta`：v2 没有"wiki vs RAG / write-loop 区分"任何内容。
- 不是 `duplicate_skip`：完全未被 v2 覆盖。
- 不是 `revise_before_gate`：draft 证据扎实（每个评论员都带行号 + 用户名）、scope 清晰、边界（不应当 RAG 看 / 也不应当超越 RAG 营销）都标注。

正确决定是 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：走 publication_gate；audit 阶段与 `karpathy-llm-wiki-vs-rag`、`anthemcreation-llm-wiki-vs-rag-multi-hop` 形成"wiki vs RAG 三视角"簇。

## 5. 备注

- 本 draft 自身预测"与 v2 中可能已有的 LLM Wiki vs RAG 卡片大概率重叠"——但实际 batch top-3 中 v2 没有该卡，重叠不存在。
- 三张同主题 vs RAG 卡（v3 内部）建议保留为不同视角：本卡 = 争论综述类、karpathy = paradigm 区分类、anthemcreation = 推理深度 + 适用区间类。三者来源不同，独立保留可保 provenance 清晰。
