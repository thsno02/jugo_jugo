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
related: [lightmem-three-stage-atkinson-shiffrin, lightmem-light2-topic-aware-stm, lightmem-sleep-time-offline-parallel-update, lightmem-precompress-and-topic-segmentation, mem0-locomo-benchmark-evaluation]
---

LightMem 论文的 §"Complexity analysis" 给出了一张严格的成本对比表，把"主流 memory system"和 LightMem 在 summary / update / API calls / runtime 四项上的渐进复杂度并排放出来。这张表是其他"LightMem 比 baseline 便宜 X 倍"的实测数字的解释根因。

**符号清单（论文 Appendix 表 1）：**

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

**降本的三处来源（论文叙述）：**

1. **预压缩**：原始 token `T` 被 `r^x` 次压缩成 `r^x·T`——`r=0.6, x=1` 时只剩 60%。
2. **STM 阈值聚合**：不再每个 turn 调 summary，而是攒到 `th` token 再调一次——summary 调用次数从 `N` 降到 `Nr^x T/th`。`th=512, T=200, r=0.6, x=1` 时大约 5–6 倍减少。
3. **离线并行更新（见 `lightmem-sleep-time-offline-parallel-update`）**：`M_2·R_2 < M_1·R_1`——更严的 top-k + 时间戳约束让"触发更新的比例"显著下降；并行化把同样的 update 串行延迟换成并行延迟。

**实测对照（LongMemEval-S 上 GPT-4o-mini）：**

- A-MEM total tokens 1,605.81k vs LightMem(r=0.7,th=512) 28.25k —— ~57× 降低；
- A-MEM API calls 986.55 vs LightMem 18.43 —— ~54× 降低；
- A-MEM runtime 5132s vs LightMem 284s —— ~18× 降低。

这与公式预期的 `O(N) / O(Nr^x T/th)` 比值（`th/(r^x T)` ≈ 512/(0.7·30) ≈ 24×）数量级一致——剩下的差距来自 `M_2·R_2` 也比 `M_1·R_1` 显著小。

**操作含义**：

- `r` 越小（压得越狠）越省；但 ACC 在 `r ≤ 0.4` 时也开始掉——论文报告 r=0.6 是 ACC 平均最优。
- `th` 越大越省；但 ACC 非单调，最优 `th` 与 backbone 长上下文能力挂钩。
- **`x`（压缩迭代次数）是隐藏放大器**：LongMemEval 因为输入冗长，单次压缩往往不够，会触发多次 → `r^x` 比单次 `r` 还小。这也是 LightMem 在 LongMemEval 比在 LoCoMo 的 token 降幅更夸张的原因（106× / 117× vs 20.92×）。

**边界**：

- 公式是渐进的，不计入 LLMLingua-2 本身的预压缩耗时与 GPU 资源——论文承诺 < 2GB GPU 显存、runtime 忽略不计，但这一前提对小服务不一定成立。
- baseline 列代表的是"每个 turn 都 summary + 触发 online update"的最坏情况；某些 baseline（如 MemoryOS）介于二者之间，公式不完全适用。

## References

- §Complexity analysis about LightMem 完整章节：`data/raw/arxiv/arxiv-lightmem/agent_source_bundle.txt` 行 989–1014。
- 符号定义（Appendix Table `tab:notation`）：行 300–326。
- 实测对照（LongMemEval-S 主结果）：行 1271–1290（表 `tab:memory_comparison` 的 GPT 分区）。

## Footnotes

- LightMem 复杂度行："LightMem & $\frac{N r^x T}{th}(L_{\text{sum-in}} + th + L_{\text{sum-out}})$ & $\frac{N r^x T}{th} M_2 R_2 (L_{\text{up-in}} + L_{\text{up-out}})$ & $\frac{N r^x T}{th}$ & $O\Big(\frac{N r^x T}{th}\Big)$"（行 1003）。
- "Summarization is triggered only when the buffer reaches capacity, yielding $\frac{Nr^x T}{th}$ summarization calls"——行 1012。
- "Each summarization produces $M_2$ memory entries, but stricter retrieval constraints, including semantic similarity and timestamp filtering, reduce the fraction $R_2$ that trigger updates."——行 1012。
- `x` 多次压缩成因（LongMemEval-S 频发）："In LightMem, the *pre-compress* module may be invoked multiple times for the same message to remove redundancy until the message is sufficiently compact. This occurs frequently in datasets such as \textbf{LongMemEval}."——行 313。
