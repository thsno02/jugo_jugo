---
id: kb-lint-deterministic-validation
title: 确定性 Lint 校验体系
status: draft
card_type: mechanism
tags: [lint, validation, schema-health, wiki-health, multimodal]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [clawhub-llm-wiki-karpathy]
evidence_basis: documentation
justification: ../justification/kb-lint-deterministic-validation.md
canonical_concept: kb-lint-deterministic-validation
aliases: [kb_lint, lint, wiki health check, schema health, 确定性 lint]
summary: >-
  kb-lint-deterministic-validation 确定性 lint 校验覆盖 schema 与 wiki 健康：
  检查 missing representation trails、stale representations、inconsistent asset_paths、
  isolated pages、stale source coverage、unsupported claims、contradiction candidates、
  missing high-value pages，对多模态 source note 额外验证 believable review trail。
related: []
---

## 确定性 Lint 校验体系

`kb_lint` 提供确定性的 schema 与 wiki 健康检查 [^src-1]，覆盖以下检查项：

- **missing representation trails**: 多模态源缺少中间表示
- **stale representations**: 已过时的中间表示
- **inconsistent asset_paths**: 资产路径与实际不一致
- **isolated pages**: 孤立页面（无链接连入）
- **stale source coverage**: 源覆盖已过时
- **unsupported claims**: 缺乏支撑的声明
- **contradiction candidates**: 潜在矛盾
- **missing high-value pages**: 缺失的高价值页面

对于多模态 source note，lint 还额外检查是否有 "believable review trail"——确保 wiki 不会依赖未经审查的多模态内容 [^src-2]。

[^src-1]: `data/raw/webpage/clawhub-llm-wiki-karpathy/markdown.md` -- "What 0.4.4 Implements" P28 -- "deterministic lint for schema and wiki health, including warnings for..."
[^src-2]: `data/raw/webpage/clawhub-llm-wiki-karpathy/markdown.md` -- "Runtime Philosophy" P120 -- "kb_lint stays deterministic, but now also checks whether multimodal source notes have a believable review trail"
[^card-1]: [[representation-first-design]] — lint 验证 representation trail 的存在性是 representation-first 设计的质量保障
