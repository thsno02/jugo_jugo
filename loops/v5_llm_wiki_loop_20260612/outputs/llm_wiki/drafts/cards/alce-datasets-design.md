---
id: alce-datasets-design
title: ALCE 三数据集设计选择
status: draft
card_type: dataset-description
tags: [ASQA, QAMPARI, ELI5, Wikipedia, Sphere, dataset-design]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-alce]
evidence_basis: experimental_paper
justification: ../justification/alce-datasets-design.md
canonical_concept: alce-datasets-design
aliases: [ASQA dataset, QAMPARI dataset, ELI5 dataset, ALCE datasets]
summary: >-
  ALCE (alce-datasets-design) 选取三个数据集覆盖不同问答类型：ASQA（歧义事实型，来自 AmbigQA，答案需覆盖多个短答案，语料为 Wikipedia 21M passages）；QAMPARI（列表型事实问答，答案为来自不同段落的实体列表，同用 Wikipedia）；ELI5（长文本 how/why/what 问答，来自 Reddit "Explain Like I'm Five"，语料为 Sphere 899M passages，Common Crawl 过滤版）。每数据集取 1000 条开发集样本，不提供训练数据。数据集选择标准：含事实性问题、需长文本多方面回答、需综合多源信息。
related: [alce-benchmark-overview]
---

ALCE 选取三个互补数据集，按照三个标准：包含事实性问题、需要长文本多方面回答、需要综合多源信息。[^src-1]

ASQA：长文本事实型数据集，每个问题是来自 AmbigQA 的歧义问题，需要多个短答案覆盖不同方面。语料为 2018-12-20 Wikipedia 快照（约 21M 100-word passages）。人类答案平均 65 词。[^src-2]

QAMPARI：列表型事实问答，答案是从不同段落中提取的实体列表。每个问题平均 13 个答案。同样使用 Wikipedia。[^src-3]

ELI5：长文本 QA，构建于 Reddit "Explain Like I'm Five" 论坛。问题多为 how/why/what 类型，需要长答案和多段落证据。语料为 Sphere（Common Crawl 过滤版，899M passages），因话题多样需要 Web 规模语料。人类答案平均 131 词。[^src-4]

基准从各数据集开发集随机抽取 1000 条样本，不提供训练数据（因无现有引用标注）。[^src-5]

[^src-1]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- "Task Setup and Datasets" -- "We choose QA datasets so that (1) they contain factual questions...;(2) questions require long-text answers...;(3) answering the questions requires synthesizing multiple sources"
[^src-2]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- "Task Setup and Datasets" -- "ASQA is a long-form factoid dataset...each question is an ambiguous question from AmbigQA"; "Dataset Statistics" -- "For ASQA, human answers have an average length of 65 words"
[^src-3]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- "Task Setup and Datasets" -- "QAMPARI is a factoid QA dataset...the answer is a list of entities"; "Dataset Statistics" -- "each question has on average 13 answers"
[^src-4]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- "Task Setup and Datasets" -- "ELI5 is a long-form QA dataset built on the Reddit forum...we use Sphere---a filtered version of Common Crawl"; "Dataset Statistics" -- "human answers have an average length of 131 words"
[^src-5]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- "Task Setup and Datasets" -- "We randomly select 1,000 examples from the development set...does not provide training data"

[^card-1]: alce-benchmark-overview
