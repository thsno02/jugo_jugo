---
id: alce-prompting-strategies
title: ALCE 实验里五种 prompting 策略的取舍
status: accepted
card_type: distinction
tags: [#citation, #alce, #prompting, #rag, #rerank]
created_time: 2026-05-26T11:25:00+08:00
edited_time: 2026-05-28T15:10:00+08:00
edited_entity: llm
source_ids: [arxiv-alce]
provenance_card: ../provenance/alce-prompting-strategies.md
aliases: ["Vanilla / Summ / Snippet / Interact / Rerank", "ALCE 提示策略对比"]
related: [alce-citation-recall-precision-nli, alce-retriever-and-context-utilization-gap, ragchecker-tuning-knobs-saturate]
---

ALCE 在 baseline 之外提出了若干种把"检索结果合成进生成"的 prompting 策略[^src1]，每种都对应一个具体的工程取舍：

- **Vanilla**：把 top-k 完整 passage 塞进 prompt，加严格 instruction（"为每条事实主张引用至少一个、至多三个 passage"）。基线，但会被 LLM 上下文长度卡住。
- **Summ**：先让模型对每个 passage 出 50 字以内带 query 条件的摘要，把摘要塞进 context。结果是 correctness 上升、citation quality 不变。摘要在压缩噪声的同时保留了核心事实。
- **Snippet**：先让模型从每个 passage 抽一段"能回答 query 的 span"，再喂给生成。和 Summ 趋势相似——correctness 改善、citation quality 持平。
- **Interact**：交互式工作流。先看 passage 的 summary/snippet，遇到关键 passage 用 `Check: Document [i][j]` 拉全文，看完后用 `Output:` 落一句。论文限制最多一次 check 3 个文档，并且 check 完要立即 output，避免连续 check 爆 context[^src2]。结果：在 ALCE 上**没有**比 Vanilla 更好，flexibility 没换来质量。
- **InlineSearch**：模型可以发起 `Search: keywords` 自己检索。同样属于交互式路径。
- **Rerank**：生成多份候选回答，用 ALCE 自己的自动 citation recall 指标[^v3-1]对候选排序，挑分最高的。citation quality 显著上升（人工评测确认），代价是 4× 生成成本。Rerank 的核心洞见是"用 metric 自己做候选选择"。
- **ClosedBook + PostCite**：完全闭卷生成 → 再用 post-hoc 检索给每条语句配 citation。correctness 不错，但 citation quality 远差，因为生成时模型没看 passage[^src5]。

把实验结论汇总成几条规则[^src3]：

- **summary / snippet 改 correctness，不改 citation quality**——压缩本身不让模型更会引用，只让它看到更多相关信息。
- **interactive retrieval ≠ 提分**——在 ALCE 这种 long-form 引用任务上，多步检索的灵活度并没有变现成更好的引用质量[^src4]。
- **rerank 用 metric 当选择器，是把"自动评估"反向再用一次**——这是少数能切实拉高 citation quality 的策略，但成本与可计算的 metric 强绑定。
- **post-hoc citation 不替代生成时检索**——闭卷生成的内容里有大量"模型记忆"，引用是事后补的，所以 citation recall 难看。

边界：

- 这些结论建立在 ALCE 的三数据集（ASQA / QAMPARI / ELI5）上；论文显式承认 multi-hop / 数学 / 代码场景未覆盖。
- ChatGPT 在加更多 passage 时表现不变，GPT-4 才能利用更多 passage[^v3-2]——这意味着 prompting 策略的收益会随基座模型缩放。
- Rerank 必须用 4 次采样的成本换 citation quality 的提升。

横向对比：RAGChecker 在 *prompt 显式要求 "更 faithful"* 的 ablation 上也得到"对 GPT-4 有效、对 Llama3-70B 几乎无效"的相同结论[^v3-3]——prompting 策略的收益普遍随基座模型缩放，不只 ALCE 一家观察到。

## Footnotes

[^src1]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` — `sections/appendix.tex` `app_sec:propmt`（L511–644）以及 `sections/model.tex` "Modeling"（L1181–1199） — 策略总览与 instruction 模板。
[^src2]: 同文件 `sections/appendix.tex` `\paragraph{Interact}` L327–331 — `"models tend to execute too many consecutive check actions, so we force the model to always output after each check. We limit the maximum number of passages to check as 3"`。
[^src3]: 同文件 `sections/intro.tex` L1138–1143 — `"summarizing the retrieved passages in a shorter text improves correctness but not citation quality; (4) reranking multiple generations boosts citation quality measured by human evaluation; (5) incorporating more retrieved passages in context does not help ChatGPT but improves GPT-4 performance."`
[^src4]: 同文件 L1140 — `"although interactive retrieval approaches ... offer more flexibility in when/what to retrieve, they do not improve the performance on this challenging benchmark"`。
[^src5]: 同文件 L1139 — `"a closed-book model (generating answers without accessing any retrieved documents) with post-hoc citing achieves good correctness but much worse citation quality"`。
[^v3-1]: [alce-citation-recall-precision-nli](alce-citation-recall-precision-nli.md) — Rerank 调用的"自动 citation recall 指标"是这张卡里描述的 NLI-based 二元判定。
[^v3-2]: [alce-retriever-and-context-utilization-gap](alce-retriever-and-context-utilization-gap.md) — "更多 passage 对 ChatGPT 无益、对 GPT-4 有益"的实测出处。
[^v3-3]: [ragchecker-tuning-knobs-saturate](ragchecker-tuning-knobs-saturate.md) — RAGChecker 的 prompt ablation 给出"对 GPT-4 有效、对 Llama3-70B 几乎无效"的并行结论。
