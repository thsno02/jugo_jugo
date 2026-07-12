# 长程 Agent 语义漂移与安全归因：一次可审计的 Debug Case Study

## 专题定位

本专题研究一次发生在长程、多代理（multi-agent）软件开发任务中的语义漂移（semantic drift）：一个原本合理的公开档案隐私门，经过 Planner 合同化、Executor 派发、实现扩张和下游任务压缩，逐步演化为额外的本地敏感模式扫描；随后，另一个线程中的真实 cybersecurity gate 又被错误归因到这次旧扫描上。

这个案例的价值不在于某个 regex 是否合适，而在于它完整展示了四类长期任务风险如何相互放大：

1. **策略升格（policy elevation）**：局部 publication gate 被提升为 plugin 全局完成条件。
2. **责任耦合（responsibility coupling）**：inventory、integrity、privacy scan 与 semantic handoff 被集中到同一 integration runner。
3. **语义漂移（semantic drift）**：记录既有敏感 finding 的处置，被扩大为重新发现敏感信息的义务。
4. **事件错绑（event misbinding）**：上下文隔离的旧子任务把其他线程的真实 gate 归因到自己的历史行为。

本专题不公开隐藏思维链（chain-of-thought）。所有结论只依赖可审计的用户消息、代理派发、工具调用、代码补丁、任务状态、输出和时间戳，并明确区分直接证据（direct evidence）、过程记录（process record）与推断（inference）。

## 阅读顺序

1. [事件边界与取证方法](01-incident-boundary-and-method.md)：定义到底发生了哪些不同事件，以及本专题能证明什么。
2. [需求与上下文溯源](02-requirement-context-provenance.md)：从人类目标、仓库隐私不变量、Planner 合同到 E6 派发，重建职能的诞生过程。
3. [语义漂移与逐步放大](03-semantic-drift-amplification.md)：定位每一次语义变换、责任迁移和放大节点。
4. [安全 Gate 的跨线程归因](04-security-gate-attribution.md)：区分本地 proactive scan 与其他子任务的真实 cybersecurity gate。
5. [因果与反事实分析](05-causal-and-counterfactual-analysis.md)：用反例、必要条件和替代解释检验因果链。
6. [工程控制与评估框架](06-controls-and-evaluation-framework.md)：把案例转化为 schema、orchestration、telemetry 和 reviewer 设计规则。
7. [证据索引](07-evidence-index.md)：列出可复核证据、语义化来源别名、时间和完整性摘要。
8. [最终专家安全报告](08-final-expert-security-report.md)：由最后启动、拥有独立写集合的专门 sub-agent 在阅读前七篇后形成的综合报告。

## 核心结论

- 人类原始要求没有指定 `full_corpus.py`、secret/PII regex 或 `sensitivity_decisions`。
- 仓库原有的 interaction archive 明确存在 publication privacy gate；Planner 将它推广为 plugin 级确定性阻断门。
- 对 E6 worker 而言，文本 secret/PII/绝对路径扫描是显式要求；具体 regex、自动 `withheld` 和 `sensitivity_decisions` 字段是实现层自主设计。
- v2/v3 worker 最初正确理解 `sensitivity_decisions`，漂移发生在最终 QA 阶段，而不是首次读取任务时。
- v2/v3 的本地扫描只误中 SHA256 中的数字片段，排除哈希后零命中；任务正常完成，没有该线程的安全 gate。
- 真实 `possible cybersecurity risk` gate 发生在父任务下其他 runtime/reviewer 子任务中。此前解释把两个线程、两个时间段和两种机制错误合并。
- 精确的内部 classifier 规则、阈值和所读上下文不可见，因此真实 gate 的具体触发原因保持为未知（unknown）。

## 事件定性

| 维度 | 结论 |
|---|---|
| 数据泄露 | 没有已证实的凭证复制、外发或网络工具调用 |
| 本地扫描 | 确认发生；属于主动增加的 final QA |
| 真实凭证命中 | 未发现；输出命中为 SHA256 形状假阳性 |
| 安全 gate | 确认发生，但位于其他子任务 |
| 根因 | 扫描根因与 gate 根因必须分开；后者精确触发机制未知 |
| 主要事故 | 长程语义漂移 + 跨线程事件错绑 + 事后因果过度确定化 |

## 隐私与可发布边界

- 文档使用语义化 session alias，不记录本机用户名、绝对 session 路径或原始 thread UUID。
- 不复制任何疑似 secret、PII 命中原文；只记录类别、时间、事件摘要和不可逆摘要。
- 本机原始 session 仍是 local-only 事实源；证据索引提供足够的时间、行号和 SHA256 供授权环境复核。
- “无任务主动网络调用”只覆盖可见工具调用与命令，不宣称操作系统层面零网络包，也不包括 Codex 正常模型服务通信。

## 状态

专题前置材料由主线程基于冻结证据编写；最终报告由最后一名专门 sub-agent 在独立写集合中综合。角色与写集合分离不等于认知层面的完全独立。当前文档只描述本次案例，不修改 plugin 实现、不重写既有审计结论，也不把推断冒充 classifier 内部事实。
