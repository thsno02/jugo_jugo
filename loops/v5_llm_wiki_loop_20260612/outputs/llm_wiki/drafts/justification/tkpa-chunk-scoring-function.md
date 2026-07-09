# Justification: tkpa-chunk-scoring-function

## Extraction Rationale
Chunk Scoring Function (Eq.2) 是 TKPA 第三步的核心，决定哪些 chunk 被优先重写。消融实验提供了各组分贡献的定量分析。

## Evidence Quality
- 公式和权重直接引自论文
- 消融实验提供定量支撑（包含等权、单组分、top-k 变化）
- 默认权重 (0.5, 0.3, 0.2) 有实验验证

## Hedge Assessment
实验结果为确定性报告。
