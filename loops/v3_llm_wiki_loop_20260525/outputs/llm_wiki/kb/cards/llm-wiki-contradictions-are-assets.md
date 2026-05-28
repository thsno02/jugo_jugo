---
id: llm-wiki-contradictions-are-assets
title: 矛盾不是 wiki 的 bug 而是资产——别让 LLM 重写，要让它标注
status: accepted
card_type: distinction
tags: [#karpathy-llm-wiki, #contradictions, #rohit-v2, #pitfalls]
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-28T11:34:00+08:00
edited_entity: llm
source_ids: [openaitoolshub-six-months]
provenance_card: ../provenance/llm-wiki-contradictions-are-assets.md
aliases: [contradictions are assets, contradiction protocol, don't overwrite mark]
related: [llm-wiki-rohit-v2-improvements, llm-wiki-schema-is-most-important, llm-wiki-tldr-load-bearing, enterprise-llm-wiki-drift-detection-loop, llm-wiki-karpathy-lint-grounding-trail, nvk-llm-wiki-audit-and-librarian]
---

## 区分对象

- **传统知识库视角**：矛盾 = 数据质量 bug，应消除（覆盖、删除、自动 reconcile）。
- **LLM Wiki 视角（Rohit v2 + Jim 实战观察）**：矛盾 = **资产**，应被显式保留并 surface。

> "contradictions are assets, not errors. I now explicitly run contradicts: and keep both versions."[^src1]

## 为什么是资产

矛盾承载的信息不是"哪条对"，而是：

1. **决策演化路径**：你 6 个月前认为 X，现在认为 Y——这是你**自己思考变化**的证据，未来辩论 / 写作时会用到。
2. **领域结构信号**：相同主题在不同时间出现互斥结论，往往说明该主题本身在演化（如"RAG vs LLM wiki"在 2025-2026 的工业实践转向）。
3. **检验后续判断的锚点**：当第三条新声明又来时，你可以用前两条矛盾去测试它是否一致——单一覆盖式知识库做不到这件事。

Jim 的 Pitfall #3 是反向证据：他 Month 4 让 Claude 把 "RAG is the right architecture for personal knowledge bases" 重写成"LLM wiki replaces RAG"，两个月后需要旧 reasoning 与人辩论时，**旧版本已经永久丢失**[^src1]。

## 操作协议（Rohit v2 给出的）[^v3-1]

**规则**：当 LLM 发现新声明与已有 wiki 页冲突 → **不要重写** → 给两个页都加 `contradicts:` frontmatter → 保留两版 → lint 时统一暴露。

具体落地需要 schema.md 配套定义：

- `contradicts:` frontmatter 的字段含义。
- lint 时矛盾的呈现方式（如"contradictions report"页面）。
- query 时如何处理矛盾——通常的做法是把两条都 surface，让用户 / agent 决定如何使用。

## 与"compliance 场景"的边界

Jim 自己明确指出：**在 regulated 领域（legal / medical / financial advisory），这个哲学不适用**：

> "You're in a regulated field (legal, medical, financial advisory). The contradictions-as-assets philosophy clashes with compliance requirements that demand single-source-of-truth."[^src2]

这些领域要求**单一权威**，矛盾必须解决并消除——"contradictions are assets"是个人 / 团队知识库的哲学，不要无脑外推到合规场景。

## 操作含义

- **schema.md 必须把 contradiction protocol 写死**：不允许 LLM 自由判断"这个矛盾应该覆盖"。
- **lint pass 应**优先**列出 contradicts: 字段未解决的页对**，提供给用户做主动 review。
- **任何 ingest 触发的 page 重写**都应留 git diff（呼应 [obsidian-as-ide-llm-as-programmer](obsidian-as-ide-llm-as-programmer.md)[^v3-2] 中"LLM 提交应可审计可撤回"）；保险起见，关键页可以 frontmatter `do-not-rewrite: true` 锁定。

## Footnotes

[^src1]: `data/raw/webpage/openaitoolshub-six-months/text.txt:96` — "I overwrote a contradiction instead of marking it. I had an old wiki page claiming 'RAG is the right architecture for personal knowledge bases.' A new article I ingested said the opposite (LLM wiki replaces RAG). I let Claude rewrite the old page to match. Wrong move. Two months later I needed the old reasoning to argue with someone, and it was gone. Lesson: contradictions are assets, not errors. I now explicitly run contradicts: and keep both versions."
[^src2]: 同文件 `text.txt:136` — "You're in a regulated field (legal, medical, financial advisory). The contradictions-as-assets philosophy clashes with compliance requirements that demand single-source-of-truth."
[^v3-1]: [llm-wiki-rohit-v2-improvements](llm-wiki-rohit-v2-improvements.md) — Rohit v2 三件事中的 Contradiction Protocol 来源卡。
[^v3-2]: [obsidian-as-ide-llm-as-programmer](obsidian-as-ide-llm-as-programmer.md) — "LLM 提交应可审计可撤回" 类比的本卡。
