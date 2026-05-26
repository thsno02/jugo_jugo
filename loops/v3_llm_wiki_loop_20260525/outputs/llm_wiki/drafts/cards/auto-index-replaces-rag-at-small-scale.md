---
id: auto-index-replaces-rag-at-small-scale
title: 小规模 wiki 下自维护索引可以替代 RAG
status: draft
card_type: operational_rule
tags: [#llm-wiki, #rag, #retrieval, #indexes, #scale]
created_time: 2026-05-25T22:05:00+08:00
edited_time: 2026-05-26T10:50:00+08:00
edited_entity: llm
source_ids: [karpathy-x-launch-post]
provenance_card: ../provenance/auto-index-replaces-rag-at-small-scale.md
aliases: ["小规模无 RAG 规则", "索引优先检索"]
related: [llm-knowledge-base-five-stage-workflow, karpathy-llm-wiki-vs-rag, karpathy-wiki-full-context-vs-rag, anthemcreation-llm-wiki-vs-rag-multi-hop, robin-cartier-scale-ceiling, file-outputs-back-as-compounding-loop]
---

一个常见的默认假设是：任何 wiki 规模的问答系统都必须搭一套基于向量嵌入的 RAG。Karpathy 的实践经验在一个具体的工作点上反驳了这个假设——约 100 篇文章、约 40 万词。在这个规模下他发现，"LLM 在自维护索引文件和每篇文档的简短摘要这件事上做得很不错，能够轻松读到所有相关的关键数据。"

由此可以总结出一条操作性规则：

- **小规模下默认走索引，而不是 embedding。** 让 LLM 用纯 markdown 维护一份顶层索引和每篇文档的简要摘要。查询时，LLM 先读索引，决定要打开哪些文档，再按路径拉取。这种方式成本低、过程完全透明、并且在 linting 阶段可以自我修复。
- **只有当索引策略真的失效时再上 RAG。** 触发条件是：索引 + 摘要不再能舒服地塞进上下文窗口；或者 LLM 开始系统性地漏读相关文档。在这条阈值之下，RAG 只会带来基础设施成本，不会改变答案质量。

之所以这种方式在小规模下成立：索引 + 摘要把整份语料"压扁"成一张可被导航的地图，整张地图能塞进单次上下文。LLM 在做的事情是"在一份精心维护的地图上按关键词/主题路由"，而不是"在一堆不透明向量里做近邻搜索"。错误是显式的（链接错了、摘要过时了），并且可以被同一个 LLM 在 linting 阶段直接修掉。

边界：这并不是在说 RAG 整体不必要。这是关于"小语料、且索引 + 摘要维护成本很低"这一段范围内的规则。作者本人也明确指出，wiki 真正变大之后下一步应当考虑"合成数据 + 微调"。

## References

- Karpathy 引用推文中的 Q&A 章节（`data/raw/webpage/karpathy-x-launch-post/text.txt`，JSON 指针 `$.tweet.quote.text`）。

## Footnotes

- `data/raw/webpage/karpathy-x-launch-post/text.txt` — JSON 指针 `$.tweet.quote.text`，"Q&A:" 章节（`"I thought I had to reach for fancy RAG, but the LLM has been pretty good about auto-maintaining index files and brief summaries of all the documents and it reads all the important related data fairly easily at this ~small scale."`）。
