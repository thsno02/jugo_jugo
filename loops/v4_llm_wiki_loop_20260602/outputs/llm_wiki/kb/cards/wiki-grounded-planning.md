---
id: wiki-grounded-planning
title: Wiki 锚定式实施规划
status: accepted
card_type: mechanism
tags: [llm-wiki, planning, evidence-based, implementation, requirements]
created_time: 2026-06-11T10:00:00+08:00
edited_time: 2026-06-11T10:00:00+08:00
edited_entity: llm
source_ids: [llm-wiki-net]
justification: ../justification/wiki-grounded-planning.md
canonical_concept: wiki-grounded-planning
aliases: [wiki锚定规划, wiki-grounded plan, 证据驱动规划, knowledge-backed planning]
summary: >-
  wiki-grounded-planning（wiki锚定规划 / wiki-grounded plan / 证据驱动规划 / knowledge-backed planning）
  是 LLM Wiki 的规划机制：读取知识库→访谈需求→针对性研究填补缺口→产出分阶段实施计划，
  每个决策引用 wiki 文章作为证据，支持 --format rfc|adr|spec 三种输出格式
related: [output-compounding-loop, parallel-multi-agent-research, audit-provenance-tracing]
---

`/wiki:plan` 命令实现**以 wiki 知识为锚点的实施规划**——计划中的每个决策都有来自已编译文章的证据支撑[^src-1]。

**四步流程**[^src-2]：
1. **读取知识库**——扫描当前 wiki 中相关文章作为决策依据
2. **需求访谈**——向用户提问以明确实施的具体约束和目标
3. **缺口研究**——当现有知识不足以支撑某个决策时，发起针对性研究填补空白
4. **产出计划**——生成分阶段的实施计划，每个关键决策引用 wiki 文章作为证据

**三种输出格式**[^src-3]：
- `--format rfc`——请求评论（Request for Comments）格式
- `--format adr`——架构决策记录（Architecture Decision Record）格式
- `--format spec`——规格说明（Specification）格式

这一机制的关键区分在于：**计划不是基于 LLM 的泛化知识，而是锚定在用户自己的知识库上**。如果 wiki 中缺乏支撑某个决策的证据，系统不会凭空生成建议，而是先通过研究填补缺口再输出。

从系统循环角度看，wiki-grounded planning 是产出复利循环的一个高杠杆实例[^card-1]——它既消费 wiki 中已积累的研究成果，自身产出的计划也回写进 wiki（存入 `output/`）供后续产出引用。规划中的缺口研究步骤复用了并行多智能体研究的基础设施[^card-2]。当计划引用了某篇 wiki 文章作为证据，审计机制可追溯验证该证据是否仍然可信[^card-3]。

## Footnotes

[^src-1]: `data/raw/webpage/llm-wiki-net/markdown.md` L38 -- "Wiki-grounded implementation plans. Reads the knowledge base, interviews you about requirements, fills gaps with targeted research, and produces a phased plan citing wiki articles as evidence."
[^src-2]: `data/raw/webpage/llm-wiki-net/markdown.md` L38 -- "Reads the knowledge base, interviews you about requirements, fills gaps with targeted research, and produces a phased plan citing wiki articles as evidence."
[^src-3]: `data/raw/webpage/llm-wiki-net/markdown.md` L38 -- "--format rfc|adr|spec."
[^card-1]: [产出复利循环](output-compounding-loop.md) -- wiki-grounded planning 是产出复利的高杠杆实例：消费已有研究，计划自身也回写进 wiki
[^card-2]: [并行多智能体研究机制](parallel-multi-agent-research.md) -- 规划中的缺口研究步骤复用并行研究基础设施
[^card-3]: [审计与溯源追踪](audit-provenance-tracing.md) -- 计划引用的 wiki 证据可通过审计机制追溯验证其可信度
