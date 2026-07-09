## Justification: memgpt-event-driven-control-flow

**为何提取此卡**: 事件驱动控制流是 MemGPT 区别于普通聊天 LLM 的关键架构特征。它使系统能在无用户输入时自主运行（如定时整理记忆），并通过 memory pressure 系统消息实现主动内存管理。论文明确将其与 OS 中断类比。

**原子性判断**: 这是控制流层面的概念，与内存结构（是什么）和函数链（如何多步执行）分离。事件驱动回答"何时触发"的问题。

**Evidence basis**: experimental_paper -- 方法设计加实验评估。
