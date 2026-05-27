---
schema: accepted_card_provenance.v3
card: ../cards/mem0-baseline-failure-modes.md
material_id: arxiv-mem0
digest_id: digest_arxiv-mem0
source_paths:
  - data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt
draft_card: ../../drafts/cards/mem0-baseline-failure-modes.md
draft_provenance: ../../drafts/provenance/mem0-baseline-failure-modes.md
similarity_result: ../../drafts/similarity/mem0-baseline-failure-modes.json
comparison_provenance: ../../drafts/comparison/mem0-baseline-failure-modes.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T11:47:00+08:00
  gate_notes: 6/6 项通过；5 个 baseline 各自失败模式 + 数字 + 论文直接判定齐备。
created_time: 2026-05-26T15:20:00+08:00
edited_time: 2026-05-27T11:47:00+08:00
edited_entity: llm
---

## 源证据

1. `data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` Table 2 第 1254–1257 行：

> "A-Mem & & 2520 & 0.668 & 1.485 & 1.410 & 4.374 & 48.38 ± 0.15%"
> "LangMem & & 127 & 17.99 & 59.82 & 18.53 & 60.40 & 58.10 ± 0.21%"
> "Zep & & 3911 & 0.513 & 0.778 & 1.292 & 2.926 & 65.99 ± 0.16%"
> "OpenAI & & 4437 & - & - & 0.466 & 0.889 & 52.90 ± 0.14%"

2. 同表第 1252 行：

> "Full-context & & 26031 & - & - & 9.870 & 17.117 & 72.90 ± 0.19%"

3. `sections/result.tex` 第 1305 行（LangMem 判定）：

> "LangMem exhibits even higher search latencies (p50: 17.99s, p95: 59.82s), rendering it impractical for interactive applications."

4. `sections/result.tex` 第 1316 行（Zep 异步图构建观察）：

> "After adding memories to Zep's system, we observed that immediate memory retrieval attempts often failed to answer our queries correctly. Interestingly, re-running identical searches after a delay of several hours yielded considerably better results."

5. `sections/result.tex` 第 1212 行（OpenAI temporal 失败定位）：

> "OpenAI notably underperforms, with scores below 15%, primarily due to missing timestamps in most generated memories despite explicit prompting in the OpenAI ChatGPT to extract memories with timestamps."

6. `sections/result.tex` 第 1313–1315 行（Zep token 通胀）：

> "Zep's memory graph consumes in excess of 600k tokens. The inflation arises from Zep's design choice to cache a full abstractive summary at every node while also storing facts on the connecting edges, leading to extensive redundancy across the graph."

## 卡片范围是否成立

本卡是 distinction 卡，把 5 个 baseline 的失败模式分别归类：

- LangMem 的 latency 判定、Zep 的 token / 异步问题、OpenAI 的 timestamp 缺失、Full-context 的延迟，**全部由论文原文直接给出**；
- A-Mem 的"高 F1 但 LLM-judge 不达标"是把 Table 1 中原始 A-Mem 行与重跑 A-Mem* 行做对比得出，结论由论文为 A-Mem* 单列 J 分这一行为本身佐证（论文说明重跑是为了在统一温度下取得可比 J 分）。
- "设计自家 memory 系统时应对五种失败模式各做防御"是引申结论，是把数据组织成可操作清单。

与已有卡 `mem0-locomo-benchmark-evaluation`（聚焦自家结果与总体相对优势）正交，不重叠。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T11:47:00+08:00
- 检查要点：
  - distinction 卡 5 个 baseline 各列失败模式 + 数字 + 论文直接判定，非标题复述。
  - 知识密度合格。
  - source_ids 含 `arxiv-mem0`，正文锚到 result.tex 第 1047-1085 / 1212 / 1252-1257 / 1305 / 1313-1318 行。
  - 含 `## References` 与 `## Footnotes`。
  - frontmatter 字段完整。
  - related 已挂上 6 张相关卡。

## 备注

- 后续可在 v3 metabolism 系列卡片里把"5 种 baseline 失败模式"映射到 memory governance 的 5 类 invariants（latency / consistency / metadata / retrieval / cost）。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/mem0-baseline-failure-modes.md`
- draft provenance: `../../drafts/provenance/mem0-baseline-failure-modes.md`
- similarity: `../../drafts/similarity/mem0-baseline-failure-modes.json`
- comparison provenance: `../../drafts/comparison/mem0-baseline-failure-modes.md`
