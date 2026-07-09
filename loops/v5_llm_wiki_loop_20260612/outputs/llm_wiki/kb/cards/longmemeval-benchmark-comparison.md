---
id: longmemeval-benchmark-comparison
title: LongMemEval 与现有长期记忆基准的对比优势
status: accepted
card_type: comparison
tags:
- benchmark
- long-term-memory
- LoCoMo
- MemoryBank
- PerLTQA
- DialSim
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-longmemeval
evidence_basis: experimental_paper
justification: ../justification/longmemeval-benchmark-comparison.md
canonical_concept: longmemeval-vs-existing-benchmarks
aliases:
- LongMemEval comparison
- 长期记忆基准对比
summary: longmemeval-vs-existing-benchmarks LongMemEval 相较 MSC、DuLeMon、MemoryBank、PerLTQA、LoCoMo、DialSim 等现有基准的核心优势：(1) 唯一同时覆盖信息提取 IE、多会话推理 MR、知识更新 KU、时间推理 TR、拒答 ABS 全部五项核心能力；(2) 上下文深度可自由扩展至 1.5M tokens（其他最多约
  1M tokens 且不可配置）；(3) 聚焦人机交互（human-AI）的个人领域对话而非人人对话或电视剧角色扮演；(4) 先前基准均不评估知识更新能力，多数不覆盖多会话推理。
related:
- longmemeval-benchmark-overview
- longmemeval-five-core-memory-abilities
---

LongMemEval 与六个现有长期记忆基准的系统对比揭示其核心优势：[^src-1]

| 基准 | 领域 | 上下文深度 | IE | MR | KU | TR | ABS |
|------|------|-----------|----|----|----|----|-----|
| MSC (2022) | 开放域人人对话 | ~1k | - | - | - | - | - |
| DuLeMon (2022) | 开放域人机 | ~1k | - | - | - | - | - |
| MemoryBank (2024) | 个人人机 | ~5k | Y | - | - | Y | - |
| PerLTQA (2024) | 个人人机 | ~1M | Y | - | - | - | Y |
| LoCoMo (2024) | 个人人人 | ~10k | Y | Y | - | Y | Y |
| DialSim (2024) | 电视剧人人 | ~350k | Y | Y(<=2) | - | Y | Y |
| **LongMemEval** | **个人人机** | **115k / 1.5M** | **Y** | **Y** | **Y** | **Y** | **Y** |

LongMemEval 是唯一：
- 同时覆盖全部五项核心能力的基准
- 提供可自由扩展上下文长度的基准
- 评估知识更新能力的基准
- 聚焦任务导向人机对话的大规模记忆基准[^src-2]

[^src-1]: `data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt` -- "tables/benchmark_comparison.tex" -- "A comparison between LongMemEval and existing long-term memory benchmarks"
[^src-2]: `data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt` -- "text/2_related_work.tex" -- "existing QA-based benchmarks overlook several memory capabilities critical to long-term user-assistant interactions: synthesizing information across numerous sessions, recalling assistant side information, and reasoning about updated user details"
