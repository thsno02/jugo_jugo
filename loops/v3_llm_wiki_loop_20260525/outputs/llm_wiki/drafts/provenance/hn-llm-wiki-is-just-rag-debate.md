---
schema: draft_card_provenance.v3
draft_card: ../cards/hn-llm-wiki-is-just-rag-debate.md
material_id: hacker-news-original-thread
digest_id: digest_hacker-news-original-thread
source_paths:
  - data/raw/hacker_news/hacker-news-original-thread/text.txt
created_time: 2026-05-26T11:10:00+08:00
edited_time: 2026-05-26T11:10:00+08:00
edited_entity: llm
---

## 源证据

- 主张 "just RAG"（行 108–111，作者 kenforthewin）：
  > "This is just RAG. Yes, it's not using a vector database - but it's building an index file of semantic connections, it's constructing hierarchical semantic structures in the filesystem to aid retrieval .. this is RAG."
- 反驳"RAG ≠ embeddings"（行 114–116，panarky）：
  > "There's nothing about RAG that requires embeddings. The retrieval part can be grep if you don't care about semantic search."
- write-loop 是关键差异（行 135–139，darkhanakh）：
  > "the interesting bit here is the write loop - the LLM is authoring and maintaining the wiki itself, building backlinks, filing its own outputs back in. thats not retrieval thats knowledge synthesis. in vanilla RAG your corpus is static, here it isnt also the linting pass is doing something genuinely different - auditing inconsistencies, imputing missing data, suggesting connections."
- "persistent memory RAG"（行 141–144，devmor）：
  > "This is just persistent memory RAG. I have had a setup like this since about a day after I started using copilot, except it's an MCP server that uses sqlite-vec and has recall endpoints to contextually load the proper data instead of a bunch of extra files polluting context."
- kenforthewin 二次回复（行 146–150）。
- "compaction for RAG"（行 419，mememememememo）。

## 卡片范围是否成立

卡片只综合了 HN 帖子里围绕"是不是 RAG"这一线索的连续评论；每个引文都对应一段帖子原文（且都引用了用户名和行号）。卡片把这场争论提炼为"差异在 write loop"的设计分歧，并明示了"反过来过度营销"的边界——这是从评论 `kenforthewin` 二次回复中合理引申。

## 发表门控结果

本轮未运行。

## 备注

- 与 v2 中可能已有的 "LLM Wiki vs RAG" 卡片大概率重叠。比较阶段决定 `merge_candidate` 还是 `new_card`。
