## Justification for long-context-adversarial-hallucination

**Why this card**: 这是论文最重要的实验发现之一——长上下文并不总是有益，在对抗性场景下反而导致灾难性的幻觉加剧。此现象对 LLM 部署有直接启示意义。

**Evidence quality**: 定量数据来自 Table 3（QA results），性能下降趋势清晰（4K→8K→12K→16K monotonically decreasing adversarial F1）。论文结论措辞审慎，使用 "can be easily misled" 而非绝对断言。

**Atomic check**: 本卡片聚焦长上下文 + adversarial 这一特定交互效应，不涉及 RAG 或其他解决方案。
