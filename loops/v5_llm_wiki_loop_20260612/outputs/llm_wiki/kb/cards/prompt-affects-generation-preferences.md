---
id: prompt-affects-generation-preferences
title: 显式 Prompt 要求影响生成器三难困境
status: accepted
card_type: experimental-finding
tags:
- prompt-engineering
- faithfulness
- context-utilization
- noise-sensitivity
- trilemma
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-ragchecker
evidence_basis: experimental_paper
justification: ../justification/prompt-affects-generation-preferences.md
canonical_concept: prompt-affects-generation-preferences
aliases:
- Explicit Requirements in Prompts Affect Generation Preferences
- prompt 影响生成偏好
- generation trilemma
summary: RAGChecker 诊断实验表明在 generation prompt 中添加显式要求（要求更高 faithfulness 和 context utilization、更低 noise sensitivity）会产生复杂效果：context utilization 改善（59.2→63.7），faithfulness 提升（92.2→93.6），但 noise sensitivity
  也上升（35.4→38.1），体现 context utilization、noise sensitivity 和 faithfulness 三者之间的微妙张力（trilemma）。GPT-4 响应 prompt 优化更显著，而 Llama3 因已有高 faithfulness 而变化不大。
related:
- ragchecker-generator-metrics
- more-context-enhances-faithfulness
- open-source-blind-trust-context
---

RAGChecker 诊断实验探索了优化 generation prompt（添加 faithfulness、context utilization、低 noise sensitivity 的显式要求）对 generator 行为的影响。[^src-1]

**效果**（优化 prompt vs 基础 prompt，平均值）：[^src-2]
- Context Utilization: 59.2 → 63.7（改善）
- Faithfulness: 92.2 → 93.6（改善）
- Noise Sensitivity: 35.4 → 38.1（恶化）
- F1: 小幅改善（GPT-4 显著，Llama3 变化可忽略）

**生成器三难困境（trilemma）**：context utilization、noise sensitivity 和 faithfulness 之间存在微妙张力。当 prompt 要求 generator 更充分利用上下文时，不可避免地也会更多利用其中的噪声。同时满足所有 prompt 要求是困难的。[^src-1]

**Generator 差异**：[^src-3]
- GPT-4 对优化 prompt 响应明显：faithfulness 相关指标改善，F1 稳步提升
- Llama3 变化甚微——与其已有的高 faithfulness 基线一致（无进一步提升空间）

**建议**：RAG 开发者应基于目标偏好和 generator 自身能力，在三个维度间做出优先级选择。[^src-1]

[^src-1]: `data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "sections/experiments.tex Diagnosis" -- "Explicit Requirements in Prompts Affect Generation Preferences...generators show improvements in faithfulness (92.2→93.6), but struggle with the subtle tension between context utilization (59.2→63.7) and noise sensitivity (35.4→38.1)"
[^src-2]: `data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "sections/appendix_diagnosis.tex" -- "we observed a general improvement in context utilization. However, as a counterpart to context utilization, noise sensitivity generally worsened"
[^src-3]: `data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "sections/appendix_diagnosis.tex" -- "GPT-4 generally showes improvements in metrics related to faithfulness...whereas Llama3 does not exhibit the same behavior"

[^card-11]: 参见 [open-source-blind-trust-context] 了解为何 Llama3 的 faithfulness 已处高位
