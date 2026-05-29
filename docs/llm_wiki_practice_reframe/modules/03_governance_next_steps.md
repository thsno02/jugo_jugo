# 模块说明

本模块建议替换 `final.md` 中第 6.2-6.6 节，并整体替换第 7 章“当前风险与待处理事项”和第 8 章“下一步计划”。如果主文档希望保持现有第 6 章编号，也可以将“治理判断”部分插入在 6.4 之后，将“风险与下一步”部分替换原第 7-8 章。

## 治理判断：LLM Wiki 不是 truth warehouse

当前阶段最重要的判断是：LLM Wiki 不应被设计成一个宣称保存“最终真理”的 truth warehouse，而应被设计成一套 knowledge governance system。它的价值不在于把所有材料压缩成一组静态结论，而在于持续管理知识如何从来源材料进入候选态、如何被检查、如何被采纳、如何被修订，以及在什么条件下可以被提升为稳定知识。

很多 LLM Wiki 相关知识都不是单一、永久、无上下文的事实，而是带有适用范围、证据强弱、解释视角和时间变化的判断。因此，系统不应过早消除差异，也不应把冲突和边界视为失败。更合理的目标是让每个重要判断都能被追溯、被比较、被质疑和被更新。换言之，可信度不是来自“系统声称它正确”，而是来自治理链条能够说明它为什么暂时可用、边界在哪里、未来如何被推翻或修订。

在这个定位下，card 是主要的阅读和维护单元，但 card 不等于机械的 claim 切片。过度追求 atomic claim 会牺牲可读性，也会把系统推向高维护成本的 knowledge graph。更合适的分层是：card 承担面向人和 agent 的可读知识表达；claim 是 card 内部可被审计的主张；provenance、conflict、boundary 和 comparison 是治理层，用来说明证据、张力、适用范围和与既有知识的关系。

这意味着一张合格的 card 不只是“写得像一段知识”，而是一个 scoped knowledge unit：它有明确问题域，有可理解的结论，有来源依托，也有边界意识。claim/provenance/conflict/boundary 不应替代 card 成为阅读主体，而应围绕 card 形成可检查的治理外壳。

## 治理链条中的关键角色

provenance 是知识可信度的一部分，不是附录或事后记录。它负责说明 card 的判断依据、证据强弱、适用边界，以及这些判断为什么可以进入候选知识库。没有 provenance 的 card 即使语言流畅，也只能算内容草稿，不能算可信知识单元。

similarity / comparison 的作用不是简单去重，而是防止候选知识库在增长过程中积累重复、冲突和隐性分叉。similarity 负责召回可能重叠的既有知识，comparison 负责判断新内容到底是 new card、provenance delta、merge candidate，还是 duplicate skip。这个环节的核心价值是让新增知识必须与已有知识发生关系，而不是孤立进入库中。

publication gate / fusion audit 是从 draft 到 candidate accepted card 的质量门。它们不应被理解为形式化审批，而是对证据、边界、重复、冲突和可读性的综合检查。publication gate 更适合处理明显可独立采纳的新卡；fusion audit 更适合处理与既有知识发生重叠、补充或合并关系的卡。

promotion decision 则是另一个层级的判断：它不决定单张 card 是否写得合格，而是决定一个 candidate KB 是否可以从候选产物提升为稳定产品。当前 v3 已经形成 candidate-ready KB，但这仍不等于 root 级 stable product。只有经过明确的人类 promotion decision，v3 才应被视为对外稳定知识库的一部分。

## Claude v3 的 citation / related 新洞察

v3 复盘中进一步澄清了 references、footnotes、card citation 和 related 的边界。这里的关键变化是：citation 不应只指向 raw source，也应允许指向 knowledge card；card 本身也应该成为 cite-able object。

更合理的模型是：references 表示 card-level 的 broad dependency，即一张 card 在整体论述上依赖哪些来源或背景材料；footnotes 表示 inline citation，用于支撑正文中的具体句子、判断或例子；card citation 表示知识卡之间的引用关系，让一个已治理的知识单元可以成为另一个知识单元的依据、补充或对照。

在这个模型下，related 不应长期作为一组独立手工维护的边。related 更适合被视为从 footnotes、card citation 和 citation graph 中派生出来的 metadata，用于导航、聚类、Obsidian 展示和后续分析。这样可以避免同一组关系在正文引用、脚注、metadata 和双链中被重复维护，也能让 related 更接近真实知识依赖，而不是人工补上的主题相似度标签。

因此，后续 citation 设计的重点不是再增加一层关系字段，而是统一 raw source citation、card citation、references、footnotes 和 related metadata 的职责：正文负责表达，footnotes 负责局部证据，references 负责整体依赖，citation graph 负责可分析关系，related metadata 负责派生导航。

## 当前风险与待处理事项

第一，v3 candidate KB 尚未 promotion。当前 171 张卡已通过 publication gate 或 fusion audit，并进入 candidate-ready 状态，但这仍是候选知识库状态。若没有明确 promotion decision，后续汇报和使用都应继续把它视为可审核、可提升的候选产物，而不是稳定发布版。

第二，similarity 仍存在 miss 风险。当前 comparison provenance 已经消化一部分重复和重叠问题，但仍有 3 个已知 similarity miss 需要定向比对。这类问题的风险不只是“漏掉重复卡”，还包括新卡没有正确继承既有 card 的 provenance、boundary 或 conflict，从而造成知识图谱中的隐性分叉。

第三，empty source 和 upstream blocked source 仍需后续处理。当前有一批来源因为本地内容为空或上游状态未就绪而没有进入本轮生产。它们不应阻塞 v3 promotion 判断，但需要保留为后续增量生产的输入，否则 candidate KB 的覆盖边界容易被误读为完整覆盖。

第四，citation / related metadata 仍需统一。v3 已经形成较密集的 related / interlink 网络，但 related 的长期维护方式需要调整。如果 related 继续独立手工维护，后续会同时带来重复劳动、关系漂移和 citation graph 不一致的问题。card citation 模型需要在下一阶段成为治理规范的一部分。

第五，治理规则仍需继续校准。card 粒度、claim 粒度、conflict 表达、boundary 表达、comparison 判定和 promotion 标准已经足以支撑下一步，但还不能视为最终规范。后续每一次增量生产都应同时验证内容产出和治理规则是否仍然有效。

## 下一步计划

短期优先级应集中在四件事上。

1. 完成 v3 candidate KB 的 promotion decision。需要由人工判断当前 candidate-ready KB 是否可以提升为稳定产品，或是否需要先完成补充审计后再 promotion。
2. 对 3 个已知 similarity miss 做定向比对。重点不是单纯确认是否重复，而是判断是否需要补充 v2 anchor、增加 provenance delta、合并边界说明，或修正 comparison 判定。
3. 设计统一的 card citation 模型。该模型需要明确 raw source citation、card citation、references、footnotes 和 related metadata 的职责边界，并将 related 调整为尽量从 citation graph 派生。
4. 建立后续增量生产节奏。empty source 和 upstream blocked source 应进入补齐队列；新来源进入生产时，应继续沿用 draft、provenance、similarity / comparison、gate / audit、promotion 的治理链条。

中期重点是把 v3 已验证有效的流程从一次性 production pass 转化为稳定的知识生产机制。后续不只是继续生成更多 card，而是要验证：新增 card 是否能自然接入既有 citation graph，similarity miss 是否下降，promotion 标准是否更清晰，related metadata 是否能从引用关系中稳定派生，以及候选知识库是否能在持续增长中保持可读、可追溯和可审计。

因此，下一阶段的核心目标不是证明“agent 能继续生成内容”，而是证明 LLM Wiki 可以在持续增量中保持治理能力：新增知识能被定位，旧知识能被修订，冲突能被保留，边界能被说明，候选产物能被明确提升或暂缓。
