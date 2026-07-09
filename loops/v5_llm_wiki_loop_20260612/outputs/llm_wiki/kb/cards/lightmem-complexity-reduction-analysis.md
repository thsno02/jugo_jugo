---
id: lightmem-complexity-reduction-analysis
title: LightMem 复杂度降低的数学分析
status: accepted
card_type: theoretical-result
tags:
- complexity-analysis
- api-call-reduction
- token-efficiency
- compression-ratio
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-lightmem
evidence_basis: experimental_paper
justification: ../justification/lightmem-complexity-reduction-analysis.md
canonical_concept: lightmem-complexity-reduction-analysis
aliases:
- LightMem complexity analysis
- 复杂度分析
- efficiency gain formula
summary: LightMem 将基线记忆系统的 O(N) API 调用复杂度降至 O(Nr^x T / th)：N 为对话轮数、r 为压缩率、x 为压缩迭代次数、T 为每轮平均 token 数、th 为 STM 缓冲区容量。Summarization token 消耗从 N(L_sum-in + T + L_sum-out) 降至 (Nr^xT/th)(L_sum-in + th + L_sum-out)。更新
  token 从 NM1R1(L_up-in + L_up-out) 降至 (Nr^xT/th)M2R2(L_up-in + L_up-out)，其中 R2 < R1 因为 LightMem 的时间戳约束和语义相似度过滤使得触发更新的比例更低。
related:
- lightmem-three-stage-architecture
- lightmem-stm-buffer-threshold
- lightmem-pre-compression-sensory-memory
---

论文第 5 节给出了 LightMem 相对于基线记忆系统的复杂度对比分析。

**基线系统复杂度**：
- Summarization tokens: N(L_sum-in + T + L_sum-out)——每轮都触发一次摘要
- Update tokens: NM1R1(L_up-in + L_up-out)——每轮产出 M1 条目，R1 比例触发更新
- API Calls: N
- Runtime: O(N)

**LightMem 复杂度**：
- Summarization tokens: (Nr^x T / th)(L_sum-in + th + L_sum-out)——仅 buffer 满时触发
- Update tokens: (Nr^x T / th) M2 R2 (L_up-in + L_up-out)
- API Calls: Nr^x T / th
- Runtime: O(Nr^x T / th)

**效率增益来源**：
1. r^x 因子：压缩迭代后仅保留 r^x 比例的 token
2. th 因子：STM buffer 积累到阈值才触发，减少调用频率
3. R2 < R1：时间戳约束 + 语义过滤使得更新触发比例更低[^src-1]

[^src-1]: `data/raw/arxiv/arxiv-lightmem/agent_source_bundle.txt` -- "Complexity analysis about LightMem" P988-1014 -- "LightMem requires only Nr^xT/th API calls for both summarization operations, substantially reducing token usage and call frequency"
