# 候选 4 草稿进入独立审计

- `decision_time`: `2026-05-25T06:12:14+08:00`
- `controller`: `main-agent`
- `decision`: `ready_for_card_audit`
- `candidate_id`: `候选 4`
- `draft_iteration`: `iteration_20260525_0033_card_drafting_persistent_composite_wiki`
- `draft_task`: `task_20260525_0034_card_drafting_candidate_4`
- `sub_agent`: `019e5c08-a423-70d3-b44d-6f3c1956f9f2`
- `lifecycle`: worker returned `LOOP_DONE` and was closed immediately after completion.

## 判断

`card_drafting_worker` 已写出一张草稿知识卡和一份 provenance。主控 agent 只验收交付形状、读写边界和生命周期，不在此决策中替代独立内容审计。

## 证据

- `inspect_delivery.py iteration_20260525_0033_card_drafting_persistent_composite_wiki` 返回 `delivery_inspection: pass`。
- `loop_delivery.md` 包含 `LOOP_DONE` marker。
- 草稿卡 `status: draft`，`References` 早于 `Footnotes`，且 `Footnotes` 是最后一个 section。
- `read_log.md` 记录读取当前任务包、候选文件和指定来源证据；没有读取已采纳 KB 卡片、provenance、旧审计报告或 `legacy/`。

## 边界观察

`read_log.md` 记录 worker 用关键词定位候选 4 时曾返回其它候选命中行，并查看本轮 iteration 目录文件名以确认允许写入目标是否存在。该内容没有进入草稿卡或 provenance；由于 `fact_candidates.md` 是任务允许输入，且目录检查只涉及本轮允许写入目录，暂记为非阻塞边界观察。若后续重复影响可审计性，再作为失败证据进入任务模板或 worker prompt 修复。

## 生命周期判断

本轮来源证据短，任务为单候选 drafting，未出现频繁大规模 I/O 或上下文复用收益。因此保持一次性 worker 并完成后关闭是合适的。当前没有需要 alive sub-agent 常驻的证据。

## 下一步

创建 `card_audit_worker` 窄任务包，输入限定为候选 4 草稿卡、provenance 和 `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:13`。dispatch 使用 `fork_context:false`，worker 完成后关闭并验收。
