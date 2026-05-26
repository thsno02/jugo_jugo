---
schema: draft_card_provenance.v3
draft_card: ../cards/ares-mock-rag-system-evaluation-design.md
material_id: arxiv-ares
digest_id: digest_arxiv-ares
source_paths:
  - data/raw/arxiv/arxiv-ares/agent_source_bundle.txt
created_time: 2026-05-26T15:30:00+08:00
edited_time: 2026-05-26T15:30:00+08:00
edited_entity: llm
---

## 源证据

### §Datasets 设计意图（第 541–547 行）

> "The efficacy of ARES relies on its ability to rank different RAG systems while only using a human preference validation set and domain-targeted LLM judges. To test the limits of ARES, we need to simulate the existence of many RAG systems that are separated by small accuracy margins on our evaluation metrics. For this, we create systems using artificial query-passage-answer triples, in which we empirically know the positive and negative examples of the mock RAG system."

### §Datasets 采样策略（第 549–553 行）

> "For our positive triples, we can simply use the KILT and SuperGLUE examples without any alteration. For gathering negative query-passage pairs and query-passage-answer triples, we randomly sample passages and answers from either: the same Wikipedia document or an entirely random Wikipedia document. This sampling allows us to artificially create mock RAG systems for testing ARES. By sampling both related and unrelated documents/answers, we hope to better gauge the efficacy of ARES in judging RAG outputs."

### §Datasets 9 splits 设计（第 557–560 行）

> "Using the validation subsets for each KILT and SuperGLUE dataset, we create nine different dataset splits, ranging from 70% success rate to 90% success rate for each of the evaluated RAG criteria; each dataset is separated by 2.5% accuracy points (e.g. 70.0%, 72.5%, 75.0%, ..., 90.0%). Each split also represents a different mock RAG system. Since we know the success percentages of each dataset split, we know the appropriate ranking of each mock RAG system. This allows us to test ARES success at both scoring and ranking the mock RAG systems appropriately across the three evaluation criteria."

### §Metrics Kendall τ 设计动机（第 569–576 行）

> "In development, researchers and engineers will be comparing different RAG configurations through individual pairwise comparisons of model choices, retriever selection, and document preprocessing. We want to make sure that ARES has satisfactory accuracy in pairwise comparisons across a variety of performance gaps between RAG systems. Kendall's τ is explicitly designed for measuring the accuracy of such pairwise comparisons."

### 与 sampled annotations baseline 比较（第 819–822 行）

> "we included a sampled annotations configuration, in which we sampled 150-datapoints from each mock RAG system, totalling 1,350 annotations. Even with all these annotations, the Kendall's tau for ARES is 0.08 higher on average, across both context and answer relevance, compared to sampled annotations, despite using 78% less annotations."

## 卡片范围是否成立

本卡聚焦"mock RAG 设计"作为独立 evaluation design 卡。现有三张 ARES 卡片：
- `ares-three-judge-rag-evaluation` 主要讲三判官机制；
- `ares-synthetic-data-pipeline` 讲合成训练数据；
- `ares-ppi-confidence-bound` 讲 PPI 统计；
- 三张卡**都未**讲清"ARES 是如何在已知 ground truth 上证明自己的"——即 9 个 2.5% 间隔的 mock split + Kendall τ 作为 self-validation 协议。

所有数字、方法步骤都直接来自 §Experiments → Datasets / Metrics 子节。"对其它 RAG 评估器同样适用"是合理引申——ARES 论文确实在同一 mock 框架下也对比了 RAGAS 和 GPT-3.5 judge。

## 发表门控结果

本轮未运行。

## 备注

- 这条 evaluation methodology 可外推到 RAG / LLM judge 类研究的元评估——任何新的 RAG 评估器都应先在 mock-with-known-accuracy 上验证排序能力。
- 与 ETAMP `etamp-pseudo-trajectory-methodology` 卡片有方法学呼应：都用"构造已知 ground truth 的实验设定"来 isolate variables。两者都属于"评估实验设计"主题。
