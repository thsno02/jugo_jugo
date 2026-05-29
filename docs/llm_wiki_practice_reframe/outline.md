# LLM Wiki 探索实验分享 Outline

## 写作定位

这是一份“分享和讨论”形式的探索实验文档，不是 README、实验日志或稳定产品发布说明。

文档分为三大部分：

```text
Part 1. Intro / Framework
  先搭一个完整的理论和框架，说明 LLM Wiki 是什么问题、为什么不是普通内容生成、核心设计哲学是什么，以及当前阶段处在什么位置。

Part 2. Case Study / 我的实践
  再讲这个实验本身：大的构想、目的、设计、结果、迭代、实现框架和阶段性结论。

Part 3. Open Questions / Takeaways
  最后回到开放问题和讨论：多模态、人机审核、多 KB 融合、超长文本，以及本阶段真正想让读者带走的判断。
```

第一部分展示专业性和先进性；第二部分展示具体实践结果；第三部分保留开放思考和讨论空间。

## Part 1. Intro / Framework：先搭理论框架

Guideline：这一部分不是项目背景介绍，而是框架搭建。目标是让读者先理解“LLM Wiki 到底是一类什么问题”。

### 1.1 这是一件什么事

需要讲清楚：

- LLM Wiki 不是 finished wiki product；
- 也不是“让 agent 写一批文档”的内容生成 demo；
- 它探索的是：当我们有大量 raw sources 时，如何把它们转化为可读、可追溯、可修订、可持续生长的知识库；
- 这个问题的难点不只是生成内容，而是知识如何进入、拆分、组织、引用、审核、修订和提升状态。

建议开场判断：

> LLM Wiki 的核心不是 content generation，而是 knowledge governance。

### 1.2 为什么需要新的框架

传统 wiki 或文档库通常假设：知识已经被人整理过，系统只需要帮助查询、补充和维护。

但这里面对的是更前置的问题：

- 起点不是已有知识库，而是网页、论文、帖子、repo、讨论串等 raw sources；
- raw source 不直接等于 knowledge；
- LLM 能生成 summary，但 summary 不自动等于可信知识；
- 知识会过期，来源会变化，分类和颗粒度也会被后续使用重新校准。

因此，这个问题需要的不是“更会写的 agent”，而是一套能支持持续生产和治理的知识框架。

### 1.3 Zen：实验背后的基本态度

这一节是全文的精神内核，要写得相对具体。

#### Zen 1：忍受边界的模糊

知识拆分没有天然统一标准。什么应该成为一张 card，什么只是 card 里的一个 claim，什么时候应该拆分，什么时候应该合并，都没有永远正确的答案。

尤其是在 LLM Wiki 这种主题里，很多知识既可以按概念拆，也可以按机制拆，还可以按 workflow、case、risk 或 source claim 拆。不同拆法服务不同阅读和维护目标，很难提前定义一套完美 taxonomy。

因此，系统不应该假装自己拥有一套一次性正确的分类和颗粒度标准。更现实的方式是承认边界会变化，让 card 的颗粒度、分类和相互关系在使用中被校准。目标不是一次性切对，而是让边界可以被看见、被讨论、被调整。

#### Zen 2：容许错误和过期

知识库不能靠“所有内容永远正确”成立。知识会过期，来源会变化，判断会被新证据修正，原本合理的结构也可能在后续使用中显得不合适。

因此，LLM Wiki 的可信度不来自静态无误，而来自过程：来源可追溯，判断可比较，冲突可保留，内容可修订，候选内容可以被暂缓或提升。

它允许错误发生，但要求错误有机会被发现、定位和改正。

#### Zen 3：追求可治理，而不是追求一次性正确

从前两点推出，LLM Wiki 不应被理解为 truth warehouse，而应被理解为 knowledge governance system。

它的目标不是宣称自己保存了最终答案，而是管理知识如何进入、如何被检查、如何被修订、如何被引用、如何被提升为更稳定的状态。

### 1.4 Design：核心设计原则

这一节讲框架层 design，不讲具体实践细节。

#### Card 是可读知识单元，不是机械 claim 切片

card 首先要能被人和 agent 阅读、引用、维护。它应该是 scoped knowledge unit，而不是把知识切到最小 claim 后得到的碎片。

claim 可以存在，但 claim 是 card 内部可被审计的主张，不是知识库的唯一主体。过度 claim-level 化会损害阅读体验，也会带来接近 knowledge graph 的维护成本。

#### Governance layer 围绕 card 展开

provenance、boundary、conflict、comparison 是治理层，不是正文的替代品。

它们要回答：

- 这个 card 基于什么来源；
- 这个判断的边界是什么；
- 它和已有知识有什么关系；
- 是否存在重复、冲突或补充；
- 为什么它可以进入候选知识库；
- 未来如果要修订，应从哪里开始检查。

#### Candidate 和 stable 必须分开

通过 gate / audit 的 card 可以进入 candidate KB，但 candidate-ready 不等于 stable product。stable 需要额外的 promotion decision。

这个区分让系统可以持续生产和吸收新知识，同时不把所有新产物都伪装成最终版本。candidate 是可审核、可使用、可提升的候选状态；stable 是经过明确承诺后的阶段性发布状态。

#### Citation / related 应该从真实引用关系里生长

references 是 card-level broad dependency；footnotes 是 inline citation；card 本身也应该成为 cite-able object。

related 不应该长期作为一组独立手工维护的关系。更好的方向是从 footnotes、card citation 和 citation graph 中派生 related metadata，再用于导航、聚类、Obsidian 展示和后续分析。

#### Hub 和 topic 应从 card 网络中生长

top-down topic map 可以提供注意力地图，但不适合作为主要生产起点。更稳的方式是先从来源材料生产 scoped cards，再让 hub、topic、cluster 和导航结构从 card 网络中逐步浮现。

### 1.5 当前阶段的位置

Guideline：这里只做框架层定位，不展开 case。

需要说明：

- 当前实验已经从“资料获取 / 主题规划”推进到“批量候选知识卡生产”；
- v3 已形成 candidate-ready KB；
- 但 candidate-ready 不等于 stable product；
- 后面 Part 2 会把这个实践作为 case study 展开。

## Part 2. Case Study / 我的实践

Guideline：这一部分才讲具体实验。它的任务是回答：这个框架在一次真实实践中是怎么被尝试、验证和修正的。

建议主线：

```text
构想 / 目的
-> 设计
-> 结果
-> 迭代
-> 实现框架
-> 阶段性结论
```

### 2.1 构想与目的

需要讲清楚：

- 这个实践不是为了交付一个最终 wiki；
- 而是为了验证能否从 raw sources 出发，让 agent loop 持续生产 LLM Wiki；
- 人的角色主要是检查、审核、反馈和 promotion decision；
- agent 的角色是构建、迭代、升级和维护候选知识库。

这一节可以把项目目的压成一句话：

> 用 agent loop 验证一套从 source 到 card、从 card 到 candidate KB、再从 candidate KB 到 stable product 的知识生产路径。

### 2.2 实验设计

Guideline：这里讲实验设计，不讲底层工程细节。

可以围绕：

- source material 是输入；
- card 是主要知识单元；
- provenance 让 card 有证据和边界；
- similarity / comparison 处理新旧知识关系；
- gate / audit 决定是否进入 candidate KB；
- promotion decision 决定是否提升为 stable product；
- citation / related 负责让知识网络可导航、可追溯。

### 2.3 Results：得到了什么

Guideline：这一节只讲规模和状态，不解释机制。

建议只保留：

- 171 cards；
- 171 provenance；
- 171 comparison provenance；
- 974 related / interlink edges；
- v3 形成 candidate-ready KB；
- 尚未 promotion 为 stable product。

这一节的目的只是让读者快速知道：实验现在跑出了一个什么规模、什么状态的候选知识网络。

### 2.4 Iteration：判断怎么演化出来的

Guideline：这里讲认知演化，不写流水账。每一轮都用同一个轻结构。

每轮格式：

```text
Idea
Flow
Result
Problem
Experience
```

#### v0

- Idea：先验证基本机制能不能跑。
- Flow：围绕来源保存、状态记录和基础推进做小规模试验。
- Result：证明机制可运行。
- Problem：内容容易偏向 meta knowledge，也就是“如何做知识库”的知识，而不是目标 LLM Wiki 知识。
- Experience：机制验证有价值，但不能替代目标知识生产。

#### v1

- Idea：先做 top-down topic map，形成整体覆盖框架。
- Flow：从主题和 hub 出发规划 origin、definition、architecture、workflow、risk、ecosystem 等方向。
- Result：形成早期注意力地图。
- Problem：结构容易压过证据，topic skeleton 容易被误当成知识库本身。
- Experience：topic 适合导航和检查 coverage，不适合作为主要生产起点。

#### v2

- Idea：转向 scoped knowledge card。
- Flow：从来源生成 card，再补 provenance，并通过审计采纳。
- Result：小规模 accepted cards 链路成立。
- Problem：吞吐低，部分内容可能过度原子化。
- Experience：card 应该是可读单元，不是最小 claim；provenance 是可信度的一部分。

#### v3

- Idea：draft-first，再用治理层筛选、比较和吸收。
- Flow：先批量生成 draft card，再补 provenance、comparison 和 interlink，最后进入 candidate KB。
- Result：形成 171 cards 的 candidate-ready KB。
- Problem：similarity miss、empty / blocked sources、citation / related 关系仍需要继续校准。
- Experience：规模化的关键不是多写，而是让新增知识能被比较、吸收、修订和提升。

### 2.5 Execution：Data Collection 怎么做

Guideline：这是具体实践里的第一个框架，只讲来源收集逻辑，不写具体命令和实现细节。

建议框架：

```text
source discovery
-> source saving
-> source digest
-> source status
-> source queue
```

需要讲清楚：

- 来源包括网页、论文、帖子、repo、讨论串等；
- raw source 只是材料，不直接等于 knowledge；
- data collection 的目标不是囤资料，而是为后续 card production 提供可追溯输入；
- source digest 帮助后续判断来源内容、覆盖范围和可用性；
- empty source、不可读来源、upstream blocked source 要保留状态，不能默默消失；
- 来源队列是知识生产的入口，也是后续增量生产的边界记录。

### 2.6 Architecture：KB 怎么构建和生长

Guideline：这是具体实践里的第二个框架，讲知识库构建和生长逻辑。

建议框架：

```text
raw sources
-> draft cards
-> provenance
-> similarity / comparison
-> gate / audit
-> candidate KB
-> citation graph / related metadata
-> promotion decision
```

需要讲清楚：

- 先从来源生成 draft card，避免一开始就被 topic skeleton 限制；
- 再补 provenance，让 card 有证据、边界和可检查基础；
- 用 similarity / comparison 判断新知识和已有知识的关系；
- 通过 gate / audit 决定哪些 draft 可以进入 candidate KB；
- citation graph 和 related metadata 让知识网络可以导航和分析；
- 最后由 promotion decision 决定 candidate KB 是否提升为 stable product。

这一节可以强调：KB 不是一次写完的文档集合，而是从 source 到 card、从 card 到 graph、从 candidate 到 stable 的持续生长过程。

### 2.7 Case Study 小结

Guideline：这里收束实践结果，不做最终 takeaways。

可以写：

- 这个实验已经证明：从 raw sources 到 candidate KB 的链路可以跑通；
- v3 的价值不是单纯多生成了 card，而是形成了一个可检查的候选知识网络；
- 但它仍是 candidate-ready，不是 stable product；
- 这个 case 的意义是把 Part 1 的框架落到了一次可观察的实践里。

## Part 3. Open Questions / Takeaways

Guideline：这一部分不是工程问题清单，而是分享讨论的开放部分。问题要围绕 LLM Wiki 作为知识系统的长期形态。

### 3.1 Open Question：多模态怎么处理

当前答案：先转文本处理。

原因是多模态搜索本身很难，不应在这个阶段把系统复杂度压到 image / video / audio 原生检索上。更现实的方式是把多模态材料转成可读文本，同时保留可追溯的原材料。

这样当 card 不足或摘要不够时，agent 仍然可以回到原始材料继续消费、检查和补充。

### 3.2 Open Question：如何完成人机交互和审核

当前答案：通过 GitHub Issues 做审核入口。

人可以用 issue 提出问题、修改建议、质疑或补充需求；agent 根据 issue 修复或补充知识库；如果用户满意，就 close issue；如果不满意，就继续讨论和修改。

这个流程天然形成自迭代：

```text
human review
-> issue
-> agent fix
-> human check
-> close or continue
```

### 3.3 Open Question：多个知识库如何融合

这是后续需要讨论的问题。

重点不是简单 merge 文件，而是判断不同 KB 之间的 card 是否重复、互补、冲突，provenance 是否兼容，citation graph 是否能合并，以及 promotion 状态是否一致。

可以强调：

> 多 KB 融合不是内容拼接，而是知识治理对象之间的对齐。

### 3.4 Open Question：如何处理超长文本

当前假设：默认内部文档长度不会超过 1M。

因此短期不需要把超长文本处理作为主要问题展开。可以保留一个基本策略：长文本先转成可分段消费的文本材料，再生成 digest / card；如果超过默认处理能力，再进入专项处理流程。

### 3.5 Takeaways：阶段性结论

Guideline：短，像分享结尾，不像项目计划。

可以收束到以下判断：

- LLM Wiki 的关键不是生成，而是治理；
- 模糊边界是知识生产的常态，不是异常；
- 错误和过期不可避免，所以系统要可追溯、可比较、可修订；
- card 是阅读和维护单元，治理层负责证据、边界、冲突和演化；
- candidate 和 stable 的区分让系统既能持续生产，也能保持发布责任；
- 这个 case 说明从 raw sources 到 candidate KB 的路径是可行的；
- 下一阶段重点是让知识库持续生长，同时保持可维护。

## 风格约束

- 不写成 README。
- 不写成实验日志。
- 不堆工程细节。
- 不展开 hooks / CLI / worker / task template / JSON schema / 路径。
- 不把开放问题写成 issue tracker。
- Part 1 负责框架和专业判断。
- Part 2 负责实践 case 和结果。
- Part 3 负责开放问题和讨论。
- Results 只讲规模和状态。
- Iteration 讲 idea、flow、result、problem、experience。
- final doc 必须可单独转发，也适合用于分享讨论。
