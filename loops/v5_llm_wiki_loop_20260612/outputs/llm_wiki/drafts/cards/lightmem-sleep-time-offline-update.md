---
id: lightmem-sleep-time-offline-update
title: LightMem 睡眠时离线并行更新机制
status: draft
card_type: mechanism
tags: [long-term-memory, offline-update, parallel-processing, sleep-consolidation, soft-update]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-lightmem]
evidence_basis: experimental_paper
justification: ../justification/lightmem-sleep-time-offline-update.md
canonical_concept: lightmem-sleep-time-offline-update
aliases: [sleep-time update, 睡眠时更新, offline parallel update, soft update, Light3, LTM module]
summary: >-
  LightMem Light3 将记忆更新从在线推理中解耦：测试时新记忆条目仅执行"软更新"（带时间戳直接插入 LTM），不触发昂贵的检索-对比-合并操作。离线阶段为每条记忆条目构建更新队列 Q(e_i) = Top_k{(e_j, sim(v_i, v_j)) | t_j >= t_i, j != i}，仅允许时间戳更晚的条目更新更早的条目。由于各队列更新目标独立，可并行执行 f_update()，相比串行在线更新，GPT 骨干减少约 5 倍延迟、Qwen 骨干减少约 8 倍延迟。该设计避免了 LLM 实时更新中因错误判断冲突而导致的不可逆信息丢失。
related: [lightmem-three-stage-architecture, lightmem-stm-buffer-threshold]
---

LightMem 的 Light3 模块（长期记忆）通过两阶段策略将更新成本从推理时延中剥离：

**在线软更新**：测试时记忆条目到达后直接插入 LTM（附带时间戳），不执行任何检索或合并操作。这将交互延迟降至最低。

**离线并行更新**：当所有条目插入完毕或触发更新信号时：
1. 为 LTM 中每个条目 e_i 计算更新队列 Q(e_i)——在所有时间戳 >= t_i 的条目中检索语义最相似的 top-k 个
2. 时间戳约束（t_j >= t_i）确保更新方向与时间因果一致
3. 由于各条目的更新队列互相独立，所有 f_update() 可并行执行

**Case Study 对比**：传统硬更新中 LLM 可能将"用户计划东京旅行"和"用户问去京都的火车"误判为冲突并删除前者。LightMem 软更新保留完整上下文——"东京旅行 + 京都问询"并存。[^src-1] [^src-2]

[^src-1]: `data/raw/arxiv/arxiv-lightmem/agent_source_bundle.txt` -- "Light3: Long-term Memory with Sleep-time Update" P851-873 -- "At test time, when memory entries arrive, LightMem directly inserts them into LTM with soft updates... updates can be executed in parallel"
[^src-2]: `data/raw/arxiv/arxiv-lightmem/agent_source_bundle.txt` -- "Analysis of Sleep-Time Update" P653-683 -- "LLMs can be unreliable when tasked with complex real-time update operations... LightMem performs only incremental additions through soft updates"
