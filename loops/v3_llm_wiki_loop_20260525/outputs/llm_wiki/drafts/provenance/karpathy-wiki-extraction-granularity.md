---
schema: draft_card_provenance.v3
draft_card: ../cards/karpathy-wiki-extraction-granularity.md
material_id: obsidian-community-plugin
digest_id: digest_obsidian-community-plugin
source_paths:
  - data/raw/webpage/obsidian-community-plugin/text.txt
created_time: 2026-05-26T12:45:00+08:00
edited_time: 2026-05-26T12:45:00+08:00
edited_entity: llm
---

## 源证据

- 第 240–250 行（五档定义 verbatim 块 + 推荐场景）。
- 第 230–238 行（升级后并发与 Batch Delay 配置）。
- 第 254 行（Smart Batch Skip v1.7.7+ 自动跳过已处理文件）。
- 第 419–432 行（FAQ "How do I speed up ingestion" / "How do I control API costs"）。

## 卡片范围是否成立

- 卡片以 operational_rule 类型记录"五档 + 三旋钮"的实际配置规则，与页面在 Performance & Cost 一节的核心建议一致。
- 直接来自源：五档典型条目数、按价值分档建议、并发 + Batch Delay + Smart Batch Skip 三旋钮的联动。
- 引申点：
  - "反对模式" 一节是把"value-first strategy" 反过来叙述的提醒，仍在页面立场范围内；
  - "成本曲面"措辞是结构化概括，未引入页面外主张。

## 发表门控结果

本轮未运行。

## 备注

- 与 `karpathy-wiki-full-context-vs-rag` 配合：抽取粒度直接决定 wiki 体积，进而影响"全 wiki context"是否仍能装入长上下文模型。
- v2 卡片中无对应 knob 卡，无重叠。
