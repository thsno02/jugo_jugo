---
id: hn-writing-as-thinking-vs-llm-wiki
title: HN 反对意见——委托写作给 LLM 等于让"思考"被外包
status: accepted
card_type: distinction
tags: [#llm-wiki, #pkm, #cognition, #ai-deskilling, #hacker-news]
created_time: 2026-05-26T11:11:00+08:00
edited_time: 2026-05-27T10:12:00+08:00
edited_entity: llm
source_ids: [hacker-news-original-thread]
provenance_card: ../provenance/hn-writing-as-thinking-vs-llm-wiki.md
aliases: ["writing-as-thinking pushback", "AI de-skilling"]
related: [hn-llm-wiki-is-just-rag-debate, hn-source-granularity-changes-synthesis-quality, karpathy-gist-bookkeeping-burden, idea-file-as-agent-era-artifact, obsidian-as-ide-llm-as-programmer]
---

HN 帖子里反对 Karpathy LLM Wiki 设想的最有质量的论点不是技术性反对（如 "model collapse" 或 "context overflow"），而是**认知论反对**——围绕"知识库的价值在产物还是在写作过程"。

**核心论点（`loveparade`，行 246–248）：**

> "Most of the value of writing docs or a wiki is not in the final artifacts, it's that the process of writing docs updates your own mental models and knowledge so that you can make better decisions down the road. Even if you can get an LLM to output good artifacts that don't eventually evolve into slop, which is questionable, it's really not that useful, especially not for a personal wiki."

**类比扩展（`kilroy123`，行 250–253）：**

> "Makes me think of all these tools that use AI to make fancy flashcards for you to study. It seems rather silly to me, as creating those flashcards is what helps you learn, with the studying after, cementing that knowledge in your brain."

**亲身见证型反例（`nidnogg`，行 205–209）：**

实际践行 wiki-driven multiagent 流程后描述出现"weird new type of tech debt. Almost like a persistent brain gap. I miss thinking harder ... the wiki workflow is just too addictive to stop."——把"产能上去 + 反思能力下降"作为现象记录。引入了一个新词 *AI de-skilling*（行 263）。

**`qaadika` 的"AI 区隔"（行 459–471）：**

不是反对 AI 写作，而是给出**可借鉴的隔离实践**：

- AI 写的内容在自己 Obsidian vault 里用 `==BEGIN AI-GENERATED CONTENT==` / `==END AI-GENERATED CONTENT==` 包起来，与个人"声音"严格区分；
- 手动复制粘贴 AI 输出到 vault（"The friction keeps me from sliding into the happy path of turning my brain off"）；
- 这种"AI 隔离 + 摩擦"既保留了 AI 的效率收益，又让人有意识地选择写还是不写。

**这场争论对"是否要建 LLM Wiki"的指导：**

- 如果目的是"做个人的研究助手 / 自动维护文档"，反对意见承认 LLM Wiki 高效，但提醒成本——长期可能损失对自己知识的内部表征；
- 如果目的是"通过写作来重构知识"，LLM Wiki 把过程外包后，知识库变成"AI 的数据库，你只是问它写东西"——`qaadika` 的原话。
- 折中实践：**让 LLM 做 bookkeeping（反向链接、stale 检查、汇总），让人做 raw 决策与 voice 写作**；用源材料 + 个人笔记的两层结构隔离两个角色。

**误用：**

- 把"我写得更快了"等同于"我懂得更多了"——这是反对者反复警告的认知陷阱；
- 反过来，把"必须自己写"绝对化也越界——`qaadika` 自己也说 "I'm not totally against AI writing"，关键在标签和摩擦。

## References

- `loveparade` 论点：`data/raw/hacker_news/hacker-news-original-thread/text.txt` 行 246–248。
- `kilroy123` 类比：行 250–253。
- `nidnogg` 系列亲身反例：行 205–209、261–267。
- "AI de-skilling" 命名出现于行 263。
- `qaadika` 隔离实践：行 459–471 包含 `==BEGIN AI-GENERATED CONTENT==` 包裹的具体模板。

## Footnotes

- `nidnogg` 关键句（行 209）：
  > "I miss thinking harder and I think it would get me out of this one for sure. But the wiki workflow is just too addictive to stop."
- `nidnogg` 命名（行 263）：
  > "A slightly related note - I recently heard the term AI de-skilling, this treads close to it imo."
- `qaadika` 模板（行 468–470）：
  > "==BEGIN AI-GENERATED CONTENT==  <% tp.file.cursor(1) %>  ==END AI-GENERATED CONTENT=="
- `qaadika` 摩擦原话（行 472）：
  > "I also manually copy and paste from wherever I'm using AI into my notes. Nothing automated. The friction keeps me from sliding into the happy path of turning my brain off."
- `qaadika` 收尾断言（行 461）：
  > "There's nothing 'personal' about a knowledge base you filled by asking AI questions. It's the AI's database, you just ask it to write stuff."
