## Justification: memgpt-archival-recall-storage

**为何提取此卡**: archival storage 和 recall storage 是 MemGPT 外部上下文的具体实现，各有不同的设计目的（长期知识存储 vs 消息历史/swap）。论文中两者在实验中扮演不同角色：archival 用于 doc QA 中的文档库，recall 用于 DMR 中的对话历史检索。

**原子性判断**: 与 memory-hierarchy（总体架构描述）和 main-context-structure（内部结构）分离。此卡专注外部存储的双系统设计及其各自职责。

**Evidence basis**: experimental_paper -- 方法描述加实验中的具体使用。
