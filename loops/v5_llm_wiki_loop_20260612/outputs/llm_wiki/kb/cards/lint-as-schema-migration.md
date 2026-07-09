---
id: lint-as-schema-migration
title: Lint 即迁移——无版本迁移命令的模式演化策略
status: accepted
card_type: design-principle
tags:
- llm-wiki
- lint
- schema-evolution
- migration
- idempotent-repair
- canonical-placement
created_time: 2026-06-12 18:00:00+08:00
edited_time: 2026-06-12 18:00:00+08:00
edited_entity: llm
source_ids:
- repo-nvk-llm-wiki
evidence_basis: code_implementation
justification: ../justification/lint-as-schema-migration.md
canonical_concept: lint-as-schema-migration
aliases:
- lint is the migration
- schema evolution via lint
- C11 canonical placement
- C13 frontmatter aliases
- no migrate command
summary: llm-wiki 明确拒绝独立的 /wiki:migrate 命令。模式演化通过 lint 规则编码：重命名目录更新放置映射（C11）；重命名字段追加别名表（C13）；改变枚举值追加值别名。"旧版本放错位置的文件"和"用户误放的文件"被视为同一缺陷，lint --fix 幂等修复两者。机械层（C11/C12/C13）全自动修复；编辑层（C8/C9 项目分组）从不自动修复。
related:
- derived-index-concurrency-protocol
- hub-topic-wiki-isolation
- multi-agent-parallel-research-pipeline
- opinionated-inventory-dataset-layers
- topic-archive-lifecycle
- volatility-freshness-scoring
---
llm-wiki 的模式演化策略可总结为一个原则："Lint is the migration"——不存在也不应存在 `/wiki:migrate` 命令。[^src-1]

**核心机制**：
- **C11 规范放置**：文件的正确路径是其 frontmatter 的纯函数（raw type -> raw/<type>/; wiki category -> wiki/<category>/; type: thesis -> wiki/theses/）。错放即结构缺陷，无论原因是用户错误还是旧版本布局
- **C13 Frontmatter 别名**：当字段重命名时，追加别名表条目（旧 -> 新）。永不删除旧别名。枚举值变更同理
- **C12 未知文件隔离**：不在允许列表中的文件被标记并可移至 `inbox/.unknown/`

**两层设计**[^src-2]：
1. **机械层**（C11/C12/C13）：原始源和 wiki 文章的放置与 frontmatter 模式。完全自动修复——规范位置和字段形状是 frontmatter 的纯函数
2. **编辑层**（C8/C9）：output/projects/ 下的项目分组。从不自动修复——"这些文件属于一起"需要人类判断

**演化操作规范**：
- 重命名了 raw/ 或 wiki/ 目录？-> 更新 C11 放置映射 + C12 允许列表
- 重命名了 frontmatter 字段？-> 追加 C13 别名表条目
- 改变了枚举值？-> 追加 C13 值别名
- 新增必需字段？-> 加入 C2 并给出推断规则或安全默认值[^src-3]

[^src-1]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- "linting.md Development Note" -- "When you change the canonical structure or frontmatter schema, update the rules in this file... do NOT write migration code."
[^src-2]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- "linting.md Development Note" -- "Mechanical layer (C11/C12/C13)... Fully auto-fixable... Editorial layer (C8/C9)... Never auto-fixed"
[^src-3]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- "linting.md Development Note" -- "Renamed a frontmatter field? Append an entry to C13's alias table (old → new). Never remove old aliases."
