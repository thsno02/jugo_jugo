---
schema: claude_code_theme.v1
theme: runtime_and_context_isolation
publish_status: sanitized
---

# Runtime And Context Isolation

Claude Code 在这个 repo 里的核心价值，不只是“生成文件”，而是暴露了 agent loop 在长任务中的 runtime boundary。

## Core Model

```text
main-agent
-> defines boundary, state, gates
-> delegates source-level work
-> receives durable file artifacts
-> audits and publishes
```

main-agent 是控制面（control plane），不是主要生产者（executor）。当 main-agent 亲自消耗大量上下文执行单源生产时，通常说明 skill 或 sub-agent 边界设计出了问题。

## Cold Start

Claude session 经常在没有完整聊天上下文的情况下恢复工作。因此 loop capsule 必须自包含：

- handoff 描述启动顺序；
- task 文件描述阶段边界；
- queue/status/state 文件记录当前进度；
- reports/learnings 记录为什么进入下一阶段。

这个设计让新的 agent 可以从文件恢复，而不是依赖聊天记忆。

## Context Isolation

需要隔离的内容：

- source reading：单源材料和引用证据；
- extraction reasoning：questioning/reframing 过程；
- governance action：链接、去重、入库；
- audit judgment：机械审计和语义判断；
- publish decision：哪些进入 git，哪些 local-only。

## Reusable Rule

如果一个工作流需要跨天、跨 session、跨模型继续执行，聊天记录不能是唯一状态。状态必须落在 repo artifact 中，聊天记录只作为辅助 evidence source。
