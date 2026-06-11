# Codex/Claude 开发时间线审计包

目标目录：`docs/audti/260611`。注意目录名是 `audti`，不是 `audit`。

本审计包用于承接 Codex/Claude 开发时间线审计计划：先建立文件化骨架、证据目录（source inventory）和日期队列（day queue），再由 sub-agent 按日执行每日梳理（daily synthesis）、独立审计（independent audit）、返修（repair）和最终总线路（final timeline）。

通用规则已经文件化到 `protocols/` 和 `tasks/`。后续派发 sub-agent 时，主控只需要指定 `day_id` 与角色，让 worker 读取对应 task 文件和 `day_queue.md`，不再重复粘贴完整 prompt。

## 工作流（Workflow）

1. 读取原始证据源（primary evidence）：Claude JSONL、Codex JSONL、loop capsule、git log、user-insights。
2. 将证据按来源类型（source type）与日期覆盖（date coverage）汇总到 `source_inventory.md`。
3. 从可证据化起点到最后实质开发记录建立 `day_queue.md`。
4. 每日梳理 worker 读取 `tasks/daily_synthesis_task.md`，一次只处理一个 `day_id`。
5. 独立审计 worker 读取 `tasks/independent_audit_task.md`，只写审计报告，不修改日报。
6. 若审计要求返修，repair worker 读取 `tasks/repair_task.md`，只处理 required changes。
7. 主控在审计通过后写 `decisions/YYYYMMDD_acceptance.md` 并更新 `day_queue.md`。
8. 所有 accepted 日期完成后，final worker 读取 `tasks/final_timeline_task.md`，只合并已验收材料。

## 门禁（Gates）

- 不把当前 `2026-06-11` 本轮审计筹备混入历史开发线路。
- 不把 `docs/**` 作为唯一事实源（sole source of truth）；`docs/**` 只能作二次对照（secondary corroboration）。
- 不回滚、删除或修改他人/主线程已有改动。
- 仅允许写入 `docs/audti/260611/**`。
- 每日队列状态从 `pending` 经独立审计和主控验收后变为 `accepted`；空窗日可用 `accepted`，但必须在 decision 中标注 `empty_window_pass`。
- 发现未跟踪文件（untracked files）只记录，不处理。
- 所有 sub-agent 默认使用 `xhigh` thinking effort，因为本任务涉及大量 transcript/log/artifact 证据。

## 目录结构（Directory Structure）

- `daily/`：后续每日梳理正文占位；本轮不写入每日正文。
- `audits/`：后续审计日报或专项审计材料占位；本轮不生成审计日报。
- `repairs/`：后续修复计划（repair plan）和修复验证（repair verification）占位。
- `decisions/`：后续审计决策记录（decision record）占位。
- `final/`：后续最终总线路（final master timeline）占位；本轮不生成。
- `logs/`：本轮 inventory 读取日志与交付说明。
- `protocols/`：不变的执行协议、门禁和路径约束。
- `tasks/`：sub-agent 每次执行时读取的通用任务文件。

## 本轮产物（Artifacts）

- `source_inventory.md`
- `day_queue.md`
- `logs/inventory_read_log.md`
- `logs/inventory_delivery.md`

## 通用任务入口（Task Entrypoints）

- 每日梳理：`tasks/daily_synthesis_task.md`
- 独立审计：`tasks/independent_audit_task.md`
- 返修：`tasks/repair_task.md`
- 最终合并：`tasks/final_timeline_task.md`

派发格式建议：

```text
读取 docs/audti/260611/tasks/<task>.md，并按 day_id=<YYYYMMDD> 执行。
只写 task 文件允许的路径。完成后按 task 文件要求返回 marker。
```
