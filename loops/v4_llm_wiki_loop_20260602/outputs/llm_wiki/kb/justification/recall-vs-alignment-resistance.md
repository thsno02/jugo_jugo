---
schema: justification_journal.v1
card: ../cards/recall-vs-alignment-resistance.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt`
源证据：
- Appendix: Long Context Recall -- "To diagnose whether a model's immunity to prompt injection stems from inability to recall... versus refusal to follow it (safety alignment)"
- Appendix: Interpretation -- "GPT-OSS-120B (6.7% recall): The extremely low recall rate indicates a severe needle-in-haystack failure."
- Appendix: Interpretation -- "a low ASR_B combined with low recall suggests the defense is incidental... while low ASR_B with high recall suggests intentional resistance"
范围论证：这是一个方法论层面的重要区分——偶然性防御 vs 有意性防御——独立于具体的攻击和模型。该区分对正确评价模型安全性至关重要，且可推广到其他注入攻击的评估场景。
