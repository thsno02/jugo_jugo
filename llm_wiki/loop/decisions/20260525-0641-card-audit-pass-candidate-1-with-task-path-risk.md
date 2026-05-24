# 候选 1 audit pass 与任务包路径风险

- `timestamp`: `2026-05-25T06:41:18+08:00`
- `iteration_id`: `iteration_20260525_0037_card_audit_llm_wiki_pattern_file`
- `task_id`: `task_20260525_0038_card_audit_candidate_1`
- `sub_agent`: `019e5c22-35a8-7c40-b089-e546cf3e0cf8`
- `decision`: `audit_pass_with_control_plane_repair_required`

## 证据

- `inspect_delivery.py iteration_20260525_0037_card_audit_llm_wiki_pattern_file` 返回 `delivery_inspection: pass`。
- `loop_delivery.md` 写入 `LOOP_DONE`，并给出 `audit_result: pass`。
- `artifacts/audit_report.md` 明确结论为 `audit_result: pass`，理由是草稿卡主事实可由 `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:1-5` 支撑。
- `read_log.md` 记录 `llm_wiki/loop/iterations/iteration_20260525_0001_source_mining_karpathy_gist/artifacts/fact_candidates.md` 读取失败。
- 实际 source mining 交付位于 `llm_wiki/loop/iterations/iteration_20260525_0002_source_mining_karpathy_gist/artifacts/fact_candidates.md`。

## 判断

本次 audit pass 可以接受为进入采纳前置结论，因为知识卡事实支撑来自任务包允许的原始来源行 `1-5`，而不是候选文件；drafting provenance 中引用的候选文件路径也是实际存在的 `0002_source_mining` 路径。

但 audit 任务包把 `fact_candidate_path` 写成不存在的 `0001_source_mining`，且 `validate_scope.py` 未能在派发前发现该允许输入路径不存在。这是控制面失败证据，应先修复 scope validation，再继续候选 1 adoption。

## 生命周期记录

候选 1 audit worker 是 one-shot worker，完成后已关闭。该任务没有表现出需要 alive worker 常驻的证据；问题来自主控任务包路径与校验工具能力不足，不来自 worker 生命周期。

## 下一步

创建显式 tooling repair iteration，最小修复 `llm_wiki/loop/tools/validate_scope.py`，使其在任务包允许输入区发现不存在的必需本地路径时失败；完成后用 independent evaluator 审计修复，再恢复候选 1 adoption。
