# 通用任务：最终总线路（Final Timeline）

## 输入

sub-agent 接到任务时必须读取：

- `docs/audti/260611/protocols/execution_protocol.md`
- `docs/audti/260611/source_inventory.md`
- `docs/audti/260611/day_queue.md`
- `docs/audti/260611/daily/*.md`
- `docs/audti/260611/audits/*.md`
- `docs/audti/260611/decisions/*_acceptance.md`

只允许合并 `day_queue.md` 中状态为 `accepted` 且存在主控验收记录的日期。

## 写入范围

只允许写：

- `docs/audti/260611/final/total_timeline.md`
- `docs/audti/260611/final/total_timeline_evidence_map.md`

不得修改 daily、audits、decisions、day_queue 或目标目录外文件。

## 工作步骤

1. 读取所有 accepted 日期，区分实质开发日、固化日、空窗日和过渡日。
2. 不直接从未审计 transcript 生成新结论；只能合并已通过日报、审计报告和主控验收。
3. 按自然阶段组织总线路，而不是机械堆叠每日摘要。
4. 每个关键转折点链接到对应 daily/audit/decision。
5. 列出未纳入内容、残余风险和证据等级差异。

## 输出结构

`total_timeline.md` 必须包含：

- `一页结论`
- `总体时间线`
- `阶段划分`
- `关键转折点`
- `决策链`
- `未纳入内容`
- `风险与残余不确定性`
- `附录：每日索引`

## 完成标记

final response 以：

```text
FINAL_TIMELINE_DONE
```

结尾。
