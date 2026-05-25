# 第 0 轮任务：建立循环控制面

- `task_id`: `task_20260525_0000_loop_bootstrap`
- `iteration_id`: `iteration_0000_bootstrap`
- `role`: `main_agent`
- `main_language`: 中文

## 目标

建立 `llm_wiki/loop/` 作为可恢复的循环控制面，并明确 sub-agent / 执行者的行为和 scope。

## 允许输入

- `llm_wiki/README.md`
- `llm_wiki/skills/`
- `data/manifests/acquired_sources_index.md`
- `data/manifests/sources.jsonl`
- `agent-loop-runner` 技能说明

## 允许写入

- `llm_wiki/README.md`
- `llm_wiki/kb/README.md`
- `llm_wiki/loop/`

## 成功门禁

- 存在专门的 `llm_wiki/loop/` 目录。
- 循环状态、清单、运行手册、任务模板、报告和决策记录都落在磁盘。
- 执行者行为边界写入 `SUBAGENT_SCOPE.md`。
- 知识库产物面与循环控制面分开。
- 新写人类可读文档主语言为中文。

## 非目标

- 不挖掘事实候选。
- 不写知识卡。
- 不采纳知识卡。
- 不启动枢纽页、聚类或主题覆盖。
