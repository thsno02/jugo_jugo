# Justification: attention-dilution-crossover

## 提取依据
Section 4 (The Scalability Gap) 完整展示 FC vs RAG 在不同规模下的逆转，包含量化的交叉证据(557 个 lost-in-middle 案例)。

## 原子性判断
文档数交叉点是独立的实验发现，不依赖 WiCER 算法，为 LLM Wiki 模式的操作边界提供关键参数。

## Evidence basis
experimental_paper -- Policygenius 和 RepLiQA 双数据集的对比实验。
