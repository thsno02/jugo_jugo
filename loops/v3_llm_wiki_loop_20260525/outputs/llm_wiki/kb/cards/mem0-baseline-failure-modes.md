---
id: mem0-baseline-failure-modes
title: Mem0 论文里 5 个 baseline 各自的失败模式（不是统一败给 Mem0）
status: accepted
card_type: distinction
tags: [#memory, #mem0, #baselines, #LangMem, #Zep, #A-Mem, #OpenAI-memory]
created_time: 2026-05-26T15:20:00+08:00
edited_time: 2026-05-28T10:54:00+08:00
edited_entity: llm
source_ids: [arxiv-mem0]
provenance_card: ../provenance/mem0-baseline-failure-modes.md
aliases: [mem0 baseline analysis, why baselines fail on LOCOMO]
related: [zep-graphiti-three-tier-graph, zep-bi-temporal-edges, longmemeval-commercial-system-failure-modes, mem0-locomo-benchmark-evaluation, zep-dmr-benchmark-critique]
---

## 为什么要分别看

Mem0 论文的标题数字（91% p95 lower latency、26% J over OpenAI）容易让人以为 baseline 是被同一种短板拖垮的。实际上 Table 2 与 §4.1–§4.3 显示**五个 baseline 各有完全不同的失败模式**[^src1]，这是讨论"通用 memory 系统该怎么设计"时不能跳过的细节。

## LangMem：搜索延迟塌房

- Overall J **58.10** —— 不算差；
- **搜索 latency p50 = 17.99s，p95 = 59.82s**——比 Mem0 高三个数量级；
- 论文判定 LangMem **"impractical for interactive applications"**[^src2]；
- 失败定位：LangMem 把"hot path"插入每次对话，但其检索/重写流程涉及多次 LLM 调用，端到端延迟无法承受。
- 含义：质量分高 ≠ 可生产部署；这是 LangMem 唯一一项被论文直接给出运营级否定的判定。

## Zep：图构建异步 + token 通胀 + 即时一致性问题

- Overall J **65.99**——和 Mem0 一线竞争；
- **token/对话约 600k**（Mem0 的 ~85 倍，Mem0g 的 ~43 倍）：每个图节点缓存全摘要 + 边上又存事实，**冗余巨大**；
- 论文观察到 Zep 添加 memory 后**短时间内即时检索常常答错**，需要等"数小时"再 query 才能恢复正常——猜测是异步 LLM 图构建尚未完成[^src3]；
- 含义：Zep 在静态质量上接近 Mem0，但**"加内存后能不能立刻用"是真实生产差距**。Mem0 自报最坏情况下图构建 <1 分钟。这一现象与 Zep Graphiti 显式分三层 + bi-temporal edges 的架构有关[^v3-1][^v3-2]。

## OpenAI ChatGPT memory：时间戳丢失

- Overall J **52.90**；
- **search latency = N/A**——OpenAI 没暴露选择性检索 API，整段对话的所有 memory 全塞 prompt；
- **temporal J 跌到 21.71**（甚至更早表中 ELI5-style temporal 跌至 14.04 F1）；
- 论文归因：**即便显式 prompt 要求 timestamps，OpenAI 大部分生成 memory 还是没带时间戳**[^src4]——所以下游问"什么时候"类问题直接失败；
- 含义：黑盒服务的 prompt 控制力有限，"我让它写时间戳" 不等于"它真的写了"。LongMemEval 上 ChatGPT 的 KU 覆盖式压缩是更细的同源观察[^v3-3]。

## A-Mem：自动 link 在 LLM-judge 下不达标

- 论文给出两个 A-Mem 行：原作者上报 F1 不错（temporal F1 45.85），但论文用 temperature=0 重跑得到 **J 49.91，single-hop J 39.79，multi-hop J 18.85**[^src5]——比 Mem0 的 67.13 / 51.15 差 25–32 个 J；
- A-Mem 用"semantic links + 更新机制"维护笔记网络，但 LLM-as-Judge 评测下其 retrieval 输出明显不及 dense memory；
- 含义：A-Mem 的高 F1 主要来自 lexical 重叠，**LLM-as-Judge 把它的相对优势削掉了**——这是单独依赖 F1 / BLEU 排序的典型坑。

## Full-context：质量天花板但延迟塌房

- Overall J **72.90**——表里最高；
- **p50 total = 9.870s, p95 = 17.117s**[^src6]；
- 含义：把 26k tokens 整段塞 prompt 仍然是"事实精度天花板"，但**端到端延迟比 Mem0 高 12 倍**；论文把这条作为"reference upper bound but not deployable"使用——这正是 Mem0 91% p95 reduction 数字的对照锚点。

## 模式总结

不是同一个短板：

- **LangMem** 因为运营级延迟；
- **Zep** 因为 token 通胀 + 异步一致性；
- **OpenAI** 因为元数据（时间戳）丢失；
- **A-Mem** 因为 retrieval 质量在严格 judge 下不达标；
- **Full-context** 因为延迟与成本。

设计自家 memory 系统时应**对这五种失败模式各做防御**，而不是只盯"J 分高低"。完整数字与 RAG 对照见 LOCOMO 评估卡[^v3-4]，与 LongMemEval 商业系统 pilot 的失败模式形成跨 benchmark 的互证[^v3-5]。

## Footnotes

[^src1]: `data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` — `sections/result.tex` 第 1047–1085 行（§4 主表）+ 第 1218–1310 行（§4.3 / Table 2）— 各 baseline F1/B1/J 全部数据；每个方法的 token/延迟/J 三轴。
[^src2]: `data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` — `result.tex` 第 1305 行 — "LangMem exhibits even higher search latencies (p50: 17.99s, p95: 59.82s), rendering it impractical for interactive applications."
[^src3]: `data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` — 第 1316 行 — "After adding memories to Zep's system, we observed that immediate memory retrieval attempts often failed to answer our queries correctly. Interestingly, re-running identical searches after a delay of several hours yielded considerably better results. This latency suggests that Zep's graph construction involves multiple asynchronous LLM calls and extensive background processing, making the memory system impractical for real-time applications."
[^src4]: `data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` — 第 1212 行 — "OpenAI notably underperforms, with scores below 15%, primarily due to missing timestamps in most generated memories despite explicit prompting in the OpenAI ChatGPT to extract memories with timestamps."
[^src5]: `data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` — Table 1 第 1068–1069 行 — A-Mem 原始 vs 重跑分：原 paper "A-Mem"行 F1=27.02/12.14/44.65/45.85，无 J；论文重跑 "A-Mem*" 行 F1=20.76/9.22/33.34/35.40, J=39.79/18.85/54.05/49.91。
[^src6]: `data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` — Table 2 第 1252 行 — "Full-context & & 26031 & - & - & 9.870 & 17.117 & 72.90 ± 0.19%"。
[^v3-1]: [zep-graphiti-three-tier-graph](zep-graphiti-three-tier-graph.md) — Zep Graphiti 三层架构与异步 LLM 图构建对应。
[^v3-2]: [zep-bi-temporal-edges](zep-bi-temporal-edges.md) — Zep 的 bi-temporal edges 是 token 通胀的部分来源。
[^v3-3]: [longmemeval-commercial-system-failure-modes](longmemeval-commercial-system-failure-modes.md) — LongMemEval 对 ChatGPT KU 覆盖式压缩的细致拆解。
[^v3-4]: [mem0-locomo-benchmark-evaluation](mem0-locomo-benchmark-evaluation.md) — 完整 LOCOMO 评估数字。
[^v3-5]: [zep-dmr-benchmark-critique](zep-dmr-benchmark-critique.md) — Zep 对 DMR 区分度不足的批评，与本卡 A-Mem F1 vs J 差异同一类问题。
