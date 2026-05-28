---
id: memgpt-docqa-pagination-failure-mode
title: MemGPT 在 DocQA 上能突破 retriever top-K 限制，但**早停 paging** 是它的真实失败模式
status: accepted
card_type: example_pattern
tags: [#memgpt, #document-qa, #NaturalQuestions, #retriever-pagination, #failure-mode]
created_time: 2026-05-26T15:30:00+08:00
edited_time: 2026-05-28T11:10:00+08:00
edited_entity: llm
source_ids: [arxiv-memgpt]
provenance_card: ../provenance/memgpt-docqa-pagination-failure-mode.md
aliases: [MemGPT NaturalQuestions evaluation, archival storage iteration, premature stop in pagination]
related: [memgpt-main-vs-external-context, memgpt-function-chaining-heartbeat, memgpt-nested-kv-multi-hop]
---

## 任务设计

MemGPT DocQA 评测建立在 `lost-in-the-middle` (Liu 2023) 的 retriever-reader 设置之上[^src1]：

- 来源：NaturalQuestions-Open，从中 sample 50 个问题；
- 检索语料：2018 年底 Wikipedia dump，**整库嵌入向量 (text-embedding-ada-002 / cosine) 公开发布**——这是论文一并 release 的 20M 文章 embedding；
- 后端：PostgreSQL + pgvector（HNSW index，sub-second 查询）[^src2]；
- baseline 与 MemGPT 共用同一 retriever；baseline 接收 top-$K$ 文档作为 prompt，MemGPT 把全 embedding 集合加载进 archival storage[^v3-1]，再用 `archival_memory_search` 函数自主翻；
- 评测用 LLM-judge，prompt 要求模型既给 ANSWER 又给 DOCUMENT，避免靠 weights 猜对。

## 理论优势

baseline 的天花板被 retriever recall@K 卡死：retriever 没把 gold passage 排进 top-K，baseline 就永远看不到。MemGPT 的"理论"上限不是 recall@K 而是 recall@∞——只要 retriever 的完整 ranking 里有 gold 文档，MemGPT 可以**通过 heartbeat 链式调用 search 函数 + 翻页**[^v3-2]，理论上能扫到第 N 页才命中也算成。

## 真实失败模式

论文实测发现 MemGPT 并没有实现这种"无限翻"[^src3]：

> "we observe that **MemGPT will often stop paging through retriever results before exhausting the retriever database**."

也就是说 — agent 自己决定"我看够了，可以回答了"的判断会**早于 retriever 真正交出 gold 文档**。这条 caveat 是 MemGPT 论文里**唯一一句**承认自家系统在 DocQA 上还有结构性问题。

附带观察：

- 当人为把检索文档截断到 fix 长度（fit fixed-context-window）做对比时，**截断越狠 baseline 越差**，但 MemGPT 仍受底层模型函数调用能力制约：**GPT-3.5 上 MemGPT 显著退化**[^src4]，**GPT-4 与 GPT-4 Turbo 结果相同**[^src5]；
- "结果相同"意味着在这个任务上**更长 context（GPT-4 Turbo 128k）并未给 MemGPT 带来额外收益**——MemGPT 的瓶颈在 retrieval 决策，不在 context 长度。

## 为什么这是个"agent control" 问题

- 翻页继续与否，是 LLM 自己根据当前 search results 决定的：若结果"看起来沾边"或"语义略相关"，模型容易选择直接 answer 而非再 search 一次；
- 缺乏"已检视 vs 待检视"集合的显式状态——MemGPT 没把"我目前看过哪些 page" 喂回 prompt（除了 message history），所以遇到一个长 ranking 时 LLM 倾向于停下；
- 这是与 nested KV 任务相反的现象：在 nested KV 里目标"明确缺失"才停（key 不再是 key），所以能稳定走 4 跳[^v3-3]；DocQA 里目标"模糊命中"也算成，所以提前停。

## 操作含义

- MemGPT-style agent 在 long-tail retrieval 任务上的关键工程点是"何时该再翻一页"——这需要：
  - 给 LLM **显式的"我已看过 N 页"状态**；
  - 给"提前 answer"加 explicit 代价（"未达 K 页禁止 answer"），或加 minimum-coverage 规则；
  - 用 ground-truth budget 而不是 LLM 自决——例如 force-paginate-until-K=20。
- 单纯允许 paginate 不够——LLM 倾向 satisfice。
- 这也意味着把 MemGPT 当 DocQA reader 来用时，**不要假设它能突破 retriever recall**——要在 prompt 层强制 paging 策略，或上层加 budget。

## Footnotes

[^src1]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` — experiments 行 1454–1488（§DocQA 设置）+ appendix 行 1296–1312（DocQA agent prompt 模板）。
[^src2]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` — experiments 行 1460 — "We use MemGPT's default storage settings which uses PostgreSQL for archival memory storage with vector search enabled via the pgvector extention. We pre-compute embeddings and load them into the database, which uses an HNSW index to enable approximate, sub-second query times."
[^src3]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` — experiments 行 1486 — "While MemGPT is theoretically not limited by sub-optimal retriever performance (even if the embedding-based ranking is noisy, as long as the full retriever ranking contains the gold document it can still be found with enough retriever calls via pagination), we observe that MemGPT will often stop paging through retriever results before exhausting the retriever database."
[^src4]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` — experiments 行 1503 — "MemGPT has significantly degraded performance using GPT-3.5, due to its limited function calling capabilities, and performs best using GPT-4."
[^src5]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` — 图 docqa caption 行 1411 — "MemGPT's performance is unaffected by increased context length. ... Running MemGPT with GPT-4 and GPT-4 Turbo have equivalent results on this task."
[^v3-1]: [memgpt-main-vs-external-context](memgpt-main-vs-external-context.md) — archival storage 是 MemGPT 五区之一。
[^v3-2]: [memgpt-function-chaining-heartbeat](memgpt-function-chaining-heartbeat.md) — heartbeat 是多跳搜索的机制基础。
[^v3-3]: [memgpt-nested-kv-multi-hop](memgpt-nested-kv-multi-hop.md) — nested KV 的对照成功案例。
