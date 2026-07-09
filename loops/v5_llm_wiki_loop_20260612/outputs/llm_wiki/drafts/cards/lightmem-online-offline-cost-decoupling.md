---
id: lightmem-online-offline-cost-decoupling
title: LightMem 在线/离线成本解耦评估框架
status: draft
card_type: evaluation-methodology
tags: [cost-evaluation, online-vs-offline, test-time-efficiency, memory-bank-construction]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-lightmem]
evidence_basis: experimental_paper
justification: ../justification/lightmem-online-offline-cost-decoupling.md
canonical_concept: lightmem-online-offline-cost-decoupling
aliases: [online vs offline cost, 在线离线成本分离, test-time cost, OP-update]
summary: >-
  LightMem 将记忆系统效率评估分为在线测试时成本和离线成本两个视角。在线成本仅计 Light1 预压缩 + Light2 STM summarization + Light3 软插入；离线成本额外包含并行更新（OP-update）。论文报告两种口径：合计（online+offline）用于公平对比基线系统（基线的更新全在在线完成）；纯在线用于评估用户感知延迟。纯在线口径下 LightMem 效率优势更大：GPT 骨干 token 减少 31-106 倍、API 调用减少 17-159 倍；Qwen 骨干 token 减少 30-117 倍、API 调用减少 25-310 倍。
related: [lightmem-sleep-time-offline-update, lightmem-three-stage-architecture]
---

LightMem 提出了一种双口径效率评估框架来公正对比不同记忆系统：

**评估范围**：聚焦记忆库构建阶段（Memory Bank Construction）中涉及 LLM 调用的两个子过程——Summarization（f_sum）和 Update（f_update）。检索与回答阶段因各方法共享相同的 f_retrieve() 和 f_chat() 而不纳入对比。

**双口径报告**：
- **Online + Offline（合计）**：将 LightMem 的离线并行更新成本计入总量，与基线系统的在线实时更新成本直接对比——这是最保守的公平对比
- **Pure Online（纯在线）**：仅计 LightMem 测试时实际消耗——反映用户感知的交互延迟

**关键发现**：纯在线口径下优势远超合计口径，说明 LightMem 的架构设计将大部分计算从交互路径中移除而非消除。[^src-1]

[^src-1]: `data/raw/arxiv/arxiv-lightmem/agent_source_bundle.txt` -- "main results" P591-599 -- "For a fair comparison, all efficiency metrics for LightMem in the following analysis refer to the combined online and offline costs... If considering only online test-time cost, LightMem shows an even larger efficiency advantage"
