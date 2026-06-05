---
card_id: comparison-locomo-vs-longmemeval-taxonomy
decision: accepted
confidence: high
---

## 为什么值得单独成卡

LoCoMo 和 LongMemEval 各自定义了包含五个维度的记忆评测分类体系，表面上高度相似（同为五维、均含时序推理和拒答），但设计视角截然不同：LoCoMo 以问题复杂度为轴（"回答需要何种推理"），LongMemEval 以系统能力为轴（"系统需要何种功能"）。这一区分对于正确使用这两套评测框架至关重要——选用 LoCoMo 侧重诊断 QA 推理深度，选用 LongMemEval 侧重诊断系统能力完备性。

LongMemEval 论文明确批评了 LoCoMo 缺少知识更新（KU）和助手侧信息回忆两个维度，这一批评构成了两套框架之间的核心张力。将这一对比关系独立记录为 distinction 卡，有助于后续研究者在设计新基准或选择评估框架时做出知情的权衡。

## 来源依据

- LoCoMo 五类推理维度定义：`data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- Section 4.1
- LongMemEval 五项能力定义：`data/raw/arxiv/arxiv-longmemeval/source/text/3_benchmark.tex` -- Section 3.2
- LongMemEval 对 LoCoMo 的批评：`data/raw/arxiv/arxiv-longmemeval/source/text/1_introduction.tex` -- Section 1
