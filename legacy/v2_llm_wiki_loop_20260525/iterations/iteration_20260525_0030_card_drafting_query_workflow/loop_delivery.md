LOOP_DONE

task_id: task_20260525_0031_card_drafting_candidate_12
role: card_drafting_worker

delivered:
- `llm_wiki/loop/iterations/iteration_20260525_0030_card_drafting_query_workflow/artifacts/draft_card.md`
- `llm_wiki/loop/iterations/iteration_20260525_0030_card_drafting_query_workflow/artifacts/provenance.md`
- `llm_wiki/loop/iterations/iteration_20260525_0030_card_drafting_query_workflow/loop_status.md`
- `llm_wiki/loop/iterations/iteration_20260525_0030_card_drafting_query_workflow/read_log.md`

summary: 已把 `候选 12` 写成一张 zet 风格原子事实草稿卡，并写出整理后的出处论证。知识卡状态保持为 `draft`。

validation:
- 只生成一张知识卡。
- 知识卡包含 `statement`、`fact_type`、`support`、`scope`、`status: draft`。
- 知识卡中 `References` 位于 `Footnotes` 前，且 `Footnotes` 是最后一个 section。
- 出处论证说明了事实来源、支撑关系、来源明说内容、整理表述、成立范围和 draft 原因。
- 未采纳知识卡，未扩写主题页，未使用额外事实来源补充卡片事实。
