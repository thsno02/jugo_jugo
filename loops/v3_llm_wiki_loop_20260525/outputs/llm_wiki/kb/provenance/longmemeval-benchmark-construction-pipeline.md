---
schema: accepted_card_provenance.v3
card: ../cards/longmemeval-benchmark-construction-pipeline.md
material_id: arxiv-longmemeval
digest_id: digest_arxiv-longmemeval
source_paths:
  - data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt
draft_card: ../../drafts/cards/longmemeval-benchmark-construction-pipeline.md
draft_provenance: ../../drafts/provenance/longmemeval-benchmark-construction-pipeline.md
similarity_result: ../../drafts/similarity/longmemeval-benchmark-construction-pipeline.json
comparison_provenance: ../../drafts/comparison/longmemeval-benchmark-construction-pipeline.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T11:12:00+08:00
  gate_notes: 6/6 项通过；6 步管线 + 164/5%/70%/115k/1.5M/25-25-50 等关键数字 + 边界齐备。
created_time: 2026-05-26T15:20:00+08:00
edited_time: 2026-05-27T11:12:00+08:00
edited_entity: llm
---

## 源证据

- 行 1357–1392（§3.2 Benchmark Curation）：管线主线描述。
  - "We define an ontology of 164 user attributes in five categories: lifestyle, belongings, life events, situations context, and demographic information."（行 1373）
  - "Each evidence statement is then separately embedded into a task-oriented \textit{evidence session} created by self-chatting ... The user LLM is instructed to convey the evidence statement indirectly"（行 1375）
  - "To ensure the data quality, all the evidence sessions are then manually screened and edited"（行 1377）

- 行 887–921（属性本体表 `tab:attribute-ontology`）：列出全部 164 个属性的细分。

- 行 1565–1605（Appendix A.1 Dataset Construction）：补充实现细节。
  - "Llama 3 70B Instruct is used as the LLM in the pipeline."（脚注，对应行 1373）
  - "In total, approximately 1000 questions were generated for each question type, and the final yield rate is about 5\%."（行 1580）
  - "In total, roughly 70\% of the sessions are human edited."（行 1586）
  - 大海捞针类比与 distractor 混合：行 1591–1599 "Our approach is analogous to the needle-in-a-haystack test ... we always use the following mixture: 25\% ShareGPT, 25\% UltraChat, and 50\% simulated sessions"。
  - "we provide two standard settings: \BENCHMARK\textsubscript{\textsc{S}} ($\sim$115k tokens/question) and \BENCHMARK\textsubscript{\textsc{M}} (500 sessions, $\sim$1.5M tokens)."（行 1391）

- 行 944–953（`fig:benchmark-basic-stats` subfig1 caption）："Distribution of the location of the evidence statement within the evidence sessions. Most evidence statements are located at the beginning of the chat."——说明 evidence 位置被有意分散；正文行 1377 强调"distribute the evidence statement across different conversation positions"。

## 卡片范围是否成立

- 全部步骤、数字（164 / 5%/ 70% / 115k / 1.5M / 25-25-50）都直接来自论文文本。
- "abstention 是从其他题型改造的" 直接来自行 1371（"we draw 30 questions from the previous question types and modify them into 'false premise' questions"）。
- "为什么这套设计能成立" 一节是合理的设计解读，未引入论文未述断言；尤其"题与历史解耦让难度可控" 是论文行 1391 显式声称的（"compile chat histories of arbitrary length"）。
- 边界中提到的"LongMemEval-S/M 是 fixed 提供的两个 setting"由行 1391 支持。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T11:12:00+08:00
- 检查要点：
  - mechanism 卡 6 步管线 + 多组关键数字，非标题复述。
  - 知识密度合格：步骤 + 设计原因 + 边界。
  - source_ids 含 `arxiv-longmemeval`，正文锚到行 1357-1392 / 887-921 / 1565-1605 / 944-953。
  - 含 `## References` 与 `## Footnotes`。
  - frontmatter 字段完整。
  - related 已挂上 4 张相关卡。

## 备注

- 与 `longmemeval-five-core-memory-abilities` 卡互补：那张卡说"测哪 5 种能力"，本卡说"题目本身怎么来的"。
- 与 `longmemeval-three-stage-memory-framework` 卡分工不同：那张卡讲"被测系统的内部结构"，本卡讲"benchmark 数据本身的产线"。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/longmemeval-benchmark-construction-pipeline.md`
- draft provenance: `../../drafts/provenance/longmemeval-benchmark-construction-pipeline.md`
- similarity: `../../drafts/similarity/longmemeval-benchmark-construction-pipeline.json`
- comparison provenance: `../../drafts/comparison/longmemeval-benchmark-construction-pipeline.md`
