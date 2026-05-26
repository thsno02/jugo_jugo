---
schema: draft_card_provenance.v3
draft_card: ../cards/hn-source-granularity-changes-synthesis-quality.md
material_id: hacker-news-original-thread
digest_id: digest_hacker-news-original-thread
source_paths:
  - data/raw/hacker_news/hacker-news-original-thread/text.txt
created_time: 2026-05-26T11:12:00+08:00
edited_time: 2026-05-26T11:12:00+08:00
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

本轮未运行。

## 备注

- 这张卡是 batch 中唯一带量化数据的 HN 卡，在比较阶段宜单独保留，避免被合并到泛论性 PKM 卡。
