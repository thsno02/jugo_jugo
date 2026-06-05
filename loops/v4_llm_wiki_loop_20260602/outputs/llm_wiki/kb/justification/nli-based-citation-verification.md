---
schema: justification_journal.v1
card: ../cards/nli-based-citation-verification.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/arxiv/arxiv-alce/agent_source_bundle.txt`
源证据：
- sections/evaluation.tex -- "We use the NLI model TRUE again to automatically examine whether the cited passages entail the model generation."
- sections/evaluation.tex -- citation recall/precision formal definitions
- sections/human_eval.tex -- "Cohen's kappa coefficient...substantial agreement for citation recall (0.698) and moderate agreement for citation precision (0.525)"
- sections/appendix.tex -- "For citation recall, ALCE achieves an accuracy of 85.1%; for citation precision, ALCE has an accuracy of 77.6%."
范围论证：NLI 驱动的引用验证机制是 ALCE 的核心技术贡献，包含 recall/precision 的形式化定义、AIS 框架对齐、及人工验证数据。作为独立机制值得单独成卡。
