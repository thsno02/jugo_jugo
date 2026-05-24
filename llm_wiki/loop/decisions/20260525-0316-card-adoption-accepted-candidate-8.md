# 决策：采纳候选 8 知识卡

- `time`: `2026-05-25T03:16:50+08:00`
- `adoption_iteration`: `iteration_20260525_0008_card_adoption_raw_sources_truth`
- `task_id`: `task_20260525_0009_card_adoption_candidate_8`
- `decision`: `accepted_card_ready_for_next_candidate`

## 证据

- `inspect_delivery.py iteration_20260525_0008_card_adoption_raw_sources_truth` 返回 `delivery_inspection: pass`。
- `llm_wiki/kb/cards/raw-sources-readonly-source-of-truth.md` 已存在，且 `status: accepted`。
- `llm_wiki/kb/provenance/raw-sources-readonly-source-of-truth.md` 已存在，并链接回知识卡。
- `llm_wiki/kb/indexes/cards.md` 包含该卡标题、路径、状态和来源。
- adoption worker 完成后已关闭；该 worker 不需要常驻。

## 非阻塞观察

adoption worker 在 `read_log.md` 中记录了读取目标 KB 卡片、目标 provenance 和索引文件，用于检查覆盖冲突与保留现有索引。这些路径在任务包中属于允许写入，但没有显式列在允许输入中。当前接受为非阻塞观察，因为任务包的阻塞条件要求检查覆盖，且 worker 已记录原因和用途。后续可把 adoption 任务模板补充为：允许读取目标写入路径以做存在性和冲突检查。

## 生命周期策略

本轮关闭 adoption worker 是合适的，因为它的写入职责已经结束。后续生命周期管理不采用“一律短命”的机械规则：如果后续出现反复读取同一大来源、同一数据域或同一检索索引的任务，可以显式创建 alive sub-agent 来降低重复 IO 与上下文消耗。alive sub-agent 必须有明确职责、允许输入、读日志边界、退出条件和主控 agent 的状态记录。

## 下一步

从第一轮 source mining 候选集中选择 `候选 7` 进入下一张卡的 drafting：该候选事实是该来源把 LLM Wiki 架构分成三个层次，即原始来源、wiki 和 schema；证据范围为 `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:25-33`。
