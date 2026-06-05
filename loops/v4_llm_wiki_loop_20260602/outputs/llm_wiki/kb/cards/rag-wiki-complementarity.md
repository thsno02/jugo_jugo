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
related: [full-context-anti-rag, llm-wiki-pattern, scenario-based-tool-selection, wiki-rag-hybrid-pattern]
---

在 LLM Wiki 的实际运用中，RAG 与 wiki 并非互斥的二选一关系，而是功能互补的两种模式[^src-1]。

**RAG 适用场景**：临时性（ad-hoc）问题，需要快速从文档片段中检索答案的查询。

**Wiki 适用场景**：全局理解、跨项目认知，需要掌握整体脉络的场景[^src-2]。

这一观察来自作者同时运用两种方式的实践经验。作者在已有的 Mem0 + pgvector 向量检索基础上叠加了 wiki 编译层，实际运行后发现两者自然形成了互补分工[^src-3]。

Karpathy 原文的表述偏向「本以为需要 RAG，但 wiki 已经够用」，语气上更倾向于 wiki 可替代 RAG[^src-4]，Obsidian 插件文档进一步将此发展为明确的反 RAG 架构立场[^dist-1]。本文作者则明确指出这不是二择一，两者在不同使用场景下各有优势。不过这一互补判断有前提条件：Karpathy 指出其 wiki 规模约为 100 篇文章、约 40 万词，在更大规模下 wiki 单独运作的局限性可能更突出[^src-5]。Atlan 的分析将这种互补推进为具体的混合架构设计模式[^card-1]。Robin Cartier 材料进一步将互补关系扩展为三方选择框架，引入关系型知识库作为第三选项[^card-2]。

## Footnotes

[^card-1]: [Wiki-RAG 混合架构模式](wiki-rag-hybrid-pattern.md) -- 日本社区从实践经验观察到 wiki 与 RAG 的互补关系，Atlan 将这一观察系统化为三种混合架构模式（wiki 作为策展上下文层、两层分离、受治理的元数据层）

[^src-1]: `data/raw/webpage/developersio-jp-pattern/text.txt` -- L82-83 -- "個人的には、「RAG か wiki か」は二択ではないと思っています"
[^src-2]: `data/raw/webpage/developersio-jp-pattern/text.txt` -- L83 -- "アドホックな質問には RAG 的な検索が便利で、全体像の把握やプロジェクト横断の理解には wiki が便利"
[^src-3]: `data/raw/webpage/developersio-jp-pattern/text.txt` -- L99 -- "自分の場合は Memory MCP（Mem0 + pgvector）という検索レイヤーが間に入っていて、RAG 的な検索と wiki の両方を使い分けています"
[^src-4]: `data/raw/webpage/developersio-jp-pattern/text.txt` -- L78-79 -- "I thought I had to reach for fancy RAG, but the LLM has been pretty good about auto-maintaining index files"
[^src-5]: `data/raw/webpage/developersio-jp-pattern/text.txt` -- L81 -- "これは規模が ~100 記事、~400K words（約 40 万語）という比較的小さなスケールでの話です"
[^dist-1]: [全上下文反 RAG 架构选择](full-context-anti-rag.md) -- 本卡主张 RAG 与 wiki 功能互补可以并存，该卡主张完全拒绝 RAG 以保持跨知识图谱推理能力，区分点在于是否承认 RAG 在临时查询场景中的独立价值
[^card-2]: [场景驱动的知识工具选择](scenario-based-tool-selection.md) -- 本卡从实践观察得出 wiki 与 RAG 互补的二元结论，该卡引入关系型知识库作为第三选项，将二元互补扩展为三段式场景选择框架
