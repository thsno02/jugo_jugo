---
schema: comparison_provenance.v3
draft_card: ../cards/llm-wiki-karpathy-lint-grounding-trail.md
draft_provenance: ../provenance/llm-wiki-karpathy-lint-grounding-trail.md
similarity_result: ../similarity/llm-wiki-karpathy-lint-grounding-trail.json
existing_cards:
  - card_id: llm-wiki-persistent-compounding-artifact
    card_path: llm_wiki/kb/cards/llm-wiki-persistent-compounding-artifact.md
    score: 0.0833
  - card_id: llm-wiki-persistent-wiki-alternative-mode
    card_path: llm_wiki/kb/cards/llm-wiki-persistent-wiki-alternative-mode.md
    score: 0.0769
  - card_id: llm-wiki-health-checks
    card_path: llm_wiki/kb/cards/llm-wiki-health-checks.md
    score: 0.0714
decision: new_card
audit_required: false
created_time: 2026-05-26T16:00:00+08:00
edited_time: 2026-05-26T16:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三个候选 jaccard 都低于 0.09，shared_tokens 仅为「wiki」一词。但这次比起其它批次，主题确实有 *间接* 邻近：draft 来源 `@harrylabs/llm-wiki-karpathy` 是受 Karpathy LLM-wiki 启发的一个具体 runtime 实现，而 v2 候选都是 Karpathy 原文里的 wiki 模式描述。Top 3 `llm-wiki-health-checks` 与本 draft 的 `kb_lint` 在功能定位上属于「Karpathy 提出的 health check 想法 vs 一个具体 lint 实现」。

## 2. draft 与候选在哪里不同

draft 是 operational_rule 卡，列出 `kb_lint` 的 8 个具体 deterministic 检查项（missing representation trails、stale representations、inconsistent asset_paths、isolated pages、stale source coverage、unsupported claims、contradiction candidates、missing high-value pages），并讨论 lint vs agent 的责任分工与边界。来源是 `clawhub-llm-wiki-karpathy/text.txt`（第三方 runtime 文档）。

三张 v2 候选：
- top 1「持久复合 wiki」：Karpathy 描述 wiki 是会复合增长的持久产物，scope 限于该原句；
- top 2「持久 wiki 替代模式」：Karpathy 描述 LLM 持久 wiki 与一次性 RAG 的对比，scope 限于原句；
- top 3「LLM health checks 清理 wiki」：Karpathy 推文 quote text 提到 LLM 可以跑 health checks（找不一致 / 补缺 / 找新连接），scope 限于该 quote text。

差别：draft 是「一个真实运行的 runtime 的 lint 命令实际做了哪 8 件事」；v2 是「Karpathy 在帖文 / quote 里提出的高层想法」。draft 是 v2 health-checks 想法的*下游实现*而非同一观点。v2 三张卡的 scope 都明确「仅限该来源 / quote text」，且 v2 health-checks 还显式说「不外推为产品功能承诺」——把 `@harrylabs` 这个第三方 runtime 的实现细节注入 v2 health-checks provenance 会突破其 scope。

## 3. 下一步的核心依据

虽然 draft 和 top 3 在概念血缘上有「想法 → 实现」的关系，但：
1. v2 health-checks scope 明确禁止外推到具体产品；做 `provenance_delta` 会突破其 scope；
2. draft 给出的是另一份来源（clawhub-llm-wiki-karpathy）上的 8 条具体 deterministic 检查清单，性质是独立的 operational_rule 卡，不会与 v2 任何一张卡 body 重合到 merge 的程度；
3. draft 本身证据完整（行号 L73 / L172–175 / L67–68 全部到位），不需要 revise。

因此判 `new_card`。但建议在备注里记录其与 v2 `llm-wiki-health-checks` 的概念血缘，未来若 KB 增加「Karpathy 想法 → 第三方实现」类型的桥接 schema，再考虑显式 cross-link。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进入 publication_gate；新卡内可加 related 字段引用 v2 `llm-wiki-health-checks` 作概念血缘提示。

## 5. 备注

- 与 v2 `llm-wiki-health-checks` 存在「想法 → 实现」血缘，但 v2 scope 明确禁止外推到具体产品。如果未来 KB 引入「实现卡」类别，可重新考虑反向链接到 v2 health-checks provenance。
- 选择 `new_card` 而非 `provenance_delta` 的关键依据：v2 scope 显式声明「不外推为产品功能承诺」。
