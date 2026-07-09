---
id: memgpt-llm-judge-evaluation
title: MemGPT 实验中的 LLM Judge 评估方法
status: draft
card_type: methodology
tags: [memgpt, llm-judge, evaluation, gpt-4-judge, automated-evaluation]
created_time: 2026-06-12T10:28:00+08:00
edited_time: 2026-06-12T10:28:00+08:00
edited_entity: llm
source_ids: [arxiv-memgpt]
evidence_basis: peer-reviewed
justification: ../justification/experiment/memgpt-llm-judge-evaluation.md
canonical_concept: llm-judge-evaluation
aliases: [LLM评判评估, LLM judge, automated evaluation, GPT-4 judge]
summary: >-
  MemGPT llm-judge-evaluation 在 DMR 和 Document QA 中使用 GPT-4 作为 LLM Judge 评估正确性，引用 GPT-4 与人类评判高一致性的先行研究作为合理性依据；DMR 宽松评分（主题触及即 CORRECT），Document QA 要求答案+文档文本双重提供。
related: [memgpt-dmr-task-results, memgpt-document-qa-pagination]
---

MemGPT 在两个关键实验中使用 GPT-4 作为 LLM Judge 进行自动化评估：

**DMR 任务**：LLM Judge 被提供 question、gold answer、generated answer，判断 CORRECT 或 WRONG。评分标准是宽松的——"as long as it touches on the same topic as the gold answer, it should be counted as CORRECT"。同时使用 ROUGE-L recall 作为补充指标处理生成答案更冗长的情况。[^src-1]

**Document QA 任务**：LLM Judge 验证两点：(a) 答案是否正确；(b) 答案是否确实来自提供的文档文本（而非模型权重中的知识）。要求响应格式为 "ANSWER: [answer], DOCUMENT: [document_text]"。若缺少文档文本或回答 "INSUFFICIENT INFORMATION" 则判 INCORRECT。[^src-2]

**合理性依据**：论文引用 Zheng et al. (2023) 的研究表明 GPT-4 作为 judge 与人类评判具有高一致性。[^src-1]

然而，使用 GPT-4 同时作为被评估系统的底层模型和评估者存在潜在偏差——GPT-4 可能对自己生成的输出模式给出更高评分。此外，DMR 的宽松评分标准（主题触及即正确）可能掩盖了回答细节上的错误。论文未报告 LLM Judge 与人工标注的具体一致性数据。[^src-1]

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- Appendix: LLM Judge (DMR) -- "as long as it touches on the same topic as the gold answer, it should be counted as CORRECT... GPT-4 has been shown to have high agreement with human evaluators"
[^src-2]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- Appendix: LLM Judge (document analysis) -- "If the LLM response contains both the correct answer and corresponding document text, the response is correct."
[^card-1]: -> memgpt-dmr-task-results -- 本卡描述 DMR 的评估方法论，该卡报告 DMR 的数值结果
