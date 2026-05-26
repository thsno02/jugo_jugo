---
schema: draft_card_provenance.v3
draft_card: ../cards/locomo-three-task-evaluation-framework.md
material_id: arxiv-locomo
digest_id: digest_arxiv-locomo
source_paths:
  - data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt
created_time: 2026-05-26T14:10:00+08:00
edited_time: 2026-05-26T14:10:00+08:00
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

本轮未运行。

## 备注

- 与 longmemeval-五大核心记忆能力卡可对照：LongMemEval 后来把 reasoning 重新划成五类（IE/MR/KU/TR/ABS），KU = knowledge-update 是 LoCoMo 五类里没有的能力。
