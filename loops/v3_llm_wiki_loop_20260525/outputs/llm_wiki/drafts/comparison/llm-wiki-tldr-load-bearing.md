---
schema: comparison_provenance.v3
draft_card: ../cards/llm-wiki-tldr-load-bearing.md
draft_provenance: ../provenance/llm-wiki-tldr-load-bearing.md
similarity_result: ../similarity/llm-wiki-tldr-load-bearing.json
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
created_time: 2026-05-26T16:09:00+08:00
edited_time: 2026-05-26T16:09:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三个 top 候选与 draft "TL;DR 强制规则比 index 更省 context window——load-bearing 设计" **token 共享为空，score 全部 0.000**。需要小心的是：draft 与候选 3 (`llm-wiki-health-checks`) 都含 "llm-wiki" 字面，且 draft 也提到 Karpathy gist；但 jieba 给出的分词里 `llm-wiki` 并未作为单 token 被算法识别为共享（draft tokens 与候选 tokens 之间真实交集为空），所以 score = 0。这是分词器的实际行为，不是相关性判断。

## 2. draft 与候选在哪里不同

- draft 主题：Jim Liu 在 35 页 wiki 实战中观察到的具体规则——TL;DR ≤50 字符是 load-bearing 的 schema 强制规则，比 index 更省 context。论据轴是 wiki 信息架构 + reader 体验 + schema enforcement。draft 来自 `openaitoolshub-six-months` 实战页面。
- 候选 1 (`idea-file-abstract-vague`)：Karpathy 推文中关于 idea file 抽象性的叙述（不谈 TL;DR 也不谈 schema）。
- 候选 2 (`idea-file-share-the-idea`)：同推文对 idea file 分享逻辑的叙述。
- 候选 3 (`llm-wiki-health-checks`)：同一段 quote text 关于 LLM 跑 health checks 找不一致数据；这是 wiki 维护一面，与 TL;DR 的 schema enforcement 是不同侧面。

draft 与候选 3 **同属 "Karpathy llm-wiki 议题"** 但**论点轴不同**：draft 谈"用 TL;DR ≤50 字符把'页摘要'升格为 schema-mandatory + 可被 1 次 read scan"；候选 3 谈"LLM 怎么用 health checks 清理 wiki 数据完整性"。Jim 文中确实"提到 Karpathy gist 提及 TL;DR-on-top"，但他的核心声明是"在我手上把它当成 load-bearing"——这是对 Karpathy 设计的工程性 sharpening / extension，但 v2 KB 里**没有 TL;DR 规则相关卡**，所以也并不构成 merge / delta。

## 3. 下一步的核心依据

(1) jieba 给出的 token 交集确实为空，但 (2) 主题域上 draft 与候选 3 都属 Karpathy llm-wiki 议题 → 必须看 body：候选 3 完全不谈 TL;DR、不谈 schema 字符上限、不谈 context 节省；draft 完全不谈 health checks / 不一致数据 / 数据完整性。两者在同一议题下覆盖**互不交叠**的两个工程面 → `new_card`（而非 `provenance_delta` / `merge_candidate`）。draft 已包含原文 quote (`text.txt:38`)、对比表、操作规则、边界，证据完整 → 不是 `revise_before_gate`。

为什么不是 `provenance_delta`：`provenance_delta` 适用于"draft 不改 v2 卡 body 多少，但加了新证据 / 新边界 / 新数值"。draft 的 TL;DR ≤50 字符规则与 `llm-wiki-health-checks` 的 health checks 论题**不是同一条陈述的补充**——把它反向链接进 health checks 的 provenance 是不合适的（不同声明）。draft 真正补的是"Karpathy gist 里 TL;DR-on-top 一笔带过"——但 v2 KB 没收录那条 Karpathy 表述（v2 三张卡只覆盖 idea file 抽象性、idea file 分享逻辑、health checks），所以没有可反向 link 的 v2 卡。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：publication_gate；在 v3 内与 `karpathy-llm-wiki-three-layers`、`llm-wiki-schema-is-most-important` 之类 related 链接。

## 5. 备注

这是 batch 里**最值得提的边界 case**：draft 与候选 3 名义上同议题（Karpathy llm-wiki），但论点轴不同。jieba score=0 在这里恰好与 body 判断一致——属于"低 score 但需要 careful 看"的正确触发点。建议后续若 v2 把 Karpathy "TL;DR-on-top" 一笔带过的事实补成 v2 卡，可再回头评估是否升级为 `provenance_delta`。
