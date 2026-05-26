---
schema: draft_card_provenance.v3
draft_card: ../cards/wicer-llm-judge-human-validation.md
material_id: arxiv-wicer
digest_id: digest_arxiv-wicer
source_paths:
  - data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt
created_time: 2026-05-26T15:00:00+08:00
edited_time: 2026-05-26T15:00:00+08:00
edited_entity: llm
---

## 源证据

### §F 开篇与方法（第 1446–1453 行）

> "To validate the LLM-as-judge scores, a domain expert independently rated a stratified sample of 100 question–answer pairs spanning all five conditions (FC raw, RAG, Wiki blind, WiCER iter 1, WiCER iter 2) using the same 1–5 rubric."

### Table tab:human_corr（第 1454–1473 行）

```
Pearson r           : 0.940
Spearman ρ          : 0.928 (p < 10^-43)
Kendall τ           : 0.873 (p < 10^-25)
Exact agreement     : 75/100 (75.0%)
Within 1 point      : 99/100 (99.0%)
Mean absolute error : 0.26
Bias (LLM − Human)  : +0.06
```

### Table tab:human_cond per-condition（第 1480–1495 行）

```
FC raw       n=30  LLM 3.50  Human 3.50  r=0.890  Exact 16/30
RAG          n=30  LLM 3.40  Human 3.23  r=0.912  Exact 24/30
Wiki blind   n=31  LLM 2.26  Human 2.19  r=0.975  Exact 27/31
WiCER iter 1 n=6   LLM 2.00  Human 2.17  r=0.937  Exact 5/6
WiCER iter 2 n=3   LLM 3.00  Human 3.00  r=1.000  Exact 3/3
```

### 唯一 >1 分歧 case（第 1497–1502 行）

> "The single sample with >1 point disagreement was a RAG response scored 4 by the judge and 2 by the human rater; manual inspection confirmed the response omitted a key detail that the human considered essential. Overall, these results confirm that the Claude Sonnet LLM-as-judge provides a reliable proxy for human quality assessment in this setting."

### NeurIPS checklist statistical significance（第 97–101 行）

> "We report means, standard deviations, and ranges across topics ... but do not report confidence intervals or significance tests for individual topic comparisons. Each topic's result is deterministic (greedy decoding, T=0), so within-topic variance is zero ... repeated runs with different QA splits or stochastic decoding would strengthen the claims."

## 卡片范围是否成立

本卡的范围限制在 Appendix F 的 LLM-as-judge 人评校准。是论文中**唯一**专门为 judge 可靠性做的独立验证，自然成为一张方法学卡片。

- 数字（r=0.94, 75%, 99%, MAE 0.26, bias +0.06）—— 直接来自 Table tab:human_corr。
- 跨条件稳定性—— 直接来自 Table tab:human_cond + 论文一句话总结。
- 唯一 >1 分歧 case—— 直接 verbatim。
- "与 statistical significance limitation 的张力"—— 是把 §F 与 NeurIPS checklist 第 7 项放到一起读得到的合成观察，论文未显式联接二者；属合理引申。

## 发表门控结果

本轮未运行。

## 备注

- 与 ARES 三判官评估卡（`ares-three-judge-rag-evaluation` 等）有方法学层面的呼应：ARES 用 fine-tuned DeBERTa + PPI，WiCER 用 Claude Sonnet zero-shot；都以"少量人评校准"为关键。可在 wiki 内做交叉引用，但**不重叠**——两张卡讲不同系统。
- 本卡数字对未来"什么时候 LLM-as-judge 够用"的判断有参考价值，应作为 methodology 类卡片归档。
