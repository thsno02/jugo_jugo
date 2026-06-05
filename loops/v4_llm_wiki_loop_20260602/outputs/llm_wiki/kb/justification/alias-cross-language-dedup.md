---
schema: justification_journal.v1
card: ../cards/alias-cross-language-dedup.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/webpage/obsidian-community-plugin/text.txt`
源证据：
- L262-263 — "Mandatory Page Aliases — Every generated page includes at least 1 alias (translation, acronym, alternate name), enabling cross-language duplicate detection"
- L413-414 — "Two-tier semantic detection: Tier 1 (always LLM-verified) catches cross-language matches, abbreviations, high-similarity titles. Tier 2 fills remaining token budget with moderate-similarity candidates."
- L265-266 — "Duplicate Detection & Merge — Semantic tiering catches true duplicates; intelligent LLM merge fuses content and preserves aliases"
- L341 — 示例中 aliases: ["监督学习", "Supervised Learning"]
范围论证：别名系统 + 两层语义去重是该插件独创的知识质量机制，现有 KB 中 lint-operation 卡仅提及去重为巡检功能之一，未展开其机制；该卡填补这一空白
