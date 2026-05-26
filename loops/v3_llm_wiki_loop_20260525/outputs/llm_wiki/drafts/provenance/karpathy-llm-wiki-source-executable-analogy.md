---
schema: draft_card_provenance.v3
draft_card: ../cards/karpathy-llm-wiki-source-executable-analogy.md
material_id: anthemcreation-en-guide
digest_id: digest_anthemcreation-en-guide
source_paths:
  - data/raw/webpage/anthemcreation-en-guide/text.txt
created_time: 2026-05-26T15:00:00+08:00
edited_time: 2026-05-26T15:00:00+08:00
edited_entity: llm
---

## 源证据

- 第 29-30 行：Karpathy 4 月发布 Gist，自用 wiki > 100 篇 / 400000 字。
- 第 80 行："raw sources are like source code, and the LLM wiki is the compiled executable" 完整类比段。
- 第 82-88 行：三层（immutable raw sources / LLM-managed wiki / agents.md instruction file）。
- 第 142-148 行：LLM wiki vs RAG 对比 + 个人规模 (10-100 文档) 优势 + 上千 chunk 时 vector search 才必要。
- 第 114 行（Tip）+ 第 152 行（Warning）：agents.md 规则与模型质量风险。

## 卡片范围是否成立

- "source / executable"类比、规模阈值、agents.md 角色全部出自页面原文。
- 对比表是对页面内多段比较的归纳（speed、reasoning depth、scale），仍在源材料覆盖范围。
- "wiki 编译比源码编译宽松"是合理引申——页面明确指出 LLM 输出依赖模型，多次 ingest 不保证一致。

## 发表门控结果

本轮未运行。

## 备注

- 与 my-llm-wiki-three-layer-implementation 卡可能在"三层结构"上有概念重叠——本卡的重点是"source/executable 类比"和"与 RAG 的对比"，my-llm-wiki 卡的重点是"工具落地"，互补不冲突。
- comparison_provenance 阶段可考察是否要新增一张"LLM wiki vs RAG 在不同规模的切换"卡。
