---
schema: justification_journal.v1
card: ../cards/structured-queryability-gap.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/hacker_news/hacker-news-original-thread/text.txt`
源证据：
- mpazik 评论 — "The friction shows up once you mix docs with structured things like work items or ADRs. Flat markdown doesn't query well and gets inconsistent."
- mpazik 评论 — "The AGENTS.md approach papers over this by teaching the LLM the folder conventions. Works until the data gets complex but gets worse after many iterations."
- mpazik 评论 — "Both are needed: files that open in any editor, and a structured interface the agent can actually query."
范围论证：结构化可查询性缺口是对 wiki-as-git-repo 和 schema-as-configuration 概念的具体局限性分析。它来自一位正在构建相关工具的开发者的实践经验，提出了纯 markdown 文件系统方案在混合使用场景下的架构限制。与 index-based-navigation 相关但焦点不同：后者描述索引如何辅助导航，本卡描述索引不足以支撑结构化查询。
