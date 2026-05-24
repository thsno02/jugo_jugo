# Run Plan / 运行计划

run_id:: run_20260524_050634_major_impact_simulation
run_type:: simulated_major_change_impact_test

## 目标

为 `20260524_050033_source_preservation_precondition_trust` 创建一个未 adopted 的 2.0 major candidate，并验证 citation graph 是否能生成 impact queue。

## 规则

不更新 root `node.yaml`，不把 candidate 渲染进 `kb/`。
