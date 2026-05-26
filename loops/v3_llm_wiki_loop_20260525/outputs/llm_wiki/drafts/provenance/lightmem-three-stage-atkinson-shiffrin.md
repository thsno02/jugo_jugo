---
schema: draft_card_provenance.v3
draft_card: ../cards/lightmem-three-stage-atkinson-shiffrin.md
material_id: arxiv-lightmem
digest_id: digest_arxiv-lightmem
source_paths:
  - data/raw/arxiv/arxiv-lightmem/agent_source_bundle.txt
created_time: 2026-05-26T11:05:00+08:00
edited_time: 2026-05-26T11:05:00+08:00
edited_entity: llm
---

## 源证据

- Abstract（行 117–123）：
  > "Inspired by the Atkinson–Shiffrin model of human memory, LightMem organizes memory into three complementary stages. First, cognition-inspired sensory memory rapidly filters irrelevant information through lightweight compression and groups information according to their topics. Next, topic-aware short-term memory consolidates these topic-based groups, organizing and summarizing content for more structured access. Finally, long-term memory with sleep-time update employs an offline procedure that decouples consolidation from online inference."
- §3 lightmem architecture（行 762–771）：
  > "Light1 implements an efficient Sensory Memory Module ... Light2 realizes a topic-aware STM Module for transient information processing ... Light3 provides an LTM module designed to minimize test time update latency ... with a sleep time update mechanism."
- Figure caption（行 135）：
  > "The LightMem architecture. LightMem consists of three modules: a) An efficient Sensory Memory Module, b) a topic aware STM Module, and c) an LTM module updated in sleep time."
- Complexity 表（行 998–1014）：Baselines = O(N) summary calls; LightMem = O(Nr^xT/th)。
- 数字直接复制自 §introduction 与 §experiments（行 594–601、755–759）。
- LightMem additional model 是 LLMlingua-2，BERT 架构 < 2GB（行 195–197）。
- 超参（行 1021）：
  > "For GPT, LightMem is configured with parameters r=0.7 and th=512; for Qwen, LightMem is configured with r=0.4 and th=768."
- Single-Assistant 反例（行 1049）：LightMem 32.14%，Naive RAG 98.21%（GPT 行）。

## 卡片范围是否成立

卡片所有"机制"段都对应论文一处显式定义（abstract、§3、Figure 1 caption）。把它讲成"目的是找帕累托更优点"而不是"刷 SOTA"，与 abstract 和 introduction 的 framing 一致（"strikes a balance between the performance and efficiency"）。Single-Assistant 反例直接来自论文自己披露的 category-wise 表。

## 发表门控结果

本轮未运行。

## 备注

- 与 v2 可能存在的"agent memory survey"或"Mem0 / A-MEM"卡片有重叠，比较阶段可能产生 `merge_candidate`。
- 三个 child 卡（pre-compress、STM、sleep-time update）会展开本卡的三模块各自机制。
