---
id: mem0-locomo-benchmark-evaluation
title: Mem0 在 LOCOMO 基准上的评估设计
status: accepted
card_type: experimental-setup
tags:
- benchmark
- LOCOMO
- evaluation-metrics
- llm-as-judge
- F1
- BLEU
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-mem0
evidence_basis: experimental_paper
justification: ../justification/mem0-locomo-benchmark-evaluation.md
canonical_concept: mem0-locomo-evaluation
aliases:
- LOCOMO benchmark
- LOCOMO evaluation
- locomo dataset
- long-term conversational memory evaluation
summary: LOCOMO 数据集包含 10 段长对话，每段约 600 轮对话 26000 tokens，附 200 问题（single-hop, multi-hop,
  temporal, open-domain 四类）。评估指标包括性能指标 F1 BLEU-1 LLM-as-a-Judge 和部署指标 token consumption
  latency。LLM-as-Judge 进行 10 次独立运行报告均值和标准差。对比六类基线：LOCOMO benchmarks、开源方案 LangMem、RAG
  不同配置、full-context、OpenAI memory、Zep。
related:
- locomo-evaluation-framework
- mem0-memory-architecture-overview
- mem0-performance-results
---

Mem0 论文采用 LOCOMO 数据集进行评估，该数据集专为评估对话系统的长期对话记忆能力设计。包含 10 段长对话，每段约 600 轮对话、平均 26000 tokens，分布于多个会话中。每段对话附带约 200 个问题，分为四种类型：single-hop、multi-hop、temporal 和 open-domain。[^src-1]

评估框架包含两类指标：[^src-2]
- **性能指标**：F1 Score、BLEU-1、LLM-as-a-Judge（由独立 LLM 评估事实准确性和相关性，10 次独立运行取均值 +/- 1 标准差）
- **部署指标**：Token Consumption（使用 tiktoken cl100k_base 编码）、Latency（分 search latency 和 total latency）

论文指出传统词汇相似度指标（F1、BLEU）在评估事实准确性方面存在根本局限——一个关键事实错误（如月份错误）可能因其余 token 重叠仍获得高分。LLM-as-a-Judge 作为互补指标提供更贴近人类判断的语义评估。[^src-3]

对比的六类基线涵盖：已有 LOCOMO benchmarks（LoCoMo、ReadAgent、MemoryBank、MemGPT、A-Mem）、开源方案（LangMem）、RAG（chunk size 128-8192，k=1,2）、full-context、OpenAI memory、Zep。[^src-4]

[^card-1]: [[mem0-memory-architecture-overview]] 描述了被评估的 Mem0 系统

[^src-1]: `data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` -- "sections/experiment_setup.tex" P1011 -- "It comprises 10 extended conversations, each containing approximately 600 dialogues and 26000 tokens on average"
[^src-2]: `data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` -- "sections/experiment_setup.tex" P1018 -- "we use LLM-as-a-Judge as a complementary evaluation metric... we conducted 10 independent runs for each method on the entire dataset and report the mean scores along with +/-1 standard deviation"
[^src-3]: `data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` -- "sections/experiment_setup.tex" P1017 -- "Despite containing a critical factual error regarding the birth month, traditional metrics would assign relatively high scores due to lexical overlap"
[^src-4]: `data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` -- "sections/experiment_setup.tex" P1025 -- "we compare against six distinct categories of baselines"
