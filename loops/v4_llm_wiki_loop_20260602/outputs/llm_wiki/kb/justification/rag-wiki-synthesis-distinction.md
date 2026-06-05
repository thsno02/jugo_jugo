---
schema: justification_journal.v1
card: ../cards/rag-wiki-synthesis-distinction.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/hacker_news/hacker-news-original-thread/text.txt`
源证据：
- kenforthewin 评论 — "This is just RAG. Yes, it's not using a vector database - but it's building an index file of semantic connections... this is RAG."
- darkhanakh 评论 — "the interesting bit here is the write loop - the LLM is authoring and maintaining the wiki itself, building backlinks, filing its own outputs back in. thats not retrieval thats knowledge synthesis."
- darkhanakh 评论 — "the linting pass is doing something genuinely different - auditing inconsistencies, imputing missing data, suggesting connections. thats closer to assistant maintaining a zettelkasten than a search engine returning top-k chunks"
- kenforthewin 回复 — "I agree with you, the linting pass seems valuable"
范围论证：该辩论明确区分了 RAG（静态语料+检索）与 LLM Wiki（动态语料+写入循环+巡检综合）的分界线，这是对 LLM Wiki 模式定义的社区共识层面的贡献，值得独立成卡。与 wiki-compounding-artifact 关联但聚焦于与 RAG 的对比。
