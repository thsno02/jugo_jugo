# KB 初始化状态

current_phase:: pre_loop_planning_gate_added
active_topic:: llm_wiki
main_language:: zh-CN
latest_run:: .llmwiki/runs/run_20260524_060000_preloop_planning
latest_archived_demo:: archive/demo_0_meta_kb_initialization_20260524
last_updated:: 2026-05-24T06:08:00+08:00

## 当前决策

上一轮 meta KB 已作为 demo-0 存档。Active workspace 已切换为真正的 LLM Wiki topic KB。

`loop_plan_init_kb.md` 只作为生产协议；`data/` 和 `reports/` 中的 source/evidence artifacts 是主题 KB 的主要输入。

## 当前决策

Turing planner sub-agent 已完成 evidence handoff，但按 `KB_INIT_KNOWLEDGE_MINING_PROTOCOL.md` 和 `llmwiki-loop-orchestration` gate，它不能直接授权 generator 写 card。

启动自治生成 loop 前，必须先执行 source mining，并把 candidate 写入 `.llmwiki/control/knowledge_frontier.yaml` 后标记为 `ready_to_build`。

## 下一步

启动第一轮 source mining：origin/canon source batch。

默认 source scope：

- `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt`
- `data/raw/webpage/karpathy-x-launch-post/raw.txt`
- `data/raw/hacker_news/hacker-news-original-thread/text.txt`
- `reports/source_gap_review.md`
- `data/manifests/claims.jsonl`
- `data/manifests/claim_source_links.jsonl`

## Planner 原则

`topic_plan.md` 是 guideline，不是执行计划。Planner sub-agent 必须从 `knowledge_frontier.yaml` 选择 `ready_to_build` candidate，才能生成 task scope。

## 检索策略

优先使用本地 `data/`。公司电脑网络受限时，只做有限普通检索；blocked/intercepted sources 记录后延期到个人设备重试。
