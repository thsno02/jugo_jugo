---
id: wicer-ablation-diagnosed-vs-random-pinning
title: WiCER 消融实验：诊断 pinning 对比随机 pinning
status: draft
card_type: 实验证据
tags: [wicer, ablation, fact-pinning, diagnosis]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-wicer]
evidence_basis: experimental_paper
justification: ../justification/wicer-ablation-diagnosed-vs-random-pinning.md
canonical_concept: wicer-ablation-diagnosed-vs-random-pinning
aliases: [WiCER ablation, diagnosed vs random pinning, 诊断pinning消融, targeted diagnosis ablation]
summary: >-
  WiCER 消融实验在 17 个 RepLiQA 主题上对比诊断 pinning 与随机 pinning。随机 pinning(从随机源文档 pin 随机 50-100 词段落)仅改进 +0.16 over blind(2.39 vs 2.23); WiCER 诊断 pinning 改进 +0.95(3.18 vs 2.23), 为 5.9x 更大增益。WiCER 在 16/17 主题获胜。唯一例外 local_education 也是 WiCER 0% recovery 的主题。确认增益来源为 targeted diagnosis 而非 pinning 机制本身。
related: []
---

WiCER 的消融实验（ablation study）隔离了诊断（diagnosis）的贡献，通过对比目标性诊断 pinning 与随机 pinning 控制条件。[^src-1]

**随机 pinning 控制条件设计**：
- 对每个 score-1 失败，从随机源文档中 pin 随机 50-100 词段落（而非诊断出的关键事实）
- 所有其他参数与 WiCER 相同
- 每个主题使用独立盲编译基线

**结果（17 个 RepLiQA 主题）**：

| 条件 | Mean 质量 | vs Blind |
|------|-----------|----------|
| Blind | 2.23 | -- |
| Random Pin | 2.39 | +0.16 |
| WiCER | 3.18 | +0.95 |

WiCER 的增益为随机 pinning 的 5.9 倍（+0.95 vs +0.16），在 16/17 主题上获胜。[^src-2]

**关键结论**：
- 增益来源为**目标性诊断**（targeted diagnosis），而非 pinning 机制本身
- 随机 pinning 的微小改进（+0.16）据推测来自偶然命中相关事实的概率
- 唯一例外 local_education 是同一个 WiCER 0% recovery 的主题，据材料推测为"compilation-resistant structure"[^src-3]

[^src-1]: `data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt` -- "Ablation: Diagnosed vs. Random Pinning" P888-937 -- Section 6.4 ablation design and results
[^src-2]: `data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt` -- "Ablation" P930-932 -- "random pinning improves only +0.16...WiCER achieves +0.95---a 5.9x larger gain"
[^src-3]: `data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt` -- "Ablation" P933-937 -- "suggesting compilation-resistant structure"

[^card-10]: 验证 [[wicer-algorithm]] 增益的来源
[^card-11]: [[random-knowledge-displacement]] 解释了为何随机 pinning 增益有限
