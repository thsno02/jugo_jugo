---
schema: claude_code_theme.v1
theme: publishing_and_redaction
publish_status: sanitized
---

# Publishing And Redaction

Claude Code / Codex 交互本身可以成为知识来源，但 raw transcript 不应直接发布。

## Decision

不把隐藏目录原样打包进 git：

- 不提交 repo-local raw transcript export folder；
- 不提交本地 Claude project JSONL；
- 不提交 Codex raw session；
- 不提交本机配置、权限配置、endpoint、token 或完整工具输出。

## Publishable Layer

可发布的是二次整理后的层：

- timeline；
- decision log；
- workflow architecture；
- failure modes；
- audit gates；
- evidence map。

## Why

raw transcript 的问题不是只有“是否有凭据”。它还包含：

- 本机路径；
- session metadata；
- tool results；
- 个人工作上下文；
- 未筛选的中间判断；
- 大量对公开读者无意义的噪声。

更好的做法是把 raw transcript 留作 local-only evidence，把真正有复用价值的机制写成文档，并链接到 repo 内已发布的 artifacts。
