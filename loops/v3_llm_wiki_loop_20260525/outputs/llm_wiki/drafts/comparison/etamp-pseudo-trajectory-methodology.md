---
schema: comparison_provenance.v3
draft_card: ../cards/etamp-pseudo-trajectory-methodology.md
draft_provenance: ../provenance/etamp-pseudo-trajectory-methodology.md
similarity_result: ../similarity/etamp-pseudo-trajectory-methodology.json
existing_cards:
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0
  - card_id: idea-file-share-the-idea
    card_path: llm_wiki/kb/cards/idea-file-share-the-idea.md
    score: 0.0
  - card_id: llm-wiki-health-checks
    card_path: llm_wiki/kb/cards/llm-wiki-health-checks.md
    score: 0.0
decision: new_card
audit_required: false
created_time: 2026-05-26T16:06:30+08:00
edited_time: 2026-05-26T16:06:30+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三个 top 候选与 draft "Pseudo vs non-pseudo trajectory：用 PR=100% 控制变量隔离攻击效力" **token 共享为空，score 全部 0.000**。三个 v2 候选都来自同一条 Karpathy "llm wiki" launch 推文，是 v2 候选池只有 15 张时算法的兜底排序，与 draft 内容无实质邻近。

## 2. draft 与候选在哪里不同

- draft 主题：ETAMP 论文 §D.1 方法学——用 pseudo trajectory 把 PR 钉死 100% 来隔离"攻击有效性"与"infrastructure noise"，并用 ASR$_B$|PR ≈ pseudo ASR$_B$ 经验等价证明合理性。论据轴是实验方法论 + 控制变量 + cost-aware evaluation。
- 候选 1：Karpathy 推文里关于 idea file 抽象性的事实卡。
- 候选 2：同推文对 idea file 分享逻辑的事实卡。
- 候选 3：LLM 对 wiki 跑 health checks 的事实卡。

draft 与候选既无共享术语，也无共享 underlying source；draft 来自 ETAMP arxiv（`arxiv-etamp-memory-poisoning`），候选都来自 `karpathy-x-launch-post`。

## 3. 下一步的核心依据

(1) 无 token 共享 + (2) v2 候选 bodies 全部围绕 Karpathy 推文叙述，跟 pseudo trajectory 实验设计完全无关 → `new_card`。draft 给出五行对照表、ASR|PR vs Pseudo ASR 五组数据、方法学边界与三段 quote 原文，证据完整 → 不是 `revise_before_gate`。v2 无任何 agent security / memory poisoning 邻近卡 → 不是 `provenance_delta`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进入 publication_gate；与 ETAMP 系列其他 draft 在 v3 内部交叉链接。

## 5. 备注

这是 ETAMP 系列第三张 draft；它们之间的相互引用应由 v3 cards 自身的 `related` 字段处理，无需依赖 v2。
