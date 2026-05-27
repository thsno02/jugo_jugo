---
schema: accepted_card_provenance.v3
card: ../cards/locomo-long-context-adversarial-collapse.md
material_id: arxiv-locomo
digest_id: digest_arxiv-locomo
source_paths:
  - data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt
draft_card: ../../drafts/cards/locomo-long-context-adversarial-collapse.md
draft_provenance: ../../drafts/provenance/locomo-long-context-adversarial-collapse.md
similarity_result: ../../drafts/similarity/locomo-long-context-adversarial-collapse.json
comparison_provenance: ../../drafts/comparison/locomo-long-context-adversarial-collapse.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T10:55:00+08:00
  gate_notes: 6/6 项通过；QA F1 表 + 单调下降趋势 + GPT-4 对照 + speaker mis-attribution + 模型版本边界齐备。
created_time: 2026-05-26T15:30:00+08:00
edited_time: 2026-05-27T10:55:00+08:00
edited_entity: llm
---

## 源证据

- 行 366–392（`tab:qa_results`）：完整 QA F1 表格。
  - Base / GPT-3.5-turbo / 4K：Adversarial 12.8
  - Base / GPT-4-turbo / 4K：Adversarial **70.2**
  - Base / Llama-2-Chat-70B / 4K：Adversarial 22.1
  - Long-context / GPT-3.5-turbo-16K：4K=13.1，8K=8.4，12K=6.4，16K=**2.1**
  - 16K overall = 37.8（行 386）

- 行 442–445（§6.1 QA 结果解读）：
  - "long-context LLMs can comprehend longer narratives, yet they are prone to generating hallucinations. \texttt{gpt-3.5-turbo-16k} outperforms other approaches, but its performance on adversarial questions drops to a mere 2.1\%, as compared to 22.1\% using \texttt{Llama-2-Chat} and 70.2\% using \texttt{GPT-4-turbo} with 4K context windows. This indicates that LLMs can be easily misled into generating hallucinations when they are subjected to long contexts"（行 444）

- 行 191–196（intro 总结 findings）：
  - "long-context LLMs demonstrate significant difficulty with adversarial questions in the QA task, showing a performance that is 83\% lower than the base model. They are especially prone to misassigning dialogs or events to the wrong speaker."（行 193）

- 行 657（`tab:dataset_statistics`）："# questions. adversarial & 1,871 (24.9\%)"。

- 行 767（`tab:summary_errors` "Speaker attribution" 行）：佐证 speaker mis-attribution 是独立观察到的错误类。

## 卡片范围是否成立

- 全部数字直接来自论文表。
- 卡片把"长上下文越长 adversarial 越塌"做成单调下降趋势——这是表数据直接显示的，没有引申。
- "操作含义" 中关于 RAG observation 在 adversarial 上拿到 44.7 的对比，引用自论文 `tab:qa_rag_results`（在另一张卡 `locomo-observation-rag-beats-summary-rag` 已记录），交叉引用合理。
- 边界中"2024 之后模型未必复现"是合理免责声明，未声称是论文断言。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T10:55:00+08:00
- 检查要点：
  - source_claim 卡给出明确数字、表格、解读与边界，非标题复述。
  - 知识密度合格。
  - source_ids 含 `arxiv-locomo`，正文锚回 agent_source_bundle.txt 行 366-392 / 442-445 / 191-196。
  - 含 `## References` 与 `## Footnotes`。
  - frontmatter 字段完整。
  - related 已挂上 5 张相关卡。

## 备注

- 与 `locomo-three-task-evaluation-framework` 卡互补：那张卡已经提到 adversarial 在 long-context 下塌到 2.1%，但是作为"五类 reasoning 之一"一句话带过；本卡把这条数字提升为独立的失败模式分析。
- 适合在未来 wiki 写"长上下文 vs RAG vs adversarial 控制项"主题时被反复引用。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/locomo-long-context-adversarial-collapse.md`
- draft provenance: `../../drafts/provenance/locomo-long-context-adversarial-collapse.md`
- similarity: `../../drafts/similarity/locomo-long-context-adversarial-collapse.json`
- comparison provenance: `../../drafts/comparison/locomo-long-context-adversarial-collapse.md`
