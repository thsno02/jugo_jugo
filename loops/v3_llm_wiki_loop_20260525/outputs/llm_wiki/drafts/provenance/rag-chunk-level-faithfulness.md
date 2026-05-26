---
schema: draft_card_provenance.v3
draft_card: ../cards/rag-chunk-level-faithfulness.md
material_id: arxiv-ragchecker
digest_id: digest_arxiv-ragchecker
source_paths:
  - data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt
created_time: 2026-05-26T11:30:00+08:00
edited_time: 2026-05-26T11:30:00+08:00
edited_entity: llm
---

## 源证据

- 现象与解读（L782–783）：*"For every baseline RAG system, there's an apparent gap between its relevant and irrelevant noise sensitivity ... it further enhance the point that generators demonstrate a chunk-level faithfulness. It means a relevant chunk is trusted as a whole, while an irrelevant one only has minimal impact."*
- retriever recall ↔ noise sensitivity 折衷（L780–781）：*"As retriever claim recall increases, all generators become more sensitive to such noise."*
- 数据库质量（L783 末段）：*"This subtle yet significant distinction supports and explains the importance of the quality and specification of the database for a RAG system."*
- 开源模型 vs GPT-4（L784）：*"GPT-4 has both higher context utilization and lower noise sensitivity than the other three open source models."*

## 卡片范围是否成立

- 这是 RAGChecker 论文的关键观察之一，独立于"三难"结论；后者描述 prompt 调优的张力，本卡描述 chunk 颗粒度的"信任开关"现象，互为补充。
- 直接来自源材料：现象本身、retriever recall × noise 折衷、数据库质量结论。
- 引申：claim-level 过滤 vs 缩 chunk size 的建议——属于工程直觉外推，论文未明文给出。已用"操作含义"标记，避免被误读为论文主张。

## 发表门控结果

本轮未运行。

## 备注

- 与 `ragchecker-generator-trilemma` 互补：trilemma 卡谈"调优时三向拉扯"，本卡谈"为什么 noise sensitivity 这一向会被 retriever 改善反推升高"。
