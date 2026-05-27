---
schema: accepted_card_provenance.v3
card: ../cards/graphrag-root-community-token-efficiency.md
material_id: arxiv-graphrag
digest_id: digest_arxiv-graphrag
source_paths:
  - data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt
draft_card: ../../drafts/cards/graphrag-root-community-token-efficiency.md
draft_provenance: ../../drafts/provenance/graphrag-root-community-token-efficiency.md
similarity_result: ../../drafts/similarity/graphrag-root-community-token-efficiency.json
comparison_provenance: ../../drafts/comparison/graphrag-root-community-token-efficiency.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T10:07:00+08:00
  gate_notes: 6/6 项通过：表格数字 + 9-43x / 97% 节省叙述 + 胜率 + empowerment 反向边界，证据全部锚定行号。
created_time: 2026-05-26T11:02:00+08:00
edited_time: 2026-05-27T10:07:00+08:00
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

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T10:07:00+08:00
- 检查要点：
  - 非标题复述：以"为什么这点重要"段 + "边界与误用"段实质展开。
  - 知识密度：C0/TS token 表 + 9-43× / 97% 数字 + 72%/62% 胜率 + empowerment 反向。
  - 源支撑：tab:community summaries 行 434-446、行 998-999、行 991-993、行 1027-1029。
  - References / Footnotes 存在。
  - frontmatter 完整。
  - related 字段 6 个 v3 draft id。

## 备注

- 与 `graphrag-leiden-community-hierarchy` 在 C0–C3 表上共用同一组数据。两张卡角度不同（结构 vs 成本），目前并行存在。
- 这一发现与 v2 中关于"分级摘要 / hierarchical summarization"的卡片可能重叠（v2 未发现该主题）。
- Adoption 阶段观察：comparison 三个 v2 候选 score 0.000，全部为 Karpathy llm-wiki 推文条目，与 GraphRAG / community summary / token budget 主题无交集。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/graphrag-root-community-token-efficiency.md`
- draft provenance: `../../drafts/provenance/graphrag-root-community-token-efficiency.md`
- similarity: `../../drafts/similarity/graphrag-root-community-token-efficiency.json`
- comparison provenance: `../../drafts/comparison/graphrag-root-community-token-efficiency.md`
