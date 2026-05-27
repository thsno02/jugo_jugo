---
schema: accepted_card_provenance.v3
card: ../cards/memgpt-dmr-task-evaluation.md
material_id: arxiv-memgpt
digest_id: digest_arxiv-memgpt
source_paths:
  - data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt
draft_card: ../../drafts/cards/memgpt-dmr-task-evaluation.md
draft_provenance: ../../drafts/provenance/memgpt-dmr-task-evaluation.md
similarity_result: ../../drafts/similarity/memgpt-dmr-task-evaluation.json
comparison_provenance: ../../drafts/comparison/memgpt-dmr-task-evaluation.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T14:30:00+08:00
  gate_notes: 6/6 项通过；正文密度高，源引用具体，frontmatter 完整。
created_time: 2026-05-26T15:25:00+08:00
edited_time: 2026-05-27T14:30:00+08:00
edited_entity: llm
---

## 源证据

1. `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` 第 1370–1376 行（DMR 任务定义）：

> "Each multi-session chat in MSC has five total sessions, and each session consists of a roughly a dozen messages. As part of our consistency experiments, we created a new session (session 6) that contains a single question-answer response pair between the same two personas. ... we generated the DMR question-answer (QA) pairs using a separate LLM that was instructed to write a question from one user to another that could only be answered correctly using knowledge gained from the past sessions."

2. 第 1378–1380 行（指标选型）：

> "We evaluate the quality of the generated response against the 'gold response' using ROUGE-L scores and an 'LLM judge' ... We use the ROUGE-L recall (R) metric to account for the verbosity of the generated agent replies compared to the relatively short gold answer labels."

3. 第 1388 行（baseline 设置）：

> "The baselines are able to see a lossy summarization of the past five conversations to mimic an extended recursive summarization procedure, while MemGPT instead has access to the full conversation history but must access it via paginated search queries to recall memory."

4. `tables/deep_memory_retrieval_table_singlecol.tex` 第 1813–1828 行（结果表）：

> "GPT-3.5 Turbo & 38.7% & 0.394 / + MemGPT & 66.9% & 0.629 / GPT-4 & 32.1% & 0.296 / + MemGPT & 92.5% & 0.814 / GPT-4 Turbo & 35.3% & 0.359 / + MemGPT & 93.4% & 0.827"

5. `sections/appendix.tex` 第 1231–1255 行（LLM judge prompt verbatim）：

> "Your task is to label an answer to a question as 'CORRECT' or 'WRONG'. ... Question: Do you remember what I got the last time I went to Hawaii? Gold answer: A shell necklace ..."

—— 这是 Mem0 后来"adapt elements from the prompt released by [MemGPT]"的同一段。

## 卡片范围是否成立

本卡集中于 DMR：

- 任务设计、双指标、结果表全部直接来自源；
- "GPT-4 baseline 反而比 GPT-3.5 baseline 差" 是表上直接观察，论文未深入分析（卡片中明确标注"论文未深入分析"，避免引申过头）。
- "92.5% 不等于永远不会忘"是 caveat，未越源。

与已有 5 张 MemGPT 卡（OS 类比 / 5 分区 / 队列驱逐 / heartbeat / nested KV）正交：没有任何一张已有卡覆盖 DMR 任务、ROUGE-L recall 选型理由、或 lossy summary baseline。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T14:30:00+08:00
- 检查要点：
  - 非标题复述，正文真正讲清 DMR 任务设计与双指标。
  - 知识密度足够：任务设计、双指标、主结果表、读法解释、为什么比 J 分有信息量、边界与误用 6 节。
  - 源支撑充分：source_ids 非空，正文 4 段 verbatim 引用 + 路径行号定位。
  - References 与 Footnotes 双存在，4 条 footnote 全部带源行号。
  - frontmatter 全字段在场，related 5 条全是 v3 draft id。

## 备注

- DMR 是 MemGPT 与 Mem0 共享的评估基础，可在比较卡片中作为锚点。
- adoption 阶段未发现需要修订的内容。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/memgpt-dmr-task-evaluation.md`
- draft provenance: `../../drafts/provenance/memgpt-dmr-task-evaluation.md`
- similarity: `../../drafts/similarity/memgpt-dmr-task-evaluation.json`
- comparison provenance: `../../drafts/comparison/memgpt-dmr-task-evaluation.md`
