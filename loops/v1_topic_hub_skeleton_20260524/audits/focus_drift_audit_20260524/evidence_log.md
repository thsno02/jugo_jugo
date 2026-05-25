# 证据记录

`status`: `LOOP_DONE`

## 当前与归档框架

旧版 v1 已归档到 `legacy/v1_topic_hub_skeleton_20260524/`。该目录本身就是证据对象：它包含运行时目录、协议、控制面、运行记录、技能、节点、KB 视图和生成视图。当前活跃目录已转向 `llm_wiki/`，其中 README 明确下一版应以原子事实知识卡和出处论证为核心。

## 协议证据

`legacy/v1_topic_hub_skeleton_20260524/protocol/KB_INIT_KNOWLEDGE_MINING_PROTOCOL.md` 把生产对象定义为 `nodes/<new_node_id>/versions/1.0/{node.yaml, card.md, provenance.md, change.md}`。这意味着循环的最小正式产物不是原子事实知识卡，而是节点版本束。

`loop_plan_init_kb.md` 和 `loop_plan_data_collection.md` 也以主题计划、覆盖框架和节点生产为主线。它们没有提供“一个事实候选 -> 一个可读知识卡 -> 一个出处论证”的强制路径。

## 控制面证据

`llm_wiki_runtime/control/topic_plan.md` 与 `topic_node_backlog.yaml` 明确推动主题骨架。`knowledge_frontier.yaml` 和 `source_candidates.yaml` 记录的是主题/节点候选的成熟度，而不是原子事实候选的可靠性。

`orchestration_gates.yaml` 和 `autonomous_loop_plan.md` 主要检查执行者分工、版本束完整性、引用、采纳、视图构建和技能评估。它们能保证“一个节点版本束是否可以发布”，但不能保证“一个原子事实是否被证据做实”。

## 运行记录 / 任务包证据

`run_20260524_062000_worker_source_mining_origin_canon/source_mining.md` 显示早期来源挖掘其实有自下而上的成分：它分开记录了观察事实、解释、讨论笔记和缺口。

漂移发生在来源挖掘之后。后续节点规划任务包把这些观察压缩成主题节点：

- `run_20260524_063000_worker_node_planning_origin_canon/next_task_packet.md`
- `run_20260524_063500_worker_node_planning_repair_origin_canon/next_task_packet.md`
- `run_20260524_095000_worker_node_planning_vs_rag_write_loop/next_task_packet.md`
- `run_20260524_105000_worker_node_planning_risks_governance_provenance/next_task_packet.md`
- `run_20260524_123000_worker_node_planning_implementation_ecosystem/next_task_packet.md`
- `run_20260524_133000_worker_node_planning_evaluation_evidence/next_task_packet.md`

这些任务包的目标不是“抽取一个原子事实并证明它”，而是“生成一个有边界的主题节点”。

## 技能证据

`llmwiki-card-generation/SKILL.md`、`llmwiki-node-planning/SKILL.md`、`node_bundle_generation/skill.md` 等旧技能围绕节点版本束、知识卡/出处论证/变更记录组合、引用审计和采纳视图展开。它们提供了很多工程纪律，但对象层仍是节点。

`llmwiki-loop-orchestration/SKILL.md` 强调主控/执行者边界，这本身是合理的；问题在于它保护的是“错误对象”的执行流程。

## 输出知识卡证据

旧版产出的知识卡不是 zet 风格原子事实知识卡，而是面向主题的综合文档。例如：

- origin/canon 知识卡包含定义、结构、操作、讨论、风险词汇和边界。
- implementation ecosystem 知识卡包含生态族群、实现界面、元数据和缺口。
- evaluation/evidence 知识卡包含评估维度、证据层级、相邻指标和缺口。

这些内容不是无价值；它们可以作为未来枢纽页或主题笔记的材料。但它们不是当前目标需要的原子事实知识卡。

## 读取边界说明

本审计尽量从一手任务、任务包、控制面、技能和知识卡文件取证。旧版报告性文件作为历史归档保留，不作为本次根因判断的主要来源。

