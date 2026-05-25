# 决策：接受 delivery marker prompt 修复

- `time`: `2026-05-25T02:54:44+08:00`
- `repair_iteration`: `iteration_20260525_0004_delivery_marker_prompt_repair`
- `audit_iteration`: `iteration_20260525_0005_prompt_repair_audit`
- `decision`: `accept_prompt_repair_and_rerun_card_drafting`

## 证据

- `iteration_20260525_0004_delivery_marker_prompt_repair` 只修改了 `llm_wiki/loop/system_prompts/base_worker.md` 中与 `loop_delivery.md` marker 有关的一条规则。
- 该修复 iteration 通过 `validate_scope.py` 和 `inspect_delivery.py`。
- `iteration_20260525_0005_prompt_repair_audit/artifacts/independent_audit.md` 的结论为 `audit_result: pass`。
- 审计确认修复没有扩大 worker 权限，没有修改知识卡正文、provenance、来源证据或 KB schema。
- prompt 修复审计 worker 完成后已关闭，避免 sub-agent 生命周期悬挂。

## 决策

接受本次 prompt 修复。旧的 `iteration_20260525_0003_card_drafting_raw_sources_truth` 产物虽有草稿卡和 provenance，但交付文件缺少标准 marker，不能作为进入 card audit 的有效交付。

## 下一步

新开 `card_drafting_worker` revision iteration，重新处理同一个 `候选 8`。主控 agent 不手工补写旧 iteration，也不亲自写卡或 provenance。
