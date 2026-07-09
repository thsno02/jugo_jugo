# Justification: openkb-pageindex-vectorless-retrieval

## 为什么产出此卡
PageIndex 是 OpenKB 实现"No Vector DB"承诺的核心技术组件，材料单独设有 "PageIndex Integration" 一节和 "Short vs. Long Document Handling" 对比表。作为独立的检索技术方案，值得原子化为一张卡。

## Evidence basis 选择
`code_implementation`：PageIndex 是已开源并可本地运行的实现（github.com/VectifyAI/PageIndex），非纯概念。

## 拆卡决策
与 OpenKB 设计哲学（为何不用 RAG/向量）和双层架构（系统如何组织）分离。本卡聚焦 PageIndex 的技术机制（怎么做到无向量检索）。
