---
schema: justification_journal.v1
card: ../cards/hub-resolution-algorithm.md
created_time: 2026-06-08T10:00:00+08:00
---

## creation | 2026-06-08T10:00:00+08:00

生成方式：Mode A extraction from repo source bundle
来源：`data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt`
源证据：
- FILE: claude-plugin/skills/wiki-manager/SKILL.md — "Resolution: At the start of every operation, resolve HUB by reading ~/.config/llm-wiki/config.json first. Prefer hub_path..."
- FILE: claude-plugin/commands/wiki.md — 完整的四步解析流程（config.json → resolved_path fallback → ~/wiki → ask user）
- FILE: README.md — "agents prefer portable hub_path, treat legacy resolved_path values as fallback caches, resolve wikis.json paths relative to the current hub"
- FILE: AGENTS.md — "store portable relative paths like topics/<name>, not /Users/<name>/... absolute paths"
- FILE: README.md — iCloud permission diagnostics: stat 成功但读取失败的诊断逻辑
范围论证：Hub 路径解析算法是每个 llm-wiki 操作的前置协议，涉及 config 优先级链、iCloud 跨机可移植性约束、权限诊断策略和 wiki 位置二次解析。这是一个完整的独立机制，不同于 llm-wiki-pattern（描述模式层面概念）或 archive-lifecycle（仅涉及归档路径处理）。已有卡片均未覆盖这一运行时基础设施层面的路径定位逻辑。
