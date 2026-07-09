# Justification: graphrag-defense-evasion

## Extraction Rationale
防御规避是衡量攻击实际威胁程度的关键证据。三种 SOTA 防御的近零 F1 值揭示了当前安全工具的盲区。

## Evidence Quality
- 数据来自论文 Table 4
- 覆盖三种代表性防御（PPL filter、LLM detector、Semantic Closeness）
- 失败原因有合理的理论分析

## Hedge Assessment
"largely ineffective" 有 F1<0.13 数据支撑，非夸大。
