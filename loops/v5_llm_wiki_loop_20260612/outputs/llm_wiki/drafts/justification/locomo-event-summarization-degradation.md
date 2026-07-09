# Justification: locomo-event-summarization-degradation

## 抽取理由
论文在 Table 5 (summ_results) 中明确展示了长上下文模型 GPT-3.5-turbo-16K 在事件摘要任务中 FactScore F1 (39.9) 低于 base GPT-3.5-turbo (45.9) 的数据，并在正文中直接分析了原因。这是一个与"长上下文自动=更好理解"的直觉相悖的重要实验发现，具有独立的知识价值。

## 原子性检验
该卡聚焦于"事件摘要任务中长上下文模型退化"这一单一发现，不包含错误分类（单独成卡）或 QA 任务表现（已有卡覆盖）。

## 来源锚定
- Table summ_results 提供完整定量数据
- Section 6.2 Event Summarization Results 提供解释性分析
