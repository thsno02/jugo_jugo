# control-plane sub-agent / task audit

`status`: `IN_PROGRESS`
`created_time`: `2026-05-25T10:50:00+08:00`
`audit_scope`: 之前的 LLM Wiki loop、sub-agent 使用、任务边界、任务流程、已有 lifecycle audit。

## 用户关心点

- sub-agent 是否开得过多、生命周期是否可恢复。
- 任务边界是否真的隔离：allowed inputs / writes / read_log / delivery / close。
- 任务流程是否导致低吞吐、过度串行、card 质量偏薄。
- 当前未提交的流程草稿必须和已提交历史分开判断。

## 分工

- `subagent_lifecycle_audit.md`: 审计 sub-agent 生命周期、registry、fork_context、close 与并行写入。
- `task_boundary_audit.md`: 审计 task packet、role prompt、read/write scope、validation 工具和实际 read_log。
- `task_flow_audit.md`: 审计生产流程、吞吐、相似门、card 质量门与审计/发布链路。

## 约束

审计 worker 只写本目录内各自负责的文件，不修改 loop 控制面、KB、source material 或 git history。
