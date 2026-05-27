---
schema: accepted_card_provenance.v3
card: ../cards/karpathy-wiki-aliases-and-dedup.md
material_id: obsidian-community-plugin
digest_id: digest_obsidian-community-plugin
source_paths:
  - data/raw/webpage/obsidian-community-plugin/text.txt
draft_card: ../../drafts/cards/karpathy-wiki-aliases-and-dedup.md
draft_provenance: ../../drafts/provenance/karpathy-wiki-aliases-and-dedup.md
similarity_result: ../../drafts/similarity/karpathy-wiki-aliases-and-dedup.json
comparison_provenance: ../../drafts/comparison/karpathy-wiki-aliases-and-dedup.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T10:19:00+08:00
  gate_notes: 6/6 项通过：强制别名 + Tier 1/2 机制 + 升级路径 + CoT/思维链实例。
created_time: 2026-05-26T12:35:00+08:00
edited_time: 2026-05-27T10:19:00+08:00
edited_entity: llm
---

## 源证据

- 第 262 行（Mandatory aliases verbatim）。
- 第 263 行（Duplicate Detection & Merge）：
  > "Semantic tiering catches true duplicates (cross-language translations, abbreviations, spelling variants); intelligent LLM merge fuses content and preserves aliases."
- 第 264 行（Smart Knowledge Fusion）：
  > "Multi-source updates merge new info without redundancy, contradictions preserved with attribution, reviewed: true pages protected from overwrite."
- 第 215–229 行（升级步骤）：Regenerate index → Lint → Complete Aliases → Merge Duplicates 的因果顺序。
- 第 277 行（Tier 1/Tier 2 verbatim）。
- 第 410–414 行（FAQ："missing aliases"、"CoT vs 思维链" 实例、"How does duplicate detection work"）。

## 卡片范围是否成立

- 卡片以 mechanism 类型记录 alias + dedup 的工程承诺，与页面 FAQ + 特性段共同呈现的"alias 是 dedup 的前置条件"叙述对齐。
- 直接来自源：mandatory aliases、Tier 1/2 分层、merge 保留双方别名、升级因果顺序、CoT vs 思维链实例。
- 引申点：与 mem0 DELETE、memory-as-metabolism minority retention 的对比是跨材料综合，未对 plugin 本身引入新主张。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T10:19:00+08:00
- 检查要点：
  - 非标题复述：以"问题 → 两层结构 → 与其它 dedup 思想的对比 → 关键设计 → 升级路径"五段实质展开。
  - 知识密度：mandatory aliases + Tier 1/2 + Merge Duplicates + 升级因果序。
  - 源支撑：obsidian-community-plugin 行 262-264 / 215-229 / 277 / 410-414。
  - References / Footnotes 存在。
  - frontmatter 完整。
  - related 字段 5 个 v3 draft id。

## 备注

- 与 `karpathy-llm-wiki-obsidian-plugin-overview` 是 zoom-in 关系，避免 overview 卡承担细节负担。
- v2 卡片中无对应 alias/dedup 卡，无重叠。
- Adoption 阶段观察：与 v2 同源 Karpathy 主题但 v2 覆盖的是 gist 概念层，插件实现层在 v2 完全空缺。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/karpathy-wiki-aliases-and-dedup.md`
- draft provenance: `../../drafts/provenance/karpathy-wiki-aliases-and-dedup.md`
- similarity: `../../drafts/similarity/karpathy-wiki-aliases-and-dedup.json`
- comparison provenance: `../../drafts/comparison/karpathy-wiki-aliases-and-dedup.md`
