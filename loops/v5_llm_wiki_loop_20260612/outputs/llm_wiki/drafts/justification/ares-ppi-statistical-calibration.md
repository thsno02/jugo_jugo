# Justification: ares-ppi-statistical-calibration

## 为什么产出此卡
PPI 是 ARES 区别于简单 LLM-as-judge 方法的核心技术创新点，材料中独立强调了其统计置信度输出和最低标注量要求。作为独立机制概念值得单独成卡。

## Evidence basis 选择
选择 `code_implementation`：Quick Start 代码示例展示了 PPI 的具体配置参数（gold_label_path、evaluation_datasets）和输出格式（Prediction、Confidence Interval、Annotated Examples used for PPI: 300），属于代码实现层面的证据。

## 关键数字
- 最低人工标注：50 条
- 理想标注量：数百条
- 示例中使用 300 条标注
- 输出置信区间示例：[0.547, 0.664]
- LLM Judge 在 ground truth 上准确率：0.789
