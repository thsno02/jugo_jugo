# KB 初始化 Demo 报告

generated_at:: 2026-05-24T05:10:00+08:00
status:: complete_for_demo_scope
language:: zh-CN

## 摘要

KB initialization demo 已经形成一个 filesystem-backed、可审计、可恢复的 loop。当前产物包括 contracts、control files、scripts、skill seeds、data inventory、adopted nodes、generated views、动态检索记录，以及 major-change impact queue。

来自 `generated/status.yaml` 的当前计数：

- adopted_nodes: 7
- kb_view_cards: 7
- citation_edges: 35
- dynamic_retrieval ok_attempts: 1
- dynamic_retrieval failed_attempts: 1
- major_candidates: 1
- impact_queue_open: 4

## Artifact Map

Contracts 与 control：

- `kb/_schema.yaml`
- `.llmwiki/control/principles.md`
- `.llmwiki/control/state.md`
- `.llmwiki/control/autonomy.md`
- `.llmwiki/control/reflection_policy.md`
- `.llmwiki/control/summary_state.md`
- `.llmwiki/control/standing_status.md`
- `.llmwiki/control/decision_log.yaml`
- `.llmwiki/control/data_inventory.yaml`
- `.llmwiki/control/source_candidates.yaml`

Scripts：

- `scripts/kb_common.py`
- `scripts/kb_bootstrap_demo.py`
- `scripts/kb_build_index.py`
- `scripts/kb_build_view.py`
- `scripts/kb_validate_node.py`
- `scripts/kb_validate_card.py`
- `scripts/kb_parse_citations.py`
- `scripts/kb_compute_impact.py`
- `scripts/kb_status.py`
- `scripts/kb_git_checkpoint.sh`

Views 与 generated artifacts：

- `kb/_index.yaml`
- `kb/*.md`
- `generated/citation_graph.yaml`
- `generated/backlinks.yaml`
- `generated/impact_queue.yaml`
- `generated/status.yaml`

Run artifacts：

- `.llmwiki/runs/run_20260524_050031_kb_initialization_bootstrap/`
- `.llmwiki/runs/run_20260524_050318_dynamic_retrieval_enterprise_scale/`
- `.llmwiki/runs/run_20260524_050634_major_impact_simulation/`

## Adopted Nodes

- `20260524_050031_llm_wiki_working_definition`
- `20260524_050032_current_kb_initialization_loop`
- `20260524_050033_source_preservation_precondition_trust`
- `20260524_050034_provenance_as_core_knowledge_asset`
- `20260524_050035_citation_driven_impact_propagation`
- `20260524_050036_dynamic_retrieval_as_controlled_fallback`
- `20260524_050318_enterprise_scale_requires_governed_context_layer`

每个 adopted node 都有 root `node.yaml`、`versions/1.0/node.yaml`、`card.md`、`provenance.md`、`change.md`，并渲染为 `kb/<node_id>.md`。

## 动态检索

Bootstrap run 记录了 enterprise/community evidence gap。动态检索 run 保存了两个尝试：

- 失败但保存：`data/raw/webpage/aicritique-enterprise-knowledge-dynamic-20260524/`
- 成功并使用：`data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/`

成功来源被 adopted node `20260524_050318_enterprise_scale_requires_governed_context_layer` 使用。失败来源保留为非 evidence retrieval attempt。

当前运行在公司电脑上，网络拦截是预期限制。策略是有限正常尝试；blocked sources 记录并延期到个人设备重新 retrieve。

## Major Impact Test

Demo 包含一个未 adopted 的 2.0 candidate：

- `nodes/20260524_050033_source_preservation_precondition_trust/versions/2.0/`

其 `change.md` 标记：

- `change_scale:: major`
- `propagation_required:: true`

`generated/impact_queue.yaml` 包含 4 个 open impact entries，均来自 parsed citation edges。Candidate 没有进入 `kb/`，`kb/` 仍只渲染 adopted 1.0。

## 验证

已运行：

- `python3 -m py_compile ...`
- `python3 scripts/kb_validate_node.py --all`
- `python3 scripts/kb_validate_card.py --all`
- `python3 scripts/kb_parse_citations.py`
- `python3 scripts/kb_compute_impact.py`
- `python3 scripts/kb_status.py`

最新结果：

- node validation passed: 7 nodes
- card validation passed: 15 cards
- citation graph edges: 35
- impact queue open: 4

## 残余风险

- Citation validation 仍偏结构性：它检查 required fields 和路径存在，但只做了轻量 semantic faithfulness audit。
- Atlan 是 vendor-authored source，适合 enterprise framing，不适合作为独立 empirical validation。
- 公司网络可能拦截网页，blocked sources 应在个人设备重新 retrieve，而不是在公司网络中绕行。
- Candidate-version validation 仍是间接的：candidate card 可验证，impact computation 会读取 candidate `change.md`，但 `kb_validate_node.py` 主要检查 adopted root metadata。

## 下一步建议

- 增加 candidate-version validator mode。
- 增加 semantic citation-audit sampling。
- Review 4 个 impact queue entries，不自动重写下游 nodes。
