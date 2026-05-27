---
id: graphrag-adaptive-benchmark-via-personas
title: 用"persona × task × question"自适应生成全局意义建构基准
status: accepted
card_type: operational_rule
tags: [#evaluation, #llm-as-judge, #benchmark, #sensemaking, #adaptive-benchmarking]
created_time: 2026-05-26T11:03:00+08:00
edited_time: 2026-05-27T10:01:00+08:00
edited_entity: llm
source_ids: [arxiv-graphrag]
provenance_card: ../provenance/graphrag-adaptive-benchmark-via-personas.md
aliases: ["GraphRAG 评测协议", "adaptive sensemaking benchmark"]
related: [graphrag-global-sensemaking-pipeline, graphrag-context-window-8k-optimal, ragas-reference-free-rag-evaluation, wicer-llm-judge-human-validation, ares-three-judge-rag-evaluation, alce-three-dimension-citation-metric]
---

GraphRAG 论文不仅给出方法，还给出一套针对"全局意义建构"问题的评测协议——因为 HotPotQA / MultiHop-RAG / MT-Bench 这些已有基准只评事实型检索，没法用来评 "What are the main themes in the dataset?" 这类没有 gold answer 的问题。论文的协议有三块：

**1. 自适应生成问题（adaptive benchmarking）：**

不是手工出题，而是用 LLM 按 `persona × task × question` 三层组合自动生成。Algorithm 1 给出的过程是：

- 给 LLM 一段语料的"高层描述"；
- 让它生成 K 个"潜在用户 persona"；
- 对每个 persona 列出 N 个该用户会执行的任务；
- 对每个 `(user, task)` 对再生成 M 个"需要全局理解、不要求检索具体事实"的问题。
- 论文取 K = M = N = 5，得到每个数据集 125 道题。

关键设计选择：问题**不直接从语料生成**，以免出题人和答题人共享同一组细节，进而把全局题降级成事实题。

**2. 头对头比较（LLM-as-judge head-to-head）：**

没有 gold answer，就用 LLM 评审两个候选答案在四个维度上的胜负：

- *Comprehensiveness*：覆盖问题的所有方面，详尽不冗余；
- *Diversity*：观点和角度的丰富度；
- *Empowerment*：帮助读者形成判断，提供推理和来源；
- *Directness*（控制项）：是否简洁直接地回答了问题——故意设成与 comprehensiveness / diversity 反向，作为评测自洽性检验（任何方法都不应该四项全赢）。

每对比较跑多次 replicate，再在题目层平均，以吸收 LLM 评审的随机性。

**3. 用 claim-based 度量交叉验证：**

为了不只依赖 LLM 评审，论文额外用 Claimify 把答案拆成可验证 *factual claims*（共 47,075 条，平均每答 31 条），然后：

- claim-based **comprehensiveness** = 平均 claim 数；
- claim-based **diversity** = ROUGE-L 距离下的 agglomerative 聚类的平均簇数。

两套度量在 78%（comp.）/ 69–70%（div.）的非平局对比中一致——说明 LLM-judge 不是在凭空打分。

**操作含义（可复用为协议）：**

- 评一套"对私有语料做意义建构"的系统时，把"出题 → 评分"全部委托给独立的 LLM；
- 出题阶段输入只用"语料的高层描述"，不喂语料原文；
- 评分阶段要有一个反向控制指标（这里的 directness），用来证伪"任何方法在所有指标上都赢"这种假阳性；
- 用 Claimify 之类的方法把答案拆成可数 claim，作为 LLM-judge 的第二条证据线。

## References

- §3.2 Global Sensemaking Question Generation 与 Algorithm 1（`data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt`，行 859–895）。
- §3.3 评测准则与四指标（行 899–916）；directness 控制项含义见行 912–915。
- §3.4 / Experiment 2 的 claim-based 度量（行 963–974）；47,075 条 claim 数字在行 966。
- LLM-judge vs claim-based 的一致率（78% / 69–70%）：行 1013。

## Footnotes

- "we propose an approach for generating a set of questions for evaluating global sensemaking over the entirety of the corpus. Our approach is related to LLM methods that use a corpus to generate questions whose answers would be summaries of the corpus ... However, in order to produce a fair evaluation, our method avoids generating the questions directly from the corpus itself"——行 741–743。
- "Since directness is effectively in opposition to comprehensiveness and diversity, we would not expect any method to win across all four criteria."——行 915。
- "we extracted 47,075 unique claims, with an average of 31 claims per answer."——行 966。
- "the aggregated LLM label matched the claim-based label in 78% of pairwise comparisons for comprehensiveness and 69-70% for diversity"——行 1013。
