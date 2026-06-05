---
total_cards: 259
generated: 2026-06-05T14:11:33
card_type_distribution:
  mechanism: 108
  source_claim: 48
  distinction: 44
  concept: 40
  operational_rule: 11
  example_pattern: 8
---

# KB Card Index (259 cards)

## Category Overview

| Category | Count |
|----------|-------|
| LLM Wiki -- Core Concepts (核心概念) | 19 |
| LLM Wiki -- Architecture (架构与运行时) | 12 |
| LLM Wiki -- Operations (操作与维护) | 11 |
| LLM Wiki -- Knowledge Growth (知识增长与复利) | 4 |
| LLM Wiki -- RAG & Context (RAG 对比与上下文) | 11 |
| LLM Wiki -- Quality & Governance (质量与治理) | 6 |
| LLM Wiki -- Compilation & WiCER (编译与精炼) | 3 |
| LLM Wiki -- Philosophy & Design (设计哲学) | 8 |
| LLM Wiki -- Research Workflow (研究工作流) | 2 |
| LLM Wiki -- Implementations & Community (实现与社区) | 9 |
| LLM Wiki -- Workflows & Use Cases (工作流与场景) | 1 |
| Companion Memory (伴侣记忆系统) | 15 |
| Agent Memory (Agent 记忆系统) | 22 |
| Memory Systems (记忆系统通用) | 12 |
| MemGPT (MemGPT 系统) | 12 |
| RAG & Retrieval (RAG 与检索) | 20 |
| GraphRAG (图谱 RAG) | 13 |
| Knowledge Graph (知识图谱) | 5 |
| Citation (引用生成与评估) | 5 |
| Evaluation & Benchmarks (评估与基准) | 7 |
| LLM Context & Scaling (LLM 上下文与扩展) | 4 |
| Token Economics (Token 经济学) | 7 |
| Security & Adversarial (安全与对抗) | 15 |
| Governance & Compliance (治理与合规) | 8 |
| Enterprise Wiki (企业级 Wiki) | 5 |
| Wikibase (Wikibase 数据模型) | 9 |
| Documentation (文档工程) | 3 |
| Other (其他) | 11 |

## LLM Wiki -- Core Concepts (核心概念)

(19 cards)

| Title | canonical_concept | Type | Summary |
|-------|-------------------|------|---------|
| [审计与溯源追踪](../cards/audit-provenance-tracing.md) | `audit-provenance-tracing` | mechanism | 是 LLM Wiki 的信任验证机制：沿 output->wiki->raw 完整制品图追踪，检测漂移， 复用 librarian 评分通道，当本地证据不足时升级为新鲜研究 |
| [跨会话连续性机制](../cards/cross-session-continuity.md) | `cross-session-continuity` | mechanism | 是 LLM Wiki 通过三个持久化组件（raw sources、wiki、schema）加 log.md 实现跨会话连续性的机制 |
| [双受众制品](../cards/dual-audience-artifact.md) | `dual-audience-artifact` | mechanism | 指编译后的 wiki 同时是人类浏览界面（Obsidian 打开、跟踪链接、阅读概念页）和 AI 知识层（结构化、交叉引用的上下文）；与 RAG 向量数据库（.faiss 文件人类无法阅读）形成对比——同一制品服务两类受众 |
| [提取粒度控制](../cards/extraction-granularity-control.md) | `extraction-granularity-control` | mechanism | 是 LLM Wiki 插件的可配置提取深度机制：五个预设级别（Minimal 5 / Coarse 10 / Standard 50 / Fine 100 / Custom 1-300）， 在分析深度与 API 成本之间取得平衡 |
| [全栈本地性](../cards/full-stack-locality.md) | `full-stack-locality` | distinction | 是个人知识库的三层本地性谱系：Notion AI = 云存储+云计算，Obsidian+插件 = 本地存储+云计算，本地 LLM wiki = 存储与计算均在本地；全栈本地的核心价值不是速度而是敏感数据永不离机 |
| [HN 社区将 LLM Wiki 视为架构模式](../cards/hn-architectural-pattern-reception.md) | `hn-architectural-pattern-reception` | source_claim | Hacker News 社区以 274 点 89 评论接受 Karpathy 的 LLM Wiki gist，将其视为 agent 工作流的架构模式而非笔记技巧 |
| [清单与证据的刻意分离](../cards/inventory-evidence-separation.md) | `inventory-evidence-separation` | distinction | 是 LLM Wiki 的设计区分：inventory/ 存放操作状态（物品/来源候选/语料/实体/待办）， 刻意不作为事实主张的证据，与 raw/+wiki/ 的证据链保持边界 |
| [文献速度论点](../cards/literature-velocity-argument.md) | `literature-velocity-argument` | source_claim | 主张在快速演进的研究前沿，手工维护的参考文献在发布前就已过时，而 LLM 维护的交叉引用 wiki 能在不失结构的前提下吸收新工作 |
| [活动日志文件](../cards/log-file.md) | `log-file` | mechanism | 是 LLM Wiki 的时间线记录： 按时间顺序 append-only 记录摄入/查询/巡检事件，可用 grep 等 unix 工具解析， 帮助 LLM 理解最近发生了什么 |
| [Map of Content 引导阅读路径](../cards/map-of-content-pattern.md) | `map-of-content-pattern` | mechanism | 是 LLM Wiki 中按主题组织的引导阅读路径，区别于 index.md 的平面目录；摄入新论文时自动更新以避免孤立节点 |
| [原创思考的逐字保留](../cards/originals-verbatim-capture.md) | `originals-verbatim-capture` | operational_rule | 指 LLM Wiki 中设置 originals/ 文件夹保存用户自己的原始思考，禁止 LLM 编辑， 因为「语言本身就是洞见」；弥补 v1 仅假设摄入外部文章的缺陷 |
| [RAG 与 Wiki 知识综合的区分](../cards/rag-wiki-synthesis-distinction.md) | `rag-wiki-synthesis-distinction` | distinction | 社区对 LLM Wiki 是否"只是 RAG"的辩论：检索循环是 RAG 形状的，但写入循环（LLM 自己编写维护 wiki、建反向链接、回填输出）构成知识综合而非检索；vanilla RAG 语料是静态的，wiki 语料是动态的；l... |
| [Schema 文件的配置角色](../cards/schema-as-configuration.md) | `schema-as-configuration` | mechanism | 指 LLM Wiki 中 schema 的配置角色：使 LLM 成为有纪律的 wiki 维护者，由人机共同演化 |
| [Schema 模板的领域垂直化](../cards/schema-template-verticals.md) | `schema-template-verticals` | example_pattern | 指 LLM Wiki 的 schema 层已被产品化为五个领域垂直模板（general / research / engineering / product / SEO），每个模板以 schema.md + CLAUDE.md 组合交... |
| [服务器力学边界原则](../cards/server-mechanics-boundary.md) | `server-mechanics-boundary` | distinction | 是 llm-wiki-mcp 的设计边界原则：服务器只强制执行力学层（原子写入、乐观并发、路径限制、日志格式）， 刻意不验证内容形状（frontmatter/分类/链接目标）——"将 schema 烘焙进服务器会违背初衷 |
| [结构化可查询性缺口](../cards/structured-queryability-gap.md) | `structured-queryability-gap` | distinction | 指纯 markdown wiki 在混入结构化数据（工作项、ADR）后暴露的查询局限：agent 无法回答"显示阻塞此 epic 的未完成任务"而不扫描散文或维护并行索引；AGENTS.md 教 LLM 文件夹约定只在数据简单时有效；... |
| [类型化 Wiki 链接](../cards/typed-wikilinks.md) | `typed-wikilinks` | mechanism | 指在 wiki 链接后附加关系类型标注（共 6 种，如 uses / alternative-to / contradicts），使知识图从 "X 连接 Y" 升级为 "X 以何种方式关联 Y"，显著提升 LLM 回答精度 |
| [Wiki 即 Git 仓库](../cards/wiki-as-git-repo.md) | `wiki-as-git-repo` | source_claim | 指 LLM Wiki 选择纯 markdown 文件作为 wiki 层意味着 wiki 即 git 仓库，免费获得版本历史、分支和协作能力 |
| [书写即思考](../cards/writing-as-thinking.md) | `writing-as-thinking` | concept | 反驳"苦差事可外包"假设：摘要、交叉引用、归档等"grunt work"正是新想法涌现和知识内化的过程；自动化过程即消灭了洞察的产生场所；Karpathy 混淆了文字（目标）与思考（真正目标） |

## LLM Wiki -- Architecture (架构与运行时)

(12 cards)

| Title | canonical_concept | Type | Summary |
|-------|-------------------|------|---------|
| [编译时与查询时知识装配](../cards/compile-time-vs-query-time.md) | `compile-time-vs-query-time` | distinction | 是 LLM wiki 与 RAG 的根本架构区分轴：wiki 在编译时将结构化索引加载到上下文中（LLM 预先读取全部相关内容）， RAG 在查询时从向量库动态检索语义相关片段 |
| [全上下文反 RAG 架构选择](../cards/full-context-anti-rag.md) | `full-context-anti-rag` | distinction | 是 Karpathy LLM Wiki 的核心架构选择：拒绝 RAG 分块检索，改为向 LLM 提供完整 Wiki 上下文， 理由是 RAG 碎片化知识并破坏跨知识图谱推理能力，因此强烈推荐 1M+ token 长上下文模型 |
| [MCP 工具与技能的双层设计](../cards/mcp-tool-skill-layering.md) | `mcp-tool-skill-layering` | mechanism | 是 llm-wiki-mcp 的双层架构：4 个 MCP 工具提供跨客户端可移植的原子原语（read/write/log/inventory）， 4 个 Claude Code 技能在其上编排工作流（init/ingest/query... |
| [多平台技能可移植性](../cards/multi-platform-skill-portability.md) | `multi-platform-skill-portability` | mechanism | 是 LLM Wiki 的分发机制：单一 wiki-manager 技能为所有运行时的行为源（Claude Code/Codex/OpenCode/Pi/AGENTS.md）， Codex/OpenCode/Pi 通过 symlink ... |
| [乐观并发控制（Etag CAS）](../cards/optimistic-concurrency-etag.md) | `optimistic-concurrency-etag` | mechanism | 是 llm-wiki-mcp 的写入冲突检测机制：每页 etag = sha256(body)\|\|mtime_ns， 更新时提交读取时获得的 etag，不匹配则抛 WikiConflictError，agent 执行 re-read-... |
| [运行时与代理的职责边界](../cards/runtime-agent-boundary.md) | `runtime-agent-boundary` | distinction | llm-wiki-karpathy 的架构核心：确定性运行时拥有路径/ID/验证/写入/清单追踪/导航生成，代理拥有摘要/OCR/综合/笔记分类/持续改进 |
| [三层架构](../cards/three-layer-architecture.md) | `three-layer-architecture` | concept | 是 LLM Wiki 的三层结构： 不可变原始资料层（source of truth）、LLM 拥有的 wiki 层（markdown 页面）、人机共同演化的 schema 层 |
| [主题隔离原则](../cards/topic-isolation.md) | `topic-isolation` | concept | 是 LLM Wiki 的设计原则：每个研究领域是独立 wiki，拥有独立的来源/文章/产出/Obsidian 配置， 避免跨主题噪声，需要时可通过 multi-wiki peek 发现交叉 |
| [Wiki 企业级三大失效模式](../cards/wiki-enterprise-failure-modes.md) | `wiki-enterprise-failure-modes` | distinction | LLM wiki 在企业规模下有三大失效模式：索引溢出（50K-100K token 上限）、无原生 RBAC、 并发写入冲突——这些不是 bug 而是设计假设的必然后果 |
| [Wiki-RAG 混合架构模式](../cards/wiki-rag-hybrid-pattern.md) | `wiki-rag-hybrid-pattern` | mechanism | LLM wiki 与 RAG 并非互斥，可以形成混合架构：wiki 提供策展过的高置信度上下文作为"种子"锚定 RAG 检索， 实现两层分离——wiki 层承载"我们确定知道的"，RAG 层承载"语料库中当前有的 |
| [WikiStorage 可插拔存储协议](../cards/wiki-storage-protocol.md) | `wiki-storage-protocol` | mechanism | 是 llm-wiki-mcp 的存储抽象层：实现 WikiStorage Protocol 的 6 个方法即可替换后端（SQLite/Notion/GDrive/test fake）， build_server 作为组合根接受存储实例 |
| [零运行时依赖](../cards/zero-runtime-dependency.md) | `zero-runtime-dependency` | concept | 是 LLM Wiki 的架构约束：完全运行在宿主智能体的内置工具上（文件读写/网络搜索/网页抓取）， 插件本身是 Markdown + 命令定义，无服务器/服务/遥测 |

## LLM Wiki -- Operations (操作与维护)

(11 cards)

| Title | canonical_concept | Type | Summary |
|-------|-------------------|------|---------|
| [主题归档生命周期](../cards/archive-lifecycle.md) | `archive-lifecycle` | mechanism | 是 LLM Wiki 的主题生命周期机制：整个 topic wiki 移至 topics/.archive/，保留知识但默认静默， 大多数工具自动跳过，需显式 --include-archived 才可读写 |
| [复杂度崩溃阈值](../cards/complexity-collapse-threshold.md) | `complexity-collapse-threshold` | mechanism | 指 LLM Wiki 系统存在一个临界点，超过该点 agent 无法维护 wiki、开发者也无法理解 wiki；人类能处理 10 单位复杂度+LLM 处理 20 单位时，用户倾向于构建 30 单位复杂度的系统并在失控前无法察觉 |
| [矛盾状态机](../cards/contradiction-state-machine.md) | `contradiction-state-machine` | mechanism | 是 LLM Wiki 插件中跟踪知识矛盾的状态机制：detected -> review_ok -> resolved（AI 修复） 或 detected -> pending_fix（手动修复），矛盾在多源融合时带归因保留而非自动消除 |
| [摄入操作](../cards/ingest-operation.md) | `ingest-operation` | operational_rule | 是 LLM Wiki 核心操作之一：LLM 读取新资料、更新索引和实体/概念页面，单次可触及 10-15 个 wiki 页面 |
| [巡检操作](../cards/lint-operation.md) | `lint-operation` | operational_rule | 是 LLM Wiki 定期健康检查操作：检测矛盾、过时主张、孤立页面、缺失概念页、缺失交叉引用、数据缺口 |
| [LLM 作为维护引擎的角色重构](../cards/llm-as-maintenance-engine.md) | `llm-as-maintenance-engine` | concept | 将 LLM 从检索层重构为维护引擎：LLM 的核心价值不是按需检索回答问题，而是持续执行人类回避的重复性簿记任务（交叉链接、摘要更新、矛盾追踪、结构一致性维护） |
| [维护成本归零论点](../cards/maintenance-cost-zero.md) | `maintenance-cost-zero` | source_claim | 是 LLM Wiki 核心论点：人类放弃 wiki 因维护负担增长快于价值，LLM 使维护成本趋近于零 |
| [记忆生命周期元数据](../cards/memory-lifecycle-metadata.md) | `memory-lifecycle-metadata` | mechanism | 指在 wiki 页面 frontmatter 中添加 last_verified / confidence / superseded_by / contradicts 等字段，管理知识的时间维度；缺失时导致过时主张与新鲜主张无法区分 |
| [查询操作与答案归档](../cards/query-and-answer-filing.md) | `query-and-answer-filing` | operational_rule | 是 LLM Wiki 查询操作：LLM 搜索 wiki 页面综合带引用答案，好答案归档为新页面使探索产生复利效应 |
| [表示先行摄入模型](../cards/representation-first-ingest.md) | `representation-first-ingest` | mechanism | llm-wiki-karpathy 运行时的双路径摄入机制：文本/结构化数据直接编译，PDF/图片须先存储中间表示（OCR、视觉描述等）至 .llm-kb/representations/ 后方可编译，运行时自身不执行 OCR/视觉处理 |
| [工作流五类分类法](../cards/workflow-taxonomy.md) | `workflow-taxonomy` | concept | 将 LLM Wiki 工作流组织为 create（ingest/batch-ingest/synthesize）、enrich（enrich/expand）、 audit（gap-analysis/verification/lint/... |

## LLM Wiki -- Knowledge Growth (知识增长与复利)

(4 cards)

| Title | canonical_concept | Type | Summary |
|-------|-------------------|------|---------|
| [缺口映射与晋升机制](../cards/gap-mapping-promotion.md) | `gap-mapping-promotion` | mechanism | llm-wiki-karpathy 运行时通过确定性缺口映射识别 wiki 覆盖空白，并将缺口晋升为一等笔记，实现持久知识增长 |
| [产出复利循环](../cards/output-compounding-loop.md) | `output-compounding-loop` | mechanism | 是 LLM Wiki 的价值放大机制：产出（报告/幻灯片/计划等）回写进 wiki， 使每个新产出建立在所有先前研究之上，研究越多产出越强 |
| [Wiki 作为复利型知识制品](../cards/wiki-compounding-artifact.md) | `wiki-compounding-artifact` | mechanism | 指 LLM Wiki 中持续积累的五类结构：交叉引用、已标记矛盾、综合叙述、实体/概念页面、归档的查询分析 |
| [Wiki 回写机制](../cards/wiki-write-back-mechanism.md) | `wiki-write-back-mechanism` | mechanism | 是使 LLM Wiki 从只读编译产物变为持续增长的复利制品的关键机制：通过 llm-wiki note "<insight>" 命令， LLM 会话中产生的洞察可反向写入知识图谱，实现双向流动 |

## LLM Wiki -- RAG & Context (RAG 对比与上下文)

(11 cards)

| Title | canonical_concept | Type | Summary |
|-------|-------------------|------|---------|
| [注意力稀释导致全上下文推理在规模化时退化](../cards/attention-dilution-at-scale.md) | `attention-dilution-at-scale` | mechanism | 是全上下文 KV cache 推理在知识规模扩大时性能退化的机制——注意力被大量无关内容稀释，导致其在规模化场景下 表现劣于 RAG |
| [上下文窗口退化现象](../cards/context-window-degradation.md) | `context-window-degradation` | source_claim | 指 LLM 在 200k-300k token 处开始"遗忘"，即使名义上下文窗口达 1M；因此 10M 上下文不会使 wiki 中间层过时；这是 LLM Wiki 中间知识层存在的实用性理据之一 |
| [索引文件导航机制](../cards/index-based-navigation.md) | `index-based-navigation` | mechanism | 是 LLM Wiki 的导航核心：index.md 按类别列出所有页面及摘要，中等规模（~100 资料）下运作良好避免 embedding RAG， 超出规模后可用 qmd（BM25/向量混合搜索 + LLM 重排序） |
| [KV cache 推理与 RAG 的性能权衡](../cards/kv-cache-vs-rag-tradeoff.md) | `kv-cache-vs-rag-tradeoff` | source_claim | 是 WiCER 论文在 17 个 RepLiQA 领域上的实证发现：全上下文 KV cache 推理在策展知识上优于 RAG（4.38 vs 4.08，TTFT 快 7.3 倍），但因注意力稀释在规模化时退化至低于 RAG |
| [LLM Wiki 的教学工具本质](../cards/llm-wiki-as-teaching-tool.md) | `llm-wiki-as-teaching-tool` | source_claim | 认为 Karpathy llm.c 的首要价值不是回答质量而是构建过程本身的教育意义——从零走通 RAG 管线比任何教程更有效；未亲手构建过 RAG 系统的 AI 工程师是在"借来的理解"上工作 |
| [LLM Wiki 模式](../cards/llm-wiki-pattern.md) | `llm-wiki-pattern` | concept | 是一种用 LLM 增量构建并维护持久化 wiki 的知识库模式，区别于 RAG 每次查询重新检索，wiki 作为编译后的知识中间层持续积累 |
| [LLM Wiki 与 RAG 的核心差异在于推理深度](../cards/llm-wiki-rag-depth-distinction.md) | `llm-wiki-rag-depth-distinction` | distinction | 指 LLM Wiki 与 RAG 的根本区别不在于速度而在于推理深度；wiki 从预先综合、互链、矛盾已解决的知识中回答，使多跳推理自然可行 |
| [LLM Wiki 的适用规模边界](../cards/llm-wiki-scale-boundary.md) | `llm-wiki-scale-boundary` | distinction | 指 LLM Wiki 在个人规模 （10 至数百篇文档）下表现最佳，超出后 interlink 管理的 token 成本上升，vector search 更为适合 |
| [RAG 与 Wiki 的互补关系](../cards/rag-wiki-complementarity.md) | `rag-wiki-complementarity` | distinction | 指实际运用中 RAG 和 Wiki 并非二选一：临时性问题适合 RAG 检索，全局理解和跨项目把握适合 Wiki，两者可并存于同一系统 |
| [场景驱动的知识工具选择](../cards/scenario-based-tool-selection.md) | `scenario-based-tool-selection` | distinction | 是三段式处方：个人第二大脑/研究/学习用 LLM wiki，运营自动化/趋势追踪用结构化知识库（关系型）， 企业级百万文档用 RAG 或混合方案 |
| [TL;DR 摘要的上下文窗口优化作用](../cards/tldr-context-optimization.md) | `tldr-context-optimization` | mechanism | 指在每个 wiki 页面顶部强制放置 <=50 字符 TL;DR 摘要，使 LLM 查询时扫描摘要而非全文，节省上下文窗口；实践中比索引更重要 |

## LLM Wiki -- Quality & Governance (质量与治理)

(6 cards)

| Title | canonical_concept | Type | Summary |
|-------|-------------------|------|---------|
| [别名系统与跨语言去重](../cards/alias-cross-language-dedup.md) | `alias-cross-language-dedup` | mechanism | 是 LLM Wiki 插件的去重机制：每页强制至少 1 个别名（翻译/缩写/别称）， 通过两层语义检测（Tier 1 直接匹配始终 LLM 验证 + Tier 2 间接信号填充 token 预算）消除跨语言重复页 |
| [矛盾作为知识资产](../cards/contradiction-as-asset.md) | `contradiction-as-asset` | operational_rule | 指 LLM Wiki 中发现矛盾时不覆盖旧主张而是标记 contradicts: 字段保留双方， 因为旧推理在未来可能有用；覆盖导致不可逆的知识损失 |
| [模型能力不足导致的错误传播风险](../cards/model-quality-error-propagation.md) | `source-faithfulness-risk` | operational_rule | 指 LLM Wiki 完全依赖 模型质量管理来源间矛盾，能力不足的模型会静默传播错误；agents.md 质量和定期人工审查是关键缓解措施 |
| [源忠实性风险与不可变锚点](../cards/source-faithfulness-risk.md) | `source-faithfulness-risk` | distinction | 指 LLM Wiki 中 wiki 内容经多轮变换后偏离来源的风险；raw sources 不可变提供锚点，lint 仅查时效性非忠实度 |
| [源文件粒度效应](../cards/source-granularity-effect.md) | `source-granularity-effect` | mechanism | 指源文件的切分粒度对 wiki 编译质量有决定性影响：整本书作为单文件产出"slop"，章节级切分则质的提升；相同模型、相同提示词，唯一变量是源粒度 |
| [Wiki 去重的脆弱性](../cards/wiki-deduplication-fragility.md) | `wiki-deduplication-fragility` | source_claim | 指 LLM Wiki 的去重完全依赖 LLM 判断、在规模增长时变得脆弱——缺乏确定性保护机制时 wiki 会逐渐积累近似重复页面 |

## LLM Wiki -- Compilation & WiCER (编译与精炼)

(3 cards)

| Title | canonical_concept | Type | Summary |
|-------|-------------------|------|---------|
| [编译缺口——Wiki 编译中的灾难性事实丢失](../cards/compilation-gap.md) | `compilation-gap` | concept | 指 LLM 将原始文档蒸馏为 wiki 时不可避免地丢弃关键事实的问题；盲编译在 17 个 RepLiQA 领域上的灾难性失败率为 53-60%， 质量仅 2.14-2.32（满分 5），远低于 RAG 基线 3.46 |
| [定向诊断优于泛化固定](../cards/targeted-diagnosis-vs-generic-pinning.md) | `targeted-diagnosis-vs-generic-pinning` | distinction | 是 WiCER 消融实验在 17 个主题上的关键发现：定向诊断（识别具体丢失事实）带来 +0.95 的 质量提升，而泛化固定（不加区分地保留信息）仅贡献 +0.16 |
| [WiCER 迭代精炼算法](../cards/wicer-iterative-refinement.md) | `wicer-iterative-refinement` | mechanism | 是一种受 CEGAR 启发的迭代算法，通过诊断探针评估编译后 wiki、识别丢失事实并在后续编译中强制保留，1-2 次迭代可 恢复 80% 的丢失质量，灾难性失败减少 55% |

## LLM Wiki -- Philosophy & Design (设计哲学)

(8 cards)

| Title | canonical_concept | Type | Summary |
|-------|-------------------|------|---------|
| [认知去技能化风险](../cards/cognitive-deskilling-risk.md) | `cognitive-deskilling-risk` | concept | 指将知识构建过度委托给 LLM 后，人类自身认知能力退化的风险；实践者报告出现"持久脑缺口"——一种新型技术债务，知识差距累积且成瘾性地持续 |
| [人机角色分工](../cards/human-llm-role-division.md) | `human-llm-role-division` | distinction | 是 LLM Wiki 的角色分工原则：人类策展/引导/提问/思考，LLM 负责摘要、交叉引用、归档和簿记 |
| [刻意抽象与模块化](../cards/intentional-abstraction.md) | `intentional-abstraction` | source_claim | 是 LLM Wiki gist 的设计哲学：描述模式而非实现，所有组件可选且模块化，与 LLM 协作实例化 |
| [Licklider 人机共生类比](../cards/licklider-symbiosis-parallel.md) | `licklider-symbiosis-parallel` | source_claim | 社区评论者将 LLM Wiki 追溯到 Licklider 1960 年智能放大论文：人类制定目标、提出假设、评判贡献、处理低概率情况；机器将假设转化为可测试模型、执行例行操作、填充决策间隔——与 LLM Wiki 的人机分工精确对应 |
| [Memex 精神联系](../cards/memex-connection.md) | `memex-connection` | source_claim | 指 LLM Wiki 与 Bush 1945 年 Memex 构想的精神联系：私人策展、关联路径与文档同等重要，维护问题由 LLM 解决 |
| [模式命名的共振效应](../cards/pattern-naming-resonance.md) | `pattern-naming-resonance` | source_claim | 指 Karpathy 的 LLM Knowledge Base 帖子引发强烈共鸣的原因：许多人已在用 CLAUDE.md、Agent 规则文件、Obsidian 等做类似实践， 该帖子为这些散发性尝试赋予了名称和结构，产生了「原来我做... |
| [人类参与程度谱系](../cards/review-involvement-spectrum.md) | `review-involvement-spectrum` | distinction | 指 LLM Wiki 中人类参与程度是可调谱系：从逐条深度审查到批量低监督处理 |
| [理解瓶颈](../cards/understanding-bottleneck.md) | `understanding-bottleneck` | concept | 是 Karpathy 在 Sequoia 访谈中提出的认知论点：即使 LLM 可以外包思维，人类无法外包理解；wiki 式投射帮助信息进入人类心智模型 |

## LLM Wiki -- Research Workflow (研究工作流)

(2 cards)

| Title | canonical_concept | Type | Summary |
|-------|-------------------|------|---------|
| [并行多智能体研究机制](../cards/parallel-multi-agent-research.md) | `parallel-multi-agent-research` | mechanism | 是 LLM Wiki 的研究核心机制：5-10 个智能体从学术/技术/应用/新闻/反面五个角度并行搜索， 经可信度去重后摄入，每轮产出缺口报告驱动迭代 |
| [论点驱动研究模式](../cards/thesis-driven-research.md) | `thesis-driven-research` | mechanism | 是 LLM Wiki 的特殊研究模式：从一个主张出发，智能体按支持/反对/机制/元分析/相邻五角度分工， 产出判决而非摘要，第二轮加权反面证据以对抗确认偏误 |

## LLM Wiki -- Implementations & Community (实现与社区)

(9 cards)

| Title | canonical_concept | Type | Summary |
|-------|-------------------|------|---------|
| [kb-compile 实现模式](../cards/kb-compile-implementation.md) | `kb-compile-implementation` | example_pattern | 是一种将 LLM Wiki 模式落地的具体实现：通过 Claude Code 自定义命令 /kb-compile 触发 wiki 编译，在已有 Mem0+pgvector 向量检索层之上叠加 wiki 层，形成四组件混合架构 |
| [LLM Wiki 生态形成速度](../cards/llm-wiki-ecosystem-velocity.md) | `llm-wiki-ecosystem-velocity` | source_claim | 指 Karpathy 于 2026 年 4 月提出 LLM Wiki 后，一周内即出现开源实现、YouTube 讲解、 大量博客文章，随后出现 aillm.wiki 等商业目录站，体现模式的极快生态形成 |
| [LLM Wiki 主流化四条件](../cards/llm-wiki-mainstream-prerequisites.md) | `llm-wiki-mainstream-prerequisites` | source_claim | 是本地 LLM wiki 走向主流的四项必要条件：更小更好的模型、更智能的分块与检索（语义分块+混合搜索）、真正的 UI、增量索引；作者以"第一部电话"类比当前阶段，预测 2027 年前出现成熟产品 |
| [LLM Wiki 搭建摩擦](../cards/llm-wiki-setup-friction.md) | `llm-wiki-setup-friction` | source_claim | 是 llm.c 搭建时的三面墙：macOS Clang 不支持 OpenMP 需改用 GCC、wiki 功能要求单一大文本文件需预处理多文件笔记、CPU 推理 30+ 秒/查询而 GPU 仅需数秒 |
| [LLM Wiki v2 社区扩展与 agentmemory 模式](../cards/llm-wiki-v2-agentmemory.md) | `llm-wiki-v2-agentmemory` | source_claim | 是 rohitg00 在 GitHub Gist 上发布的社区扩展，通过引入 agentmemory 模式将 LLM Wiki 从个人研究工具扩展为 适合自主编程代理持续填充的持久化记忆引擎 |
| [my-llm-wiki PyPI 实现](../cards/my-llm-wiki-implementation.md) | `my-llm-wiki-implementation` | example_pattern | 是 Karpathy LLM Wiki 三层架构的 Python CLI 实现：pip 安装后 llm-wiki . 即可将任意文件夹编译为可查询的 Obsidian vault， 支持 19 语言代码（Tree-sitter AST... |
| [Obsidian 社区插件 Karpathy LLM Wiki](../cards/obsidian-karpathy-wiki-plugin.md) | `obsidian-karpathy-wiki-plugin` | example_pattern | 是 Karpathy LLM Wiki 概念的 Obsidian 社区插件实现：v1.10.2，94/100 评分， 实现三层架构 + 六大命令（摄入/查询/巡检/索引/Schema 建议），支持 10+ LLM 供应商 |
| [Obsidian 工具生态](../cards/obsidian-tooling.md) | `obsidian-tooling` | operational_rule | 是 LLM Wiki 实践中的 Obsidian 工具生态：Web Clipper 采集资料、graph view 可视化连接、 Marp 生成幻灯片、Dataview 查询 frontmatter，Obsidian 作为「IDE」供... |
| [生产级 Wiki 参考实现](../cards/production-scale-wiki-reference.md) | `production-scale-wiki-reference` | example_pattern | 是 Karpathy LLM Wiki 模式的首个公开生产级实现：120 页、1400+ 交叉引用、27 源、13 实体、9 MOC、9 分析页， 带完整工作流和双许可 |

## LLM Wiki -- Workflows & Use Cases (工作流与场景)

(1 cards)

| Title | canonical_concept | Type | Summary |
|-------|-------------------|------|---------|
| [应用领域](../cards/use-case-domains.md) | `use-case-domains` | example_pattern | 列举 LLM Wiki 的五类应用：个人成长、研究深耕、书籍阅读（类似 fan wiki）、团队/业务内部 wiki、 以及竞争分析/尽职调查/旅行规划等知识积累场景，模式统一适用 |

## Companion Memory (伴侣记忆系统)

(15 cards)

| Title | canonical_concept | Type | Summary |
|-------|-------------------|------|---------|
| [架构可分离性作为安全承诺](../cards/architectural-separability-as-safety.md) | `architectural-separability-as-safety` | distinction | 伴侣记忆框架的安全设计承诺：wiki 必须保持在基模型权重之外，因为可分离性在结构上必要——使基模型演进作为外部纠正通道对抗用户耦合认知固化；将 wiki 折叠进权重则永久关闭此通道 |
| [AUDIT 结构性压力测试](../cards/audit-stress-test.md) | `audit-stress-test` | mechanism | 是伴侣记忆框架中运行于慢周期（月度+）的补偿机制：临时悬挂最高引力条目，运行历史查询测试性能影响；三种结果——性能下降则恢复、不变则降低引力（死权重）、改善则归档（主动干扰）；目标是中断库恩式范式僵化 |
| [循环性作为论题](../cards/circularity-as-thesis.md) | `circularity-as-thesis` | distinction | 伴侣记忆框架的哲学立场：基于一致性的记忆策略的循环性（一致性对照当前 wiki 衡量，而 wiki 是过去一致性决策的产物）在真理追踪框架下是致命缺陷，但在伴侣框架下是拥有稳定自我的样子；框架接受镜像侧的循环性，并通过补偿侧（整合+审... |
| [伴侣系统合规不变量](../cards/companion-conformance-invariants.md) | `companion-conformance-invariants` | operational_rule | 伴侣记忆框架为每个操作定义的规范性不变量集合，将"说服性框架"转变为"可测试的规范"；核心不变量包括：TRIAGE 禁止读取活跃 wiki、CONSOLIDATE 必须先缓冲区内评分、DECAY 不得衰减引力保护下限以上的条目、任何操... |
| [伴侣知识系统](../cards/companion-knowledge-system.md) | `companion-knowledge-system` | concept | 是一种服务于单一用户的持久化 LLM 记忆系统设计类别，其规范性治理义务是：在操作维度上镜像用户（词汇、结构、上下文连续性），在认知失败维度上补偿用户（固化、证据压制、库恩式僵化） |
| [伴侣系统对象模型](../cards/companion-object-model.md) | `companion-object-model` | concept | 伴侣记忆框架定义的五种核心实体及其生命周期状态：原始缓冲区条目（pending→consolidated/rejected/expired）、活跃 wiki 条目（active→decaying→archived，带 gravity-... |
| [CONTEXTUALIZE 深度适配压缩](../cards/contextualize-depth-fitted-compression.md) | `contextualize-depth-fitted-compression` | mechanism | 伴侣记忆框架中将外部来源压缩到用户当前工作上下文深度的操作；在梦周期而非流式摄取时运行，必须保留到原始来源的链接（linkout）；引入冷存储层作为第三存储层；代谢隐喻——细胞不吸收环境中的一切，只吸收当前代谢状态能使用的 |
| [用户耦合漂移下的固化](../cards/entrenchment-under-user-coupled-drift.md) | `entrenchment-under-user-coupled-drift` | concept | 是伴侣记忆框架针对的核心失败模式：个人 LLM wiki 随时间使主导解释越来越受保护、新矛盾证据越来越容易被驳回，知识库从活的知识基础变成范式维护系统；这是库恩正常科学的记忆层类比 |
| [记忆引力](../cards/memory-gravity.md) | `memory-gravity` | mechanism | 是伴侣记忆框架中保护结构承重条目免受朴素剪枝的机制；基于中心性 C(i) 和下游碎片化成本 F(i) 计算，必须满足四个属性：中心性单调、碎片化单调、亚线性增长（防止绝对在位者陷阱）、有界性；关键区别于 PageRank 在于引力是前... |
| [少数派压力提升机制](../cards/minority-pressure-promotion.md) | `minority-pressure-promotion` | mechanism | 是伴侣记忆框架中防止单一文化坍缩的补偿机制：少数派假设跨多个整合周期在缓冲区和隔离区保留，当积累的互相支持证据跨过提升阈值时可挑战引力保护的在位条目；这是论文最尖锐的可证伪预测（Prediction 4） |
| [镜像-补偿设计原则](../cards/mirror-vs-compensate-principle.md) | `mirror-vs-compensate-principle` | mechanism | 伴侣记忆系统的核心设计规则：在操作维度（词汇、结构、连续性）镜像用户，在认知失败维度（固化、证据压制）补偿用户；冲突时流式路径默认镜像、定期整合窗口执行补偿、AUDIT 作为慢周期仲裁者 |
| [睡眠整合架构](../cards/sleep-consolidation-architecture.md) | `sleep-consolidation-architecture` | mechanism | 将摄取与整合分离：原始缓冲区接受浅层 TRIAGE 过滤的条目，活跃 wiki 仅在定期 CONSOLIDATE 周期中修改；核心理由是流式一致性判断是自密封的——单条矛盾条目会被立即隔离，使主导解释永远不更新 |
| [三纠正通道](../cards/three-correction-channels.md) | `three-correction-channels` | concept | 伴侣记忆框架的安全故事：三个不同时间尺度的纠正通道——代理内整合周期（小时到天）、跨代理联邦（周到年）、基模型演进（月到年）；没有单一通道充分，组合构成非平凡但明确部分的安全叙事 |
| [TRIAGE 浅层过滤器](../cards/triage-shallow-filter.md) | `triage-shallow-filter` | operational_rule | 是伴侣记忆框架中摄取操作的合规级别约束：TRIAGE 只做垃圾拒绝、去重、结构验证、时间戳分配，禁止读取活跃 wiki 或执行语义矛盾解决；一旦 TRIAGE 开始做一致性工作，架构就退回流式模式、自密封问题回归 |
| [活力评分公式](../cards/vitality-score-formula.md) | `vitality-score-formula` | mechanism | 伴侣记忆框架中 DECAY 操作使用的多信号保留度量：recency + frequency + task_predictive_utility + memory_gravity - summarization_distortion；... |

## Agent Memory (Agent 记忆系统)

(22 cards)

| Title | canonical_concept | Type | Summary |
|-------|-------------------|------|---------|
| [Agent 记忆四阶段生命周期](../cards/agent-memory-lifecycle-phases.md) | `agent-memory-lifecycle-phases` | concept | Cognition 产品提出 agent 记忆的四阶段模型：Evidence（会话痕迹成为类型化学习事件）→ Consolidation（原始痕迹压缩为人工审批的技能）→ Decay（召回率与新鲜度随时间建模）→ Teaching（下... |
| [先查后做的 Agent 工作循环](../cards/ask-first-retrieve-loop.md) | `ask-first-retrieve-loop` | mechanism | Cognition 的四步 agent 工作循环：任务开始时先查询团队已有技能（Ask first）→ 捕获工作证据（Capture work）→ 起草并审批技能（Save skills）→ 未来 agent 加载已有技能后再行动（R... |
| [双时间线事实建模](../cards/bi-temporal-fact-model.md) | `bi-temporal-fact-model` | mechanism | Graphiti 对每条 edge/fact 维护两条时间线：事件时间线 T（事实何时为真）和事务时间线 T'（数据何时被摄入系统），通过四个时间戳实现动态对话数据的时序建模 |
| [确认优先的技能捕获规则](../cards/confirm-first-skill-capture.md) | `confirm-first-skill-capture` | operational_rule | Cognition 的设计规则：系统自动起草技能文档（SKILL.md），但必须等待人类明确批准后才保存到团队共享空间，防止未经审核的工作流污染团队知识库 |
| [情景记忆与语义记忆的双存储设计](../cards/episodic-semantic-memory-duality.md) | `episodic-semantic-memory-duality` | concept | Zep 同时存储原始事件数据（episodic）和提取的概念关联（semantic），镜像人类记忆心理学中情景记忆与语义记忆的区分，使 agent 形成更精细的记忆结构 |
| [LLM 事件摘要的五类错误分类](../cards/event-summarization-error-taxonomy.md) | `event-summarization-error-taxonomy` | distinction | LoCoMo 对 LLM 事件摘要的手动分析识别出五类主要错误：信息缺失（时序/因果连接失败）、幻觉（填充无关细节）、对话线索误读（如幽默当真）、说话者归属错误、显著性判断错误（将无关寒暄识别为重要事件） |
| [可执行指引 vs 上下文堆积](../cards/executable-guidance-vs-context-pile.md) | `executable-guidance-vs-context-pile` | distinction | Cognition 的核心区分：通用知识库（company brain）存储上下文，agent 记忆系统应提供可执行指引——包含步骤、检查点、失败模式、作者归属和结果历史的结构化技能，而非一堆笔记 |
| [LoCoMo 超长期对话记忆评测基准](../cards/locomo-benchmark.md) | `locomo-benchmark` | source_claim | 首个超长期多模态对话记忆评测基准，50 段对话各含约 300 轮 / 9K tokens / 最多 35 个会话，覆盖 QA（五类推理）、事件图摘要、多模态对话生成三项任务，人类 QA F1=87.9 远超最佳模型 41.4 |
| [LoCoMo 对话记忆 QA 的五类推理维度](../cards/locomo-five-reasoning-types.md) | `locomo-five-reasoning-types` | distinction | 将对话记忆的 QA 评测分为 single-hop（36%）、multi-hop（14.6%）、temporal reasoning（20.6%）、open-domain knowledge（3.9%）、adversarial（24.... |
| [长上下文 LLM 对对抗性问题的脆弱性](../cards/long-context-adversarial-vulnerability.md) | `long-context-adversarial-vulnerability` | source_claim | 随上下文窗口从 4K 扩展到 16K，GPT-3.5-turbo-16K 在对抗性问题上的 F1 从 13.1% 暴跌至 2.1%，而受限窗口的 GPT-4-turbo 达 70.2%，说明长上下文易误导模型生成幻觉 |
| [长上下文模型的理解假象](../cards/long-context-comprehension-illusion.md) | `long-context-comprehension-illusion` | source_claim | LoCoMo 事件摘要任务中长上下文 GPT-3.5-turbo-16K（FactScore F1=39.9）反而低于基座 GPT-3.5-turbo（F1=45.9），精度降 3.0% 召回降 8.7%，表明长上下文模型可能抓住事实... |
| [LongMemEval 上下文压缩与准确率提升](../cards/longmemeval-context-compression.md) | `longmemeval-context-compression` | source_claim | Zep 在 LongMemEval 基准上将平均上下文从 115k 压缩至 1.6k tokens，同时提升准确率最高 18.5%、降低延迟 90%，但在 single-session-assistant 类问题上表现下降 |
| [记忆 CRUD 操作分类法](../cards/memory-crud-operation-taxonomy.md) | `memory-crud-operation-taxonomy` | mechanism | Mem0 将记忆更新分类为四种操作：ADD（无语义等价记忆时新增）、UPDATE（增强已有记忆的信息内容）、DELETE（删除被新事实矛盾的记忆）、NOOP（事实已存在或不相关），由 LLM 通过 tool call 自主判断而非使用... |
| [记忆提取-更新双阶段管线](../cards/memory-extraction-update-pipeline.md) | `memory-extraction-update-pipeline` | mechanism | Mem0 提出的增量式记忆管理架构：提取阶段将新消息对与上下文摘要合并后由 LLM 抽取候选事实；更新阶段将候选事实与已有记忆做语义比对并由 LLM 通过 tool call 决定执行 ADD/UPDATE/DELETE/NOOP 操作 |
| [记忆系统 vs RAG 的显著性优势](../cards/memory-vs-rag-salience.md) | `memory-vs-rag-salience` | source_claim | Mem0 实验表明提取显著事实的记忆系统（Judge 67-68%）一致优于检索原始文本块的 RAG（最高 61%），因为记忆系统将对话历史转化为简洁结构化表示以减少噪声并提供更精确的线索 |
| [观察断言式记忆表示优于原始对话检索](../cards/observation-based-memory-representation.md) | `observation-based-memory-representation` | mechanism | 将对话轮次转化为关于说话者的断言式陈述（observations）作为检索单元，在 LoCoMo QA 中以 top-5 获得最佳 F1=41.4，优于原始对话 31.7 和摘要 29.9，因为消除了共指和对话噪声 |
| [原始轨迹记忆与整合记忆的脆弱性差异](../cards/raw-vs-consolidated-memory-vulnerability.md) | `raw-vs-consolidated-memory-vulnerability` | distinction | agent 记忆有两种范式：原始轨迹记忆直接存储完整观察-行动对作为上下文示例，整合记忆通过 LLM 摘要/反思进行处理；前者因保留了 agent 观察的精确文本（含恶意内容）而对环境注入攻击更脆弱，后者的处理过程可能过滤或转换恶意内... |
| [检索量与信噪比的权衡效应](../cards/retrieval-snr-tradeoff.md) | `retrieval-snr-tradeoff` | mechanism | LoCoMo 实验表明增加检索数量（top-k）可反而降低 QA 性能——observation 从 top-5 的 F1=41.4 降至 top-50 的 37.8，因为更多检索结果引入噪声干扰模型对正确上下文的识别 |
| [搜索-重排-构造三步检索管线](../cards/search-rerank-construct-pipeline.md) | `search-rerank-construct-pipeline` | mechanism | Zep 的记忆检索形式化为 f(alpha)=chi(rho(phi(alpha)))=beta，即搜索（召回候选边/节点）、重排（提升精度）、构造（转为文本上下文）三步组合 |
| [静态 RAG 与动态 agent 记忆的鸿沟](../cards/static-rag-dynamic-memory-gap.md) | `static-rag-dynamic-memory-gap` | distinction | 当前 RAG 方法聚焦于广泛领域知识和静态语料（文档内容很少变化），而企业 agent 需要从持续对话和业务数据中动态集成知识，这种根本差距需要知识图谱等新方法来弥合 |
| [时序知识图谱的三层子图架构](../cards/temporal-knowledge-graph-three-tier.md) | `temporal-knowledge-graph-three-tier` | mechanism | Zep/Graphiti 将 agent 记忆组织为 episode 子图（原始数据）、semantic entity 子图（提取的实体与关系）、community 子图（聚类摘要）三层递进结构 |
| [时序推理是 LLM 对话记忆中最困难的能力维度](../cards/temporal-reasoning-difficulty.md) | `temporal-reasoning-difficulty` | source_claim | LoCoMo QA 中时序推理与人类差距最大（73%），即便最佳 RAG（observation）也仅达 42.1 vs 人类 92.6，LLM 难以理解对话中的时间概念和时序线索，与独立时序推理基准 TRAM 的发现一致 |

## Memory Systems (记忆系统通用)

(12 cards)

| Title | canonical_concept | Type | Summary |
|-------|-------------------|------|---------|
| [AI 记忆操作系统框架](../cards/ai-memory-operating-system.md) | `ai-memory-operating-system` | concept | 是 Jack Roberts 提出的框架：将 AI 记忆视为操作系统级组件，Obsidian/markdown 是可读的长期记忆选项， Pinecone/vector 是可扩展的语义搜索选项 |
| [先提取后阅读的记忆读取策略](../cards/extract-then-read-memory-strategy.md) | `extract-then-read-memory-strategy` | mechanism | 在记忆系统的阅读阶段，应用 Chain-of-Note（先从每个记忆项提取相关信息再推理）结合 JSON 结构化格式呈现检索结果，将长上下文阅读分解为"复制关键细节"和"基于精简笔记推理"两步，即使在完美检索条件下也能带来高达 10 ... |
| [事实增强的索引键扩展](../cards/fact-augmented-key-expansion.md) | `fact-augmented-key-expansion` | mechanism | 将从记忆值中提取的用户事实拼接到原始值上作为索引键，实现多路径检索；相比仅用值本身作键，平均提升 recall@k 9.4%、下游 QA 准确率 5.4%；单独使用压缩形式作键反而不如原始值 |
| [LightMem 三阶段记忆架构](../cards/lightmem-three-stage-memory.md) | `lightmem-three-stage-memory` | mechanism | 借鉴人类 Atkinson-Shiffrin 认知模型，将 LLM 记忆系统分为感觉记忆（轻量压缩+主题分组）、短期记忆（主题感知的整合摘要）、长期记忆（离线 sleep-time 更新）三个互补阶段，在性能与效率间取得平衡。 |
| [LoCoMo 反思-回应双层记忆代理架构](../cards/locomo-reflect-respond-architecture.md) | `locomo-reflect-respond-architecture` | mechanism | LoCoMo 代理采用双层记忆：短期记忆为逐会话递增摘要（avg 127.4 tokens），长期记忆为对话轮次的 observation 断言（avg 18.2 tokens），回复时综合最新摘要+检索的相关 observation... |
| [LongMemEval 五项核心长期记忆能力](../cards/longmemeval-five-memory-abilities.md) | `longmemeval-five-memory-abilities` | distinction | 将聊天助手的长期记忆评估分解为五项核心能力：信息提取(IE)、跨会话推理(MR)、知识更新(KU)、时间推理(TR)、拒答(ABS)，覆盖了先前基准遗漏的关键维度如知识更新与助手侧信息回忆 |
| [LLM 记忆系统的开销问题](../cards/memory-augmentation-overhead.md) | `memory-augmentation-overhead` | source_claim | 现有 LLM 记忆系统虽使模型超越无状态交互，但普遍引入大量时间和计算开销，成为记忆增强生成的核心瓶颈。 |
| [记忆覆写与遗漏两种失败模式](../cards/memory-overwrite-vs-omission-failure.md) | `memory-overwrite-vs-omission-failure` | distinction | 商业记忆系统呈现两种互补的失败模式：ChatGPT 在压缩历史时覆写关键信息（先记后丢），Coze 则经常未能记录间接提供的用户信息（从未记下），揭示了可靠个性化与效率之间的潜在权衡 |
| [记忆存储粒度权衡（会话/轮次/事实）](../cards/memory-value-granularity-tradeoff.md) | `memory-value-granularity-tradeoff` | mechanism | 在对话记忆系统中，将会话分解为轮次（round）级别是比整个会话（session）更优的存储粒度；进一步压缩为事实/摘要虽降低 token 消耗但因信息丢失损害总体 QA 性能，唯一例外是跨会话推理任务因事实格式的一致性而受益 |
| [命名空间-键值记忆数据模型](../cards/namespace-key-memory-model.md) | `namespace-key-memory-model` | mechanism | 是 LangChain/LangGraph 用于持久化 agent 长期记忆的数据模型：以 JSON 文档为记忆单元，按层级命名空间（元组）+ 唯一键组织，支持精确过滤与向量相似度混合检索 |
| [睡眠期离线记忆巩固机制](../cards/sleep-time-memory-consolidation.md) | `sleep-time-memory-consolidation` | mechanism | 将 LLM 记忆系统的长期记忆巩固过程从在线推理中解耦为离线程序，使测试时在线成本进一步大幅降低（token 减少最高 106x/117x，API 调用减少最高 159x/310x）。 |
| [工具中介的记忆访问模式](../cards/tool-mediated-memory-access.md) | `tool-mediated-memory-access` | mechanism | 是 LangChain agent 通过工具函数间接访问长期记忆的架构模式：agent 不直接读写 store，而是调用声明了 ToolRuntime 参数的工具函数，由工具代为执行 get/put/search 操作 |

## MemGPT (MemGPT 系统)

(12 cards)

| Title | canonical_concept | Type | Summary |
|-------|-------------------|------|---------|
| [DMR 基准测试的局限性](../cards/dmr-benchmark-inadequacy.md) | `dmr-benchmark-inadequacy` | source_claim | Zep 论文批评 MemGPT 的 DMR 基准测试：每段对话仅 60 条消息可放入上下文窗口、仅含单轮事实检索问题、未反映企业场景，简单全上下文方法即可达 94-98% 准确率 |
| [MemGPT 对话开场白实验结果](../cards/memgpt-conversation-opener-results.md) | `memgpt-conversation-opener-results` | source_claim | 评估代理利用多会话记忆生成吸引性开场白的能力，MemGPT 的开场白在 persona 相似度（CSIM）上达到甚至超过人类手写水平，倾向于更冗长且覆盖更多 persona 信息 |
| [MemGPT 深度记忆检索实验结果](../cards/memgpt-deep-memory-retrieval-results.md) | `memgpt-deep-memory-retrieval-results` | source_claim | 基于 MSC 数据集的一致性评估中，MemGPT+GPT-4 Turbo 准确率 93.4% 大幅超越基线 35.3%；基线使用有损摘要而 MemGPT 通过分页搜索访问完整对话历史，底层 LLM 能力是关键瓶颈 |
| [MemGPT 文档问答的上下文无关扩展性](../cards/memgpt-document-qa-scaling.md) | `memgpt-document-qa-scaling` | source_claim | 在基于 NaturalQuestions-Open 的文档 QA 任务中，MemGPT 性能不受文档数量增加影响，而固定上下文基线受限于检索器性能和截断降质；MemGPT 通过多次查询 archival storage 并迭代分页突破... |
| [MemGPT 事件驱动控制流](../cards/memgpt-event-driven-control-flow.md) | `memgpt-event-driven-control-flow` | mechanism | MemGPT 中事件（events）触发 LLM 推理，事件类型包括用户消息、系统消息（如内存压力警告）、用户交互（如登录/上传通知）、定时事件（允许 LLM 无需用户输入自主运行），类比 OS 中断管理 |
| [MemGPT 函数链与心跳机制](../cards/memgpt-function-chaining.md) | `memgpt-function-chaining` | mechanism | 通过 request_heartbeat=true 标志让函数执行后立即将控制权交回 LLM 处理器而非等待下一个外部事件，实现多步连续函数调用，支持分页浏览搜索结果和跨文档信息汇集 |
| [MemGPT 主上下文三段式结构](../cards/memgpt-main-context-structure.md) | `memgpt-main-context-structure` | mechanism | 将 LLM prompt tokens 分为 system instructions（只读，控制流与函数说明）、working context（固定大小读写块，存储关键事实）、FIFO queue（滚动消息历史，首位存递归摘要），三者... |
| [MemGPT 两级内存层次结构](../cards/memgpt-memory-hierarchy.md) | `memgpt-memory-hierarchy` | mechanism | 将 LLM 存储分为 main context（prompt tokens = RAM，LLM 可直接访问）和 external context（recall storage + archival storage = 磁盘，需通过函数... |
| [MemGPT 嵌套键值检索与多跳能力](../cards/memgpt-nested-kv-retrieval.md) | `memgpt-nested-kv-retrieval` | source_claim | 扩展了 KV 检索任务使 value 可能也是 key 需要多跳查找；MemGPT+GPT-4 在 0-4 层嵌套中性能稳定，而 GPT-4/GPT-4 Turbo 基线在 3 层嵌套时降至 0%，证明函数链支撑多步信息汇集能力 |
| [MemGPT 队列驱逐与内存压力机制](../cards/memgpt-queue-eviction-policy.md) | `memgpt-queue-eviction-policy` | mechanism | 在 prompt tokens 达到 warning token count（如 70%）时插入内存压力系统消息让 LLM 主动保存重要信息，达到 flush token count（如 100%）时驱逐消息并生成递归摘要，被驱逐消息... |
| [MemGPT 自主内存编辑与检索](../cards/memgpt-self-directed-memory.md) | `memgpt-self-directed-memory` | mechanism | LLM 处理器输出被解析为函数调用，自主决定何时在上下文层级间移动数据、更新 working context、搜索 archival/recall storage；函数执行结果（含运行时错误）反馈回 LLM 形成闭环，分页机制防止检索溢出 |
| [虚拟上下文管理](../cards/virtual-context-management.md) | `virtual-context-management` | mechanism | 借鉴操作系统虚拟内存分页机制，通过在 LLM 有限上下文窗口（类比 RAM）与外部存储（类比磁盘）之间移动数据，为 LLM 提供无限上下文的幻觉 |

## RAG & Retrieval (RAG 与检索)

(20 cards)

| Title | canonical_concept | Type | Summary |
|-------|-------------------|------|---------|
| [ARES 自动化 RAG 评估框架](../cards/ares-rag-evaluation-framework.md) | `ares-rag-evaluation-framework` | concept | ARES 通过合成数据微调轻量 LM 评审 + PPI 校准，仅需数百条人工标注即可自动评估 RAG 系统，且跨领域迁移鲁棒 |
| [分块大小权衡](../cards/chunk-size-tradeoff.md) | `chunk-size-tradeoff` | mechanism | 是 RAG 管线中文档分块大小（典型 256-512 token）的核心权衡：太小则丢失上下文，太大则检索噪声增大；朴素固定大小分块丢弃文档结构，语义分块和混合搜索是演进方向 |
| [声明级蕴含检验评估方法](../cards/claim-level-entailment-evaluation.md) | `claim-level-entailment-evaluation` | mechanism | 将文本分解为原子声明（claim），再逐一检查每个声明是否被参考文本蕴含；相比 response-level 评估（BLEU/ROUGE/BERTScore），该方法能捕捉长文本回答中正确与错误声明的混合分布，RAGChecker 在... |
| [上下文利用率是 RAG 性能的关键生成器指标](../cards/context-utilization-as-performance-key.md) | `context-utilization-as-performance-key` | source_claim | RAGChecker 实验发现在所有生成器指标中，上下文利用率（context utilization）与整体 F1 的相关性最强，且在不同检索器间相对稳定，意味着改善检索器可直接通过稳定的 CU 转化为整体 recall 提升 |
| [上下文利用率-噪声敏感度-忠实度三难困境](../cards/context-utilization-noise-faithfulness-trilemma.md) | `context-utilization-noise-faithfulness-trilemma` | mechanism | RAGChecker 实验发现通过 prompt 优化同时改善 context utilization（59.2->63.7）、faithfulness（92.2->93.6）和降低 noise sensitivity（35.4->3... |
| [Agentic ROI 成本独立性假设批判](../cards/cost-independence-assumption.md) | `cost-independence-assumption` | distinction | 指 Liu et al. (2026) Agentic ROI 公式中隐含的三个未经检验的假设（成本/质量/时间独立性）， 在传统 RAG 范式下大体成立但引入持久化知识层后全部失效 |
| [双路检索策略（实体锚定 + 语义三元组）](../cards/dual-retrieval-entity-semantic.md) | `dual-retrieval-entity-semantic` | mechanism | Mem0^g 实现两种互补检索路径：实体锚定法先识别查询中的实体再探索其关系子图；语义三元组法将整个查询编码为向量与所有关系三元组做细粒度相似度匹配，前者适合定向实体查询后者适合宽泛概念查询 |
| [三种互补搜索方法的混合检索](../cards/hybrid-triple-search-complementarity.md) | `hybrid-triple-search-complementarity` | mechanism | Zep 组合三种搜索方法：余弦相似度（语义相似）、BM25 全文搜索（词汇相似）、广度优先图搜索（上下文相似），分别捕获不同维度的相关性 |
| [开源模型与闭源模型在上下文辨别力上的差距](../cards/open-source-vs-proprietary-context-discrimination.md) | `open-source-vs-proprietary-context-discrimination` | source_claim | RAGChecker 实验发现开源模型（Llama3/Mixtral）具有更高的 faithfulness 但这主要源于更高的 noise sensitivity——盲目信任上下文；GPT-4 的 context utilizatio... |
| [RAG 组件评估三维度：上下文相关性、回答忠实性、回答相关性](../cards/rag-component-evaluation-tri-dimension.md) | `rag-component-evaluation-tri-dimension` | distinction | ARES 将 RAG 评估分解为上下文相关性（检索质量）、回答忠实性（生成是否基于上下文）、回答相关性（生成是否回答问题）三个正交组件级维度 |
| [RAG 评估框架的元评估方法论](../cards/rag-evaluation-meta-evaluation.md) | `rag-evaluation-meta-evaluation` | mechanism | RAGChecker 提出的元评估方法：构建 280 个成对人类偏好实例（10 领域 x 28 系统对），计算评估指标得分差与人类偏好标签的相关性；RAGChecker 在 correctness/completeness/overa... |
| [RAG 评估三维度分解](../cards/rag-evaluation-tri-dimension.md) | `rag-evaluation-tri-dimension` | distinction | RAGAS 将 RAG 管道评估分解为三个独立维度：检索系统识别相关且聚焦的上下文段落的能力、LLM 忠实利用上下文的能力、生成输出本身的质量。 |
| [RAG 生成器的自有知识指标](../cards/rag-generator-self-knowledge.md) | `rag-generator-self-knowledge` | concept | RAGChecker 定义的生成器指标：回答中正确但不被任何检索块蕴含的声明比例，反映生成器依赖自身参数化知识而非检索上下文的程度；在 RAG 场景中该值越低越好，因为 RAG 期望生成器完全依赖检索上下文 |
| [RAGAS 无参考评估框架](../cards/ragas-reference-free-rag-evaluation.md) | `ragas-reference-free-rag-evaluation` | mechanism | RAGAS 是一个无需人工标注黄金答案即可评估 RAG 管道的自动化框架，通过消除对 ground truth 的依赖来加速 RAG 架构的评估迭代周期。 |
| [RAGChecker 三层诊断指标体系](../cards/ragchecker-three-tier-metrics.md) | `ragchecker-three-tier-metrics` | mechanism | RAGChecker 面向用户和开发者两类角色设计三层指标：整体层（precision/recall/F1）、检索器层（claim recall / context precision）、生成器层（faithfulness / noi... |
| [相关噪声与无关噪声敏感度的区分](../cards/relevant-vs-irrelevant-noise-sensitivity.md) | `relevant-vs-irrelevant-noise-sensitivity` | distinction | RAGChecker 将生成器的噪声敏感度拆分为相关块噪声（NS-I）和无关块噪声（NS-II），实验显示 NS-I 始终远高于 NS-II，揭示生成器以块为单位信任上下文——相关块被整体信任其噪声也被采纳，而无关块仅有最小影响 |
| [Rerank 策略：多次采样并按引用 recall 选优以提升引用质量](../cards/rerank-citation-boost.md) | `rerank-citation-boost` | mechanism | 对每个问题随机采样4次回答，按自动 citation recall 分数选最优，在 ASQA 上将 citation recall 从 73.6% 提升至 84.8%（+11.2pp），在 ELI5 上从 51.1% 提升至 69.3... |
| [检索质量是引用生成的根本瓶颈](../cards/retrieval-as-citation-bottleneck.md) | `retrieval-as-citation-bottleneck` | source_claim | 检索 recall 构成模型正确性的上界；即使使用 oracle 段落，模型正确性仍低于检索 recall，表明 LLM 难以充分利用上下文中的正确答案；GTR 优于 DPR，更多段落在 ChatGPT 上收益饱和但 GPT-4 能持续受益 |
| [检索改善引发的忠实度与噪声敏感度权衡](../cards/retrieval-improvement-faithfulness-noise-tradeoff.md) | `retrieval-improvement-faithfulness-noise-tradeoff` | mechanism | RAGChecker 实验表明更好的检索器或更多上下文同时提升生成器忠实度（faithfulness 87.9->92.9）和噪声敏感度（NS-I 26.2->28.9），因为固定大小分块使相关块不可避免地携带噪声，生成器的块级信任无... |
| [意义建构查询与检索查询的区分](../cards/sensemaking-vs-retrieval-query.md) | `sensemaking-vs-retrieval-query` | distinction | 区分需要全局理解语料库的意义建构查询（如主题趋势）与可通过局部文本片段回答的检索查询，前者是 QFS 任务而非检索任务 |

## GraphRAG (图谱 RAG)

(13 cards)

| Title | canonical_concept | Type | Summary |
|-------|-------------------|------|---------|
| [图模块性作为层级摘要的结构基础](../cards/graph-modularity-for-summarization.md) | `graph-modularity-for-summarization` | concept | GraphRAG 利用知识图谱固有的模块性——将图分割为嵌套模块化社区的能力——作为层级摘要的结构基础，这是此前图+RAG 方法未曾探索的图属性 |
| [GraphRAG 层级社区检测与摘要机制](../cards/graphrag-community-hierarchy.md) | `graphrag-community-hierarchy` | mechanism | 使用 Leiden 算法递归检测知识图谱中的层级社区，每层覆盖互斥穷尽的节点分区，LLM 自底向上生成社区摘要实现分治式全局理解 |
| [GraphRAG 社区层级的 token 效率与回答质量权衡](../cards/graphrag-community-level-tradeoff.md) | `graphrag-community-level-tradeoff` | distinction | 根层级社区摘要 C0 仅需最大 token 量的 2.3-2.6%，但仍保持对向量 RAG 72% 全面性和 62% 多样性的胜率；低层级 C3 更详细但需 67-74% token |
| [GraphRAG 全面性与多样性大幅优于向量 RAG 的实证结果](../cards/graphrag-comprehensiveness-diversity-result.md) | `graphrag-comprehensiveness-diversity-result` | source_claim | 在百万 token 数据集上 GraphRAG 全面性胜率 72-83%、多样性 62-82%（p<.001），但向量 RAG 在直接性上占优；全面性与直接性存在内在对立 |
| [GraphRAG 知识投毒防御空白](../cards/graphrag-defense-gap.md) | `graphrag-defense-gap` | source_claim | 现有最先进的防御方法无法检测针对 GraphRAG 的知识投毒攻击，该安全领域仍处于基本未探索状态 |
| [GraphRAG 全局语义理解方法](../cards/graphrag-global-sensemaking.md) | `graphrag-global-sensemaking` | mechanism | 通过 LLM 构建实体知识图谱并预生成层级社区摘要，以 map-reduce 方式回答传统向量 RAG 无法处理的全局语义理解（sensemaking）查询 |
| [GraphRAG 知识投毒攻击](../cards/graphrag-knowledge-poisoning-attack.md) | `graphrag-knowledge-poisoning-attack` | concept | GraphRAG 依赖 LLM 从原始文本提取知识构建图谱，攻击者仅需修改少量原文词语即可显著扭曲生成的知识图谱并误导下游推理 |
| [GraphRAG 查询时 Map-Reduce 应答流程](../cards/graphrag-map-reduce-query.md) | `graphrag-map-reduce-query` | mechanism | 在查询时将社区摘要随机分块后并行生成带有用性评分的中间回答（map），再按评分降序聚合为最终全局回答（reduce） |
| [GraphRAG 自我反思拾遗实体提取技术](../cards/graphrag-self-reflection-gleaning.md) | `graphrag-self-reflection-gleaning` | mechanism | 通过将已提取实体回馈给 LLM 并用 logit bias 强制评估完整性，迭代"拾遗"遗漏实体，使大 chunk 下的实体提取量可接近小 chunk 水平（600 token chunk + 3 次迭代从约 9k 增至约 27k 实... |
| [GraphRAG 中小上下文窗口反而更优的发现](../cards/graphrag-small-context-window-advantage.md) | `graphrag-small-context-window-advantage` | source_claim | GraphRAG 评估中 8k 上下文窗口在全面性上普遍优于 16k/32k/64k（平均胜率 58.1%），呼应 lost-in-the-middle 现象，因此采用 8k 作为统一设置 |
| [定向知识投毒攻击（TKPA）](../cards/targeted-kpa.md) | `targeted-kpa` | mechanism | 利用图论分析定位知识图谱中的脆弱节点并用 LLM 改写对应叙述文本，以 93.1% 成功率精确控制特定问答结果且保持文本自然流畅 |
| [文本微扰的图谱放大效应](../cards/text-perturbation-amplification.md) | `text-perturbation-amplification` | mechanism | GraphRAG 图谱构建过程将极小的文本修改（<0.05%）放大为大规模图谱结构变化，暴露了 LLM 驱动的知识提取管道的内在脆弱性 |
| [通用知识投毒攻击（UKPA）](../cards/universal-kpa.md) | `universal-kpa` | mechanism | 利用代词和依存关系等语言学线索篡改全局影响力词汇，仅修改不到 0.05% 的文本即可将 GraphRAG 问答准确率从 95% 降至 50% |

## Knowledge Graph (知识图谱)

(5 cards)

| Title | canonical_concept | Type | Summary |
|-------|-------------------|------|---------|
| [标签传播动态社区检测](../cards/dynamic-community-detection.md) | `dynamic-community-detection` | mechanism | Graphiti 选择标签传播算法（而非 Leiden）进行社区检测，因其支持简单的动态扩展——新实体加入时仅需单步邻居投票即可分配社区，显著降低延迟和 LLM 推理成本 |
| [边失效与动态知识更新机制](../cards/edge-invalidation-mechanism.md) | `edge-invalidation-mechanism` | mechanism | Graphiti 通过 LLM 比较新边与已有语义相关边来检测矛盾，当发现时间重叠的矛盾时，将旧边的 t_invalid 设为新边的 t_valid，始终优先采纳新信息 |
| [混合搜索实体消解流程](../cards/entity-resolution-hybrid-search.md) | `entity-resolution-hybrid-search` | mechanism | Graphiti 的实体消解分三步：1024维向量嵌入余弦相似度搜索 + 全文搜索找候选、LLM 判定是否重复、预定义 Cypher 查询写入图（避免 LLM 生成查询的幻觉风险） |
| [图记忆在时序推理中的优势](../cards/graph-memory-temporal-advantage.md) | `graph-memory-temporal-advantage` | distinction | Mem0^g 的图结构记忆在时序推理任务上显著优于扁平自然语言记忆（Judge 58.13 vs 55.51），但在单跳和多跳任务上反而引入冗余开销，表明图结构的收益与查询类型高度相关 |
| [无损 Episode 数据存储与双向溯源](../cards/non-lossy-episodic-store.md) | `non-lossy-episodic-store` | operational_rule | Graphiti 的 episode 子图作为无损数据存储保留所有原始输入，并通过双向索引支持正向/反向遍历：语义制品可追溯到源 episode 用于引用，episode 可快速检索其相关实体 |

## Citation (引用生成与评估)

(5 cards)

| Title | canonical_concept | Type | Summary |
|-------|-------------------|------|---------|
| [ALCE：首个自动化 LLM 引用评估基准](../cards/alce-citation-benchmark.md) | `alce-citation-benchmark` | concept | 是首个可复现的 LLM 引用生成自动评估基准，要求端到端系统从语料库检索证据并生成带引用的回答，解决了此前依赖商业搜索引擎和人工评估难以复现对比的问题 |
| [引用评估三维度框架：流畅度-正确性-引用质量](../cards/citation-quality-tri-dimension.md) | `citation-quality-tri-dimension` | mechanism | ALCE 沿流畅度（MAUVE）、正确性（数据集特定指标）、引用质量（NLI 驱动的 recall/precision）三个维度评估，三者联合构成抗捷径的鲁棒评估 |
| [LLM 引用支持缺口：最佳模型仍有约 50% 陈述缺乏完整引用](../cards/citation-support-gap.md) | `citation-support-gap` | source_claim | 在 ALCE 基准上，即使最佳模型（ChatGPT/GPT-4）在 ELI5 数据集上仍有约 50% 的陈述缺乏被引段落的完整支持，反映当前 LLM 引用生成能力的根本不足 |
| [指令微调对 LLM 引用能力的显著提升效应](../cards/instruction-tuning-citation-effect.md) | `instruction-tuning-citation-effect` | source_claim | 指令微调显著提升 LLM 引用能力：ASQA 上 LLaMA-13B 的 citation recall 仅 10.6%，Vicuna-13B 达 51.1%（+40.5pp）；原始 LLaMA 能从上下文复制事实但无法准确标注引用源... |
| [基于 NLI 模型的引用验证机制](../cards/nli-based-citation-verification.md) | `nli-based-citation-verification` | mechanism | ALCE 使用 NLI 模型 TRUE（T5-11B）自动评估引用质量：citation recall 检查引用段落拼接后是否蕴含陈述，citation precision 检查去除某引用后支持是否不变；与人工评估 Cohen's k... |

## Evaluation & Benchmarks (评估与基准)

(7 cards)

| Title | canonical_concept | Type | Summary |
|-------|-------------------|------|---------|
| [基于 LLM 人设生成的自适应基准测试](../cards/adaptive-benchmarking-persona-generation.md) | `adaptive-benchmarking-persona-generation` | mechanism | 用 LLM 从语料库描述推断潜在用户人设、任务和全局理解问题（K*N*M 组合），为缺乏标准答案的 sensemaking 查询生成领域特定评估基准 |
| [全上下文方法的准确率天花板效应](../cards/full-context-accuracy-ceiling.md) | `full-context-accuracy-ceiling` | source_claim | Mem0 LOCOMO 实验中全上下文方法（~26K token）达到最高 Judge=72.90%，但 p95 延迟 17.1 秒，而 Mem0（1764 token）以 Judge=66.88% 实现 p95=1.44 秒（91%... |
| [词汇匹配指标 vs 语义评估的鸿沟](../cards/lexical-vs-semantic-eval-gap.md) | `lexical-vs-semantic-eval-gap` | distinction | Mem0 论文指出 F1 和 BLEU-1 等词汇匹配指标无法捕获事实性错误（如将 March 误为 July 仍得高分），提出 LLM-as-a-Judge 作为语义评估补充，同时引入 10 次独立运行取均值以应对其随机性 |
| [LOCOMO 长期对话记忆基准测试设计](../cards/locomo-benchmark-design.md) | `locomo-benchmark-design` | example_pattern | LOCOMO 包含 10 段长对话（各约 600 轮、26K token），配有平均 200 个问题，分为四类：单跳（单轮事实检索）、多跳（跨会话信息整合）、时序（事件排序与时间推理）、开放域（需外部知识整合），用于全面评估长期对话记忆系统 |
| [长期记忆准确率差距（30-60% 下降）](../cards/long-term-memory-accuracy-gap.md) | `long-term-memory-accuracy-gap` | source_claim | LongMemEval 实证表明，当前商业系统（ChatGPT/Coze）和长上下文 LLM 在持续交互中均出现 30%-64% 的准确率下降；这一差距揭示"构建看似个性化的助手"与"展现真正强大的记忆能力"之间存在根本性鸿沟 |
| [记忆压缩的 token 效率差异](../cards/memory-compression-token-ratio.md) | `memory-compression-token-ratio` | source_claim | Mem0 实验显示不同记忆架构的 token 效率差异悬殊：Mem0 平均 7K token/对话，Mem0^g 14K，原始对话 26K，而 Zep 图谱膨胀至 600K+，原因是 Zep 在每个节点缓存完整摘要且边上存储事实导致大量冗余 |
| [时间感知的查询扩展策略](../cards/time-aware-query-expansion.md) | `time-aware-query-expansion` | mechanism | 针对记忆系统中的时间推理问题，在索引阶段提取事件日期、在检索阶段用 LLM 推断查询的时间范围以过滤无关值；使用强模型（GPT-4o）时平均提升时间推理召回率 6.8%-11.3%，弱模型（8B）因时间范围幻觉反而有害 |

## LLM Context & Scaling (LLM 上下文与扩展)

(4 cards)

| Title | canonical_concept | Type | Summary |
|-------|-------------------|------|---------|
| [上下文窗口扩展的不充分性](../cards/context-extension-insufficiency.md) | `context-extension-insufficiency` | source_claim | Mem0 论文论证即使扩展到 10M token 的上下文窗口也仅推迟而非解决持久记忆问题，原因有二：长期交互必然超越任何窗口上限；主题不连续导致关键信息淹没在无关内容中且注意力机制在远距离 token 上退化 |
| [上下文窗口扩展的递减收益问题](../cards/context-scaling-diminishing-returns.md) | `context-scaling-diminishing-returns` | distinction | MemGPT 论文论证直接扩展 LLM 上下文窗口面临二次方计算开销、长上下文模型存在不均匀注意力分布（中间位置信息利用差）、以及实际文档长度可能远超可行上下文规模等三重困境，为虚拟上下文管理方案提供动机 |
| [有损压缩的引用权衡：摘要/片段提升正确性但损害引用质量](../cards/lossy-compression-citation-tradeoff.md) | `lossy-compression-citation-tradeoff` | mechanism | 将检索段落压缩为摘要或片段可平均缩短6倍，放入更多段落（5→10），提升正确性（ASQA EM 40.4→43.3），但因压缩丢失信息导致引用质量下降（citation recall 73.6→68.9），交互式全文检查（Intera... |
| [权重内化知识的愿景](../cards/weight-internalization-aspiration.md) | `weight-internalization-aspiration` | source_claim | 随 wiki 规模增长，自然产生通过合成数据+微调让 LLM 将知识内化到权重而非仅依赖上下文窗口的愿望 |

## Token Economics (Token 经济学)

(7 cards)

| Title | canonical_concept | Type | Summary |
|-------|-------------------|------|---------|
| [资本化延迟与瞬时延迟](../cards/capitalized-latency.md) | `capitalized-latency` | distinction | 是 token 资本品重分类向延迟维度的推广： Compounding 的 81 秒中 65.7 秒是用户等待的瞬时延迟，15.3 秒是用户已获答案后构建持久制品的 资本化延迟，后者应在未来查询中摊销而非计入当次 ROI 损失 |
| [复利方案在原始 token 成本上从不胜出](../cards/compounding-cost-honesty.md) | `compounding-cost-honesty` | source_claim | 是 Wen & Ku (2026) 的核心诚实发现：Compounding 在任何场景、任何时间跨度下的原始 token 消耗均高于 Chunk-RAG （4查询 47K vs 13.6K, 30天高集中度 3.92M vs 1.02... |
| [动态 Agentic ROI 模型](../cards/dynamic-agentic-roi.md) | `dynamic-agentic-roi` | mechanism | 覆盖率模型）将 Agentic ROI 的成本项 从静态常量推广为 Ci = (1-Hi)*C_generate + Hi*C_retrieve + C_writeback，其中知识库覆盖率 H(t) 遵循凹饱和递推方程 H(i+1)... |
| [投资-收获振荡成本曲线](../cards/invest-harvest-cycle.md) | `invest-harvest-cycle` | example_pattern | 是 Compounding 方案独有的成本轨迹模式：Q1 冷启动 12K→Q2 缓存命中 3K→Q3 搜索回写投资 28K→Q4 复用收获 4K， 呈现尖峰=资本形成、波谷=资本收获的振荡凹曲线，是三种方案中唯一的历史依赖型轨迹 |
| [知识复利效应](../cards/knowledge-compounding.md) | `knowledge-compounding` | concept | 是 Wen & Ku (2026) 对 Agentic ROI 框架的扩展：当持久化知识层存在时，每任务成本不再独立，而是关于知识库覆盖率 H(t) 的递减时间函数，表现为凹饱和曲线 |
| [Token 供需双重红利](../cards/supply-demand-token-dividend.md) | `supply-demand-token-dividend` | concept | 指 NVIDIA 的供给侧优化（token 生产成本指数下降）与知识复利的需求侧优化（每个 token 的持久价值提升） 相互强化，使 token 同时变得更便宜且更有价值，构成 LLM 经济学中最美的双重红利 |
| [Token 资本品重分类](../cards/token-capital-goods.md) | `token-capital-goods` | concept | 是 Wen & Ku (2026) 的核心理论贡献：产生持久化可查询制品的 LLM token 应从消耗品重分类为资本品，具备持久产品、 复利回报、跨模型可继承、负折旧四个资本品属性，类比会计准则 SFAS 86 对软件开发成本的处理 |

## Security & Adversarial (安全与对抗)

(15 cards)

| Title | canonical_concept | Type | Summary |
|-------|-------------------|------|---------|
| [Agent 治理标准合规映射](../cards/agent-governance-standards-mapping.md) | `agent-governance-standards-mapping` | mechanism | Microsoft Agent Governance Toolkit 将治理控制显式映射到 OWASP Agentic AI Top 10（全部覆盖）、NIST AI RMF 1.0 （GOVERN/MAP/MEASURE/MANAG... |
| [Agent 记忆作为持久性攻击面](../cards/agent-memory-persistent-attack-surface.md) | `agent-memory-persistent-attack-surface` | concept | LLM agent 的记忆系统通过存储过去交互来个性化未来任务，但同时创建了一个跨网站、跨会话的持久性攻击面：单次投毒记忆可在任何检索到受污染轨迹的未来任务中反复触发，且能绕过基于权限的防御 |
| [Chaos Monkey 式 Agent 压力测试](../cards/chaos-monkey-agent-stress-testing.md) | `chaos-monkey-agent-stress-testing` | mechanism | 借鉴混沌工程原理，对 web agent 的操作施加概率性扰动（点击丢弃 p=0.4、滚动方向反转 p=1、输入文本 Caesar 密码变换 p=1）来模拟真实部署中的网络延迟、UI 故障等环境噪声，系统性地测试 agent 在压力下... |
| [条件触发器的隐蔽性设计](../cards/conditional-trigger-stealth-design.md) | `conditional-trigger-stealth-design` | mechanism | eTAMP 的攻击载荷使用基于可观察环境特征（URL 模式、任务状态）的条件触发器，确保恶意指令在注入阶段（Task A）保持休眠、在激活阶段（Task B）才触发，实验中 ASR_A 几乎为 0% 验证了该设计的隐蔽性 |
| [环境注入式轨迹记忆投毒攻击](../cards/etamp-environment-memory-poisoning.md) | `etamp-environment-memory-poisoning` | mechanism | 首个通过环境观察单独实现跨会话、跨站点记忆投毒的攻击：攻击者在网页用户生成内容中嵌入恶意指令，agent 浏览后将其存入轨迹记忆，未来在不同网站的任务中被语义检索并触发恶意行为，无需直接访问记忆存储 |
| [挫败利用攻击](../cards/frustration-exploitation-attack.md) | `frustration-exploitation-attack` | mechanism | 当 LLM web agent 在环境压力下（点击丢失、文本乱码、重复失败）陷入挣扎时，其对恶意注入指令的易感性可提高最多 8 倍——挫败状态创造一个"脆弱窗口"使 agent 更倾向于跟从看似提供解决方案的注入指令 |
| [模型能力与安全性的脱钩](../cards/model-capability-security-disconnect.md) | `model-capability-security-disconnect` | source_claim | 更强大的 LLM 模型并不必然更安全：GPT-5.2 尽管任务成功率最高却对记忆投毒表现出显著脆弱性，其更高的环境感知能力同时关联着更高的任务成功率和更大的攻击面 |
| [OWASP Agentic Top 10 框架](../cards/owasp-agentic-top10-framework.md) | `owasp-agentic-top10-framework` | concept | OWASP 发布的针对自主式 agentic AI 系统的十大安全风险框架，由 100+ 专家同行评审，面向构建者/防御者/决策者，将 GenAI 安全生态浓缩为可操作的风险清单 |
| [PoisonedRAG 的 S+I 文本分解策略](../cards/poisonedrag-text-decomposition.md) | `poisonedrag-text-decomposition` | mechanism | PoisonedRAG 将每条恶意文本分解为 P=S⊕I 两个子文本，I 由 LLM 生成以满足生成条件（约 2 次查询），S 在黑盒下直接用目标问题、在白盒下用对抗文本方法优化以满足检索条件，从而同时实现双条件。 |
| [高级 RAG 方案对知识腐蚀攻击的脆弱性](../cards/rag-advanced-scheme-vulnerability.md) | `rag-advanced-scheme-vulnerability` | source_claim | Self-RAG 和 CRAG 等加入检索质量评估的高级 RAG 方案仍被 PoisonedRAG 以 70-87% ASR 攻破，因为恶意文本在语义上确实与目标问题相关，质量过滤器无法将其排除。 |
| [RAG 知识腐蚀攻击](../cards/rag-knowledge-corruption-attack.md) | `rag-knowledge-corruption-attack` | concept | 攻击者向 RAG 知识库注入少量恶意文本（每个目标问题 5 条），即可在百万级文本库中以约 90% 成功率使 LLM 生成攻击者指定答案，跨 8 种 LLM 和多种检索器有效，计算成本极低。 |
| [RAG 知识库作为新攻击面](../cards/rag-knowledge-database-attack-surface.md) | `rag-knowledge-database-attack-surface` | concept | RAG 系统的知识库引入了一个新的、实用的攻击面：攻击者可通过向知识库注入少量恶意文本来操纵 LLM 生成攻击者指定的错误答案。 |
| [RAG 投毒中的参数偏差失效模式](../cards/rag-parametric-bias-failure.md) | `rag-parametric-bias-failure` | distinction | PoisonedRAG 存在两类失败模式：一是恶意文本未被全部检索到（检索条件不完美），二是 LLM 因参数偏差忽略恶意上下文仍输出正确答案——即便恶意文本中也不慎包含了正确答案。 |
| [现有防御对 RAG 知识腐蚀攻击的不充分性](../cards/rag-poisoning-defense-insufficiency.md) | `rag-poisoning-defense-insufficiency` | source_claim | 四种防御策略对 PoisonedRAG 均不充分：释义防御仍允许 79-93% ASR，困惑度检测因恶意文本质量正常而无法区分，去重过滤因 LLM 生成多样性而完全无效，知识扩展在 k=50 时仍有 41% ASR。 |
| [RAG 攻击的检索与生成双条件](../cards/rag-retrieval-generation-dual-condition.md) | `rag-retrieval-generation-dual-condition` | mechanism | 有效的 RAG 知识腐蚀攻击必须同时满足两个必要条件：检索条件（恶意文本被检索到）和生成条件（恶意文本作为上下文时 LLM 生成目标答案），现有基线方法只能满足其中一个条件因而效果不佳。 |

## Governance & Compliance (治理与合规)

(8 cards)

| Title | canonical_concept | Type | Summary |
|-------|-------------------|------|---------|
| [Agent 治理模块化分包架构](../cards/agent-governance-modular-packages.md) | `agent-governance-modular-packages` | concept | Microsoft Agent Governance Toolkit 将 agent 治理分解为八个独立包——Agent OS（策略引擎）、Mesh（发现与信任）、 Runtime（沙箱）、SRE（可靠性）、Compliance（合规... |
| [AI RMF 的自愿性与可信赖性导向](../cards/ai-rmf-voluntary-trustworthiness.md) | `ai-rmf-voluntary-trustworthiness` | concept | NIST AI RMF 1.0 定位为自愿性使用框架，不具备法律强制力，其核心目标是帮助组织在 AI 全生命周期 （设计、开发、使用、评估）中系统性融入可信赖性考量 |
| [数据目录作为企业级 Wiki 的结构等价物](../cards/data-catalog-as-enterprise-wiki.md) | `data-catalog-as-enterprise-wiki` | concept | 受治理的数据目录在结构上等价于 Karpathy 个人 wiki 的企业版：策展摘要=wiki文章、 血缘=反向链接、认证=质量分数、RBAC=访问控制、主动元数据传播=健康检查； 连接（MCP/API）是缺失的环节而非构建 |
| [确定性策略执行](../cards/deterministic-policy-enforcement.md) | `deterministic-policy-enforcement` | mechanism | Microsoft Agent Governance Toolkit 的核心设计原则：agent 治理使用确定性策略执行而非概率性 LLM 判断， 通过 OPA/Rego/Cedar 等引擎实现 Policy-as-Code，保证策略... |
| [框架无关的治理层](../cards/framework-agnostic-governance-layer.md) | `framework-agnostic-governance-layer` | concept | Microsoft Agent Governance Toolkit 将治理设计为与 agent 框架解耦的独立层，通过 Framework Adapter Contract 规范适配器接口，支持 LangChain/CrewAI/A... |
| [治理优先于检索架构](../cards/governance-over-retrieval.md) | `governance-over-retrieval` | source_claim | Atlan 文章的核心论点：企业知识库的真正问题不是检索架构（wiki vs RAG），而是上游数据治理—— 访问控制、新鲜度、并发都是治理问题；规模决定架构，治理决定结果 |
| [NIST AI 600-1 生成式 AI 风险管理框架概况](../cards/nist-ai-600-1-gai-profile.md) | `nist-ai-600-1-gai-profile` | source_claim | NIST 于 2024 年 7 月发布 AI 600-1，作为 AI RMF 1.0 的跨部门生成式 AI 概况文件， 依据行政令 EO 14110 编制，旨在为组织将可信赖性纳入 AI 全生命周期提供自愿性指南 |
| [规范驱动的合规测试](../cards/spec-driven-conformance-testing.md) | `spec-driven-conformance-testing` | mechanism | Microsoft Agent Governance Toolkit 为每个主要组件编写 RFC 2119 形式规范，并配以合规测试（共 13,000+ 测试、 10 份形式规范），用可执行测试取代自然语言约束来定义治理行为的正确性 |

## Enterprise Wiki (企业级 Wiki)

(5 cards)

| Title | canonical_concept | Type | Summary |
|-------|-------------------|------|---------|
| [持续偏移检测](../cards/continuous-drift-detection.md) | `continuous-drift-detection` | mechanism | 是个人 LLM Wiki 按需巡检在企业规模下的演化：从用户触发变为后台循环自动运行， 检测跨千篇文档和百万行代码的偏移，按团队可操作的节奏（周度而非季度）呈现结果 |
| [跨工具实体解析](../cards/cross-tool-entity-resolution.md) | `cross-tool-entity-resolution` | mechanism | 是企业级知识链接从文件内双向链接升级为跨工具语义实体识别的机制；知识图谱需理解 "payments service"在设计文档、GitHub 仓库和 Slack 频道中是同一实体 |
| [知识作为工作副产品](../cards/knowledge-as-work-byproduct.md) | `knowledge-as-work-byproduct` | concept | 是企业 LLM Wiki 的设计原则：知识图谱应作为 PR 合并、Slack 讨论、决策落地等正常工作的 副产品自动增长，而非作为额外的文档工作 |
| [检索与维护的区别](../cards/retrieval-vs-maintenance.md) | `retrieval-vs-maintenance` | distinction | 是企业知识系统的关键区分：大多数企业工具只是检索工具，而 LLM Wiki 的核心贡献是维护循环； 在陈旧内容上做更好的检索只是更快地返回错误答案 |
| [单一策展人瓶颈](../cards/single-curator-bottleneck.md) | `single-curator-bottleneck` | distinction | 是个人 LLM Wiki 向企业扩展时的核心结构性障碍：个人模式成功依赖一个有动力的人控制策展， 企业依赖单一策展人则重新制造它试图解决的 wiki 问题 |

## Wikibase (Wikibase 数据模型)

(9 cards)

| Title | canonical_concept | Type | Summary |
|-------|-------------------|------|---------|
| [Wikibase 概念模型与技术表示的分离](../cards/wikibase-conceptual-model-separation.md) | `wikibase-conceptual-model-separation` | concept | Wikibase 数据模型明确定位为概念模型（"需要支持哪些信息"），与技术表示（"软件应使用哪些数据结构"）和语法表示（"数据在文件中如何表达"）分离，JSON/RDF 序列化由独立文档规定 |
| [Wikibase 数据模型的六项设计要求](../cards/wikibase-data-model-design-goals.md) | `wikibase-data-model-design-goals` | concept | Wikibase 数据模型在六项有时冲突的要求间寻求平衡：覆盖度、简单性、可扩展性、灵活性、可交换性、技术可支持性；同时明确划定模型边界——不规定内部数据结构、导出格式和形式语义 |
| [EntityDescription 的多语言数据容器](../cards/wikibase-entity-description.md) | `wikibase-entity-description` | mechanism | EntityDescription 为每个实体聚合 Statements 和多语言词汇信息（label/description/aliases），其中 label+description 在 Item 中构成给定语言下的唯一键，lab... |
| [Wikibase 实体与数据值的层次划分](../cards/wikibase-entity-value-hierarchy.md) | `wikibase-entity-value-hierarchy` | distinction | Wikibase 将 Value 分为 Entity（Item/Property/Datatype，以 IRI 全局标识，可做 Statement 主语）和 DataValue（数值/字符串/坐标等，以内容标识，不可做主语），这一分层... |
| [Property 的非严格类型设计](../cards/wikibase-flexible-typing.md) | `wikibase-flexible-typing` | concept | Wikibase 数据模型有意不要求 Snak 中的 Value 严格匹配 Property 声明的 Datatype：UI/API 层面强制类型一致，但底层模型允许不匹配，以应对 Datatype 变更后旧数据无法即时全量更新的现实 |
| [Qualifier Snaks 的上下文限定机制](../cards/wikibase-qualifier-mechanism.md) | `wikibase-qualifier-mechanism` | mechanism | Wikibase 中 Statement 的 qualifierSnaks 是对 mainSnak 的上下文限定，用于附加"不直接指向主语"的信息如时间范围、角色、比例等，使单一 Property-Value 断言能表达复合事实 |
| [Snak 的三种认识论状态](../cards/wikibase-snak-triple-epistemology.md) | `wikibase-snak-triple-epistemology` | distinction | Wikibase 用三种 Snak 编码不同的认识论状态：PropertyValueSnak（已知值）、PropertyNoValueSnak（明确无值，区别于"尚未录入"）、PropertySomeValueSnak（存在值但未知）... |
| [Statement 三级排名机制](../cards/wikibase-statement-ranking.md) | `wikibase-statement-ranking` | mechanism | Wikibase 为每条 Statement 赋予 Preferred（最重要/最新）、Normal（正确但次要）、Deprecated（不可靠/已知错误）三级排名，并据此定义 best rank（有 preferred 则取 pre... |
| [Statement 的复合结构](../cards/wikibase-statement-structure.md) | `wikibase-statement-structure` | mechanism | 一条 Statement 由 subject（主语实体）、mainSnak（核心断言）、qualifierSnaks（限定上下文如时间/角色）、referenceRecords（来源证据的 Snak 集合列表）和 rank（排名）五部... |

## Documentation (文档工程)

(3 cards)

| Title | canonical_concept | Type | Summary |
|-------|-------------------|------|---------|
| [Docs as Code 理念](../cards/docs-as-code.md) | `docs-as-code` | concept | 指一种文档哲学：用与代码相同的五类工具（Issue Tracker、版本控制、纯文本标记、代码评审、自动化测试）和相同的开发工作流来编写文档 |
| [文档合并门禁机制](../cards/documentation-merge-gate.md) | `documentation-merge-gate` | mechanism | 指在 docs-as-code 工作流中，若新功能未附带文档则阻止合并，从而激励开发者在功能记忆犹新时撰写文档 |
| [文档共同所有权文化](../cards/documentation-shared-ownership.md) | `documentation-shared-ownership` | concept | 指 docs-as-code 理念所促成的文化转变：技术写作者与开发者双方均对文档拥有所有权感，并协同提升文档质量 |

## Other (其他)

(11 cards)

| Title | canonical_concept | Type | Summary |
|-------|-------------------|------|---------|
| [引用评估中"部分支持"检测的缺失问题](../cards/citation-partial-support-limitation.md) | `citation-partial-support-limitation` | distinction | ALCE 的 NLI 引用精度评估无法区分"部分支持"与"不支持"：当引用 [2] 部分蕴含陈述 s3 且 [4][5] 完全覆盖时，[2] 被错误判为无关；尝试用 ChatGPT 做三级判断效果差，留为未来工作 |
| [闭卷-引用悖论：无检索生成正确性更高但无法有效引用](../cards/closed-book-citation-paradox.md) | `closed-book-citation-paradox` | distinction | ClosedBook 模式在 ELI5 上正确性（18.6 claim recall）超过 Vanilla（12.0），但 PostCite 后引用 recall 仅 15.5%，因为：(1) 开卷模型被无关段落干扰降低正确性；(2)... |
| [Idea File 分发范式](../cards/idea-file-paradigm.md) | `idea-file-paradigm` | concept | LLM agent 时代的分发单元从代码/应用转向抽象想法文件，接收者的 agent 负责定制化构建实现 |
| [LoCoMo LLM 生成+人工编辑的对话数据管线](../cards/locomo-human-machine-pipeline.md) | `locomo-human-machine-pipeline` | mechanism | 用 GPT-3.5-turbo 双代理对话生成+人工标注者编辑 15% 轮次、替换 19% 图片以确保长程一致性，生成 50 段超长期多模态对话，是 LLM 合成+人工质控的混合数据构建范式 |
| [OWASP LLM Top 10 安全倡议](../cards/owasp-llm-top10-initiative.md) | `owasp-llm-top10-initiative` | source_claim | 2023年启动的社区驱动安全倡议，随LLM在客户交互与内部运营中的深入嵌入而持续识别AI特有安全漏洞 |
| [召回失败与安全对齐的区分](../cards/recall-vs-alignment-resistance.md) | `recall-vs-alignment-resistance` | distinction | 模型对注入攻击的表面抗性可能来自两种截然不同的原因：长上下文召回失败（偶然性防御）或安全对齐拒绝执行（有意性防御）；通过长上下文召回测试可区分两者——GPT-OSS-120B 仅 6.7% 召回率暴露其"免疫"实为处理能力限制 |
| [搜索回写机制](../cards/search-write-back.md) | `search-write-back` | mechanism | 是知识复利的第三微观机制： 当 wiki 不足以回答查询时触发外部搜索，搜索结果不蒸发而是由 wiki 专家合并回写至实体页面， 使 wiki 从单向（仅接受 INGEST）变为双向呼吸，是 Qing Claw 区别于所有其他 LLM... |
| [合成数据训练 LM 评审 + PPI 校准流水线](../cards/synthetic-judge-ppi-pipeline.md) | `synthetic-judge-ppi-pipeline` | mechanism | ARES 先自动生成合成数据微调轻量 LM 评审模型，再用少量（数百条）人工标注通过 PPI 校准预测误差，实现低成本高精度的自动评估 |
| [时序事件图作为对话锚定机制](../cards/temporal-event-graph-grounding.md) | `temporal-event-graph-grounding` | mechanism | 为每个对话代理构建含日期和因果连接的生活事件图（最多 25 事件 / 6-12 个月），作为长期对话的叙事锚定，迫使对话反映真实时间推移和因果关系 |
| [主题集中度与复利收益关系](../cards/topic-concentration-compounding.md) | `topic-concentration-compounding` | mechanism | 揭示高主题集中度领域（编程、研究）获得最大知识复利收益，低集中度领域（电商、个人助理） wiki 无法积累可复用结构，为 Liu et al. 的可用性鸿沟提供了全新解释维度 |
| [Tree-sitter AST 代码知识提取](../cards/tree-sitter-code-extraction.md) | `tree-sitter-code-extraction` | mechanism | 是一种通过 Tree-sitter 增量解析器对源代码进行 AST 级结构化知识提取的机制：从 19 种语言中提取类、函数、类型继承、 函数签名、文档注释和调用图，无需 LLM 参与即可生成知识图谱的代码层节点 |
