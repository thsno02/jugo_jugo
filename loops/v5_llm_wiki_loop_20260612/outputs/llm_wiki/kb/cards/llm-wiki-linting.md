---
id: llm-wiki-linting
title: LLM Wiki Linting 健康检查机制
status: accepted
card_type: mechanism
tags:
- linting
- data-integrity
- llm-agent
- health-check
- knowledge-quality
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- karpathy-x-launch-post
evidence_basis: practitioner_report
justification: ../justification/llm-wiki-linting.md
canonical_concept: llm-wiki-linting
aliases:
- LLM health checks
- wiki linting
- LLM lint
- 知识库健康检查
- wiki health check
summary: llm-wiki-linting LLM Wiki Linting健康检查机制 LLM对wiki执行"健康检查"以增量提升数据完整性： 发现不一致数据、用web搜索补充缺失数据(impute missing data)、发现概念间有趣连接、建议新文章候选。 超越传统代码lint：能主动生成内容、执行创造性关联发现。LLM擅长建议进一步探索问题。
related:
- llm-knowledge-base-workflow
- wiki-compilation-by-llm
- kb-lint-deterministic-validation
- lint-as-quality-driver
- llm-wiki-output-filing-back
---
Karpathy 将代码领域的 "linting" 概念迁移到知识库维护，描述 LLM 对 wiki 执行的"健康检查"操作：

**检测层（类似传统 lint）**:
- 发现不一致数据 (find inconsistent data)
- 检查整体数据完整性 (data integrity)

**生成层（超出传统 lint）**:
- 用 web 搜索补充缺失数据 (impute missing data with web searchers)
- 发现概念间"有趣连接"以生成新文章候选 (find interesting connections for new article candidates)
- 建议进一步可探索的问题

此机制超越传统代码 lint 的边界：传统 lint 仅检测规则违反，此处 LLM lint 具备主动数据生成能力（补充缺失）和创造性关联发现能力（建议新文章）。[^src-1]

作者观察："The LLMs are quite good at suggesting further questions to ask and look into" — 暗示 lint 过程本身可驱动知识库的持续增长。[^src-2] [^card-1]

[^src-1]: `data/raw/webpage/karpathy-x-launch-post/text.txt` -- "Linting" -- "I've run some LLM \"health checks\" over the wiki to e.g. find inconsistent data, impute missing data (with web searchers), find interesting connections for new article candidates, etc."
[^src-2]: `data/raw/webpage/karpathy-x-launch-post/text.txt` -- "Linting" -- "The LLMs are quite good at suggesting further questions to ask and look into"
[^card-1]: 参见 [[wiki-compilation-by-llm]] 编译阶段产出的索引为 lint 提供检查基础
