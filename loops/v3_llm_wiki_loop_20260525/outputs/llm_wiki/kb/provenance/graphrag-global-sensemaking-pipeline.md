---
schema: accepted_card_provenance.v3
card: ../cards/graphrag-global-sensemaking-pipeline.md
material_id: arxiv-graphrag
digest_id: digest_arxiv-graphrag
source_paths:
  - data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt
draft_card: ../../drafts/cards/graphrag-global-sensemaking-pipeline.md
draft_provenance: ../../drafts/provenance/graphrag-global-sensemaking-pipeline.md
similarity_result: ../../drafts/similarity/graphrag-global-sensemaking-pipeline.json
comparison_provenance: ../../drafts/comparison/graphrag-global-sensemaking-pipeline.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T10:03:00+08:00
  gate_notes: 6/6 项通过：索引五步 + 查询 map-reduce + 评测胜率全部锚定到论文行号。
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-27T10:03:00+08:00
edited_entity: llm
---

## 源证据

- 摘要原文（行 671–680）：
  > "RAG fails on global questions directed at an entire text corpus, such as 'What are the main themes in the dataset?', since this is inherently a query-focused summarization (QFS) task ... Our approach uses an LLM to build a graph index in two stages: first, to derive an entity knowledge graph from the source documents, then to pregenerate community summaries for all groups of closely related entities."
- §3.1 Methods 给出 6 个小节标题，对应卡片里的索引五步（行 769、776、808、821、829）。
- 查询时 map-reduce 三步直接引自行 853–857：
  > "Prepare community summaries. Community summaries are randomly shuffled and divided into chunks of pre-specified token size."
  > "Map community answers. Intermediate answers are generated in parallel. ... Answers with score 0 are filtered out."
  > "Reduce to global answer. Intermediate community answers are sorted in descending order of helpfulness score ..."
- §4.1 Results 给出 vector RAG vs 全局方法的胜率与显著性（行 987–989）：
  > "global approaches achieved comprehensiveness win rates between 72-83% (p<.001) for Podcast transcripts and 72-80% (p<.001) for News articles, while diversity win rates ranged from 75-82% (p<.001) and 62-71% (p<.01) respectively."
- "Directness as validity test confirmed that vector RAG produces the most direct responses" 同样出现在行 989，支撑卡片里"directness 反向"这一边界。

## 卡片范围是否成立

卡片只复述了论文 §3.1 Methods 的索引步骤、§3.1.6 的 map-reduce 查询机制，以及 §4 Results 中报告的胜率。所有数字均按原文引用，未做外推。"~100 万 token 量级"对应论文报告的 Podcast (~1M tokens) 和 News (~1.7M tokens)（行 931、934）。卡片的边界段落只强调了 vector RAG 在 directness 上更强这一论文显式发现，并未声称 GraphRAG 在事实型问题上失败——这是合理引申，因为 directness 衡量的就是"specifically and clearly addresses the question"（行 499）。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T10:03:00+08:00
- 检查要点：
  - 非标题复述：以"索引阶段 + 查询阶段"两段实质机制铺开。
  - 知识密度：索引五步骤 + 查询 map-reduce 三步 + 胜率数字 + directness 反向边界。
  - 源支撑：source_ids=[arxiv-graphrag]；行 671-680、769-829、853-857、987-989 多锚点。
  - References / Footnotes 存在。
  - frontmatter 完整。
  - related 字段 7 个 v3 draft id。

## 备注

- v2 可能已有"GraphRAG 概念卡"。如已存在，应将本卡作为 `merge_candidate`，按"索引-查询双阶段"补足细节后再合并。
- Adoption 阶段观察：comparison 三个 v2 候选 score ≤ 0.07 全部是 Karpathy llm-wiki 元描述，shared token 仅「的」，无 fusion 必要——v2 实际无 GraphRAG 邻近卡。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/graphrag-global-sensemaking-pipeline.md`
- draft provenance: `../../drafts/provenance/graphrag-global-sensemaking-pipeline.md`
- similarity: `../../drafts/similarity/graphrag-global-sensemaking-pipeline.json`
- comparison provenance: `../../drafts/comparison/graphrag-global-sensemaking-pipeline.md`
