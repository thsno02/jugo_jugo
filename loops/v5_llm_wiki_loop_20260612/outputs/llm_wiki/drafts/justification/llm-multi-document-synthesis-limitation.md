# Justification: llm-multi-document-synthesis-limitation

## 为何产出此卡
多文档综合能力不足是论文揭示的三大挑战之一，且是长上下文 LLM 发展的核心 research direction。

## 材料锚点
- Section 5.3 Retrieval Analysis 的 "more passages do not help" 讨论
- Table 4 的 ChatGPT-16K vs GPT-4 对比
- ClosedBook 正确性超过 Vanilla 的反直觉发现

## Reframe 决策
- 将多处散布的 "LLM 不擅长利用长上下文" 证据整合
- ChatGPT-16K 性能下降是关键 counter-evidence against "bigger context = better"
- 保持 "non-trivial" 等 hedge 表达
