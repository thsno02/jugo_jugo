---
id: random-knowledge-displacement
title: 随机知识置换效应
status: draft
card_type: 机制现象
tags: [wicer, convergence-limit, token-budget, fact-pinning]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-wicer]
evidence_basis: experimental_paper
justification: ../justification/random-knowledge-displacement.md
canonical_concept: random-knowledge-displacement
aliases: [random knowledge displacement, knowledge displacement, 知识置换, 随机置换效应]
summary: >-
  Random knowledge displacement 是 WiCER 中 pinning 已诊断事实消耗 token 预算从而置换其他未 pinned 内容、在先前通过的探针上产生新失败的现象。这是 WiCER 改进在 1-2 次迭代后趋于平台期的主因，也是与 CEGAR 的关键分歧点(CEGAR 中精化不引入新反例)。消融实验显示随机 pinning 甚至可能损害质量。
related: []
---

随机知识置换（random knowledge displacement）是 WiCER 迭代过程中的核心限制机制：pinning 已诊断的事实会消耗 wiki 的 token 预算，将其他未被 pinned 的内容挤出，从而在先前通过的探针上产生新的失败。[^src-1]

**表现**：
- WiCER 改进在 1-2 次迭代后趋于平台期（10/17 主题在 iteration 2 达峰）
- 净改进取决于"已诊断事实恢复"与"随机置换"的平衡
- 消融实验中随机 pinning 仅带来 +0.16 改进（vs WiCER +0.95），且在某些条件下可能损害质量[^src-2]

**与 CEGAR 的关键分歧**：
在经典 CEGAR 中，精化抽象以消除伪反例不会在已验证属性上引入新的伪反例。但在 WiCER 中，pinning 事实消耗部分 token 预算，似乎会置换其他内容并创造新失败——这意味着 WiCER 的收敛是经验性的而非形式化的。[^src-3]

**实际含义**：每次失败诊断提取约 50-100 词，而每个源文档约 700 词。只要保留预算不过度挤压一般覆盖，净效应为正。

[^src-1]: `data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt` -- "WiCER / Analysis and Limitations" P886 -- "random knowledge displacement effect---fixing targeted facts displaces others---limits further improvement"
[^src-2]: `data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt` -- "Ablation" P930-937 -- "random pinning improves only +0.16...WiCER achieves +0.95"
[^src-3]: `data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt` -- "CEGAR-WiCER Mapping / Limitations" P1427-1435 -- "pinning facts consumes part of the token budget, potentially displacing other content"

[^card-6]: [[wicer-algorithm]] 的核心收敛限制
