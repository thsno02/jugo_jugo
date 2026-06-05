---
schema: justification_journal.v1
card: ../cards/zero-runtime-dependency.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/llm-wiki-net/text.txt`
源证据：
- L166-168 — "Runs entirely on the host agent's built-in tools. Plugin is Markdown + commands. No servers, no services, no telemetry."
- L490-492 — "LLM Wiki uses only the built-in tools of the host agent (file read/write, web fetch, web search). The plugin itself is Markdown: command definitions, skills, and reference docs."
范围论证：零运行时依赖是与 maintenance-cost-zero（人力维护成本归零）不同维度的约束——后者讨论人类的维护负担，前者定义技术架构的依赖边界。两者共同解释了 LLM Wiki 的轻量化设计，但各自原子性完整。
