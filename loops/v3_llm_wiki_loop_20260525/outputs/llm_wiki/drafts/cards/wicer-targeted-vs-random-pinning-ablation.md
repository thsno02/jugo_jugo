---
id: wicer-targeted-vs-random-pinning-ablation
title: 钉机制本身只值 +0.16，是"诊断"在做事
status: draft
card_type: source_claim
tags: [#ablation, #knowledge-compilation, #wicer]
created_time: 2026-05-26T11:15:00+08:00
edited_time: 2026-05-26T11:15:00+08:00
edited_entity: llm
source_ids: [arxiv-wicer]
provenance_card: ../provenance/wicer-targeted-vs-random-pinning-ablation.md
aliases: [WiCER ablation, random pinning control, targeted diagnosis matters]
related: [wicer-cegar-compile-evaluate-refine, wicer-recovery-distribution-exceeds-fc-raw, wicer-blind-compilation-catastrophic-loss, ragchecker-tuning-knobs-saturate, ares-mock-rag-system-evaluation-design]
---

WiCER 的核心做法可以拆成两件事：(a) **pinning 机制**——把若干段 50–100 字的文本作为硬约束塞回下一轮编译；(b) **diagnosis**——这些段从哪里来。如果 (a) 单独就能修复盲编译，那论文里的复杂诊断流程其实没必要。论文做了一组对照来回答这个问题。

对照设定：保持 WiCER 全部超参不变，只把"对每条 score-1 失败提取其源文档的关键事实"换成"从一篇随机源文档里取 50–100 词的随机片段"。其余完全一致——同样的探针集合、同样的 pinning prompt、同样的编译器（Sonnet）、同样的目标压缩率。

结果（论文 Table 5，17 个 RepLiQA 主题平均）：

- 盲基线：2.23
- 随机 pinning：2.39（+0.16）
- WiCER（诊断 pinning）：3.18（**+0.95**）
- 差距：5.9×

WiCER 在 17 个主题里赢 16 个；唯一的反例是 `local_education_systems`——同一个主题在主表里也是 0% recovery，意味着这是一个"编译抵抗"的结构性问题，而不是 pinning 机制的功劳。

这条结果是论文里最反直觉的部分：随机 pinning 不是"完全没用"，它确实加了 +0.16（说明"塞回额外内容"本身能让 wiki 更稠密一点），但它远远低于诊断版的 +0.95。三条解读：

1. **诊断信号比"加密度"重要**。决定 wiki 质量的是"覆盖了哪些事实"，而不是"塞了多少字"——因为 pinned 内容从压缩预算里抢空间，覆盖错点的事实是负收益。
2. **盲基线本身有 LLM 编译器的非确定性**。表里 Blind 列 2.23 与主表的 2.17 不完全一样——论文明确说每个主题用独立的盲编译，所以基线本就会漂；这意味着 WiCER 不是在"挑了个好基线"。
3. **它给"为什么要把评测当 CEGAR 反例"提供了反事实证据**。如果一个反例是"假阳性"（随机选的），细化就没有方向；只有"先证明 fact 在 D 里、再确认它从 W_t 里掉了"这种真反例才能驱动收敛——这与 §6 里 CEGAR 的 spurious 检查严格对应。

把这条结果当作工程教训：任何"基于失败做强化"的循环都该有一个 random control，才能区分"修复的功劳"和"动作本身的功劳"。WiCER 的 5.9× 差距是设计这种 control 的范例。

## References

- WiCER 论文 §6.4 "Ablation: Diagnosed vs. Random Pinning"（`main.tex` 第 888–937 行）与 Table 5 `tab:ablation`。本卡的全部数字、唯一反例主题、"基线在两表之间漂移"的说明都直接出自该节。

## Footnotes

[^1]: `data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt` 第 930–937 行（§6.4 结尾）：
    > "Table tab:ablation shows random pinning improves only +0.16 over blind compilation, while WiCER achieves +0.95—a 5.9× larger gain, winning sixteen of seventeen topics. The sole exception (local_education) is the same topic where WiCER itself shows 0% recovery, suggesting compilation-resistant structure. These results confirm that WiCER's gains stem from targeted diagnosis, not the pinning mechanism itself."
[^2]: 同文件第 894–896 行（控制实验设定）：
    > "for each score-1 failure, a random 50–100 word passage from a random source document is pinned instead of the diagnosed critical facts. All other parameters are identical to WiCER. Each topic uses an independent blind compilation; blind baselines differ slightly from Table tab:wicer due to LLM compiler non-determinism."
