---
schema: comparison_provenance.v3
draft_card: ../cards/nist-ai-rmf-gai-profile.md
draft_provenance: ../provenance/nist-ai-rmf-gai-profile.md
similarity_result: ../similarity/nist-ai-rmf-gai-profile.json
existing_cards:
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.1176
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0667
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.0625
decision: new_card
audit_required: false
created_time: 2026-05-26T16:05:00+08:00
edited_time: 2026-05-26T16:05:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

共享 token 只有 `是`、`的` 这两个中文虚词。draft 的核心 token `NIST`、`AI`、`RMF`、`600`、`profile`、`生成式` 在任何候选标题都不出现。jaccard 0.1176 完全由虚词产生，没有任何主题对接。

## 2. draft 与候选在哪里不同

- 候选 #1 `llm-wiki-schema-configuration-document`：Karpathy gist 的 schema 配置文档定义。与 NIST AI 风险治理框架毫无概念交集。
- 候选 #2 `idea-file-abstract-vague`：idea file 抽象性事实。无关。
- 候选 #3 `llm-wiki-three-layer-architecture`：Karpathy gist 三层架构。无关。
- draft 来源是 NIST publications 索引页（`nist-gai-profile/text.txt` L208–241），记录 `NIST AI 600-1: AI RMF Generative AI Profile` 的标题、报告号、作者、发布日期、abstract、与 EO 14110 / RMF 1.0 / voluntary use 的定位。这是政策类参考资料卡，v2 KB 无相关条目。

## 3. 下一步的核心依据

- 不是 `merge_candidate`：v2 无 AI 治理 / 政策 / 风险框架卡。
- 不是 `provenance_delta`：候选都是 Karpathy gist 元事实，与 NIST 文档无对接面。
- 不是 `duplicate_skip`：无重叠。
- 不是 `revise_before_gate`：draft 已有清楚的元信息引用（行号、报告号、DOI、作者列表）和明确边界（"PDF 内容未读，控制项要去全文找"）；门控可继续。
- 综合判 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：publication_gate；本卡定位为索引层卡，后续若抓 NIST.AI.600-1 PDF 全文可再拆"风险类目""控制项映射"等卡。

## 5. 备注

- jaccard 0.1176 仅由"是 / 的"两个虚词产生，是中文 jieba 分词下不可避免的低分误中。
- v2 KB 当前完全围绕 Karpathy LLM Wiki 主题；NIST AI RMF 是不同维度（治理/合规）的引入。
