---
id: cost-independence-assumption
title: Agentic ROI 成本独立性假设批判
status: accepted
card_type: distinction
tags: [agentic-roi, assumption, cost-independence, rag, persistent-knowledge]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-knowledge-compounding]
justification: ../justification/cost-independence-assumption.md
canonical_concept: cost-independence-assumption
aliases: [成本独立性假设, cost independence assumption, A1假设, 时间无关假设]
summary: >-
  cost-independence-assumption（成本独立性假设 / A1假设 / 时间无关假设）指 Liu et al. (2026)
  Agentic ROI 公式中隐含的三个未经检验的假设（成本/质量/时间独立性），
  在传统 RAG 范式下大体成立但引入持久化知识层后全部失效
related: [compounding-cost-honesty, knowledge-compounding]
  - knowledge-compounding
  - dynamic-agentic-roi
---

Wen & Ku (2026) 指出 Liu et al. (2026) 的 Agentic ROI 公式 ROIi = (Delta-Qi x Delta-Ti) / Ci 中包含三个**隐含的未经检验的假设**[^src-1]：

**假设 A1（成本独立性）**：任务 i 的成本 Ci 仅由当前任务的复杂度决定，与历史任务集 {1, 2, ..., i-1} 无关[^src-2]。

**假设 A2（质量独立性）**：Q_Agent,i 仅由当前任务输入和模型能力决定，不受先前任务影响。

**假设 A3（时间独立性）**：T_Agent,i 仅取决于当前交互的复杂度，不从该用户或领域的系统级历史经验中获益。

这三个假设在**传统 RAG 范式下大体成立**——系统没有记忆：每次查询重新检索原始文档、重新组装上下文、从头生成答案[^src-3]。

然而，**一旦引入持久化结构化知识层，三个假设全部失效**。本文聚焦于修正 A1；A2 和 A3 的修正留待后续工作[^src-4]。

这一批判的意义在于揭示了现有 LLM 经济学框架（包括 Liu et al. 的 Agentic ROI 和 NVIDIA 的 token 经济学叙事）的共同盲区：**两个框架都将成本视为独立的、非累积的边际费用**，在每次新交互中重复发生[^src-5]。

假设失效后的替代理论——知识复利效应——在知识复利卡中有完整建构[^card-knowledge-compounding]。然而即使在修正后的框架中，Compounding 的原始 token 成本仍高于 Chunk-RAG，这一实证事实在成本诚实卡中有详细记录[^card-compounding-cost-honesty]。

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-knowledge-compounding/source.pdf` -- Section 3.1 P7 -- "This formulation contains three implicit assumptions that have not been examined"
[^src-2]: `data/raw/arxiv/arxiv-knowledge-compounding/source.pdf` -- Section 3.1 P7 -- "Assumption A1 (cost independence): Cᵢ is determined solely by the complexity of the current task i and is independent of the historical task set {1, 2, ..., i−1}"
[^src-3]: `data/raw/arxiv/arxiv-knowledge-compounding/source.pdf` -- Section 3.1 P7 -- "These assumptions broadly hold in the traditional RAG paradigm, where the system has no memory: each query re-retrieves raw documents, re-assembles context, and re-generates the answer from scratch"
[^src-4]: `data/raw/arxiv/arxiv-knowledge-compounding/source.pdf` -- Section 3.1 P7 -- "once a persistent structured knowledge layer is introduced, all three assumptions break down. The remainder of this section focuses on revising A1; A2 and A3 follow analogously and are left to future work"
[^src-5]: `data/raw/arxiv/arxiv-knowledge-compounding/source.pdf` -- Section 1.1 P3 -- "Both frameworks treat cost as an independent, non-cumulative marginal expense that recurs with each new interaction"
[^card-knowledge-compounding]: [知识复利效应](knowledge-compounding.md) -- 本卡批判原框架的成本独立性假设，该卡在此基础上构建了知识复利的完整经济学理论
[^card-compounding-cost-honesty]: [复利方案在原始 token 成本上从不胜出](compounding-cost-honesty.md) -- 本卡指出成本独立性假设失效，该卡的实证数据表明即使在修正后的框架中 Compounding 的原始 token 成本仍高于 Chunk-RAG
