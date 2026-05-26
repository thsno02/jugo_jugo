---
id: graphrag-context-window-8k-optimal
title: GraphRAG 用 8K 上下文窗口反而压过 16K/32K/64K——"小窗口"更全
status: draft
card_type: source_claim
tags: [#graphrag, #context-window, #lost-in-the-middle, #sensemaking]
created_time: 2026-05-26T15:01:00+08:00
edited_time: 2026-05-26T15:01:00+08:00
edited_entity: llm
source_ids: [arxiv-graphrag]
provenance_card: ../provenance/graphrag-context-window-8k-optimal.md
aliases: ["GraphRAG 8k window", "context window ablation"]
related: [graphrag-global-sensemaking-pipeline, graphrag-root-community-token-efficiency]
---

GraphRAG 论文做的一个反直觉但被作者定为"全局默认"的设置：在做 query-time map-reduce 时，**8K 上下文窗口在所有比较里都是最优的**——比 16K / 32K / 64K 更能产出 comprehensive、diverse、empowering 的答案。

**实验数据（vs `SS` 基线 vector RAG，128K-context `gpt-4-turbo` 上跑）**：

| 维度 | 8K 平均胜率 |
|---|---|
| Comprehensiveness | **58.1%**（全维度最高） |
| Diversity | 52.4%（与大窗口持平） |
| Empowerment | 51.3%（与大窗口持平） |

而 16K/32K/64K 窗口在 comprehensiveness 上都低于 8K。

**为什么"小窗口"会赢**：

- 这是 lost-in-the-middle（Liu et al., 2023）现象的直接证据：即使模型号称 128K 上下文，**真正"利用得动"的有效注意力区间远小于宣称值**。Comprehensiveness 要求每一份信息都被对答案有贡献，因此对"中部塌陷"最敏感。
- 把窗口压到 8K 后，每次 map 调用看到的局部 community summaries 都被"读得充分"；超过 8K 反而部分信息被注意力稀释。
- map-reduce 结构本身把问题切成多个小窗口并行处理，所以单窗口缩到 8K 不会丢覆盖率——只是把"局部完整性"换"全局并行度"，对 sensemaking 任务正合适。

**操作含义（论文据此固化的默认）**：

- 论文所有 condition（C0–C3、TS、SS）在生成 community summary / community answer / global answer 时**统一用 8K window**，确保横向对比公平。
- 同样的逻辑可以挪到其他 map-reduce 长文档 / 多文档 RAG pipeline：与其堆 context 长度，不如压窗口 + 加并行度。

**边界**：

- 8K 是在 `gpt-4-turbo` 上得出的；换更小或更新的模型（更弱的中段注意力、或更好的长上下文）这个最优点可能漂移。
- 这条结论是对 **map / reduce 阶段** 的窗口选择，不是对 *graph indexing* 阶段的 chunk size（后者 600 token，由 entity recall + 自反思 gleaning 决定，见 `graphrag-self-reflection-gleaning`）。
- 衡量指标只覆盖 comprehensiveness / diversity / empowerment / directness——若任务需要"长引用 / 跨片段事实链"，8K 可能反而不够。

## References

- Appendix C "Context Window Selection"：`data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` 行 86–91。
- 论文正文 §3.1.4 Configuration 里固化为全局默认 8K：行 956。
- "Lost in the middle"参考：行 89 引用 `liu-etal:2023:tacl` 与 `kuratov2024search`。

## Footnotes

- "we tested four context window sizes: 8k, 16k, 32k and 64k. Surprisingly, the smallest context window size tested (8k) was universally better for all comparisons on comprehensiveness (average win rate of 58.1\%)"——行 89。
- "performing comparably with larger context sizes on diversity (average win rate = 52.4\%), and empowerment (average win rate = 51.3\%). Given our preference for more comprehensive and diverse answers, we therefore used a fixed context window size of 8k tokens for the final evaluation."——行 89。
- 全局默认确认："We used a fixed context window size of 8k tokens for generating community summaries, community answers, and global answers"——行 956。
