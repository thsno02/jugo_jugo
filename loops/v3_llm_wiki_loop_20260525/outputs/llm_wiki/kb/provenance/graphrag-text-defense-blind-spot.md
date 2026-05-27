---
schema: accepted_card_provenance.v3
card: ../cards/graphrag-text-defense-blind-spot.md
material_id: arxiv-graph-poisoning
digest_id: digest_arxiv-graph-poisoning
source_paths:
  - data/raw/arxiv/arxiv-graph-poisoning/agent_source_bundle.txt
draft_card: ../../drafts/cards/graphrag-text-defense-blind-spot.md
draft_provenance: ../../drafts/provenance/graphrag-text-defense-blind-spot.md
similarity_result: ../../drafts/similarity/graphrag-text-defense-blind-spot.json
comparison_provenance: ../../drafts/comparison/graphrag-text-defense-blind-spot.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T10:09:00+08:00
  gate_notes: 6/6 项通过：F1 0.04-0.13 表 + 按攻击类型的失败解释 + 操作含义 + 边界，证据锚定 L731-757 / L706-712。
created_time: 2026-05-26T11:15:00+08:00
edited_time: 2026-05-27T10:09:00+08:00
edited_entity: llm
---

## 源证据

- 防御失效总结（L731）：*"existing defenses are largely ineffective against both TKPA and UKPA, with F1-scores close to 0."*
- TKPA 隐蔽性解释（L733–735）：*"the manipulations are guided by graph structure: selected chunks are rewritten by advanced LLMs so that the style, fluency, and local semantics remain natural."*
- UKPA 隐蔽性解释（L735–737）：*"Breaking these signals leaves the sentence-level meaning intact but causes long-range fragmentation in the knowledge graph."*
- Query-side 防御无效（L738–740）：见 References。
- 防御对照表（L749–757）：PF F1 0.07 / 0.04，LLMDet F1 0.13 / 0.11，SCC F1 0.07。
- PPL Ratio 在被注释的旧表（L706–712）：TKPA 1.15–1.21，Naive Swap 5.12+。

## 卡片范围是否成立

- 卡片把"防御失败"作为独立 source_claim 抽取，原因是它具有可立即指导工程的含义（不要只靠 PPL 与 LLMDet），且与攻击机制卡正交。
- 直接来自源材料：F1 数字、TKPA / UKPA 失败原因、query-side 无效论证。
- 引申主张已显式标注：建议把防御前移到构图阶段、对比图差 / 实体集差——论文未明文给出方案，但与其结论方向一致，仅作"操作含义"放在边界段。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T10:09:00+08:00
- 检查要点：
  - 非标题复述：以"按攻击类型分别看失明原因 → 两个操作含义 → 边界"三段实质展开。
  - 知识密度：F1 0.04-0.13 区间 + PPL Ratio 比较 + query-side 无效证明。
  - 源支撑：L731-757 / L706-712 多锚点。
  - References / Footnotes 存在。
  - frontmatter 完整。
  - related 字段 6 个 v3 draft id。

## 备注

- 与同批 TKPA / UKPA 卡形成"攻击–防御对照"组。
- Adoption 阶段观察：comparison 三个 v2 候选 score 0.000，全部为 Karpathy llm-wiki 推文，与 RAG 防御主题无交集。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/graphrag-text-defense-blind-spot.md`
- draft provenance: `../../drafts/provenance/graphrag-text-defense-blind-spot.md`
- similarity: `../../drafts/similarity/graphrag-text-defense-blind-spot.json`
- comparison provenance: `../../drafts/comparison/graphrag-text-defense-blind-spot.md`
