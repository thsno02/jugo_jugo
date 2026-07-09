---
id: lightmem-pre-compression-sensory-memory
title: LightMem 预压缩感知记忆模块
status: draft
card_type: mechanism
tags: [token-compression, sensory-memory, llmlingua-2, information-filtering]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-lightmem]
evidence_basis: experimental_paper
justification: ../justification/lightmem-pre-compression-sensory-memory.md
canonical_concept: lightmem-pre-compression-sensory-memory
aliases: [Pre-Compressing Submodule, 预压缩子模块, sensory memory module, Light1]
summary: >-
  LightMem Light1 的预压缩子模块使用 LLMLingua-2（轻量 BERT 架构，<2GB GPU 显存）对原始对话 token 执行二元分类保留/丢弃决策。压缩率 r 为保留比例（0.4-0.8），阈值 tau 设为留存概率的第 r 百分位。实验表明 r 在 50%-80% 时压缩后内容的 QA 准确率与未压缩可比。该模块还支持基于交叉熵的生成式 LLM 替代方案——高条件熵 token 语义独特性更强因此被保留。
related: [lightmem-three-stage-architecture]
---

LightMem 的预压缩子模块（Light1 第一部分）设计目标是在信息进入 LLM 处理前过滤冗余 token，类似人类感知记忆的预注意过滤功能。

**核心机制**：给定原始输入 token 序列 x，压缩模型 theta（默认 LLMLingua-2）为每个 token 输出 retain/discard 二元分类 logit。保留概率为 softmax(logit) 的 retain 维度。阈值 tau 动态设为所有 token 保留概率的第 r 百分位，仅保留概率高于 tau 的 token。

**替代方案**：论文还提出基于生成式 LLM 条件熵的过滤——高条件熵 token 更不可预测，因此语义独特性更高，对记忆构建更关键。

**实验验证**：在 LongMemEval 1/5 随机采样上，r 为 0.5-0.8 时直接用压缩文本做 in-context QA 的准确率与未压缩可比，验证了 LLM 可有效理解压缩内容。[^src-1]

[^src-1]: `data/raw/arxiv/arxiv-lightmem/agent_source_bundle.txt` -- "Light1: Cognitive-inspired sensory memory" P773-807 -- "This module leverages a compression model theta to eliminate redundant tokens... P(retain x_i | x; theta) = softmax(l_i)_1"
