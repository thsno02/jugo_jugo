---
schema: draft_card_provenance.v3
draft_card: ../cards/graphrag-root-community-token-efficiency.md
material_id: arxiv-graphrag
digest_id: digest_arxiv-graphrag
source_paths:
  - data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt
created_time: 2026-05-26T11:02:00+08:00
edited_time: 2026-05-26T11:02:00+08:00
edited_entity: llm
---

## 源证据

- 表格 caption（行 434）：
  > "Map-reduce summarization of source texts is the most resource-intensive approach requiring the highest number of context tokens. Root-level community summaries (C0) require dramatically fewer tokens per query (9x-43x)."
- 表数据（行 438–446）：Podcast C0 = 34 单元 / 26,657 tokens / 2.6%；News C0 = 55 单元 / 39,770 tokens / 2.3%。
- 行 998：
  > "for low-level community summaries (C3), GraphRAG required 26-33% fewer context tokens, while for root-level community summaries (C0), it required over 97% fewer tokens."
- 行 999：
  > "For a modest drop in performance compared with other global methods, root-level GraphRAG offers a highly efficient method for the iterative question answering that characterizes sensemaking activity, while retaining advantages in comprehensiveness (72% win rate) and diversity (62% win rate) over vector RAG."
- Empowerment 反向证据（行 991–993）：
  > "the ability to provide specific examples, quotes, and citations was judged to be key to helping users reach an informed understanding. Tuning element extraction prompts may help to retain more of these details in the GraphRAG index."
- Future work：embedding 局部匹配 + 社群报告 just-in-time（行 1027–1029）。

## 卡片范围是否成立

卡片把"两个具体数据集上 C0 vs TS 的 token 比例"和"C0 vs SS 的胜率"这两组论文原表数据做成了运营建议。两组数字均按原文引述，未做插值。"对话式 / 看板式 LLM 应用里把 C0 当默认上下文"这一句是从论文 §5.2 future work 中"hybrid RAG schemes that combine embedding-based matching with just-in-time community report generation"做的合理引申，仍在论文原始视角内。

## 发表门控结果

本轮未运行。

## 备注

- 与 `graphrag-leiden-community-hierarchy` 在 C0–C3 表上共用同一组数据。两张卡角度不同（结构 vs 成本），目前并行存在；comparison provenance 阶段决定是否合并。
- 这一发现与 v2 中关于"分级摘要 / hierarchical summarization"的卡片可能重叠。
