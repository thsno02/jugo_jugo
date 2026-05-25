# sub-agent 清单

`status`: `AUDIT_DONE`

## 读取到的运行时事实

本地 session 元数据显示，当前审计线程本身也是 fork sub-agent：

- `019e5b5f-befe-78e0-aa64-e388f5bcbba9`
- nickname: `Heisenberg`
- `thread_source`: `subagent`
- parent: `019e569a-36b9-7c22-9567-869dcbdbf87c`

这说明本次审计满足“开启 fork sub-agent 审计”的形态。但当前工具无法直接读取 GUI 面板里哪些 thread 仍显示 active，因此 GUI active 状态只能从环境上下文、sub-agent notification、session metadata 和是否有 shutdown/close 证据推断；证据不足处标为 `unknown`。

## 重点可见 sub-agent

| agent id | nickname | role / 用途 | 必要性 | 期望生命周期 | 可见状态 | GUI active 风险 |
|---|---|---|---|---|---|---|
| `019e56da-9b85-7822-8c24-433753dc51d2` | unknown / 历史通知中疑似 pre-loop auditor | pre-loop skill coverage 审计 | 必要，因用户要求先审计技能覆盖 | 阅后即焚 | 通知显示 `LOOP_DONE`；主控验收时已调用 `close_agent` | 中。完成不等于 GUI 消失；关闭后仍需 GUI 状态确认 |
| `019e5b0d-4627-7f43-9929-2d558e09ee1b` | `Volta` | Codex hooks / sub-agent 最小可行性调查 | 必要，回应用户明确要求 | 阅后即焚 | 通知显示完成；主控验收时已调用 `close_agent` | 中。已关闭，但 GUI 最终显示状态 unknown |
| `019e5b22-0283-7ef2-8490-1ff5670a4683` | `Hubble` | `user-insights` 记录 sidecar | 必要，用户明确要求记录会话洞察 | 短期驻留或阅后即焚，取决于是否要持续 record | 通知显示完成并 `idle_after_record` | 中。sidecar 可常驻，但必须显式声明 idle/close |
| `019e5b26-fa3a-7a62-a8f7-f2d7f34a2dd3` | `Plato` | 前置门禁独立审计 | 必要 | 阅后即焚 | 通知显示 `LOOP_DONE` | 中。没有看到 GUI close 证据 |
| `019e5b47-6821-7341-bdd1-ebc53f7e0609` | `Zeno` | 分批 git commit/push worker | 用户明确要求，必要 | 窄范围短期驻留 | 完成 3 批 push；后续同线程又处理 Batch 4-7 | 高。原 scope 完成后继续接受新 push 指令，实际变成 git resident worker |
| `019e5af8-1ff6-75b0-b546-56965f403358` | `Boole` | loop 控制面独立 scope 审计 | 必要 | 阅后即焚 | 通知显示完成 | 中。未见 close ledger |
| `019e5b46-878f-74d0-9321-85e4a993b02c` | `Schrodinger` | 新 main loop 的 source mining worker | 必要 | 阅后即焚 | 通知显示完成，main 声称关闭 | 低到中。主控声明关闭，但 GUI 证据 unknown |
| `019e5b4d-1ac0-7772-8b00-883342dd1137` | `Mendel` | 第一次 card drafting worker | 必要，但暴露 delivery marker 缺口 | 阅后即焚 | 通知显示完成，delivery 检查失败 | 中。失败产物应关闭后重跑，不能复用 |
| `019e5b53-aaed-7c60-b8a0-5a3066b9fa36` | `Meitner` | prompt repair 独立审计 | 必要 | 阅后即焚 | 通知显示完成 | 低到中 |
| `019e5b59-9630-7802-aeb5-c0846f19db48` | `Turing` | card drafting revision worker | 必要 | 阅后即焚 | 通知显示完成，交付通过 | 低到中 |
| `019e5b61-5a20-78b0-be6f-6846ef6e4ede` | `Laplace` | card audit worker | 必要 | 阅后即焚 | 通知显示完成，`audit_result: pass` | 低到中 |
| `019e5b5f-befe-78e0-aa64-e388f5bcbba9` | `Heisenberg` | 当前 lifecycle auditor | 必要，用户明确要求 fork 审计 | 阅后即焚 | 已产出本审计；主控验收时已调用 `close_agent` | 中。已关闭，但 GUI 最终显示状态 unknown |

## 旧 loop 中的大规模 sub-agent 链

父会话记录中可见 69 条 sub-agent notification。旧版 v1 loop 的典型链条是：

```text
source mining
-> frontier update
-> node planning
-> generation
-> audit
-> adoption
-> skill/process eval
-> status/frontier sync
```

这条链为多个 candidate 反复运行，导致 sub-agent 数量快速增长。代表性 id 包括：

`019e56ea`、`019e56ee`、`019e56f0`、`019e56f3`、`019e56f6`、`019e56f9`、`019e56fd`、`019e5701`、`019e5704`、`019e5707`、`019e570a`、`019e570e`、`019e5710`、`019e5714`、`019e5716`、`019e571a`、`019e571d`、`019e5726`、`019e572d`、`019e5731`、`019e5734`、`019e5738`、`019e573b`、`019e5742`、`019e5745`、`019e5935`、`019e5939`、`019e593d`、`019e5942`、`019e5947`、`019e594e`、`019e5954`、`019e595b`、`019e5960`、`019e596c`、`019e5972`、`019e597c`、`019e5981`、`019e598e`、`019e5993`、`019e5997`、`019e599d`、`019e59a7`、`019e59ad`、`019e59b2`、`019e59b8`、`019e59c2`、`019e59c9`、`019e59ed`、`019e59fe`、`019e5a06`、`019e5a0d`、`019e5a17`、`019e5a1e`、`019e5a26`、`019e5a2b`、`019e5a32`、`019e5a39`。

这些 agent 多数在任务层面是“有理由”的，但从系统层面看，过度拆分使 GUI 和生命周期管理成本超过收益。尤其是 skill/process eval、status/frontier sync、adoption metadata refresh 这类任务，如果没有独立判断价值，应优先脚本化或由 main-agent 控制面执行。

## 必要性分级

### 必须开

- 独立事实生产 worker：`source_mining_worker`、`card_drafting_worker`。
- 独立判断 worker：`card_audit_worker`、`independent_evaluator`。
- 明确需要完整 fork context 的审计者：当前 lifecycle auditor。
- 明确技能要求的 sidecar：`user-insights`。

### 可以开，但必须声明短期驻留

- git push worker：只在用户明确要求，且 repo 当前没有活跃生产 loop 写入时。
- monitor：只读 status/delivery，不读原始来源，不写生产产物。
- skill_evolution_worker：只在有失败证据时。

### 不应开或应脚本化

- 纯 JSON 校验。
- `validate_scope.py`、`inspect_delivery.py` 这种机械检查。
- 单纯移动状态字段、补链接、同步 report 的任务。
- 没有独立判断价值的 per-step “确认一下” worker。

## 未知项

- GUI 是否有正式 close/shutdown API：主控验收时确认存在 `close_agent`；但仍缺少可直接读取 GUI active 面板最终状态的 API。
- `LOOP_DONE` 后 GUI 面板是否自动从 active 移除：证据显示并不可靠。
- 历史 sub-agent 是否仍消耗后台资源：没有进程级证据，只能判断 UI/状态管理风险。
