---
schema: comparison_provenance.v3
draft_card: ../cards/mem0-locomo-benchmark-evaluation.md
draft_provenance: ../provenance/mem0-locomo-benchmark-evaluation.md
similarity_result: ../similarity/mem0-locomo-benchmark-evaluation.json
existing_cards:
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0667
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.0625
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.0556
---

## 1. draft 与候选为什么看起来相关

三张候选的分数都在 0.055–0.067，落在"主题大概率无关"的低分区间。共享 token 限于中文虚词与少数泛用词。三张 v2 候选都是 Karpathy LLM Wiki gist 卡片，不出现 mem0、LOCOMO、LLM-as-Judge、F1 / BLEU 等任何 draft 关键概念。

## 2. draft 与候选在哪里不同

draft 是对 Mem0 论文 §4 整套 LOCOMO 评估的高密度记录：四类题目（single-hop / multi-hop / temporal / open-domain）下的 J 分主表、Mem0 与 Mem0g 相对 Zep / LangMem / OpenAI / A-Mem 的具体数字、p50/p95 latency 对照（91% 降幅）、token 成本对比（Mem0 ~7k vs Zep ~600k），并列出 abstract 的 26% relative improvement 来源以及论文未声称的事。

v2 三张候选属于 Karpathy LLM Wiki 概念层卡片，没有任何对外部 memory 系统的评估、benchmark 数据或 latency 数字。论点轴与来源类型完全不同。

## 3. 下一步的核心依据

(1) 与 (2) 表明 draft 在 v2 没有任何接近物：v2 没有 mem0 卡，没有 LOCOMO 卡，没有 baseline 评估卡。draft 已具备完整的表格、数字、来源和边界，可直接走 publication_gate。决策为 `new_card`。

不是 `merge_candidate`：v2 中没有对应卡需要合并。
不是 `provenance_delta`：v2 中没有对应卡 body 需要补充证据。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进 publication_gate；与同 batch 的 `mem0-baseline-failure-modes`、`mem0-rag-chunk-size-ablation`、`mem0-answer-generation-prompt-design` 等卡形成 mem0 系列簇，可在后续轮次互相 cite。

## 5. 备注

本批次大量 mem0/lightmem/locomo 系列卡同时给出同一组 Karpathy 候选 top 3——证实经验性提示中"高频干扰卡"的判断。
