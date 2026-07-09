# Justification: volatility-freshness-scoring

## 抽卡理由
波动性分级与新鲜度评分是 llm-wiki 维护优先级的量化机制——通过 hot/warm/cold 分级控制衰减速度，通过四维复合评分标记需要注意的文章。Lindy Effect 的应用使 cold 内容随时间变得更持久。

## 证据强度
- wiki-structure.md Volatility Classification 和 Freshness Score 段完整定义
- linting.md C14/C15 规则实现检查
- librarian.md Staleness Scoring 使用该公式
- compilation.md 要求设置 volatility 和 verified
- evidence_basis: code_implementation

## 原子性检验
单一核心 idea：volatility 分级驱动的复合新鲜度评分机制。
