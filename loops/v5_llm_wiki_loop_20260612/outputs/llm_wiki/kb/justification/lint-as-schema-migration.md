# Justification: lint-as-schema-migration

## 抽卡理由
"Lint is the migration"是 llm-wiki 最具特色的设计原则之一，明确拒绝独立迁移命令，将模式演化编码为 lint 规则。这是一个在 LLM 驱动系统中独特的 schema evolution 策略。

## 证据强度
- linting.md 开头 Development Note 用粗体声明原则
- 完整的演化操作规范（重命名目录/字段/枚举时的具体步骤）
- C11/C12/C13 规则实现该原则
- CLAUDE.md "When to update tests" 段进一步强化
- evidence_basis: code_implementation

## 原子性检验
单一核心 idea：schema evolution 通过 lint 规则编码，无独立迁移命令。幂等修复、旧版本与用户错误同等对待是该原则的直接推论。
