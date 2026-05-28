---
id: karpathy-wiki-extraction-granularity
title: 五档抽取粒度（Minimal / Coarse / Standard / Fine / Custom）：把成本与深度变成可调的旋钮
status: accepted
card_type: operational_rule
tags: [#karpathy-wiki, #extraction, #cost-control, #knobs]
created_time: 2026-05-26T12:45:00+08:00
edited_time: 2026-05-28T11:24:00+08:00
edited_entity: llm
source_ids: [obsidian-community-plugin]
provenance_card: ../provenance/karpathy-wiki-extraction-granularity.md
aliases: [extraction granularity, Minimal/Coarse/Standard/Fine/Custom, ingestion budget knob]
related: [karpathy-llm-wiki-obsidian-plugin-overview, karpathy-wiki-full-context-vs-rag, karpathy-wiki-aliases-and-dedup, hn-source-granularity-changes-synthesis-quality, robin-cartier-scale-ceiling, anthemcreation-llm-wiki-setup-cost-envelope]
---

## 五档定义

Karpathy LLM Wiki 插件[^v3-1]在 `Settings → Wiki Output / Extraction` 中提供五档抽取粒度（v1.6.2 引入，v1.10.0 扩展），控制 LLM 从单一源中**抽出的实体/概念条目数量**[^src1]：

| 档位 | 约束 | 典型条目数 | 推荐场景 |
| --- | --- | --- | --- |
| **Fine** | 深度分析，包含边缘提及 | ~100 | 关键源、值得深挖的文档 |
| **Standard** | 平衡抽取，日常默认 | ~50 | 日常笔记 |
| **Coarse** | 快速概览、核心实体 | ~10 | 大文件夹批处理、成本敏感场景 |
| **Minimal** | 仅留必要项 | ~5 | 100+ 文件批处理 / 新源试水 |
| **Custom** | 用户定义 1–300 | 自由 | 特殊工作流 |

## 设计动机

- **Token 成本可控**：Fine 每文档约 100 个 LLM 子任务（实体/概念页生成），Minimal 大约 5 个，差 20 倍。Standard / Coarse 是大多数日常使用的 sweet spot；
- **wiki 体积可控**：直接影响 wiki 长大的速度，间接影响 query 时的全 wiki context 是否仍然装得下长上下文模型；
- **试水成本低**：用户在新源上可以先 Minimal，再决定是否升 Standard / Fine。

页面建议：**Minimal / Coarse 适合大文件夹**，**Fine 选择性用于关键文档**——这是一个明确的"按价值分档"使用模式[^src2]。

## 与其它"成本旋钮"的配合

插件页面在 "Performance & Cost" 与 "How do I speed up ingestion" FAQ 中把抽取粒度与另外两个旋钮联动：

1. **Page Generation Concurrency**（1–5，默认 3）：每秒并发生成多少个实体/概念页。配合 Fine 档时建议提到 3–5；配合 Minimal 时其实无所谓。
2. **Batch Delay**（默认 300ms；起 100ms，建议 500–800ms 抗限流）：批之间的间隔。Standard 以下档位下可放小。
3. **Smart Batch Skip**（v1.7.7+）：自动跳过已处理文件，与粒度选择正交。

三个旋钮一起构成"**深度 × 并发 × 节奏**"的成本曲面，让 ingestion 在 API 费用、限流概率、wiki 增长速度之间取得平衡。

## 反对模式（容易踩的坑）

- **整个 vault 用 Fine 跑一次**：直接打爆 API 配额且产生大量边缘条目（被 lint 标为 orphans / 死链），后续 Smart Fix All 还要再花更多调用——典型的"过度抽取"陷阱。
- **Custom 设为 300**：除非确知文档值得，否则会让 wiki 出现大量低质量页，反过来损害去重和 lint 性能。
- **Minimal 用在分析型文档**：会错过关键实体，未来检索找不到。

## References

- 来源页面：`data/raw/webpage/obsidian-community-plugin/text.txt`。
- 第 240–250 行：五档定义与典型条目数 + 推荐场景。
- 第 230–238 行：升级后启用并发与 Batch Delay 的指引（v1.7.3+）。
- 第 419–432 行：FAQ "How do I speed up ingestion" / "How do I control API costs"。

## Footnotes

[^1]: 五档及典型条目数 verbatim（第 241–249 行）："Fine (~100 items) — Deep analysis, edge-case mentions included. High token cost, best for key sources. Standard (~50 items) — Balanced extraction. Good default for daily notes. Coarse (~10 items) — Quick overview, core entities only. Low cost, fast ingestion. Minimal (~5 items) — Essential items only. Ideal for batch processing 100+ files or testing new sources. Custom (1–300 items) — User-defined entity/concept limits for specialized workflows."

[^2]: 按价值分档使用 verbatim（第 250 行）："Recommendation: Use Minimal or Coarse for large folders to save time and API costs. Use Fine selectively on key documents that warrant deep analysis."

[^3]: 三旋钮配合 verbatim（第 420 行）："In Settings → Ingestion Acceleration: increase Page Generation Concurrency to 3–5 (parallel page creation), lower Batch Delay to 100–300ms (watch for rate limits). Choose 'Minimal', 'Coarse', or 'Standard' Extraction Granularity to reduce page count and save API costs."
