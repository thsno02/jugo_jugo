# 通用任务：每日梳理（Daily Synthesis）

## 输入

sub-agent 接到任务时必须读取：

- `docs/audti/260611/protocols/execution_protocol.md`
- `docs/audti/260611/source_inventory.md`
- `docs/audti/260611/day_queue.md`

调用方必须提供 `day_id=YYYYMMDD`。worker 从 `day_queue.md` 找到对应日期、候选主题、主要证据源和下一步摘要。

## 写入范围

只允许写：

- `docs/audti/260611/daily/YYYYMMDD_<slug>.md`
- `docs/audti/260611/logs/day_YYYYMMDD_read_log.md`

不得修改 `audits/`、`decisions/`、`final/`、`repairs/`、`day_queue.md` 或目标目录外文件。

## 工作步骤

1. 建立本地日期窗口：`YYYY-MM-DD 00:00:00 +0800` 到下一日 `00:00:00 +0800`。
2. 读取 `day_queue.md` 的当天行，提取候选主题和主要证据源。
3. 回到一手证据做三角校验（triangulation）：优先 transcript + loop artifact + git history。
4. 判断当天类型：
   - `substantive_development`: 有实质开发。
   - `solidification_day`: 主要是 git 固化/归档/push。
   - `empty_window`: 未确认实质项目开发。
   - `transition_day`: 只有过渡或外部工作证据。
5. 产出日报，不能把推测写成事实，不能把后续日期写进当天结论。
6. 写 read log，记录读取路径、命令、用途和未读原因。

## 日报结构

日报必须包含：

- 标题：`# YYYY-MM-DD 每日梳理：<短标题>`
- metadata：`status: draft`、`day_id`、`audit_status: pending`、`source_window`
- `当日结论`
- `时间线`
- `关键决策`
- `实现变化`
- `问题、坑、解决方案`
- `证据地图（Evidence Map）`
- `未解决问题`
- `当日边界`
- `自检`

空窗日也必须完整写这些 section，但可以说明无实质事件。

## 质量要求

- 主语言中文，术语用「中文（English）」锚定。
- `docs/**` 和 `user-insights/**` 不能作为唯一事实源。
- 区分 transcript 发生事实、loop artifact 落地事实、git 固化事实。
- 明确残余风险（Residual Risk）和证据缺口。

## 完成标记

final response 以：

```text
DAILY_SYNTHESIS_DONE YYYYMMDD
```

结尾。
