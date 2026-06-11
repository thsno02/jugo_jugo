# 通用任务：独立审计（Independent Audit）

## 输入

sub-agent 接到任务时必须读取：

- `docs/audti/260611/protocols/execution_protocol.md`
- `docs/audti/260611/source_inventory.md`
- `docs/audti/260611/day_queue.md`
- `docs/audti/260611/daily/YYYYMMDD_*.md`
- `docs/audti/260611/logs/day_YYYYMMDD_read_log.md`

调用方必须提供 `day_id=YYYYMMDD`。审计者不继承 daily worker 的结论，必须从日报和一手证据重新核查。

## 写入范围

只允许写：

- `docs/audti/260611/audits/YYYYMMDD_<slug>_audit.md`

不得修改 `daily/`、`logs/`、`decisions/`、`final/`、`repairs/`、`day_queue.md` 或目标目录外文件。

## 工作步骤

1. 读取日报和 read log，列出所有 claim_id。
2. 回到一手证据核查每个 claim：transcript、loop artifact、git history、user-insights/docs 二次对照。
3. 检查日期归属：本地日期、UTC 转换、运行时间 vs git 固化时间。
4. 检查是否有跨日污染、无证据重大结论、summary 误用、后验归档误用。
5. 给出 `audit_result: pass | revise | block`。
6. 给出 `gate_decision: advance | repair_required | blocked`。

## 审计报告结构

必须包含：

- 标题：`# YYYY-MM-DD 独立审计：<短标题>`
- metadata：`status: AUDIT_DONE`、`audit_result`、`gate_decision`、`audited_artifact`
- `审计结论`
- `必须返修（Required Changes）`
- `证据核查`
- `范围核查`
- `结构核查`
- `残余风险（Residual Risk）`
- `门禁建议`

## 判定规则

- `pass`: 关键结论被证据支撑；弱证据或缺口已在日报中清楚降级。
- `revise`: 有明确返修项，但无需用户裁决。
- `block`: 证据不足、范围不清、冲突无法自解，或需要用户判断。

空窗日可 `pass`，但必须明确这是空窗日通过（empty-window pass），不是实质开发通过。

## 完成标记

final response 以：

```text
INDEPENDENT_AUDIT_DONE YYYYMMDD
```

结尾。
