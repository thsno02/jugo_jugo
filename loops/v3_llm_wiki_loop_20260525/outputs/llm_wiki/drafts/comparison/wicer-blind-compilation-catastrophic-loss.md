---
schema: comparison_provenance.v3
draft_card: ../cards/wicer-blind-compilation-catastrophic-loss.md
draft_provenance: ../provenance/wicer-blind-compilation-catastrophic-loss.md
similarity_result: ../similarity/wicer-blind-compilation-catastrophic-loss.json
existing_cards:
  - card_id: llm-wiki-persistent-compounding-artifact
    card_path: llm_wiki/kb/cards/llm-wiki-persistent-compounding-artifact.md
    score: 0.0714
  - card_id: llm-wiki-persistent-wiki-alternative-mode
    card_path: llm_wiki/kb/cards/llm-wiki-persistent-wiki-alternative-mode.md
    score: 0.0667
  - card_id: llm-wiki-health-checks
    card_path: llm_wiki/kb/cards/llm-wiki-health-checks.md
    score: 0.0625
decision: new_card
audit_required: false
created_time: 2026-05-26T16:00:00+08:00
edited_time: 2026-05-26T16:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三个候选 jaccard 都低于 0.08，shared_tokens 仅为「wiki」。draft 与 v2 候选**都谈 wiki**，但语义不同：draft 是 WiCER 论文里把 80 篇 RepLiQA 原文压缩成 wiki 的失败实测（盲编译超压 2-3 倍 + 关键事实丢失），v2 三张卡是 Karpathy 描述的「持久复合 wiki」「持久 wiki 替代模式」「health checks 清理 wiki」高层主张。词形重合但论点层与对象层不同。

## 2. draft 与候选在哪里不同

draft 是 source_claim 卡，来源 `arxiv-wicer`，给出 Table 3 的具体数字（FC raw / Wiki-light / Wiki-moderate / Wiki-aggressive / RAG 五行）、score-1 比率（17% → 53-60% 的塌方）、压缩 compliance 失败模式、并把 TTFT 加速换质量损失作为「compilation gap」论证。属于「LLM 离线文档压缩失败模式」论点轴。

三张 v2 候选都是 Karpathy LLM-wiki 元描述。论点轴差异：
- v2「持久复合 wiki」「持久 wiki 替代模式」是「wiki 是值得做」的正向命题（Karpathy 推介）；
- draft 是「盲编译做 wiki 会塌方」的负向命题（WiCER 实测）。
- v2「health checks 清理 wiki」是「wiki 可自检」的想法；draft 是「编译 wiki 时事实丢失」的失败模式实测。

来源（Karpathy 个人主张 vs RepLiQA 6800 题量化实测）、机制（描述性 wiki 模式 vs compression compliance failure 指标）、读者（个人知识管理者 vs RAG / cache-augmented serving 系统工程师）都不同。v2 候选 scope 严格限于 Karpathy 来源，无法承载 WiCER 论文实验。

## 3. 下一步的核心依据

shared_tokens 仅是「wiki」（同一词两端语义不同），无实质论点重叠。v2 候选 scope 不允许纳入 WiCER 实测数据。draft 引文具体到 Table 3 与 L758-762 段落，scope 自洽（只用论文给的 6800 题 17 主题数据，不外推）。综合判 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进入 publication_gate；与 sibling `wicer-cegar-compile-evaluate-refine` 同 source 互引。

## 5. 备注

- draft 与 v2 持久 wiki 系列卡在抽象上构成「主张 vs 实测反例」的对偶关系。未来若 KB 引入「主张-反例」桥接卡 schema，可考虑显式 cross-link，但本批次不在 provenance_delta 范畴。
