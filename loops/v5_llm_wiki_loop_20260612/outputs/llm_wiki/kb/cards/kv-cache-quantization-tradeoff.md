---
id: kv-cache-quantization-tradeoff
title: KV Cache 量化的规模依赖权衡
status: accepted
card_type: 实验发现
tags:
- kv-cache
- quantization
- apple-silicon
- inference-optimization
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-wicer
evidence_basis: experimental_paper
justification: ../justification/kv-cache-quantization-tradeoff.md
canonical_concept: kv-cache-quantization-tradeoff
aliases:
- KV cache quantization
- KV量化
- Q4 vs Q8 KV cache
- KV cache precision tradeoff
summary: 'KV cache 量化(Q4/Q8)的质量影响依赖于上下文规模。在 30 文档/67K tokens(Policygenius)上 Q4 与 Q8
  质量相当(4.38 vs 4.35, 差异<0.03)且 TTFT 略优。但在 80 文档/55-95K tokens(RepLiQA)上 Q4 质量退化: Q8
  在 13/14 主题上胜出(mean delta +0.14), Q4 score-1 率更高(20.9% vs 17.3%)。降低 KV 精度似乎加剧了规模上的
  lost-in-the-middle 效应。CUDA 原生 Flash Attention 内核可无开销处理 Q8 KV。'
related:
- fc-kv-cache-latency-advantage
- wicer-deployment-envelope
---

KV cache 量化对推理质量的影响呈规模依赖（scale-dependent）特征。[^src-1]

**小规模（30 文档, 67K tokens, Policygenius）**：
- Q4K/Q4V, Q8K/Q4V, Q8K/Q8V 三种配置质量差异 <0.03 分（4.38, 4.36, 4.35）
- Q4 提供 4x 内存节省（相比 FP16）且 TTFT 略优（0.857s vs 0.876s）
- 结论：Apple Silicon Metal 架构在此规模下高效处理 KV 反量化[^src-2]

**大规模（80 文档, 55-95K tokens, RepLiQA）**：
- Q8 在 13/14 主题上质量优于 Q4（mean delta = +0.14, range -0.01 to +0.28）
- Q4 产生更多 score-1 失败（20.9% vs 17.3%）
- Q4 仍提供 4.8% TTFT 改善（0.989s vs 1.040s）
- 降低 KV 精度似乎加剧了 attention dilution 效应[^src-3]

**硬件差异**：CUDA 的 fused Flash Attention 内核原生处理 8-bit 对称量化 KV 无反量化开销；因此 CUDA 上推荐 Q8 KV（2x 节省无质量损失）。Apple Silicon Metal 需要 Q4 以获得内存优势但承担质量风险。[^src-4]

[^src-1]: `data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt` -- "Multi-Domain Results / KV cache quantization on RepLiQA" P1260-1268 -- "Q4 degrades quality...reduced KV precision apparently exacerbates the lost in the middle effect"
[^src-2]: `data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt` -- "KV Cache Quantization Ablation" P1180-1214 -- Table kvquant
[^src-3]: `data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt` -- "Multi-Domain Results" P1260-1268 -- "Q8 outscores Q4 in 13 of 14 topics"
[^src-4]: `data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt` -- "Hardware Architecture Projections" P1086-1094 -- "CUDA's fused Flash Attention kernels handle 8-bit symmetric quantized KV with no dequantization overhead"

[^card-9]: 与 [[attention-dilution-crossover]] 相关: Q4 加剧规模上的注意力稀释
