---
schema: accepted_card_provenance.v3
card: ../cards/karpathy-gist-memex-connection.md
material_id: karpathy-gist-llm-wiki
digest_id: digest_karpathy-gist-llm-wiki
source_paths:
  - data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt
draft_card: ../../drafts/cards/karpathy-gist-memex-connection.md
draft_provenance: ../../drafts/provenance/karpathy-gist-memex-connection.md
similarity_result: ../../drafts/similarity/karpathy-gist-memex-connection.json
comparison_provenance: ../../drafts/comparison/karpathy-gist-memex-connection.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T10:14:00+08:00
  gate_notes: 6/6 项通过：Memex 原文段 + Bush 未解决问题论证 + 评估锚点 + 边界，证据锚 gist 行 70。
created_time: 2026-05-26T11:55:00+08:00
edited_time: 2026-05-27T10:14:00+08:00
edited_entity: llm
---

## 源证据

- 行 70 完整段："The idea is related in spirit to Vannevar Bush's Memex (1945) — a personal, curated knowledge store with associative trails between documents. Bush's vision was closer to this than to what the web became: private, actively curated, with the connections between documents as valuable as the documents themselves. The part he couldn't solve was who does the maintenance. The LLM handles that."

## 卡片范围是否成立

本卡只覆盖"LLM Wiki ↔ Memex"这一历史性的源主张，独立成立，不与三层架构卡或 bookkeeping 卡重复。所有 Memex 内容来自 gist 原文。"任何不解决维护的工具都复刻 Memex 失败"是把 gist 的逻辑显式化为评估标准，属于 source_claim 的合理引申。"Memex 还有其它设想 / LLM Wiki 不必匹配技术细节"是 boundary 声明，不依赖原文以外的考据，仅用作不夸大边界。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T10:14:00+08:00
- 检查要点：
  - 非标题复述：以 Memex 原始设想 + Bush 未解决问题 + LLM Wiki 填补 + 评估锚点 + 边界五段实质展开。
  - 知识密度：1945 历史背景 + associative trails 原文 + "who does the maintenance" 评估锚点。
  - 源支撑：gist 行 70。
  - References / Footnotes 存在。
  - frontmatter 完整。
  - related 字段 4 个 v3 draft id。

## 备注

- 这张卡偏概念史叙事，适合作为"Why this matters"的引子页；具体技术细节交给三层架构 / bookkeeping 卡。
- Adoption 阶段观察：v2 candidates 都是架构内部机制卡，不触及 Memex 类比与"谁来维护"的历史命题；本卡是知识管理史长时间线的升维定位。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/karpathy-gist-memex-connection.md`
- draft provenance: `../../drafts/provenance/karpathy-gist-memex-connection.md`
- similarity: `../../drafts/similarity/karpathy-gist-memex-connection.json`
- comparison provenance: `../../drafts/comparison/karpathy-gist-memex-connection.md`
