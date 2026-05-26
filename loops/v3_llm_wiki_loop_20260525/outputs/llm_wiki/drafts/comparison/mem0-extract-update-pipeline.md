---
schema: comparison_provenance.v3
draft_card: ../cards/mem0-extract-update-pipeline.md
draft_provenance: ../provenance/mem0-extract-update-pipeline.md
similarity_result: ../similarity/mem0-extract-update-pipeline.json
existing_cards:
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0526
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.05
  - card_id: raw-sources-readonly-source-of-truth
    card_path: llm_wiki/kb/cards/raw-sources-readonly-source-of-truth.md
    score: 0.0476
decision: new_card
audit_required: false
created_time: 2026-05-26T12:00:00+08:00
edited_time: 2026-05-26T12:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

similarity 中 top 1/2 共享 `的`，top 3 共享 `事实`（draft "...变成可增量管理的**事实**"，候选 "Raw sources 是只读**事实**来源"）。分数 ≤0.0526 是通用 token 误中。

## 2. draft 与候选在哪里不同

- draft 描述 Mem0 论文 §3.1 的提取-更新两阶段管线：extraction phase 用 $\phi(P)=\phi(S, \text{recent window}, m_{t-1}, m_t)$ 抽候选记忆；update phase 检索 top-s=10 相似记忆后用 LLM tool-call 选择 ADD/UPDATE/DELETE/NOOP；默认 m=10, s=10, GPT-4o-mini。与 full-context / RAG 切块 / MemGPT 分页的差异。来源 `arxiv-mem0` (arXiv:2504.19413)。
- top 1 `idea-file-abstract-vague`：Karpathy idea file 抽象性。
- top 2 `llm-wiki-three-layer-architecture`：Karpathy 三层架构。
- top 3 `raw-sources-readonly-source-of-truth`：Karpathy gist 中 Raw sources 层是只读事实来源。这里 "事实来源" 指文档级别 source of truth；draft 中 "事实" 指从对话抽取的 atomic memory，含义层级完全不同。
- 论点轴（agent 记忆增量管理 pipeline vs Karpathy 架构层定义）、来源、机制完全不重叠。

## 3. 下一步的核心依据

(1) 与 (2) 表明分数来自 `的` / `事实` 同形，主题无交集。判 `new_card`：直接走 publication_gate。draft 含两阶段定义、默认配置、与 full-context/RAG/MemGPT 的差异分析，发表条件齐备。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：直接进入 publication_gate。

## 5. 备注

`事实` 在两个语境中所指层级不同（文档 source of truth vs 抽取出的 atomic memory），是 token 同形误中的另一例。
