# Justification: ukpa-structural-impact-score

## Extraction Rationale
I_score (Eq.3) 是 UKPA 第三步的核心代理评分，在无法访问最终图的约束下估计局部结构破坏。消融验证了权重设计的合理性。

## Evidence Quality
- 公式直接引自论文 Eq.(3)
- 消融实验提供等权/单组分/编辑距离对比
- 默认权重 (0.25, 0.25, 0.5) 有实验优化依据

## Hedge Assessment
"favors candidates that cause larger perturbations" 为设计意图描述，非推测。
