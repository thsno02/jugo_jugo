# 入库机制（Ingestion Mechanism）

## Recall 目标

这个专题回答一份 raw material 如何变成 LLM Wiki knowledge object，以及每个版本为什么重写上一版。稳定的八个节点只是跨版本坐标；页面同时保留当时规定的流程（specified）、实际执行（executed）、用户反证（observed failure）和后验解释（retrospective），不会用最终文档覆盖历史。

## 为什么 V5 先做 Demo

V5 同时拥有最完整的结构产物和最明确的质量反证：source router、487/488 drafts、477 active cards、fusion、YAML 与 graph audit 都能找到 artifact，但用户仍能用具体卡片证明“有 citation、没有知识展开”。它因此适合先验证 recall 模型是否能区分结构完成、合同执行和知识成功，而不是因为 V5 天然代表最佳实践。

## V0-V5 演化主线

| 版本 | 核心生产对象 | 主要改变 | 暴露的问题 |
|---|---|---|---|
| V0 | versioned meta node | 跑通 provenance、adoption、view 与 impact graph | 把“如何建 KB”错当成 LLM Wiki topic |
| V1 | top-down topic hub | source mining、frontier、candidate、audit、adoption 分段 | 目标仍不是 bottom-up atomic card，周期长且不可读 |
| V2 | accepted atomic/scoped card | 逐卡强 gate，后期明确 Top-3 comparison 与轻 schema | 7 小时只产 15 卡；最终设计晚于既有产物 |
| V3 | batch-first draft card | 先穷举 drafts，再比较、链接和 adoption | comparison 硬编码 V2；171 张 V3 卡没有 self-dedup |
| V4 | Q&A card / direct accepted card | seed 验证角色分离，full batch 扩大吞吐，后期引入 FSJS | 全量折叠角色并直写 KB；source route、fusion、graph 均靠发布后补救 |
| V5 | routed draft + scripted ingest | source-type router、deterministic ingest、机械图审计 | 完整 skills 未传给执行节点；结构成功掩盖知识空壳 |

## 稳定主链

```text
来源进入与阅读面
  → 材料读取与知识提取
  → 知识对象生产
  → 入库与 Promotion Gate
  → 比较、Fusion 与边界判断
  → 关系治理与图修复
  → 验收、固化与发布
  → 失败反馈与重提取实验
```

这条链不是“V0 当时就拥有八个节点”。例如 V0-V2 没有 questioning loop，V0-V1 没有 fusion，V4 也只在 seed 阶段真实执行 promotion。节点详情中的 Version Evolution（版本演化）才是事实层。

## 跨版本结论

- 生产对象比流程完备度更先决定成败：V0、V1 都是“错误目标被完整执行”。
- 吞吐优化会改变证据形态：V2 的逐卡 ledger 很重，V3 的 batch-first 很快，却把 set-level fusion 做错。
- 设计文件存在不等于执行节点收到完整合同：V4、V5 都出现 skill 可访问但 prompt 被压缩的情况。
- publication 只证明可见性与版本化；root stable product 需要独立 human promotion。
- source path、citation、YAML 和 graph health 都是必要条件，不是 knowledge quality 的替代指标。
- failure-feedback 必须保留原始快照和用户纠错链，不能用后验 repaired snapshot 反推原 pipeline 成功。

## 证据边界

当前专题已覆盖 V0-V5 的八阶段演化，并链接 query events 与 repository artifacts。它是机制级 recall，不是逐工具调用 replay；同一版本内部的 seed、full batch 与 remediation 等 runtime shape 通过阶段证据和 known gaps 保留，不被压成单一成功叙事。
