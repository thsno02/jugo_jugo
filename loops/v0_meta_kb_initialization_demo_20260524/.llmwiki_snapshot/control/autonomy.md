# 自治 Loop 策略

created_at:: 2026-05-24T05:10:00+08:00
latest_run:: .llmwiki/runs/run_20260524_050634_major_impact_simulation

## 目的

这个 KB initialization loop 需要在人类离开电脑时仍能推进。Agent 应把状态落盘，选择边界清晰的下一步，并定期反思当前行动是否仍在降低核心不确定性。

## 可自治执行

- 运行 validators 和 builders。
- 基于已保存的本地 evidence 创建额外 0-1 nodes。
- 为 evidence gap 写 retrieval request。
- 在 request 已存在且 raw source 可保存时，做小范围动态检索。
- 模拟一个 major candidate 来测试 impact analysis。
- 当 run 暴露明确 failure mode 时，更新 skill seeds。
- 写 report、summary state 和 decision log。

## 必须停止或记录 blocker

- 破坏性 git 操作。
- 覆盖 KB 初始化范围以外的人类文件。
- 把 audit 失败的 version 当作 adopted。
- 没有 retrieval request 和 preservation plan 就扩展到大规模 web research。
- 改变核心 node/version/citation contract，导致已有 bundles 失效。

## 公司网络检索限制

当前是在公司电脑中运行，网页检索可能被拦截或限制。不要尝试绕过网络控制。只做有限的正常 retrieval attempts；如果被 blocked/intercepted，就保存响应、写入 `retrieval_log.yaml`，并把完整 retrieve 留到未来个人设备运行。

## 决策规则

每个暂停点只选择一个 next action：

1. 如果脚本或 validators 失败，选择 `repair_instrumentation`。
2. 如果 adopted node 少于 5 且 evidence 充足，选择 `iterate_node_batch`。
3. 如果 recorded evidence gap 阻塞有用 node，选择 `dynamic_retrieval_test`。
4. 如果 citation graph 已存在但 impact propagation 未测试，选择 `major_impact_test`。
5. 如果 run 暴露重复 skill failure，选择 `skill_reflection`。
6. 如果 acceptance criteria 基本满足，选择 `demo_report`。
