# 模板修复报告：adoption 目标路径读取边界

## 失败证据

两次 adoption worker 都需要读取目标 KB 卡片、目标 provenance 和 `llm_wiki/kb/indexes/cards.md`，并把这些读取记录为“额外读取”：

- `llm_wiki/loop/iterations/iteration_20260525_0008_card_adoption_raw_sources_truth/read_log.md`
- `llm_wiki/loop/iterations/iteration_20260525_0011_card_adoption_architecture_layers/read_log.md`

读取用途是合理的：检查目标文件是否存在、避免覆盖已有不同内容、保留既有索引并做最小增量更新。问题在于模板没有把这些目标路径列为允许输入。

## 修改内容

修改 `llm_wiki/loop/task_templates/card_adoption_task.md`：

- 在 `允许输入` 中增加 `target_card_path`、`target_provenance_path` 和 `target_index_path`。
- 明确这些路径只能用于存在性检查、覆盖冲突检查和最小索引增量更新。
- 在 `采纳规则` 中强调不得用目标 KB 里的其它内容补充事实。

## 为什么是最小修改

本次修复只补齐 worker 实际需要的读边界，没有改变 adoption worker 的写入范围、采纳条件、card schema、KB schema 或生产目标。它不允许 worker 读取未授权来源，也不允许创建 hub、cluster、topic coverage 或批量采纳。

## 剩余风险

后续 `create_task.py` 生成 adoption task 时，仍需要主控 agent 填入具体 `target_card_path` 和 `target_provenance_path`，否则任务包可能不够精确。这个风险属于任务包创建纪律，不需要扩大模板结构。
