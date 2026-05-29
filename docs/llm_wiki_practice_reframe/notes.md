# LLM Wiki 实践复盘写作 Notes

本文件是写作备忘，不是正式交付物。正式交付见 `final.md`。

## 取材来源

- 当前 repo 状态：
  - root README：当前没有 promoted stable `llm_wiki/` 产品。
  - loop registry：v0/v1/v2 archived，v3 active。
  - v3 status / report：当前 active phase 为 `adoption_complete`，product status 为 `candidate_ready`；下一步是由人判断是否 promote v3 candidate KB 到 root `llm_wiki/`。
- user-insights：
  - 记录了用户对目标、语言、bottom-up、card/provenance、main-agent 控制面、文件管理、审计机制等关键纠偏。
  - 已补充 Claude v3 执行会话中的用户输入，包括全文读取、批量处理全部材料、中文主语言、interlink 前置、以及 related/citation 边界。
  - coverage 标记为 mixed，因此写作时不声称覆盖完整聊天，只提炼当前可见脉络。
- 链接 A：
  - 主题是把静态 LLM Wiki coverage framework 转成可执行 agent loop。
  - 关键点：framework 不能只是静态 Markdown，要变成 source、claim、coverage、audit、judgment gate 的运行约束。
- 链接 B：
  - 主题是 knowledge governance、truth、conflict、claim/card 粒度、knowledge graph 的维护成本。
  - 关键点：LLM Wiki 不应是 truth warehouse，而应是 claim/card/provenance/conflict/boundary/revision 的治理系统。

## 关键用户输入脉络

- 核心目标是生成 LLM Wiki topic 的 KB，而不是讨论如何生产这个 KB 的 meta topic。
- topic plan 只是建议，不是可执行单元；知识需要从 papers、webpages、threads、repos 等 sources 里挖掘。
- 最初交付物同时包括 skills 和完整知识库；skills 是生产 KB 的工具，不是替代交付物。
- main-agent 应作为控制面和决策者，保持上下文干净，不亲自做批量来源挖掘、写卡、审计和采纳。
- 当前阶段应 bottom-up：先生长 atomic / scoped cards，再逐步形成 hub、topic、cluster。
- card 应该像 zettelkasten card 一样可读，不应是不可读的中间状态。
- provenance 是 justify card as fact / knowledge 的过程，是可读 artifact，不是简单日志。
- `References` 应在 `Footnotes` 前，`Footnotes` 放最后，避免 Markdown 渲染问题。
- 当前网络环境有限，retrieve 失败应有限尝试、记录、暂时搁置，不应阻塞主流程。

## Claude v3 执行会话新增洞察

- v3 是第一轮正式 production pass，应以 v3 文件和当前 report/status 为 source of truth，不依赖早期对话上下文。
- draft-first 不是抽样实验：当 agent 只产出 4 张卡时，用户明确要求继续处理全部材料，说明吞吐和覆盖是 v3 的核心目标。
- 用户要求所有输出以中文为主，后续文档和知识卡都应默认中文表达，保留必要英文术语。
- 因当前 context window 足够大，执行时应全文读取来源材料；过度分页或只读开头会漏掉关键论点，影响 card coverage。
- adoption 之前需要先做 interlink，因为知识库不是一组孤立卡片，card 之间的可导航关系也是候选 KB 的一部分。
- raw sources 之外，knowledge cards 本身也应逐渐成为可引用对象；这意味着 cite-able objects 从“原始资料”扩展到“知识库内部卡片”。
- `related` 不应长期作为独立手工维护关系层，而应从 footnotes / citation graph 中提取，再写入 metadata，服务 Obsidian 和脚本消费。

## 阶段判断

### v0

- 价值：证明机制可跑通。
- 问题：把“知识库生产机制”误当成 LLM Wiki 主题本身。
- 写作定位：机制 demo，有审计价值，不是目标知识库。

### v1

- 价值：形成 8 个 LLM Wiki 主题节点，可作为注意力地图。
- 问题：top-down topic/hub skeleton，替代了 bottom-up card 生长。
- 写作定位：方向校准前的主题骨架实验。

### v2

- 价值：验证 scoped knowledge card 的 production chain。
- 结果：15 张 accepted cards。
- 问题：流程太重、吞吐较低，部分卡片过原子或像标题复述。
- 写作定位：小规模链路验证。

### v3

- 价值：draft-first，提高吞吐，把 expensive reasoning 后移；在 adoption 前补上 interlink，让候选 KB 不是孤立卡片集合。
- 当前结果：
  - 72 条来源全部完成一轮处理；
  - 43 条来源 drafted；
  - 22 empty source；
  - 7 upstream pending/blocked；
  - 171 draft cards；
  - 171 draft provenance；
  - 171 similarity；
  - 171 comparison provenance；
  - 163 new_card；
  - 8 provenance_delta；
  - 163 张 new card 通过 publication gate；
  - 8 张 provenance delta 通过 fusion audit；
  - 171 张 accepted cards；
  - 171 份 accepted provenance；
  - 974 related/interlink；
  - 0 orphan cards；
  - 0 dangling ids；
  - 8 张 cards 带有 v2_anchor；
  - product status 为 `candidate_ready`。
- 写作定位：规模化候选产物已经完成首轮 adoption，形成 candidate-ready KB；但它仍未 promote 到 root stable product。

## final.md 写作策略

- 不使用本地路径做理解前提。
- 不列太多文件名。
- 不展开 worker、hook、CLI、JSON/XML。
- 用“阶段演变 + 原则变化 + 当前结果”的叙事方式。
- 让读者理解为什么当前结果已经是 v3 candidate-ready KB，但还不是 root stable product。
