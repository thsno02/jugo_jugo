# Justification: collection-ingestion-adapter-system

## 抽卡理由
集合 ingest 适配器系统解决了"如何批量导入有界上游语料库"的问题——5 种适配器覆盖 Git 仓库、MediaWiki dump/API、消息归档、Wayback 存档快照。核心原则是"从不递归爬取 HTML"。

## 证据强度
- ingest-collection.md 完整命令规格
- ingestion.md Collection Ingestion 段定义适配器
- AGENTS.md 描述适配器表格
- README Quick Start 展示用法
- evidence_basis: code_implementation

## 原子性检验
单一核心 idea：结构化适配器模式 + manifest + child sources + 选择性编译。
