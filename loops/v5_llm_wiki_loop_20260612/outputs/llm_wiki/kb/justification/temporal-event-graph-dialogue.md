## Justification for temporal-event-graph-dialogue

**Why this card**: Temporal event graph 是 LoCoMo 管线的方法论创新——将 persona-grounded 因果事件链作为对话的底层支架，同时兼作评估 ground truth。这是独立于数据集本身的方法概念。

**Evidence quality**: 论文 Section 3.2 详细描述构建流程和参数（k=3, 25 events, 6-12 months），附录 Figure 给出 prompt 和示例，并在 Section 4.2 将其作为 event summarization 的 gold standard。

**Atomic check**: 本卡片聚焦事件图的构建方法和在对话生成中的作用机制，不涉及评估结果。
