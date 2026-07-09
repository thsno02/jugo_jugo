# Justification: llm-wiki-write-loop-vs-static-rag

## 为什么产出此卡
"这只是 RAG" 的辩论是本帖最核心的技术争议之一，darkhanakh 和 kenforthewin 的交锋清晰地界定了 write loop 作为区别点。这是理解 LLM Wiki 技术定位的基础卡。

## 证据强度
- 来自多位技术从业者的对辩，观点明确且对立
- darkhanakh 和 kenforthewin 各自有开源项目背景
- hombre_fatal 补充了原帖 /raw 目录设计的技术细节
- evidence_basis 取 community_discussion

## 边界与局限
- "RAG" 的定义边界本身有争议（是否包含写循环）
- 讨论未触及 write loop 的具体实现质量和 failure mode
- lint pass 的规模化问题（N*N 比较）在另一条线程中被提出但未解决
