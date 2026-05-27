---
schema: accepted_card_provenance.v3
card: ../cards/karpathy-llm-wiki-vs-rag.md
material_id: marvin-hn-persistent-knowledge
digest_id: digest_marvin-hn-persistent-knowledge
source_paths:
  - data/raw/webpage/marvin-hn-persistent-knowledge/text.txt
draft_card: ../../drafts/cards/karpathy-llm-wiki-vs-rag.md
draft_provenance: ../../drafts/provenance/karpathy-llm-wiki-vs-rag.md
similarity_result: ../../drafts/similarity/karpathy-llm-wiki-vs-rag.json
comparison_provenance: ../../drafts/comparison/karpathy-llm-wiki-vs-rag.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T10:18:00+08:00
  gate_notes: 6/6 项通过：对比表 + compiled artifact 关键句 + 增量动作清单 + 边界。
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-27T10:18:00+08:00
edited_entity: llm
---

## 源证据

1. `data/raw/webpage/marvin-hn-persistent-knowledge/text.txt:23` —— HN 反响（274 / 89）与"start from a simple complaint about RAG"。
2. `text.txt:25` —— compiled artifact vs transient answer 的关键论断。
3. `text.txt:25` —— ingest 时应同时执行的增量动作清单。

## 卡片范围是否成立

- 卡片范围严格在"wiki vs RAG"这一区分维度展开，不涉及 three-layer architecture / Obsidian-as-IDE 等兄弟主题。
- "前 agent 时代 wiki 退化、RAG 兴起；agent 时代 wiki 复兴"是合理的归纳引申，源文章用"the LLM as a maintenance engine"角度暗示但未显式给出时间线，已在卡片以编辑评论形式标注。
- "文档规模 >10K 时 RAG 仍不可替代" 是借自 openaitoolshub 同源主题 FAQ 的合理引申，已在边界段标注。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T10:18:00+08:00
- 检查要点：
  - 非标题复述：以"区分对象 + 对比表 + 增量动作 + 时代成立条件 + 边界"五段实质展开。
  - 知识密度：5 行知识形态/价值对比 + 5 项 ingest 动作 + 时代切换论证。
  - 源支撑：marvin-hn-persistent-knowledge text:23 / text:25 锚定。
  - References / Footnotes 存在。
  - frontmatter 完整。
  - related 字段 7 个 v3 draft id。

## 备注

- 与 v2 卡 `auto-index-replaces-rag-at-small-scale` 主题强相关；comparison_provenance 阶段应明确两者关系（v2 偏定性，本卡偏 paradigm 区分）。
- 与 `knowledge-compounding-dynamic-roi` 互链：那张卡给定量证据，本卡给概念区分。
- Adoption 阶段观察：comparison 显示 v2 候选均为 Karpathy gist 事实卡，无 wiki-vs-RAG paradigm 区分卡，无 fusion 必要。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/karpathy-llm-wiki-vs-rag.md`
- draft provenance: `../../drafts/provenance/karpathy-llm-wiki-vs-rag.md`
- similarity: `../../drafts/similarity/karpathy-llm-wiki-vs-rag.json`
- comparison provenance: `../../drafts/comparison/karpathy-llm-wiki-vs-rag.md`
