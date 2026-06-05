---
id: dynamic-agentic-roi
title: 动态 Agentic ROI 模型
status: accepted
card_type: mechanism
tags: [agentic-roi, dynamic-model, cost-function, coverage-rate, H(t)]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-knowledge-compounding]
justification: ../justification/dynamic-agentic-roi.md
canonical_concept: dynamic-agentic-roi
aliases: [动态Agentic ROI, dynamic Agentic ROI, 时变成本模型, H(t)覆盖率模型]
summary: >-
  dynamic-agentic-roi（动态Agentic ROI / 时变成本模型 / H(t)覆盖率模型）将 Agentic ROI 的成本项
  从静态常量推广为 Ci = (1-Hi)*C_generate + Hi*C_retrieve + C_writeback，其中知识库覆盖率 H(t)
  遵循凹饱和递推方程 H(i+1) = Hi + alpha*(1-Hi)*pi
related:
  - knowledge-compounding
  - cost-independence-assumption
---

Wen & Ku (2026) 提出的动态 Agentic ROI 模型将原始 Agentic ROI 公式中的静态成本项推广为时变函数，由两个核心公式构成。

**修正成本函数**[^src-1]：

Ci = (1 - Hi) * C_generate,i + Hi * C_retrieve,i + C_writeback,i

其中：
- **Hi** 属于 [0, 1]，是知识库覆盖率——任务 i 所需信息中可由现有知识库直接满足的比例
- **C_generate,i** 是完全通过实时推理回答的成本（无状态基线的成本）
- **C_retrieve,i** 是从结构化知识库读取已有答案的成本
- **C_writeback,i** 是更新知识库的一次性成本（新实体创建、综合写作、搜索回写）

当 Hi 随 i 单调递增时，每查询支出 Ci 向下界 C_retrieve 单调递减——这是知识复利效应在运营成本边际上的数学本质[^src-2]。

**覆盖率演化方程**[^src-3]：

H(i+1) = Hi + alpha * (1 - Hi) * pi

其中：
- **alpha** 属于 (0, 1) 是每任务耕作率（cultivation rate），取决于 wiki 专家的 INGEST/回写质量
- **pi** 属于 [0, 1] 是第 i 个任务落在历史已覆盖区域之外的概率（取决于用户查询流的主题集中度）

解析求解表明 H(t) 呈**凹饱和曲线**：初期快速增长，后期缓慢增长，渐近趋近于主题分布的稳态覆盖[^src-4]。实验参数标定为 H0 = 0.05, alpha = 0.18[^src-5]。

Hi 具有**马尔可夫性质**：其当前值取决于历史任务对知识库的贡献[^src-6]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-knowledge-compounding/source.pdf` -- Section 3.2 P8 -- "Cᵢ = (1 − Hᵢ) · C_generate,ᵢ + Hᵢ · C_retrieve,ᵢ + C_writeback,ᵢ"
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-knowledge-compounding/source.pdf` -- Section 3.2 P8 -- "When Hᵢ grows monotonically with i, the per-query expenditure Cᵢ decreases monotonically with i toward the floor C_retrieve—this is the mathematical essence of the knowledge compounding effect on the operating-cost margin"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-knowledge-compounding/source.pdf` -- Section 3.3 P8 -- "Hᵢ₊₁ = Hᵢ + α · (1 − Hᵢ) · pᵢ"
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-knowledge-compounding/source.pdf` -- Section 3.3 P9 -- "H(t) takes a concave saturation curve: rapid early growth, slow late growth, asymptotically approaching the steady-state coverage of the topic distribution"
[^src-5]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-knowledge-compounding/source.pdf` -- Section 5.3 P18 -- "H(t) evolves according to the equation in Section 3.3 with H₀ = 0.05 and α = 0.18"
[^src-6]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-knowledge-compounding/source.pdf` -- Section 3.2 P8 -- "Hᵢ is a time-varying random variable possessing a Markov property: its current value depends on the contributions of historical tasks to the knowledge base"
