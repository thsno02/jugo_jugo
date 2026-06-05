---
id: ai-memory-operating-system
title: AI 记忆操作系统框架
status: accepted
card_type: concept
tags: [memory-architecture, obsidian, pinecone, vector-search, long-term-memory]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [robin-cartier-llm-knowledge-bases]
justification: ../justification/ai-memory-operating-system.md
canonical_concept: ai-memory-operating-system
aliases: [AI 记忆操作系统, AI memory operating system, 记忆系统分类]
summary: >-
  ai-memory-operating-system（AI 记忆操作系统 / AI memory operating system / 记忆系统分类）
  是 Jack Roberts 提出的框架：将 AI 记忆视为操作系统级组件，Obsidian/markdown 是可读的长期记忆选项，
  Pinecone/vector 是可扩展的语义搜索选项
related:
  - llm-wiki-pattern
  - llm-wiki-scale-boundary
  - episodic-semantic-memory-duality
---

Jack Roberts 将 LLM Wiki 模式定位在一个更宏观的框架中：**AI 记忆操作系统（AI memory operating system）**[^src-1]。在这一框架下，AI agent 的持久记忆被视为操作系统层面的基础设施，有不同的实现选项：

- **Obsidian/markdown**——可读的长期记忆选项。人类可以直接浏览、编辑和理解存储的知识。LLM Wiki 模式属于这一类别。
- **Pinecone/vector memory**——可扩展的语义搜索选项。适合大规模语料库的自动检索，但人类可读性较低。

这一分类的价值在于将 LLM Wiki 从「一个具体的知识管理方法」提升为「AI 记忆架构中的一种设计选择」，明确了其定位：它是在可读性与可扩展性之间做出的权衡[^src-1]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/robin-cartier-llm-knowledge-bases/text.txt` -- L33 -- "Jack Roberts places the same pattern inside a broader AI memory operating system: Obsidian/markdown is the readable long-term memory option, while Pinecone/vector memory is the scalable semantic-search option [src-059]."
