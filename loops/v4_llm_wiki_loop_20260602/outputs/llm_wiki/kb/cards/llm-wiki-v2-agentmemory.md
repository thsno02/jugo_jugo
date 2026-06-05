---
id: llm-wiki-v2-agentmemory
title: LLM Wiki v2 社区扩展与 agentmemory 模式
status: accepted
card_type: source_claim
tags: [llm-wiki, community-extension, agentmemory, autonomous-agent, rohitg00]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [anthemcreation-en-guide]
justification: ../justification/llm-wiki-v2-agentmemory.md
canonical_concept: llm-wiki-v2-agentmemory
aliases: [LLM Wiki v2, agentmemory 模式, rohitg00 扩展]
summary: >-
  llm-wiki-v2-agentmemory（LLM Wiki v2 / agentmemory 模式 / rohitg00 扩展）是 rohitg00
  在 GitHub Gist 上发布的社区扩展，通过引入 agentmemory 模式将 LLM Wiki 从个人研究工具扩展为
  适合自主编程代理持续填充的持久化记忆引擎
related: [llm-wiki-pattern]
---

Karpathy 的 LLM Wiki 原始 Gist 被设计为**协作蓝图（collaborative blueprint）**而非完成品[^src-1]。自 2026 年 4 月发布以来，社区已产出显著扩展。

其中最值得注意的是 rohitg00 在 GitHub Gist 上发布的 **LLM Wiki v2**，它通过引入 **agentmemory 模式**扩展了原始概念——这是一个为 AI 编程代理设计的持久化记忆引擎[^src-2]。该版本整合了在规模化（scaling）和长期一致性（long-term consistency）方面的经验教训，使 wiki 更适合**自主代理持续填充**的使用场景[^src-3]。

该来源同时预测 LLM Wiki 的最可能演化方向之一是**自主代理原生集成**——代理在无人工干预的情况下维护 wiki[^src-4]。agentmemory 模式是这一方向的早期社区实践。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/anthemcreation-en-guide/text.txt` -- L156-157 -- "Karpathy's original Gist is designed as a collaborative blueprint, not a finished product. Since its publication in April 2026, the community has already produced notable extensions."
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/anthemcreation-en-guide/text.txt` -- L158-159 -- "LLM Wiki v2, published on GitHub Gist by rohitg00, extends the concept with agentmemory patterns: a persistent memory engine designed for AI coding agents."
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/anthemcreation-en-guide/text.txt` -- L159 -- "This version incorporates lessons on scaling and long-term consistency, making the wiki more suitable for autonomous agents that continuously feed it."
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/anthemcreation-en-guide/text.txt` -- L166 -- "Native integration into autonomous agents that maintain the wiki without human intervention"
