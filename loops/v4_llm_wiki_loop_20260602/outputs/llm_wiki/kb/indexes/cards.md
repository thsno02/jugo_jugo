---
total_cards: 259
generated: 2026-06-05T14:43:07
card_type_distribution:
  mechanism: 108
  source_claim: 48
  distinction: 44
  concept: 40
  operational_rule: 11
  example_pattern: 8
---

# KB Card Index (259 cards)

## 分类概览

| 分类 | 数量 |
|------|------|
| Wikibase 数据模型 | 9 |
| LLM Wiki 模式 | 25 |
| MemGPT 架构 | 10 |
| LoCoMo 基准 | 5 |
| GraphRAG | 9 |
| RAG 攻击与安全 | 10 |
| RAG 评估 | 6 |
| RAG 检索机制 | 16 |
| 引用与评估 | 13 |
| 上下文窗口与 Token 经济 | 16 |
| Agent 记忆系统 | 28 |
| Agent 记忆攻击 | 3 |
| Agent 治理与安全框架 | 14 |
| 图知识与时序 | 9 |
| 知识管理与 Zettelkasten | 11 |
| 伴侣系统 | 3 |
| 文档工程 | 3 |
| 成本与 ROI | 6 |
| 知识摄入与提取 | 7 |
| 知识治理操作 | 13 |
| 其他（系统设计与杂项） | 43 |

## Wikibase 数据模型 (9)

| slug | title | card_type |
|------|-------|-----------|
| [[wikibase-conceptual-model-separation]] | Wikibase 概念模型与技术表示的分离 | concept |
| [[wikibase-data-model-design-goals]] | Wikibase 数据模型的六项设计要求 | concept |
| [[wikibase-entity-description]] | EntityDescription 的多语言数据容器 | mechanism |
| [[wikibase-entity-value-hierarchy]] | Wikibase 实体与数据值的层次划分 | distinction |
| [[wikibase-flexible-typing]] | Property 的非严格类型设计 | concept |
| [[wikibase-qualifier-mechanism]] | Qualifier Snaks 的上下文限定机制 | mechanism |
| [[wikibase-snak-triple-epistemology]] | Snak 的三种认识论状态 | distinction |
| [[wikibase-statement-ranking]] | Statement 三级排名机制 | mechanism |
| [[wikibase-statement-structure]] | Statement 的复合结构 | mechanism |

## LLM Wiki 模式 (25)

| slug | title | card_type |
|------|-------|-----------|
| [[compilation-gap]] | 编译缺口——Wiki 编译中的灾难性事实丢失 | concept |
| [[compile-time-vs-query-time]] | 编译时与查询时知识装配 | distinction |
| [[data-catalog-as-enterprise-wiki]] | 数据目录作为企业级 Wiki 的结构等价物 | concept |
| [[kb-compile-implementation]] | kb-compile 实现模式 | example_pattern |
| [[llm-wiki-as-teaching-tool]] | LLM Wiki 的教学工具本质 | source_claim |
| [[llm-wiki-ecosystem-velocity]] | LLM Wiki 生态形成速度 | source_claim |
| [[llm-wiki-mainstream-prerequisites]] | LLM Wiki 主流化四条件 | source_claim |
| [[llm-wiki-pattern]] | LLM Wiki 模式 | concept |
| [[llm-wiki-rag-depth-distinction]] | LLM Wiki 与 RAG 的核心差异在于推理深度 | distinction |
| [[llm-wiki-scale-boundary]] | LLM Wiki 的适用规模边界 | distinction |
| [[llm-wiki-setup-friction]] | LLM Wiki 搭建摩擦 | source_claim |
| [[llm-wiki-v2-agentmemory]] | LLM Wiki v2 社区扩展与 agentmemory 模式 | source_claim |
| [[my-llm-wiki-implementation]] | my-llm-wiki PyPI 实现 | example_pattern |
| [[obsidian-karpathy-wiki-plugin]] | Obsidian 社区插件 Karpathy LLM Wiki | example_pattern |
| [[production-scale-wiki-reference]] | 生产级 Wiki 参考实现 | example_pattern |
| [[rag-wiki-complementarity]] | RAG 与 Wiki 的互补关系 | distinction |
| [[rag-wiki-synthesis-distinction]] | RAG 与 Wiki 知识综合的区分 | distinction |
| [[typed-wikilinks]] | 类型化 Wiki 链接 | mechanism |
| [[wiki-as-git-repo]] | Wiki 即 Git 仓库 | source_claim |
| [[wiki-compounding-artifact]] | Wiki 作为复利型知识制品 | mechanism |
| [[wiki-deduplication-fragility]] | Wiki 去重的脆弱性 | source_claim |
| [[wiki-enterprise-failure-modes]] | Wiki 企业级三大失效模式 | distinction |
| [[wiki-rag-hybrid-pattern]] | Wiki-RAG 混合架构模式 | mechanism |
| [[wiki-storage-protocol]] | WikiStorage 可插拔存储协议 | mechanism |
| [[wiki-write-back-mechanism]] | Wiki 回写机制 | mechanism |

## MemGPT 架构 (10)

| slug | title | card_type |
|------|-------|-----------|
| [[memgpt-conversation-opener-results]] | MemGPT 对话开场白实验结果 | source_claim |
| [[memgpt-deep-memory-retrieval-results]] | MemGPT 深度记忆检索实验结果 | source_claim |
| [[memgpt-document-qa-scaling]] | MemGPT 文档问答的上下文无关扩展性 | source_claim |
| [[memgpt-event-driven-control-flow]] | MemGPT 事件驱动控制流 | mechanism |
| [[memgpt-function-chaining]] | MemGPT 函数链与心跳机制 | mechanism |
| [[memgpt-main-context-structure]] | MemGPT 主上下文三段式结构 | mechanism |
| [[memgpt-memory-hierarchy]] | MemGPT 两级内存层次结构 | mechanism |
| [[memgpt-nested-kv-retrieval]] | MemGPT 嵌套键值检索与多跳能力 | source_claim |
| [[memgpt-queue-eviction-policy]] | MemGPT 队列驱逐与内存压力机制 | mechanism |
| [[memgpt-self-directed-memory]] | MemGPT 自主内存编辑与检索 | mechanism |

## LoCoMo 基准 (5)

| slug | title | card_type |
|------|-------|-----------|
| [[locomo-benchmark-design]] | LOCOMO 长期对话记忆基准测试设计 | example_pattern |
| [[locomo-benchmark]] | LoCoMo 超长期对话记忆评测基准 | source_claim |
| [[locomo-five-reasoning-types]] | LoCoMo 对话记忆 QA 的五类推理维度 | distinction |
| [[locomo-human-machine-pipeline]] | LoCoMo LLM 生成+人工编辑的对话数据管线 | mechanism |
| [[locomo-reflect-respond-architecture]] | LoCoMo 反思-回应双层记忆代理架构 | mechanism |

## GraphRAG (9)

| slug | title | card_type |
|------|-------|-----------|
| [[graphrag-community-hierarchy]] | GraphRAG 层级社区检测与摘要机制 | mechanism |
| [[graphrag-community-level-tradeoff]] | GraphRAG 社区层级的 token 效率与回答质量权衡 | distinction |
| [[graphrag-comprehensiveness-diversity-result]] | GraphRAG 全面性与多样性大幅优于向量 RAG 的实证结果 | source_claim |
| [[graphrag-defense-gap]] | GraphRAG 知识投毒防御空白 | source_claim |
| [[graphrag-global-sensemaking]] | GraphRAG 全局语义理解方法 | mechanism |
| [[graphrag-knowledge-poisoning-attack]] | GraphRAG 知识投毒攻击 | concept |
| [[graphrag-map-reduce-query]] | GraphRAG 查询时 Map-Reduce 应答流程 | mechanism |
| [[graphrag-self-reflection-gleaning]] | GraphRAG 自我反思拾遗实体提取技术 | mechanism |
| [[graphrag-small-context-window-advantage]] | GraphRAG 中小上下文窗口反而更优的发现 | source_claim |

## RAG 攻击与安全 (10)

| slug | title | card_type |
|------|-------|-----------|
| [[poisonedrag-text-decomposition]] | PoisonedRAG 的 S+I 文本分解策略 | mechanism |
| [[rag-advanced-scheme-vulnerability]] | 高级 RAG 方案对知识腐蚀攻击的脆弱性 | source_claim |
| [[rag-knowledge-corruption-attack]] | RAG 知识腐蚀攻击 | concept |
| [[rag-knowledge-database-attack-surface]] | RAG 知识库作为新攻击面 | concept |
| [[rag-parametric-bias-failure]] | RAG 投毒中的参数偏差失效模式 | distinction |
| [[rag-poisoning-defense-insufficiency]] | 现有防御对 RAG 知识腐蚀攻击的不充分性 | source_claim |
| [[rag-retrieval-generation-dual-condition]] | RAG 攻击的检索与生成双条件 | mechanism |
| [[targeted-kpa]] | 定向知识投毒攻击（TKPA） | mechanism |
| [[text-perturbation-amplification]] | 文本微扰的图谱放大效应 | mechanism |
| [[universal-kpa]] | 通用知识投毒攻击（UKPA） | mechanism |

## RAG 评估 (6)

| slug | title | card_type |
|------|-------|-----------|
| [[ares-rag-evaluation-framework]] | ARES 自动化 RAG 评估框架 | concept |
| [[rag-component-evaluation-tri-dimension]] | RAG 组件评估三维度：上下文相关性、回答忠实性、回答相关性 | distinction |
| [[rag-evaluation-meta-evaluation]] | RAG 评估框架的元评估方法论 | mechanism |
| [[rag-evaluation-tri-dimension]] | RAG 评估三维度分解 | distinction |
| [[ragas-reference-free-rag-evaluation]] | RAGAS 无参考评估框架 | mechanism |
| [[ragchecker-three-tier-metrics]] | RAGChecker 三层诊断指标体系 | mechanism |

## RAG 检索机制 (16)

| slug | title | card_type |
|------|-------|-----------|
| [[chunk-size-tradeoff]] | 分块大小权衡 | mechanism |
| [[dual-retrieval-entity-semantic]] | 双路检索策略（实体锚定 + 语义三元组） | mechanism |
| [[entity-resolution-hybrid-search]] | 混合搜索实体消解流程 | mechanism |
| [[full-context-anti-rag]] | 全上下文反 RAG 架构选择 | distinction |
| [[hybrid-triple-search-complementarity]] | 三种互补搜索方法的混合检索 | mechanism |
| [[kv-cache-vs-rag-tradeoff]] | KV cache 推理与 RAG 的性能权衡 | source_claim |
| [[rag-generator-self-knowledge]] | RAG 生成器的自有知识指标 | concept |
| [[rerank-citation-boost]] | Rerank 策略：多次采样并按引用 recall 选优以提升引用质量 | mechanism |
| [[retrieval-as-citation-bottleneck]] | 检索质量是引用生成的根本瓶颈 | source_claim |
| [[retrieval-improvement-faithfulness-noise-tradeoff]] | 检索改善引发的忠实度与噪声敏感度权衡 | mechanism |
| [[retrieval-snr-tradeoff]] | 检索量与信噪比的权衡效应 | mechanism |
| [[retrieval-vs-maintenance]] | 检索与维护的区别 | distinction |
| [[search-rerank-construct-pipeline]] | 搜索-重排-构造三步检索管线 | mechanism |
| [[search-write-back]] | 搜索回写机制 | mechanism |
| [[sensemaking-vs-retrieval-query]] | 意义建构查询与检索查询的区分 | distinction |
| [[static-rag-dynamic-memory-gap]] | 静态 RAG 与动态 agent 记忆的鸿沟 | distinction |

## 引用与评估 (13)

| slug | title | card_type |
|------|-------|-----------|
| [[adaptive-benchmarking-persona-generation]] | 基于 LLM 人设生成的自适应基准测试 | mechanism |
| [[alce-citation-benchmark]] | ALCE：首个自动化 LLM 引用评估基准 | concept |
| [[citation-partial-support-limitation]] | 引用评估中"部分支持"检测的缺失问题 | distinction |
| [[citation-quality-tri-dimension]] | 引用评估三维度框架：流畅度-正确性-引用质量 | mechanism |
| [[citation-support-gap]] | LLM 引用支持缺口：最佳模型仍有约 50% 陈述缺乏完整引用 | source_claim |
| [[claim-level-entailment-evaluation]] | 声明级蕴含检验评估方法 | mechanism |
| [[closed-book-citation-paradox]] | 闭卷-引用悖论：无检索生成正确性更高但无法有效引用 | distinction |
| [[dmr-benchmark-inadequacy]] | DMR 基准测试的局限性 | source_claim |
| [[instruction-tuning-citation-effect]] | 指令微调对 LLM 引用能力的显著提升效应 | source_claim |
| [[lexical-vs-semantic-eval-gap]] | 词汇匹配指标 vs 语义评估的鸿沟 | distinction |
| [[lossy-compression-citation-tradeoff]] | 有损压缩的引用权衡：摘要/片段提升正确性但损害引用质量 | mechanism |
| [[nli-based-citation-verification]] | 基于 NLI 模型的引用验证机制 | mechanism |
| [[synthetic-judge-ppi-pipeline]] | 合成数据训练 LM 评审 + PPI 校准流水线 | mechanism |

## 上下文窗口与 Token 经济 (16)

| slug | title | card_type |
|------|-------|-----------|
| [[attention-dilution-at-scale]] | 注意力稀释导致全上下文推理在规模化时退化 | mechanism |
| [[context-extension-insufficiency]] | 上下文窗口扩展的不充分性 | source_claim |
| [[context-scaling-diminishing-returns]] | 上下文窗口扩展的递减收益问题 | distinction |
| [[context-utilization-as-performance-key]] | 上下文利用率是 RAG 性能的关键生成器指标 | source_claim |
| [[context-utilization-noise-faithfulness-trilemma]] | 上下文利用率-噪声敏感度-忠实度三难困境 | mechanism |
| [[context-window-degradation]] | 上下文窗口退化现象 | source_claim |
| [[executable-guidance-vs-context-pile]] | 可执行指引 vs 上下文堆积 | distinction |
| [[full-context-accuracy-ceiling]] | 全上下文方法的准确率天花板效应 | source_claim |
| [[long-context-adversarial-vulnerability]] | 长上下文 LLM 对对抗性问题的脆弱性 | source_claim |
| [[long-context-comprehension-illusion]] | 长上下文模型的理解假象 | source_claim |
| [[longmemeval-context-compression]] | LongMemEval 上下文压缩与准确率提升 | source_claim |
| [[open-source-vs-proprietary-context-discrimination]] | 开源模型与闭源模型在上下文辨别力上的差距 | source_claim |
| [[supply-demand-token-dividend]] | Token 供需双重红利 | concept |
| [[tldr-context-optimization]] | TL;DR 摘要的上下文窗口优化作用 | mechanism |
| [[token-capital-goods]] | Token 资本品重分类 | concept |
| [[virtual-context-management]] | 虚拟上下文管理 | mechanism |

## Agent 记忆系统 (28)

| slug | title | card_type |
|------|-------|-----------|
| [[agent-memory-lifecycle-phases]] | Agent 记忆四阶段生命周期 | concept |
| [[agent-memory-persistent-attack-surface]] | Agent 记忆作为持久性攻击面 | concept |
| [[ai-memory-operating-system]] | AI 记忆操作系统框架 | concept |
| [[cross-session-continuity]] | 跨会话连续性机制 | mechanism |
| [[episodic-semantic-memory-duality]] | 情景记忆与语义记忆的双存储设计 | concept |
| [[etamp-environment-memory-poisoning]] | 环境注入式轨迹记忆投毒攻击 | mechanism |
| [[extract-then-read-memory-strategy]] | 先提取后阅读的记忆读取策略 | mechanism |
| [[graph-memory-temporal-advantage]] | 图记忆在时序推理中的优势 | distinction |
| [[lightmem-three-stage-memory]] | LightMem 三阶段记忆架构 | mechanism |
| [[long-term-memory-accuracy-gap]] | 长期记忆准确率差距（30-60% 下降） | source_claim |
| [[longmemeval-five-memory-abilities]] | LongMemEval 五项核心长期记忆能力 | distinction |
| [[memory-augmentation-overhead]] | LLM 记忆系统的开销问题 | source_claim |
| [[memory-compression-token-ratio]] | 记忆压缩的 token 效率差异 | source_claim |
| [[memory-crud-operation-taxonomy]] | 记忆 CRUD 操作分类法 | mechanism |
| [[memory-extraction-update-pipeline]] | 记忆提取-更新双阶段管线 | mechanism |
| [[memory-gravity]] | 记忆引力 | mechanism |
| [[memory-lifecycle-metadata]] | 记忆生命周期元数据 | mechanism |
| [[memory-overwrite-vs-omission-failure]] | 记忆覆写与遗漏两种失败模式 | distinction |
| [[memory-value-granularity-tradeoff]] | 记忆存储粒度权衡（会话/轮次/事实） | mechanism |
| [[memory-vs-rag-salience]] | 记忆系统 vs RAG 的显著性优势 | source_claim |
| [[namespace-key-memory-model]] | 命名空间-键值记忆数据模型 | mechanism |
| [[non-lossy-episodic-store]] | 无损 Episode 数据存储与双向溯源 | operational_rule |
| [[observation-based-memory-representation]] | 观察断言式记忆表示优于原始对话检索 | mechanism |
| [[raw-vs-consolidated-memory-vulnerability]] | 原始轨迹记忆与整合记忆的脆弱性差异 | distinction |
| [[recall-vs-alignment-resistance]] | 召回失败与安全对齐的区分 | distinction |
| [[sleep-consolidation-architecture]] | 睡眠整合架构 | mechanism |
| [[sleep-time-memory-consolidation]] | 睡眠期离线记忆巩固机制 | mechanism |
| [[tool-mediated-memory-access]] | 工具中介的记忆访问模式 | mechanism |

## Agent 记忆攻击 (3)

| slug | title | card_type |
|------|-------|-----------|
| [[conditional-trigger-stealth-design]] | 条件触发器的隐蔽性设计 | mechanism |
| [[entrenchment-under-user-coupled-drift]] | 用户耦合漂移下的固化 | concept |
| [[frustration-exploitation-attack]] | 挫败利用攻击 | mechanism |

## Agent 治理与安全框架 (14)

| slug | title | card_type |
|------|-------|-----------|
| [[agent-governance-modular-packages]] | Agent 治理模块化分包架构 | concept |
| [[agent-governance-standards-mapping]] | Agent 治理标准合规映射 | mechanism |
| [[ai-rmf-voluntary-trustworthiness]] | AI RMF 的自愿性与可信赖性导向 | concept |
| [[architectural-separability-as-safety]] | 架构可分离性作为安全承诺 | distinction |
| [[audit-provenance-tracing]] | 审计与溯源追踪 | mechanism |
| [[audit-stress-test]] | AUDIT 结构性压力测试 | mechanism |
| [[chaos-monkey-agent-stress-testing]] | Chaos Monkey 式 Agent 压力测试 | mechanism |
| [[deterministic-policy-enforcement]] | 确定性策略执行 | mechanism |
| [[framework-agnostic-governance-layer]] | 框架无关的治理层 | concept |
| [[governance-over-retrieval]] | 治理优先于检索架构 | source_claim |
| [[model-capability-security-disconnect]] | 模型能力与安全性的脱钩 | source_claim |
| [[nist-ai-600-1-gai-profile]] | NIST AI 600-1 生成式 AI 风险管理框架概况 | source_claim |
| [[owasp-agentic-top10-framework]] | OWASP Agentic Top 10 框架 | concept |
| [[owasp-llm-top10-initiative]] | OWASP LLM Top 10 安全倡议 | source_claim |

## 图知识与时序 (9)

| slug | title | card_type |
|------|-------|-----------|
| [[bi-temporal-fact-model]] | 双时间线事实建模 | mechanism |
| [[cross-tool-entity-resolution]] | 跨工具实体解析 | mechanism |
| [[dynamic-community-detection]] | 标签传播动态社区检测 | mechanism |
| [[edge-invalidation-mechanism]] | 边失效与动态知识更新机制 | mechanism |
| [[graph-modularity-for-summarization]] | 图模块性作为层级摘要的结构基础 | concept |
| [[temporal-event-graph-grounding]] | 时序事件图作为对话锚定机制 | mechanism |
| [[temporal-knowledge-graph-three-tier]] | 时序知识图谱的三层子图架构 | mechanism |
| [[temporal-reasoning-difficulty]] | 时序推理是 LLM 对话记忆中最困难的能力维度 | source_claim |
| [[time-aware-query-expansion]] | 时间感知的查询扩展策略 | mechanism |

## 知识管理与 Zettelkasten (11)

| slug | title | card_type |
|------|-------|-----------|
| [[archive-lifecycle]] | 主题归档生命周期 | mechanism |
| [[idea-file-paradigm]] | Idea File 分发范式 | concept |
| [[index-based-navigation]] | 索引文件导航机制 | mechanism |
| [[knowledge-as-work-byproduct]] | 知识作为工作副产品 | concept |
| [[knowledge-compounding]] | 知识复利效应 | concept |
| [[log-file]] | 活动日志文件 | mechanism |
| [[map-of-content-pattern]] | Map of Content 引导阅读路径 | mechanism |
| [[obsidian-tooling]] | Obsidian 工具生态 | operational_rule |
| [[topic-concentration-compounding]] | 主题集中度与复利收益关系 | mechanism |
| [[topic-isolation]] | 主题隔离原则 | concept |
| [[writing-as-thinking]] | 书写即思考 | concept |

## 伴侣系统 (3)

| slug | title | card_type |
|------|-------|-----------|
| [[companion-conformance-invariants]] | 伴侣系统合规不变量 | operational_rule |
| [[companion-knowledge-system]] | 伴侣知识系统 | concept |
| [[companion-object-model]] | 伴侣系统对象模型 | concept |

## 文档工程 (3)

| slug | title | card_type |
|------|-------|-----------|
| [[docs-as-code]] | Docs as Code 理念 | concept |
| [[documentation-merge-gate]] | 文档合并门禁机制 | mechanism |
| [[documentation-shared-ownership]] | 文档共同所有权文化 | concept |

## 成本与 ROI (6)

| slug | title | card_type |
|------|-------|-----------|
| [[compounding-cost-honesty]] | 复利方案在原始 token 成本上从不胜出 | source_claim |
| [[cost-independence-assumption]] | Agentic ROI 成本独立性假设批判 | distinction |
| [[dynamic-agentic-roi]] | 动态 Agentic ROI 模型 | mechanism |
| [[invest-harvest-cycle]] | 投资-收获振荡成本曲线 | example_pattern |
| [[maintenance-cost-zero]] | 维护成本归零论点 | source_claim |
| [[output-compounding-loop]] | 产出复利循环 | mechanism |

## 知识摄入与提取 (7)

| slug | title | card_type |
|------|-------|-----------|
| [[contextualize-depth-fitted-compression]] | CONTEXTUALIZE 深度适配压缩 | mechanism |
| [[extraction-granularity-control]] | 提取粒度控制 | mechanism |
| [[fact-augmented-key-expansion]] | 事实增强的索引键扩展 | mechanism |
| [[ingest-operation]] | 摄入操作 | operational_rule |
| [[representation-first-ingest]] | 表示先行摄入模型 | mechanism |
| [[source-granularity-effect]] | 源文件粒度效应 | mechanism |
| [[tree-sitter-code-extraction]] | Tree-sitter AST 代码知识提取 | mechanism |

## 知识治理操作 (13)

| slug | title | card_type |
|------|-------|-----------|
| [[confirm-first-skill-capture]] | 确认优先的技能捕获规则 | operational_rule |
| [[contradiction-as-asset]] | 矛盾作为知识资产 | operational_rule |
| [[contradiction-state-machine]] | 矛盾状态机 | mechanism |
| [[gap-mapping-promotion]] | 缺口映射与晋升机制 | mechanism |
| [[inventory-evidence-separation]] | 清单与证据的刻意分离 | distinction |
| [[lint-operation]] | 巡检操作 | operational_rule |
| [[minority-pressure-promotion]] | 少数派压力提升机制 | mechanism |
| [[originals-verbatim-capture]] | 原创思考的逐字保留 | operational_rule |
| [[query-and-answer-filing]] | 查询操作与答案归档 | operational_rule |
| [[schema-as-configuration]] | Schema 文件的配置角色 | mechanism |
| [[schema-template-verticals]] | Schema 模板的领域垂直化 | example_pattern |
| [[triage-shallow-filter]] | TRIAGE 浅层过滤器 | operational_rule |
| [[vitality-score-formula]] | 活力评分公式 | mechanism |

## 其他（系统设计与杂项） (43)

| slug | title | card_type |
|------|-------|-----------|
| [[alias-cross-language-dedup]] | 别名系统与跨语言去重 | mechanism |
| [[ask-first-retrieve-loop]] | 先查后做的 Agent 工作循环 | mechanism |
| [[capitalized-latency]] | 资本化延迟与瞬时延迟 | distinction |
| [[circularity-as-thesis]] | 循环性作为论题 | distinction |
| [[cognitive-deskilling-risk]] | 认知去技能化风险 | concept |
| [[complexity-collapse-threshold]] | 复杂度崩溃阈值 | mechanism |
| [[continuous-drift-detection]] | 持续偏移检测 | mechanism |
| [[dual-audience-artifact]] | 双受众制品 | mechanism |
| [[event-summarization-error-taxonomy]] | LLM 事件摘要的五类错误分类 | distinction |
| [[full-stack-locality]] | 全栈本地性 | distinction |
| [[hn-architectural-pattern-reception]] | HN 社区将 LLM Wiki 视为架构模式 | source_claim |
| [[human-llm-role-division]] | 人机角色分工 | distinction |
| [[intentional-abstraction]] | 刻意抽象与模块化 | source_claim |
| [[licklider-symbiosis-parallel]] | Licklider 人机共生类比 | source_claim |
| [[literature-velocity-argument]] | 文献速度论点 | source_claim |
| [[llm-as-maintenance-engine]] | LLM 作为维护引擎的角色重构 | concept |
| [[mcp-tool-skill-layering]] | MCP 工具与技能的双层设计 | mechanism |
| [[memex-connection]] | Memex 精神联系 | source_claim |
| [[mirror-vs-compensate-principle]] | 镜像-补偿设计原则 | mechanism |
| [[model-quality-error-propagation]] | 模型能力不足导致的错误传播风险 | operational_rule |
| [[multi-platform-skill-portability]] | 多平台技能可移植性 | mechanism |
| [[optimistic-concurrency-etag]] | 乐观并发控制（Etag CAS） | mechanism |
| [[parallel-multi-agent-research]] | 并行多智能体研究机制 | mechanism |
| [[pattern-naming-resonance]] | 模式命名的共振效应 | source_claim |
| [[relevant-vs-irrelevant-noise-sensitivity]] | 相关噪声与无关噪声敏感度的区分 | distinction |
| [[review-involvement-spectrum]] | 人类参与程度谱系 | distinction |
| [[runtime-agent-boundary]] | 运行时与代理的职责边界 | distinction |
| [[scenario-based-tool-selection]] | 场景驱动的知识工具选择 | distinction |
| [[server-mechanics-boundary]] | 服务器力学边界原则 | distinction |
| [[single-curator-bottleneck]] | 单一策展人瓶颈 | distinction |
| [[source-faithfulness-risk]] | 源忠实性风险与不可变锚点 | distinction |
| [[spec-driven-conformance-testing]] | 规范驱动的合规测试 | mechanism |
| [[structured-queryability-gap]] | 结构化可查询性缺口 | distinction |
| [[targeted-diagnosis-vs-generic-pinning]] | 定向诊断优于泛化固定 | distinction |
| [[thesis-driven-research]] | 论点驱动研究模式 | mechanism |
| [[three-correction-channels]] | 三纠正通道 | concept |
| [[three-layer-architecture]] | 三层架构 | concept |
| [[understanding-bottleneck]] | 理解瓶颈 | concept |
| [[use-case-domains]] | 应用领域 | example_pattern |
| [[weight-internalization-aspiration]] | 权重内化知识的愿景 | source_claim |
| [[wicer-iterative-refinement]] | WiCER 迭代精炼算法 | mechanism |
| [[workflow-taxonomy]] | 工作流五类分类法 | concept |
| [[zero-runtime-dependency]] | 零运行时依赖 | concept |
