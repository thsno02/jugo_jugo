---
id: wicer-cegar-compile-evaluate-refine
title: WiCER 把 wiki 编译当作 CEGAR 抽象细化
status: accepted
card_type: mechanism
tags: [#llm-wiki, #knowledge-compilation, #cegar, #wicer]
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-28T11:35:00+08:00
edited_entity: llm
source_ids: [arxiv-wicer]
provenance_card: ../provenance/wicer-cegar-compile-evaluate-refine.md
aliases: [WiCER 算法, Wiki-memory Compile Evaluate Refine, 反例制导的 wiki 编译]
related: [wicer-blind-compilation-catastrophic-loss, wicer-targeted-vs-random-pinning-ablation, wicer-recovery-distribution-exceeds-fc-raw, wicer-llm-judge-human-validation, docs-as-code-merge-block-incentive, graphrag-leiden-community-hierarchy, llm-knowledge-base-five-stage-workflow, morishige-kb-compile-mem0-overlay]
---

WiCER 把"raw 文档 → 编译成 wiki"当作一次有损抽象，把"诊断探针打分"当作反例制导的细化（CEGAR），用迭代把丢失的事实重新钉回下一轮编译。这不是简单的"评测后重写一遍"——关键在于把每次失败的探针拆成一个具体的事实片段（约 50–100 字），放进累积集合 `F_cumulative`，作为下一次编译调用的硬约束。

算法骨架（论文 Algorithm 1）：

1. 对每个源文档采一条 QA 作为探针，构成 `Q_probe`；
2. 用目标压缩率 `r` 做一次盲编译得到 `W_0`；
3. 每一轮：用 `W_t` 回答全部探针，由 LLM judge 打分；
4. 把 score = 1 的探针标为 `Failures_t`，从对应源文档抽出"被丢掉的关键事实"加入 `F_cumulative`；
5. 调用 `Compile(D, r, preserve=F_cumulative)` 得到 `W_{t+1}`；
6. 退出条件：无失败，或 `t>0` 且相对提升 < 10%。

机制要点：

- **抽象/具体的对应关系**：concrete 系统是文档集合 D，abstract 模型是 wiki `W_t`，规约是"所有探针都不能拿 1 分"，反例就是 score-1 的探针，spurious 检查就是去 D 里确认事实确实存在但被 wiki 删掉了。
- **单调收敛**：被显式钉过的事实不会再丢，所以"已钉事实集合上的失败子集"单调缩小；但未钉事实可能因为预算被挤占而新崩，所以净增益依赖编译预算够大。
- **代价**：每轮 ~130K 输入 token + ~17K 输出 token（1 次编译 + 80 次 judge + ~15 次诊断），约 \$1–2，~50 分钟；80 次本地推理探针 0 API 成本。
- **典型停在第 2 轮**：17 个 RepLiQA 主题中 10 个在第 2 轮达到峰值，其余在第 1 轮或不再改进——继续迭代会被"随机知识置换"（修一处挤掉另一处）抵消。

把 WiCER 和静态编译流水线（RAPTOR、GraphRAG、层次摘要）对照：那些方法构建索引或树后就固化；WiCER 的差别在闭环——同一个 flat wiki 用评测信号反复重写。论文原话：「WiCER differs in two respects: (1) it targets a flat wiki artifact optimized for KV cache serving rather than a retrieval index, and (2) it closes the loop by evaluating the compiled artifact against diagnostic probes and iteratively refining it—a feedback mechanism absent from static compilation pipelines.」[^1]

边界 / 失败模式：

- 当盲基线已经较高、score-1 不多时（如 `local_education_systems`，盲 2.41 / score-1 38.8%），可诊断的灾难性失败少，WiCER 提升为 0；
- 当对预算外的事实需求高时，钉得越多越挤占通用覆盖；
- 监督信号来自 LLM judge，judge 的偏差会被钉进下一轮编译。

## References

- WiCER 论文 `main.tex` 第 6 节 "WiCER: Wiki-memory Compile, Evaluate, Refine"，包含 Algorithm 1 的伪代码、设计理由（CEGAR 类比）与收敛性讨论；本卡的算法骨架、代价数字与失败边界全部来自该节正文与附录 D（CEGAR 映射）。

## Footnotes

[^1]: `data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt` 第 460–464 行（"Structured Knowledge Compilation" 段落末尾的两点对比）。
