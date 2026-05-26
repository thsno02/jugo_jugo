---
schema: draft_card_provenance.v3
draft_card: ../cards/graphrag-context-window-8k-optimal.md
material_id: arxiv-graphrag
digest_id: digest_arxiv-graphrag
source_paths:
  - data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt
created_time: 2026-05-26T15:01:00+08:00
edited_time: 2026-05-26T15:01:00+08:00
edited_entity: llm
---

## 源证据

- 行 86–91（Appendix C "Context Window Selection"）：
  - "The effect of context window size on any particular task is unclear, especially for models like \texttt{gpt-4-turbo} with a large context size of 128k tokens."（行 89）
  - "Given the potential for information to be ``lost in the middle'' of longer contexts~\citep{liu-etal:2023:tacl, kuratov2024search}, we wanted to explore the effects of varying the context window size for our combinations of datasets, questions, and metrics."（行 89）
  - "we tested four context window sizes: 8k, 16k, 32k and 64k. Surprisingly, the smallest context window size tested (8k) was universally better for all comparisons on comprehensiveness (average win rate of 58.1\%), while performing comparably with larger context sizes on diversity (average win rate = 52.4\%), and empowerment (average win rate = 51.3\%). Given our preference for more comprehensive and diverse answers, we therefore used a fixed context window size of 8k tokens for the final evaluation."（行 89）

- 行 956（§3.1.4 Configuration）："We used a fixed context window size of 8k tokens for generating community summaries, community answers, and global answers (explained in \autoref{app:window})."

## 卡片范围是否成立

- 三组数字 58.1% / 52.4% / 51.3% 直接来自源文本，未引申。
- "为什么小窗口会赢" 部分由源文本中明确给出的 lost-in-the-middle 因果（行 89）展开，属于合理解释，没有外部假设。
- "可以挪到其他 RAG pipeline" 是合理的工程引申，但措辞为"同样的逻辑可以挪"，不是论文断言——这一引申仅作为运营建议出现。

## 发表门控结果

本轮未运行。

## 备注

- 与 `graphrag-self-reflection-gleaning` 卡互补：那张管"索引阶段 chunk size"，这张管"查询阶段 context window"。两条参数互相独立。
- 与 `graphrag-root-community-token-efficiency` 卡互补：C0 是"索引侧 token 极少"，8K 是"查询侧 window 较小"——两者叠加才是 GraphRAG 的成本优势全貌。
