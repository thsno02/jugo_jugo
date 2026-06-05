---
id: graphrag-small-context-window-advantage
title: GraphRAG 中小上下文窗口反而更优的发现
status: accepted
card_type: source_claim
tags: [context-window, lost-in-the-middle, graphrag, evaluation]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-graphrag]
justification: ../justification/graphrag-small-context-window-advantage.md
canonical_concept: graphrag-small-context-window-advantage
aliases: [小上下文窗口优势, smaller context window advantage, 8k 上下文优于更大窗口]
summary: >-
  graphrag-small-context-window-advantage（小上下文窗口优势 / smaller context window advantage）GraphRAG 评估中 8k 上下文窗口在全面性上普遍优于 16k/32k/64k（平均胜率 58.1%），呼应 lost-in-the-middle 现象，因此采用 8k 作为统一设置
related: [context-window-degradation, graphrag-map-reduce-query]
---

GraphRAG 论文在选择上下文窗口大小时发现了一个反直觉的结果。尽管 gpt-4-turbo 支持 128k token 的大上下文窗口，但论文测试了 8k、16k、32k 和 64k 四种窗口大小后发现：最小的 8k 窗口在全面性上普遍优于所有更大的窗口（平均胜率 58.1%），同时在多样性（52.4%）和赋能性（51.3%）上与更大窗口表现相当 [^src-1]。

论文将这一现象与"lost in the middle"研究联系起来——信息在较长上下文中可能"丢失" [^src-2]。

基于这一发现，论文选择了固定的 8k token 上下文窗口用于生成社区摘要、社区回答和全局回答的所有最终评估 [^src-3]。

这一发现对 RAG 系统设计有实际意义：更大的上下文窗口并非总是更好；当信息量大时，分而治之（如 map-reduce 式处理多个较小上下文）可能优于将所有信息塞入一个大上下文窗口。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- Appendix C (appendix.tex) -- "Surprisingly, the smallest context window size tested (8k) was universally better for all comparisons on comprehensiveness (average win rate of 58.1%), while performing comparably with larger context sizes on diversity (average win rate = 52.4%), and empowerment (average win rate = 51.3%)."
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- Appendix C (appendix.tex) -- "Given the potential for information to be 'lost in the middle' of longer contexts"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- Section 2.1.3 (graph_rag.tex) -- "We used a fixed context window size of 8k tokens for generating community summaries, community answers, and global answers"
