# Justification: ragchecker-generator-diagnostic-metrics

## 为什么产出此卡
Generator metrics 包含六个独立维度的诊断指标，构成一个完整的生成器质量评估子体系。与 overall metrics 和 retriever metrics 不同，generator metrics 的复杂度和诊断粒度值得单独成卡。

## Evidence basis 选择: code_implementation
六个指标的名称和示例数值均来自 CLI 和 Python API 的实际输出结果（两组不同数值），属于代码实现的直接产物。

## 提取判断
- 六个指标在两处代码输出中均完整列出（CLI 和 Python 示例）
- noise_sensitivity 区分 relevant/irrelevant 的设计选择从字段命名可直接观察
- hallucination 与 self_knowledge 的关系为基于字段语义的合理推断（已加 hedge "似乎表明"）
