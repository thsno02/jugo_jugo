# v1 主题骨架归档

这个目录保存 2026-05-24 产出的 8 节点 LLM Wiki v1 主题骨架。

它已经通过当时的最终 QA：

- 8 个已采纳节点
- 8 个 KB 视图
- 185 条引用边
- `impact_queue_open=0`
- 节点/知识卡校验器通过
- 脚注布局门禁通过

但它现在被降级为旧产物，因为它不符合新的核心目标。

## 为什么归档

本轮真正应该生产的是自下而上的原子事实知识卡。实际产物却是自上而下的主题节点：

1. `origin/canon`
2. `working definition`
3. `architecture`
4. `workflow`
5. `vs-RAG/write-loop`
6. `risks/governance/provenance`
7. `implementation ecosystem`
8. `evaluation/evidence`

这些节点可以作为注意力地图，但不是扎实的原子事实基础。

## 主要问题

- 候选主题被当成生产单元。
- 来源支持的观察被压缩进 evidence matrix，再服务于枢纽页综合。
- 知识卡像综合报告，不像 zet 风格知识卡。
- 出处论证和审计残留过度靠近知识卡阅读层。
- 最终 QA 用主题覆盖判断 v1，而不是原子事实可靠性。
- sub-agent 循环周期过重，控制面成本过高。

## 保留内容

- `nodes/`：8 个已采纳主题节点。
- `kb/`：8 个已采纳视图知识卡。
- `generated/`：引用图、反向链接、影响队列、状态。
- `llm_wiki_runtime/`：原 `.llmwiki/`，已改为可见目录，包含 control、runs、skills。
- `reports/`：本轮报告。
- `protocol/`：本轮使用过的旧协议和循环文件。

## 如何使用这个目录

可以读它来了解哪里跑偏了，也可以用它作为未来枢纽页/注意力地图的参考。

不要继续在这里新增主题节点。下一轮应在 `llm_wiki/` 里做原子事实生产。
