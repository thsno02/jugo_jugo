---
schema: draft_card_provenance.v3
draft_card: ../cards/alce-retriever-and-context-utilization-gap.md
material_id: arxiv-alce
digest_id: digest_arxiv-alce
source_paths:
  - data/raw/arxiv/arxiv-alce/agent_source_bundle.txt
created_time: 2026-05-26T15:45:00+08:00
edited_time: 2026-05-26T15:45:00+08:00
edited_entity: llm
---

## 源证据

1. `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` `sections/benchmark.tex` 第 741–746 行（100 词 passage、top-100）：

> "We divide the corpus D into 100-word passages following previous works on open-domain question answering ... in contrast to commercial systems like Bing Chat, which cite entire Web pages. We take 100-word passages because it is easier for humans to verify, and allows for more retrieved passages to fit in LLMs' limited context."

2. `sections/model.tex` 第 1195–1201 行（retriever 选型）：

> "We use dense retrievers for Wikipedia, including GTR and DPR; we use BM25 for Sphere. For each question, we retrieve the top-100 passages."

3. `tables/retrieval_asqa.tex` 第 2343–2347 行（ASQA retrieval recall@k）：

> "DPR & 29.6 & 44.5 & 51.5 & 64.6 & 74.1 / GTR & 35.1 & 50.7 & 56.8 & 70.3 & 78.4 / Oracle & 63.8 & 72.8 & 78.4 & - & -"

4. `tables/retrieval_eli5.tex` 第 2361 行（ELI5 BM25 R@100 = 31.8）。

5. `tables/asqa_full.tex` 第 1684 行（ASQA oracle 5-psg）：

> "oracle (5-psg) & 64.4 & 48.9 & 74.5 & 72.7 & 38.2 & 37.4"

6. `tables/asqa_different_llms.tex` 第 1629–1647 行（ChatGPT 4K / ChatGPT-16K / GPT-4 不同 passage 数对比）。

7. `sections/results.tex` 第 1428–1436 行（GPT-4 vs ChatGPT-16K 段）：

> "GPT-4 can also incorporate more passages due to its longer context window, which boosts both correctness and citation quality. On the contrary, including more passages with ChatGPT-16K does not improve the results, suggesting that processing more passages is non-trivial and GPT-4 is better at synthesizing information from its long context than ChatGPT."

8. `sections/results.tex` 第 1513–1517 行（oracle 与 retrieval recall 的差距）：

> "both models' correctness lags behind the corresponding retrieval recall (except for ELI5 top-5). The discrepancy suggests that despite the presence of accurate answers in context, LLMs struggle to utilize them in their outputs."

9. 第 1156 行（论文结论部分明确三大挑战）：

> "(1) the retrieval quality is crucial to the final performance and has substantial room for improvement; (2) LLMs' limited context window restricts the number of passages they can incorporate; (3) current LLMs struggle to synthesize multiple documents in context without being distracted by irrelevant ones."

## 卡片范围是否成立

本卡专门做 retrieval 与 LLM context utilization 的双重瓶颈分析：

- 三条挑战来自论文 §intro 与 §results；
- 表数据全部直接引用；
- "ELI5 上 BM25 R@100=31.8% 是所有方法的硬上限"是引申，但有 retrieval table 直接佐证；
- "5-psg 之后几乎没用 → 16K 也没用 → 只有 GPT-4 加 passage 还在涨" 是对 asqa_different_llms 表三段的直接读取。

与已有 ALCE 三卡（三维度 / NLI / prompting）、新写的 `alce-eli5-claim-recall-design` 卡均不重叠：本卡是 retrieval & context utilization 专题。

## 发表门控结果

本轮未运行。

## 备注

- 本卡的"ELI5 R@100 = 31.8" 数字可在 v3 retrieval-design 系列中作为"corpus scale × retriever 选型决定上限"的锚点。
