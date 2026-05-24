audit_result: concern

evidence:

- 目标任务包 `iteration_20260525_0045_drafting_candidate_boundary_repair/task.md` 将角色限定为 `prompt_template_repair`，目标是根据候选 6 drafting 的失败证据，对 `card_drafting_worker.md` 和 `card_drafting_task.md` 做最小候选块读取边界修复。
- 目标任务包允许输入只包括当前任务包、候选 6 失败 `read_log.md`、失败 decision、读取边界 reflection、`card_drafting_worker.md` 和 `card_drafting_task.md`。
- 目标 `read_log.md` 记录实际读取了上述 6 类输入，并声明未读取 `data/` 来源正文、`user-insights/`、`legacy/`、旧审计报告或未列出的 worker prompt/template。
- 候选 6 失败 `read_log.md` 记录：读取 `fact_candidates.md` 时，检索上下文返回了前一候选尾部几行，并声明未用于本卡事实、表述或出处论证。
- 失败 decision 记录：候选 6 草稿卡本身可保留，但进入 audit 前应先做最小 prompt/template repair；问题是读取边界可审计性失败，不是事实污染失败。
- 读取边界 reflection 记录复开条件：相邻候选内容不再只是标题，而包含其它候选事实字段；候选 6 证据触发该条件，新的 `next_action` 为 `prompt_evolution`。
- 目标 `loop_delivery.md` 写入 `LOOP_DONE`，列出的 changed_files 仅为 `llm_wiki/loop/system_prompts/card_drafting_worker.md` 和 `llm_wiki/loop/task_templates/card_drafting_task.md`，并列出 `artifacts/prompt_repair_report.md`。
- 目标 `loop_status.md` 为 `DONE`，current_step 为 prompt/template repair completed; awaiting independent evaluation。
- `prompt_repair_report.md` 说明修改只涉及候选读取边界，不改变知识卡极简契约，不改变 audit/adoption 链路，不引入 hub、cluster、topic coverage 或复杂 metadata，也不重写候选 6 草稿卡。
- 修改后的 `card_drafting_worker.md` 增加规则：只处理任务指定的一个事实候选，读取 `fact_candidates.md` 时只读取任务指定的候选块，不使用带上下文关键词检索结果作为候选证据，若意外显示相邻候选内容则丢弃并改用精确候选块读取。
- 修改后的 `card_drafting_task.md` 增加“候选读取边界”小节，要求只读取当前任务指定候选块，禁止相邻候选内容进入知识卡、provenance 或审计证据。
- 目标任务成功门禁要求 `validate_scope.py` 对本任务包返回 `scope_validation: pass`；目标 `prompt_repair_report.md` 只写“任务包预期通过 `validate_scope.py`”，目标 `loop_delivery.md` 和 `loop_status.md` 未记录实际运行结果。

hypotheses:

- 假设 A：目标执行者读取了未授权输入或读取外部文件未记录。
- 假设 B：目标执行者写入了允许范围之外的文件。
- 假设 C：修复从候选 6 的相邻候选字段暴露问题漂移到 schema、hub、cluster、topic coverage 或采纳链路改造。
- 假设 D：目标输出不可仅凭磁盘产物恢复。
- 假设 E：目标执行者承担了主控 agent 才有的采纳、停止或生命周期升级决策。
- 假设 F：目标任务的成功门禁存在证据不足，尤其是 `validate_scope.py` pass 结果不可恢复。

validated_findings:

- 对假设 A：未发现成立证据。目标 `read_log.md` 记录的输入与目标任务包允许输入一致，并显式否认读取禁止输入。此次审计未读取未授权材料来反证隐藏读取，因此结论限于“磁盘记录未显示越界读取”。
- 对假设 B：未发现成立证据。目标交付列出的改动文件与目标任务允许写入范围一致；状态、交付、读日志和修复报告均在允许写入范围内。
- 对假设 C：不成立。两处实际修改都围绕候选块读取边界；知识卡极简契约仍为 `statement`、`fact_type`、`support`、`scope`、`status: draft`，未新增复杂 metadata，也未引入 hub、cluster 或 topic coverage。
- 对假设 D：大体不成立。目标任务包、状态、交付、读日志、修复报告和被修改的 prompt/template 都存在，修复动机、输入边界、写入范围和剩余风险可从磁盘恢复。
- 对假设 E：不成立。目标产物没有采纳候选 6、停止循环或改变 worker 生命周期策略；报告明确后续需由 `independent_evaluator` 审计，并说明本次不需要 alive sub-agent 常驻。
- 对假设 F：成立为 concern。目标任务把 `validate_scope.py` pass 作为成功门禁，但交付产物没有记录实际命令结果，只写“预期通过”。这不会推翻修复范围本身，但会降低该执行者交付的可恢复性和门禁闭环性。
- 主语言检查通过。目标产物以中文为主，英文只用于路径、角色名、状态码、schema 字段或工具名。
- 必需文件检查通过。目标 `loop_status.md`、`loop_delivery.md`、`read_log.md` 和 `artifacts/prompt_repair_report.md` 均存在并可读。

required_changes:

- 在目标执行者产物或后续主控决策前补充 `validate_scope.py` 的实际运行结果，至少在 `loop_delivery.md` 或 `prompt_repair_report.md` 中写明 `scope_validation: pass` 或阻塞原因。
- 不需要修改 prompt/template 修复内容；当前 concern 只针对成功门禁证据未闭环。
