---
schema: accepted_card_provenance.v3
card: ../cards/longmemeval-five-core-memory-abilities.md
material_id: arxiv-longmemeval
digest_id: digest_arxiv-longmemeval
source_paths:
  - data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt
draft_card: ../../drafts/cards/longmemeval-five-core-memory-abilities.md
draft_provenance: ../../drafts/provenance/longmemeval-five-core-memory-abilities.md
similarity_result: ../../drafts/similarity/longmemeval-five-core-memory-abilities.json
comparison_provenance: ../../drafts/comparison/longmemeval-five-core-memory-abilities.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T11:24:00+08:00
  gate_notes: 6/6 项通过；IE/MR/KU/TR/ABS 五能力定义 + 7 问题类型 + 对比表 + 边界齐备。
created_time: 2026-05-26T14:20:00+08:00
edited_time: 2026-05-27T11:24:00+08:00
edited_entity: llm
---

## 源证据

- 第 1361-1369 行：五能力 IE / MR / KU / TR / ABS 的完整定义（论文 §3.2 起首 itemize）。
- 第 1371 行：7 个 question type 列表。
- 第 977-984 行：表 `tab:benchmark-comparison`，对比 LongMemEval 与 MSC、DuLeMon、MemoryBank、PerLTQA、LoCoMo、DialSim 在五能力上的覆盖。表内 LongMemEval 是唯一 5 项全 √。
- 第 1407 行：commercial systems 实验中"ChatGPT 修改之前记下的事实"——KU 失败的真实案例。
- 第 1629 行 appendix：相同发现的更详细描述。

## 卡片范围是否成立

- 五能力字面来自论文 §3.2，没有合并改写。
- "KU/ABS 是 LongMemEval 独有"直接对应对比表里 LoCoMo / MemoryBank / PerLTQA 在 KU 列的 ✗——是表中事实。
- "ChatGPT 在 KU 上失败"是论文 pilot 观察的引用，未跨论文综合。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T11:24:00+08:00
- 检查要点：
  - concept 卡给出五能力分明定义 + 与既有 benchmark 对比 + 设计动机 + 边界，非标题复述。
  - 知识密度合格。
  - source_ids 含 `arxiv-longmemeval`，正文锚到第 1361-1369 / 1371 / 977-984 行。
  - 含 `## References` 与 `## Footnotes`。
  - frontmatter 字段完整。
  - related 已挂上 5 张相关卡。

## 备注

- 与 v2 卡片无直接重叠；与 locomo-three-task-evaluation-framework 卡片配对成"长期记忆评测能力图谱"。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/longmemeval-five-core-memory-abilities.md`
- draft provenance: `../../drafts/provenance/longmemeval-five-core-memory-abilities.md`
- similarity: `../../drafts/similarity/longmemeval-five-core-memory-abilities.json`
- comparison provenance: `../../drafts/comparison/longmemeval-five-core-memory-abilities.md`
