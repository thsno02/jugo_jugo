---
schema: comparison_provenance.v3
draft_card: ../cards/wicer-cegar-compile-evaluate-refine.md
draft_provenance: ../provenance/wicer-cegar-compile-evaluate-refine.md
similarity_result: ../similarity/wicer-cegar-compile-evaluate-refine.json
existing_cards:
  - card_id: llm-wiki-persistent-compounding-artifact
    card_path: llm_wiki/kb/cards/llm-wiki-persistent-compounding-artifact.md
    score: 0.1
  - card_id: llm-wiki-persistent-wiki-alternative-mode
    card_path: llm_wiki/kb/cards/llm-wiki-persistent-wiki-alternative-mode.md
    score: 0.0909
  - card_id: llm-wiki-health-checks
    card_path: llm_wiki/kb/cards/llm-wiki-health-checks.md
    score: 0.0833
decision: new_card
audit_required: false
created_time: 2026-05-26T16:05:00+08:00
edited_time: 2026-05-26T16:05:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三张候选共享 token 仅为 `wiki`。draft 的核心 token `WiCER`、`CEGAR`、`抽象`、`细化`、`编译` 都不出现在任何候选标题。jaccard 0.1 完全由 `wiki` 这一主题词撞分。

## 2. draft 与候选在哪里不同

- 候选 #1 `llm-wiki-persistent-compounding-artifact`：仅记录 Karpathy gist 第 13 行 wiki 是持久复合产物的性质论断（保留 cross-references / 矛盾标记 / 综合内容）。是 wiki 的产物性质卡，不涉及任何编译算法。
- 候选 #2 `llm-wiki-persistent-wiki-alternative-mode`：v2 中"持久 wiki 替代模式"概念卡。与 WiCER 算法不在同一层级。
- 候选 #3 `llm-wiki-health-checks`：仅记录 LLM 对 wiki 做 health checks 这一事实。和 CEGAR 闭环编译无关。
- draft 来源是 `arxiv-wicer` §6 (Algorithm 1 第 781–802 行) + §CEGAR 类比 (第 806–820 行) + §代价分析 (第 886 行)，论点是把 wiki 编译当作 CEGAR 抽象细化的迭代闭环：每轮把 score=1 探针的失败事实加进 `F_cumulative`，由下一次 `Compile(D, r, preserve=F_cumulative)` 钉回。draft 含具体代价（每轮 ~130K input / ~17K output token、~$1–2、~50 分钟）与典型停在第 2 轮的收敛观察。v2 KB 中无 wiki 编译算法卡。

## 3. 下一步的核心依据

- 不是 `merge_candidate`：v2 无 wiki 编译算法 / CEGAR 类比卡，三张候选都是 wiki 性质或维护方式的小事实卡。
- 不是 `provenance_delta`：候选 #1 的"持久复合"性质论断与 WiCER 算法机制无直接对接面（一个是性质描述，一个是编译实现）。
- 不是 `duplicate_skip`：无任何覆盖。
- 不是 `revise_before_gate`：draft 已有算法骨架 6 步、CEGAR 抽象/具体的映射、代价数字、收敛性论证（单调收敛/随机置换）与失败模式（盲基线高 / 预算紧 / judge 偏差）；门控可继续。
- 综合判 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：publication_gate；门控阶段建议核 Algorithm 1 6 步与论文 `algorithm` 环境 (第 781–802 行) 是否字面对齐。

## 5. 备注

- draft 自身 provenance 已指出："v2 现有 4 张卡的 slug 题面与本卡均不在同一个抽象层级，预计为 new_card"——本判断与之一致。
- 与同源 `wicer-fc-rag-document-count-crossover`、`wicer-blind-compilation-catastrophic-loss`、`wicer-llm-judge-human-validation` 共同构成 WiCER 系列卡。
