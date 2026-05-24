# 接受 validate_scope 路径检查修复

- `timestamp`: `2026-05-25T06:54:51+08:00`
- `repair_iteration_id`: `iteration_20260525_0038_validate_scope_path_check_repair`
- `audit_iteration_id`: `iteration_20260525_0039_validate_scope_path_check_repair_audit`
- `decision`: `accept_tooling_repair`

## 失败证据

候选 1 audit 任务包中的 `fact_candidate_path` 指向不存在的 `llm_wiki/loop/iterations/iteration_20260525_0001_source_mining_karpathy_gist/artifacts/fact_candidates.md`，但旧版 `validate_scope.py` 派发前仍返回 `scope_validation: pass`。该失败由候选 1 audit worker 的 `read_log.md` 和主控决策 `20260525-0641-card-audit-pass-candidate-1-with-task-path-risk.md` 记录。

## 修复

`llm_wiki/loop/tools/validate_scope.py` 已最小增加 `## 允许输入` 区本地路径存在性检查：

- 缺失必需输入路径时输出 `missing_input_path` 并失败。
- 支持 `raw.txt:1-5` 这类行号后缀归一化。
- 跳过 `target_card_path` 和 `target_provenance_path`，避免误伤 adoption 前用于存在性检查的目标路径。
- 不检查允许写入区，避免把输出路径误判为缺失输入。

## 审计结论

`iteration_20260525_0039_validate_scope_path_check_repair_audit` 返回 `audit_result: pass`：

- bad task 现在按预期失败并报告 `missing_input_path`。
- valid task 与 repair task 均通过。
- 修复未扩大 role、template、schema 或知识卡生产 scope。
- 未发现枢纽页、聚类、主题覆盖或主控权限漂移。

审计 worker 的 `read_log.md` 记录曾读取 `/Users/lw/.codex/skills/agent-loop-runner/SKILL.md`，用途为运行环境技能约束，且明确“不作为审计证据”。这是非阻塞边界记录，不影响接受修复。

## 生命周期记录

repair audit 使用 one-shot independent evaluator，完成后已关闭。当前没有证据表明此类短审计需要 alive sub-agent 常驻；若未来出现大量重复读同一大型数据来源，可再通过 decision 明确 resident worker 边界。

## 下一步

恢复候选 1 adoption。创建 `card_adoption_worker` 任务包，输入限定为候选 1 draft/provenance、候选 1 audit report，以及目标 KB 卡片/provenance/index 路径；dispatch 使用 `fork_context:false`，完成后关闭 worker。
