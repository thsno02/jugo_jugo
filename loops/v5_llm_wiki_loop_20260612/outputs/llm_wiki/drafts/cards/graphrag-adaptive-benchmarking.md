---
id: graphrag-adaptive-benchmarking
title: GraphRAG 自适应基准测试方法
status: draft
card_type: evaluation-methodology
tags: [graphrag, evaluation, adaptive-benchmarking, llm-as-judge, persona-generation, sensemaking-questions]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-graphrag]
evidence_basis: experimental_paper
justification: ../justification/graphrag-adaptive-benchmarking.md
canonical_concept: graphrag-adaptive-benchmarking
aliases: [adaptive benchmarking, GraphRAG evaluation, 自适应基准测试, sensemaking question generation, LLM-as-a-judge evaluation]
summary: >-
  GraphRAG graphrag-adaptive-benchmarking 自适应基准测试通过 LLM 生成语料特定的全局 sensemaking 问题：给定语料描述生成 K 个假设用户 persona，每用户 N 个任务，每任务 M 个需全局理解的问题（K=N=M=5, 共 125 题/数据集）。评估使用 LLM-as-a-judge 头对头比较按 comprehensiveness diversity empowerment directness 四维度判定。Directness 作为控制准则验证结果合理性（与前三者对立）。多次复制取平均消除 LLM 随机性。
related: [graphrag-global-sensemaking, graphrag-claim-based-validation]
---

GraphRAG 论文提出一套自适应基准测试方法，用于评估全局 sensemaking 性能。

**为何需要新方法**: 传统 QA benchmark（HotPotQA、MultiHop-RAG、MT-Bench）面向具体事实检索，无法评估全语料理解能力。

**问题生成（Algorithm 1）**:
1. 给定语料描述，LLM 生成 K=5 个假设用户 persona
2. 每用户生成 N=5 个会使用 RAG 系统完成的任务
3. 每（用户, 任务）对生成 M=5 个需要全局理解的问题
4. 合计 125 题/数据集
5. 问题不从语料本身直接生成，避免评估偏差

**评估准则**:
- **Comprehensiveness**: 答案覆盖问题各方面的详尽程度
- **Diversity**: 提供不同视角和洞察的丰富程度
- **Empowerment**: 帮助读者理解并做出知情判断的能力
- **Directness**（控制准则）: 回答的简洁直接性——与前三者预期对立，用于验证结果合理性

**评估流程**: LLM 获得问题 + 两个系统的答案 → 按各准则判定胜者（或平局）→ 每对比较运行 5 次取平均。

[^src-1]: `data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- "Global Sensemaking Question Generation" (Section 3.2) -- "the LLM is prompted to generate personas of hypothetical users of the RAG system"
[^src-2]: `data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- "Criteria for Evaluating Global Sensemaking" (Section 3.3) -- "we use directness...to behave as a reference against which we can judge the soundness of results"
[^card-1]: [graphrag-global-sensemaking] 此评估方法专门服务于全局 sensemaking 场景
