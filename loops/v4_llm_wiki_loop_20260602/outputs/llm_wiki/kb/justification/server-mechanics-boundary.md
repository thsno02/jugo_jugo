---
schema: justification_journal.v1
card: ../cards/server-mechanics-boundary.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/pypi/pypi-llm-wiki-mcp/text.txt`
源证据：
- L177 — "The server enforces mechanics, not content shape"
- L187 — "The server does not validate frontmatter shape, page categories, or link targets. That layer lives in your wiki/CLAUDE.md schema doc and grows with the LLM. Karpathy's gist is deliberately silent on content shape; baking a schema into the server would defeat the point."
- L117 — "The server handles the boring layer LLMs keep getting wrong: atomic writes, etag conflict checks, append-only log integrity, path containment."
范围论证：此卡聚焦于服务器的力学-内容边界划分原则及其设计论据，与 three-layer-architecture（数据的三层分类）和 schema-as-configuration（schema 的配置角色）为不同维度：前者是「服务器做什么/不做什么」的工程边界，后两者分别是数据模型和 schema 的语义角色
