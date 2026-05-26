---
id: lightmem-three-stage-atkinson-shiffrin
title: LightMem 把 Atkinson–Shiffrin 三级人类记忆移植成 LLM agent 的三层记忆架构
status: draft
card_type: mechanism
tags: [#memory-system, #lightmem, #atkinson-shiffrin, #agent-memory]
created_time: 2026-05-26T11:05:00+08:00
edited_time: 2026-05-26T11:05:00+08:00
edited_entity: llm
source_ids: [arxiv-lightmem]
provenance_card: ../provenance/lightmem-three-stage-atkinson-shiffrin.md
aliases: ["LightMem architecture", "human-memory-inspired LLM memory"]
related: [lightmem-precompress-and-topic-segmentation, lightmem-light2-topic-aware-stm, lightmem-sleep-time-offline-parallel-update, lightmem-complexity-formula, memgpt-virtual-context-os-analogy, memgpt-main-vs-external-context]
---

LightMem（Fang et al., ZJU + NUS, ICLR 2026 投稿）把 Atkinson–Shiffrin 人类记忆模型的三级结构——感觉记忆、短期记忆（STM）、长期记忆（LTM）——直接映射成 LLM agent 的三个独立模块，目的不是提精度的极限，而是在已有 memory system（Mem0、A-MEM、MemoryOS、LangMem）"高效精度但极高 overhead"之间找到帕累托更优的点。

**三模块的分工与产物：**

- **Light1：感觉记忆模块（cognition-inspired sensory memory）。** 用 LLMLingua-2（BERT 类 < 2GB 显存）做 token 级的 *预压缩*，按保留概率打分，留下比例 r 的 token；满 buffer 后触发"基于注意力 + 相似度"的 *话题分段*。负责"过滤冗余 + 切出语义单元"。
- **Light2：短期记忆模块（topic-aware STM）。** 累计若干 topic 段直到 STM token 阈值 th，然后调用主干 LLM 的 `f_sum` 一次性把整段 STM 总结成结构化记忆条目（schema：`{topic, sum, embedding, user, model}`），再灌入 LTM。topic 约束的输入粒度是为了同时压缩 API 调用次数和保持总结准确。
- **Light3：带"睡眠时更新"的长期记忆（LTM with sleep-time update）。** 在线只做 *soft update*（直接插入带时间戳的新条目）；真正的 add/delete/merge 都集中到离线触发的 *parallel update* 里，对每个条目预计算"可能更新它的 top-k 候选队列"，多个独立队列并行跑 `f_update`。

**为什么这三层映射有意义：**

- 主流 memory system 把 *summary* 和 *update* 都放在 online，导致 test-time latency 和 token 成本随 N（对话回合数）线性增长（O(N) API calls）；
- LightMem 通过预压缩降到 r^x·T、又通过 STM 阈值 th 进一步把调用频率降到 N·r^x·T/th；
- 把 update 整体从在线挪到离线，online latency 几乎只剩"插入 + 检索"。

**关键评测数字：**

- LongMemEval：用 GPT-4o-mini 和 Qwen3-30B 两种 backbone，accuracy 比最强基线（A-MEM）提升 2.09–6.40%（GPT）/ 最多 7.67%（Qwen）；token 总量降 10–38×（GPT）/ 6.9–21.8×（Qwen）；runtime 降 2.9–12.4× / 1.6–6.3×。
- 若只看 online test-time：token 量降到 31.4–105.9×（GPT）/ 30.1–117.1×（Qwen），API calls 降 17.1–159.4× / 24.8–309.9×。
- LoCoMo：accuracy 提升 6.10–18.12%（GPT）/ 4.41–29.29%（Qwen），API calls 降 13.29–39.78× / 12.96–55.48×。

**边界与误用：**

- "lightweight" 是相对其他 memory system 而言；vs. naive RAG / Full Text，它在 *Single-Assistant* 这种问句简单的类目反而劣（GPT 32.14% vs naive 98.21%），因为 topic 重组打散了原句证据。category-wise accuracy 表显式承认这一点。
- 三模块的最优超参（r, th）依赖 backbone：GPT 4o-mini 用 r=0.7, th=512；Qwen3-30B 用 r=0.4, th=768。换模型必须重新调。

## References

- Fang et al., "LightMem: Lightweight and Efficient Memory-Augmented Generation"，ICLR 2026 投稿。架构图与三模块组合：`data/raw/arxiv/arxiv-lightmem/agent_source_bundle.txt` 行 131–139（Figure 1 caption）、行 762–771（§3 lightmem architecture）。
- 主结果：行 594–601、行 749–759（abstract + introduction）。
- Category-wise accuracy 反例：行 1043–1063。

## Footnotes

- 三模块在源代码档对应小节：Light1 §3.1（行 773–828）、Light2 §3.2（行 830–848）、Light3 §3.3（行 850–873）。
- 复杂度对比表（行 998–1014）：Baselines 是 O(N)，LightMem 是 O(N·r^x·T/th)。
- LongMemEval 结果数字直接引自 §experiments（行 594–599）。
- LoCoMo 结果数字引自 §experiments（行 601）。
- 超参选择：行 1021"For GPT, LightMem is configured with parameters r=0.7 and th=512; for Qwen, LightMem is configured with r=0.4 and th=768."
