---
id: memex-llm-kb-lineage
title: Memex 到 LLM KB 的思想谱系
status: accepted
card_type: historical-lineage
tags:
- knowledge-management
- memex
- vannevar-bush
- intellectual-history
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- developersio-jp-pattern
evidence_basis: practitioner_report
justification: ../justification/memex-llm-kb-lineage.md
canonical_concept: memex-llm-kb-lineage
aliases:
- Memex
- メメックス
- Vannevar Bush
- 連想トレイル
summary: '作者将 Karpathy LLM KB 与 Vannevar Bush 1945 年 Memex 概念(文档间联想 trail 装置)类比: 80
  年越しに LLM が Markdown ファイルの中で実現しつつある。LLM KB 的 backlink + entity page 结构类似 Memex 的
  associative trail。memex-llm-kb-lineage メメックス Vannevar Bush 連想'
related:
- connections-as-value
- karpathy-llm-wiki-three-layer-architecture
- karpathy-llm-wiki-concept
---

作者将 LLM Knowledge Base 置于 Vannevar Bush Memex (1945) 的思想谱系中 [^src-1]:

- **Memex**: Bush 在 "As We May Think" 中提出的装置, 核心功能是在文档间建立联想 trail(連想トレイル)并可随时回溯
- **LLM KB 对应**: Wiki 中的 backlink、entity page、index 构成类似的联想网络
- **作者观察**: "80 年越しに、LLM がそれを Markdown ファイルの中で実現しつつあるのかもしれません"

这一类比暗示 LLM KB 并非全新发明, 而是长久以来人类对"外部化联想记忆"需求的最新技术实现 [^card-1]。

[^src-1]: `data/raw/webpage/developersio-jp-pattern/markdown.md` -- "意図的な「抽象さ」" P24 -- "概念としては、Vannevar Bush が 1945 年に提唱した Memex（ドキュメント間の連想トレイルを辿る装置）を思い出します。80 年越しに、LLM がそれを Markdown ファイルの中で実現しつつあるのかもしれません。"
[^card-1]: 参见 [llm-as-knowledge-compiler] — LLM 编译器隐喻是 Memex 愿景的现代实现手段
