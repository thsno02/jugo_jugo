# Run Plan / 纠偏计划

run_id:: run_20260524_053000_topic_replan
run_type:: topic_replan
main_language:: zh-CN

## 目标

把 active KB 从“KB 生产机制自身”纠偏为真正的 LLM Wiki topic KB。

## 操作

1. 将 demo-0 meta KB 存档到 `archive/demo_0_meta_kb_initialization_20260524/`。
2. 清空并重建 active `nodes/`、`kb/`、`generated/`。
3. 写入 `.llmwiki/control/topic_plan.md` 和 `.llmwiki/control/topic_node_backlog.yaml`。
4. 明确 `data/` 是 primary evidence layer。
5. 重建空的 active `kb/_index.yaml`、`generated/status.yaml`、citation graph 和 impact queue。

## 下一步

生成第一个真正 topic node：`llm_wiki_origin_and_canon`。
