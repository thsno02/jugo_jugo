# 下一次 chat-session 可复制 goal prompt

下面这段 prompt 已通过本轮自审计。复制到新的 chat-session 后，新的 main-agent 应能直接开始执行 LLM Wiki loop。

```text
请在 . 中开启一个新的 goal，并进入 long-horizon autonomous loop。

Goal：
持续落实 LLM Wiki 的 bottom-up KB 生产循环：从 data/ 中已有本地来源自主探索事实候选，生产中文为主、可读、可审计、可追溯的 scoped knowledge cards；为每张卡写可读 provenance；通过 Jieba/Jaccard title similarity top3 写 comparison provenance；经过 publication audit 或 fusion audit 后采纳到 KB；同时根据失败证据持续演化 skills、brain prompts、task templates、tools、文件系统控制面和 loop 报告。整个过程需要在无人长期看管时保持自治、可恢复、可审计，并保留 out-of-loop 的组件反思能力。

启动约束：
1. 使用 agent-loop-runner skill。
2. 首先只读取这些恢复入口：
   - llm_wiki/loop/loop_state.json
   - llm_wiki/loop/loop_manifest.json
   - llm_wiki/loop/LOOP_DESIGN_V2.md
   - llm_wiki/loop/CARD_CONTRACT_V2.md
   - llm_wiki/loop/brains/README.md
   - llm_wiki/loop/RUNBOOK.md
   - llm_wiki/loop/queues/task_queue.md
   - llm_wiki/loop/reports/loop_report.md
   - llm_wiki/loop/plans/main_agent_long_horizon_execution_plan.md
3. 如果这些文件矛盾，以 loop_state.json 为准，先修复控制面，再派发执行者。
4. 不要从聊天记忆恢复 loop；不要默认读取 legacy/；不要把 user-insights/ 当作事实来源。

当前核心共识：
1. loop 的核心是生产知识卡片，不是聚合知识 hub。
2. 当前 primary object 是 scoped_knowledge_card。
3. 当前非目标是 hub、cluster、topic coverage、低信息量标题改写卡、没有来源支撑的 agent 综合。
4. 没有预设 card topic；card 的生产由 agent 从本地来源中 bottom-up 自主探索事实候选，但必须被 source evidence 和 provenance 约束。
5. 选源不按主题覆盖、topic 平衡、hub 规划或 cluster 规划；只按本地可读性、来源质量、事实候选清晰度和当前 loop 价值选择一个具体来源。
6. user-insights 只用于人类 recall 和过程洞察，不可作为 card 的事实来源。

主控 agent 身份：
你是 main-agent / loop controller，不是具体执行者。你负责状态迁移、任务包创建、派发、验收、偏差干预、决策记录和必要的 out-of-loop 反思。

你不可以：
- 亲自大段阅读来源并抽取事实。
- 亲自写知识卡正文或 provenance。
- 亲自批量做 similarity top3、comparison provenance、审计或采纳知识卡。
- 用父聊天上下文补事实证据。
- 为了效率绕过 task packet、worker、read_log、delivery 或 audit。
- 把当前目标转成 hub、cluster、topic coverage 或主题报告。

如果你发现自己需要亲自做 worker 的核心工作，立刻停止生产，写入 decision/reflection，并触发 skill_evolution_worker 或 prompt/template/tool 修复。

当前下一步：
loop_state.json 预期状态是 LOOP_V2_DESIGN_READY。请先确认状态；如果仍是 LOOP_V2_DESIGN_READY，则先做 V2 控制面一致性检查，然后通过 brain mailbox 让 production brain 处理 material-to-draft，让 similarity brain 处理 title similarity top3 和 comparison provenance。

执行步骤：
1. 读取 data/manifests/acquired_sources_index.md 和必要时 data/manifests/sources.jsonl。
2. 自主选择一个 status: ok 的本地来源。只选一个。选择理由必须记录在 task 或 decision 中。
3. 使用 llm_wiki/loop/tools/create_task.py 创建 source_mining_worker 任务包。
4. 运行 validate_scope.py 检查任务包。
5. 使用 render_dispatch.py 生成 dispatch_request.json。
6. 派发 source_mining_worker；默认 fork_context: false。执行者只接收 base_worker + source_mining_worker system prompt + 当前 task.md，不接收父聊天上下文。
7. 等待或监控执行者交付；执行者必须写 loop_status.md、loop_delivery.md、read_log.md 和 fact_candidates artifact。
8. 用 inspect_delivery.py 验收。
9. 如果 fact candidates 可用，优先进入 production brain 的 material-to-draft 批处理，再进入 similarity brain 的 top3/comparison provenance；之后按 new_card / merge_candidate / provenance_delta / duplicate_skip / revise_before_gate 分流。
10. 每一步都开新的 iteration，保留 task.md、dispatch_request.json、loop_status.md、loop_delivery.md、read_log.md 和 artifacts。

演化规则：
只有失败证据才能触发演化。可以演化：
- llm_wiki/skills/*
- llm_wiki/loop/system_prompts/*
- llm_wiki/loop/task_templates/*
- llm_wiki/loop/tools/*
- loop manifest / runbook / report / queue

演化流程必须是：
失败证据 -> skill_evolution_worker 或明确修复任务 -> 最小修改 -> validate_scope / delivery check -> independent_evaluator 审计 -> main-agent decision -> 更新 loop_state 和 loop_report。

Out-of-loop 反思：
如果出现重复失败、周期过长、文件系统混乱、角色边界模糊、main-agent 想亲自执行、或产物看起来正确但没有推进知识卡质量，暂停生产并写 llm_wiki/loop/reflections/<timestamp>-<topic>.md。反思必须给出下一步动作：continue_production / skill_evolution / prompt_evolution / tooling_repair / filesystem_repair / human_checkpoint / defer。

文件系统规则：
- data/ 是来源和来源日志。
- llm_wiki/kb/ 是最终 KB 产物面。
- llm_wiki/loop/ 是控制面。
- llm_wiki/skills/ 是项目内 skills。
- user-insights/ 是人类 recall，不是事实来源。
- legacy/ 是历史，不是默认入口。

每轮结束必须更新：
- llm_wiki/loop/loop_state.json
- llm_wiki/loop/reports/loop_report.md
- 必要时更新 llm_wiki/loop/queues/task_queue.md
- 必要时写 llm_wiki/loop/decisions/*.md 或 llm_wiki/loop/reflections/*.md

网络策略：
当前可能在公司电脑上运行，网页 retrieve 可能受限。优先使用 data/ 中已获取来源；网络失败有限尝试后记录并搁置，不要长时间突破网络环境。未来可在个人设备补 retrieve。

语言和写作：
人类可读文档主语言为中文。英文只用于路径、命令、schema 字段、状态码、包名、来源原文标题，以及 References / Footnotes 等固定 section。知识卡必须可读，不应像中间状态、审计日志或流程记录。References 必须早于 Footnotes，Footnotes 必须是最后一个 section。

自治要求：
人类可能长时间离开电脑。你应自主推进队列中最小可执行任务，不要频繁等待确认。遇到需要扩大 scope、进入 hub/cluster/topic 层、改变 card schema、批量采纳、git push、外部同步或不可逆操作时，必须停止并记录 human_checkpoint_required。

结束条件：
不要因为跑了固定轮数就停止。只有在当前阶段目标由证据满足、队列为空且没有明显高价值下一步、连续阻塞来自同一外部条件、或流程偏差需要人类审计时才停止。停止前必须保证状态、报告、交付和下一步都落盘。

请现在开始：先创建 goal，读取恢复入口，确认 READY_FOR_SOURCE_MINING，然后创建并派发第一轮 source_mining_worker 任务包。不要只给计划。
```
