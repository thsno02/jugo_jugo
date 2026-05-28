---
id: wicer-blind-compilation-catastrophic-loss
title: 盲编译 wiki 会 2–3 倍超压并丢失关键事实
status: accepted
card_type: source_claim
tags: [#llm-wiki, #knowledge-compilation, #failure-mode, #wicer]
created_time: 2026-05-26T11:05:00+08:00
edited_time: 2026-05-28T11:30:00+08:00
edited_entity: llm
source_ids: [arxiv-wicer]
provenance_card: ../provenance/wicer-blind-compilation-catastrophic-loss.md
aliases: [compilation gap, 盲编译失败, wiki 编译过度压缩]
related: [wicer-cegar-compile-evaluate-refine, wicer-recovery-distribution-exceeds-fc-raw, wicer-fc-rag-document-count-crossover, karpathy-llm-wiki-source-executable-analogy, locomo-event-summarization-five-error-types]
---

如果没有评测反馈，让 LLM "把 80 篇原始文档压缩成 wiki" 这种最直觉的做法会同时踩两个坑：**压缩率失控**和**关键事实被删**。WiCER 论文在 17 个 RepLiQA 主题、6,800 道题上量化了这件事——结果不是"略有损失"，而是塌方式的灾难失败率。

数字表（论文 Table 3）：

| 条件 | 目标压缩 | 实际压缩 | 质量(1–5) | score-1 % | vs. FC raw |
| --- | --- | --- | --- | --- | --- |
| FC raw（80 篇原文） | — | 100% | 3.46 | 17.3% | — |
| Wiki-light | 75% | **35.4%** | 2.32 | 52.9% | −1.14 |
| Wiki-moderate | 50% | **12.2%** | 2.25 | 57.1% | −1.21 |
| Wiki-aggressive | 25% | **8.2%** | 2.14 | 60.3% | −1.32 |
| RAG | — | — | 3.63 | 17.7% | +0.17 |

两个独立观察：

1. **Compression compliance failure**：LLM 编译器把"光压一点"理解成了"狠狠压"——目标 75% 实际做到 35%，目标 50% 实际做到 12%，每一档都比目标多压 2–3 倍。这不是模型规模或 prompt 措辞的问题，是当前模型在"按字数预算输出"这件事上系统性不可控。
2. **失败模式是"信息缺失"而非"找不到"**：score-1 比率从 FC raw 的 17.3% 直接跳到 52.9–60.3%。论文原话：「The score-1 rate (53–60% for wikis vs. 17% for FC raw) confirms that answers fail because information is missing, not unfindable.」[^1] 这给了"为什么 WiCER 用 score-1 当反例信号"的因果依据——盲编译失败时事实真的不在 wiki 里。

延迟侧的代价反向：所有 wiki 档位的 TTFT 都低于 400 ms（FC raw 是 1.06 s），是 2.8–5.6× 加速。换句话说，**盲编译换来的是"快但错"——质量丢的远比延迟省的多**，这是 WiCER 试图修复的"compilation gap"。

操作含义：

- 不能假设 LLM 编译器会"按你说的目标比例"输出，必须用实际 token / 字数比例去校准；
- 单纯的"再压一遍"在质量上没有 sweet spot——light/moderate/aggressive 三档单调变差；
- 任何想用 LLM 离线压缩做 cache-augmented serving 的系统，**必须有一个评测回路**把丢失的事实抓回来（这正是 WiCER 的设计动机）。

## References

- WiCER 论文 `main.tex` 第 5 节 "The Compilation Gap" 与 Table 3（`tab:wiki_results`）。本卡所有数字来自该节正文与表格；"信息缺失而非找不到"的判断来自该节 "Analysis" 子节。

## Footnotes

[^1]: `data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt` 第 758–762 行（"Analysis" 段落）：
    > "The root cause is compression compliance failure: the compiler ignores target word counts, compressing 2×–3× beyond the requested level (light target 75% → actual 35%). At the actual ratios achieved (8–35%), the compiler discards too many specific facts for the model to recover. The score-1 rate (53–60% for wikis vs. 17% for FC raw) confirms that answers fail because information is missing, not unfindable."
