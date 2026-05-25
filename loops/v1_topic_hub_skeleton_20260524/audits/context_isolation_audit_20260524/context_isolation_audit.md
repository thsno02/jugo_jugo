# 上下文隔离审计

`status`: `LOOP_DONE`
`decision`: `context_isolation_issues_found`

## 证据边界

本审计只使用文件系统中可见的一手执行者交接物、控制面状态、action queue、standing status 和必要 trace。它没有读取已有的结论型审计报告，因此结论来自任务、状态和交付记录，而不是复述上一个报告。

被排除的文件类型包括 `audit_report.md`、`skill_eval_report.md`、`process_findings.md`、`final_delivery_report.md`、`goal_satisfaction_audit.md`、`kb_initialization_demo_report.md`、`final_qa_report.md`。若这些文件名出现在允许读取的任务或交付文件中，只按路径字符串处理，不打开正文。

## 总体判断

旧版循环有真实的上下文隔离问题，但也有后续修复痕迹。最重要的问题不是不可恢复的数据损坏，而是角色边界不够可靠：

- 主控 agent 曾直接执行具体来源挖掘，并被记录为 `controller_drift_main_agent_executed_concrete_artifacts`。
- 审计执行者曾运行会写入 `generated/` 的引用解析脚本，超出了只读审计边界。
- 一些任务包依赖“当前线程里的用户/控制器指令”，无法完全从磁盘复现。
- 一些任务包在执行者读取证据前就给出了过强的叙事框架，使执行者容易执行控制器结论，而不是独立判断事实。

## 主 Agent 边界

`run_20260524_061000_source_mining_origin_canon/loop_status.md` 明确记录 `LOOP_BLOCKED`，阻塞原因为 `controller_drift_main_agent_executed_concrete_artifacts`。这不是文档措辞问题，而是实际的角色边界失败：来源挖掘在 `orchestration_gates.yaml` 中属于主控 agent 不应直接执行的具体工作。

后续控制面保留了这个样本、阻止直接采纳，并派发 `run_20260524_062000_worker_source_mining_origin_canon` 重新由执行者完成。这说明循环有恢复意识，但不能抵消最初的边界失败。

## 任务包泄漏风险

部分执行者任务包不只是给出输入、输出和成功条件，而是提前写入控制器的综合判断。例如：

- `run_20260524_094000_worker_source_mining_vs_rag_write_loop/next_task_packet.md` 已经把答案框在 LLM Wiki artifact 与 RAG/GraphRAG/agent memory 机制的差异中。
- `run_20260524_104000_worker_source_mining_risks_governance_provenance/next_task_packet.md` 预先给出规划目标、建议节点 ID、证据类别和生成风险。
- `run_20260524_131000_worker_skill_eval_implementation_ecosystem/next_task_packet.md` 给执行者大范围本地数据和旧 KB anchor，同时已经列出目标评估维度。

这些任务包仍保留了 `needs_retrieval`、`defer`、`blocked` 等选项，所以不是完全失控；但它们把控制器叙事带进了执行层，削弱了 sub-agent 的独立判断。

## 执行者输出边界

生成执行者通常遵守“只写版本束与本次运行 trace”的边界。例如 implementation ecosystem 的生成交付记录只写 `nodes/.../versions/1.0/*` 和本次运行 trace，没有写 root node、`kb/` 或 `generated/`。

采纳/视图执行者本来就被授权更新 root node metadata、KB view、生成图/状态和控制面状态；这类写入在角色上是合理的。

薄弱点在审计执行者。`run_20260524_101000_worker_audit_vs_rag_write_loop/validation_trace.md` 记录曾运行 `kb_parse_citations.py`，它写入 `generated/citation_graph.yaml` 和 `generated/backlinks.yaml`。后续 trace 又显示类似脚本被短暂运行或检查。对 audit-only 任务包来说，这属于越权写入。

## 特殊事件

### 审计执行者写入 Generated

已确认。这一问题出现在 `run_20260524_101000_worker_audit_vs_rag_write_loop/validation_trace.md`，并在 implementation ecosystem 的采纳/视图与技能评估交付中再次被记录。后续采纳/视图刷新 generated 文件作为权威状态是合理恢复，但不能改变审计执行者曾越权写入的事实。

### 替换执行者静默卡住风险

已确认但已有后续修复。`run_20260524_131000_worker_skill_eval_implementation_ecosystem/task.md` 把 replacement audit startup failure / silent initialized risk 纳入范围，并要求未来执行者在长任务前先写 `task.md` 和初始 `loop_status.md`，无进展则写 `LOOP_BLOCKED`。后续 evaluation evidence 的来源挖掘任务已体现这个启动门。

### 主 Agent 状态检查

主控 agent 读取执行者 summary/status/gate/delivery 并更新控制面状态，本身不是违规。边界问题只在主控 agent 借状态检查去执行来源挖掘、规划、生成、审计、视图构建、技能评估等具体工作时发生。可见的硬失败是早期主控 agent 写出的来源挖掘运行。

## 结论

旧版循环的上下文隔离没有通过。它有恢复机制，但还不够强：执行权、证据权、结论权和写入权没有被清晰拆开。下一版原子事实循环必须让每个执行者的任务、允许输入、允许写入和成功条件都能从磁盘独立复现。

