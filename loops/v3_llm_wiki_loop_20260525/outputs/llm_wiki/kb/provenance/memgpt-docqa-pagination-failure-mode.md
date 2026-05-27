---
schema: accepted_card_provenance.v3
card: ../cards/memgpt-docqa-pagination-failure-mode.md
material_id: arxiv-memgpt
digest_id: digest_arxiv-memgpt
source_paths:
  - data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt
draft_card: ../../drafts/cards/memgpt-docqa-pagination-failure-mode.md
draft_provenance: ../../drafts/provenance/memgpt-docqa-pagination-failure-mode.md
similarity_result: ../../drafts/similarity/memgpt-docqa-pagination-failure-mode.json
comparison_provenance: ../../drafts/comparison/memgpt-docqa-pagination-failure-mode.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T14:32:00+08:00
  gate_notes: 6/6 项通过；失败模式刻画与源引用紧密对齐。
created_time: 2026-05-26T15:30:00+08:00
edited_time: 2026-05-27T14:32:00+08:00
edited_entity: llm
---

## 源证据

1. `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` 第 1454–1464 行（DocQA 任务定义与基础设置）：

> "we benchmark MemGPT against fixed-context baselines on the retriever-reader document QA task from [Liu 2023]. ... In our evaluation setup, both the fixed-context baselines and MemGPT use the same retriever ... We use MemGPT's default storage settings which uses PostgreSQL for archival memory storage with vector search enabled via the pgvector extention. We pre-compute embeddings and load them into the database, which uses an HNSW index to enable approximate, sub-second query times."

2. 第 1486 行（早停 paging）：

> "While MemGPT is theoretically not limited by sub-optimal retriever performance (even if the embedding-based ranking is noisy, as long as the full retriever ranking contains the gold document it can still be found with enough retriever calls via pagination), we observe that MemGPT will often stop paging through retriever results before exhausting the retriever database."

3. 第 1503 行（GPT-3.5 退化）：

> "MemGPT has significantly degraded performance using GPT-3.5, due to its limited function calling capabilities, and performs best using GPT-4."

4. 第 1411 行（GPT-4 与 GPT-4 Turbo 持平）：

> "MemGPT's performance is unaffected by increased context length. ... Running MemGPT with GPT-4 and GPT-4 Turbo have equivalent results on this task."

5. `sections/appendix.tex` 第 1296–1312 行（DocQA agent 与 baseline prompt 全文）：

> "You are MemGPT DOC-QA bot. Your job is to answer questions about documents that are stored in your archival memory. The answer to the users question will ALWAYS be in your archival memory, so remember to keep searching if you can't find the answer."

—— prompt 显式让 LLM "keep searching"，但实测中 LLM 仍提前停止——这正佐证卡片对 "satisficing" 失败模式的解读。

## 卡片范围是否成立

本卡聚焦 DocQA：

- "理论上 retrieval recall 不再受 top-K 卡死"：直接来自第 1486 行；
- "实际中提前停止"：直接来自第 1486 行后半段；
- "GPT-4 vs GPT-4 Turbo 相同结果"：来自图 caption 第 1411 行；
- "需要给 agent 提供 explicit 已看过状态"是引申，但有 nested KV 与 DocQA 行为差异作为对比依据；
- prompt 已显式要求 "keep searching"，但模型仍提前停——证明仅靠 prompt 指令不足以解决 satisficing。

已有 5 张 MemGPT 卡均未覆盖 DocQA / NaturalQuestions 任务或 pagination 失败模式。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T14:32:00+08:00
- 检查要点：
  - 正文真正解释失败模式而非复述标题。
  - 知识密度足：任务设计、理论优势、真实失败模式、为什么是 agent control 问题、操作含义 5 节。
  - 源支撑：source_ids 非空；4 段 verbatim 引用 + 行号；prompt 全文亦在 provenance。
  - References + Footnotes 双在。
  - frontmatter 完整；related 列出 4 张同系列 MemGPT 卡。

## 备注

- 这是 MemGPT 论文里**唯一**一处明确承认自家系统结构性短板的段落，值得在比较卡 / agent control 系列里反复引用。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/memgpt-docqa-pagination-failure-mode.md`
- draft provenance: `../../drafts/provenance/memgpt-docqa-pagination-failure-mode.md`
- similarity: `../../drafts/similarity/memgpt-docqa-pagination-failure-mode.json`
- comparison provenance: `../../drafts/comparison/memgpt-docqa-pagination-failure-mode.md`
