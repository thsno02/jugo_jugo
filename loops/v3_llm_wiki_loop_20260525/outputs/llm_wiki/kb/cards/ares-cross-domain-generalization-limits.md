---
id: ares-cross-domain-generalization-limits
title: ARES 跨域可迁移：query/document 类型可变，但语言/代码/抽取跨域会塌
status: accepted
card_type: distinction
tags: [#rag, #ares, #cross-domain, #generalization, #llm-judge]
created_time: 2026-05-26T15:30:00+08:00
edited_time: 2026-05-28T15:30:00+08:00
edited_entity: llm
source_ids: [arxiv-ares]
provenance_card: ../provenance/ares-cross-domain-generalization-limits.md
aliases: [ARES cross-domain transfer, ARES judge generalization boundary, ARES XGLUE CodeSearchNet T-Rex]
related: [ares-three-judge-rag-evaluation, ares-ppi-confidence-bound, ares-synthetic-data-pipeline]
---

## 主张

Saad-Falcon 等（2024）测了 ARES[^v3-1] fine-tuned LLM judge 的跨域迁移，给出一个清晰的"什么能迁移、什么不能"的分界线：

- **能迁移**：query 类型变（NQ ↔ FEVER）、document 类型变(NQ ↔ MultiRC)、两者同时变（NQ ↔ ReCoRD）。Kendall's τ 普遍 ≥ 0.78，多数 ≥ 0.89。
- **不能迁移**：
  - **语言切换**（NQ → XGLUE 多语）：τ ≈ 0.33
  - **文本→代码**（NQ → CodeSearchNet）：τ ≈ 0.28
  - **检索 → 实体抽取**（NQ → T-Rex）：τ ≈ 0.38

## 跨域表 tab:cross_domain 数字（pseudo RAG，6 个迁移对）[^src4]

| 迁移 | C.R. τ | A.R. τ | PPI range | 评估准确率 |
| --- | --- | --- | --- | --- |
| NQ→FEVER | 0.89 | 0.89 | 8.7% / 7.2% | 92.4% / 28.4% |
| FEVER→NQ | 1.0 | 0.83 | 6.5% / 11.5% | 85.7% / 22.6% |
| NQ→MultiRC | 0.94 | 0.89 | 10.2% / 11.3% | 81.5% / 92.1% |
| MultiRC→NQ | 1.0 | 0.89 | 11.9% / 11.5% | 87.6% / 80.2% |
| NQ→ReCoRD | 0.78 | 0.89 | 10.5% / 10.1% | 29.1% / 81.2% |
| ReCoRD→NQ | 0.89 | 0.94 | 9.7% / 6.2% | 80.1% / 92.1% |

**关键观察**：即便某些迁移上判官 raw accuracy 显著下降（如 NQ→FEVER 的 A.R. accuracy 跌到 28.4%），**Kendall's τ 仍能维持 ≥0.78**——因为 PPI[^v3-2] 把判官系统性偏移在 ranking 上"扯回来"。这是论文写得很清楚的一条："even in scenarios where the fine-tuned LLM judge's accuracy significantly dropped out-of-domain (e.g. answer relevance for NQ to FEVER), PPI mitigated the decrease in judge performance"[^src1]。

## 三条剧烈域漂移的失败

跨语言 / 文本→代码 / 抽取任务时 τ 跌到 0.28–0.38，**远低于** Kendall τ > 0.9 的"可用"门槛。论文给出的原因：合成数据[^v3-3] + DeBERTa 判官**学到的是 NQ 的查询/段落 surface pattern**，跨结构性域漂移时这些模式失效。「LLM judges are unable to generalize when making more drastic shifts in domain」[^src2]。

## 操作含义

- **同样语言、同样模态、同样任务范式**（QA / fact-checking / 对话）下，ARES 判官可以**复用**——不必每个新数据集重训。300 条 human preference + 5 条 few-shot 已足够 PPI 复用[^src3]。
- **跨语言部署**必须从头训：换成中文 / 多语 RAG，要换 LLM judge backbone（如 mDeBERTa）并重新合成 query/answer。
- **跨模态部署**（文本→代码 / 表格 / 图）必须重设计 negative 生成策略：现有 weak/strong negative 假设是文本相邻段落，对代码 / 抽取任务无效。
- **PPI 是关键缓冲**：判官 raw accuracy 跌 50% 不一定致命，只要 ranking 还对——这是 ARES 用 PPI 而不是纯监督评测的核心理由。

## 边界

- 论文没有测试 query/document **同步**剧烈变化（如多语 + 代码）——可能比单独剧烈漂移更糟，但没有数据；
- "可迁移"是在 KILT/SuperGLUE 内部跨 6 个数据集；其它领域（医疗、法律、金融）是否同样可迁移，论文 §Limitations 标记为 future work，因为这些领域**需要 domain expert annotator**——这是 ARES 的实际部署瓶颈[^src5]。
- PPI 校准集大小决定缓冲强度[^v3-2]；100 条以下，跨域漂移会与小样本噪声叠加。

## Footnotes

[^src1]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` §Cross-Domain 第 893–896 行 — "the fine-tuned LLM judges used in ARES proved successful in cross-domain applications. Across all settings, we found that LLM judges in ARES had strong generalizability, even when only using 300 datapoints in our human preference validation set for PPI. Furthermore, we found that even when the LLM judge's accuracy suffered in cross-domain applications, PPI helped mitigate the loss in accuracy and still allow ARES to be successful."
[^src2]: 同文件 第 898–904 行 — "While LLM judges in ARES were successful in cross-domain applications for KILT and SuperGLUE, LLM judges are unable to generalize when making more drastic shifts in domain, such as: switching languages (e.g. English to Spanish, German, and other languages), switching from text to code (e.g. questions + passages to coding functions + documentation), and switching from retrieving text to extraction of entities, webpages, or citations. To test cross-lingual transfer, we used the XGLUE datasets; a LLM judge fine-tuned on NQ achieved a Kendall's tau of 0.33 ... To test text-to-code, we used CodeSearchNet ... achieved a Kendall's tau of 0.28 ... To test extraction task generalizability, we used T-Rex ... achieved a Kendall's tau of 0.38."
[^src3]: 同文件 第 904 行 — "Each cross-domain shift requires in-domain passages and few-shot query examples for reconfiguring ARES judges."
[^src4]: 同文件 第 80–101 行（`Cross_Domain.tex`） — Table tab:cross_domain 完整 6 个迁移对的 C.R. τ / A.R. τ / PPI range / 评估准确率。
[^src5]: 同文件 §Limitations 第 666–678 行 — "specialized domain 需要 domain expert"，medical/legal/financial 领域被列为 future work。
[^v3-1]: [ares-three-judge-rag-evaluation](ares-three-judge-rag-evaluation.md) — 跨域评测的是 ARES 三个独立判官（C.R. / A.F. / A.R.）的迁移性能。
[^v3-2]: [ares-ppi-confidence-bound](ares-ppi-confidence-bound.md) — PPI 在 raw accuracy 下跌时仍能维持 ranking 的机制，以及校准集大小阈值。
[^v3-3]: [ares-synthetic-data-pipeline](ares-synthetic-data-pipeline.md) — DeBERTa 判官的合成 query/answer + weak/strong negative 流程；跨语言 / 跨模态需要重设计 negative。
