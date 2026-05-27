---
schema: accepted_card_provenance.v3
card: ../cards/rag-chunk-level-faithfulness.md
material_id: arxiv-ragchecker
digest_id: digest_arxiv-ragchecker
source_paths:
  - data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt
draft_card: ../../drafts/cards/rag-chunk-level-faithfulness.md
draft_provenance: ../../drafts/provenance/rag-chunk-level-faithfulness.md
similarity_result: ../../drafts/similarity/rag-chunk-level-faithfulness.json
comparison_provenance: ../../drafts/comparison/rag-chunk-level-faithfulness.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T14:30:00+08:00
  gate_notes: 6/6 通过；现象有 L782–783 verbatim 引文，retriever-noise 折衷与数据库质量结论均回到论文章节，操作含义与边界分别标注。
created_time: 2026-05-26T11:30:00+08:00
edited_time: 2026-05-27T14:30:00+08:00
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

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T14:30:00+08:00
- 检查要点：
  - 非标题复述：正文展开 chunk 级 faithfulness 现象、retriever-noise 折衷、fixed-size chunking hidden cost、操作含义与边界，多段 substantive。
  - 知识密度：覆盖机制 + 反例 + 边界 + 操作含义，远超主题简介。
  - 源支撑：source_ids 含 arxiv-ragchecker；正文给出 L782–783 verbatim 引文与 L780/L784 章节引用。
  - References / Footnotes：均存在，定位到 agent_source_bundle.txt 第 780–784 行。
  - frontmatter 完整：id/title/card_type/tags/source_ids/provenance_card/created_time/edited_time/edited_entity 全部齐备。
  - related 已填充：5 张 RAGChecker / Ragas / ALCE 同簇 draft 卡。

## 备注

- 与 `ragchecker-generator-trilemma` 互补：trilemma 卡谈"调优时三向拉扯"，本卡谈"为什么 noise sensitivity 这一向会被 retriever 改善反推升高"。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/rag-chunk-level-faithfulness.md`
- draft provenance: `../../drafts/provenance/rag-chunk-level-faithfulness.md`
- similarity: `../../drafts/similarity/rag-chunk-level-faithfulness.json`
- comparison provenance: `../../drafts/comparison/rag-chunk-level-faithfulness.md`
