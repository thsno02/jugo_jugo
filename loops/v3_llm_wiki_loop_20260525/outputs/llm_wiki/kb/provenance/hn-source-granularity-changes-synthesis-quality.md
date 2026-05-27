---
schema: accepted_card_provenance.v3
card: ../cards/hn-source-granularity-changes-synthesis-quality.md
material_id: hacker-news-original-thread
digest_id: digest_hacker-news-original-thread
source_paths:
  - data/raw/hacker_news/hacker-news-original-thread/text.txt
draft_card: ../../drafts/cards/hn-source-granularity-changes-synthesis-quality.md
draft_provenance: ../../drafts/provenance/hn-source-granularity-changes-synthesis-quality.md
similarity_result: ../../drafts/similarity/hn-source-granularity-changes-synthesis-quality.json
comparison_provenance: ../../drafts/comparison/hn-source-granularity-changes-synthesis-quality.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T10:11:00+08:00
  gate_notes: 6/6 项通过：vbarsoum 量化数据 + 操作规则 + 边界 + 仓库链接，证据锚定行 521-523。
created_time: 2026-05-26T11:12:00+08:00
edited_time: 2026-05-27T10:11:00+08:00
edited_entity: llm
---

## 源证据

- 全部数字直接出自单条评论 `vbarsoum`（行 521–523）：
  > "I built an implementation of this and tested it on 3 Alex Hormozi books (~155K words, 68 source files). Some data for the skeptics: The naive version (each book as 1 file) produced exactly the slop people are describing here. But splitting into chapter-level files and recompiling changed the output categorically. Same model, same prompts — the only variable was source granularity. The compiler produced 210 concept pages with 4,597 cross-references (19.2 avg links per page). 20+ concepts synthesized across all 3 books unprompted — one pulled from 11 source files and found a genuine contradiction between two books that neither makes explicit. 173K words of output from 155K input. It's not compression — it's synthesis."
  > "a vector database is only useful to machines. You can't open a .faiss file and browse it. A wiki is useful to both. I open these files in Obsidian, browse the graph, follow links, read concept pages — no AI needed. But when I do ask the AI a question, it reads the same wiki pages I do, and the answers are better than RAG because the knowledge is already structured and cross-referenced instead of retrieved as raw chunks."
  > "~Cost: 12M tokens, ~10-15 min. Repo: https://github.com/vbarsoum1/llm-wiki-compiler"

## 卡片范围是否成立

卡片把 vbarsoum 提供的所有具体数字 + 关键论断逐字复用；"通用化为操作规则"是合理推广，但显式标出"边界"——这是一个个人报告而非受控实验、样本是商业书籍而非学术论文、数字未公开复核。仓库链接也明示出来以便后续验证。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T10:11:00+08:00
- 检查要点：
  - 非标题复述：实验设置 + 结果对比 + 作者点睛 + 通用化规则 + 边界，五段实质展开。
  - 知识密度：210 concept pages / 4597 cross-refs / 19.2 avg / 12M tokens / 10-15min 等具体数字。
  - 源支撑：HN 行 521-523 锚定，仓库 URL 给出。
  - References / Footnotes 存在。
  - frontmatter 完整。
  - related 字段 5 个 v3 draft id。

## 备注

- 这张卡是 batch 中唯一带量化数据的 HN 卡，单独保留有评测价值。
- Adoption 阶段观察：comparison 三个 v2 候选 jaccard 0.14-0.29 完全靠 `llm/wiki/是/的` 撞分，v2 卡都不涉源粒度评测。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/hn-source-granularity-changes-synthesis-quality.md`
- draft provenance: `../../drafts/provenance/hn-source-granularity-changes-synthesis-quality.md`
- similarity: `../../drafts/similarity/hn-source-granularity-changes-synthesis-quality.json`
- comparison provenance: `../../drafts/comparison/hn-source-granularity-changes-synthesis-quality.md`
