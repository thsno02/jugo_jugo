---
schema: draft_card_provenance.v3
draft_card: ../cards/etamp-chaos-monkey-agent-robustness.md
material_id: arxiv-etamp-memory-poisoning
digest_id: digest_arxiv-etamp-memory-poisoning
source_paths:
  - data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-26T11:00:00+08:00
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

本轮未运行。

## 备注

- 本卡更偏 operational_rule（"评测协议指引"），可在 comparison_provenance 阶段考虑是否应纳入 v3 的 "agent evaluation methodology" 索引页。
