# Pre-Loop Plan: Autonomous LLM Wiki KB Mining

run_id:: run_20260524_060000_preloop_planning
created_at:: 2026-05-24T06:00:00+08:00
status:: pre_loop_planning_gate_added
main_language:: zh-CN

## 为什么先做这个 run

人类会离开电脑，后续 loop 需要 Codex agent 自治推进。因此启动生成 loop 之前，必须先把可恢复状态、skill 调用顺序、frontier、停止条件和第一轮 source mining 范围落盘。

## 已调用的上层 skills

- `agent-loop-runner`：定义 loop 为 filesystem-backed state machine。
- `skill-creator`：初始化 repo-local skill scaffold，并将 protocol roles 拆成可迭代 skill。

## 已初始化的 repo-local skills

- `llmwiki-source-mining`
- `llmwiki-frontier-management`
- `llmwiki-node-planning`
- `llmwiki-card-generation`
- `llmwiki-citation-formatting`
- `llmwiki-provenance-generation`
- `llmwiki-change-generation`
- `llmwiki-node-metadata`
- `llmwiki-citation-audit`
- `llmwiki-adoption-audit`
- `llmwiki-dynamic-retrieval`
- `llmwiki-view-building`
- `llmwiki-impact-analysis`
- `llmwiki-skill-evolution`

## Planner Output 的处理

Turing 的 planner output 确认了第一候选是 `llm_wiki_origin_and_canon`，但它不再被视为直接 generator packet。按 protocol，它被降级为 evidence handoff。下一步必须先执行 Source Mining Loop：

1. 写 `source_scope.md`。
2. 写 `source_mining.md`。
3. 写 `candidate_frontier_delta.yaml`。
4. 更新 `knowledge_frontier.yaml`。
5. 只有候选进入 `ready_to_build` 后，才由 Node Planner 生成可执行 build packet。

## 第一轮自治动作

next_action:: source_mining_origin_and_canon_batch

Source batch:

- `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt`
- `data/raw/webpage/karpathy-x-launch-post/text.txt`
- `data/raw/webpage/karpathy-x-launch-post/raw.txt`
- `data/raw/hacker_news/hacker-news-original-thread/item.json`
- `data/raw/hacker_news/hacker-news-original-thread/text.txt`

Expected outputs:

- `.llmwiki/runs/<next_run>/source_scope.md`
- `.llmwiki/runs/<next_run>/source_mining.md`
- `.llmwiki/runs/<next_run>/candidate_frontier_delta.yaml`
- `.llmwiki/runs/<next_run>/evidence_gaps.md`
- `.llmwiki/runs/<next_run>/retrieval_requests.md`
- `.llmwiki/runs/<next_run>/mining_trace.md`

## 不启动卡片生成的理由

当前已经有 planner evidence handoff，但缺少 protocol 要求的 mining artifacts。直接生成 card 会重新落入“topic plan 当执行计划”的偏差。自治 loop 应从 mining 开始，而不是从 card writing 开始。

## Independent audit integration

Newton audit found the missing hard orchestration/planner gate. This run now includes `llmwiki-loop-orchestration` and `.llmwiki/control/orchestration_gates.yaml`.

Current decision: do not start card generation. Next loop action remains `source_mining_origin_and_canon_batch`.
