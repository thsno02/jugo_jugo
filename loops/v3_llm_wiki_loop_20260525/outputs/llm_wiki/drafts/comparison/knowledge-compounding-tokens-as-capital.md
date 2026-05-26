---
schema: comparison_provenance.v3
draft_card: ../cards/knowledge-compounding-tokens-as-capital.md
draft_provenance: ../provenance/knowledge-compounding-tokens-as-capital.md
similarity_result: ../similarity/knowledge-compounding-tokens-as-capital.json
existing_cards:
  - card_id: llm-wiki-human-llm-role-division
    card_path: llm_wiki/kb/cards/llm-wiki-human-llm-role-division.md
    score: 0.0769
  - card_id: llm-wiki-health-checks
    card_path: llm_wiki/kb/cards/llm-wiki-health-checks.md
    score: 0.0714
  - card_id: llm-wiki-listed-use-cases
    card_path: llm_wiki/kb/cards/llm-wiki-listed-use-cases.md
    score: 0.0714
decision: new_card
audit_required: false
created_time: 2026-05-26T16:00:00+08:00
edited_time: 2026-05-26T16:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三个候选 jaccard 都低于 0.08，shared_tokens 仅为「llm」一词（任何提到 LLM 的卡都会共享这个 token）。draft 标题主体是「token / 消耗品 / 资本品 / 归类」，与三张 v2 候选标题（人 LLM 分工 / health checks / 应用场景清单）无术语级重合。属于 jaccard 噪声。

## 2. draft 与候选在哪里不同

draft 是 distinction 卡，来源 `arxiv-knowledge-compounding`（Wen & Ku 2026），核心论点是 LLM token 的会计归类应从 consumables 重构为 capital goods，从「边际成本分析」切换到「资本积累 / 折旧 / ROI 分析」框架。论点轴是「LLM 经济学」。

三张 v2 候选都是 Karpathy LLM-wiki 元描述：top 1「人提问，LLM 维护」是分工模式、top 2「health checks 清理 wiki」是 lint 想法、top 3「应用场景清单」是 use case 列表。它们与 draft 的「token 资本品归类」在论点轴（经济学会计归类 vs 个人知识库使用场景描述）、来源（学术论文 vs 个人帖 / quote）、机制（capital goods 资本化 vs LLM 写 markdown）层面全部不同。

需要承认的间接联系：draft 提到「INGEST 与 synthesis 写入持久 wiki 页才能资本化」，与 v2 整个 KB 关注的「持久 wiki」概念有抽象血缘，但 draft 的论点是经济学层级（NPV、折旧、回本期），不是 wiki 设计层级；不存在足以 merge 或 provenance_delta 的卡。

## 3. 下一步的核心依据

shared_tokens 仅是「llm」，无语义关联。v2 候选 scope 严格限于 Karpathy 来源，无法承载 Wen & Ku 论文的经济学归类。draft 自身证据完整（行号 L37 / L39 到位，含 JEL 分类佐证），scope 自洽。综合判 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进入 publication_gate。

## 5. 备注

- 与 sibling `knowledge-compounding-dynamic-roi` / `knowledge-compounding-three-mechanisms` 是同 source 内的概念互引。
- 「持久 wiki 复利」是 Karpathy KB 与 Wen & Ku 论文的潜在桥接概念，但需要新的桥接卡来连接，本批次不可由 provenance_delta 完成。
