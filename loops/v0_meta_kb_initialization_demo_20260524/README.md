# Demo 0 归档：KB 生产机制自身的初始化 KB

archived_at:: 2026-05-24T05:30:00+08:00
archive_reason:: 该 demo 把 `loop_plan_init_kb.md` 中的生产机制误当成 topic KB 内容，但它仍可作为第一个机制验证 demo 供后续审计。

## 说明

这个归档保存的是上一轮产物：一个关于“如何生产 KB”的 meta KB。它不是最终要建设的 LLM Wiki topic KB，但可以作为 demo-0 来审计：

- 文件契约是否能跑通。
- version bundle 是否完整。
- provenance / citation / impact queue 是否可解析。
- dynamic retrieval 记录是否完整。
- 中文主内容重写是否可验证。

## 保存内容

- `nodes/`：demo-0 的 node database 快照。
- `kb/`：demo-0 的 adopted view 快照。
- `generated/`：demo-0 的 citation graph、backlinks、impact queue、status 快照。
- `.llmwiki_snapshot/`：demo-0 的 control、runs、skills 快照。
- `kb_initialization_demo_report.md`：demo-0 报告。
- `active_nodes_before_topic_reset/`、`active_kb_before_topic_reset/`、`active_generated_before_topic_reset/`：从 active workspace 移入 archive 的目录。

## 当前活跃方向

该说明是归档当时写下的状态。后来 topic KB 又被降级为 `legacy/v1_topic_hub_skeleton_20260524/`，因为它仍然是 top-down hub skeleton，不是 bottom-up atomic fact KB。

当前活跃方向是 `llm_wiki/` 下的 atomic fact production。
