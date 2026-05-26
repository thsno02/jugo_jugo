---
id: wicer-fc-rag-document-count-crossover
title: 全上下文 KV cache 与 RAG 在文档数处发生质量翻转
status: draft
card_type: distinction
tags: [#kv-cache, #rag, #lost-in-the-middle, #llm-wiki]
created_time: 2026-05-26T11:10:00+08:00
edited_time: 2026-05-26T11:10:00+08:00
edited_entity: llm
source_ids: [arxiv-wicer]
provenance_card: ../provenance/wicer-fc-rag-document-count-crossover.md
aliases: [FC vs RAG crossover, scalability gap, attention dilution crossover]
related: [wicer-blind-compilation-catastrophic-loss, wicer-hardware-architecture-deployment, wicer-cegar-compile-evaluate-refine, graphrag-context-window-8k-optimal, locomo-long-context-adversarial-collapse, karpathy-wiki-full-context-vs-rag]
---

WiCER 论文最值得收藏的"操作信号"不是 WiCER 本身，而是它先在两个语料上同时跑了 full-context（FC, 全文档塞进 KV cache）和 RAG（top-5 retrieval），观察到一个完整的"质量翻转"：

- **30 篇精编 Policygenius 文档（67K token，占 96K 窗 70%）**：FC 4.38 / RAG 4.08，FC 赢 0.30 分，TTFT 快 **7.3×**。
- **80 篇 RepLiQA 原始文档 / 主题（55–95K token，占窗 57–99%，共 17 个主题）**：FC 3.47 / RAG 3.64，FC 输 0.18 分；在 15 个有 FC 基线的主题里 **FC 一题没赢**（13 输 2 平）。

翻转的机制是 **lost in the middle**：FC 出现 17% 的 score-1（vs. Policygenius 的 1.2%），且 15 个主题里有 557 个题"FC 拿 1 分但 RAG 拿 ≥4 分"——模型把答案放在了上下文里却找不到，retriever 把它压缩到 2K token 后反而对了。RAG 在另一些题上拿 1 分（17.7%），但失败的是 retrieval miss（87.9% retrieval accuracy）——失败的不是同一批题。

把这一组数据当作"操作分界"，可以读出几条结论：

1. **窗口占比不是唯一变量**。Policygenius 占窗 70%，RepLiQA 占窗 57–99%，光看百分比 Policygenius 还更"挤"——但 Policygenius 还能赢，RepLiQA 不能。差别在编译质量：Policygenius 是"已经被人类编辑过"的 wiki，RepLiQA 是 raw 文档。论文原话：「That full-context excels on compiled knowledge but degrades on raw collections reinforces the LLM Wiki thesis: the quality of compilation, not just context length, determines viability.」[^1]
2. **Q4 KV cache 量化在大语料下会再吃一刀**。在 Policygenius 上 Q4 vs Q8 质量差 ≤0.03；在 RepLiQA 80 文档上 Q8 在 14 个主题中胜 13 个（mean Δ = +0.14），原因是低精度 KV 会放大 lost-in-the-middle。
3. **TTFT 优势保持但量级缩小**：Policygenius 上 FC TTFT 是 RAG 的 7.3×；RepLiQA 上仅 4.6×，因为更大的语料把 FC TTFT 也拉高了。

操作启示：

- **TTFT 在挑数据上能省 4–7×，但当 raw 文档塞满 60% 以上窗口时质量会翻转**——单凭 TTFT 不能压 RAG；
- **"塞满窗口"不是上限，"信息密度"才是**——Policygenius 之所以能赢，是因为它已经是被人类压过的精编 wiki；
- 这正好支撑 WiCER 的论证链：FC 在精编 wiki 上赢 → 大语料 raw 文档上 FC 输 RAG → 用 LLM 盲编译 wiki 又会塌方 → 所以需要 WiCER 这种带反馈的编译。

## References

- WiCER 论文 `main.tex` 第 4 节 "Full-Context KV Cache on Compiled Knowledge"（Policygenius，Table 1/2）与第 5 节 "The Scalability Gap"（RepLiQA，第 629–691 行）。本卡的数字、翻转结论与 lost-in-the-middle 解释都源自这两节及附录 `tab:generalization`。

## Footnotes

[^1]: `data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt` 第 687–690 行：
    > "These results establish a clear crossover: full-context's quality advantage at 30 documents and 67K tokens (Policygenius, 70% window fill) reverses at 80 documents and 55–95K tokens (RepLiQA, 57–99% fill) due to attention dilution. That full-context excels on compiled knowledge but degrades on raw collections reinforces the LLM Wiki thesis: the quality of compilation, not just context length, determines viability."
