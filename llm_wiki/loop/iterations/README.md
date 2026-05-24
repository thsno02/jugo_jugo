# 循环轮次目录

每一轮循环都应该有独立目录。

推荐结构：

```text
iteration_YYYYMMDD_NNN_<slug>/
  task.md
  loop_status.md
  loop_delivery.md
  read_log.md
  artifacts/
```

## 文件职责

- `task.md`：主控 agent 写出的窄任务包。
- `loop_status.md`：执行者开始后先写，记录当前状态。
- `loop_delivery.md`：执行者结束前写，记录交付、阻塞和下一步建议。
- `read_log.md`：记录所有允许输入之外的读取。
- `artifacts/`：事实候选、草稿卡、出处论证、审计报告或其它任务产物。

不要把多个逻辑任务混在同一个 iteration 目录里。一个 iteration 只推进一个主要动作。
