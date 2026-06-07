---
id: hub-resolution-algorithm
title: Hub 路径解析算法
status: accepted
card_type: mechanism
tags: [llm-wiki, hub-resolution, icloud, portable-path, config]
created_time: 2026-06-08T10:00:00+08:00
edited_time: 2026-06-08T10:00:00+08:00
edited_entity: llm
source_ids: [repo-nvk-llm-wiki]
justification: ../justification/hub-resolution-algorithm.md
canonical_concept: hub-resolution-algorithm
aliases: [Hub 解析, hub resolution, wiki 路径解析, hub path resolution]
summary: >-
  hub-resolution-algorithm（Hub 解析 / hub resolution / wiki 路径解析 / hub path resolution）
  是 llm-wiki 每次操作前的路径定位协议：config.json hub_path 优先、resolved_path 作为遗留回退、
  ~/wiki 最后兜底，iCloud 跨机场景使用可移植相对路径而非绝对路径
related: [archive-lifecycle, llm-wiki-pattern, three-layer-architecture]
---

llm-wiki 的每个命令在执行前都必须先**解析 Hub 路径**——即确定 wiki 数据的根目录位置。这一解析遵循严格的优先级链[^src-1]：

1. 读取 `~/.config/llm-wiki/config.json`，如存在 `hub_path` 字段则使用（仅展开前导 `~`，不展开 `com~apple~CloudDocs` 中的 `~`）[^src-2]
2. 如配置中仅有 `resolved_path`，将其作为遗留回退缓存使用[^src-3]
3. 如无配置文件，检查 `~/wiki/_index.md` 是否存在[^src-4]
4. 如以上均失败，询问用户

**iCloud 跨机可移植性**是该算法的核心约束。`wikis.json` 中的主题路径存储为相对路径（如 `topics/<slug>`），而非 `/Users/<name>/...` 绝对路径——因为绝对路径在另一台 Mac 上无效[^src-5]。旧配置中的 `resolved_path` 被视为机器本地缓存，不写入共享配置[^src-6]。

**iCloud 权限诊断**：当 `stat` 成功但读取 `wikis.json` 或列出 `topics/` 失败并返回 `Operation not permitted` 时，说明路径本身正确，问题在于 macOS 隐私权限阻止了启动器应用的访问——应引导用户授予「完全磁盘访问」或 iCloud Drive 权限并重启，而非回退到其他路径[^src-7]。

Wiki 位置在 Hub 确定后进一步按优先级解析：`--local` 标记指向 `.wiki/`；`--wiki <name>` 通过 `wikis.json` 查找（支持 `<HUB>`、`~`、绝对路径或 HUB 相对路径）；当前目录有 `.wiki/` 则使用之；否则回退到 HUB[^src-8]。

该算法使 llm-wiki 能在无外部依赖的情况下跨 Claude Code、Codex、OpenCode、Pi 四个运行时正确定位数据[^card-1]，也确保归档主题在解析后能被正确识别和跳过[^card-2]。

## Footnotes

[^card-1]: [LLM Wiki 模式](llm-wiki-pattern.md) -- Hub 解析算法是 LLM Wiki 模式的运行时实现基础：模式描述"做什么"，解析算法解决"数据在哪里"
[^card-2]: [主题归档生命周期](archive-lifecycle.md) -- Hub 解析完成后，归档主题通过 wikis.json status 和 topics/.archive/ 路径被识别并默认跳过

[^src-1]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- FILE: claude-plugin/skills/wiki-manager/SKILL.md -- "Resolution: At the start of every operation, resolve HUB by reading ~/.config/llm-wiki/config.json first."
[^src-2]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- FILE: claude-plugin/commands/wiki.md -- "If it has hub_path, expand leading ~ only (not tildes in com~apple~CloudDocs) and prefer that path"
[^src-3]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- FILE: AGENTS.md -- "Treat resolved_path from older configs as a machine-specific fallback cache, not as the source of truth"
[^src-4]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- FILE: claude-plugin/commands/wiki.md -- "If no config -> read $HOME/wiki/_index.md. If it exists -> HUB = $HOME/wiki."
[^src-5]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- FILE: AGENTS.md -- "store portable relative paths like topics/<name>, not /Users/<name>/... absolute paths; absolute user-home paths break when an iCloud wiki is opened from another Mac"
[^src-6]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- FILE: README.md -- "agents prefer portable hub_path, treat legacy resolved_path values as fallback caches"
[^src-7]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- FILE: README.md -- "stat succeeds for the iCloud wiki path, but reading wikis.json or listing topics/ fails with Operation not permitted. That means the configured hub_path is correct; grant Full Disk Access"
[^src-8]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- FILE: claude-plugin/commands/wiki.md -- "Wiki location (first match): --local -> .wiki/ in CWD; --wiki <name> -> HUB/wikis.json lookup..."
