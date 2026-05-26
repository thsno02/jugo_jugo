---
schema: draft_card_provenance.v3
draft_card: ../cards/wicer-hardware-architecture-deployment.md
material_id: arxiv-wicer
digest_id: digest_arxiv-wicer
source_paths:
  - data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt
created_time: 2026-05-26T15:00:00+08:00
edited_time: 2026-05-26T15:00:00+08:00
edited_entity: llm
---

## 源证据

### Appendix B 开篇（第 1044–1051 行）

> "Our benchmark runs entirely on a single Apple M4 Pro computer (24 GB unified memory, 273 GB/s memory bandwidth). This appendix projects expected performance on discrete GPU and cloud accelerator hardware to inform deployment decisions."

### RTX 4090 投影表 tab:hw_rtx（第 1059–1075 行）

```
Metric              & M4 Pro      & RTX 4090 (est.)
Memory bandwidth    & 273 GB/s    & 1,008 GB/s
Decode throughput   & 12 tok/s    & ~53 tok/s
Cold prefill (67K)  & ~130 s      & ~26 s
Warm TTFT           & 0.86 s      & ~0.2 s
KV quant penalty    & None        & None (fused FA)
```

### RTX 4090 implications（第 1077–1095 行）

> "Decode is bandwidth-bound: The 3.7× bandwidth advantage translates to ~4.4× higher generation throughput (~53 vs. 12 tok/s) ... Prefill is compute-bound: CUDA tensor cores provide ~2,600 tok/s prefill throughput, reducing cold-start from ~130s to ~26s (5× speedup) ... KV quantization has zero penalty on CUDA: ... fused Flash Attention kernels handle 8-bit symmetric quantized KV with no dequantization overhead ... RAG advantage diminishes: ... the latency case for RAG largely disappears on desktop GPU hardware."

### Inferentia2 constraints（第 1099–1121 行）

> "Static tensor shapes: Neuron compilation requires fixed sequence lengths at compile time ... No KV cache quantization: The Neuron runtime does not expose KV cache quantization options. All KV states are stored in FP16/BF16, requiring 2× the memory of Q8 and 4× the memory of Q4 configurations ... Memory scaling: A single Inferentia2 chip has 32 GB HBM. At 67K context with FP16 KV, the cache requires ~4.5 GB ... scaling to longer contexts (128K+) would require multi-chip tensor parallelism via inf2.24xlarge (~\$12/hr) ... Throughput-oriented: Inferentia2 excels at high-batch, fixed-length workloads ... Our single-user, variable-length, long-context QA workload underutilizes the hardware."

### Deployment Recommendations 摘要（第 1147–1154 行）

> "For cached knowledge base applications—where a domain-specific corpus fits within a single context window—the M4 Pro provides a compelling cost-performance ratio with full offline capability. The RTX 4090 offers the best absolute performance for latency-sensitive deployments. Cloud accelerators like Inferentia2 are better suited for high-throughput batch inference workloads rather than the interactive, variable-length pattern characteristic of cached document QA."

## 卡片范围是否成立

本卡的范围限制在 Appendix B 的硬件投影部分；这是论文中**唯一**做跨硬件对照的章节，与算法 / WiCER / 评测主线分立，足以独立成片。

直接来自源材料：所有数字、所有定性结论。
引申部分：将三类硬件归纳为"个人 / 延迟敏感生产 / 云批推理"三套部署建议——论文 §B Summary 已有相近表述，本卡只是把它中文化并把硬件适配机制（bandwidth-bound / compute-bound / static-shape）显式拆出。

## 发表门控结果

本轮未运行。

## 备注

- 本卡与 v2 的 KV cache 相关卡片不会重叠：v2 阶段的 KV cache 讨论应聚焦机制（如 PagedAttention、Flash Attention），不会做这种"硬件部署画像"。
- 与 `wicer-fc-rag-document-count-crossover` 卡片关联：那张卡讨论"什么时候用 FC vs RAG"，本卡讨论"在哪种硬件上用"。两条问题独立但互补。
