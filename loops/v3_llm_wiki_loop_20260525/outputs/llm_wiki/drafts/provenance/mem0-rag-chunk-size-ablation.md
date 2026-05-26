---
schema: draft_card_provenance.v3
draft_card: ../cards/mem0-rag-chunk-size-ablation.md
material_id: arxiv-mem0
digest_id: digest_arxiv-mem0
source_paths:
  - data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt
created_time: 2026-05-26T15:15:00+08:00
edited_time: 2026-05-26T15:15:00+08:00
edited_entity: llm
---

## 源证据

1. `data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` Table 2（result.tex 第 1218–1264 行）给出 RAG 全部 14 行数据，节选两行：

> "& \multirow{7}{*}{1} & 128 & 0.281 & 0.823 & 0.774 & 1.825 & 47.77 ± 0.23%"
> "& & 256 & 0.255 & 0.699 & 0.802 & 1.907 & 60.97 ± 0.20%"
> "& & 8192 & 0.288 & 1.124 & 2.312 & 9.942 & 60.53 ± 0.16%"

—— 表证：k=1 chunk=128 → J=47.77；k=2 chunk=256 → J=60.97（甜点）；k=2 chunk=8192 → J=60.53 但 p95 latency 9.942s。

2. 同表 Mem0 / Mem0g 行（第 1259–1260 行）：

> "Mem0 & & 1764 & 0.148 & 0.200 & 0.708 & 1.440 & 66.88 ± 0.15%"
> "Mem0g & & 3616 & 0.476 & 0.657 & 1.091 & 2.590 & 68.44 ± 0.17%"

3. `sections/experiment_setup.tex` 第 1034–1035 行（RAG 设置）：

> "we segment each conversation into fixed-length chunks (128, 256, 512, 1024, 2048, 4096, and 8192 tokens), where 8192 is the maximum chunk size supported by our embedding model. All chunks are embedded using OpenAI's text-embedding-small-3 ... we set k ∈ {1,2}: ... We avoid k>2 since the average conversation length (26000 tokens) would be fully covered, negating the benefits of selective retrieval."

4. `sections/result.tex` 第 1297 行（关键对比断言）：

> "Even the strongest RAG approach peaks at around 61% in the J metric, whereas Mem0 reaches 67%—about a 10% relative improvement—and Mem0g reaches over 68%, achieving around a 12% relative gain."

## 卡片范围是否成立

本卡严格围绕 RAG ablation：

- 数据全部来自 Table 2，**没有引申**之外的数字；
- "非单调曲线"是把 7 个 chunk 数字一字排开后的直接观察，论文未明文说"非单调"但表格自证；
- "10% / 12% relative improvement" 与 J 绝对差由论文原文 §4.2 给出；
- "$k>2$ 退化成 full-context 是 LOCOMO-specific 的"为引申结论，但有"average 26000 tokens"作为依据。

已有卡片 `mem0-locomo-benchmark-evaluation` 提到 RAG 最优配置一行（"最强 RAG 配置（k=2, chunk=256）J ≈ 60.97"）但未展开整张扫表与时延-质量权衡。本卡补全。

## 发表门控结果

本轮未运行。

## 备注

- 与 v2 已有卡片不重叠。
- 后续若做"何时该用 RAG / 何时该用 memory layer"的 distinction 卡，可把本卡数据当锚点。
