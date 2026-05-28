---
id: hn-source-granularity-changes-synthesis-quality
title: HN 实证——源文件粒度是 LLM Wiki 合成质量的杠杆
status: accepted
card_type: example_pattern
tags: [#llm-wiki, #source-granularity, #empirical, #hacker-news]
created_time: 2026-05-26T11:12:00+08:00
edited_time: 2026-05-28T11:05:00+08:00
edited_entity: llm
source_ids: [hacker-news-original-thread]
provenance_card: ../provenance/hn-source-granularity-changes-synthesis-quality.md
aliases: ["source granularity matters", "chapter-level vs book-level"]
related: [karpathy-wiki-extraction-granularity]
---

HN 评论里最稀有的不是观点，而是**数字**。`vbarsoum` 给了一个可复现的实证[^src1]——把同样的模型、同样的提示词、同样的 3 本 Alex Hormozi 书（~155K 词、68 个源文件）按两种粒度喂给 Karpathy 的 LLM Wiki 模式，结果"完全不同类"。

**实验设置：**

- 输入：155K 词 / 68 文件；
- 模型与提示词：固定不变；
- **唯一变量**：源文件粒度——"naive 版（每本书 1 个文件）" vs "章节级（每章 1 个文件）"。

**结果对比：**

- naive 版："produced exactly the slop people are describing here"——印证 HN 里大量"LLM 输出是 slop"的吐槽；
- 章节级 + 重新编译：210 个概念页 / **4,597 个交叉引用** / 平均每页 19.2 个 link；
- 20+ 个跨三本书的合成概念出现，其中一个跨 11 个源文件被合到一起；
- 找到了两本书之间一个**两书都未明说**的内在矛盾；
- 输出 173K 词，输入 155K 词——`vbarsoum` 强调："**It's not compression — it's synthesis**"；
- 成本 12M tokens，10–15 分钟。

**作者点睛**[^src2]：

> "a vector database is only useful to machines. You can't open a .faiss file and browse it. A wiki is useful to both. ... when I do ask the AI a question, it reads the same wiki pages I do, and the answers are better than RAG because the knowledge is already structured and cross-referenced instead of retrieved as raw chunks."

**通用化为操作规则：**

- 在搭 LLM Wiki 之前，把"raw 文档要切到什么粒度"作为**第一个超参**调[^v3-1]，而不是默认"一篇文章一文件"或"一整本书一文件"；
- 评估粒度时盯三件事：**合成概念数**、**跨文件引用数**、**跨文件矛盾被识别数**——这是 vector RAG 评测不会用、但对 sensemaking 任务最相关的指标；
- "wiki is useful to both humans and machines" 是 LLM Wiki 相对 vector DB 的根本设计差异；如果你的 raw 粒度让人类也无法浏览/校验，那机器读出来也不会更好。

**边界：**

- 这是单个用户报告的实测，不是受控实验；样本是商业书籍而非学术论文。
- "20+ 概念合成 / 找到矛盾"等数字未公开数据集供复核。
- 仓库地址 [github.com/vbarsoum1/llm-wiki-compiler](https://github.com/vbarsoum1/llm-wiki-compiler)[^url1]（评论中给出）。

## Footnotes

[^src1]: `data/raw/hacker_news/hacker-news-original-thread/text.txt` 行 521-523（`vbarsoum` 完整原文）— "But splitting into chapter-level files and recompiling changed the output categorically. Same model, same prompts — the only variable was source granularity. The compiler produced 210 concept pages with 4,597 cross-references (19.2 avg links per page). 20+ concepts synthesized across all 3 books unprompted — one pulled from 11 source files and found a genuine contradiction between two books that neither makes explicit. 173K words of output from 155K input. It's not compression — it's synthesis. ~Cost: 12M tokens, ~10-15 min."
[^src2]: 同文件 行 523 — "a vector database is only useful to machines. You can't open a .faiss file and browse it. A wiki is useful to both."
[^url1]: <https://github.com/vbarsoum1/llm-wiki-compiler>
[^v3-1]: [karpathy-wiki-extraction-granularity](karpathy-wiki-extraction-granularity.md) — Karpathy 插件的五档抽取粒度作为另一种"粒度即超参"实现。
