---
schema: accepted_card_provenance.v3
card: ../cards/etamp-chaos-monkey-agent-robustness.md
material_id: arxiv-etamp-memory-poisoning
digest_id: digest_arxiv-etamp-memory-poisoning
source_paths:
  - data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt
draft_card: ../../drafts/cards/etamp-chaos-monkey-agent-robustness.md
draft_provenance: ../../drafts/provenance/etamp-chaos-monkey-agent-robustness.md
similarity_result: ../../drafts/similarity/etamp-chaos-monkey-agent-robustness.json
comparison_provenance: ../../drafts/comparison/etamp-chaos-monkey-agent-robustness.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T14:52:00+08:00
  gate_notes: 6/6 通过；三类扰动定义 + 默认参数 + 步数补偿 + Netflix 类比全部锁到原文行号；评测建议段已 hedge 标注。
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-27T14:52:00+08:00
edited_entity: llm
---

## 源证据

1. `agent_source_bundle.txt:103` —— "Inspired by chaos engineering principles that test system resilience through controlled failure injection, we introduce Chaos Monkey to study whether such stress creates a 'frustration window'..."
2. `agent_source_bundle.txt:191` —— Section 2.3 标题 "Chaos Monkey"。
3. `agent_source_bundle.txt:196-202` —— 三类扰动定义。
4. `agent_source_bundle.txt:204` —— 默认参数与步数补偿规则。

## 卡片范围是否成立

- 卡片范围严格限定在"Chaos Monkey 的方法学定义 + 设计意图 + 给评测者的操作含义"，避免与 frustration-exploitation 卡（讲发现 / 数据）重叠。
- "把 Chaos Monkey 作为标配第二档" 是合理的评测建议引申，论文本身没写"应该 mandatory"，已标注。
- "三个 p 参数应作为评测协议参数公开" 是基于可比性的合理评测协议建议；论文没明确呼吁，但其透明披露参数本身蕴含此意图。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T14:52:00+08:00
- 检查要点：
  - 不是标题复述：三类扰动 + 设计 rationale + 不是什么 + 操作含义。
  - 知识密度足够：定义 + 参数 + 机制 + 评测建议。
  - 源支撑齐全：每条主张锁到 `agent_source_bundle.txt` 行号。
  - References 与 Footnotes 双章节存在。
  - frontmatter 完整合法，operational_rule 类型与正文一致。
  - related 已链 eTAMP 系列、ares-mock、owasp。

## 备注

- 本卡更偏 operational_rule（"评测协议指引"），可在未来纳入 v3 的 "agent evaluation methodology" 索引页。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/etamp-chaos-monkey-agent-robustness.md`
- draft provenance: `../../drafts/provenance/etamp-chaos-monkey-agent-robustness.md`
- similarity: `../../drafts/similarity/etamp-chaos-monkey-agent-robustness.json`
- comparison provenance: `../../drafts/comparison/etamp-chaos-monkey-agent-robustness.md`
