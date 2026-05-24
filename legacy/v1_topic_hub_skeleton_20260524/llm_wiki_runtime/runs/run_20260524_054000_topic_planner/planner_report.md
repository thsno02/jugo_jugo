# LLM Wiki Topic Planner Report

run_id: run_20260524_054000_topic_planner  
role: Planner sub-agent  
main_language: zh-CN  
status: ready_for_generator  

## 角色边界

本轮 planner 只做只读证据检查和 generator handoff 设计，不生成 KB node，不 adopt node，不修改 `nodes/`、`kb/`、`generated/` 或任何无关文件。

当前 object-level topic 是 **LLM Wiki**。这里的 KB 应该解释 LLM Wiki 作为一种知识系统、工作流和生态现象，而不是解释“如何生产这个 KB”的机制。`.llmwiki/control/topic_plan.md` 和 `.llmwiki/control/topic_node_backlog.yaml` 只是方向性指南；真正的执行单元必须来自本地 `data/` corpus 的证据闭环。

## 已检查输入

只读检查范围：

- `data/raw/`
- `data/manifests/sources.jsonl`
- `data/manifests/source_digests.jsonl`
- `data/manifests/claims.jsonl`
- `data/manifests/claim_source_links.jsonl`
- `data/manifests/coverage_records.jsonl`
- `data/manifests/acquired_sources_index.md`
- `data/manifests/source_digests_index.md`
- `reports/source_gap_review.md`
- `reports/coverage_framework.md`
- `.llmwiki/control/topic_plan.md`
- `.llmwiki/control/topic_node_backlog.yaml`

证据状态摘要：

- `sources.jsonl` 和 source index 显示本地已有 Karpathy gist、X mirror、HN 原帖、HN mirror、secondary explainers、GitHub repos、PyPI packages、arXiv papers、governance/evaluation/comparison sources。
- `claims.jsonl` 中 `claim_000001` 到 `claim_000008` 已把 `origin_and_canon` 的关键输出标为 `source_linked`、`confidence: high`、`evidence_grade: A`。
- `coverage_records.jsonl` 中 `covrec_origin_and_canon_*` 显示 origin/canon 的 8 个 required outputs 都是 `supported`。
- `source_gap_review.md` 判断 origin/definition coverage 为 strong，但提醒“pre-Karpathy historical precedence”仍不充分。
- `coverage_framework.md` 定义了 LLM Wiki 的边界：persistent source-backed artifacts、LLM/agent-mediated compilation、provenance/auditability、maintenance over time。

## 首个 Node 选择

确认首个 generator node 为：

`llm_wiki_origin_and_canon`

选择理由：

1. 它是后续 definition、architecture、workflow、comparison nodes 的前置锚点；如果 canonical origin 没有固定，后续节点容易把二级解读误当成原始定义。
2. 本地 evidence 最强，且无需 web retrieval：Karpathy gist、X mirror、HN item/thread、manifest claims 和 coverage records 足以支持第一版 node。
3. scope 可控：可以先回答“谁提出了什么、何时传播、原始文本中哪些主张构成 canonical pattern、早期讨论有哪些分歧”，不需要立即展开整个生态或企业适用性。
4. 它能直接纠正上一轮 meta/object 混淆：node 内容必须围绕 LLM Wiki topic 本身，而不是围绕 KB 初始化流程。

未选择其他候选的原因：

- `llm_wiki_working_definition` 更适合作为第二个 node，因为它应引用 origin/canon 已固定的原始概念，再结合 coverage framework 做抽象定义。
- `llm_wiki_implementation_ecosystem` 虽然证据丰富，但 raw repos 面很宽，第一步就做会把规划面扩大过快。
- `llm_wiki_vs_rag_and_adjacent_systems` 需要更多 comparison baselines，适合在 origin 和 working definition 后生成。

## Evidence Scope 摘要

Primary evidence 应限于直接原始材料：

- `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt`
- `data/raw/webpage/karpathy-x-launch-post/text.txt`
- `data/raw/webpage/karpathy-x-launch-post/raw.txt`
- `data/raw/hacker_news/hacker-news-original-thread/item.json`
- `data/raw/hacker_news/hacker-news-original-thread/text.txt`

Secondary/navigation evidence 用于定位、校验和解释覆盖状态：

- `data/manifests/sources.jsonl`
- `data/manifests/source_digests.jsonl`
- `data/manifests/claims.jsonl`
- `data/manifests/claim_source_links.jsonl`
- `data/manifests/coverage_records.jsonl`
- `data/manifests/acquired_sources_index.md`
- `data/manifests/source_digests_index.md`
- `reports/source_gap_review.md`
- `reports/coverage_framework.md`

可选 secondary raw evidence 只在 generator 需要校验早期二级传播语境时使用：

- `data/raw/webpage/hacker-news-lens-thread/text.txt`
- `data/raw/webpage/marvin-hn-persistent-knowledge/text.txt`

## Retrieval 决策

本轮不做 web retrieval。公司电脑网络受限，且首个 node 已有足够本地证据。任何 Reddit、AICritique、X live page 或其他动态网页缺口，只能写入未来 retrieval request，不允许突破网络环境。

## Generator Handoff

generator 的下一步不是“继续改 plan”，而是按 `next_task_packet.md` 生成 `llm_wiki_origin_and_canon` 的 candidate version bundle，并按 `evidence_scope.yaml` 限定输入范围。

Planner 对 generator 的核心要求：

- 中文为主，英文术语可保留。
- 所有 substantive claims 必须落到 source id、raw path、claim id 或 coverage record。
- 明确区分 observed facts、interpretations、early discourse/skepticism、unknowns。
- 不要把 `.llmwiki/control/*`、`loop_plan_init_kb.md` 或 KB 生产机制写成 object-level topic 内容。
- 不要做 web retrieval；如发现证据不足，只记录 retrieval request。

## 下一步建议

1. generator 执行 `next_task_packet.md`，产出 `llm_wiki_origin_and_canon` candidate bundle。
2. independent evaluator/auditor 检查 citation/provenance/source sufficiency gates。
3. 审计通过后再 adopt 到 active KB view。
4. 第二个 planner run 再决定是否生成 `llm_wiki_working_definition`，不要直接从 backlog 顺延。
