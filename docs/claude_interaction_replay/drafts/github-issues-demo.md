# LLM Wiki GitHub Issues 草稿 Demo

> 状态：仅本地草稿（draft only），未提交到 GitHub。

## 建议的 Issue 数据合同

一条 Issue 应对应一个可以独立阅读的“问题 → 决策 → 落实 → 结果”闭环，而不是一条聊天消息，也不应粗到覆盖整个版本。建议固定保留以下字段：`Title` 用于检索；`Question` 还原用户真正要解决的问题；`Context` 提供回忆现场；`User Signals` 保留 1-3 条脱敏原话；`Decision` 记录取舍；`Implemented Solution` 概括落实方式；`Outcome/Evidence` 指向仓库证据；`Why This Matters` 解释长期价值；`Open Questions` 防止把阶段结果写成终局；`Suggested Labels` 支持分类；`Version/Timeline` 和 `Source Events` 负责追溯。

---

## Issue 1

### Title
建立以覆盖率驱动的 LLM Wiki 原始资源库，而不是先写结论

### Question
怎样先建立足够全面的原始知识库（raw knowledge database），并持续发现证据缺口？

### Context
项目最初并不是直接生成知识卡，而是从 Karpathy 的相关讨论出发，收集论文、博客、代码仓库和社区讨论。用户随后纠正了静态采集计划，要求由覆盖框架持续驱动补充来源。

### User Signals
- “当前阶段的调研，只需要聚焦于【资源获取】……作为一个 raw knowledge database。”（`codex:codex-prehistory-research:H001`）
- “根据第一性原理罗列出来，llm wiki 这个 topic，需要 cover 哪些 facts 和 aspects。”（`codex:codex-prehistory-research:H004`）
- “plan 的核心逻辑是根据 coverage 不断去寻找信息，直到当前的 data 足够满足 coverage。”（`codex:codex-prehistory-research:H009`）

### Decision
把来源采集设计为覆盖率驱动（coverage-driven）的循环：先定义应覆盖的事实和方面，再审计现有材料缺口并继续采集。

### Implemented Solution
建立本地来源池，并在后续 v1 中形成覆盖框架（coverage framework）、证据矩阵（evidence matrix）和来源缺口审阅。

### Outcome/Evidence
- `data/`
- `loops/v1_topic_hub_skeleton_20260524/reports/coverage_framework.md`
- `loops/v1_topic_hub_skeleton_20260524/reports/evidence_matrix.md`

### Why This Matters
它把“搜到一些资料”升级成可检查的证据建设过程，也奠定了后续来源追踪和材料穷尽的基础。

### Open Questions
- 覆盖率何时可以判定“足够”？
- repo、论文与社区讨论应采用相同还是不同的覆盖标准？

### Suggested Labels
`area:ingestion`, `type:decision`, `version:v0`, `theme:coverage`

### Version/Timeline
v0 前史，2026-05-21。

### Source Events
`codex:codex-prehistory-research:H001`, `H004`, `H009`

---

## Issue 2

### Title
arXiv 论文优先保存 TeX，避免以 PDF 作为智能体主要阅读面

### Question
面向智能体消费论文时，应优先保存 PDF，还是尽可能获取结构更清晰的 TeX？

### Context
原始资源库主要供智能体读取。用户观察到 PDF 解析成本高且结构容易丢失，因此改变了论文下载策略。v4 再次发现把 TeX 转成混乱的 TXT 属于不必要的降质步骤。

### User Signals
- “pdf 论文是不好解析的，但是 tex 是好解析的……尽量去下载 tex 而不是 pdf。”（`codex:codex-prehistory-research:H003`）
- “期望是直接消化 tex 文件了……这个 txt 是明确的错误。为什么要多此一举呢？”（`claude_code:claude-primary-v4:H048`）

### Decision
论文采集优先 TeX；保留原始结构并让 reader 直接消费，不把 TXT 转换当成默认中间层。

### Implemented Solution
重新下载论文来源，并在 v4 数据管线审计中将 TeX 处理、网页转 Markdown 和 repo 专用解析拆成不同问题。

### Outcome/Evidence
- `loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/data_collection_fix_plan.md`
- `loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/pipeline_gaps_report.md`

### Why This Matters
来源格式决定可读取的证据表面（evidence surface）；错误的预处理会在知识提取前永久损失结构和可读性。

### Open Questions
- TeX 缺失时，PDF fallback 应采用什么解析与质量门禁？
- 数学公式、图表和附录怎样进入统一读取面？

### Suggested Labels
`area:ingestion`, `type:bug`, `version:v0`, `version:v4`, `source:paper`

### Version/Timeline
v0 前史提出，v4 管线审计再次确认；2026-05-21 至 2026-06-04。

### Source Events
`codex:codex-prehistory-research:H003`, `claude_code:claude-primary-v4:H047`, `H048`, `H049`

---

## Issue 3

### Title
纠正 v0 的主题漂移：机制验证不能替代 LLM Wiki 内容建设

### Question
当知识生产机制已经跑通，但生成的知识主题变成了“如何建设知识库”本身，应该怎样纠偏？

### Context
v0 成功验证了文件系统版本包、来源追踪、引用图和影响队列，却把生产机制误当成了 LLM Wiki 的主题内容。结构上成功，产品目标上失败。

### User Signals
- “这个 repo 的目的是，对 llm_wiki 进行全面的网络调研。”（`codex:codex-prehistory-research:H001`）
- “需要 cover 哪些 facts 和 aspects。”（`codex:codex-prehistory-research:H004`）

### Decision
保留 v0 的可审计机制，但停止把 meta-KB 机制当作知识主题；下一轮直接围绕 LLM Wiki 本身组织内容。

### Implemented Solution
v1 建立 8 个 LLM Wiki 主题枢纽，并加入 coverage framework、evidence matrix 和主题 QA。

### Outcome/Evidence
- `loops/v0_meta_kb_initialization_demo_20260524/kb_initialization_demo_report.md`
- `loops/v1_topic_hub_skeleton_20260524/README.md`
- v0：7 个 adopted nodes、35 条 citation edges；v1：8 个主题视图、185 条 citation edges。

### Why This Matters
它揭示了一个通用风险：流程指标全部通过，并不代表系统正在生产正确的对象。

### Open Questions
- 如何在 loop 启动前验证“机制目标”和“内容目标”没有混淆？
- 主题正确性应由用户、评审智能体还是证据覆盖共同判定？

### Suggested Labels
`type:postmortem`, `version:v0`, `version:v1`, `theme:topic-drift`

### Version/Timeline
v0 → v1，2026-05-24。

### Source Events
`codex:codex-prehistory-research:H001`, `H004`

---

## Issue 4

### Title
从主题枢纽切换到来源驱动的限定范围知识卡

### Question
知识生产单元应该是预先规划的 hub，还是从来源中自底向上生长的 scoped knowledge card？

### Context
v1 的 8 个主题枢纽通过了覆盖 QA，但卡片更像综合报告。用户明确要求 loop 生产知识卡，而不是继续聚合 hub，也不预设 card topic。

### User Signals
- “没有约定 card topic……card 的生产完全是 agent 的自主探索。”（`codex:codex-primary-v0-v2-boundary:H046`）
- “loop 的核心是生产知识卡片，而不是聚合知识 hub。”（`codex:codex-primary-v0-v2-boundary:H047`）

### Decision
取消 taxonomy / hub 作为前置生产目标；从原始来源发现 scoped cards，允许卡片有依赖，但要求范围可辨、可独立消费和可追溯。

### Implemented Solution
v2 建立 card contract、来源挖掘、draft、provenance、独立审计与 adoption 流程。

### Outcome/Evidence
- `loops/v2_llm_wiki_loop_20260525/CARD_CONTRACT_V2.md`
- `loops/v2_llm_wiki_loop_20260525/LOOP_DESIGN_V2.md`
- `loops/v2_llm_wiki_loop_20260525/reports/loop_report.md`

### Why This Matters
生产单元决定系统优化方向：hub 优化覆盖叙事，scoped card 优化局部可靠性、复用和演化。

### Open Questions
- scoped 的可操作判定标准是什么？
- 卡片何时应保留为上层 card，何时才需要拆分？

### Suggested Labels
`area:knowledge-model`, `type:architecture`, `version:v2`, `theme:scoped-card`

### Version/Timeline
v1 → v2，2026-05-24 至 2026-05-25。

### Source Events
`codex:codex-primary-v0-v2-boundary:H046`, `H047`, `H048`

---

## Issue 5

### Title
用上下文隔离和生命周期规则治理 sub-agent 协作

### Question
长程 loop 中，怎样既避免 sub-agent 泛滥和上下文污染，又不因过度关闭 worker 而反复支付读取成本？

### Context
v2 早期出现大量 sub-agent 长期 active、边界不清和重复 I/O。用户同时指出，简单地“一次性关闭所有 worker”也可能浪费上下文，应区分常驻 brain、一次性 worker 和独立审计者。

### User Signals
- “注意管理 sub-agent 的生命周期。这是很重要的一点。”（`codex:codex-primary-v2-v3-handoff:H002`）
- “是否过度管理了？比如有一些 sub-agent 可以 alive 常驻的。”（`codex:codex-primary-v2-v3-handoff:H003`）
- “哪些 sub-agent 是必要的，哪些是不必要的。”（`codex:codex-primary-v0-v2-boundary:H050`）

### Decision
主代理负责决策与调度；worker 只能读取明确范围；以 task packet、marker、mailbox 和生命周期状态显式传递上下文；高复用角色可常驻，一次性任务及时关闭。

### Implemented Solution
形成上下文隔离（context isolation）、sub-agent lifecycle、任务模板和 mailbox/queue 的设计与审计文档。

### Outcome/Evidence
- `loops/v2_llm_wiki_loop_20260525/CONTEXT_ISOLATION.md`
- `loops/v2_llm_wiki_loop_20260525/SUBAGENT_LIFECYCLE.md`
- `loops/v2_llm_wiki_loop_20260525/audits/20260525-subagent-lifecycle-session-audit/lifecycle_audit.md`

### Why This Matters
智能体协作结构本身会改变知识质量、成本和可恢复性；它不是单纯的运行时细节。

### Open Questions
- 哪些指标可以判断一个 worker 值得常驻？
- mailbox 如何避免旧任务、重复唤醒和跨角色信息污染？

### Suggested Labels
`area:agents`, `type:architecture`, `version:v2`, `theme:context-isolation`

### Version/Timeline
v2，2026-05-24 至 2026-05-25。

### Source Events
`codex:codex-primary-v0-v2-boundary:H042`, `H050`, `codex:codex-primary-v2-v3-handoff:H002`, `H003`, `H014`, `H018`

---

## Issue 6

### Title
将知识卡生产改为 draft-first，解决 7 小时仅产出 15 张卡的吞吐瓶颈

### Question
怎样在不放弃 provenance 和审计的前提下，提高知识卡生产吞吐？

### Context
v2 的强控制串行流程耗时 7 小时只得到 15 张卡。用户判断瓶颈来自“每张卡立即融合、审计、入库”，提出先消费材料形成草稿，再统一比较与收敛。

### User Signals
- “7h，你总结出来 15 条 card？这效率疑似有点太低了吧。”（`codex:codex-primary-v2-v3-handoff:H004`）
- “先去把所有的 raw material 都跑一遍，生成 draft card 之后，然后再进行融合？”（`codex:codex-primary-v2-v3-handoff:H005`）

### Decision
采用草稿优先（draft-first）：材料先转成知识密集草稿，之后再做相似比较、融合判断、审计和发布。

### Implemented Solution
v3 建立 material → draft → similarity → comparison provenance → publication/fusion gate 的批处理管线。

### Outcome/Evidence
- `loops/v3_llm_wiki_loop_20260525/CARD_CONTRACT_V3.md`
- `loops/v3_llm_wiki_loop_20260525/reports/loop_report.md`
- 约 171 张卡进入 accepted 状态。

### Why This Matters
它把探索速度与发布质量解耦，使系统可以先形成候选空间，再用治理流程收敛。

### Open Questions
- draft 数量增长到更大规模时，融合成本怎样保持可控？
- 哪些门禁必须逐卡执行，哪些适合批处理？

### Suggested Labels
`area:pipeline`, `type:performance`, `version:v3`, `theme:draft-first`

### Version/Timeline
v2 → v3 前置决策，2026-05-25。

### Source Events
`codex:codex-primary-v2-v3-handoff:H004`, `H005`, `H006`

---

## Issue 7

### Title
用 Top-3 相似卡与 comparison provenance 约束融合决策

### Question
新草稿出现后，怎样轻量找到潜在重复项，并留下“为何融合或保留”的可审计依据？

### Context
全库语义比较成本过高，但只凭标题或直觉融合会丢失差异。用户要求先召回少量候选，再回答共同点、差异和下一步依据三个问题。

### User Signals
- “similarity 的 check，这里应该有一个机制。”（`codex:codex-primary-v2-v3-handoff:H007`）
- “标题用结巴分词之后，用 jacord……直接给 top 3 做比较。”（`codex:codex-primary-v2-v3-handoff:H008`）
- “为什么认为和 A 卡有共同点？和 A 的不同在哪里？进行下一步操作的核心依据是什么？”（`codex:codex-primary-v2-v3-handoff:H006`）

### Decision
用标题 Jieba 分词 + Jaccard 作为低成本 Top-3 候选召回；相似度只负责找候选，最终 fusion / distinct 决策由全文比较和 provenance 支撑。

### Implemented Solution
在 v3 pipeline 中加入 Top-3 similarity、三问 comparison provenance 和 publication/fusion gate。

### Outcome/Evidence
- `loops/v3_llm_wiki_loop_20260525/CARD_CONTRACT_V3.md`
- `loops/v3_llm_wiki_loop_20260525/audits/`
- `loops/v3_llm_wiki_loop_20260525/reports/loop_report.md`

### Why This Matters
它明确区分了召回（recall）与判断（judgment）：相似不等于重复，算法分数不能替代知识决策。

### Open Questions
- 反义、冲突和概念别名怎样进入候选召回？
- Top-3 在卡片规模继续扩大时是否仍有足够召回率？

### Suggested Labels
`area:retrieval`, `type:architecture`, `version:v3`, `theme:provenance`

### Version/Timeline
v3 前置设计，2026-05-25。

### Source Events
`codex:codex-primary-v2-v3-handoff:H006`, `H007`, `H008`

---

## Issue 8

### Title
提高知识卡信息密度，并将稳定 metadata 与自由正文分离

### Question
怎样避免知识卡退化成标题复述，同时保留后续治理所需的结构化字段？

### Context
v3 设计时，用户发现卡片虽然“原子”，但缺乏知识含量；过强正文模板又会压平不同类型的知识。

### User Signals
- “card 太【atomic】了，没有【信息量】……如果只是 title 的 restate 或者 paraphrase，没有意义。”（`codex:codex-primary-v2-v3-handoff:H008`）
- “card 本身是知识……最重要的应该是：knowledge 本身。”（`codex:codex-primary-v2-v3-handoff:H009`）
- “metadata 可以是确定的模版……正文部分倾向于没有固定的模版。”（`codex:codex-primary-v2-v3-handoff:H010`）

### Decision
卡片是可完整消费的信息簇，不以机械“一句话一卡”为目标；metadata 保持稳定 schema，正文按知识本身自由组织。

### Implemented Solution
调整 v3 card contract，加入 tags、创建/编辑时间、编辑主体及引用字段，同时降低正文模板强度。

### Outcome/Evidence
- `loops/v3_llm_wiki_loop_20260525/CARD_CONTRACT_V3.md`
- `loops/v3_llm_wiki_loop_20260525/outputs/llm_wiki/`

### Why This Matters
该决策在机器可治理（machine-governable）与人类可读（human-readable）之间建立了边界，防止 schema 取代知识本身。

### Open Questions
- 信息密度应如何度量，避免只用字符数？
- metadata 哪些字段应由脚本派生，而不是模型填写？

### Suggested Labels
`area:card-schema`, `type:design`, `version:v3`, `theme:information-density`

### Version/Timeline
v3 前置设计，2026-05-25。

### Source Events
`codex:codex-primary-v2-v3-handoff:H008`, `H009`, `H010`, `H011`, `H012`

---

## Issue 9

### Title
将 footnote citation 设为引用事实源，并从中派生 related metadata

### Question
References、footnotes、卡片链接和 related 是否需要并行维护，还是可以收敛成一个引用模型？

### Context
v3 一度同时维护 References、Footnotes 和 related cards，边界模糊且容易不同步。用户逐步明确：一句话可能由多个 raw sources 或 cards 支撑，footnote 更接近论文引用模型。

### User Signals
- “最好就是 footnotes 这种形式，因为可以多个。和论文的 citations 一样。”（`claude_code:claude-primary-v3:H018`）
- “related 不应该是【单独维护的】而是应该从【footnotes】里面提出来的。”（`claude_code:claude-primary-v3:H019`）

### Decision
正文统一使用 footnote-style citation；可引用对象扩展到 raw source 和 knowledge card；`related` 不再手工维护，而从 footnotes 派生到 metadata。

### Implemented Solution
编写 metadata 派生脚本，统一引用事实源，并让 Obsidian 双链适配派生后的卡片关系。

### Outcome/Evidence
- `loops/v3_llm_wiki_loop_20260525/tools/derive_metadata_from_footnotes.py`
- `loops/v3_llm_wiki_loop_20260525/CARD_CONTRACT_V3.md`

### Why This Matters
单一事实源（single source of truth）减少引用、链接与 metadata 漂移，也让关系图可以被确定性重建。

### Open Questions
- 如何表达“相关但不构成证据支持”的关系？
- v4 typed footnotes 是否应反向迁移为统一 schema？

### Suggested Labels
`area:citations`, `type:architecture`, `version:v3`, `theme:graph`

### Version/Timeline
v3 执行期，2026-05-27。

### Source Events
`claude_code:claude-primary-v3:H012`, `H016`, `H017`, `H018`, `H019`

---

## Issue 10

### Title
按来源类型路由 evidence surface，并将图治理拆成独立 pass

### Question
当材料扩展到论文、网页、代码仓库和社区内容后，怎样避免统一 fallback 降低信息质量，并治理数百张卡片的链接完整性？

### Context
v4 的 questioner/reader 证明了问题驱动消费材料的价值，但 repo 未被充分解析、TXT 中间层混乱、卡片治理遗漏。v5 因而把来源读取和图治理提升为独立基础设施。

### User Signals
- “repo2doc 应该是要先做的。然后才是 doc2card。”（`claude_code:claude-primary-v4:H046`）
- “webpage to markdown……没必要转 txt 吧。txt……人几乎读不了。”（`claude_code:claude-primary-v4:H052`）
- “没有进行 card governance，导致入库里面的卡片的关系都不明确，也没有 fusion 这个机制。”（`claude_code:claude-primary-v4:H015`）

### Decision
按 source type 选择 evidence surface：论文、网页、repo 等走不同 reader/router；提取完成后再顺序执行 fusion、YAML、backlink 和 orphan governance。

### Implemented Solution
v5 引入 `source_router.py`、source-type 分片审计、YAML parser/lint、fusion scan、backlink 与 orphan 修复 pass，并保留 question-driven discovery 的核心经验。

### Outcome/Evidence
- `loops/v5_llm_wiki_loop_20260612/tools/source_router.py`
- `loops/v5_llm_wiki_loop_20260612/learnings/execution_summary.md`
- 63 个有效来源、477 张 active cards；orphan rate 降至 0%，backlink asymmetry 降至约 0.5%。

### Why This Matters
来源路由决定知识提取上限，图治理决定规模化后卡片是否仍可导航、审计和复用；两者不能靠统一 prompt 或逐卡手改解决。

### Open Questions
- repo2doc 如何兼顾 README、代码语义和成本？
- v5 信息密度下降说明 router 正确但 extraction workflow 仍可能错误，下一版应如何恢复 v4 的全文 QA 消化？

### Suggested Labels
`area:ingestion`, `area:graph-governance`, `type:architecture`, `version:v4`, `version:v5`

### Version/Timeline
v4 → v5，2026-06-02 至 2026-06-12。

### Source Events
`claude_code:claude-primary-v4:H014`, `H015`, `H042`, `H045`, `H046`, `H048`, `H052`; `claude_code:claude-primary-v5:H002`, `H010`, `H018`
