# Part 3. Open Questions / Takeaways

## 3.1 多模态怎么处理

当前答案：先转文本处理。

多模态搜索本身很难，当前阶段更现实的做法是把 image / video / audio 转成可读文本，同时保留可追溯的原材料。这样当 card 信息不足或摘要质量偏弱时，agent 仍然可以回到原始材料继续消费、检查和补充。

## 3.2 如何完成人机交互和审核

当前答案：通过 GitHub Issues 做审核入口。

人可以用 issue 提出问题、修改建议、质疑或补充需求；agent 根据 issue 修复或补充知识库；用户满意后 close issue，仍有分歧则继续讨论和修改。

```text
human review
-> issue
-> agent fix
-> human check
-> close or continue
```

这个流程天然形成自迭代，也让人的审核保持轻量。

## 3.3 多个知识库如何融合

多 KB 融合的重点是治理对象之间的对齐。需要判断不同 KB 之间的 card 是否重复、互补、冲突，provenance 是否兼容，citation graph 是否能合并，promotion 状态是否一致。

真正困难的部分在于：两个 KB 可能使用不同颗粒度、不同事实类型、不同 citation 约定和不同 stable 承诺。融合时需要先对齐治理语义，再考虑内容合并。

## 3.4 如何处理超长文本

当前假设：默认内部文档长度通常不会超过 1M context。

短期策略是把长文本转成可分段消费的文本材料，再生成 digest / card；超过默认处理能力的材料进入专项处理流程。v3 的经验也说明，在上下文窗口允许时，完整读取来源优于防御性只读开头。

## 3.5 Takeaways

- **核心不是生成，而是治理。** 生成内容只是入口；长期价值来自对来源、边界、冲突、引用、修订和 promotion 的持续管理。
- **DIKW 帮助区分知识状态。** Data 对应 raw sources，Information 对应 draft，Knowledge 对应 accepted knowledge，Wisdom 则来自 accepted knowledge 中生长出的结构性判断。
- **事实需要类型和状态分开处理。** `known_fact` 和 `accepted_fact` 分别处理外部稳定事实 / 来源明示事实，以及当前系统采纳的阶段性事实；它们不等同于 card 的 draft / accepted 状态。
- **颗粒度决定可维护性。** 从 doc base 编译到 card / page-level KB，决定 agent 是否能长期维护，也决定人是否能快速消费。
- **候选层和稳定层必须分开。** Candidate 支持持续吸收新知识，stable 代表阶段性发布承诺；candidate-ready 不应被直接当成 stable product。
- **v3 的价值在于跑通候选知识闭环。** 它已经形成 candidate-ready KB；下一阶段重点是 promotion decision、citation / related 统一、多 KB 融合和后续增量生产。

这轮实验最重要的 takeaway 是：**从 raw documents 到 LLM-usable / human-readable knowledge base 的生产闭环已经开始成立。** 后续真正要验证的是，这个闭环能否在持续增长中保持可治理、可维护、可复用。
