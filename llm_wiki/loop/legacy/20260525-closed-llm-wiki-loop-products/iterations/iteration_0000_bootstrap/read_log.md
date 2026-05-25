# 第 0 轮读取记录

## 允许输入内读取

- `llm_wiki/README.md`：确认当前目标、语言约定、非目标和技能列表。
- `data/manifests/acquired_sources_index.md`：确认本地来源池存在。
- `data/manifests/sources.jsonl`：确认来源 manifest 存在。
- `agent-loop-runner` 技能说明：确认循环控制面、任务包、状态、报告和执行者隔离要求。

## 允许输入外读取

- `find llm_wiki -maxdepth 3 -type f`：确认当前 `llm_wiki/` 尚无 loop 目录。
- `find . -path ./.git -prune -o -maxdepth 3 -type d`：确认仓库存在 `data/`、`legacy/`、`llm_wiki/` 等目录。
- `find scripts -maxdepth 2 -type f`：确认历史脚本存在，但本轮没有修改或依赖脚本。

这些读取用于建立文件管理边界，没有进入事实挖掘。
