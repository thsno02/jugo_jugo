# Justification: olw-llm-as-compiler

## 为何产卡
"LLM as compiler, not conversation partner" 是 olw 的核心设计哲学，源自 Karpathy 的 LLM Wiki 构想，构成独立于实现细节的原子理念。

## 证据来源
- README "The idea (Karpathy's LLM Wiki)" 一节完整阐述该哲学
- "Why not just use a chatbot?" 一节对比论证
- 引用 Karpathy 原文

## evidence_basis 选择
选择 `author_claim`：这是设计理念/哲学主张，非纯代码实现事实。README 作者阐述其对 Karpathy 构想的理解和采纳。

## 边界决策
- 不与三阶段管线合并：管线是实现层面的架构描述，此卡是更高层的哲学定位
- 不纳入 Synto 后继信息：maintenance mode 转 Synto 是项目生命周期事件，非核心概念
