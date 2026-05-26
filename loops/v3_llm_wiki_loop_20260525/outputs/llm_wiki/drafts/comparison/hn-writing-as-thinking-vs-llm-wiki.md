---
schema: comparison_provenance.v3
draft_card: ../cards/hn-writing-as-thinking-vs-llm-wiki.md
draft_provenance: ../provenance/hn-writing-as-thinking-vs-llm-wiki.md
similarity_result: ../similarity/hn-writing-as-thinking-vs-llm-wiki.json
existing_cards:
  - card_id: llm-wiki-human-llm-role-division
    card_path: llm_wiki/kb/cards/llm-wiki-human-llm-role-division.md
    score: 0.0667
  - card_id: llm-wiki-health-checks
    card_path: llm_wiki/kb/cards/llm-wiki-health-checks.md
    score: 0.0625
  - card_id: llm-wiki-listed-use-cases
    card_path: llm_wiki/kb/cards/llm-wiki-listed-use-cases.md
    score: 0.0625
decision: new_card
audit_required: false
created_time: 2026-05-26T16:00:00+08:00
edited_time: 2026-05-26T16:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三个候选 jaccard 都低于 0.07，shared_tokens 仅为「llm」。本卡在主题层确实直接讨论 Karpathy LLM Wiki 设想（HN 帖子的反对意见），所以与 v2 任何 Karpathy 卡都有概念血缘——但本批次 top 3 命中是 jaccard 的字面 token 命中（「llm」一词），不是因为 v2 卡 body 真的涉及 HN pushback。

## 2. draft 与候选在哪里不同

draft 是 distinction 卡，来源 `hacker-news-original-thread`，记录 HN 帖子上 `loveparade` / `kilroy123` / `nidnogg` / `qaadika` 等用户对 Karpathy LLM Wiki 的认识论反对：写作的价值在过程而非产物、AI 写 flashcard 错过学习、AI de-skilling 现象、`==BEGIN AI-GENERATED CONTENT==` 隔离实践等。属于「LLM Wiki 的社群反对意见」论点轴。

三张 v2 候选：
- top 1「人提问，LLM 维护」：Karpathy 描述的分工模式（人策展+提问、LLM 写作维护）；
- top 2「health checks 清理 wiki」：Karpathy quote 描述的 lint 想法；
- top 3「应用场景清单」：Karpathy 列举的 use cases。

差别：v2 是 Karpathy 主张本身的事实描述（scope 严格限于 Karpathy 来源），draft 是 HN 用户对该主张的反对论证（来源是 HN 帖子）。两者论点轴对立——一个是「LLM Wiki 设想本身」、一个是「为什么有人反对它」。v2 候选 scope 都明确「仅限该来源 / quote text」，无法把外部 HN 用户反对意见纳入其 provenance。draft 与 top 1「人提问，LLM 维护」尤其形成「主张 vs 反例」关系，但仍是两张分立的卡。

## 3. 下一步的核心依据

虽然 draft 与 v2 KB 在主题层确实相关（同是关于 LLM Wiki），但：
1. draft 来源是 HN 帖子（不同 source），且要从多个用户的多段 quote 抽出结论；
2. v2 卡的 scope 都明确禁止外推到该来源以外的讨论；
3. draft 自身证据完整（行号 246-248 / 250-253 / 205-209 / 459-471 / 263 等到位），不需要 revise；
4. draft 是一个独立的「pushback summary」卡，不试图改写或合并任何 v2 卡 body。

不是 `merge_candidate`（论点轴对立、来源不同）；不是 `provenance_delta`（v2 scope 禁止外推）；不是 `duplicate_skip`（draft 是新论点）；不是 `revise_before_gate`（证据完整）。综合判 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进入 publication_gate；新卡 related 字段建议显式引用 v2 `llm-wiki-human-llm-role-division`、`llm-wiki-persistent-compounding-artifact` 等作为「被反对的主张」的对位卡。

## 5. 备注

- 这是本批次主题相关度最高的一张 draft——与 v2 KB 在论域上直接互文。但选择 `new_card` 而非 `provenance_delta` 的关键依据：v2 卡 scope 均严格限定在 Karpathy 来源内，外部反对意见不可直接注入。
- 与 sibling `hn-llm-wiki-is-just-rag-debate` 同 source 互引。
