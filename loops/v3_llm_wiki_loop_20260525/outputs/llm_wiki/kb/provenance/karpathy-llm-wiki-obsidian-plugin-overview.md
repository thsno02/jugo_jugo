---
schema: accepted_card_provenance.v3
card: ../cards/karpathy-llm-wiki-obsidian-plugin-overview.md
material_id: obsidian-community-plugin
digest_id: digest_obsidian-community-plugin
source_paths:
  - data/raw/webpage/obsidian-community-plugin/text.txt
draft_card: ../../drafts/cards/karpathy-llm-wiki-obsidian-plugin-overview.md
draft_provenance: ../../drafts/provenance/karpathy-llm-wiki-obsidian-plugin-overview.md
similarity_result: ../../drafts/similarity/karpathy-llm-wiki-obsidian-plugin-overview.json
comparison_provenance: ../../drafts/comparison/karpathy-llm-wiki-obsidian-plugin-overview.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T10:16:00+08:00
  gate_notes: 6/6 项通过：插件元信息 + 架构 + 命令 + 提供商 + 选型 + 维护机制 + 平台与许可，全部锚定页面行号。
created_time: 2026-05-26T12:30:00+08:00
edited_time: 2026-05-27T10:16:00+08:00
edited_entity: llm
---

## 源证据

- 第 81–98 行：插件名、作者、官方分数 94/100、8 语言原生支持、~781 下载等元信息。
- 第 100–113 行（What is LLM-Wiki + 与 Karpathy 思想关系）。
- 第 196–212 行（命令面表 verbatim）。
- 第 256–305 行（知识质量与维护特性，含 Aliases、Duplicate detection tier、Smart Fix All、Contradiction state machine）。
- 第 343–370 行（模型选型表 verbatim）。
- 第 376–392 行（三层架构 ASCII + 文件结构）。
- 第 449 行（升级安全承诺）。

## 卡片范围是否成立

- 卡片以 example_pattern 类型给出"Karpathy 三层架构落地到 Obsidian 的完整概览"，含元信息、架构、命令、提供商、模型选型、维护机制——与页面的"产品介绍"层叙述对齐。
- 直接来自源：架构 ASCII、命令清单、模型表、特性清单、安全升级承诺。
- 引申点：未引入页面外主张。
- 切分理由：详细的 alias 机制、extraction granularity、full-context vs RAG 立场单独拆卡（同 batch），避免 overview 卡膨胀。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T10:16:00+08:00
- 检查要点：
  - 非标题复述：example_pattern 卡含 7 段产品级元描述。
  - 知识密度：架构 ASCII + 命令表 + 模型档位 + 维护机制 + 许可信息。
  - 源支撑：obsidian-community-plugin 行 81-449 多处锚点。
  - References / Footnotes 存在。
  - frontmatter 完整。
  - related 字段 7 个 v3 draft id。

## 备注

- 与 v2 `idea-file-as-agent-era-artifact` 概念相关，但本卡片专注于 Karpathy 思想的 Obsidian 实现落地。
- 与 batch 其它三张 Karpathy-wiki 子主题卡（aliases-and-dedup、full-context-vs-rag、extraction-granularity）形成 overview + 子主题集。
- Adoption 阶段观察：与 v2 `llm-wiki-three-layer-architecture` 共享"三层架构"概念但卡片类型不同（known_fact vs example_pattern），不可合并。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/karpathy-llm-wiki-obsidian-plugin-overview.md`
- draft provenance: `../../drafts/provenance/karpathy-llm-wiki-obsidian-plugin-overview.md`
- similarity: `../../drafts/similarity/karpathy-llm-wiki-obsidian-plugin-overview.json`
- comparison provenance: `../../drafts/comparison/karpathy-llm-wiki-obsidian-plugin-overview.md`
