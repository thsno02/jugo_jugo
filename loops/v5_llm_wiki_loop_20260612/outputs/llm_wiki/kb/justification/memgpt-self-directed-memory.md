## Justification: memgpt-self-directed-memory

**为何提取此卡**: 自主内存编辑是 MemGPT 的核心设计理念 -- LLM 自己决定何时何物进出上下文，无需用户干预。这区别于传统 RAG 中由外部系统控制检索的被动模式。论文明确用 "self-directed" 命名该特性并详细阐述其实现。

**原子性判断**: 与 function chaining 不同（后者关注多步调用的控制流），此卡关注的是"LLM 作为自身内存管理者"这一设计哲学及其闭环反馈实现。

**Evidence basis**: experimental_paper -- 方法描述结合实验验证。
