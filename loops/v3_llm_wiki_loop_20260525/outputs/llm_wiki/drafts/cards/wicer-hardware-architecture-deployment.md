---
id: wicer-hardware-architecture-deployment
title: WiCER 跨硬件部署画像：M4 Pro / RTX 4090 / Inferentia2
status: draft
card_type: distinction
tags: [#kv-cache, #hardware, #inference, #deployment, #wicer]
created_time: 2026-05-26T15:00:00+08:00
edited_time: 2026-05-26T15:00:00+08:00
edited_entity: llm
source_ids: [arxiv-wicer]
provenance_card: ../provenance/wicer-hardware-architecture-deployment.md
aliases: [WiCER hardware projection, M4 Pro vs RTX 4090 vs Inferentia2, cached knowledge serving hardware]
related: [wicer-fc-rag-document-count-crossover]
---

## 主张

WiCER 论文 Appendix B 给出了"cached knowledge base QA"工作负载的跨硬件部署对照，结论与"用 GPU 越大越好"的直觉相反——**Apple M4 Pro 的可用性能 / 成本比对个人或单实例 KV-cache 部署最优；RTX 4090 是延迟敏感场景的最佳绝对性能；Inferentia2 对该工作负载结构性不适配**。

## 三套硬件画像

| 因素 | M4 Pro | RTX 4090 | Inferentia2 |
| --- | --- | --- | --- |
| KV 量化支持 | Q4 / Q8 | Q8 (native) | None（仅 FP16/BF16） |
| 可变长 context | ✓ | ✓ | 受限（需固定形状） |
| 67K 暖 TTFT | 0.86 s | ~0.2 s | ~0.3 s |
| 解码吞吐 | 12 tok/s | ~53 tok/s | ~40 tok/s |
| 硬件成本 | $2,400 | $1,600 | $1.58/hr |
| 离线可用 | ✓ | ✓ | ✗ |

## 三条非平凡机制

1. **解码受 bandwidth-bound**：RTX 4090 1,008 GB/s vs M4 Pro 273 GB/s（3.7×），换来 ~4.4× 的生成吞吐（53 vs 12 tok/s），因为单 batch autoregressive decode 是内存带宽瓶颈。
2. **Prefill 受 compute-bound**：CUDA tensor cores 提供 ~2,600 tok/s prefill，cold-start 67K context 从 M4 的 ~130s 降到 ~26s（5×）；暖 TTFT 跌到 0.2s 以下，**此时 RAG 的延迟优势消失**——"the latency case for RAG largely disappears on desktop GPU hardware"[^1]。
3. **CUDA 下 Q8 KV 零代价**：fused Flash Attention kernel 处理 8-bit 对称量化 KV 无 dequantization 开销，所以 CUDA 上推荐 Q8（2× 显存节省）而非 Apple Silicon 下需要的 Q4（4×）。

## Inferentia2 为什么结构性不适配

- **静态张量形状**：Neuron compilation 要求固定 seq length，可变长输入需要 padding 或多 buckets，浪费算力；
- **无 KV 量化**：所有 KV 走 FP16/BF16，需 2× Q8 / 4× Q4 显存；
- **吞吐导向硬件**：擅长高 batch、固定长度（embedding/classification），单用户、可变长、长上下文 QA 利用率低。
- 单卡 32GB HBM 在 67K context + Llama 3.1 8B 下需要 ~4.5 GB KV cache，>128K 要 inf2.24xlarge (~\$12/hr) 多卡 TP。

## 部署建议（原文 §B summary）

- **个人 / 单实例 cached wiki**：M4 Pro 性价比最高 + 完全离线；
- **延迟敏感生产**：RTX 4090 最佳绝对性能（warm TTFT < 0.2s，decode 50+ tok/s）；
- **云加速器**：Inferentia2 适合高 batch 批推理 workload，**不适合**交互式可变长 cached QA。

## 边界

- 数字是 Appendix B 的 **projection**，不是 RTX 4090 / Inferentia2 的实测；M4 Pro 是论文实测平台。
- "RAG 延迟优势消失"假设 RAG pipeline 至少 1-2s（embedding + retrieval + prompt 构造）；在 lean 实现下这条阈值可能下移。
- 硬件成本是 2026 年挂牌价，云价格按 inf2.xlarge spot 估算。

## References

- §B "Hardware Architecture Projections"：`data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt` 第 1044–1154 行。
- Table tab:hw_rtx（RTX 4090 投影）：第 1059–1075 行。
- Table tab:hw_summary（三硬件总对照）：第 1128–1146 行。
- §B Deployment Recommendations：第 1147–1154 行。

## Footnotes

[^1]: 第 1090–1095 行（RTX 4090 implications）：
    > "RAG advantage diminishes: With 0.2s warm TTFT on full-context vs. ~1–2s RAG pipeline latency (embedding + retrieval + prompt construction), the latency case for RAG largely disappears on desktop GPU hardware."

[^2]: 第 1086–1091 行（CUDA Q8 零代价）：
    > "KV quantization has zero penalty on CUDA: Unlike Metal, CUDA's fused Flash Attention kernels handle 8-bit symmetric quantized KV with no dequantization overhead. Q8 KV is therefore recommended on CUDA, providing 2× memory savings without the 4× compression needed on Apple Silicon."

[^3]: 第 1103–1121 行（Inferentia2 architectural constraints）："Static tensor shapes ... No KV cache quantization ... Memory scaling ... Throughput-oriented"。
