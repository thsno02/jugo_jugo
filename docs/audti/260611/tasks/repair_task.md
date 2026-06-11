# 通用任务：返修（Repair）

## 输入

sub-agent 接到任务时必须读取：

- `docs/audti/260611/protocols/execution_protocol.md`
- `docs/audti/260611/daily/YYYYMMDD_*.md`
- `docs/audti/260611/audits/YYYYMMDD_*_audit.md`

调用方必须提供 `day_id=YYYYMMDD` 和返修轮次（repair round），例如 `r1`。

## 写入范围

只允许写：

- `docs/audti/260611/repairs/YYYYMMDD_rN_repair_notes.md`
- 需要时覆盖或新增同一天 `daily/YYYYMMDD_*.md`
- 需要时覆盖或新增 `logs/day_YYYYMMDD_read_log.md`

不得修改审计报告、decisions、final、day_queue 或目标目录外文件。

## 工作步骤

1. 只处理审计报告 `必须返修（Required Changes）` 中列出的 P0/P1/P2。
2. 每条返修必须映射到审计项。
3. 不新增审计未要求的大范围重写，除非它是修复审计项所必需。
4. 写 `repair_notes.md`，说明每个问题如何修复、引用了哪些证据。
5. 返修后等待新的 independent audit；repair worker 不得自判通过。

## 完成标记

final response 以：

```text
REPAIR_DONE YYYYMMDD rN
```

结尾。
