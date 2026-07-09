# Justification: llmwiki-epistemic-metadata

## 提取依据

"Page metadata" 和 "Claim-level provenance" 两个章节详细描述了认识论元数据的三个字段、多源合并协调规则、段落/行级溯源标记格式、以及 lint 校验规则。

## 原子性判断

将页面级元数据（confidence/provenanceState/contradictedBy）与声明级溯源（^[source.md:L-L]）合为一卡，因两者共同构成 llmwiki 的"可信度/溯源"子系统，拆分会失去语义完整性。

## Evidence basis 选择

选 `code_implementation`：metadata 字段和 lint 规则均为已实现功能（0.3.0+ 版本 shipped）。

## Hedge 审查

源材料对元数据功能使用确定性描述（"can carry", "are reconciled"），无推测性语言需保留。
