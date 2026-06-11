# 读取边界噪声反思

- `timestamp`: `2026-05-25T07:10:16+08:00`
- `topic`: `fact_candidates.md adjacent-read noise and environment skill reads`
- `next_action`: `continue_production`

## 检查对象

本次反思检查执行者读取边界中的两类非阻塞噪声：

- `fact_candidates.md` 检索候选字段时偶尔带出相邻候选标题。
- 执行者按运行环境要求读取 `agent-loop-runner` skill 文件，并在 `read_log.md` 中声明只用于流程约束。

## 证据

- `iteration_20260525_0027_card_drafting_ingest_workflow/read_log.md` 曾记录候选字段复核时相邻扫到候选 12 标题开头，但未用于卡片或 provenance。
- `iteration_20260525_0033_card_drafting_persistent_composite_wiki/read_log.md` 曾记录关键词定位返回其它候选命中行和一次目录文件名检查，但未用于卡片或 provenance。
- `iteration_20260525_0041_card_drafting_human_llm_roles/read_log.md` 记录 `rg` 带上下文输出时意外显示下一候选标题起始行，随后改用精确 `sed` 读取候选 5；同时记录 `~/.codex/skills/agent-loop-runner/SKILL.md` 只用于执行流程约束，不用于知识卡事实内容或来源支撑。
- `iteration_20260525_0039_validate_scope_path_check_repair_audit/read_log.md` 也记录过 skill 文件读取，但明确不作为审计证据。

## 假设

- 假设 A：这些读取噪声污染了知识卡事实内容。
- 假设 B：这些读取噪声没有污染事实内容，但会降低恢复审计的清晰度。
- 假设 C：立即修改 worker prompt 或任务模板可以降低噪声，但也可能把小问题扩大为流程改造。

## 判断

假设 A 暂不成立。当前记录显示相邻候选标题和 skill 文件都未用于知识卡正文、provenance 或审计证据；候选 5 草稿卡的事实支撑仍限定在任务包指定来源行 `15-16,68-69`。

假设 B 成立。重复出现的相邻候选读取会让未来审计者额外判断“看见但未使用”的边界，因此需要在报告中计数，并保留复开条件。

假设 C 暂不充分。当前失败证据还没有表现为事实污染、未记录读取、写入越界或审计失败。直接演化模板可能比问题本身更重。

## 下一步

继续生产候选 5 的 audit 链路。若后续再次出现以下任一情况，则触发 prompt/template repair：

- 相邻候选内容被用于知识卡、provenance 或 audit 证据。
- `fact_candidates.md` 的相邻读取不再只是标题，而包含其它候选事实字段。
- read_log 未记录相邻读取。
- independent evaluator 因读取边界不清给出 `concern` 或 `fail`。

当前不使用 alive sub-agent 解决该问题；证据量小，且问题不来自重复大规模 I/O，而来自候选定位命令的边界习惯。

## 复开记录

- `timestamp`: `2026-05-25T07:33:28+08:00`
- `iteration`: `iteration_20260525_0044_card_drafting_llm_wiki_use_cases`
- `evidence`: `read_log.md` 记录候选 6 drafting 时检索 `fact_candidates.md` 返回了前一候选的尾部几行，且未用于卡片事实、表述或出处论证。

该证据触发上文复开条件：相邻候选内容不再只是标题，而包含其它候选字段片段。当前候选 6 草稿卡本身仍通过交付验收，事实支撑限定在 `raw.txt:17-23`，因此不需要重写产物；但在继续 audit 前应先做最小 prompt/template repair，要求后续 drafting worker 读取 `fact_candidates.md` 时使用精确候选块读取，避免带上下文检索暴露相邻候选。

新的 `next_action`: `prompt_evolution`。
