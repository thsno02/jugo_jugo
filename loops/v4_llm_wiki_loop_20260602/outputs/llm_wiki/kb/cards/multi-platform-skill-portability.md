---
id: multi-platform-skill-portability
title: 多平台技能可移植性
status: accepted
card_type: mechanism
tags: [llm-wiki, portability, plugin, multi-platform, skill-sharing]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [llm-wiki-net]
justification: ../justification/multi-platform-skill-portability.md
canonical_concept: multi-platform-skill-portability
aliases: [多平台可移植, skill portability, 跨平台技能, multi-platform plugin]
summary: >-
  multi-platform-skill-portability（多平台可移植 / skill portability / 跨平台技能 / multi-platform plugin）
  是 LLM Wiki 的分发机制：单一 wiki-manager 技能为所有运行时的行为源（Claude Code/Codex/OpenCode/Pi/AGENTS.md），
  Codex/OpenCode/Pi 通过 symlink 链到 Claude 源，漂移由自愈测试捕获
related: []
---

LLM Wiki 支持**五种安装模式**，但行为逻辑来自单一来源[^src-1]：

| 安装模式 | 形式 | 调用方式 |
|---------|------|---------|
| Claude Code | 原生插件（marketplace） | `/wiki:*` |
| OpenAI Codex | marketplace 插件 | `@wiki` |
| OpenCode | 指令文件（opencode.json） | 通过指令加载 |
| Pi | 指令文件 | 通过 `--instructions` 加载 |
| 任意 agent | 便携 AGENTS.md | 放入项目根目录 |

关键架构决策：**行为逻辑全部存在于单一的 wiki-manager 技能中**，跨运行时共享。Codex、OpenCode 和 Pi 的目录树通过 symlink 链接到 Claude 的 source of truth——因此不存在代码分叉[^src-2]。

**漂移防护**：自愈同步测试（self-healing sync tests）负责捕获任何运行时间的偏离[^src-3]。

Pi 的特殊优势在于其 1K 系统提示留有足够空间在 32K 上下文的本地模型上加载完整的 wiki 技能[^src-4]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/llm-wiki-net/text.txt` -- "FAQ: agents" L440 -- "Five install modes: Claude Code (native plugin via the llm-wiki marketplace), OpenAI Codex (marketplace plugin...), OpenCode (instruction file...), Pi (instruction file...), and any other LLM agent via the portable AGENTS.md file."
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/llm-wiki-net/text.txt` -- "FAQ: agents" L442 -- "The behavioral logic lives in a single wiki-manager skill shared across runtimes — Codex, OpenCode, and Pi trees symlink into the Claude source of truth so there is no fork."
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/llm-wiki-net/text.txt` -- "FAQ: agents" L442 -- "Drift is caught by self-healing sync tests."
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/llm-wiki-net/text.txt` -- "Pi" L92-96 -- "Pi's 1K system prompt leaves room for the full wiki skill on 32K context local models."
