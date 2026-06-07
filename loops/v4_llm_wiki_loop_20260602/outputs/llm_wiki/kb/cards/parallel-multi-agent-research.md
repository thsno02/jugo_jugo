---
id: parallel-multi-agent-research
title: 并行多智能体研究机制
status: accepted
card_type: mechanism
tags: [llm-wiki, research, parallel-agents, credibility, gap-driven]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [llm-wiki-net]
justification: ../justification/parallel-multi-agent-research.md
canonical_concept: parallel-multi-agent-research
aliases: [并行研究, parallel agents, multi-agent research, 多智能体搜索]
summary: >-
  parallel-multi-agent-research（并行研究 / parallel agents / multi-agent research / 多智能体搜索）
  是 LLM Wiki 的研究核心机制：5-10 个智能体从学术/技术/应用/新闻/反面五个角度并行搜索，
  经可信度去重后摄入，每轮产出缺口报告驱动迭代
related: [thesis-driven-research, gap-mapping-promotion, ingest-operation]
---

LLM Wiki 的研究命令启动 **5-10 个并行智能体**同时搜索，每个智能体从不同角度出发[^src-1]：

- 默认 5 个智能体，`--deep` 提升至 8 个，`--retardmax` 提升至 10 个[^src-2]
- 角度覆盖：学术（academic）、技术（technical）、应用（applied）、新闻（news）、反面（contrarian）[^src-3]
- 每个智能体执行 2-3 次网络搜索、全文抓取、质量评分（1-5 分）[^src-4]

搜索完成后经过**可信度通道（credibility pass）**去重，筛选出的优质来源存入 `raw/`（不可变），再由编译通道综合为带交叉引用和置信度评分的 wiki 文章[^src-5]。

每轮结束后产出**缺口报告（gap report）**——列出已覆盖和仍缺失的内容，并提供后续建议。如果有 2 个以上缺口，可选择并行关闭[^src-6]。配合 `--min-time` 可持续多轮迭代，每轮深入前一轮发现的缺口[^src-7]。

配合 `--plan` 可先将广泛主题分解为独立研究路径，再为每条路径各启动一个 5 智能体群（swarm），所有路径同时执行[^src-8]。

并行研究机制与论点驱动模式共享基础设施，但角度分配不同：通用研究按信息源类型（学术/技术/新闻等）分工，论点模式按主张立场（支持/反对/机制等）分工[^card-1]。缺口报告是研究轮次间的桥梁，与 llm-wiki-karpathy 运行时的 kb_map_gaps / kb_promote_gap 操作在功能上对齐——两者都识别知识空白并驱动补全[^card-2]。研究产出的来源经过可信度通道筛选后，最终通过摄入操作进入 wiki 的三层结构[^card-3]。

## Footnotes

[^card-1]: [论点驱动研究模式](thesis-driven-research.md) -- 论点模式是并行研究的特化变体：同一基础设施，但角度从信息源类型替换为主张立场
[^card-2]: [缺口映射与晋升机制](gap-mapping-promotion.md) -- 缺口报告与 kb_map_gaps 在功能上对齐：都识别知识空白并驱动补全
[^card-3]: [摄入操作](ingest-operation.md) -- 研究产出经可信度筛选后通过摄入操作进入 wiki 三层结构

[^src-1]: `data/raw/webpage/llm-wiki-net/text.txt` -- "Research" section L20-22 -- "5-10 parallel agents search academic, technical, applied, news, and contrarian angles."
[^src-2]: `data/raw/webpage/llm-wiki-net/text.txt` -- "Stage 2" L285 -- "5 agents (8 with --deep, 10 with --retardmax) search simultaneously from different angles"
[^src-3]: `data/raw/webpage/llm-wiki-net/text.txt` -- "Quick Start" L250 -- "Five parallel agents search the web from different angles (academic, technical, applied, news, contrarian)"
[^src-4]: `data/raw/webpage/llm-wiki-net/text.txt` -- "Stage 2" L286 -- "2-3 web searches each, full-content fetch, quality scoring (1-5)"
[^src-5]: `data/raw/webpage/llm-wiki-net/text.txt` -- "Stage 2-3" L286-290 -- "A credibility pass deduplicates before ingestion... synthesizes them into wiki articles under wiki/concepts/, wiki/topics/, and wiki/references/"
[^src-6]: `data/raw/webpage/llm-wiki-net/text.txt` -- "Stage 4" L293-295 -- "After each round, you see what's covered, what's still missing, and suggested follow-ups."
[^src-7]: `data/raw/webpage/llm-wiki-net/text.txt` -- "Multi-round" L296 -- "Add --min-time 2h to keep researching in rounds, each drilling into gaps the previous round found."
[^src-8]: `data/raw/webpage/llm-wiki-net/text.txt` -- "Deep research with --plan" L351-356 -- "decomposes your research into independent paths and runs them all in parallel"
