---
schema: accepted_card_provenance.v3
card: ../cards/gragpoison-additive-vs-edit-attack.md
material_id: arxiv-graph-poisoning
digest_id: digest_arxiv-graph-poisoning
source_paths:
  - data/raw/arxiv/arxiv-graph-poisoning/agent_source_bundle.txt
draft_card: ../../drafts/cards/gragpoison-additive-vs-edit-attack.md
draft_provenance: ../../drafts/provenance/gragpoison-additive-vs-edit-attack.md
similarity_result: ../../drafts/similarity/gragpoison-additive-vs-edit-attack.json
comparison_provenance: ../../drafts/comparison/gragpoison-additive-vs-edit-attack.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T10:00:00+08:00
  gate_notes: 6/6 项通过：distinction 卡有真对比表与四类操作含义，引文锚定到 L193-205/L226-230/L749-757/L778-789，frontmatter 完整。
created_time: 2026-05-26T11:42:00+08:00
edited_time: 2026-05-27T10:00:00+08:00
edited_entity: llm
---

## 源证据

- L193–198：*"Recent work has taken the first step toward poisoning GraphRAG: GRAGPOISON~\cite{...} injects crafted chunks that create or amplify false relations, showing that such relation-level manipulation can mislead multiple queries once the graph is built. While GRAGPOISON demonstrates that GraphRAG can indeed be poisoned, its attack strategies all operate in an additive manner: it introduces malicious content into the corpus either by injecting new relations, repeating existing relations to strengthen them, or adding narrative chunks that blend false and true information."*
- L197–199：*"An unexplored question is whether GraphRAG is also vulnerable when the adversary cannot add new text, but is only able to make small, subtle modifications to the existing corpus."*
- L226–230：贡献列表中明确把"manipulation-only attack surface"列为第一条贡献：*"modifying a small number of words in the trusted corpus is sufficient to corrupt the constructed knowledge graph"*。
- L778–784：词量统计表 TKPA × {LP, FC08, JAPB}、UKPA × {LP, RUW} 的 min/avg 修改词量与修改比。
- L749–757：PF、LLMDet、SCC 对 TKPA / UKPA 的 Precision / Recall / F1 全部 ≤ 0.13。

## 卡片范围是否成立

本卡范围是"两类家族的对照"，不重做单个攻击的机制描述。每一行表格内容都来自上述源段落直接抽取（包括论文对 GRAGPOISON additive 策略的三种刻画）。"复合攻击未被研究"是论文未明确提及但可从两类的可叠加性推得的工程提示，已在边界栏注明为"论文未研究"。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T10:00:00+08:00
- 检查要点：
  - 非标题复述：以「两条家族对照」立论，表格 + 三段操作含义实质区分。
  - 知识密度：六维对照表 + 操作含义 + 边界与误读，三段以上 substantive 中文段落。
  - 源支撑：source_ids=[arxiv-graph-poisoning]，正文给出 GRAGPOISON 原文与 in-place edit 原话。
  - References / Footnotes 存在：含 L193-198 / L226-230 / L749-757 / L778-784 指针。
  - frontmatter 完整：id/title/card_type/tags/source_ids/provenance_card/created_time/edited_time/edited_entity 齐。
  - related 字段已填充：6 个 v3 draft 卡片 id。

## 备注

- 与 v2 卡片潜在重叠：若 v2 有 RAG 投毒分类卡，可能与本卡 scope 部分重叠；本卡的特殊价值在于专属 GraphRAG 的"加 vs 改"两条路线，比通用 RAG 投毒分类更细。
- 与同 material 的 `graphrag-manipulation-only-attack-surface` 互补：那张说"in-place edit 是新攻击面"，本卡说"它和 additive 是如何并列的不同家族"。
- Adoption 阶段观察：comparison 显示三个 v2 候选均为 Karpathy LLM-wiki 元描述，jaccard ≤ 0.08，shared token 仅「的」，无 fusion 必要。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/gragpoison-additive-vs-edit-attack.md`
- draft provenance: `../../drafts/provenance/gragpoison-additive-vs-edit-attack.md`
- similarity: `../../drafts/similarity/gragpoison-additive-vs-edit-attack.json`
- comparison provenance: `../../drafts/comparison/gragpoison-additive-vs-edit-attack.md`
