# task boundary audit

## status

`status`: `COMPLETE`
`audit_time`: `2026-05-25T14:20:53+08:00`
`worker_role`: `task_boundary_audit_worker`
`allowed_write`: `llm_wiki/loop/audits/20260525-control-plane-subagent-task-audit/task_boundary_audit.md`

## audit_result

`audit_result`: `CONCERN`

总体判断：LLM Wiki loop 的 task packet 已经形成了可审计的边界骨架，包括 `允许输入`、`禁止输入`、`允许写入`、`成功门禁`、`阻塞条件`、`read_log.md` 和 `LOOP_DONE` / `LOOP_BLOCKED`。已提交历史中，`validate_scope.py` 的路径存在性修复和候选块读取边界修复都经过独立审计，说明控制面确实从失败证据中演化。

但当前隔离质量仍不是强隔离。`validate_scope.py` 和 `inspect_delivery.py` 只能检查少量结构条件，无法证明 worker 没有读取父聊天、相邻候选、旧审计、未列出的 KB 卡片或未授权 JSON 字段。`read_log.md` 对人类复盘有用，但仍是自报账本，不是执行级读审计。当前未提交的相似门/融合草稿进一步引入了 accepted card 对照链路，方向合理，但需要更明确的两阶段输入授权，否则 worker 可能把“快速列出相似卡”理解成读取未列出的 KB 卡片。

## evidence_read

### 允许范围内读取

- `llm_wiki/loop/task_templates/*`：检查各类任务包模板是否包含 allowed inputs / forbidden inputs / allowed writes / success gate / blocker。
- `llm_wiki/loop/system_prompts/*`：检查 base worker、drafting、batch drafting、audit、adoption、similarity gate、fusion、independent evaluator、monitor 的角色边界。
- `llm_wiki/loop/tools/validate_scope.py`：检查 scope validation 实际覆盖面。
- `llm_wiki/loop/tools/inspect_delivery.py`：检查 delivery inspection 实际覆盖面。
- `llm_wiki/loop/iterations/iteration_20260525_0051_source_mining_karpathy_x_launch/artifacts/fact_candidates.md`：检查真实候选集结构和相邻候选风险面。
- 最近 iteration 的 `task.md`、`read_log.md`、`loop_delivery.md`、audit report：重点看 `0038`-`0048` 的边界修复链路、`0051` source mining、`0060`-`0064` 最新生产任务。
- `llm_wiki/loop/reports/loop_report.md`：核对已提交历史中的边界失败、修复、验收和当前 Atomic Draft First 状态。
- `llm_wiki/loop/audits/20260525-subagent-lifecycle-session-audit/*`：读取已有 lifecycle audit，区分生命周期问题和本次 task boundary 问题。

### 额外读取及原因

- `~/.codex/skills/agent-loop-runner/SKILL.md`：系统技能触发要求读取，用于本次 loop 审计方法约束，不作为 LLM Wiki 事实证据。
- `git status --short`、`git diff --name-status`、`git log --oneline`：读取 git 元数据，用于区分已提交历史和当前未提交控制面草稿；未把未授权文件正文作为审计证据。
- `llm_wiki/loop/audits/20260525-control-plane-subagent-task-audit/README.md`：读取本审计目录的分工说明，确认本 worker 只负责 `task_boundary_audit.md`。

### 工具实测

- `validate_scope.py` 对所抽查的 `0038`、`0039`、`0045`、`0046`、`0047`、`0048`、`0051`、`0060`、`0061`、`0062`、`0063`、`0064` task packet 均返回 `scope_validation: pass`。
- `inspect_delivery.py` 对已完成抽样 iteration `0038`、`0039`、`0045`、`0046`、`0047`、`0048`、`0051`、`0060`、`0061`、`0062`、`0063` 返回 `delivery_inspection: pass`。
- `inspect_delivery.py` 对 `iteration_20260525_0064_card_batch_drafting_karpathy_launch_remaining_a` 返回 fail，缺 `loop_status.md`、`loop_delivery.md`、`read_log.md` 和 completion marker；该 iteration 看起来是当前派发后尚未交付的任务，不应和已完成历史混为一谈。

### 已提交历史 vs 当前未提交草稿

- 已提交历史：`git log` 显示控制面已有 `Switch loop to atomic draft first` 等提交；`loop_report.md` 记录从 source mining、drafting、audit、adoption 到 validate_scope / candidate boundary 修复的完整历史。
- 当前未提交控制面草稿：`git status` 显示 `card_similarity_gate_worker.md`、`card_similarity_gate_task.md`、`system_prompts/README.md` 有修改；`card_fusion_audit_worker.md`、`card_fusion_adoption_worker.md`、`card_fusion_audit_task.md`、`card_fusion_adoption_task.md` 为未跟踪新文件。它们只能作为草稿风险评估，不能算已生效历史。
- 当前未提交 lifecycle audit folder 也存在，但已有 `main_agent_acceptance.md` 说明主控已接受并做事实修正；本审计把它作为当前控制面草稿/审计材料，而不是已提交基线。

## boundary_model

当前 task boundary 由四层组成：

1. `base_worker.md` 定义通用隔离：只把当前 `task.md` 当任务来源，不依赖父聊天上下文，只能读写 task 指定范围，额外读取必须先记入 `read_log.md`，最终回复和 delivery 必须有 `LOOP_DONE` 或 `LOOP_BLOCKED`。
2. role system prompt 定义角色不可做事项：例如 drafting 不采纳、不审计、不读 accepted KB 补事实；audit 不用父聊天或未列来源补事实；adoption 不运行 git、不大改卡片；similarity gate 不做事实审计。
3. 具体 `task.md` 应把模板落成实例：列出具体 source path、candidate id、JSON pointer、allowed writes、success gate、blocker。
4. 工具和审计做后验检查：`validate_scope.py` 在派发前做结构与允许输入路径检查；`inspect_delivery.py` 在交付后检查基本产物；independent evaluator 用磁盘证据做人工审计。

这个模型目前能降低普通越界风险，但不是执行沙箱。真实隔离仍依赖 worker 遵守 prompt、主控选择 `fork_context: false`、read_log 自报和后续人工审计。

## findings

### P0

- 无 P0。没有发现已提交历史中存在明确的生产 worker 越权写入、采纳未授权卡片、或把父聊天当事实来源落入 KB 的证据。

### P1

- `validate_scope.py` 和 `inspect_delivery.py` 无法覆盖真实读写隔离风险。
  - 证据：`validate_scope.py` 的 required phrases 只检查固定短语，包括 `## 允许输入`、`## 禁止输入`、`## 允许写入`、`## 成功门禁`、`## 阻塞条件`、`父聊天上下文`；允许输入路径检查只解析 `## 允许输入` 中的 code span 和本地路径存在性。
  - 证据：`inspect_delivery.py` 只要求 `task.md`、`loop_status.md`、`loop_delivery.md`、`read_log.md` 存在，并检查 delivery 中包含 `LOOP_DONE` 或 `LOOP_BLOCKED`。
  - 风险：工具不会检查实际读了哪些文件、是否只用了允许 JSON pointer、是否读了相邻候选、是否读了旧审计、是否读了未列 KB 卡片，也不会验证 success gate 中的语义条件。

- `read_log.md` 有复盘价值，但仍是自报，无法证明没有隐藏越界读取。
  - 证据：`0051` source mining 的 `read_log.md` 记录递归 `rg` 验证交付标记时意外扫到 `dispatch_request.json`，并在 delivery 中标为 `passed_with_disclosed_extra_read`。
  - 证据：`0046` 和 `0048` 独立审计都把结论限定为“磁盘记录未显示越界读取”，并承认没有读取未授权材料来反证隐藏读取。
  - 风险：如果 worker 没有主动记录，当前工具链不会发现。`read_log` 是良好审计面，不是强制访问日志。

- 当前未提交的 similarity gate 草稿存在“两阶段相似发现”边界歧义。
  - 证据：当前草稿要求 worker “先快速列出可能相似的现有卡”，同时允许输入只列 `target_index_path` 和 `similar_existing_card_paths`，禁止读取未列出的 KB 卡片。
  - 风险：如果“快速列出”只基于 `cards.md` 索引，是合理的；如果 worker 为了判断相似而打开未列出的 accepted cards，就会违反禁止输入。当前工具无法发现这种越界。
  - 范围：这是未提交工作区草稿，不是已提交历史缺陷。

### P2

- task packet 没有统一区分“控制面选择理由”和“worker 可用事实证据”。
  - 证据：多个具体 task.md 包含选择理由，例如“不重复已采纳卡”“当前 loop 价值”“生命周期判断”等。生产 worker 同时被禁止读取 accepted KB 或父聊天来验证这些判断。
  - 风险：这些文字不是原始父聊天，但会把 main-agent 的叙事判断带给 worker。它们适合作为 dispatch metadata，不应作为事实支撑、重复判断或审计结论依据。

- 候选块和 JSON 字段隔离主要靠自然语言约束。
  - 证据：`0063` task 明确只允许 `候选 11` 和 JSON pointer `$.tweet.quote.text`；`0064` task 明确 allowed candidates 和 source evidence pointers；这是好模式。
  - 缺口：`validate_scope.py` 不解析 candidate id、line range、JSON pointer，也不验证 worker artifact 是否引用了未授权字段。

- `read_log.md` 格式不统一，后续很难自动审计。
  - 证据：`0051` 使用 Markdown 表格，`0063` 使用 bullet list。两者人类可读，但工具无法稳定解析 path/reason/use，也无法对照 allowed inputs。

- task templates 的占位字段仍允许空列表通过人工派发。
  - 证据：模板中有 `similar_existing_card_paths:`、`draft_card_paths:`、`source_evidence_paths:` 等空占位；当前工具只检查固定短语，不检查关键字段是否非空或 role-specific required keys 是否存在。

## tooling_gaps

- `validate_scope.py` 应只算派发前 smoke，不应被当作完整边界证明。
- 缺少 role-specific schema validation：例如 drafting 必须有 candidate id 和 source pointer；batch drafting 必须有 allowed candidates；similarity gate 必须有索引读取和 explicit A-card list 的阶段边界；fusion adoption 必须有 audit pass evidence。
- 缺少 `allowed_writes` 检查：工具不验证输出路径是否和 task packet 匹配，也不检查同一输出是否被两个 worker 同时写。
- 缺少 artifact success gate 检查：`inspect_delivery.py` 不检查任务要求的 draft card、provenance、audit report、batch manifest、similarity gate report 是否存在，也不检查数量。
- 缺少 read_log 对账：没有把 `read_log.md` 的 path 和 task 的 allowed inputs、forbidden inputs 做差集。
- 缺少 JSON pointer / candidate block extractor：当前靠 worker 用 `awk` / `jq` 自律读取精确块；工具不提供可审计的候选块读取证明。
- 缺少执行级 read telemetry：要真正证明没有隐藏读取，需要 shell wrapper、hook、sandbox policy 或至少 command log，而不是纯 Markdown 自报。
- 缺少未提交草稿状态标记：当前相似门/融合链路在工作区草稿中已经可见，但任务包没有显式 `draft_control_plane: true` 或 `committed_baseline: false` 字段。

## task_packet_rules

建议把以下规则提升为 task packet 硬约束：

1. 每个任务包必须包含 `boundary_contract`：`allowed_inputs`、`forbidden_inputs`、`allowed_writes`、`success_gate`、`blockers`、`final_marker`。
2. 每个允许输入必须有 `path`、`use`、`allowed_scope`。对 JSON 证据必须写 `json_pointer`；对候选集必须写 `candidate_id` 和精确块边界；对行号证据必须写 `line_range`。
3. task packet 中的 `selection_reason` / `lifecycle_judgment` 必须标注 `control_metadata_only: true`，并说明不得作为事实证据或重复判断证据。
4. drafting / audit worker 默认禁止读取 accepted KB；只有 similarity / fusion / adoption 任务可以读任务包列出的 accepted card 或 provenance。
5. similarity gate 分两阶段：第一阶段只能读 KB index 并产出 candidate A-card list；第二阶段必须由主控重新派发或显式写入 `similar_existing_card_paths` 后，worker 才能读取具体 accepted cards。
6. `read_log.md` 使用统一表格或 JSONL 字段：`path`、`reason`、`use`、`allowed_by_task`、`scope_note`、`extra_read_before_log`。
7. 任何额外读取必须先写 `read_log.md`；如果因为命令意外暴露相邻内容，必须写 `boundary_noise`，并说明是否丢弃输出、如何重新精确读取。
8. `loop_delivery.md` 必须列出 `validation_commands` 和实际输出摘要；只写“预期通过”不满足成功门禁。
9. 当前工作区草稿 task/control-plane 文件必须在报告中标注 `uncommitted_draft`，不能和 HEAD 中已提交历史混用。
10. 如果任务需要父聊天或完整 fork context，必须明确标注 `fork_context: true`、使用原因、偏差控制和哪些结论必须回到磁盘证据验证；生产 worker 默认 `fork_context: false`。

## next_actions

1. 把 `validate_scope.py` 升级为 role-aware task packet checker，至少检查 required keys 非空、JSON pointer / candidate id / allowed writes / expected artifacts。
2. 给 `inspect_delivery.py` 增加 `task.md` 解析：按 allowed writes 和 success gate 检查 artifact 是否存在、数量是否匹配、delivery 是否记录实际 validation output。
3. 增加 `inspect_read_log.py`：解析统一 read_log，报告 allowed、extra-disclosed、forbidden-risk、unparseable 四类读取。
4. 为 `fact_candidates.md` 增加候选块提取工具，输入 candidate id，输出单块内容和边界证明；禁止 worker 用带上下文 `rg` 结果作为候选证据。
5. 在 similarity gate 草稿落地前，先修订 task packet：明确 index-only discovery 和 explicit A-card reading 的边界。
6. 在 loop report 或 control-plane audit README 中显式列出：HEAD 已提交历史、当前未提交控制面草稿、当前 active/incomplete iteration，避免 future worker 把草稿当事实基线。
