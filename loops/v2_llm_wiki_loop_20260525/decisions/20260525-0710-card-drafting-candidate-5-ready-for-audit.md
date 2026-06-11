# 候选 5 drafting 可进入 audit

- `timestamp`: `2026-05-25T07:10:16+08:00`
- `iteration_id`: `iteration_20260525_0041_card_drafting_human_llm_roles`
- `task_id`: `task_20260525_0042_card_drafting_candidate_5`
- `sub_agent`: `019e5c3d-a498-7541-8ad4-39ff64ec6654`
- `decision`: `ready_for_card_audit`

## 证据

- `inspect_delivery.py iteration_20260525_0041_card_drafting_human_llm_roles` 返回 `delivery_inspection: pass`。
- `loop_delivery.md` 写入 `LOOP_DONE`。
- `artifacts/draft_card.md` 只生成一张草稿卡，包含 `statement`、`fact_type`、`support`、`scope`、`status: draft`。
- `References` 位于 `Footnotes` 前，`Footnotes` 是最后一个 section。
- `artifacts/provenance.md` 说明事实来源、支撑关系、整理边界、成立范围和 draft 原因。

## 边界记录

`read_log.md` 记录两类非阻塞读取：

- 读取 `~/.codex/skills/agent-loop-runner/SKILL.md`，仅用于运行环境要求的流程约束，不用于知识卡事实内容或来源支撑。
- 用 `rg` 核对候选 5 时意外显示下一候选标题起始行，随后改用精确 `sed` 读取候选 5；相邻候选内容未用于卡片或 provenance。

这些边界噪声已写入 `llm_wiki/loop/reflections/20260525-read-boundary-noise-reflection.md`。当前不阻塞 audit，因为草稿事实支撑仍限定在任务包指定来源行 `15-16,68-69`。

## 生命周期记录

候选 5 drafting worker 是 one-shot worker，完成后已关闭。当前没有证据表明该任务应使用 alive worker 常驻；证据量小，重复 I/O 成本不高。

## 下一步

创建候选 5 `card_audit_worker` 任务包，输入限定为候选 5 草稿卡、provenance、来源 `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:15-16,68-69`、以及候选 5 字段；dispatch 使用 `fork_context:false`。
