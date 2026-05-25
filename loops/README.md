# Loop Capsules

这个目录保存所有 loop capsule。`legacy` 不再是一个顶层目录语义；一个 loop 是否已经过期、关闭、废弃或可恢复，由它自己的 metadata 决定。

## Repository Contract

仓库根目录目前不保存 promoted stable `llm_wiki/` 产品。

当前阶段只有实验 loop 和候选产物：

- `loops/<loop_id>/`：一轮实验 loop 的完整 capsule。
- `loops/<loop_id>/outputs/`：该 loop 生产出的候选产物。
- `loops/current_loop.json`：当前 active loop 指针；没有 active loop 时为 `null`。
- `loops/registry.json`：所有已登记 loop 的状态索引。

不要通过移动目录来表达 archive。结束一个 loop 时，只更新该 loop 的 `status.json` 和 `loops/registry.json`。

## Capsule Contract

每个 loop capsule 至少应该提供：

- `manifest.json`：loop capsule 的稳定入口 metadata。
- `status.json`：active / archived / abandoned / promoted 等状态。
- `INDEX.md`：人类可读索引，说明该 capsule 内部结构。

除此之外，loop 内部结构可以自由演化。`iterations/`、`brains/`、`mailbox/`、`snapshots/`、`outputs/` 等都只是某一轮实验的内部事实，不是仓库级固定规范。

## Registered Loops

### v0_meta_kb_initialization_demo_20260524

路径：`loops/v0_meta_kb_initialization_demo_20260524/`

状态：`archived`

问题：

- 把“如何生产 KB 的机制”误当成了 LLM Wiki 主题本身。
- 内容是“生产机制”的元 KB，不是目标主题 KB。
- 可以证明版本束、引用、出处论证、影响队列等工程机制能跑通，但不能证明知识生产方向正确。

### v1_topic_hub_skeleton_20260524

路径：`loops/v1_topic_hub_skeleton_20260524/`

状态：`archived`

问题：

- 核心生产对象错了，把原子事实知识卡跑成了主题/枢纽节点。
- 采用自上而下的主题覆盖，而不是自下而上的事实生产。
- 知识卡写作像中间流程产物，不像可读的 zet 风格原子事实知识卡。
- 出处论证、审计、发布流程的痕迹侵入了知识卡，导致人类审计和阅读体验变差。

### v2_llm_wiki_loop_20260525

路径：`loops/v2_llm_wiki_loop_20260525/`

状态：`archived`

这是一轮已经关闭的 LLM Wiki loop。它包含：

- loop docs / state / manifest；
- iterations、decisions、audits、reports、queues；
- brain mailbox、hooks、tools、logs；
- system prompts 和 task templates；
- `outputs/llm_wiki/` 候选 KB 产物；
- `snapshots/` 内部控制面快照。

该 loop 的 `outputs/llm_wiki/` 不是 promoted stable 产品。只有明确的人类 promotion decision 才能把候选产物发布到仓库根目录的稳定 `llm_wiki/`。
