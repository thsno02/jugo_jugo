# 候选 6 drafting 交付与读取边界修复要求

- `timestamp`: `2026-05-25T07:33:28+08:00`
- `iteration_id`: `iteration_20260525_0044_card_drafting_llm_wiki_use_cases`
- `task_id`: `task_20260525_0045_card_drafting_candidate_6`
- `sub_agent`: `019e5c53-1675-78b2-ae82-029f1ec37cdd`
- `decision`: `delivery_accepted_prompt_repair_required_before_audit`

## 交付证据

- `inspect_delivery.py iteration_20260525_0044_card_drafting_llm_wiki_use_cases` 返回 `delivery_inspection: pass`。
- `loop_delivery.md` 写入 `LOOP_DONE`。
- `artifacts/draft_card.md` 只生成一张草稿卡，包含 `statement`、`fact_type`、`support`、`scope`、`status: draft`。
- `References` 位于 `Footnotes` 前，`Footnotes` 是最后一个 section。
- 草稿卡保持为“该来源列举了一组可能应用场景”这一清单型事实，没有扩写成场景报告、用例体系、hub、cluster 或 topic coverage。

## 失败证据

`read_log.md` 记录读取 `fact_candidates.md` 时“检索上下文返回了前一候选的尾部几行；未用于本卡事实、表述或出处论证”。这满足 `llm_wiki/loop/reflections/20260525-read-boundary-noise-reflection.md` 中的复开条件：相邻候选内容不再只是标题，而包含其它候选字段片段。

## 判断

候选 6 草稿卡本身可保留，不需要由主控 agent 重写；但在进入 audit 之前，应先做最小 prompt/template repair，降低后续 drafting worker 暴露相邻候选字段的概率。

这不是事实污染失败，也不是上下文泄漏导致的产物失败；它是读取边界可审计性失败。修复范围应限于 drafting worker / drafting task template 的候选块读取规则。

## 生命周期记录

候选 6 drafting worker 是 one-shot worker，完成后已关闭。当前问题不来自长期 worker 记忆或大规模 I/O 成本，因此不需要改为 alive worker。

## 下一步

创建显式 prompt/template repair iteration，最小修改 `llm_wiki/loop/system_prompts/card_drafting_worker.md` 或 `llm_wiki/loop/task_templates/card_drafting_task.md`，要求读取 `fact_candidates.md` 时只读取指定候选块；修复后用 independent evaluator 审计，再恢复候选 6 audit。
