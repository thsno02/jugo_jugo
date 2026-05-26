---
id: alce-eli5-claim-recall-design
title: ALCE 的 ELI5 claim-recall：用 InstructGPT 拆 3 条子主张，再让 NLI 判蕴含
status: draft
card_type: mechanism
tags: [#citation, #alce, #eli5, #correctness, #sub-claim, #NLI, #instructGPT]
created_time: 2026-05-26T15:40:00+08:00
edited_time: 2026-05-26T15:40:00+08:00
edited_entity: llm
source_ids: [arxiv-alce]
provenance_card: ../provenance/alce-eli5-claim-recall-design.md
aliases: [ELI5 claim recall, sub-claim correctness, ALCE long-form correctness metric]
related: [alce-three-dimension-citation-metric, alce-citation-recall-precision-nli]
---

## 为什么不能用 ROUGE

ELI5 是长篇开放式回答（人类答案平均 131 词），传统 ROUGE-L 在这个数据集上**严重失真**：

| 方法 | ROUGE-L | Claim recall |
| --- | --- | --- |
| ChatGPT \vani{} | 20.6 | 12.0 |
| ChatGPT \oracle{} | 21.2 | 21.3 |
| LLaMa-13B \vani{} | 16.2 | 3.9 |
| **Top-1 passage 直接返回** | **19.1** | **3.0** |

最后一行是 ALCE 论文用来说明问题的关键反例：**直接把 BM25 top-1 passage 当回答**就能拿到 ROUGE-L=19.1，几乎不输 ChatGPT 的 20.6，但 claim recall 只有 3.0——它根本没覆盖 gold answer 的不同侧面。

## 替代方案：sub-claim 抽取 + NLI 判蕴含

ALCE 在 ELI5 上的 correctness 度量分两步：

1. **claim 抽取（离线，一次性）**：用 `text-davinci-003` (InstructGPT) **从 ELI5 训练集人工答案里抽 3 条 sub-claim**。论文先手工标 3 个示例做 in-context demo，再以此 prompt 大规模生成；
2. **claim recall 评估（在线，每次评测）**：拿待评模型的生成回答当 premise，把每条 sub-claim 当 hypothesis 喂 TRUE NLI 模型；只要 NLI 输出"1"，该 sub-claim 算被覆盖；3 条里覆盖几条直接给百分比作为 claim recall。

## 质量检查（论文给出的关键数字）

为了证明这套抽取-评估流程站得住脚，作者做了两条独立人工校验：

- **InstructGPT sub-claim 抽取质量**：随机抽 40 个答案 × 3 条 = **120 sub-claims** 人工打分（1=与问题相关且忠实于 gold，0=否）。**112/120 = 93.33% 通过**，平均 14 词、一句一条——符合"短事实主张"的设计意图；
- **NLI 判蕴含的预测准确率**：拿同样 120 (output, sub-claim) 对人工标蕴含，再用 TRUE 模型预测，**accuracy = 80.0%**。

这 80% 是 ELI5 correctness 自动评估的上限——任何方法的 claim recall 差异在 ±2-3 个点之内都可能是 NLI 噪声而非真正差距。

## 为什么这套设计能避开 ROUGE 的失败模式

- ROUGE-L 奖励"和 gold 字面重合"；BM25 top-1 passage 因为是 Wikipedia/Web 自然文本，自然有大量与 gold 主题词重合的 token——容易刷分；
- claim recall 测"是否覆盖关键事实"，重叠词无效——top-1 passage 看似切题，但常常**只覆盖问题的一个 facet**，而 ELI5 gold 是多 facet 综合答案；
- 论文显式援引 Krishna 2021 "hurdles" 论文作为反 ROUGE 的依据，意思是这一选型不是 ALCE 首创，而是 long-form QA 评估的共识转向。

## 操作含义

- 复现 ALCE 不需要每次都跑 InstructGPT——sub-claims 是**离线一次性生成**的（论文随数据 release）；
- 用别的 NLI 模型替代 TRUE 会动摇 80% 的可靠性上限——必须重新做 120 对人工校验；
- 同一套"抽 N 条子主张 + NLI 判蕴含"的范式可以推广到任何 long-form QA，但**抽几条、由谁抽、抽多长**都会影响 ceiling。论文选择 N=3、平均一句一条，是经验取舍。

## 已知失败模式

- sub-claim 不能完全覆盖 gold——ELI5 答案多样，3 条可能漏掉合理变体（论文 Limitations §2 明确承认）；
- claim recall 8/120 (6.67%) 错抽率不可忽视，会在小规模评测里制造 noise；
- 若被测系统**回答风格与 sub-claim 完全错位**（如 ASCII art / 列表），NLI 模型的判定会偏向 0——这一边界论文未量化。

## References

- ELI5 claim 抽取流程：`sections/appendix.tex` §"Generating Claims for ELI5"（第 244–278 行）。
- ELI5 claim 抽取 prompt：`tables/eli5_claims_prompt.tex`（第 1823–1866 行）。
- ROUGE vs claim recall 对比表（`tables/eli5_rouge.tex` 第 1954–1973 行）。
- 论文 limitations 中关于 sub-claim 不全的承认（第 106–110 行）。
- 来源：`data/raw/arxiv/arxiv-alce/agent_source_bundle.txt`。

## Footnotes

[^1]: 抽取质量 verbatim（appendix.tex 第 266–270 行）："To ensure that the generated sub-claims are of good quality, we manually inspect a random sample of 40 answers and their generated sub-claims (totaling to 120 sub-claims). ... We found that 112 out of the 120 (93.33%) sub-claims received a score of 1, meaning that our generated sub-claims are of high quality and faithful to the ground truth. Furthermore, the average number of words in the generated sub-claims is 14 words, and they are typically just one sentence long."

[^2]: NLI accuracy（appendix.tex 第 273–277 行）："we first manually annotate the entailment scores between 40 outputs and their sub-claims (in total of 120 pairs; ...). We then use the NLI model to obtain the entailment scores for the output and sub-claims. Using the human annotations as the ground truth label, we found that the NLI model achieved an accuracy of 80.0%."

[^3]: ROUGE 反例表（tables/eli5_rouge.tex 第 1962–1967 行）："ChatGPT vani 20.6 12.0 / ChatGPT oracle 21.2 21.3 / LLaMa-13B vani 16.2 3.9 / Top-1 passage 19.1 3.0"

[^4]: 反 ROUGE 论证（appendix.tex 第 249–252 行）："We elect not to use ROUGE-L as our main correctness metrics since it does not account for the different ways of expressing the same answer and it can be easily gamed [Krishna 2021]. ... A system can easily achieve high ROUGE-L score by retrieving and returning the top passage from a BM25 index."
