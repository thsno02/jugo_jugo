# v1 → v5：生产系统怎样逐步换掉自己的错误假设

| 维度 | v1 | v2 | v3 | v4 | v5 |
|---|---|---|---|---|---|
| 生产对象 | 主题枢纽 | scoped card | draft-first card | question-driven card | routed、governed card |
| 发现顺序 | 先主题后证据 | 先来源后卡片 | 先草稿后比较 | 先问题后回到材料 | 先按来源类型选择 evidence surface |
| 主代理角色 | 名义决策者，曾越界执行 | 强控制面 | 编排批量流水线 | 编排 questioner/reader | 编排 waves 与顺序治理 |
| 相似与融合 | 不适用 | 开始形成比较环节 | Top-3 + comparison provenance | cross-link / distinction | pairwise fusion + anti-merge bias |
| 引用模型 | References + Footnotes | card / provenance 分层 | unified citation；related 派生 | typed footnotes | evidence_basis + hedge preservation |
| 治理方式 | topic coverage QA | worker boundary gate | publication / fusion gate | grep + FSJS | YAML lint + graph passes + FSJS |
| 主要失败 | 错误生产对象被完整执行 | 控制成本过高 | 仍可能受既有管线结构影响 | source fallback 与图治理不足 | repo 信息密度和审计指标仍需改进 |

## 贯穿五版的变化

### 1. 从“结构完整”转向“证据扎实”

v1 的成功标准是主题覆盖；v2 之后，成功标准逐渐转向单张卡片能否被来源支撑、能否保持可读、能否经过 provenance 和审计。

### 2. 从“代理写文档”转向“代理系统治理”

main agent 的职责逐步从亲自阅读和写作，收敛为选择下一动作、派发有界任务、检查交付、处理冲突和演化流程。sub-agent 是否越界、何时关闭，成为知识质量的一部分。

### 3. 从“链接存在”转向“链接可解释、可计算”

v1 主要验证 citation graph；v3 把正文 citation 变成事实源；v4 增加 typed footnotes；v5 再通过 YAML parser、orphan 和 backward backlink passes 治理整张图。

### 4. 每次完成都会暴露新的瓶颈

v1 完成后才看见生产对象错误；v3 达到规模后才看见发现方式的结构先验；v4 达到 328 卡后才看见来源路由和图治理问题；v5 达到 477 卡后又暴露 repo 信息密度和指标设计问题。版本演化不是替换失败品，而是让下一层问题变得可见。
