# Justification: longmemeval-retrieval-augmentation

## 为什么产出此卡
检索增强策略（基线、index expansion、time-aware expansion）是 LongMemEval 区别于纯 long-context 评测的核心方法贡献，构成独立原子概念。

## 证据充分性
README Memory Retrieval 节详述了四种检索器、五种 expansion type、三种 join mode 及 time-aware pruning 机制，均有对应命令行参数和说明。

## evidence_basis 选择
`code_implementation` — 所有策略均有对应代码实现（src/retrieval/、src/index_expansion/），且提供了预生成的 expansion 输出下载链接。
