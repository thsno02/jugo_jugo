# Autonomy Contract

run_id:: run_20260524_060000_preloop_planning
human_absent_assumption:: true
network_policy:: limited_company_network_attempts_then_defer

## Agent 可以继续做什么

Codex agent 可以在无人值守时继续执行：

- Source mining。
- Frontier merge。
- Node planning。
- Candidate bundle generation。
- Citation/provenance/adoption audit。
- Adopted KB view building。
- Generated graph/status rebuild。
- Skill evaluation and targeted skill patches。

## Agent 不能做什么

Codex agent 不能：

- 破坏性 git 操作。
- 绕过公司网络限制。
- 用未保存的网页答案直接支持 KB claim。
- 跳过 source mining/frontier 直接写 object-level adopted node。
- 把 KB 生产协议写成 LLM Wiki topic content。

## 网络策略

当前在公司电脑。网页 retrieve 失败时：

1. 记录失败 source、URL、状态和时间。
2. 写 retrieval request。
3. 标记为未来个人设备重试。
4. 回到可由本地 data 支持的候选。

## 反思策略

每轮完成后必须写：

- `.llmwiki/runs/<run_id>/skill_eval.md`
- `.llmwiki/control/summary_state.md`
- `.llmwiki/control/standing_status.md`
- `.llmwiki/control/decision_log.yaml`

每次只选择一个 next action。

