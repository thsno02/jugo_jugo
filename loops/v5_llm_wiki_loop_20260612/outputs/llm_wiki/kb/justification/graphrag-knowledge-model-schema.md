# Justification: graphrag-knowledge-model-schema

## 提取依据
材料 docs/index/outputs.md 完整列出了所有 7 种输出表的字段 schema，包括类型和描述。docs/index/default_dataflow.md 和 docs/index/architecture.md 描述了 Knowledge Model 的抽象层角色。

## 原子性判断
Knowledge Model Schema 是一个统一的数据模型规范。虽涉及多张表，但它们共同构成一个自洽的知识表示 schema，是 GraphRAG 的核心数据契约，适合作为单卡记录。

## Evidence basis
code_implementation -- 这些 schema 对应实际的 Parquet 输出文件和 Python model 类定义。
