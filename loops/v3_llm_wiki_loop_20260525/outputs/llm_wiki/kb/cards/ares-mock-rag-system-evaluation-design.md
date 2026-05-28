---
id: ares-mock-rag-system-evaluation-design
title: 用 mock RAG（已知准确率梯度）作为 ARES 自身的 ranking 基准
status: accepted
card_type: operational_rule
tags: [#rag, #ares, #evaluation-design, #experimental-methodology, #mock-systems]
created_time: 2026-05-26T15:30:00+08:00
edited_time: 2026-05-28T15:35:00+08:00
edited_entity: llm
source_ids: [arxiv-ares]
provenance_card: ../provenance/ares-mock-rag-system-evaluation-design.md
aliases: [mock RAG systems, ARES evaluation design, pseudo RAG ranking, controlled accuracy splits]
related: [ares-three-judge-rag-evaluation, ares-ppi-confidence-bound, ares-synthetic-data-pipeline, ragas-wikieval-dataset, graphrag-adaptive-benchmark-via-personas]
---

## 主张

Saad-Falcon 等（2024）测 ARES[^v3-1] 的关键挑战是：**怎么知道 ARES 给出的排名是对的？** 真实 RAG 系统没有 ground-truth 排名。论文的方法是**构造 9 个"准确率已知"的 mock RAG 系统**，每个相差 2.5% 准确率，覆盖 70%–90% 区间——这样既能测试 ARES 能不能正确排序，又能测试它能不能区分**只差几个百分点**的相邻系统[^src1]。

## 构造方法

对 KILT / SuperGLUE 的每个验证子集做：

1. **正例 query-passage-answer 三元组**：直接用原数据集的标注样本，不动；
2. **负例采样**两种类型：
   - **同文档相关负例**：从同一 Wikipedia 文档的其他段落随机抽
   - **跨文档无关负例**：从完全随机的 Wikipedia 文档抽
3. **按准确率梯度做 9 个 splits**：70.0%、72.5%、75.0%、...、90.0%——每个 split 是一个独立的"mock RAG 系统"
4. **Kendall's τ 计算**：因为每个 mock RAG 的准确率事先已知，**真实排名固定**；ARES 的排名与真实排名之间的 Kendall's τ 就是 ARES 是否合格的客观指标[^src2][^src4]。

## 为什么这种构造比"用真实 RAG 比"更可信

- **没有 ground truth 漂移**：真实 RAG 的"哪个更好"依赖人工评测，本身有噪声；mock RAG 准确率是构造保证的；
- **可控梯度密度**：刻意选 2.5% 间隔——这是真实 RAG 评估里"两个配置只差几个百分点"的常见难度；如果 ARES 能在 2.5% 间隔下还排对，工程上就够用；
- **可重复**：mock split 是数据集衍生，任何复现者都能拿到同一份 mock RAG 集合。

## 实际结果（从而支持 ARES 的可信度）

- 在 NQ / HotpotQA / WoW / FEVER / MultiRC / ReCoRD 六个数据集上，ARES 平均 Kendall's τ：context relevance 0.065 高于 RAGAS[^v3-4]、answer relevance 0.132 高于 RAGAS（见 [ares-three-judge-rag-evaluation](ares-three-judge-rag-evaluation.md)）。
- 与 "sampled annotations baseline"（每个 mock RAG 抽 150 条共 1,350 条人工标注）对比：ARES τ 仍高 0.08，**且仅用 78% 更少标注**[^src3]。

## 操作含义（给"想测自己 RAG 评估器"的人）

- **不要只用真实 RAG 测 RAG 评估器**：你无法知道评估器错在哪、错多少。先用 mock 已知系统测排序能力。
- **梯度间隔应当与你部署场景的"配置差距"对齐**：如果你日常比较的 RAG 系统差 5%，那 mock 也用 5% 间隔；差 1%，那 mock 也用 1%（但需要更多 splits）。
- **正负例采样策略要复合**：同文档 + 跨文档混合采样能模拟 RAG 系统典型失败——只用其中一种会偏向某类错误。
- **此方法对其它 RAG 评估器同样适用**：RAGAS[^v3-4]、GPT-3.5 judge、人工 sampled annotations 都在论文中用同一 mock 框架被对比——ARES 论文实际**也是**第一个把 mock-RAG-with-known-accuracy 当作 RAG 评估器的"meta-benchmark"。Ragas 自家则另走 *WikiEval* 50 题人工 pairwise 标注的路线[^v3-2]，二者并不互斥。

## 边界

- mock RAG 的"准确率"是**模拟**的（人工调 split 至 70/72.5/.../90%），不是端到端模型的真实输出错误率。极端 RAG 失败模式（如长链幻觉）mock 中没有；
- 准确率 < 70% 和 > 90% 的区间未覆盖——非常差或非常好的 RAG 系统 ARES 的稳定性论文未测；
- 不评估 answer faithfulness（KILT/SuperGLUE 没有 hallucination 标签）；这部分论文用 AIS 数据集另测（§ARES on AIS）。
- mock RAG 是排序基准，最终置信区间还要靠 PPI[^v3-3]——两者协同构成 ARES 的可信度论证。

## Footnotes

[^src1]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` §Datasets 第 541–547 行 — "The efficacy of ARES relies on its ability to rank different RAG systems while only using a human preference validation set and domain-targeted LLM judges. To test the limits of ARES, we need to simulate the existence of many RAG systems that are separated by small accuracy margins on our evaluation metrics. For this, we create systems using artificial query-passage-answer triples, in which we empirically know the positive and negative examples of the mock RAG system."
[^src2]: 同文件 第 557–560 行 — "Using the validation subsets for each KILT and SuperGLUE dataset, we create nine different dataset splits, ranging from 70% success rate to 90% success rate for each of the evaluated RAG criteria; each dataset is separated by 2.5% accuracy points (e.g. 70.0%, 72.5%, 75.0%, ..., 90.0%). Each split also represents a different mock RAG system. Since we know the success percentages of each dataset split, we know the appropriate ranking of each mock RAG system. This allows us to test ARES success at both scoring and ranking the mock RAG systems appropriately across the three evaluation criteria."
[^src3]: 同文件 第 819–822 行 — "we included a sampled annotations configuration, in which we sampled 150-datapoints from each mock RAG system, totalling 1,350 annotations. Even with all these annotations, the Kendall's tau for ARES is 0.08 higher on average, across both context and answer relevance, compared to sampled annotations, despite using 78% less annotations."
[^src4]: 同文件 §Datasets 第 549–553 行 — 正例（数据集自带 query-passage-answer）/ 负例（同文档随机段落 + 跨文档随机段落）的采样策略说明。
[^src5]: 同文件 第 562–576 行 — 用 Kendall's τ 而非绝对分数差作 ARES 排序合格性指标的设计理由。
[^v3-1]: [ares-three-judge-rag-evaluation](ares-three-judge-rag-evaluation.md) — mock RAG 验证的是 C.R. / A.F. / A.R. 三个独立判官的排序能力。
[^v3-2]: [ragas-wikieval-dataset](ragas-wikieval-dataset.md) — 同样是"为验证 RAG 评估器构造数据集"的范式，Ragas 选 50 题人工 pairwise 标注路线。
[^v3-3]: [ares-ppi-confidence-bound](ares-ppi-confidence-bound.md) — mock RAG 是 ranking 基准，PPI 是置信区间机制，两者协同构成 ARES 可信度论证。
[^v3-4]: [ragas-reference-free-rag-evaluation](ragas-reference-free-rag-evaluation.md) — ARES 在 mock RAG 上与 RAGAS 对比 τ 高 0.065 / 0.132，这是被对照的另一个 reference-free RAG 评估器。
