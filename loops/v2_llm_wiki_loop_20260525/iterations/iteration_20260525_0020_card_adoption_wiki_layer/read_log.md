# read_log

## 任务允许输入

| 路径 | 原因 | 用途 |
| --- | --- | --- |
| `llm_wiki/loop/iterations/iteration_20260525_0020_card_adoption_wiki_layer/task.md` | 当前任务包 | 确认采纳对象、允许输入、允许写入和成功门禁 |
| `llm_wiki/loop/iterations/iteration_20260525_0018_card_drafting_wiki_layer/artifacts/draft_card.md` | 任务允许的草稿知识卡 | 生成采纳后的知识卡，保持轻量整理并将 `status` 改为 `accepted` |
| `llm_wiki/loop/iterations/iteration_20260525_0018_card_drafting_wiki_layer/artifacts/provenance.md` | 任务允许的出处论证 | 生成采纳后的出处论证并与知识卡互链 |
| `llm_wiki/loop/iterations/iteration_20260525_0019_card_audit_wiki_layer/artifacts/audit_report.md` | 任务允许的审计报告 | 确认 `audit_result: pass` 和无必改项 |
| `llm_wiki/kb/cards/llm-wiki-wiki-layer-generated-markdown-directory.md` | 任务允许的目标卡路径 | 采纳前用于存在性和覆盖冲突检查，采纳后用于门禁验证 |
| `llm_wiki/kb/provenance/llm-wiki-wiki-layer-generated-markdown-directory.md` | 任务允许的目标出处路径 | 采纳前用于存在性和覆盖冲突检查，采纳后用于门禁验证 |
| `llm_wiki/kb/indexes/cards.md` | 任务允许的目标索引路径 | 保留既有最小索引并追加采纳卡片行 |

## 任务外读取

| 路径 | 原因 | 用途 |
| --- | --- | --- |
| `~/.codex/skills/agent-loop-runner/SKILL.md` | 系统级技能指令要求在循环任务中使用该技能 | 仅用于遵守循环文件纪律；未作为知识事实来源 |
| `llm_wiki/loop/iterations/iteration_20260525_0020_card_adoption_wiki_layer/loop_status.md` | 启动时确认状态文件是否已存在 | 避免误用 `Add File` 覆盖既有输出 |
| `llm_wiki/loop/iterations/iteration_20260525_0020_card_adoption_wiki_layer/read_log.md` | 启动时确认读取日志是否已存在 | 避免误用 `Add File` 覆盖既有输出 |

## 未读取

- 未读取 `legacy/`。
- 未读取旧审计报告、父 agent 总结或其它执行者产物。
- 未使用父聊天上下文作为事实来源。
