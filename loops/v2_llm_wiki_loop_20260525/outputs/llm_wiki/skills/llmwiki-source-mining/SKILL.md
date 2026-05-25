---
name: llmwiki-source-mining
description: 从指定论文、网页、代码库、帖子或本地原始资料中抽取可追溯的原子事实候选；用于让执行者读取一个来源或严格限定的一组来源并产出事实候选，不写知识卡、枢纽页、主题节点或摘要。
---

# LLM Wiki 来源挖掘

## 目标

把一个明确来源中的事实挖成候选，不写知识卡，不做枢纽页，不做主题覆盖。来源挖掘的产物是事实候选和证据定位，不是知识库正文。

## 输入边界

优先读取任务包指定的主来源。已有知识卡、旧笔记或状态记录只能用于避免重复和理解边界，不能作为事实支持。

如果网页检索受公司网络限制，有限尝试后记录 `retrieval_deferred`，不要长时间突破网络环境。

## 工作流

1. 确认任务包完整落盘，并写初始 `loop_status.md`。
2. 读取指定来源的原始文件、可读文本、source bundle、代码库 README 或 manifest；这些文件类型名称按原始数据命名保留。
3. 抽取 5-10 个原子事实候选。
4. 每个候选只表达一个事实。
5. 为每个候选记录证据定位、适用范围、事实类型候选和不确定性。
6. 把证据不足、粒度过大或依赖外部检索的内容放入 `deferred`，不强行写成事实。

## 输出

建议输出：

```yaml
fact_candidates:
  - statement: <一句事实候选>
    fact_type_candidate: known_fact | accepted_fact
    support:
      source_path: <path>
      locator: <章节 / 行号 / 引文定位>
    scope: <成立范围>
    uncertainty: <不确定性>
    status: candidate
deferred:
  - reason: <为什么暂缓>
```

同时写：

- `source_notes.md`：中文记录来源中与候选有关的观察。
- `retrieval_requests.md`：需要未来个人设备重新检索的内容。
- `loop_status.md` 与 `loop_delivery.md`。

## 禁止事项

- 不生成主题节点。
- 不生成枢纽页。
- 不写原子事实知识卡正文。
- 不把多个事实压缩成一个候选。
- 不把来源观点改写成无适用范围的普遍真理。
