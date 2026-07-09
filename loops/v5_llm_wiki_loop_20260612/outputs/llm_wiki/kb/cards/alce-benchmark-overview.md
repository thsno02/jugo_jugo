---
id: alce-benchmark-overview
title: ALCE 带引用生成自动评测基准
status: accepted
card_type: benchmark-system
tags:
- citation-evaluation
- LLM-generation
- benchmark
- retrieval-augmented-generation
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-alce
evidence_basis: experimental_paper
justification: ../justification/alce-benchmark-overview.md
canonical_concept: alce-citation-benchmark
aliases:
- ALCE
- Automatic LLMs' Citation Evaluation
- ALCE benchmark
summary: ALCE (alce-citation-benchmark) 是首个用于自动评估大语言模型带引用文本生成的可复现基准。给定查询 q 和文档语料库 D，系统需检索支持证据并生成带引用的回答。基准收集三个数据集 ASQA/QAMPARI/ELI5，覆盖事实性问答、列表问答和长文本 QA，语料从 Wikipedia(21M passages) 到 Web 规模 Sphere(899M passages)。ALCE
  的核心价值在于提供自动化、可复现的评测替代昂贵的人工评估，弥补此前 WebGPT/Menick 等工作依赖商业搜索引擎和闭源模型的不足。
related:
- alce-citation-support-gap
- alce-datasets-design
- alce-prompting-strategies
- alce-three-dimensional-evaluation
- closedbook-posthoc-citation-gap
- instruction-tuning-citation-ability
- retrieval-quality-bottleneck
---
ALCE 是首个用于自动评估 LLM 带引用生成能力的可复现基准。[^src-1]

任务形式化为：给定查询 q 和文本段落语料 D，系统返回由 n 个语句 s_1...s_n 组成的输出 S，每个语句 s_i 引用若干段落 C_i（实践中每句最多引用 3 篇）。引用以方括号标注如 [1][2]。[^src-2]

语料 D 按 100 词切分段落，这一粒度既便于人类验证，也允许在 LLM 有限上下文中放入更多检索结果，与商业系统引用整页 Web 的做法不同。[^src-3]

[^src-1]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- "Introduction" -- "We present ALCE, the first reproducible benchmark for automatically evaluating LLMs' generations with citations."
[^src-2]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- "Task Setup and Datasets" -- "the system is required to return an output S, which consists of n statements s_1, ..., s_n, and each statement s_i cites a list of passages"
[^src-3]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- "Task Setup and Datasets" -- "We divide the corpus D into 100-word passages...it is easier for humans to verify, and allows for more retrieved passages to fit in LLMs' limited context."
