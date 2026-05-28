---
id: llm-wiki-rohit-v2-improvements
title: Rohit v2 在 Karpathy 原始 gist 上加的三件事：Lifecycle / Typed Links / Contradiction Protocol
status: accepted
card_type: mechanism
tags: [#rohit-v2, #karpathy-llm-wiki, #memory-lifecycle, #typed-relationships, #contradictions]
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-28T11:44:00+08:00
edited_entity: llm
source_ids: [openaitoolshub-six-months]
provenance_card: ../provenance/llm-wiki-rohit-v2-improvements.md
aliases: [Rohit Ghumare v2, memory lifecycle frontmatter, typed wikilinks, contradiction protocol]
related: [llm-wiki-contradictions-are-assets]
---

## 背景

Jim Liu 用 Karpathy v1 跑了 35 页之后，发现三个**v1 不修就会反复踩**的失败模式。Rohit Ghumare 的 v2 各加了一个 schema-level 机制来修，Jim 在自己的 wiki 上验证后留下了这三条。

## 三件事

### 1. Memory Lifecycle frontmatter

v1 没有"page 何时被验证过 / 我对它的把握有多大 / 它是否被新页取代"这些元数据；结果**过期的 ChatGPT 定价声明和最新的并排站着**，两者都被自信断言。

v2 给每页加[^src1]：
- `last_verified: 2026-05-01`
- `confidence: high | medium | low`
- `superseded_by: another-page.md`（如适用）
- `contradicts: an-older-claim.md`（如适用）

时间维度被显式编码后，agent 在 query 时可以**按时间衰减加权**，过期内容自动降权。

### 2. Typed wikilinks（有类型的链接）

v1 的 `[[obsidian]]` 只携带"X 与 Y 相关"这一弱信息。v2 把链接变成有 6 种 relationship type 的标注：

- `[[obsidian]] (uses)`
- `[[gbrain]] (alternative-to)`
- `[[X]] (contradicts)`
- ...

> "It feels fussy at first; by month two it lets Claude give much sharper answers because the graph isn't just 'X is connected to Y' but 'X uses Y' or 'X contradicts Y'."[^src2]

## 3. Contradiction protocol（矛盾不重写，标注）

**v1 默认行为**：LLM 发现新声明与旧页冲突 → 通常重写旧页。
**v2 强制规则**[^v3-1]：发现冲突 → 加 `contradicts:` frontmatter → **两版都保留** → lint 时统一暴露[^src3]。

Jim 的 Pitfall #3 是真实损失的对照：他 Month 4 让 Claude 把"RAG 是 PKM 正确架构"的旧页重写成"LLM wiki 替代 RAG"，两个月后他需要旧 reasoning 与人辩论，已经没了。

## 共同主题

三件事都是把 v1 里**隐式的、靠 agent 自由发挥**的行为**显式化、合同化、可 lint 化**：

| 关注点 | v1 默认 | v2 机制 |
|---|---|---|
| 时间 / 新鲜度 | 隐式 | `last_verified` + `superseded_by` |
| 关系类型 | 弱标 `[[link]]` | 6 种 typed link |
| 冲突 | 让 LLM 自己处理 | 强制保留 + lint 暴露 |

## 边界

- v2 的复杂度增量是非零的：每天维护时间从 ~5 min 升到 ~10 min（Jim 表格），值不值得取决于 wiki 规模与跨时间使用频率。
- 6 种 link type 是 Jim / Rohit 的选择；实际数量应按主题复杂度调；过少失去区分力，过多 LLM 标注不一致。
- Jim 同时声明：在他 35 页规模下尚未需要 GBrain 的 Postgres + Dream Cycle；v2 是 100-500 页范围的"刚刚好"。

## Footnotes

[^src1]: `data/raw/webpage/openaitoolshub-six-months/text.txt:52` — "Memory Lifecycle frontmatter: every page has last_verified: 2026-05-01, confidence: high|medium|low, and (when relevant) superseded_by: another-page.md or contradicts: an-older-claim.md. v1 has none of these."
[^src2]: 同文件 `text.txt:56` — "instead of plain [[obsidian]], I write [[obsidian]] (uses) or [[gbrain]] (alternative-to). Six relationship types total... it lets Claude give much sharper answers because the graph isn't just 'X is connected to Y' but 'X uses Y' or 'X contradicts Y'."
[^src3]: 同文件 `text.txt:58` — "when Claude finds a new claim that contradicts a wiki page, the rule is don't overwrite, mark. Add contradicts: field, keep both, surface during lint."
[^v3-1]: [llm-wiki-contradictions-are-assets](llm-wiki-contradictions-are-assets.md) — Contradiction Protocol 在 Jim Pitfall #3 视角下的展开。
