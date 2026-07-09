---
id: ares-synthetic-data-generation
title: ARES 合成数据生成策略
status: accepted
card_type: mechanism
tags:
- synthetic-data
- flan-t5
- negative-generation
- rag-evaluation
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-ares
evidence_basis: experimental_paper
justification: ../justification/ares-synthetic-data-generation.md
canonical_concept: ares-synthetic-data-generation
aliases:
- ARES synthetic dataset
- LLM generation of synthetic dataset
summary: ARES 使用 FLAN-T5 XXL 从语料库段落 few-shot 生成合成 query-answer 对，通过检索过滤（query 须能将原始段落检索为
  top-1）保证质量。负例生成采用弱负例（随机无关段落/答案）和强负例（同文档段落或 BM25 top-10 相似段落；LLM 生成矛盾答案）两种策略，正负例数量相等。
related:
- ares-automated-rag-evaluation-system
- ares-llm-judge-finetuning
- ares-human-preference-validation-set
---

ARES 第一阶段使用 FLAN-T5 XXL 从领域内段落生成合成 query 和 answer，利用 few-shot prompt 引导生成。[^src-1]

质量过滤：用 FAISS IndexFlatL2 + OpenAI text-embedding-ada-002 做相似度搜索，丢弃无法将原始段落检索为 top-1 结果的合成 query。此策略源自 Promptagator 和 UDAPDR。[^src-2]

弱负例生成：C.R. 随机采样无关段落；A.F./A.R. 随机采样其他段落的合成答案。强负例生成：C.R. 从同文档其他段落或 BM25 top-10 相似段落采样；A.F./A.R. 用 FLAN-T5 XXL 生成矛盾答案。[^src-3]

正负例数量相等，用于后续对比学习微调。[^src-4]

[^card-1]: [^ref→ares-automated-rag-evaluation-system] 三阶段流程之阶段 1

[^src-1]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` -- "methods.tex" P700-703 -- "We generate synthetic queries and answers from the corpus passages using generative LLMs"
[^src-2]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` -- "methods.tex" P707-708 -- "we filter out low-quality queries by testing if a given query can retrieve its original passage as the top result"
[^src-3]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` -- "methods.tex" P713-719 -- "Weak Negative Generation...Strong Negative Generation"
[^src-4]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` -- "methods.tex" P721 -- "the number of negatives generated equals the number of positives"
