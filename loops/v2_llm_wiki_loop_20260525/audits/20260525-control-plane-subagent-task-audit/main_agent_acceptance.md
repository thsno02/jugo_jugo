# 主控验收记录

`status`: `ACCEPTED_WITH_CORRECTIONS`
`accepted_at`: `2026-05-25T14:29:00+08:00`

## 验收范围

本次验收覆盖三个 one-shot sub-agent 审计产物：

- `subagent_lifecycle_audit.md`
- `task_boundary_audit.md`
- `task_flow_audit.md`

三个 worker 均已完成并由主控 agent 调用 `close_agent` 关闭：

- `019e5dc4-eb72-7fd1-8fc5-929a746a88ff` / Darwin
- `019e5dc4-ec89-7c20-a3e1-6d1ebd58dca4` / Bohr
- `019e5dc4-ef58-76a2-bfaf-9569a9b60e03` / Banach

## 总体判断

三份审计都给出 `concern`，且没有 P0 阻塞。主控 agent 接受核心结论：当前 loop 已经比旧 loop 更可恢复、更有任务边界，但 sub-agent 生命周期、任务边界工具化、similarity 流程和 card 质量门仍需要下一轮控制面修正。

本次审计同时确认了一个重要事实：当前工作区存在未提交的 similarity/fusion 控制面草稿，不能把这些草稿当成稳定历史。后续修正应先回到用户已确认的设计，再决定是否保留、改写或丢弃这些草稿。

## 接受的结论

1. sub-agent 不是单点失控，而是旧 loop 把许多机械小步骤都人格化，缺少 `spawned -> completed -> closed` 生命周期账本。
2. `fork_context: false`、one-shot worker、任务包、`read_log.md`、`loop_delivery.md` 和完成后关闭，是正确方向。
3. `LOOP_DONE` 不能等同于 sub-agent 已关闭；`close_agent` 也需要落盘 registry 记录。
4. `validate_scope.py` 和 `inspect_delivery.py` 目前只是结构检查，不能证明真实读写隔离。
5. `read_log.md` 有审计价值，但仍是 worker 自报；需要更结构化的 read-log 对账。
6. Atomic Draft First 方向正确，但必须把 title similarity top3 和三问 comparison 拆清楚。
7. card 质量门应从 `atomic fact card` 转向 `scoped knowledge card`：card 本身必须是有信息量的知识单位，而不是标题或候选 statement 的 paraphrase。

## 主控修正

流程审计中有一条建议不采纳：它建议暂缓把 `tags`、`created_time`、`edited_time`、`edited_entity` 放入 card drafting gate。该建议与用户刚刚明确的 card schema 方向冲突。

主控修正为：

- card metadata 需要稳定 schema。
- `tags` 是 agent 自主生成的 hashtag 列表，如 `#llm`，不要求固定范式。
- `created_time` 记录 card 创建时间。
- `edited_time` 记录最近一次实质修改时间。
- `edited_entity` 必须区分 `llm`、`human`、`llm+human`。
- 正文不应套强模板，但 metadata、References、Footnotes 和 provenance link 应稳定。
- References 是 source-level citation，需要说明引用范围。
- Footnotes 是 inline citation，只给 locator/link，且保持最后一个 section。

## 下一步优先级

1. 先冻结当前未提交的 similarity/fusion 草稿状态：决定是重写、保留为草稿，还是丢弃旧误解产生的部分。
2. 设计轻量 similarity 工具/流程：对 card title 用 jieba 分词，按 Jaccard 或 set similarity 取 top 3。
3. 将 top 3 与三问 comparison 分成清楚阶段：先列相似候选，再阅读 A 卡并回答共同点、差异、下一步依据。
4. 更新 card 模板：稳定 metadata，自由知识正文，References / Footnotes 分工清楚。
5. 新增 sub-agent lifecycle registry，至少记录 spawned、completed、closed / close_unverified。
6. 增强 task boundary 工具：role-aware validation、expected artifacts、read_log 对账、candidate block / JSON pointer 检查。

## 当前不做

- 不把当前未提交的 similarity/fusion 草稿直接当成已接受实现。
- 不继续派发 `iteration_20260525_0064_card_batch_drafting_karpathy_launch_remaining_a`，直到 card schema 和 similarity gate 被修正。
- 不把 draft backlog 当作公开 KB。
