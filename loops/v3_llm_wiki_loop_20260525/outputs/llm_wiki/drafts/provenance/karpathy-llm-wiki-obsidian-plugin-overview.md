---
schema: draft_card_provenance.v3
draft_card: ../cards/karpathy-llm-wiki-obsidian-plugin-overview.md
material_id: obsidian-community-plugin
digest_id: digest_obsidian-community-plugin
source_paths:
  - data/raw/webpage/obsidian-community-plugin/text.txt
created_time: 2026-05-26T12:30:00+08:00
edited_time: 2026-05-26T12:30:00+08:00
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

本轮未运行。

## 备注

- 与 v2 `idea-file-as-agent-era-artifact` 概念相关（都把 markdown 作为 agent-era artifact），但本卡片专注于 Karpathy 思想的 Obsidian 实现落地——comparison 阶段可建立 cross-link。
- 与 batch 其它三张 Karpathy-wiki 子主题卡（aliases-and-dedup、full-context-vs-rag、extraction-granularity）形成 overview + 子主题集。
