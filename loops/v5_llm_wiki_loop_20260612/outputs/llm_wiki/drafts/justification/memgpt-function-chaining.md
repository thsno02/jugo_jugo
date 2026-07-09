## Justification: memgpt-function-chaining

**为何提取此卡**: 函数链（function chaining）是 MemGPT 实现多步检索的核心控制流机制，区别于普通的单次函数调用模式。request_heartbeat=true 是该论文独创的实现方案，在实验中直接决定了嵌套 KV 检索和文档 QA 的性能表现。

**原子性判断**: 函数链是一个独立的控制流概念，与内存层级（结构性概念）和队列管理器（数据流管理）有关联但在机制层面是独立的。

**Evidence basis**: experimental_paper -- 论文既描述了机制设计，也通过嵌套 KV 实验验证了其有效性。
