---
schema: accepted_card_provenance.v3
card: ../cards/obsidian-as-ide-llm-as-programmer.md
material_id: marvin-hn-persistent-knowledge
digest_id: digest_marvin-hn-persistent-knowledge
source_paths:
  - data/raw/webpage/marvin-hn-persistent-knowledge/text.txt
draft_card: ../../drafts/cards/obsidian-as-ide-llm-as-programmer.md
draft_provenance: ../../drafts/provenance/obsidian-as-ide-llm-as-programmer.md
similarity_result: ../../drafts/similarity/obsidian-as-ide-llm-as-programmer.json
comparison_provenance: ../../drafts/comparison/obsidian-as-ide-llm-as-programmer.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T15:16:00+08:00
  gate_notes: 6/6 项通过；类比承诺三条 + 边界提醒清晰，源行号准确。
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-27T15:16:00+08:00
edited_entity: llm
---

## 源证据

1. `data/raw/webpage/marvin-hn-persistent-knowledge/text.txt:35` —— "Karpathy explicitly describes Obsidian as the IDE, the LLM as the programmer, and the wiki as the codebase."
2. `text.txt:35` —— 类比命中的原因（重复 bookkeeping 同构）。
3. `text.txt:37` —— 模式的抽象性声明。

## 卡片范围是否成立

- 卡片专门讲"这个 analogy 到底承诺了什么、其工程含义、其边界"，与三层 / vs-RAG 兄弟卡职责分离。
- "wiki 没有等价 CI" 是基于类比函数对应限制的合理引申；marvin 原文未指出这一点，已隐式标注。
- "Obsidian 不是必需"借鉴 openaitoolshub 经验文章 FAQ 的明确共识。
- "LLM 当程序员假设其 markdown 写作能力达标"是对类比中"LLM"角色的合理工程化审视。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T15:16:00+08:00
- 检查要点：
  - 类比 + 三承诺 + 命中分析 + 边界 + 操作含义 5 节。
  - 知识密度足；非标题复述。
  - 源支撑：text.txt:35 / 37 verbatim 引用。
  - References + Footnotes 双在；Footnotes 3 条 verbatim。
  - frontmatter 完整；related 含 6 张邻接卡。

## 备注

- 与 `karpathy-llm-wiki-three-layers` 和 `karpathy-llm-wiki-vs-rag` 共同构成"Karpathy gist 主题集合"。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/obsidian-as-ide-llm-as-programmer.md`
- draft provenance: `../../drafts/provenance/obsidian-as-ide-llm-as-programmer.md`
- similarity: `../../drafts/similarity/obsidian-as-ide-llm-as-programmer.json`
- comparison provenance: `../../drafts/comparison/obsidian-as-ide-llm-as-programmer.md`
