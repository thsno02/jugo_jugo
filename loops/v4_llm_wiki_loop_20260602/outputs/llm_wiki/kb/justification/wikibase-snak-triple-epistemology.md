---
schema: justification_journal.v1
card: ../cards/wikibase-snak-triple-epistemology.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/webpage/wikibase-data-model/text.txt`
源证据：
- "Snaks" section, lines 464-475 — "Snaks are the basic information structures... PropertySnak := PropertyValueSnak | PropertySomeValueSnak | PropertyNoValueSnak"
- "PropertyNoValueSnak" section, lines 507-513 — 明确无值与尚未录入的区分
- "PropertySomeValueSnak" section, lines 515-527 — 存在但未知的值
范围论证：三种 Snak 类型不仅是语法分类，更编码了三种不同的认识论状态（已知值/明确无值/存在但未知），这一设计在知识库系统中具有范式意义，值得独立成卡。
