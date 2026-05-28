---
id: alce-eli5-claim-recall-design
title: ALCE 的 ELI5 claim-recall：用 InstructGPT 拆 3 条子主张，再让 NLI 判蕴含
status: accepted
card_type: mechanism
tags: [#citation, #alce, #eli5, #correctness, #sub-claim, #NLI, #instructGPT]
created_time: 2026-05-26T15:40:00+08:00
edited_time: 2026-05-28T15:15:00+08:00
edited_entity: llm
source_ids: [arxiv-alce]
provenance_card: ../provenance/alce-eli5-claim-recall-design.md
aliases: [ELI5 claim recall, sub-claim correctness, ALCE long-form correctness metric]
related: [alce-three-dimension-citation-metric, alce-citation-recall-precision-nli, ragas-faithfulness-metric, ragchecker-claim-entailment-decomposition, ares-synthetic-data-pipeline]
---

## 为什么不能用 ROUGE

ELI5 是长篇开放式回答（人类答案平均 131 词），传统 ROUGE-L 在这个数据集上**严重失真**：

| 方法 | ROUGE-L | Claim recall |
| --- | --- | --- |
| ChatGPT \vani{} | 20.6 | 12.0 |
| ChatGPT \oracle{} | 21.2 | 21.3 |
| LLaMa-13B \vani{} | 16.2 | 3.9 |
| **Top-1 passage 直接返回** | **19.1** | **3.0** |

最后一行是 ALCE 论文用来说明问题的关键反例：**直接把 BM25 top-1 passage 当回答**就能拿到 ROUGE-L=19.1，几乎不输 ChatGPT 的 20.6，但 claim recall 只有 3.0——它根本没覆盖 gold answer 的不同侧面[^src3]。

## 替代方案：sub-claim 抽取 + NLI 判蕴含

ALCE 在 ELI5 上的 correctness 度量[^v3-1]分两步：

1. **claim 抽取（离线，一次性）**：用 `text-davinci-003` (InstructGPT) **从 ELI5 训练集人工答案里抽 3 条 sub-claim**。论文先手工标 3 个示例做 in-context demo，再以此 prompt 大规模生成[^src5]；
2. **claim recall 评估（在线，每次评测）**：拿待评模型的生成回答当 premise，把每条 sub-claim 当 hypothesis 喂 TRUE NLI 模型[^v3-2]；只要 NLI 输出"1"，该 sub-claim 算被覆盖；3 条里覆盖几条直接给百分比作为 claim recall。

## 质量检查（论文给出的关键数字）

为了证明这套抽取-评估流程站得住脚，作者做了两条独立人工校验：

- **InstructGPT sub-claim 抽取质量**：随机抽 40 个答案 × 3 条 = **120 sub-claims** 人工打分（1=与问题相关且忠实于 gold，0=否）。**112/120 = 93.33% 通过**，平均 14 词、一句一条——符合"短事实主张"的设计意图[^src1]；
- **NLI 判蕴含的预测准确率**：拿同样 120 (output, sub-claim) 对人工标蕴含，再用 TRUE 模型预测，**accuracy = 80.0%**[^src2]。

这 80% 是 ELI5 correctness 自动评估的上限——任何方法的 claim recall 差异在 ±2-3 个点之内都可能是 NLI 噪声而非真正差距。

## 为什么这套设计能避开 ROUGE 的失败模式

- ROUGE-L 奖励"和 gold 字面重合"；BM25 top-1 passage 因为是 Wikipedia/Web 自然文本，自然有大量与 gold 主题词重合的 token——容易刷分；
- claim recall 测"是否覆盖关键事实"，重叠词无效——top-1 passage 看似切题，但常常**只覆盖问题的一个 facet**，而 ELI5 gold 是多 facet 综合答案；
- 论文显式援引 Krishna 2021 "hurdles" 论文作为反 ROUGE 的依据[^src4]，意思是这一选型不是 ALCE 首创，而是 long-form QA 评估的共识转向。Ragas 的 faithfulness[^v3-3]与 RAGChecker 的 claim entailment[^v3-4]也都跳过表面相似指标、走"拆原子主张→蕴含判定"同一条路。

## 操作含义

- 复现 ALCE 不需要每次都跑 InstructGPT——sub-claims 是**离线一次性生成**的（论文随数据 release）；
- 用别的 NLI 模型替代 TRUE 会动摇 80% 的可靠性上限——必须重新做 120 对人工校验；
- 同一套"抽 N 条子主张 + NLI 判蕴含"的范式可以推广到任何 long-form QA，但**抽几条、由谁抽、抽多长**都会影响 ceiling。论文选择 N=3、平均一句一条，是经验取舍。

## 已知失败模式

- sub-claim 不能完全覆盖 gold——ELI5 答案多样，3 条可能漏掉合理变体（论文 Limitations §2 明确承认）[^src6]；
- claim recall 8/120 (6.67%) 错抽率不可忽视，会在小规模评测里制造 noise；
- 若被测系统**回答风格与 sub-claim 完全错位**（如 ASCII art / 列表），NLI 模型的判定会偏向 0——这一边界论文未量化。

## Footnotes

[^src1]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` `sections/appendix.tex` 第 266–270 行 — "To ensure that the generated sub-claims are of good quality, we manually inspect a random sample of 40 answers and their generated sub-claims (totaling to 120 sub-claims). ... We found that 112 out of the 120 (93.33%) sub-claims received a score of 1, meaning that our generated sub-claims are of high quality and faithful to the ground truth. Furthermore, the average number of words in the generated sub-claims is 14 words, and they are typically just one sentence long."
[^src2]: 同文件 `sections/appendix.tex` 第 273–277 行 — "we first manually annotate the entailment scores between 40 outputs and their sub-claims (in total of 120 pairs; ...). We then use the NLI model to obtain the entailment scores for the output and sub-claims. Using the human annotations as the ground truth label, we found that the NLI model achieved an accuracy of 80.0%."
[^src3]: 同文件 `tables/eli5_rouge.tex` 第 1962–1967 行 — "ChatGPT vani 20.6 12.0 / ChatGPT oracle 21.2 21.3 / LLaMa-13B vani 16.2 3.9 / Top-1 passage 19.1 3.0"。
[^src4]: 同文件 `sections/appendix.tex` 第 249–252 行 — "We elect not to use ROUGE-L as our main correctness metrics since it does not account for the different ways of expressing the same answer and it can be easily gamed [Krishna 2021]. ... A system can easily achieve high ROUGE-L score by retrieving and returning the top passage from a BM25 index."
[^src5]: 同文件 `tables/eli5_claims_prompt.tex` 第 1823–1866 行 — ELI5 claim 抽取的 few-shot prompt 模板（3 例 in-context demo）。
[^src6]: 同文件 limitations 第 106–110 行 — sub-claim 只取 3 条，无法完全覆盖 ELI5 多样答案的局限。
[^v3-1]: [alce-three-dimension-citation-metric](alce-three-dimension-citation-metric.md) — ELI5 claim recall 是 ALCE 三维度评估中 *correctness* 那一维针对 long-form 数据集的口径。
[^v3-2]: [alce-citation-recall-precision-nli](alce-citation-recall-precision-nli.md) — TRUE NLI 模型与 citation quality 用的是同一个 T5-11B；对该模型的能力上限和 Cohen κ 在那里展开。
[^v3-3]: [ragas-faithfulness-metric](ragas-faithfulness-metric.md) — 同样"先拆原子断言再做蕴含判定"的范式，judge 换成 LLM-as-judge。
[^v3-4]: [ragchecker-claim-entailment-decomposition](ragchecker-claim-entailment-decomposition.md) — 同样的 claim + entailment 原语，extractor/checker 改为 Llama3-70B（RefChecker）。
