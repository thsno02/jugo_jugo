---
schema: draft_card_provenance.v3
draft_card: ../cards/auto-index-replaces-rag-at-small-scale.md
material_id: karpathy-x-launch-post
digest_id: digest_karpathy-x-launch-post
source_paths:
  - data/raw/webpage/karpathy-x-launch-post/text.txt
created_time: 2026-05-25T22:05:00+08:00
edited_time: 2026-05-26T09:30:00+08:00
edited_entity: llm
---

## 源证据

- 主要片段：`data/raw/webpage/karpathy-x-launch-post/text.txt`，JSON 指针 `$.tweet.quote.text`，"Q&A:" 章节：
  - 规模锚：`"once your wiki is big enough (e.g. mine on some recent research is ~100 articles and ~400K words)"`
  - 核心主张：`"I thought I had to reach for fancy RAG, but the LLM has been pretty good about auto-maintaining index files and brief summaries of all the documents and it reads all the important related data fairly easily at this ~small scale."`
- 支撑边界的片段：同一被引用推文中 "Further explorations:" 章节—— `"the natural desire is to also think about synthetic data generation + finetuning to have your LLM \"know\" the data in its weights instead of just context windows."`

## 卡片范围是否成立

卡片从源材料中提取出一条操作性规则：在 ~100 篇 / ~400K 词的规模下，索引 + 摘要的维护已经足够，没必要额外铺设 RAG 层。卡片保留了源材料的两层限定：

1. 规模限定（`~small scale`）——保留在卡片的"边界"段而不是被剥离。
2. 非普适限定——源材料把它呈现为个人经验，卡片对应地写明"不是在说 RAG 整体不必要"。

操作要点是对源材料描述的同义改写，不引入源材料没有提到的机制（例如混合检索、reranking）。

## 发表门控结果

本轮未运行。

## 备注

- 本卡片可能与 v2 卡片 "RAG 式文档问答不积累综合知识" 共享 token，但它从"语料规模"轴论证，而不是"知识合成"轴。comparison provenance 阶段需要在内容层面而不是 token 层面区分这两张卡片。
