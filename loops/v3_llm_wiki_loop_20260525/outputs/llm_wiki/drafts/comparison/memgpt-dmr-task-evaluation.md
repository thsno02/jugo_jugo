---
schema: comparison_provenance.v3
draft_card: ../cards/memgpt-dmr-task-evaluation.md
draft_provenance: ../provenance/memgpt-dmr-task-evaluation.md
similarity_result: ../similarity/memgpt-dmr-task-evaluation.json
existing_cards:
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0625
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.0588
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.0526
decision: new_card
audit_required: false
created_time: 2026-05-26T16:00:00+08:00
edited_time: 2026-05-26T16:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三张候选属 v2 高频干扰簇，分数 0.052–0.062。MSC / DMR / ROUGE-L / GPT-4 / MemGPT 等核心 token 在 v2 不出现。共享 token 仅是中文虚词。

## 2. draft 与候选在哪里不同

draft 描述 MemGPT 论文为量化对话 agent consistency 而新造的 DMR 任务：在 MSC 5 个 session 后自造 session 6（单 Q-A，明确回指前面某细节）；评测用 ROUGE-L recall + LLM-as-Judge；GPT-4 baseline 32.1% / +MemGPT 92.5%。论点轴是"主动 retrieval vs 被动摘要"的差距与"lossy 压缩在 ingestion 阶段丢的细节下游救不回"。

v2 三张候选是 Karpathy LLM Wiki 概念层，与 MemGPT / DMR / 对话 agent 评估无关。

## 3. 下一步的核心依据

(1) (2) 共同表明无主题重叠。draft 完整。结论 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进 publication_gate；与 `memgpt-function-chaining-heartbeat` 等 MemGPT 系列卡互相 cite。

## 5. 备注

无。
