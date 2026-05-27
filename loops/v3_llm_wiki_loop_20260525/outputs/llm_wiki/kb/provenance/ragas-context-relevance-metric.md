---
schema: accepted_card_provenance.v3
card: ../cards/ragas-context-relevance-metric.md
material_id: arxiv-ragas
digest_id: digest_arxiv-ragas
source_paths:
  - data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt
draft_card: ../../drafts/cards/ragas-context-relevance-metric.md
draft_provenance: ../../drafts/provenance/ragas-context-relevance-metric.md
similarity_result: ../../drafts/similarity/ragas-context-relevance-metric.json
comparison_provenance: ../../drafts/comparison/ragas-context-relevance-metric.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T14:30:00+08:00
  gate_notes: 6/6 通过；句子级算法、prompt 全文、公式、WikiEval 0.70 与 "hardest dimension" 自述均回到 L172–182 / L238–244 / L271。
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-27T14:30:00+08:00
edited_entity: llm
---

## 源证据

1. `agent_source_bundle.txt:172-182` —— Context Relevance 段完整算法。
2. `agent_source_bundle.txt:175-176` —— Extraction prompt 全文。
3. `agent_source_bundle.txt:181-182` —— CR 公式。
4. `agent_source_bundle.txt:120` —— 与 lost-in-the-middle 的关联。
5. `agent_source_bundle.txt:238-244, 271` —— CR accuracy = 0.70 与 "the hardest quality dimension" 描述。

## 卡片范围是否成立

- 卡片严格围绕 CR 算法 / 公式 / 设计要点 / 已知弱点展开，与 framework / 其它两张指标卡职责分离。
- "句子级公式无法识别同义重复" 是基于公式分子分母都按句子计数的合理工程读法。
- "F 与 CR 联合诊断 pipeline 失效点" 是 framework 卡定义的延续，本卡聚焦 CR 视角。
- "早期草稿曾尝试多次抽取 + BERTScore 但最终去掉" 是从源文件 line 178 的 commented-out 段落推得（论文草稿可见性证据）；已在 footnote 标注。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T14:30:00+08:00
- 检查要点：
  - 非标题复述：正文展开算法、设计要点、为何重要、边界，多段 substantive。
  - 知识密度：算法 + 设计动机 + pipeline 诊断含义 + 已知弱点。
  - 源支撑：source_ids 含 arxiv-ragas；L173 / L175–176 / L181–182 / L271 均有 verbatim。
  - References / Footnotes 齐备。
  - frontmatter 完整且合法。
  - related 已填充：6 张 Ragas / ALCE / RAGChecker 同簇 draft 卡。

## 备注

- CR 的"句子级"局限是 v2 已知讨论的潜在主题（chunking strategy），可在 comparison_provenance 阶段连接。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/ragas-context-relevance-metric.md`
- draft provenance: `../../drafts/provenance/ragas-context-relevance-metric.md`
- similarity: `../../drafts/similarity/ragas-context-relevance-metric.json`
- comparison provenance: `../../drafts/comparison/ragas-context-relevance-metric.md`
