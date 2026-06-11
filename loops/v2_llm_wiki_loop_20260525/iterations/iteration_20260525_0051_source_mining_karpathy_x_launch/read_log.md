# read_log

| path | reason | use |
| --- | --- | --- |
| `~/.codex/skills/agent-loop-runner/SKILL.md` | 当前任务属于 filesystem-backed loop 执行，开发者指令要求使用匹配技能 | 仅用于执行流程约束；不作为事实来源 |
| `llm_wiki/loop/iterations/iteration_20260525_0051_source_mining_karpathy_x_launch/task.md` | 当前任务包 | 确认允许输入、允许写入、输出要求和成功门禁 |
| `data/manifests/sources.jsonl` | 任务包允许的 `source_manifest` | 确认 `karpathy-x-launch-post` 的本地目录、URL 和状态 |
| `data/raw/webpage/karpathy-x-launch-post` | 任务包指定的 `source_path` | 列出本地来源文件并确认存在 |
| `data/raw/webpage/karpathy-x-launch-post/metadata.json` | 指定来源目录内文件 | 确认抓取状态、URL、HTTP 状态和来源元数据 |
| `data/raw/webpage/karpathy-x-launch-post/raw.json` | 指定来源目录内文件 | 抽取事实候选的主要证据来源 |
| `data/raw/webpage/karpathy-x-launch-post/text.txt` | 指定来源目录内文件 | 确认文本镜像可读；内容为单行 JSON |
| `data/raw/webpage/karpathy-x-launch-post/raw.txt` | 指定来源目录内文件 | 仅用于行数检查；未作为事实证据 |
| `llm_wiki/loop/iterations/iteration_20260525_0051_source_mining_karpathy_x_launch/dispatch_request.json` | 递归 `rg` 验证交付标记时被意外扫到 | 未作为任务来源或事实来源；仅记录该次额外读取 |
