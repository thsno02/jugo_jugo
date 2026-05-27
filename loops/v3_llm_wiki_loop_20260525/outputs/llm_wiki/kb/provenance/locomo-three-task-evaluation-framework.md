---
schema: accepted_card_provenance.v3
card: ../cards/locomo-three-task-evaluation-framework.md
material_id: arxiv-locomo
digest_id: digest_arxiv-locomo
source_paths:
  - data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt
draft_card: ../../drafts/cards/locomo-three-task-evaluation-framework.md
draft_provenance: ../../drafts/provenance/locomo-three-task-evaluation-framework.md
similarity_result: ../../drafts/similarity/locomo-three-task-evaluation-framework.json
comparison_provenance: ../../drafts/comparison/locomo-three-task-evaluation-framework.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T11:08:00+08:00
  gate_notes: 6/6 项通过；三任务分工 + 五类 reasoning + long-context 跨任务差异 + 边界齐备。
created_time: 2026-05-26T14:10:00+08:00
edited_time: 2026-05-27T11:08:00+08:00
edited_entity: llm
---

## 源证据

- 第 296-310 行（QA 任务定义 + 五类 reasoning + F1 metric + recall@k）。
- 第 312-324 行（事件摘要任务 + FactScore precision/recall）。
- 第 327-333 行（多模态对话生成 + MMRelevance）。
- 第 443-444 行（QA 实验结果："$\texttt{gpt-4-turbo}$ ... overall score of 32.4, it notably lags behind the human benchmark of 87.9"；adversarial 在 long-context 上降到 2.1%）。
- 第 491 行（long-context 在事件摘要上 precision -3%、recall -8.7%）。

## 卡片范围是否成立

- 三任务划分与五类 reasoning 直接出自论文标题和正文，零引申。
- "long-context 在 QA 上更强但在事件摘要上更弱"是论文 §6.1-6.2 的直接发现，并未跨章节合成。
- "adversarial 失败更多反映模型本身"是对实验表的合理解读：表 1 显示 GPT-4-turbo（4K）70.2 vs GPT-3.5-turbo-16K 2.1。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T11:08:00+08:00
- 检查要点：
  - 三任务定义清晰，非标题复述。
  - 知识密度合格：任务定义 + 五类 reasoning + 设计原因 + 边界。
  - source_ids 含 `arxiv-locomo`，正文锚到第 296-333 行 / 443-444 / 491。
  - 含 `## References` 与 `## Footnotes`。
  - frontmatter 字段完整。
  - related 已挂上 6 张相关卡。

## 备注

- 与 longmemeval-五大核心记忆能力卡可对照：LongMemEval 后来把 reasoning 重新划成五类（IE/MR/KU/TR/ABS），KU = knowledge-update 是 LoCoMo 五类里没有的能力。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/locomo-three-task-evaluation-framework.md`
- draft provenance: `../../drafts/provenance/locomo-three-task-evaluation-framework.md`
- similarity: `../../drafts/similarity/locomo-three-task-evaluation-framework.json`
- comparison provenance: `../../drafts/comparison/locomo-three-task-evaluation-framework.md`
