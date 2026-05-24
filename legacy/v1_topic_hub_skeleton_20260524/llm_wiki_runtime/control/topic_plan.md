# LLM Wiki Topic KB Guidelines

updated_at:: 2026-05-24T06:08:00+08:00
main_language:: zh-CN
active_topic:: llm_wiki
status:: guideline_not_execution_plan_frontier_gated

## 定位

本文件只是 topic KB 的方向性 guidelines，不是可直接执行的 node generation plan。

真正的执行计划必须先经过 Source Mining Loop 和 Candidate Frontier Loop。Planner 每轮只能从 `.llmwiki/control/knowledge_frontier.yaml` 中选择 `ready_to_build` candidate，再输出 generator handoff。Planner 不能仅凭本文件、backlog 或默认候选直接授权 generator。

## 纠偏说明

上一轮 demo 把 `loop_plan_init_kb.md` 当成了 KB 内容主题，导致生成了关于“KB 生产机制”的 meta KB。正确方向应该是：把 `loop_plan_init_kb.md` 当作生产协议，把 `data/`、`data/manifests/`、`reports/coverage_framework.md`、`reports/source_gap_review.md` 当作 LLM Wiki topic KB 的主要 evidence layer。

## 核心目标

生成一个关于 LLM Wiki 这个 topic 的 agent-maintained KB。它应覆盖：

- 起源与 canonical sources。
- Working definition。
- raw/wiki/schema 三层架构。
- ingest / compile / query / lint 工作流。
- 与 RAG、PKM、knowledge graph、agent memory、documentation systems 的关系。
- 现有 implementations / ecosystem。
- evaluation evidence 与 empirical claims。
- risks、governance、provenance、citation accuracy。
- scale boundaries 与 enterprise applicability。

## Primary Evidence Inputs

必须优先使用本地已采集 data：

- `data/raw/`
- `data/manifests/sources.jsonl`
- `data/manifests/source_digests.jsonl`
- `data/manifests/claims.jsonl`
- `data/manifests/claim_source_links.jsonl`
- `data/manifests/coverage_records.jsonl`
- `data/manifests/source_digests_index.md`
- `reports/coverage_framework.md`
- `reports/source_gap_review.md`
- `reports/evidence_matrix.md`
- `reports/judgment_status.md`

动态检索只作为 fallback：当本地 evidence 不足、source 被拦截、或 topic node 需要新 evidence 时，先写 retrieval request，再保存 raw source。公司电脑网络受限时，只做有限尝试，失败即记录并延期到个人设备重试。

## Suggested Topic Areas

以下只是建议 topic areas，不是固定执行顺序。Planner sub-agent 可以合并、拆分、跳过或重新排序：

1. `llm_wiki_origin_and_canon`
2. `llm_wiki_working_definition`
3. `llm_wiki_three_layer_architecture`
4. `llm_wiki_ingest_compile_query_lint_workflow`
5. `llm_wiki_vs_rag_and_adjacent_systems`
6. `llm_wiki_implementation_ecosystem`
7. `llm_wiki_evaluation_evidence`
8. `llm_wiki_risks_governance_and_provenance`
9. `llm_wiki_scale_boundaries_and_enterprise_limits`

## Planner-Driven Node Planning Rules

每个 topic node 必须先经过 source mining 和 frontier gate，再由 planner sub-agent 选择。Planner 需要给出：

1. 为什么此 node 是当前最高价值下一步。
2. 它服务哪个 coverage area / source gap / synthesis need。
3. 它的 precise evidence scope，包括 primary raw paths、secondary manifest/report paths、可用 claim ids/source ids。
4. generator 的 allowed inputs 和禁止事项。
5. audit gates：citation、provenance、source sufficiency、adoption readiness。

Generator 不能绕过 source mining、frontier、planner 和 generation-entry gate 直接从 suggested backlog 生成 adopted node。

## 当前 Planner Run

planner_run:: .llmwiki/runs/run_20260524_054000_topic_planner
planner_agent:: sub-agent
planner_status:: completed_as_evidence_handoff_not_generation_authority

Planner 已确认 `origin/canon` 是强候选，但该 run 早于 frontier gate，不是可直接执行的 generator packet。下一步必须先执行 source mining，并把 candidate 在 `knowledge_frontier.yaml` 中更新为 `ready_to_build`。

## 默认候选 evidence scope

- `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt`
- `data/raw/webpage/karpathy-x-launch-post/raw.txt`
- `data/raw/hacker_news/hacker-news-original-thread/text.txt`
- `reports/source_gap_review.md`
- `data/manifests/claims.jsonl`
- `data/manifests/claim_source_links.jsonl`
