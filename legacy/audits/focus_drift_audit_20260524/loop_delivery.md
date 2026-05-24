# 循环交付

`status`: `LOOP_DONE`
`decision`: `focus_drift_root_cause_identified`

## 写入文件

- `task.md`
- `evidence_log.md`
- `drift_timeline.md`
- `hypotheses.md`
- `hypothesis_validation.md`
- `root_cause_analysis.md`
- `recommendations_for_atomic_fact_loop.md`
- `loop_status.md`
- `loop_delivery.md`

## 发现摘要

根因已经确认：旧版 v1 系统把 `node` 设为生产对象，把主题覆盖设为规划框架，把版本束、采纳和视图构建设为质量门，并用已采纳主题节点与覆盖完成衡量成功。来源挖掘里曾有接近原子事实的观察，但任务包把它们压缩成主题节点生成。

## 关键回答

偏差不是来自单个执行者粗心，也不是引用或出处论证机制本身有问题。偏差来自对象层定义错误：系统把“要生产的东西”理解成主题节点，而不是来源支撑的原子事实知识卡。

## 建议下一步

停止沿用旧版主题/枢纽骨架循环。下一版先只做原子事实循环：来源 -> 事实候选 -> 知识卡草稿 -> 出处论证 -> 审计/采纳。枢纽页、聚类、主题等聚合要等原子事实基础稳定后再从下往上生长。
