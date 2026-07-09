---
id: wicer-algorithm
title: WiCER 迭代编译算法
status: draft
card_type: 算法方法
tags: [knowledge-compilation, iterative-refinement, cegar, fact-pinning]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-wicer]
evidence_basis: experimental_paper
justification: ../justification/wicer-algorithm.md
canonical_concept: wicer-algorithm
aliases: [WiCER, Wiki-memory Compile Evaluate Refine, WiCER algorithm, compile-evaluate-refine loop]
summary: >-
  WiCER (Wiki-memory Compile, Evaluate, Refine) 是受 CEGAR 范式启发的迭代知识编译算法。流程: 盲编译->诊断探针评估->识别 score-1 失败->从源文档提取丢失事实(~50-100词/失败)->累积 pinning 约束->带约束重编译。1-2 次迭代恢复盲编译丢失质量的 80%(3.24 vs 3.47 FC raw, 15 topics), 灾难性失败降 55%。单调性保证: 已 pinned 事实不可再丢失。
related: []
---

WiCER（Wiki-memory Compile, Evaluate, Refine）是一种迭代知识编译算法，通过 QA 反馈识别编译过程中丢失的事实，并在后续迭代中强制保留。[^src-1]

**算法流程**：
1. **探针选择**：每个源文档选取一个 QA 对作为诊断探针
2. **盲编译**：将文档集 D 按目标比率 r 编译为初始 wiki W_0
3. **迭代循环**（直至收敛或达最大迭代数 T）：
   - **评估**：对每个探针，从当前 wiki 生成回答并用 LLM judge 评分
   - **失败识别**：收集所有 score<=1 的探针
   - **诊断**：对每个失败探针，从其源文档提取关键事实（约 50-100 词/失败，vs 约 700 词/源文档）
   - **约束累积**：将诊断出的事实加入累积保留集 F_cumulative
   - **受约束重编译**：W_{t+1} = Compile(D, r, preserve=F_cumulative)
4. **收敛条件**：无失败，或改进 <10%

**设计原理——CEGAR 映射**：
- 具体系统 M = 完整文档集 D
- 抽象模型 = 编译 wiki W_t
- 规范 = "所有探针评分 >1"
- 反例 = score-1 探针
- 精化 = 添加 pinning 约束并重编译

**单调性保证**：已 pinned 的事实通过显式约束不可再丢失，因此在已 pinned 事实子集上失败集单调缩减。[^src-2]

[^src-1]: `data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt` -- "WiCER / Algorithm" P775-801 -- Algorithm 1 WiCER
[^src-2]: `data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt` -- "CEGAR-WiCER Mapping / Monotonicity Guarantee" P1388-1406 -- "once a fact is pinned, it cannot be lost again"

[^card-2]: 解决 [[compilation-gap]] 的核心方案
[^card-3]: 受 [[cegar-paradigm-in-wicer]] 启发
