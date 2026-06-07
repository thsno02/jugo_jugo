---
id: zero-runtime-dependency
title: 零运行时依赖
status: accepted
card_type: concept
tags: [llm-wiki, architecture, dependencies, portability]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [llm-wiki-net]
justification: ../justification/zero-runtime-dependency.md
canonical_concept: zero-runtime-dependency
aliases: [零依赖, zero dependencies, 无运行时依赖, no runtime deps]
summary: >-
  zero-runtime-dependency（零依赖 / zero dependencies / 无运行时依赖 / no runtime deps）
  是 LLM Wiki 的架构约束：完全运行在宿主智能体的内置工具上（文件读写/网络搜索/网页抓取），
  插件本身是 Markdown + 命令定义，无服务器/服务/遥测
related: [multi-platform-skill-portability, llm-wiki-pattern, full-stack-locality]
---

LLM Wiki 的一个核心架构约束是**零运行时依赖**[^src-1]。具体含义：

- 完全运行在宿主智能体的**内置工具**上：文件读写（file read/write）、网络搜索（web search）、网页抓取（web fetch）[^src-2]
- 插件本身是 **Markdown**：命令定义、技能描述、参考文档——不是可执行代码[^src-3]
- **无服务器、无服务、无遥测**[^src-4]

这一约束使得 LLM Wiki 天然可移植——同一套技能定义可以在 Claude Code、Codex、OpenCode、Pi 和任意 LLM agent 上运行[^src-5]。零依赖是多平台技能可移植性的前提条件：正因为不依赖任何特定运行时的专有 API，单一的 wiki-manager 技能才能跨五种安装模式共享[^card-1]。这一架构约束也是 LLM Wiki 模式的核心设计决策之一——通过消除基础设施依赖，将系统的复杂性压缩到 Markdown 和宿主工具两个维度[^card-2]。在隐私敏感场景下，零依赖与全栈本地性形成天然互补：无外部服务意味着数据不必离开本机，满足「敏感数据永不离机」的全栈本地架构需求[^card-3]。

可选依赖仅在特定场景推荐：`ask-grok-mcp` 用于 tweet 摄入、`tobi/qmd` 用于超过约 100 篇文章时的本地搜索[^src-6]。离线时 compile、query、lint、output 正常工作——所有内容都是磁盘上的纯 Markdown；研究和摄入需要网络[^src-7]。

## Footnotes

[^card-1]: [多平台技能可移植性](multi-platform-skill-portability.md) -- 零依赖是跨平台可移植的前提：无运行时依赖使单一技能定义可在五种安装模式中共享
[^card-2]: [LLM Wiki 模式](llm-wiki-pattern.md) -- 零依赖是 LLM Wiki 模式的核心架构约束，将系统复杂性压缩到 Markdown 和宿主工具
[^card-3]: [全栈本地性](full-stack-locality.md) -- 零依赖与全栈本地性互补：无外部服务使数据可完全保留在本机

[^src-1]: `data/raw/webpage/llm-wiki-net/text.txt` -- "Zero dependencies" L166-168 -- "Runs entirely on the host agent's built-in tools. Plugin is Markdown + commands. No servers, no services, no telemetry."
[^src-2]: `data/raw/webpage/llm-wiki-net/text.txt` -- "FAQ: dependencies" L490-491 -- "LLM Wiki uses only the built-in tools of the host agent (file read/write, web fetch, web search)."
[^src-3]: `data/raw/webpage/llm-wiki-net/text.txt` -- "FAQ: dependencies" L491 -- "The plugin itself is Markdown: command definitions, skills, and reference docs."
[^src-4]: `data/raw/webpage/llm-wiki-net/text.txt` -- "Zero dependencies" L168 -- "No servers, no services, no telemetry."
[^src-5]: `data/raw/webpage/llm-wiki-net/text.txt` -- "FAQ: agents" L440-442 -- "The behavioral logic lives in a single wiki-manager skill shared across runtimes"
[^src-6]: `data/raw/webpage/llm-wiki-net/text.txt` -- "FAQ: dependencies" L492 -- "Optional: ask-grok-mcp for best-in-class tweet ingestion, tobi/qmd for local search beyond ~100 articles."
[^src-7]: `data/raw/webpage/llm-wiki-net/text.txt` -- "FAQ: offline" L486-487 -- "Compiling, querying, linting, and generating artifacts from an existing wiki work offline... Research and ingestion need internet"
