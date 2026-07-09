# Justification: opinionated-inventory-dataset-layers

## 抽卡理由
Inventory 和 Datasets 层的"有态度"设计（opinionated fit check + lazy initialization）是 llm-wiki 对"什么值得跟踪"问题的独特回答。两层共享相同的设计哲学但服务不同用途，合并成卡因为核心原则统一。

## 证据强度
- inventory.md 完整参考（Fit Check 段）
- datasets.md 完整参考（Boundary 段）
- AGENTS.md Operations 段描述适配性边界
- 多个 command spec 包含 "Inventory awareness" 段
- evidence_basis: code_implementation

## 原子性检验
核心 idea：有态度的惰性可选层 + 适配性声明 + dry-run-first 迁移。两层虽然功能不同，但共享完全相同的设计哲学（惰性、有态度、显式迁移），合并表达更有信息密度。
