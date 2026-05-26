---
schema: draft_card_provenance.v3
draft_card: ../cards/obsidian-as-ide-llm-as-programmer.md
material_id: marvin-hn-persistent-knowledge
digest_id: digest_marvin-hn-persistent-knowledge
source_paths:
  - data/raw/webpage/marvin-hn-persistent-knowledge/text.txt
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-26T11:00:00+08:00
edited_entity: llm
---

## 源证据

1. `data/raw/webpage/marvin-hn-persistent-knowledge/text.txt:35` —— "Karpathy explicitly describes Obsidian as the IDE, the LLM as the programmer, and the wiki as the codebase."
2. `text.txt:35` —— 类比命中的原因（重复 bookkeeping 同构）。
3. `text.txt:37` —— 模式的抽象性声明。

## 卡片范围是否成立

- 卡片专门讲"这个 analogy 到底承诺了什么、其工程含义、其边界"，与三层 / vs-RAG 兄弟卡职责分离。
- "wiki 没有等价 CI" 是基于类比函数对应限制的合理引申；marvin 原文未指出这一点，已隐式标注（属编辑性边界提醒）。
- "Obsidian 不是必需"借鉴 openaitoolshub 经验文章 FAQ 的明确共识。
- "LLM 当程序员假设其 markdown 写作能力达标"是对类比中"LLM"角色的合理工程化审视。

## 发表门控结果

本轮未运行。

## 备注

- 与 `karpathy-llm-wiki-three-layers` 和 `karpathy-llm-wiki-vs-rag` 共同构成"Karpathy gist 主题集合"，建议 comparison_provenance 阶段考虑做一个 synthesis 页。
