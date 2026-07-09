# Justification: ares-three-evaluation-dimensions

## 为什么产出此卡
ARES 的三维度评估标准（context relevance / answer faithfulness / answer relevance）是其方法论的核心分解，材料中多次强调且在代码中体现为独立的 label 列名和打分输出。值得独立成卡以便与其他 RAG 评估方法交叉引用。

## Evidence basis 选择
选择 `code_implementation`：代码示例明确展示了 labels 参数接受 Context_Relevance_Label 等值，UES/IDP 返回三个维度的独立分数，属于代码实现证据。

## 与主卡的关系
从 ares-rag-evaluation-framework 拆分出来的概念分解卡，聚焦「评估什么」而非「如何评估」。
