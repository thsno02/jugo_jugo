# 输入输出边界问题

`status`: `LOOP_DONE`
`decision`: `context_isolation_issues_found`

## P1：主 Agent 写出了具体来源挖掘产物

证据：

- `run_20260524_061000_source_mining_origin_canon/loop_status.md`
- `run_20260524_061000_source_mining_origin_canon/loop_delivery.md`
- `control/orchestration_gates.yaml`

该运行被阻塞的原因是主控 agent 执行了具体来源挖掘。它直接违反了控制面中 `main_agent.must_not_do` 的边界。后续处理是正确的：保留样本、标记为控制器漂移、阻止直接采纳，并要求执行者重新执行或独立复核。

## P1：审计角色运行了会写入的引用解析脚本

证据：

- `run_20260524_101000_worker_audit_vs_rag_write_loop/validation_trace.md`
- `run_20260524_111000_worker_audit_risks_governance_provenance/validation_trace.md`
- `run_20260524_130000_worker_adoption_view_implementation_ecosystem/loop_delivery.md`
- `run_20260524_131000_worker_skill_eval_implementation_ecosystem/loop_delivery.md`

审计执行者应该只读既有产物，并只写本次运行目录内的审计输出。`kb_parse_citations.py` 会写 `generated/citation_graph.yaml` 和 `generated/backlinks.yaml`，因此在 audit-only 角色中运行它属于越界。后续恢复删除或刷新 generated 文件是必要的，但不能抹掉边界问题。

## P2：部分执行者任务包不能完全从磁盘复现

证据：

- action queue 中存在 `task_packet:: user/controller instruction in current thread` 一类记录。
- 部分执行者任务依赖当前聊天上下文，而不是完整落盘的任务包。

如果权威任务不完整落盘，未来审计者无法从文件中还原执行者的完整输入、写入和成功条件。这会让 sub-agent 的行为依赖未归档的 parent-chat wording，形成上下文泄漏风险。

## P2：来源挖掘与最终 QA 的输入范围过宽

证据：

- `run_20260524_131000_worker_skill_eval_implementation_ecosystem/next_task_packet.md`
- `run_20260524_141000_worker_skill_eval_evaluation_evidence/next_task_packet.md`
- `run_20260524_132000_worker_source_mining_evaluation_evidence/task.md`

来源挖掘和最终 QA 有时确实需要宽读，但任务包应该把输入分成主证据、只用于边界的旧 KB、过程上下文、控制面元数据。旧版主要靠自然语言说明，机器边界不够清楚，执行者容易从旧 KB anchor 或状态摘要中带入控制器结论。

## P2：任务包结论提前塑形执行者输出

证据：

- `run_20260524_094000_worker_source_mining_vs_rag_write_loop/next_task_packet.md`
- `run_20260524_104000_worker_source_mining_risks_governance_provenance/next_task_packet.md`
- `run_20260524_133000_worker_node_planning_evaluation_evidence/next_task_packet.md`

这些任务包包含有用的风险控制，但也预先给出叙事边界、节点方向和预期综合方式。执行者仍可选择 `defer` 或 `blocked`，不过它已经被强烈导向“把控制器的框架做出来”，而不是从证据中抽取最小事实。

## P2：启动与静默无进展保护出现得太晚

证据：

- `run_20260524_131000_worker_skill_eval_implementation_ecosystem/loop_delivery.md`
- `run_20260524_132000_worker_source_mining_evaluation_evidence/task.md`
- `run_20260524_141000_worker_skill_eval_evaluation_evidence/next_task_packet.md`

后续确实增加了执行者启动门：先写 `task.md` 与初始 `loop_status.md`，长时间无进展要显式 `LOOP_BLOCKED`。问题在于这个规则是中后期补上的，不是循环初始契约的一部分。

## P3：写入目录冲突处理正确

证据：

- `run_20260524_120000_worker_skill_eval_risks_governance_provenance/next_task_packet.md`
- `run_20260524_122000_worker_source_mining_implementation_ecosystem/task.md`
- `run_20260524_122000_worker_source_mining_implementation_ecosystem/loop_delivery.md`

上游任务包建议 `121000` 运行目录，而直接指令允许 `122000`。执行者选择当前、更严格的写入边界并记录冲突，这是一个正向样例。

## P3：Footnote Layout 阻止采纳是正确边界行为

证据：

- `run_20260524_112000_worker_adoption_view_risks_governance_provenance/loop_delivery.md`
- `run_20260524_113000_worker_repair_footnote_layout_contract/loop_delivery.md`

采纳/视图执行者在脚注布局门禁失败时停止，没有写 root metadata 或 generated view。随后修复执行者获得明确权限再修知识卡和技能契约。这是合理的角色分离。

## 判断

主要风险不是已造成不可恢复污染，而是角色边界不稳定：主控 agent 曾直接执行具体工作，只读审计执行者曾运行会写入的脚本，一些任务包过宽或依赖聊天上下文。下一版必须把角色、读取集合、写入集合、成功门禁和阻塞条件都写成磁盘可审计契约。
