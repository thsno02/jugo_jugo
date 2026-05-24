# drafting 候选块读取边界修复报告

- `task_id`: `task_20260525_0046_drafting_candidate_boundary_repair`
- `iteration_id`: `iteration_20260525_0045_drafting_candidate_boundary_repair`
- `result`: `repair_completed`

## 失败证据

候选 6 drafting 的 `read_log.md` 记录：读取 `fact_candidates.md` 时，检索上下文返回了前一候选的尾部几行。该内容未用于知识卡事实、表述或 provenance，但满足 `20260525-read-boundary-noise-reflection.md` 中的复开条件：相邻候选内容不再只是标题，而包含其它候选字段片段。

## 修改内容

- `card_drafting_worker.md`：要求读取 `fact_candidates.md` 时只读取任务指定的候选块；禁止把带上下文的关键词检索结果作为候选证据；若工具意外显示相邻候选内容，必须丢弃、改用精确候选块读取并写入 `read_log.md`。
- `card_drafting_task.md`：在任务模板中加入候选读取边界，明确相邻候选字段、标题或表述不得进入知识卡、provenance 或审计证据。

## 为什么是最小修复

本次只处理候选字段读取边界，不改变知识卡极简契约，不改变 audit/adoption 链路，不引入 hub、cluster、topic coverage 或复杂 metadata，也不重写候选 6 草稿卡。

## 生命周期判断

本次失败来自单次 drafting worker 的候选定位命令，而不是大规模来源读取成本或长期记忆需求。因此继续使用 one-shot worker；暂不引入 alive sub-agent。若未来 source mining 对同一大型来源反复读取且任务包能稳定限制写入面，再单独记录 lifecycle decision。

## 验证

- 任务包预期通过 `validate_scope.py`。
- 后续需由 `independent_evaluator` 审计：改动是否与失败证据匹配、范围是否最小、是否保留 atomic fact card 生产目标。

## 剩余风险

Prompt/template 只能降低 worker 使用带上下文检索的概率，不能从工具层完全阻止相邻文本显示。若后续仍出现相邻候选字段暴露，应考虑在 task packet 中提供精确行号或增加专用 candidate-block extractor 工具。
