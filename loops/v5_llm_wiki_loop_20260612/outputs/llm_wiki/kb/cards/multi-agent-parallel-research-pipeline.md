---
id: multi-agent-parallel-research-pipeline
title: 多 Agent 并行研究管线与模式分级
status: accepted
card_type: system-design
tags:
- llm-wiki
- multi-agent
- parallel-research
- research-pipeline
- credibility-scoring
- retardmax
created_time: 2026-06-12 18:00:00+08:00
edited_time: 2026-06-12 18:00:00+08:00
edited_entity: llm
source_ids:
- repo-nvk-llm-wiki
evidence_basis: code_implementation
justification: ../justification/multi-agent-parallel-research-pipeline.md
canonical_concept: multi-agent-parallel-research
aliases:
- parallel research agents
- research swarm
- multi-agent research
- retardmax mode
- thesis-driven research
- question research mode
summary: 'llm-wiki 实现三级并行研究模式：Standard (5 agents: Academic/Technical/Applied/News/Contrarian)、Deep (8 agents, +Historical/Adjacent/Data)、Retardmax (10 agents, +2 Rabbit Hole, 跳过规划)。支持 Question Mode（问题分解为子问题每个分配一个
  agent）和 Thesis Mode（for/against/mechanistic/meta/adjacent 分组，反确认偏差）。Phase 2b 独立信誉评分防止"狐狸守鸡舍"问题。--min-time 启用多轮研究含进度评分与反思协议。'
related:
- llm-as-knowledge-compiler-metaphor
- derived-index-concurrency-protocol
- lint-as-schema-migration
- volatility-freshness-scoring
---
llm-wiki 的研究系统实现了一个结构化的多 Agent 并行管线：

**三级模式**[^src-1]：
| 模式 | Agent 数 | 角色 |
|------|---------|------|
| Standard | 5 | Academic, Technical, Applied, News/Trends, Contrarian |
| Deep | 8 | +Historical, Adjacent fields, Data/Stats |
| Retardmax | 10 | +2 Rabbit Hole agents; 跳过规划，激进 ingest |

**输入类型自动检测**：
- Topic -> 标准研究（探索主题领域）
- Question -> 分解为 3-5 子问题，每个 agent 回答一个具体问题，产出 playbook
- Thesis -> for/against 证据框架，产出判决（supported/contradicted/mixed/insufficient）[^src-2]

**Phase 2b 信誉评分**（独立于 agent 自评）：
- 同行评审 +2，近期 +1，知名作者 +1，偏差信号 -1（不叠加），交叉佐证 +1/agent（max +2）
- 分层：High (4-6) -> Medium (2-3) -> Low (0-1) -> Reject (<0)[^src-3]

**多轮研究（--min-time）**：
- 每轮后反思：优先发现跨主题连接（据材料描述可多发现 34% 的交叉引用）
- 进度评分 0-100：sources x3 + articles x5 + cross-refs x2 + credibility x4
- 终止条件：score >= 80 且无高影响缺口，或连续两轮 < 40[^src-4]

**Thesis 反确认偏差**：Round 2 自动聚焦于 Round 1 证据的较弱一侧。[^src-5]

[^src-1]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- "README.md Research Modes" -- "Standard 5, Deep 8, Retardmax 10"
[^src-2]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- "research.md Thesis Research Mode" -- "Agents split by purpose: Supporting, Opposing, Mechanistic, Meta/Review, Adjacent"
[^src-3]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- "research-infrastructure.md Credibility Scoring" -- "Peer-reviewed +2... Tiers: High (4-6) → Medium (2-3) → Low (0-1) → Reject (<0)"
[^src-4]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- "research-infrastructure.md Progress Scoring" -- "Sources ingested count x 3... max 30... Articles created/updated count x 5"
[^src-5]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- "research.md Thesis Research Mode" -- "Round 2 focuses harder on the WEAKER side of Round 1's evidence"
