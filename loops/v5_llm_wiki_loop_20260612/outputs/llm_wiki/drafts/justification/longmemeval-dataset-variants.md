# Justification: longmemeval-dataset-variants

## 为什么产出此卡
三种数据集变体是独立原子概念: 各有不同规模、设计意图和适用场景。与基准概览和能力分类是正交维度。

## 证据充分性
README Dataset Format 节明确给出三种文件的 token 数、session 数；Long-Context Generation 节说明 M 不适合 full-history；Custom History 节描述可扩展机制。均为直接陈述。

## evidence_basis 选择
`code_implementation` — 三种变体已作为数据文件在 HuggingFace 上发布，README 中给出下载命令。
