---
id: lightmem-complexity-formula
title: LightMem 的成本公式——O(N) 降到 O(Nr^x T/th) 的来源拆解
status: accepted
card_type: source_claim
tags: [#lightmem, #complexity-analysis, #cost-model, #api-calls]
created_time: 2026-05-26T15:11:00+08:00
edited_time: 2026-05-28T10:14:00+08:00
edited_entity: llm
source_ids: [arxiv-lightmem]
provenance_card: ../provenance/lightmem-complexity-formula.md
aliases: ["LightMem cost model", "LightMem complexity"]
related: [lightmem-precompress-and-topic-segmentation, lightmem-light2-topic-aware-stm, lightmem-sleep-time-offline-parallel-update, longmemeval-benchmark-construction-pipeline, locomo-very-long-term-dialogue-dataset]
---

LightMem 论文的 §"Complexity analysis" 给出了一张严格的成本对比表，把"主流 memory system"和 LightMem 在 summary / update / API calls / runtime 四项上的渐进复杂度并排放出来[^src1]。这张表是其他"LightMem 比 baseline 便宜 X 倍"的实测数字的解释根因。

**符号清单（论文 Appendix 表 1）[^src2]：**

- `N`：对话总回合数；`T`：每回合平均 token 数；
- `r`：单次压缩保留率（pre-compress 之后 token 数 = `r·T`）；`x`：每条消息触发的压缩迭代次数；
- `th`：STM buffer 容量（token）；
- `L_sum-in / L_sum-out`：summary 单次调用的 input/output prompt 模板长度；
- `M_1, R_1`：baseline 单次 summary 产出的 memory entry 数 / 触发 update 的比例；`M_2, R_2`：LightMem 对应值（更小，因为时间戳 + 相似度约束更严）。

**复杂度对照（论文 Table `tab:complexity_comparison`）：**

| 方法 | Summary tokens | Update tokens | API Calls | Runtime |
|---|---|---|---|---|
| Baselines | `N(L_sum-in + T + L_sum-out)` | `N·M_1·R_1·(L_up-in + L_up-out)` | `N` | `O(N)` |
| **LightMem** | `(Nr^x T/th)·(L_sum-in + th + L_sum-out)` | `(Nr^x T/th)·M_2·R_2·(L_up-in + L_up-out)` | `Nr^x T/th` | `O(Nr^x T/th)` |

**降本的三处来源（论文叙述）[^src3]：**

1. **预压缩**：原始 token `T` 被 `r^x` 次压缩成 `r^x·T`——`r=0.6, x=1` 时只剩 60%。来源即 Light1[^v3-1]。
2. **STM 阈值聚合**：不再每个 turn 调 summary，而是攒到 `th` token 再调一次——summary 调用次数从 `N` 降到 `Nr^x T/th`[^src4]。`th=512, T=200, r=0.6, x=1` 时大约 5–6 倍减少。来源即 Light2[^v3-2]。
3. **离线并行更新**：`M_2·R_2 < M_1·R_1`[^src5]——更严的 top-k + 时间戳约束让"触发更新的比例"显著下降；并行化把同样的 update 串行延迟换成并行延迟。来源即 Light3[^v3-3]。

**实测对照（LongMemEval-S 上 GPT-4o-mini）[^src6]：**

- A-MEM total tokens 1,605.81k vs LightMem(r=0.7,th=512) 28.25k —— ~57× 降低；
- A-MEM API calls 986.55 vs LightMem 18.43 —— ~54× 降低；
- A-MEM runtime 5132s vs LightMem 284s —— ~18× 降低。

这与公式预期的 `O(N) / O(Nr^x T/th)` 比值（`th/(r^x T)` ≈ 512/(0.7·30) ≈ 24×）数量级一致——剩下的差距来自 `M_2·R_2` 也比 `M_1·R_1` 显著小。其中 LongMemEval-S 的"输入冗长"特性是 LightMem 在 LongMemEval 上 token 降幅比在 LoCoMo 更夸张的直接原因[^v3-4]。

**操作含义**：

- `r` 越小（压得越狠）越省；但 ACC 在 `r ≤ 0.4` 时也开始掉——论文报告 r=0.6 是 ACC 平均最优。
- `th` 越大越省；但 ACC 非单调，最优 `th` 与 backbone 长上下文能力挂钩。
- **`x`（压缩迭代次数）是隐藏放大器**：LongMemEval 因为输入冗长，单次压缩往往不够，会触发多次 → `r^x` 比单次 `r` 还小[^src7]。这也是 LightMem 在 LongMemEval 比在 LoCoMo[^v3-5] 的 token 降幅更夸张的原因（106× / 117× vs 20.92×）。

**边界**：

- 公式是渐进的，不计入 LLMLingua-2 本身的预压缩耗时与 GPU 资源——论文承诺 < 2GB GPU 显存、runtime 忽略不计，但这一前提对小服务不一定成立。
- baseline 列代表的是"每个 turn 都 summary + 触发 online update"的最坏情况；某些 baseline（如 MemoryOS）介于二者之间，公式不完全适用。

## Footnotes

[^src1]: `data/raw/arxiv/arxiv-lightmem/agent_source_bundle.txt` — 行 989–1014（§Complexity analysis 完整章节）—— 给出 baselines vs LightMem 的 summary/update/API calls/runtime 四列对比表。
[^src2]: `data/raw/arxiv/arxiv-lightmem/agent_source_bundle.txt` — 行 300–326（Appendix Table `tab:notation`）—— 符号 `N, T, r, x, th, L_*` 的定义。
[^src3]: `data/raw/arxiv/arxiv-lightmem/agent_source_bundle.txt` — 行 1003 — "LightMem & $\frac{N r^x T}{th}(L_{\text{sum-in}} + th + L_{\text{sum-out}})$ & $\frac{N r^x T}{th} M_2 R_2 (L_{\text{up-in}} + L_{\text{up-out}})$ & $\frac{N r^x T}{th}$ & $O\Big(\frac{N r^x T}{th}\Big)$"。
[^src4]: `data/raw/arxiv/arxiv-lightmem/agent_source_bundle.txt` — 行 1012 — "Summarization is triggered only when the buffer reaches capacity, yielding $\frac{Nr^x T}{th}$ summarization calls"。
[^src5]: `data/raw/arxiv/arxiv-lightmem/agent_source_bundle.txt` — 行 1012 — "Each summarization produces $M_2$ memory entries, but stricter retrieval constraints, including semantic similarity and timestamp filtering, reduce the fraction $R_2$ that trigger updates."
[^src6]: `data/raw/arxiv/arxiv-lightmem/agent_source_bundle.txt` — 行 1271–1290（表 `tab:memory_comparison` GPT 分区）—— A-MEM vs LightMem 在 LongMemEval-S 上的具体数字。
[^src7]: `data/raw/arxiv/arxiv-lightmem/agent_source_bundle.txt` — 行 313 — "In LightMem, the *pre-compress* module may be invoked multiple times for the same message to remove redundancy until the message is sufficiently compact. This occurs frequently in datasets such as \textbf{LongMemEval}."
[^v3-1]: [lightmem-precompress-and-topic-segmentation](lightmem-precompress-and-topic-segmentation.md) — Light1 是 `r^x` 来源。
[^v3-2]: [lightmem-light2-topic-aware-stm](lightmem-light2-topic-aware-stm.md) — Light2 阈值 th 决定 summary 调用频率。
[^v3-3]: [lightmem-sleep-time-offline-parallel-update](lightmem-sleep-time-offline-parallel-update.md) — Light3 时间戳 + top-k 是 `M_2·R_2 < M_1·R_1` 的机制根因。
[^v3-4]: [longmemeval-benchmark-construction-pipeline](longmemeval-benchmark-construction-pipeline.md) — LongMemEval 由多 session 拼接而成，平均长度远超 LoCoMo，使 `x` 显著放大。
[^v3-5]: [locomo-very-long-term-dialogue-dataset](locomo-very-long-term-dialogue-dataset.md) — LoCoMo 的对话长度参考点。
