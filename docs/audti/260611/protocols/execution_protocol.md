# 执行协议（Execution Protocol）

## 目标

把 Codex/Claude 开发过程按日期梳理为可审计文档。所有具体梳理、审计、返修和最终合并由 sub-agent 执行；主控 agent 只负责调度、验收、状态推进和协议维护。

## 通用变量

- `audit_root`: `docs/audti/260611`
- `project_root`: `.`
- `day_id`: `YYYYMMDD`
- `source_date`: `YYYY-MM-DD`
- `main_language`: 中文
- `terminology_policy`: 用「中文（English）」锚定关键术语。

## 角色边界

- inventory worker：只写 `README.md`、`source_inventory.md`、`day_queue.md`、`logs/inventory_*` 和必要目录。
- daily synthesis worker：只写 `daily/YYYYMMDD_*.md` 与 `logs/day_YYYYMMDD_read_log.md`。
- independent audit worker：只写 `audits/YYYYMMDD_*_audit.md`。
- repair worker：只写 `repairs/YYYYMMDD_*` 和返修版 daily 文件；不得自行判通过。
- final synthesis worker：只读取已 `accepted` 日期，写 `final/total_timeline.md` 与必要 evidence map。
- main agent：只写 `decisions/YYYYMMDD_acceptance.md`、更新 `day_queue.md` 状态、维护通用协议。

## 证据优先级

1. 原始会话记录（transcript）：Claude JSONL、Codex JSONL。
2. 循环产物（loop artifacts）：`loops/v0*` 到 `loops/v4*`。
3. 提交历史（git history）：`git log --date=iso --name-status`。
4. 人类洞察索引（user-insights）：仅作二级索引，不能作为唯一事实源。
5. `docs/**`：仅作二次对照，不能作为唯一事实源。

## 日期归属

- 默认使用 Asia/Shanghai 本地日期。
- UTC 字面日期命中必须转换到本地日期后再归属。
- 区分运行发生时间（execution time）和 git 固化时间（git solidification time）。
- 后验归档文件（retrospective archive）不能直接当作原始当天事实。

## 门禁

每日推进必须满足：

- 日报存在且 `audit_status: pending` 或已进入返修链路。
- 独立审计明确 `audit_result: pass`。
- 审计明确 `gate_decision: advance`。
- 主控写入 `decisions/YYYYMMDD_acceptance.md`。
- `day_queue.md` 更新为 `accepted`、`repair_required` 或 `blocked`。

空窗日也必须经过 daily synthesis、independent audit 和 main-agent acceptance；验收记录必须标注 `empty_window_pass`。
