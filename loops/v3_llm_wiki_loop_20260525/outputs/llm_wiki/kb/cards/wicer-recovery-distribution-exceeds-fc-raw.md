---
id: wicer-recovery-distribution-exceeds-fc-raw
title: WiCER 在三个主题上超越 FC raw 基线（>100% recovery）
status: accepted
card_type: source_claim
tags: [#llm-wiki, #knowledge-compilation, #wicer, #empirical-result]
created_time: 2026-05-26T15:00:00+08:00
edited_time: 2026-05-28T11:55:00+08:00
edited_entity: llm
source_ids: [arxiv-wicer]
provenance_card: ../provenance/wicer-recovery-distribution-exceeds-fc-raw.md
aliases: [WiCER recovery distribution, super-recovery topics, WiCER beats FC raw]
related: [wicer-cegar-compile-evaluate-refine, wicer-fc-rag-document-count-crossover, wicer-blind-compilation-catastrophic-loss, wicer-targeted-vs-random-pinning-ablation]
---

## 主张

WiCER 论文最容易被忽略的非平凡结果不是"平均 80% recovery"，而是 **recovery 率分布从 0% 到 125% 跨度极宽，且有三个主题在两次迭代后超过了 FC raw 基线**[^src3]。这违背了"压缩+pinning 最多只能逼近原文质量"的直觉——它说明在某些语料上，**带反馈的有损编译可以比直接读所有 80 篇原文更好**。WiCER 算法骨架本身见 CEGAR 流水线卡[^v3-1]。

## 三个超越 FC raw 的主题（Table tab:wicer）

| Topic | Blind | Best WiCER | FC raw | Recovery |
| --- | --- | --- | --- | --- |
| news_stories | 2.50 / 40.0% | **3.61** / 11.2% | 3.60 | **101%** |
| local_arts_&_culture | 1.65 / 73.8% | **3.61** / 15.0% | 3.34 | **116%** |
| small_medium_ent. | 2.21 / 56.2% | **3.75** / 13.8% | 3.44 | **125%** |

后两个主题绝对收益 +1.96 / +1.54，对应论文原话："Topics with many entity-specific facts benefit most in absolute terms (+1.96 for local_arts_and_culture, +1.54 for small_and_medium_enterprises)."[^src1]

## 为什么会超过 FC raw

机制可解释：FC raw 在 80 篇 RepLiQA 文档上受 **lost in the middle** 折磨（mean score-1 17.3%）[^v3-2]；当 WiCER 用诊断 pinning 把"实体特定事实"明确钉进 wiki，模型在更短上下文里反而能更可靠地找到它们，attention dilution 的代价 > 信息损失的代价。换句话说，**压缩本身不是单调有害**——只要 (a) 关键事实没丢、(b) 上下文密度提升带来的注意力收益大，编译后的 wiki 可以在 lost-in-the-middle 主题上反超 raw 全文。

## 分布的另一极：单调失败的主题

另一极是 `local_education_systems`：盲基线 2.41、score-1 38.8%（17 个主题里最低），WiCER 0% 改善，所有迭代都不提升。论文给出的解释："its relatively high blind baseline (2.41) and low score-1 rate (38.8%) leave fewer catastrophic failures to diagnose"[^src2]。这指出 WiCER 的**适用条件**：当盲编译已经"够好"（少灾难性失败[^v3-3]），可诊断的反例就少，CEGAR 反例制导失去抓手。这也是 random pinning ablation 在该主题成为唯一反例的同源原因[^v3-4]。

## 操作含义

- **不要假设 WiCER 只是"补救工具"**：在 entity-dense 语料上它能反超 raw 全文，应作为可选生产部署而非纯实验探针；
- **应当区分主题画像**：高 score-1 + 大 entity 密度的主题最受益；低 score-1 + 已被 LLM 编译器较好处理的主题收益边际为零；
- **绝对收益与相对收益脱钩**：local_arts_and_culture 的 +1.96 来自盲基线 1.65 的巨低起点；small_and_medium_enterprises 的 +1.54 来自盲 2.21；两者的 best WiCER 已经把 FC raw 显著拉开（3.61/3.75 vs 3.34/3.44）。

## Footnotes

[^v3-1]: [wicer-cegar-compile-evaluate-refine](wicer-cegar-compile-evaluate-refine.md) — WiCER 算法骨架与 CEGAR 反例制导细化
[^v3-2]: [wicer-fc-rag-document-count-crossover](wicer-fc-rag-document-count-crossover.md) — FC raw 在 80 篇 RepLiQA 文档上 17% score-1 的 lost-in-the-middle 来源
[^v3-3]: [wicer-blind-compilation-catastrophic-loss](wicer-blind-compilation-catastrophic-loss.md) — 盲编译的灾难失败率正是 CEGAR 反例信号的来源
[^v3-4]: [wicer-targeted-vs-random-pinning-ablation](wicer-targeted-vs-random-pinning-ablation.md) — `local_education_systems` 同时是 random pinning ablation 的唯一反例主题
[^src1]: `data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt` 第 884–886 行（§6.4 Analysis）："Recovery rates span 0–125% across the 15 topics with FC raw baselines, with three topics (news_stories at 101%, local_arts_and_culture at 116%, small_and_medium_enterprises at 125%) exceeding FC raw quality after two iterations. Topics with many entity-specific facts benefit most in absolute terms (+1.96 for local_arts_and_culture, +1.54 for small_and_medium_enterprises)."
[^src2]: `data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt` 同文件第 884 行："One topic (local_education_systems) shows no WiCER improvement; its relatively high blind baseline (2.41) and low score-1 rate (38.8%) leave fewer catastrophic failures to diagnose."
[^src3]: `data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt` 主表 `tab:wicer`（第 847–882 行，17 个主题的 Blind/Best WiCER/FC raw/Recovery/Iter 列）；平均 80% recovery 论述见第 842–846 行
