---
id: lightmem-sleep-time-offline-parallel-update
title: LightMem 的"睡眠时更新"——把 LTM 整合从在线推理中解耦
status: draft
card_type: mechanism
tags: [#lightmem, #long-term-memory, #soft-update, #offline-parallel]
created_time: 2026-05-26T11:07:00+08:00
edited_time: 2026-05-26T11:07:00+08:00
edited_entity: llm
source_ids: [arxiv-lightmem]
provenance_card: ../provenance/lightmem-sleep-time-offline-parallel-update.md
aliases: ["Light3 sleep-time update", "LightMem soft update"]
related: [lightmem-three-stage-atkinson-shiffrin]
---

LightMem 把 LTM 维护问题拆成 *online soft update* 和 *offline parallel update* 两步。这是它"online cost 几乎只剩插入 + 检索"的核心来源，也是它能 outperform Mem0/MemoryOS/A-MEM 这类把 update 留在 online 的系统的工程关键。

**Online：直接 soft insert，不做合并不做删除。**

测试时，新的 STM 输出记忆条目到来时，LightMem 仅做带时间戳的"插入"——`add/delete/merge/update` 全部推迟。在线延迟因此被压到只取决于"检索 + 插入"两步，不再触发 LLM 调用。

**Offline：为每个条目预算更新队列，并行 update。**

离线触发时（"sleep"），对 LTM 中每个条目 $e_i$ 算一条独立的更新候选队列：

$$\mathcal{Q}(e_i) = \operatorname{Top}_{k}\{(e_j, \mathrm{sim}(v_i, v_j)) \mid t_j \geq t_i, j \neq i\}_{:n}$$

- 用 embedding 余弦相似度选 top-k 候选，**时间戳约束** $t_j \geq t_i$ 保证只允许"更新的"内容更新"更旧的"，对齐真实时间动态；
- 这一步只做检索（向量相似度），所以快、轻、可并行；
- 关键洞察：每个条目的更新队列是**独立**的——它们不读取彼此的写后状态——因此多个 `f_update` 调用可以**并行**执行；
- 反之，传统 memory system 因为"read-after-write / write-after-read"的依赖，被迫串行 update，延迟随更新数线性叠加。

**为什么 soft update 比 hard update 安全：**

论文给的 case study：

- History1: "Monday, 2 PM, User is planning a trip to Tokyo."
- History2: "Monday, 4 PM, User asks about trains to Kyoto."

Hard update 把"Tokyo 计划"理解成与"Kyoto 询问"冲突而 *覆盖* 掉，结果丢失了 Tokyo 上下文；soft update 只是把两条都加进去——"Tokyo trip + Kyoto inquiry"。LLM 在实时 update 操作中常错把"相关但非冲突"判为"冲突"，从而造成不可逆的信息丢失，所以宁可推后整合。

**实践含义：**

- 在长对话 agent 里，给 memory system 设计一个"sleep / quiet hours"窗口（如夜间、用户离开会话时）来批量跑 update，而不是在每个 turn 都跑；
- update 队列必须 **per-entry** 独立，才能享受并行收益；如果设计成一个全局队列，依赖关系一回来，online vs offline 的延迟差异就会缩小；
- 时间戳是必须的——既是"谁可以更新谁"的偏序约束，也是 soft 插入时的不可变锚。

**边界：**

- "sleep-time" 是工程概念，论文未严格定义触发条件——可以是"所有 entry 已插入"，也可以是"用户给的更新 trigger"；选择哪一个对延迟分布影响很大。
- 这套机制不解决"信息陈旧 / 实时一致性"——刚被 soft 插入的 entry 在下一次 offline 跑完前可能与现有条目内容矛盾，retrieve 时可能两个版本都被返回。

## References

- §3.3 Long-term Memory with Sleep-time Update（`data/raw/arxiv/arxiv-lightmem/agent_source_bundle.txt`，行 850–872）。
- Case study "Memory Update Mechanism Comparison"（行 660–683）。
- Online vs Offline cost 数字（行 596–598）：online-only token 量降 105.9× / 117.1×。

## Footnotes

- 更新队列公式见行 860–862。
- "we further impose the constraint that only entries with later timestamps are allowed to update earlier ones ($t_j \geq t_i$), which is consistent with realistic temporal dynamics."——行 864。
- 并行更新与传统串行对比：行 866–872。
- soft update 优势：
  > "an LLM might incorrectly interpret them as a conflict and delete the older memory entry, leading to irreversible information loss. Instead, the optimal operations might be to merge the information or simply add the new entry." (行 656–658)
- Case 原文出自行 666–683。
