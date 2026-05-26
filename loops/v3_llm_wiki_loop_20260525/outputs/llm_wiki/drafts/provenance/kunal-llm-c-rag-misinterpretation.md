---
schema: draft_card_provenance.v3
draft_card: ../cards/kunal-llm-c-rag-misinterpretation.md
material_id: kunal-local-knowledge-base
digest_id: digest_kunal-local-knowledge-base
source_paths:
  - data/raw/webpage/kunal-local-knowledge-base/text.txt
created_time: 2026-05-26T12:10:00+08:00
edited_time: 2026-05-26T12:10:00+08:00
edited_entity: llm
---

## 源证据

- 行 48："Andrej Karpathy's open-source project makes this possible with a minimalist C-based setup"——文章开头把 Karpathy LLM Wiki 等同于 llm.c 本地实现。
- 行 60："Karpathy's approach with llm.c is intentionally minimalist: pure C/CUDA, no external dependencies, no Python packaging nightmares."
- 行 70–76：三阶段 RAG 描述（Ingestion / Embedding / Generation；chunks 256–512 tokens；cosine 相似度 top-K）。
- 行 173–195：FAQ 把 LLM Wiki = llm.c 项目，等同于本地 RAG 系统。
- 行 115："the local wiki wins for one specific use case ... For everything else, I'll be honest — Obsidian with a good plugin is more practical today."
- 行 137：作者自评最大收益是构建 RAG 流水线的过程本身。

## 卡片范围是否成立

本卡是一张 distinction 卡，核心范围是"标注'LLM Wiki'一词在 Kunal 文章中的解读与 Karpathy gist 解读之间的差异"。Kunal 解读的所有内容来自其原文。"Karpathy gist 实际定义"用来对照，依据另一材料（karpathy-gist-llm-wiki）——只在 boundary 标注中提及，不引用其逐字内容；这是合理的横向对照，因为 distinction 卡的本质就是显式两个概念的差别。"SEO 与术语污染"是 distinction 引申，未声称为 Kunal 文章主张，属于本卡的解读层。

## 发表门控结果

本轮未运行。

## 备注

- 这张卡是本批次里典型的 "防混淆" 卡，wiki 在写主题页时若不显式区分两种"LLM Wiki"会让读者误以为 Karpathy 的 wiki 模式就是 llm.c 本地 RAG。
- 与 karpathy-gist-three-layers / karpathy-gist-bookkeeping-burden 一起组成"LLM Wiki 真实定义 + 常见误读"二联视图。
