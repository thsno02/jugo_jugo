---
schema: justification_journal.v1
card: ../cards/memory-lifecycle-metadata.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/openaitoolshub-six-months/text.txt`
源证据：
- L54 — "every page has last_verified: 2026-05-01, confidence: high|medium|low, and (when relevant) superseded_by: another-page.md or contradicts: an-older-claim.md"
- L54 — "v1 has none of these."
- L54 — "After three months I had pages with stale ChatGPT pricing claims sitting next to fresh ones, both confidently asserted. The lifecycle fields fixed it."
范围论证：记忆生命周期元数据是一组具体的 frontmatter 字段，解决知识时效性管理问题。它与 schema-as-configuration（schema 的配置角色）层级不同——schema 定义总体规则，lifecycle 字段是 schema 中的具体字段设计。与 continuous-drift-detection（漂移检测）相关但更具体——本卡定义的是字段本身，漂移检测关注的是检测过程。
