# Justification: longmemeval-five-memory-abilities

## 为什么产出此卡
五类记忆能力是 LongMemEval 的核心分类框架，独立于基准的整体定位，值得原子化记录。每种能力有明确的评测语义和 question_type 映射。

## 证据充分性
README Overview 节列出五类能力名称；Dataset Format 节给出 question_type 枚举值及其映射；Custom History 节的任务名映射表提供内部名→官方名对应；Retrieval 节补充了 abstention 的 30 条实例和评测跳过逻辑。

## evidence_basis 选择
`code_implementation` — 五类能力通过 question_type 字段在数据集中实现，评测代码据此分类统计。
