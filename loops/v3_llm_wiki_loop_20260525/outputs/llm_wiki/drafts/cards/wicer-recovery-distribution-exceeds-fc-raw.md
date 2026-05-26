---
id: wicer-recovery-distribution-exceeds-fc-raw
title: WiCER 在三个主题上超越 FC raw 基线（>100% recovery）
status: draft
card_type: source_claim
tags: [#llm-wiki, #knowledge-compilation, #wicer, #empirical-result]
created_time: 2026-05-26T15:00:00+08:00
edited_time: 2026-05-26T15:00:00+08:00
edited_entity: llm
source_ids: [arxiv-wicer]
provenance_card: ../provenance/wicer-recovery-distribution-exceeds-fc-raw.md
aliases: [WiCER recovery distribution, super-recovery topics, WiCER beats FC raw]
related: [wicer-cegar-compile-evaluate-refine, wicer-blind-compilation-catastrophic-loss]
---

## 主张

WiCER 论文最容易被忽略的非平凡结果不是"平均 80% recovery"，而是 **recovery 率分布从 0% 到 125% 跨度极宽，且有三个主题在两次迭代后超过了 FC raw 基线**。这违背了"压缩+pinning 最多只能逼近原文质量"的直觉——它说明在某些语料上，**带反馈的有损编译可以比直接读所有 80 篇原文更好**。

## 三个超越 FC raw 的主题（Table tab:wicer）

| Topic | Blind | Best WiCER | FC raw | Recovery |
| --- | --- | --- | --- | --- |
| news_stories | 2.50 / 40.0% | **3.61** / 11.2% | 3.60 | **101%** |
| local_arts_&_culture | 1.65 / 73.8% | **3.61** / 15.0% | 3.34 | **116%** |
| small_medium_ent. | 2.21 / 56.2% | **3.75** / 13.8% | 3.44 | **125%** |

后两个主题绝对收益 +1.96 / +1.54，对应论文原话：「Topics with many entity-specific facts benefit most in absolute terms」[^1]。

## 为什么会超过 FC raw

机制可解释：FC raw 在 80 篇 RepLiQA 文档上受 **lost in the middle** 折磨（mean score-1 17.3%）；当 WiCER 用诊断 pinning 把"实体特定事实"明确钉进 wiki，模型在更短上下文里反而能更可靠地找到它们，attention dilution 的代价 > 信息损失的代价。换句话说，**压缩本身不是单调有害**——只要 (a) 关键事实没丢、(b) 上下文密度提升带来的注意力收益大，编译后的 wiki 可以在 lost-in-the-middle 主题上反超 raw 全文。

## 分布的另一极：单调失败

另一极是 `local_education_systems`：盲基线 2.41、score-1 38.8%（17 个主题里最低），WiCER 0% 改善。论文给出的解释：「its relatively high blind baseline (2.41) and low score-1 rate (38.8%) leave fewer catastrophic failures to diagnose」[