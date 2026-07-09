---
schema: claude_code_process_pack.v1
publish_status: sanitized
source_class: local_claude_code_sessions
created: 2026-07-09
---

# Claude Code Process Pack

这个目录是 Claude Code 交互的公开主题包（themed process pack）。它不是隐藏配置目录或本地 Claude session 的原样上传，而是从本地交互、loop artifacts、user-insights 和 git history 中提炼出来的可发布机制。

## What This Is

- 对 Claude Code session 中有价值的 workflow、runtime lesson、failure mode 和 design decision 做主题化整理。
- 把“这些文档为什么长出来”连接到 repo 内可审计证据。
- 保留中文主语言（Chinese main language），用 English anchor 标注关键术语。

## What This Is Not

- 不是完整 raw transcript。
- 不包含 Claude JSONL、Codex JSONL、本机隐藏配置、token、endpoint、邮箱或绝对路径。
- 不把 repo-local 或 user-home 的 Claude hidden folder 打包进 git。

## Themes

| Theme | File | Focus |
| --- | --- | --- |
| Runtime Boundary | [01-runtime-and-context-isolation.md](themes/01-runtime-and-context-isolation.md) | main-agent / sub-agent 边界、冷启动、context isolation |
| Source To Card | [02-source-to-card-workflow.md](themes/02-source-to-card-workflow.md) | source mining、draft-first、provenance、KB adoption |
| Governance And Audit | [03-governance-and-audit.md](themes/03-governance-and-audit.md) | fusion、interlink、backlink、FSJS audit |
| Failure Corrections | [04-failure-modes-and-corrections.md](themes/04-failure-modes-and-corrections.md) | drift、截断、过度合并、信息密度退化 |
| Publishing And Redaction | [05-publishing-and-redaction.md](themes/05-publishing-and-redaction.md) | raw transcript local-only、公开摘要、process provenance |

## Evidence

证据地图见 [evidence_map.md](evidence_map.md)。本目录只链接到 repo 内可发布 artifact；本地 raw session 只作为未公开证据源（local-only evidence source）。
