# Justification: lint-as-quality-driver

## Extraction rationale
Lint 是三大操作之一，且有独特的双重角色（修复 + 发现驱动）。检查项目清单是具体可操作的知识。

## Evidence quality
- 检查项有明确列表
- "good at suggesting" 暗示基于实践经验的观察而非理论推演
- 无 hedge

## Atomicity check
仅覆盖 lint 操作的定义、检查项和驱动性角色。与 ingest/query 操作分别成卡。
