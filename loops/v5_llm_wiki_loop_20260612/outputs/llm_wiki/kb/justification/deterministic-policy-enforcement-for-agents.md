# Justification: deterministic-policy-enforcement-for-agents

## 为什么产出此卡
"确定性策略执行"是工具包最核心的设计原则，在文档开篇第一句和合规章节均被强调，且与当下 AI 治理领域"概率性审查 vs 确定性控制"的讨论高度相关。

## 证据强度
- "deterministic policy enforcement" 出现于文档首句
- "deterministic controls" 出现于 OWASP 合规描述
- Agent OS 作为策略引擎的角色直接引用自 Packages 列表
- evidence_basis = documentation

## 原子性判断
本卡聚焦"确定性策略执行"这一设计原则及其实现载体（Agent OS + Compliance），不涉及执行层（Runtime）或运维层（SRE）的具体机制。

## Hedge 标注
- "与基于 LLM 的概率性审查形成对比" — 这是从"deterministic"一词的语义推断而非材料显式陈述，但推断合理，未标记为强 hedge
