# Justification: ukpa-graph-fragmentation-results

## Extraction Rationale
UKPA 的图结构破坏和 QA 精度下降是其核心效果的定量证据。Node/Edge Retention Rate 和 Jaccard 指标揭示了拓扑重写而非简单信息删除的攻击特征。

## Evidence Quality
- 数据来自论文 Table 2 和 Table 3
- 在 MS-GraphRAG 和 LightRAG 两个系统上测试显示泛化能力
- Edge Jaccard 低至 0.0789 是强有力的结构破坏证据

## Hedge Assessment
实验数据为确定性报告。
