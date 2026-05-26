---
id: lightmem-light2-topic-aware-stm
title: LightMem 的 Light2 STM——以 topic 为输入粒度的"批 summary"
status: draft
card_type: mechanism
tags: [#lightmem, #short-term-memory, #topic-granularity, #batched-summary]
created_time: 2026-05-26T15:10:00+08:00
edited_time: 2026-05-26T15:10:00+08:00
edited_entity: llm
source_ids: [arxiv-lightmem]
provenance_card: ../provenance/lightmem-light2-topic-aware-stm.md
aliases: ["Light2 STM", "topic-aware short-term memory"]
related: [lightmem-three-stage-atkinson-shiffrin, lightmem-precompress-and-topic-segmentation, lightmem-sleep-time-offline-parallel-update, lightmem-complexity-formula, memgpt-queue-eviction-policy]
---

LightMem 的第二层模块 Light2 是"中转和总结"层：它把上游 Light1 切好的 topic 段堆进 STM buffer，等达到 token 阈值 `th` 时一次性调用主干 LLM 的 `f_sum` 做总结、产出可索引的记忆条目交给 LTM。这是 LightMem 把 API 调用从 O(N) 压到 O(Nr^x T/th) 的中间一环。

**输入与输出：**

- 上游送入的是结构 `{topic, message_turns}`，`message_turns = {user_i, model_i}`；
- 一旦 STM buffer 累计的 token 数 ≥ `th`，触发 `f_sum`，生成每段的精简摘要 `sum_i`；
- 摘要被打包成 LTM 条目：`Entry_i = {topic, embedding(sum_i), user_i, model_i}`——即"topic 作分组键 / sum 的向量作检索 key / 原始 user+model 文本作可追溯证据"。

**为什么用 topic 作输入粒度**：

论文显式比较了"逐 turn / 逐 session / 逐 topic"三种粒度的代价：

- **逐 turn**：summary 调用次数等于对话回合数 N，API 成本最高；
- **逐 session**：把多个 session 直接塞进 summary，主题混杂，导致摘要错位、检索召回质量塌；
- **逐 topic**：调用次数被压到 N/th 量级，并且每次输入语义内聚 → summary 准确。

Light2 选了第三种，并把"什么时候触发 summary"绑定到 STM 的 token 阈值而非时间或回合数——这样阈值大小直接换 API 频率与摘要稠密度。

**STM 阈值 `th` 的可调性（论文 §experiments / radar 图）**：

- `th` 越大 → 触发摘要越不频繁 → token 总量、API 调用、runtime 越低（**单调下降**）；
- `th` 与 accuracy 的关系是**非单调**：太小 → buffer 利用不足，摘要太密反而引入冗余；太大 → 摘要输入太长，进入 lost-in-the-middle 区间。
- 论文最终在 LongMemEval 上 GPT-4o-mini 选 `th=512`、Qwen3-30B 选 `th=768`；ACC 的最优值依赖 backbone 模型的长上下文利用能力。

**实践含义**：

- "summary 延迟到 buffer 满"等价于把多次小调用合并成一次大调用——只要 backbone LLM 在 `th` 长度内能稳定 summary，就纯赚 API 成本。
- entry 同时保留 `user_i, model_i` 原文，所以即使 `sum_i` 抽错也能在 retrieve 阶段回到原文证据——这是"不可逆压缩 + 可追溯证据"双重保险。

**边界**：

- 这一层不主动检查"摘要是否漏了关键信息"——靠的是 Light1 已经把语义内聚的 topic 段送过来。如果 Light1 的 topic segmentation 切错（如 ablation 显示去掉它准确率掉 6.3% / 5.4%），Light2 的 summary 也会跟着错。
- `f_sum` 的 prompt 与提示工程未在正文中给出 prompt 细节（在 appendix 模板里），所以"summary 出错"是 backbone + prompt 的联合责任。

## References

- §3.2 Light2 完整描述：`data/raw/arxiv/arxiv-lightmem/agent_source_bundle.txt` 行 830–848。
- "逐 topic 优于逐 session" 的对照论述：行 846–848（"directly feeding multiple sessions can reduce subsequent API calls but often introduces inaccurate memory entries due to excessive topic mixing"）。
- STM 阈值非单调与最优依赖 backbone：行 643–650（§Analysis of the STM Threshold's Impact）。
- Category-wise 最优超参（GPT r=0.7 th=512、Qwen r=0.4 th=768）：行 1021。

## Footnotes

- 输入结构与触发条件：行 836–837 "After obtaining individual topic segments, forming an index structure of \{topic, message turns\} ... When the token count in the buffer reaches a preset threshold, we invoke LLM $f_{\text{sum}}$ to generate concise summaries"。
- Entry schema 公式：行 843–845 "$\mathrm{Entry}_i = \left\{\, \mathrm{topic},\; \mathbf{e}_i := \operatorname{embedding}(\mathrm{sum}_i),\; \mathrm{user}_i,\; \mathrm{model}_i \,\right\}$"。
- topic 粒度的优势论证："topic-constrained input granularity minimizes API calls to the greatest extent while preserving summarization accuracy and maintaining stable system performance."（行 848）
- th 与 accuracy 非单调："the effect on QA accuracy is non-monotonic. The optimal threshold for accuracy varies depending on the model and the compression ratio"（行 647–648）。
