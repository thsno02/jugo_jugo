# 反思策略

## 反思频率

每个 run 完成后反思一次；每次 validation/build failure 后也反思一次。

## 反思问题

1. 最近一步是提高了 KB auditability，还是只是增加了内容？
2. 哪个假设失败了？
3. 这是 case-level 问题，还是 reusable skill failure？
4. 另一个 agent 是否能只凭磁盘状态恢复？
5. 下一步最高价值的单一 action 是什么？

## 必需输出

- `.llmwiki/control/summary_state.md`
- `.llmwiki/control/standing_status.md`
- `.llmwiki/control/decision_log.yaml`
- `.llmwiki/runs/<run_id>/skill_eval.md`
