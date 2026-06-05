---
id: rag-wiki-complementarity
title: RAG 与 Wiki 的互补关系
status: accepted
card_type: distinction
tags: [llm-wiki, rag, complementarity, practical-observation]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [developersio-jp-pattern]
justification: ../justification/rag-wiki-complementarity.md
canonical_concept: rag-wiki-complementarity
aliases: [RAG-Wiki互补, RAG与Wiki并用, rag-wiki-both]
summary: >-
  rag-wiki-complementarity（RAG-Wiki互补 / RAG与Wiki并用）指实际运用中 RAG 和 Wiki
  并非二选一：临时性问题适合 RAG 检索，全局理解和跨项目把握适合 Wiki，两者可并存于同一系统
related: [llm-wiki-pattern]
---

在 LLM Wiki 的实际运用中，RAG 与 wiki 并非互斥的二选一关系，而是功能互补的两种模式[^src-1]。

**RAG 适用场景**：临时性（ad-hoc）问题，需要快速从文档片段中检索答案的查询。

**Wiki 适用场景**：全局理解、跨项目认知，需要掌握整体脉络的场景[^src-2]。

这一观察来自作者同时运用两种方式的实践经验。作者在已有的 Mem0 + pgvector 向量检索基础上叠加了 wiki 编译层，实际运行后发现两者自然形成了互补分工[^src-3]。

Karpathy 原文的表述偏向「本以为需要 RAG，但 wiki 已经够用」，语气上更倾向于 wiki 可替代 RAG[^src-4]。本文作者则明确指出这不是二择一，两者在不同使用场景下各有优势。不过这一互补判断有前提条件：Karpathy 指出其 wiki 规模约为 100 篇文章、约 40 万词，在更大规模下 wiki 单独运作的局限性可能更突出[^src-5]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/developersio-jp-pattern/text.txt` -- L82-83 -- "個人的には、「RAG か wiki か」は二択ではないと思っています"
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/developersio-jp-pattern/text.txt` -- L83 -- "アドホックな質問には RAG 的な検索が便利で、全体像の把握やプロジェクト横断の理解には wiki が便利"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/developersio-jp-pattern/text.txt` -- L99 -- "自分の場合は Memory MCP（Mem0 + pgvector）という検索レイヤーが間に入っていて、RAG 的な検索と wiki の両方を使い分けています"
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/developersio-jp-pattern/text.txt` -- L78-79 -- "I thought I had to reach for fancy RAG, but the LLM has been pretty good about auto-maintaining index files"
[^src-5]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/developersio-jp-pattern/text.txt` -- L81 -- "これは規模が ~100 記事、~400K words（約 40 万語）という比較的小さなスケールでの話です"
