# Justification: locomo-summarization-error-taxonomy

## 抽取理由
论文通过人工分析 GPT-3.5-turbo 预测摘要，归纳出五类错误模式并在 Table summary_errors 中给出具体示例。这一分类法对理解 LLM 在对话摘要场景的失败模式具有实操价值，尤其"dialog cues misunderstanding"是对话场景特有的错误类型。

## 原子性检验
该卡是一个完整的错误分类法（taxonomy），与"事件摘要退化"卡互补——后者报告现象，本卡解释具体机制。五类错误内聚为一个分类体系，不宜拆分。

## 来源锚定
- Section 6.2 段落"we identify five broad categories of event summarization errors"
- Table summary_errors (Appendix) 提供每类错误的具体示例
