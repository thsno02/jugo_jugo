---
schema: accepted_card_provenance.v3
card: ../cards/hn-writing-as-thinking-vs-llm-wiki.md
material_id: hacker-news-original-thread
digest_id: digest_hacker-news-original-thread
source_paths:
  - data/raw/hacker_news/hacker-news-original-thread/text.txt
draft_card: ../../drafts/cards/hn-writing-as-thinking-vs-llm-wiki.md
draft_provenance: ../../drafts/provenance/hn-writing-as-thinking-vs-llm-wiki.md
similarity_result: ../../drafts/similarity/hn-writing-as-thinking-vs-llm-wiki.json
comparison_provenance: ../../drafts/comparison/hn-writing-as-thinking-vs-llm-wiki.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T10:12:00+08:00
  gate_notes: 6/6 项通过：四位 HN 用户引语带行号 + AI de-skilling 命名 + qaadika 隔离实践 + 误用边界。
created_time: 2026-05-26T11:11:00+08:00
edited_time: 2026-05-27T10:12:00+08:00
edited_entity: llm
---

## 源证据

- `loveparade`（行 246–248）原文已在卡片中引用。
- `kilroy123`（行 250–253）：
  > "Makes me think of all these tools that use AI to make fancy flashcards for you to study. It seems rather silly to me, as creating those flashcards is what helps you learn"
- `nidnogg`（行 205–209）：自述用 multiagent + wiki，"this creates a weird new type of tech debt. Almost like a persistent brain gap."；行 209 提到"too addictive to stop"。
- `nidnogg`（行 263）："AI de-skilling" 命名。
- `qaadika`（行 459–471）：详细 PKM 隔离实践，含模板。
- `qaadika`（行 472）：手动复制粘贴 + "friction" 反思。
- 反对"It's the AI's database"原句（行 461）。

## 卡片范围是否成立

卡片把帖子中跨多个评论的同一主题（"过程 vs 产物"）综合成一张"distinction"卡。所有引文都按用户名 + 行号定位；并明确保留了 `qaadika` "I'm not totally against AI writing in a personal knowledgebase" 这一原话的边界，避免把这一阵营写成绝对反对。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T10:12:00+08:00
- 检查要点：
  - 非标题复述：四位用户引语 + 折中实践 + 误用边界。
  - 知识密度：核心论点 + 类比 + 现象命名 + 隔离实践模板 + 折中规则 + 误用。
  - 源支撑：HN 行 246-248 / 250-253 / 205-209 / 263 / 459-472 多锚点。
  - References / Footnotes 存在。
  - frontmatter 完整。
  - related 字段 5 个 v3 draft id。

## 备注

- 与 v2 中可能已有的 PKM / writing-as-thinking / AI de-skilling 卡片可能重叠。
- 与 `hn-llm-wiki-is-just-rag-debate` 卡是这场 HN 帖的两条主要争论线索之一。
- Adoption 阶段观察：与 v2 候选论点轴对立而非重叠（v2 是 Karpathy 主张本身，本 draft 是对该主张的反对）；v2 候选 scope 限于 Karpathy 来源，禁止外推到 HN 反对意见。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/hn-writing-as-thinking-vs-llm-wiki.md`
- draft provenance: `../../drafts/provenance/hn-writing-as-thinking-vs-llm-wiki.md`
- similarity: `../../drafts/similarity/hn-writing-as-thinking-vs-llm-wiki.json`
- comparison provenance: `../../drafts/comparison/hn-writing-as-thinking-vs-llm-wiki.md`
