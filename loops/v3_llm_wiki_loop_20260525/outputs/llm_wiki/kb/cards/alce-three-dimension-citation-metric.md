---
id: alce-three-dimension-citation-metric
title: ALCE 用 fluency / correctness / citation quality 三维度堵住作弊路径
status: accepted
card_type: mechanism
tags: [#citation, #benchmark, #alce, #rag, #evaluation]
created_time: 2026-05-26T11:15:00+08:00
edited_time: 2026-05-28T15:20:00+08:00
edited_entity: llm
source_ids: [arxiv-alce]
provenance_card: ../provenance/alce-three-dimension-citation-metric.md
aliases: ["ALCE benchmark", "ALCE 三维度评估"]
related: [alce-citation-recall-precision-nli, alce-eli5-claim-recall-design, ares-three-judge-rag-evaluation, ragas-reference-free-rag-evaluation, ragchecker-generator-trilemma]
---

ALCE（Automatic LLMs' Citation Evaluation）是第一个把"LLM 生成带引用"做成可自动评分的 benchmark[^src1]。它故意把得分拆成三个互相牵制的维度：

- **Fluency**：用 MAUVE 量回答整体的流畅性（仅 ASQA / ELI5 用；QAMPARI 因为输出是短答案列表，跳过 MAUVE）。MAUVE 在这里只做"sanity check"，因为它对输出长度敏感而所有现代 LLM 文本一般都已经够流畅。
- **Correctness**：每个数据集有自己的口径——ASQA 用 short answer 的 EM recall；QAMPARI 用 list 上的 precision + recall-5（生成里至少 5 个对就算 recall=100%）；ELI5 用 InstructGPT 从 gold answer 派生 3 条 sub-claim、再用 TRUE NLI 模型判断 entailment（"claim recall"）[^v3-1]。
- **Citation quality**：用 TRUE NLI 模型在"citation 拼起来的 premise"与"被引语句"之间判 entailment，得出 citation recall（每条语句是否被自己的引用支撑）和 citation precision（每条引用是否对该语句有贡献，否则算 irrelevant）[^v3-2]。

之所以非要三维度并列，原因写在 `app_sec:short_cut`[^src5]：单一维度极容易被作弊。例如"直接把 top-1 retrieved passage 当回答并自引"几乎能拿到接近满分的 citation quality，但 fluency（不像人写的长答案）和 correctness（覆盖不全）都会塌掉；"截 top-1 passage 的前两句"也是一样的下场[^src2]。三维度同时及格才算系统真的"能带引用地回答问题"。

跨系统对照：ARES 也把 RAG 评估拆成 *context relevance / answer faithfulness / answer relevance* 三个独立判官[^v3-3]，Ragas 用 *faithfulness / answer relevance / context relevance* 同样三轴 reference-free 评测[^v3-4]，RAGChecker 则用 retriever × generator × overall 三组 claim-level 指标[^v3-5]。三大 RAG-评测体系都在"用一维分数容易被作弊、必须多维度互相牵制"这件事上收敛。

操作含义：

- **citation quality 必须搭 correctness 看**。论文里好几个 baseline 在 ELI5 上 ChatGPT/GPT-4 的回答 ~50% 都没被 cited passage 完整支撑——这是"citation recall 偏低"在长文回答里的真实分布[^src3]。
- **MAUVE 截断要小心**。论文在 ELI5 上把 reference 和生成都截到 100 词，因为 ELI5 的人工 answer 长尾极大，超过这一长度 MAUVE 不稳定。
- **NLI judge 的精度上限**：citation recall 自动评估准确率 85.1%，citation precision 77.6%（vs 人工）[^src4]。这是 ALCE 自动分对 LLM 排序的可信范围。

边界 / 局限：

- citation precision 不能识别"部分支撑"的引用，会高估 irrelevant 率。论文显式承认这是 NLI 模型能力的天花板。
- ALCE 三数据集覆盖事实型 / 列表型 / why-how-what 三种问题，但**不**覆盖 multi-hop 推理、数学、代码——这些更难的引用任务留给未来[^src6]。
- ALCE 假设只有评测数据可用、不提供训练集，所以它评的是"prompting 路径"，不是"训练带 citation 的模型"。

## Footnotes

[^src1]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` `sections/evaluation.tex` "Automatic Evaluation" 起始段（L814–826，关键 L823-825） — `"Fluency: whether the model's generated text is fluent and coherent." / "Correctness: whether the answer is accurate and covers all aspects of interest." / "Citation quality: whether the answer is well supported by the cited passages and no irrelevant passages are cited."`
[^src2]: 同文件 `sections/evaluation.tex` "ALCE is Robust to Shortcut Cases" L975–979 — 作弊路径："using the top-1 retrieved passage as the response and citing itself" 与 "using the first two sentences of the top-1 passage" 两条都会被 fluency / correctness 维度抓出来。
[^src3]: 同文件 L83-84（摘要） — `"on the ELI5 dataset, even the best models lack complete citation support 50% of the time."`
[^src4]: 同文件 `sections/appendix.tex` "More Human Evaluation" L482–486（关键 L483-484） — `"For citation recall, ALCE achieves an accuracy of 85.1%; for citation precision, ALCE has an accuracy of 77.6%."`
[^src5]: 同文件 附录 `app_sec:short_cut` L343–352 — 作弊路径与三维度互相牵制的设计动机。
[^src6]: 同文件 `sections/limitations` L102–121 — ALCE 三数据集对 multi-hop / 数学 / 代码场景的不覆盖。
[^v3-1]: [alce-eli5-claim-recall-design](alce-eli5-claim-recall-design.md) — ELI5 上 correctness 的具体机制：InstructGPT 拆 3 条 sub-claim + TRUE NLI 判蕴含。
[^v3-2]: [alce-citation-recall-precision-nli](alce-citation-recall-precision-nli.md) — citation quality 的 NLI 形式化定义和 irrelevant 的双条件判定。
[^v3-3]: [ares-three-judge-rag-evaluation](ares-three-judge-rag-evaluation.md) — ARES 用 *context relevance / answer faithfulness / answer relevance* 三个独立 fine-tuned 判官。
[^v3-4]: [ragas-reference-free-rag-evaluation](ragas-reference-free-rag-evaluation.md) — Ragas 同样把 RAG 拆成 *faithfulness / answer relevance / context relevance* 三轴 reference-free 评测。
[^v3-5]: [ragchecker-generator-trilemma](ragchecker-generator-trilemma.md) — RAGChecker 在 generator 端进一步拆出 *faithfulness × context utilization × noise sensitivity* 三难，原理同源。
