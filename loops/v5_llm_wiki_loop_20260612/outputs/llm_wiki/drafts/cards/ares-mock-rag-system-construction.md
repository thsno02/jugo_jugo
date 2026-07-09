---
id: ares-mock-rag-system-construction
title: ARES 模拟 RAG 系统构建方法
status: draft
card_type: methodology
tags: [mock-rag, evaluation-methodology, dataset-construction, controlled-experiment]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-ares]
evidence_basis: experimental_paper
justification: ../justification/ares-mock-rag-system-construction.md
canonical_concept: ares-mock-rag-system-construction
aliases: [mock RAG systems, pseudo RAG systems, artificial RAG splits]
summary: >-
  为测试 ARES 区分细微性能差异的能力，论文构建模拟 RAG 系统：从 KILT/SuperGLUE 验证集创建 9 个不同 split，成功率从 70% 到 90%（每级间隔 2.5%）。正例直接使用原始数据，负例通过随机采样同文档/随机文档的段落和答案生成。每个 split 代表一个已知性能的 mock RAG 系统，使研究者能精确计算排名相关性。
related: []
---

为精确评估 ARES 的排名能力，论文需要已知 ground truth 排名的多个 RAG 系统。解决方案是构建模拟系统。[^src-1]

方法：从各数据集的 validation subset 创建 9 个 split，成功率从 70% 到 90%，每级间隔 2.5%（70.0%, 72.5%, ..., 90.0%）。每个 split 代表一个不同的 mock RAG 系统。[^src-2]

正例直接使用 KILT/SuperGLUE 原始数据。负例从同 Wikipedia 文档或完全随机文档中采样段落和答案，混合相关和无关文档以更好评估 ARES 的判别能力。[^src-3]

由于已知各 split 的确切成功百分比，可直接计算 Kendall's tau 来评估 ARES 的排名准确度。[^src-4]

[^card-1]: [^ref→ares-ranking-accuracy-vs-baselines] 使用这些 mock 系统的实验结果

[^src-1]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` -- "experiments.tex" P541-543 -- "we need to simulate the existence of many RAG systems that are separated by small accuracy margins"
[^src-2]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` -- "experiments.tex" P557-558 -- "nine different dataset splits, ranging from 70% success rate to 90% success rate...separated by 2.5% accuracy points"
[^src-3]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` -- "experiments.tex" P549-553 -- "For our positive triples...we randomly sample passages and answers from either: the same Wikipedia document or an entirely random Wikipedia document"
[^src-4]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` -- "experiments.tex" P559-561 -- "Since we know the success percentages...we know the appropriate ranking...allows us to test ARES success"
