---
schema: accepted_card_provenance.v3
card: ../cards/wicer-recovery-distribution-exceeds-fc-raw.md
material_id: arxiv-wicer
digest_id: digest_arxiv-wicer
source_paths:
  - data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt
draft_card: ../../drafts/cards/wicer-recovery-distribution-exceeds-fc-raw.md
draft_provenance: ../../drafts/provenance/wicer-recovery-distribution-exceeds-fc-raw.md
similarity_result: ../../drafts/similarity/wicer-recovery-distribution-exceeds-fc-raw.json
comparison_provenance: ../../drafts/comparison/wicer-recovery-distribution-exceeds-fc-raw.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T14:30:00+08:00
  gate_notes: 6/6 通过；三个主题 101/116/125% recovery、entity-dense 主题最受益、local_education 反例均回到 Table tab:wicer 第 870–873 行与 §6.4 Analysis（L884–886）。
created_time: 2026-05-26T15:00:00+08:00
edited_time: 2026-05-27T14:30:00+08:00
edited_entity: llm
---

## 源证据

### 主表数据行（第 870–873 行）

```
news_stories           & 2.50 / 40.0\% & \textbf{3.61} / 11.2\% & 3.60 & 101\% & 2 \\
local_arts_\&_culture & 1.65 / 73.8\% & \textbf{3.61} / 15.0\% & 3.34 & 116\% & 2 \\
small_medium_ent.     & 2.21 / 56.2\% & \textbf{3.75} / 13.8\% & 3.44 & 125\% & 2 \\
```

### §6.4 Analysis（第 884–886 行）

> "Recovery rates span 0–125% across the 15 topics with FC raw baselines, with three topics (news_stories at 101%, local_arts_and_culture at 116%, small_and_medium_enterprises at 125%) exceeding FC raw quality after two iterations. Topics with many entity-specific facts benefit most in absolute terms (+1.96 for local_arts_and_culture, +1.54 for small_and_medium_enterprises)."

### local_education 反例（同段）

> "One topic (local_education_systems) shows no WiCER improvement; its relatively high blind baseline (2.41) and low score-1 rate (38.8%) leave fewer catastrophic failures to diagnose."

### lost-in-the-middle 解释（第 671–679 行）

> "full-context produces 17.0% score-1 answers (vs. 1.2% on Policygenius), and cross-referencing per-question scores reveals 557 cases across all 15 FC topics ... where FC scored 1 but RAG scored ≥4. In these cases, the model has all 80 documents in context but cannot locate the relevant passage."

## 卡片范围是否成立

本卡的范围聚焦在"recovery 分布"这一独立观察。它**不重复**已有四张卡：
- `wicer-cegar-compile-evaluate-refine` 覆盖算法骨架与 CEGAR 类比；
- `wicer-blind-compilation-catastrophic-loss` 覆盖盲编译失败的原因；
- `wicer-fc-rag-document-count-crossover` 覆盖 FC vs RAG 翻转；
- `wicer-targeted-vs-random-pinning-ablation` 覆盖诊断 vs 随机的 ablation。

本卡的全部数字与解释均直接来自 Table tab:wicer 和 §6.4 Analysis 段。"为什么会超过 FC raw"的因果推理（lost-in-the-middle + 压缩后注意力收益）是对论文已陈述事实的合成，论文未把这条机制写得这么直白，但其证据链（FC raw 17% score-1、entity-dense 主题最受益、超越发生在两次迭代后）都在原文。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T14:30:00+08:00
- 检查要点：
  - 非标题复述：正文展开 recovery 分布表、超越 FC raw 机制、单调失败反例、操作含义。
  - 知识密度：数字 + 机制 + 边界 + 操作建议。
  - 源支撑：source_ids 含 arxiv-wicer；Table tab:wicer 与 §6.4 verbatim。
  - References / Footnotes 齐备。
  - frontmatter 完整且合法。
  - related 已填充：6 张 WiCER / docs-as-code / Karpathy 相邻卡。

## 备注

与 v2 已有卡片可能的重叠：暂无已知的 v2 卡片覆盖"WiCER recovery 分布形态"——v2 阶段对 WiCER 的覆盖应该停留在算法本身。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/wicer-recovery-distribution-exceeds-fc-raw.md`
- draft provenance: `../../drafts/provenance/wicer-recovery-distribution-exceeds-fc-raw.md`
- similarity: `../../drafts/similarity/wicer-recovery-distribution-exceeds-fc-raw.json`
- comparison provenance: `../../drafts/comparison/wicer-recovery-distribution-exceeds-fc-raw.md`
