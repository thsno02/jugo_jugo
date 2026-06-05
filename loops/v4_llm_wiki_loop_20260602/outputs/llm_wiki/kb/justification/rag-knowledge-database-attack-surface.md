---
schema: justification_journal.v1
card: ../cards/rag-knowledge-database-attack-surface.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt`
源证据：
- introduction.tex — "we find that knowledge databases of RAG systems introduce a new and practical attack surface"
- introduction.tex — "an attacker could inject malicious texts by maliciously editing Wikipedia pages"
- preliminary.tex — "We consider that an attacker cannot access texts in a knowledge database, and cannot access the parameters nor query the LLM"
- background.tex — "our attacks do not poison the training dataset of a LLM or a retriever. Instead, our attacks exploit the new and practical attack surface introduced by knowledge databases of RAG systems."
范围论证：此概念是 PoisonedRAG 论文的核心前提，将知识库识别为 RAG 特有的攻击面，独立于 LLM 本身或检索器的安全性。这一概念界定清晰、原子性强，不与具体攻击方法或防御混淆。
