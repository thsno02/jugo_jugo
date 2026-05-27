---
schema: accepted_card_provenance.v3
card: ../cards/poisonedrag-baselines-isolate-two-conditions.md
material_id: arxiv-poisonedrag
digest_id: digest_arxiv-poisonedrag
source_paths:
  - data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt
draft_card: ../../drafts/cards/poisonedrag-baselines-isolate-two-conditions.md
draft_provenance: ../../drafts/provenance/poisonedrag-baselines-isolate-two-conditions.md
similarity_result: ../../drafts/similarity/poisonedrag-baselines-isolate-two-conditions.json
comparison_provenance: ../../drafts/comparison/poisonedrag-baselines-isolate-two-conditions.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T15:26:00+08:00
  gate_notes: 6/6 项通过；五基线-两条件消融逻辑严密，行号 verbatim。
created_time: 2026-05-26T11:46:00+08:00
edited_time: 2026-05-27T15:26:00+08:00
edited_entity: llm
---

## 源证据

- L1221–1244：*"Naive Attack ... If we view $Q$ as the malicious text, it will likely be retrieved. We compare with this attack to demonstrate that the generation condition is necessary ..."*；*"Corpus Poisoning Attack ... this attack is similar to PoisonedRAG (white-box) when PoisonedRAG uses $S$ alone as the malicious text"*；*"GCG Attack ... we view the optimized adversarial text as a malicious text and inject it into the knowledge database. Our results show that GCG achieves a very low ASR ... The reason is that it cannot achieve the retrieval condition."*；*"Disinformation Attack ... we view the crafted $I$ as a malicious text, i.e., $P=I$. This baseline can be viewed as a variant of PoisonedRAG."*
- L1332–1354：基线表 ASR / F1（NQ / HotpotQA / MS-MARCO）。
- L1403–1404：*"those baselines are not designed to simultaneously achieve retrieval and generation conditions, resulting in sub-optimal performance."*
- L110–151：附录中把 GCG 适配到 RAG 的具体例子——明确把 context 初始化为 40 个 "!"，优化目标是让 LLM 输出 target answer，**没有 retrieval 项**。

## 卡片范围是否成立

本卡是"distinction"型，专门聚焦 5 个基线如何分别证伪两条件之一，所有 ASR / F1 数字、每个基线为什么失败的解释都来自论文 §"Compared baselines" 与 §"Main Results" 的对应段落。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T15:26:00+08:00
- 检查要点：
  - 表格 + 工程含义 + 边界 + 误读，substantive。
  - 知识密度高；非标题复述。
  - 源支撑：4 段 verbatim + 行号。
  - References + Footnotes 双在；Footnotes 5 条 verbatim。
  - frontmatter 完整；related 含 6 张邻接卡。

## 备注

- 与 `poisonedrag-retrieval-generation-two-conditions` 紧密配对：正向机制 vs 反证。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/poisonedrag-baselines-isolate-two-conditions.md`
- draft provenance: `../../drafts/provenance/poisonedrag-baselines-isolate-two-conditions.md`
- similarity: `../../drafts/similarity/poisonedrag-baselines-isolate-two-conditions.json`
- comparison provenance: `../../drafts/comparison/poisonedrag-baselines-isolate-two-conditions.md`
