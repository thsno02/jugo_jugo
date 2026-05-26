---
schema: comparison_provenance.v3
draft_card: ../cards/ragchecker-tuning-knobs-saturate.md
draft_provenance: ../provenance/ragchecker-tuning-knobs-saturate.md
similarity_result: ../similarity/ragchecker-tuning-knobs-saturate.json
existing_cards:
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0833
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.0769
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.0667
decision: new_card
audit_required: false
created_time: 2026-05-26T16:00:00+08:00
edited_time: 2026-05-26T16:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三个候选 jaccard 都低于 0.09，shared_tokens 仅为「的」。draft 标题主体是 RAG / RAGChecker / 调优 / 结论 / 四个 等术语，与 v2 候选（Karpathy LLM-wiki 元描述）没有任何术语级重合。属于 jaccard 噪声。

## 2. draft 与候选在哪里不同

draft 是 operational_rule 卡，来源 `arxiv-ragchecker`，把论文「Suggestions to RAG Builders」总结的四条调优规则展开（k 与 chunk size 收益饱和、大 chunk + 小 k 优于反向、overlap 不必精调、prompt 优化对 GPT-4 有效对 Llama3-70B 无用），并给出具体扫描数字与 trilemma 含义。属于「RAG 工程调优实证」论点轴。

三张 v2 候选都是 Karpathy LLM-wiki 元描述卡，scope 仅限 gist 文本范围；与 RAG 调优实验在论点轴、来源、读者、机制层面全部不同。RAGChecker 论文里 `RAG 不积累综合知识` 这种「问题陈述层」也许会和 v2 `rag-document-qa-does-not-accumulate-synthesized-knowledge`（虽不在本批次 top 3 里）有概念邻近，但本批次 top 3 里没有这种邻近候选。

## 3. 下一步的核心依据

shared_tokens 全是助词「的」，无语义关联。draft 引文具体到 L358-410 / L819-830 / 多个 ablation 表行号，scope 自洽，不需要 revise。无任何 v2 卡可 merge 或 provenance_delta。综合判 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进入 publication_gate。

## 5. 备注

- 与 sibling 卡 `ragchecker-generator-trilemma` 是同 source 内的互引关系；与 v2 KB 无任何重叠。
