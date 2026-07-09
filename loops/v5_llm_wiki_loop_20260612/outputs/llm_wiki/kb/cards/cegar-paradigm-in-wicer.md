---
id: cegar-paradigm-in-wicer
title: CEGAR 范式在知识编译中的应用
status: accepted
card_type: 理论映射
tags:
- cegar
- abstraction-refinement
- formal-methods
- knowledge-compilation
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-wicer
evidence_basis: experimental_paper
justification: ../justification/cegar-paradigm-in-wicer.md
canonical_concept: cegar-paradigm-in-wicer
aliases:
- CEGAR
- Counterexample-Guided Abstraction Refinement
- CEGAR-WiCER mapping
- 反例引导抽象精化
summary: 'WiCER 将 CEGAR (Clarke et al. 2000) 范式从形式验证迁移到知识编译: 具体系统=文档集D, 抽象模型=编译wiki
  W_t, 抽象映射=LLM编译器(有损压缩), 规范="所有探针>1分", 反例=score-1探针, 伪反例验证=诊断确认事实存在于D但丢失于W_t, 精化=添加pinning约束重编译。映射成立但三点分歧:
  随机编译器(非确定性), 近似验证(LLM judge非精确), 随机知识置换(精化可引入新反例)。'
related:
- wicer-algorithm
- random-knowledge-displacement
- compilation-gap
---

WiCER 将反例引导抽象精化（CEGAR, Clarke et al. 2000）范式从形式验证领域迁移到 LLM 知识编译设定中。[^src-1]

**形式映射**：

| CEGAR | WiCER |
|-------|-------|
| 具体系统 M | 完整文档集 D |
| 抽象模型 M-hat | 编译 wiki W_t |
| 抽象映射 h | LLM 编译器（有损压缩）|
| 规范 phi | "所有探针评分 >1" |
| 反例 | Score-1 失败探针 |
| 伪反例验证 | 诊断：事实存在于 D 但丢失于 W_t |
| 精化（分裂状态）| 添加 pinning 约束，重编译 W_{t+1} |

**单调性保证**：在已 pinned 事实子集上，失败集单调缩减。形式化为：F_t intersect {q : facts(q) subset P_t} supseteq F_{t+1} intersect {q : facts(q) subset P_t}。[^src-2]

**映射的三个限制**：
1. **随机编译器**：CEGAR 精化确定性抽象函数；WiCER 的 LLM 编译器输出非确定性
2. **近似验证**：CEGAR 精确模型检查；WiCER 使用 LLM-as-judge 近似评估
3. **随机知识置换**：CEGAR 中精化不引入新反例；WiCER 中 pinning 可能置换内容造成新失败[^src-3]

因此 WiCER 的收敛是经验性的（empirical）而非形式化的（formal）。

[^src-1]: `data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt` -- "WiCER / Design Rationale" P804-821 -- "WiCER instantiates the CEGAR paradigm"
[^src-2]: `data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt` -- "CEGAR-WiCER Mapping / Monotonicity" P1392-1406 -- monotonicity formula
[^src-3]: `data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt` -- "CEGAR-WiCER Mapping / Limitations" P1409-1443 -- three differences

[^card-7]: 为 [[wicer-algorithm]] 提供理论基础
[^card-8]: [[random-knowledge-displacement]] 打破 CEGAR 的精化无副作用假设
