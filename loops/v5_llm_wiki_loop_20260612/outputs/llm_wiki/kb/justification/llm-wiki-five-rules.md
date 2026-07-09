# Justification: llm-wiki-five-rules

## 为什么产出此卡
五条规则在材料中以编号列表明确列出，构成系统的操作纪律。虽有五点，但它们作为一个 principle-set 形成完整约束体系，拆分则失去互补关系语义。

## 证据强度
- 材料原文逐条列出，措辞明确（"mandatory", "every single one"）
- 第 3 条给出量化阈值（~100 docs / ~80k tokens）
- evidence_basis 取 code_implementation：仓库提供 wiki_size_report.py 实现规则 3 的检测

## 边界决策
- 作为整体保留而非拆 5 张卡：规则间呈递进关系且共同约束同一系统
- 与编译范式分离：范式是"是什么"，规则是"怎么做"
- 与三层架构分离：架构是"结构"，规则是"行为约束"
