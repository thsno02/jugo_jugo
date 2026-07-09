---
id: wicer-deployment-envelope
title: KV Cache Wiki 部署策略包络
status: draft
card_type: 实践建议
tags: [deployment, kv-cache, rag, wicer, topic-sharding]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-wicer]
evidence_basis: experimental_paper
justification: ../justification/wicer-deployment-envelope.md
canonical_concept: wicer-deployment-envelope
aliases: [deployment envelope, operational envelope for KV cache wikis, 部署包络, KV cache wiki deployment strategy]
summary: >-
  论文基于实验证据提出 KV cache wiki 部署策略: (1) <=50 文档用 full-context Q8 KV cache; (2) 文档超出上下文时用 RAG; (3) 大型语料用 WiCER 编译的 topic shards 配合 RadixAttention/Mooncake/CacheBlend 等 KV cache 共享系统。生产环境中真实查询流可替代合成探针驱动持续 wiki 精化。WiCER 相比 RAG: 质量差距缩小至 0.46 分(3.18 vs 3.64)同时 TTFT 约 12x 更快。三个未来方向: wiki-RAG 混合推理, 自适应每文档压缩, 形式化置换界。
related: []
---

论文基于实验结果提出分级部署策略（operational envelope）：[^src-1]

**三级推荐**：
1. **<=50 文档**：Full-context Q8 KV cache
   - 质量优于 RAG（如 Policygenius 4.38 vs 4.08）
   - 亚秒 TTFT
   - 无检索失败风险

2. **文档超出上下文窗口**：RAG
   - 不受上下文长度限制
   - 检索精度约 87.9%

3. **大型语料库**：WiCER 编译的 topic shards
   - 配合 KV cache 共享系统（RadixAttention, Mooncake, CacheBlend）
   - 生产查询流替代合成探针驱动持续精化
   - 质量: 3.18 vs RAG 3.64（差距 0.46）
   - TTFT: 约 12x 快于 RAG

**生产环境的关键洞察**：在部署系统中，真实查询流可作为免费、持续更新的探针集——常见问题自然浮现用户最需要的事实，驱动持续 wiki 精化而无需合成探针。[^src-2]

**三个未来方向**：
1. Wiki-RAG 混合推理：低置信度时回退 RAG
2. 自适应每文档压缩：用诊断信号为信息密集文档分配更多预算
3. 形式化置换界（displacement bounds）：提供更紧收敛保证[^src-3]

[^src-1]: `data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt` -- "Discussion and Conclusion" P940-945 -- "we recommend full-context Q8 KV cache for <=50 documents; RAG when they exceed context; and WiCER-compiled topic shards"
[^src-2]: `data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt` -- "Introduction / WiCER" P371-374 -- "real query stream could act as a free, continuously updated probe set"
[^src-3]: `data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt` -- "Discussion and Conclusion" P945 -- "Three extensions merit investigation"

[^card-16]: 综合 [[llm-wiki-pattern]], [[attention-dilution-crossover]], [[wicer-algorithm]] 的实践指导
