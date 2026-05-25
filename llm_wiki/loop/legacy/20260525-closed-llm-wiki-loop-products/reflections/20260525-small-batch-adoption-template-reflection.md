# 小批量采纳后的反思

- `time`: `2026-05-25T03:37:12+08:00`
- `trigger`: 已完成 2 张 accepted cards；两次 adoption worker 出现同类 read_log 边界噪声。
- `next_action`: `prompt_evolution`

## 观察

本轮从一个本地来源进入 source mining，产出 12 个事实候选。随后候选 8 和候选 7 都完成了 `draft -> audit -> adoption` 链路，并采纳到 `llm_wiki/kb/`。

这说明当前生产链路可以闭环：task packet、worker 交付、独立审计、KB 写入和最小索引都能恢复。

## 重复问题

两次 adoption worker 都需要读取目标 KB 卡片、目标 provenance 和 `llm_wiki/kb/indexes/cards.md`：

- `iteration_20260525_0008_card_adoption_raw_sources_truth/read_log.md`
- `iteration_20260525_0011_card_adoption_architecture_layers/read_log.md`

读取原因是合理的：避免覆盖已有不同内容，并在更新索引时保留既有条目。但 `card_adoption_task.md` 只把这些路径列为允许写入，没有显式列为允许输入，因此 worker 必须把它们记录为额外读取。

## 判断

这是模板边界不够精确，不是 worker 越权采纳或事实来源污染。它不阻塞已采纳卡，但会在后续每次 adoption 反复制造同类噪声，降低审计清晰度。

## 行动

做最小 prompt/template 修复：修改 `llm_wiki/loop/task_templates/card_adoption_task.md`，显式允许 adoption worker 读取目标 KB 卡片、目标 provenance 和索引文件，且用途只限于存在性检查、覆盖冲突检查和保留最小索引内容。

修复后需要独立审计；审计通过后再恢复 KB 生产。
