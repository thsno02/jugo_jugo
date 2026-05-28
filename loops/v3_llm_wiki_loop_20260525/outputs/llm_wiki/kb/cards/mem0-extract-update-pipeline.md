---
id: mem0-extract-update-pipeline
title: Mem0 提取-更新两阶段管线：把每对消息变成可增量管理的事实
status: accepted
card_type: mechanism
tags: [#memory, #llm-agent, #mem0, #incremental-pipeline]
created_time: 2026-05-26T11:30:00+08:00
edited_time: 2026-05-28T10:46:00+08:00
edited_entity: llm
source_ids: [arxiv-mem0]
provenance_card: ../provenance/mem0-extract-update-pipeline.md
aliases: [Mem0 pipeline, extraction phase, update phase, mem-zero]
related: [mem0-tool-call-add-update-delete-noop, mem0-graph-memory-variant, mem0-answer-generation-prompt-design, mem0-locomo-benchmark-evaluation, memgpt-main-vs-external-context, lightmem-sleep-time-offline-parallel-update]
---

## 设计目标

Chhikara 等 (2025, arXiv:2504.19413) 提出 Mem0（mem-zero）作为面向多轮长程对话的可扩展长期记忆架构，核心是把对话流"边走边整理"为结构化记忆，而不是把所有上下文塞进窗口、也不是 RAG 切块[^src1]。论文用"用户在第一会话中说自己是素食 + 拒绝乳制品，下一次问晚餐建议时希望不被推荐鸡肉或牛奶产品"作为最小诱因案例。

## 提取阶段（Extraction Phase）

每收到一对新消息 $(m_{t-1}, m_t)$（通常是 user 消息 + assistant 响应），系统组装三段上下文交给抽取函数 $\phi$（LLM 实现）[^src2]：

1. **对话级摘要 S**：由**异步摘要模块**周期性从数据库刷新，提供贯穿全对话的语义骨架，**不阻塞主管线**[^src3]。
2. **最近消息窗口** $\{m_{t-m}, \ldots, m_{t-2}\}$：超参 $m$ 控制窗口长度（实验中 $m=10$），给出粒度较细的时序线索。
3. **新消息对** $(m_{t-1}, m_t)$ 本身。

拼成 $P = (S, \{m_{t-m}, \ldots, m_{t-2}\}, m_{t-1}, m_t)$ 后，$\phi(P)$ 输出一组候选 salient memories $\Omega = \{\omega_1, \ldots, \omega_n\}$，即可能写入知识库的事实候选。

这个组合让抽取**同时拥有**全局主题理解（来自 S）和细粒度近期上下文（来自最近窗口），异步摘要让全局视图始终新鲜而不增加 ingestion 延迟。

## 更新阶段（Update Phase）

对每个候选事实 $\omega_i \in \Omega$，系统[^src4]：

1. 用向量嵌入从数据库**检索 top-$s$（实验 $s=10$）语义相似的现有记忆**；
2. 把候选事实 + 这些相似记忆一起通过 "tool call" 接口呈给 LLM；
3. 由 LLM 选择四种操作之一并执行：ADD / UPDATE / DELETE / NOOP[^v3-1]。

**关键设计选择**：不是用独立分类器，而是**直接利用 LLM 的推理能力**判断候选事实与现有记忆的语义关系，让操作选择本身就是语义任务[^src5]。

## 默认配置（论文实验）[^src6]

- 上下文窗口：$m = 10$ 条最近消息；
- 相似检索：$s = 10$ 条最相似已有记忆；
- 推理引擎：`GPT-4o-mini`（所有 LLM 调用）；
- 向量库：dense embeddings 支撑相似检索。

## 与现有路径的差异

- **vs 全 context**：避免在每个查询时塞入完整 26k token 对话历史；
- **vs RAG 切块**：不存储原始 token chunks，而是存"已抽取的、可增量更新的事实"——噪声更少；
- **vs MemGPT 的虚拟内存分页**：MemGPT 把上下文窗口当作 RAM、外部存储当作磁盘做 paging[^v3-2]，但**对"什么该保留"无设计立场**；Mem0 通过 update 阶段的 ADD/UPDATE/DELETE/NOOP 把保留决策显式化为语义任务。
- **vs LightMem 的 offline parallel update**：Mem0 把 update 留在 online，LightMem 把它推到 sleep-time 离线并行[^v3-3]；两者代表了 update 应该放在哪一侧的不同立场。
- 在 LongMemEval 三阶段框架视角下，Mem0 是"indexing 阶段完全 LLM 化"的典型实例[^v3-4]。

## Footnotes

[^src1]: `data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` — `sections/intro.tex` 第 1094–1128 行（§1 动机与素食晚餐示例）— 提出 Mem0 的 motivation 与 baseline 对照。
[^src2]: `data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` — `sections/proposed_work.tex` 第 1139–1158 行（§3.1）— 提取与更新阶段定义。
[^src3]: `data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` — 第 1153 行附近 — "we implement an asynchronous summary generation module that periodically refreshes the conversation summary. This component operates independently of the main processing pipeline."
[^src4]: `data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` — `sections/appendix.tex` 第 911–966 行（Algorithm 1）— 更新阶段伪代码。
[^src5]: `data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` — 第 1155 行 — "Rather than using a separate classifier, we leverage the LLM's reasoning capabilities to directly select the appropriate operation based on the semantic relationship between the candidate fact and existing memories."
[^src6]: `data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` — 第 1158 行 — "we configured the system with `m` = 10 previous messages for contextual reference and `s` = 10 similar memories for comparative analysis. All language model operations utilized `GPT-4o-mini`."
[^v3-1]: [mem0-tool-call-add-update-delete-noop](mem0-tool-call-add-update-delete-noop.md) — 四操作的语义与触发条件。
[^v3-2]: [memgpt-main-vs-external-context](memgpt-main-vs-external-context.md) — MemGPT 把上下文当 RAM、外部存储当磁盘的对照。
[^v3-3]: [lightmem-sleep-time-offline-parallel-update](lightmem-sleep-time-offline-parallel-update.md) — LightMem 把 update 推到离线的对立选择。
[^v3-4]: [longmemeval-three-stage-memory-framework](longmemeval-three-stage-memory-framework.md) — Mem0 在三阶段四控制点框架下的落点。
