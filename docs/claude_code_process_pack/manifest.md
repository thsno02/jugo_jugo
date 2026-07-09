---
schema: claude_code_process_pack_manifest.v1
publish_status: sanitized
raw_transcripts_included: false
---

# Manifest

## Source Classes

| Source Class | Coverage | Publish Decision |
| --- | --- | --- |
| Claude Code local session group | partial/session-file | 摘要化发布；raw JSONL 不入 git |
| Codex thread context | limited/current-thread | 仅用于补断档；raw Codex transcript 不入 git |
| loop artifacts | high/repo-tracked | 直接作为证据链接 |
| user-insights summaries | sanitized | 可发布 |
| git history | high/process commits | 可发布 |

## Redaction Rules

- 删除或抽象本机路径、邮箱、endpoint、token、权限配置和完整工具输出。
- 不发布完整 `Raw Input` 长摘录。
- session id 只用抽象标识，例如 `claude:v3-primary`。
- 可公开内容必须是机制（mechanism）、决策（decision）、失败模式（failure mode）、门禁（gate）或证据地图（evidence map）。

## Package Boundaries

本包发布的是“Claude Code 参与构建这个 repo 的方法论层”，不是 Claude Code 的运行状态。隐藏目录和原始 session 仍然是本地工作材料。
