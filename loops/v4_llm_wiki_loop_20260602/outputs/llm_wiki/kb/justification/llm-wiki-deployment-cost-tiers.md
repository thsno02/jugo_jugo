---
schema: justification_journal.v1
card: ../cards/llm-wiki-deployment-cost-tiers.md
created_time: 2026-06-11T10:00:00+08:00
---

## creation | 2026-06-11T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/webpage/anthemcreation-en-guide/markdown.md`
源证据：
- L40-44 — 三行结构化成本表格：Obsidian + Llama 3 (Free/0), Obsidian + Claude API (Free/~0.01-0.10 per doc), Wiki of 100 docs (Less than 10 EUR/Low)
- L7 — "The cost is almost zero for personal use, with open-source LLMs for no recurring cost."
- L59 — "Optimized local LLMs (like Llama) making the system zero-cost and fully private"
范围论证：该来源的大部分内容已被现有卡片覆盖（llm-wiki-pattern、three-layer-architecture、compile-time-vs-query-time、ingest-operation、model-quality-error-propagation、llm-wiki-scale-boundary、llm-wiki-rag-depth-distinction、wiki-rag-hybrid-pattern、llm-wiki-v2-agentmemory 等）。本卡提取了一项增量原子知识——具体的部署成本三档结构化数据。现有卡片中 compounding-cost-honesty 从学术 token 消耗角度分析成本，maintenance-cost-zero 从维护负担角度分析成本，full-stack-locality 从隐私角度分析开源/本地方案，但无卡给出终端用户实际现金支出的结构化数据。本卡填补这一空白。
