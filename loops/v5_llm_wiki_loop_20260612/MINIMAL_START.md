# Minimal Start (copy-paste to new session)

```
cd /Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo

你是 v5 llm_wiki loop 执行者。先依序读以下文件获取完整上下文：

1. loops/v5_llm_wiki_loop_20260612/CLAUDE_CODE_HANDOFF.md（全貌 + 约束 + 管线改进）
2. loops/v5_llm_wiki_loop_20260612/task.md（Phase 0-5 任务清单）
3. loops/v5_llm_wiki_loop_20260612/LOOP_START_PROMPT.md（完整启动 prompt + 源目录 + 设计文档位置索引）
4. loops/v4_llm_wiki_loop_20260602/learnings/next_loop_prep.md（v5 可执行输入）

不可等待的关键约束：
- Loop 独立 0->1：不引用/比较 v4/v3 KB，只用本 loop 自己的卡片
- 中文主语言输出（schema key/path/code 保持英文）。输出形式「中文（英文）」
- 所有 Agent() 调用必须传 model: "opus"
- git commit 禁止 Co-Authored-By trailer

第一步行动：执行 Phase 0 -- Setup。读完上述 4 个文件后，继续读 v4 learnings 全部 7 份文档，然后实现 tools/source_router.py、tools/repo2doc.py、tools/yaml_lint.py，更新 skills，直到 Phase 0 完成条件全部满足。
```
