---
schema: comparison_provenance.v3
draft_card: ../cards/longmemeval-benchmark-construction-pipeline.md
draft_provenance: ../provenance/longmemeval-benchmark-construction-pipeline.md
similarity_result: ../similarity/longmemeval-benchmark-construction-pipeline.json
existing_cards:
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0714
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.0667
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.0588
decision: new_card
audit_required: false
created_time: 2026-05-26T16:00:00+08:00
edited_time: 2026-05-26T16:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三个候选 jaccard 都低于 0.08，shared_tokens 仅为「的」。draft 标题的实质 token（LongMemEval / persona / 大海捞针 / 拼装 / 构造 / 管线 / 自对话）与 v2 候选（Karpathy LLM-wiki 元描述）无术语级重合。属于 jaccard 噪声。

## 2. draft 与候选在哪里不同

draft 是 mechanism 卡，来源 `arxiv-longmemeval`，论述 LongMemEval 的 6 步基准构造管线：164 属性本体 → Llama-3-70B 生背景 → 1000 候选→ 50 题（5% 通过率）→ 70% 人工编辑的 evidence session → ShareGPT/UltraChat 25/25/50 大海捞针拼装 → evidence 位置均匀分布。提供 LongMemEval-S (~115k) / -M (~1.5M) 两标准长度。属于「长期记忆基准设计」论点轴。

三张 v2 候选都是 Karpathy LLM-wiki 元描述。论点轴（基准构造管线 vs 个人 LLM wiki 模式）、来源（学术基准论文 vs Karpathy gist）、机制（合成对话拼装 + needle-in-haystack vs LLM 写 markdown）完全不同。

## 3. 下一步的核心依据

shared_tokens 全是「的」，无语义关联。draft 引文具体到 L1357-1392 / L887-921 / L1375-1377 / L1594-1599 等多处，scope 自洽（已说明合成数据与真实分布的差距、abstention 样本小等边界）。无任何 v2 卡可 merge 或 provenance_delta。综合判 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进入 publication_gate；与 sibling `longmemeval-five-core-memory-abilities` 同 source 互引。
