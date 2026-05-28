---
id: karpathy-llm-wiki-vs-rag
title: LLM Wiki 与 RAG 的根本区别：wiki 是会被复利的 compiled artifact，RAG 是 transient 答案
status: accepted
card_type: distinction
tags: [#karpathy-llm-wiki, #rag, #persistent-rag, #compounding]
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-28T11:19:00+08:00
edited_entity: llm
source_ids: [marvin-hn-persistent-knowledge]
provenance_card: ../provenance/karpathy-llm-wiki-vs-rag.md
aliases: [persistent rag, wiki vs RAG, compiled artifact]
related: [karpathy-llm-wiki-three-layers, obsidian-as-ide-llm-as-programmer, knowledge-compounding-dynamic-roi, karpathy-wiki-full-context-vs-rag, anthemcreation-llm-wiki-vs-rag-multi-hop, hn-llm-wiki-is-just-rag-debate, karpathy-llm-wiki-source-executable-analogy]
---

## 区分对象

Karpathy 的 LLM Wiki gist（2026-04-04 发布，HN 274 分 89 评论）[^src1]从一个**对 RAG 的不满**出发[^src2]：现有 document workflow 大多还停在 "RAG 模式"——上传文件、query 时检索 chunk、每次从零拼装答案。Karpathy 主张换一个**中间层**：让 LLM 在每次新源到达时**增量构建并维护**一个由互链 markdown 页面组成的持久 wiki。

## 两种范式的对比

| 维度 | RAG | LLM Wiki |
|---|---|---|
| 知识形态 | 原始文档 + 向量索引 | 已编译的互链 markdown 页 |
| query 时做什么 | 检索 chunk → 重新生成答案 | 直接读已编译的 page |
| 新源到达时做什么 | 加入索引 | 更新摘要 / 修订实体页 / 标矛盾 / 加 cross-link / 强化 synthesis |
| 答案性质 | transient（每次重生成） | compiled artifact（会被累积复用） |
| 价值随时间 | 与质问数量无关 | 单调累积 |

> "In that model, the wiki becomes a compiled artifact that keeps getting better over time rather than a transient answer assembled on demand."[^src3]

## 关键的"增量动作"

Karpathy gist 不是"用 LLM 写 wiki"，而是规定每次 ingest 时 agent **同时**做几件事：

1. 写 / 更新该源的主题摘要。
2. 修订相关 entity 页。
3. 显式 flag 与既有页面的矛盾（**不直接覆盖**）。
4. 加 cross-link。
5. 强化 running synthesis 页。

少做任何一项，wiki 都会从 "活的编译产物"退化为"另一个文档堆"。

## 为什么这种区分在 agent 时代成立

- 在前 agent 时代，wiki 维护成本高，人写不动 → wiki 退化 → 大家转向 RAG（让机器每次重生成）。
- LLM agent 把"维护成本"压到接近零[^v3-1] → wiki 可以被"实时"维护 → compiled artifact 成为可行选项 → RAG 的"重生成"反而显得浪费。

Karpathy 在 gist 里用"Obsidian 是 IDE，LLM 是程序员，wiki 是 codebase"的类比来强调这是**软件开发范式**的迁移而非"做笔记的小技巧"[^v3-2]。

## 边界

- 在文档规模极大（>10K）时，pre-compile 整张 wiki 不可行——RAG 仍然有不可替代的位置（见 openaitoolshub 经验文章 FAQ）。
- 在主题极度跳跃的 workflow 里，cross-link / synthesis 的复利收益弱，wiki 的相对优势不明显。

## Footnotes

[^src1]: `data/raw/webpage/marvin-hn-persistent-knowledge/text.txt:23` — "At crawl time, the Hacker News thread around the gist had 274 points and 89 comments, with readers treating it less as a note-taking trick and more as an architectural pattern for agent workflows."
[^src2]: 同文件 `text.txt:23` — "Andrej Karpathy's LLM Wiki, posted on April 4, 2026, starts from a simple complaint: most document workflows still look like RAG. You upload files, the model retrieves relevant chunks at query time, and then rebuilds the answer from scratch every time."
[^src3]: 同文件 `text.txt:25` — "In that model, the wiki becomes a compiled artifact that keeps getting better over time rather than a transient answer assembled on demand." 以及 ingest 时的"摘要 / 实体页 / 矛盾 flag / cross-link / synthesis"增量动作清单。
[^v3-1]: [karpathy-gist-bookkeeping-burden](karpathy-gist-bookkeeping-burden.md) — "维护成本压到接近零"的本卡。
[^v3-2]: [obsidian-as-ide-llm-as-programmer](obsidian-as-ide-llm-as-programmer.md) — Obsidian = IDE / LLM = 程序员 / wiki = codebase 类比的本卡。
