---
id: karpathy-llm-wiki-source-executable-analogy
title: Karpathy 把 LLM wiki 比作"源码 vs 编译产物"
status: draft
card_type: distinction
tags: [#llm-wiki, #karpathy, #rag-vs-wiki]
created_time: 2026-05-26T15:00:00+08:00
edited_time: 2026-05-26T15:00:00+08:00
edited_entity: llm
source_ids: [anthemcreation-en-guide]
provenance_card: ../provenance/karpathy-llm-wiki-source-executable-analogy.md
aliases: [source vs executable, Karpathy compiled wiki]
related: [my-llm-wiki-three-layer-implementation]
---

## 核心区分

Karpathy 2026-04 发布 LLM Wiki Gist 时给出的核心类比是：

- **原始资料 = 源代码（source code）**——论文、PDF、笔记，保持不变。
- **LLM 维护的 wiki = 编译产物（compiled executable）**——markdown 互联文件，被 LLM 主动写入、合并、消解矛盾。
- **每次查询 = 运行 executable**，而不是 "重新编译"。

这与 RAG 的本质差异不是速度，而是**推理深度**：
| 维度 | RAG | LLM wiki |
|---|---|---|
| 每次 query 做什么 | 检索原始文档 chunk → 即时生成 | 在已经合成好的 wiki 上读 |
| 跨文档关系 | 隐式（向量空间临近） | 显式（`[[wikilinks]]`、矛盾段、合成总结） |
| 多跳推理 | 难（要在 chunk 之间临时拼） | 自然（图边已经构造好） |
| 个人规模 10-100 份 | 过度设计 | 正合适 |
| 万级以上语料 | 仍然合适 | 维护互联成本变高 |

## 为什么这条类比是关键

- 它把"知识库"从"检索问题"重新定位为"编译问题"：编译器对源代码的承诺是 *"重新编译会得到等价结果"*，于是允许把编译产物缓存复用；同理，LLM wiki 把"反复 query 源文件"压缩成"一次性 ingest + 长期查询编译后的版本"。
- 它解释了 Karpathy 自己的实践规模——超过 100 篇文章、40 万字——为什么不需要向量数据库：在该规模下，markdown + Obsidian backlink 就够；向量检索只有上千 chunk 才必要。

## 边界与误用

- "wiki 编译"比"源码编译"宽松：LLM 的编译结果**不确定**且依赖模型质量。换模型重 ingest，wiki 结构可能漂移。
- 没有官方 Karpathy 实现——只有一个 Gist 作为蓝图，需要用户自己用 `agents.md` 把"如何命名页面 / 何时新建 entity vs 更新已有 / 如何记录矛盾"等规则写清楚。`agents.md` 质量直接决定 wiki 一致性。
- 当语料 > 几百文档，token 维护互联的成本会让 vector search 重新变得划算——文章明确指出这是 LLM wiki 与 RAG 的"切换点"。

## References

- "source code / executable" 类比：`data/raw/webpage/anthemcreation-en-guide/text.txt` 第 80 行。
- 三层定义：第 82-88 行。
- 规模阈值（10-100 文档 vs 上千 chunk）：第 144-148 行。
- agents.md 重要性 + 警告：第 114 行 + 第 152 行。

## Footnotes

- 类比原文："He describes the following analogy: raw sources are like source code, and the LLM wiki is the compiled executable. You don't recompile every time you run a program. The wiki remains canonical, alive, and improves with each new source ingested."（第 80 行）
- 个人规模优势："For wikis of 100 articles, structured markdown is more than sufficient. A vector database becomes useful only beyond a certain scale, where semantic search over thousands of chunks becomes necessary."（第 148 行）
- 模型质量警告："A weak model can propagate errors without flagging them. Plan for periodic human review of key pages, especially in the first weeks. The quality of your agents.md directly determines the base's reliability."（第 152 行）
