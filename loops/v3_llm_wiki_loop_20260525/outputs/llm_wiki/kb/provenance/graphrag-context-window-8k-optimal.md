---
schema: accepted_card_provenance.v3
card: ../cards/graphrag-context-window-8k-optimal.md
material_id: arxiv-graphrag
digest_id: digest_arxiv-graphrag
source_paths:
  - data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt
draft_card: ../../drafts/cards/graphrag-context-window-8k-optimal.md
draft_provenance: ../../drafts/provenance/graphrag-context-window-8k-optimal.md
similarity_result: ../../drafts/similarity/graphrag-context-window-8k-optimal.json
comparison_provenance: ../../drafts/comparison/graphrag-context-window-8k-optimal.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T10:02:00+08:00
  gate_notes: 6/6 项通过：胜率表 + lost-in-the-middle 机制 + 边界 + Appendix C 行号锚定。
created_time: 2026-05-26T15:01:00+08:00
edited_time: 2026-05-27T10:02:00+08:00
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

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T10:02:00+08:00
- 检查要点：
  - 非标题复述：胜率表 + 解释 + 操作含义 + 边界，四段实体内容。
  - 知识密度：4 个窗口大小、3 个指标数值、lost-in-the-middle 机制阐释、与 indexing 阶段 chunk size 分离的边界。
  - 源支撑：Appendix C 行 86-91 + §3.1.4 行 956 双锚点。
  - References / Footnotes 存在。
  - frontmatter 完整。
  - related 字段 6 个 v3 draft id。

## 备注

- 与 `graphrag-self-reflection-gleaning` 卡互补：那张管"索引阶段 chunk size"，这张管"查询阶段 context window"。两条参数互相独立。
- 与 `graphrag-root-community-token-efficiency` 卡互补：C0 是"索引侧 token 极少"，8K 是"查询侧 window 较小"——两者叠加才是 GraphRAG 的成本优势全貌。
- Adoption 阶段观察：comparison 三个 v2 候选 score 0.000，全是 Karpathy llm-wiki 推文条目，与 GraphRAG 主题无交集。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/graphrag-context-window-8k-optimal.md`
- draft provenance: `../../drafts/provenance/graphrag-context-window-8k-optimal.md`
- similarity: `../../drafts/similarity/graphrag-context-window-8k-optimal.json`
- comparison provenance: `../../drafts/comparison/graphrag-context-window-8k-optimal.md`
