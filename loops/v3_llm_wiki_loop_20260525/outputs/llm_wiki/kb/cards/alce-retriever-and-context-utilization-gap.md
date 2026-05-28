---
id: alce-retriever-and-context-utilization-gap
title: ALCE 的 retrieval 分析揭示 "passage 越多不等于答案越好" 的 LLM 利用瓶颈
status: accepted
card_type: source_claim
tags: [#citation, #alce, #retrieval, #context-window, #chatgpt, #gpt-4]
created_time: 2026-05-26T15:45:00+08:00
edited_time: 2026-05-28T15:05:00+08:00
edited_entity: llm
source_ids: [arxiv-alce]
provenance_card: ../provenance/alce-retriever-and-context-utilization-gap.md
aliases: [ALCE retrieval analysis, oracle vs vanilla, GTR vs DPR, context utilization ceiling]
related: [alce-three-dimension-citation-metric, alce-prompting-strategies, mem0-rag-chunk-size-ablation, ragchecker-retriever-claim-vs-chunk-precision, wicer-fc-rag-document-count-crossover, karpathy-wiki-full-context-vs-rag]
---

## ALCE 的检索栈

- **Wikipedia 21M passages**（ASQA + QAMPARI）：dense retrieval (GTR, DPR)；
- **Sphere 899M Web passages**（ELI5）：BM25；
- 所有任务**预先把语料切成 100 词 passage**；这与 Bing Chat 引整页 Web 不同——动机是"人更容易验证，且能在小 context 内多放几条";
- 每题统一**取 top-100 passages**，再由 prompting 策略截到 top-$k$；
- 答案侧统一允许"每条语句至多 3 个 citations"。

## Retrieval recall 是性能天花板

论文 Figure 2 把三数据集上 retriever recall@$k$ 与 correctness 并排画出来，揭示了一条简洁的因果链：

| 数据集 | 指标 | R@1 | R@3 | R@5 | R@20 | R@100 | Oracle (5) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ASQA | EM recall | 35.1 (GTR) | 50.7 | 56.8 | 70.3 | 78.4 | 78.4 |
| QAMPARI | recall-5 | 14.6 (GTR) | 24.7 | 31.6 | 49.7 | 65.6 | 65.6 |
| ELI5 | claim recall | 3.0 (BM25) | 6.6 | 9.6 | 19.3 | **31.8** | 31.8 |

关键观察：

- **ELI5 上 BM25 R@100 才 31.8%**——这是任何下游 reader 在 ELI5 上的硬上限。换言之，**ELI5 的 correctness 跌得难看不是 LLM 笨，是 retriever 没把 gold 召回来**。
- ASQA 上 GTR > DPR（R@5: 56.8 vs 51.5）——dense retriever 的选择直接影响 reader；
- "Oracle" 用 top-100 passages 重排出来的 5 条 gold 集合在三个数据集上都和 R@100 一致——证明 oracle 设置确实对应了 retrieve 能达到的最高覆盖。

## LLM context utilization gap

这是论文最反直觉的发现。在 ASQA 上，ChatGPT \vani{} 配 GTR 检索：

| Passage 数 | EM recall (Correct.) | Citation recall | Citation precision |
| --- | --- | --- | --- |
| 1-psg | 38.4 | 56.0 | 64.0 |
| 3-psg | 39.6 | 72.8 | **73.9** |
| 5-psg | **40.4** | **73.6** | 72.5 |

而 ChatGPT-16K (16k context) 同样配 GTR：

| Passage 数 | Correct. | Citation recall | Citation precision |
| --- | --- | --- | --- |
| 5-psg | 36.1 | 76.2 | 76.5 |
| 10-psg | 36.7 | 75.3 | 75.0 |
| 20-psg | 36.1 | 73.7 | 73.5 |

两条规律：

1. **ChatGPT 4K 模式**下 correctness 从 top-1 到 top-5 平台化（38.4 → 39.6 → 40.4），**top-3 之后基本不再增加**；
2. **ChatGPT-16K 模式**给更多 passage 反而**不涨甚至略跌**——"长 context"对 ChatGPT 在 ALCE 上是浪费；
3. GPT-4 是少有的例外：5-psg → 20-psg 时 correctness 41.3 → 44.4 单调升，citation recall 也升——**只有 GPT-4 这一档模型**能从更多 passage 里继续提取信息。

论文用一句结论收尾："processing more passages is non-trivial and GPT-4 is better at synthesizing information from its long context than ChatGPT."

## ASQA correctness 平台化的更细节据点

| 配置 | EM recall |
| --- | --- |
| Vanilla 5-psg (retrieved) | 40.4 |
| Oracle 5-psg (gold) | **48.9** |
| Retrieval recall@5 (GTR) | 56.8 |

读法：

- retrieval recall 56.8 是天花板；
- 给 gold passage 时 LLM 拿到 48.9——还差 8 个点没拣干净（"context 里有答案但模型没用上"）；
- 给真实 retrieve 结果时再降到 40.4——8.5 个点的下降归因于 retriever 噪声。

ALCE 由此推出三条挑战：**(1) retriever 质量是上限**；**(2) context window 限制了能塞多少 passage**；**(3) LLM 在上下文里 synthesize 多文档的能力本身就有限**。后两条之所以同时成立，是因为 (3) 即便给到长 context（ChatGPT-16K）也不会自动好。

## 操作含义

- 选 ALCE 报数据时**必须报 retriever 与其 R@k**——否则无法判断 reader 上限；
- **在 ELI5 上做开放 evaluation 时尤其要警告**：BM25 R@100=31.8% 意味着所有方法都不可能在 claim recall 上超过 ~32 分。这是为什么 ELI5 上 ChatGPT \vani{} claim recall 才 12 分却仍然算"合理水平"；
- 给 4K 上下文模型加 passage **超过 5 条几乎没用**；给 16K 也没用；只有 GPT-4 级模型加 passage 才继续涨——投入算力前要看模型档次。

## References

- §"Retrieval Analysis" 与 retrieval 表（`sections/results.tex` 第 1499–1531 行，`tables/retrieval_asqa.tex` 第 2336–2351 行，`tables/retrieval_eli5.tex` 第 2353–2367 行，`tables/retrieval_qampari.tex` 第 2369–2383 行）；
- ASQA different LLMs 表（`tables/asqa_different_llms.tex` 第 1608–1656 行）；
- 数据集设置：100 词 passages、top-100 检索（`sections/benchmark.tex` 第 741–746 行）；
- "GPT-4 brings limited improvement but is better at using long context" 段（`sections/results.tex` 第 1428–1436 行）；
- 来源：`data/raw/arxiv/arxiv-alce/agent_source_bundle.txt`。

## Footnotes

[^1]: GPT-4 vs ChatGPT-16K 段（results.tex 第 1434–1435 行）："including more passages with ChatGPT-16K does not improve the results (Table 2), suggesting that processing more passages is non-trivial and GPT-4 is better at synthesizing information from its long context than ChatGPT."

[^2]: Oracle vs Vanilla vs retrieval recall（results.tex 第 1513–1517 行）："both models' correctness lags behind the corresponding retrieval recall (except for ELI5 top-5). The discrepancy suggests that despite the presence of accurate answers in context, LLMs struggle to utilize them in their outputs."

[^3]: ASQA oracle 48.9 vs vanilla 40.4（tables/asqa_full.tex 第 1684 行）："oracle (5-psg) & 64.4 & 48.9 & 74.5 & 72.7"。

[^4]: ELI5 retrieval R@100 = 31.8（tables/retrieval_eli5.tex 第 2361 行）："BM25 & 3.0 & 6.6 & 9.6 & 19.3 & 31.8"。
