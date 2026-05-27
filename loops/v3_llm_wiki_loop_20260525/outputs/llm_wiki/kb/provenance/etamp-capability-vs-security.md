---
schema: accepted_card_provenance.v3
card: ../cards/etamp-capability-vs-security.md
material_id: arxiv-etamp-memory-poisoning
digest_id: digest_arxiv-etamp-memory-poisoning
source_paths:
  - data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt
draft_card: ../../drafts/cards/etamp-capability-vs-security.md
draft_provenance: ../../drafts/provenance/etamp-capability-vs-security.md
similarity_result: ../../drafts/similarity/etamp-capability-vs-security.json
comparison_provenance: ../../drafts/comparison/etamp-capability-vs-security.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T14:50:00+08:00
  gate_notes: 6/6 通过；GPT-5.2 22.3% vs mini 2.5% vs Qwen3.5 0.0% 三组对照 + abstract 引述 + Table 1 行号定位完整；ASR ≠ final harm 的方法学边界标明。
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-27T14:50:00+08:00
edited_entity: llm
---

## 源证据

1. `agent_source_bundle.txt:88` —— "Notably, more capable models are not more secure. GPT-5.2 shows substantial vulnerability despite superior task performance."
2. `agent_source_bundle.txt:243-265` —— Table 1 数字：GPT-5.2 Authority=22.3、GPT-5-mini Authority=2.5、Qwen3.5-122B Authority=0.0。
3. `agent_source_bundle.txt:243` —— "Surprisingly, GPT5.2 is highly vulnerable to authority framing attack, whereas GPT5-mini and Qwen3.5-122B are not."
4. `agent_source_bundle.txt:271` —— Qwen 鲁棒性不是因为长上下文 recall 不足。

## 卡片范围是否成立

- 卡片范围只覆盖"能力 ≠ 安全"的反直觉结论，与 frustration / payload 卡职责分离。
- "GPT-5.2 → GPT-5-mini 升级可能是 regression" 是基于 Table 1 数字的合理读取（GPT-5.2 在某些列上 ASR 更高）。
- "Qwen3.5-122B 同时高 TSR 低 ASR 说明对齐路径可以避免 trade-off" 是合理的归因引申；其他可能解释（如 Qwen 训练数据分布）未被论文实验排除，已隐含在"对齐路径"措辞中。
- ASR 不等于 final harm 是合理的方法学保留。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T14:50:00+08:00
- 检查要点：
  - 不是标题复述：三组对照 + 区分对象 + 三条操作含义 + 边界。
  - 知识密度足够：数字 + 反例 + 操作规则 + 方法学保留。
  - 源支撑齐全：每个数字锁到 Table 1 / abstract 行号。
  - References 与 Footnotes 双章节存在。
  - frontmatter 完整合法，distinction 类型与正文一致。
  - related 已链 eTAMP 系列、owasp、nist。

## 备注

- 本卡的"区分"维度可与 v3 未来的 "evaluation methodology" 概念页互链。
- v2 KB 当前完全无 agent security 主题。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/etamp-capability-vs-security.md`
- draft provenance: `../../drafts/provenance/etamp-capability-vs-security.md`
- similarity: `../../drafts/similarity/etamp-capability-vs-security.json`
- comparison provenance: `../../drafts/comparison/etamp-capability-vs-security.md`
