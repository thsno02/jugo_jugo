# Justification: lightmem-soft-vs-hard-memory-update

## 为什么产出此卡
软/硬更新对比是独立于 LightMem 具体实现的设计原则——它揭示了 LLM 作为更新决策者的可靠性问题，对任何记忆系统设计者有参考价值。与 offline update 卡分离是因为此卡聚焦"为什么"（rationale），而非"怎么做"（mechanism）。

## 材料锚定
- "Why Soft Updates Work" 段落
- Case Study tcolorbox 给出具体示例
- 该论证逻辑为全篇 Light3 设计的基础

## Hedge 说明
"可能将...误判" 保留了原文 "might incorrectly interpret" 的不确定性。
