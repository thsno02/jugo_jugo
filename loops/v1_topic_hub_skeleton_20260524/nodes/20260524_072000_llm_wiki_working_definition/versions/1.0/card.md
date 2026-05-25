# LLM Wiki 的工作定义

**工作定义。** 在当前证据边界内，LLM Wiki 可以被定义为一种 source-preserving、LLM/agent-maintained 的知识组织模式：不可变 raw sources 作为来源真值，LLM 或 agent 将这些来源编译成持久、可检查、互联的 markdown/wiki 知识层，并在 schema 或 instruction 文件约束下，通过 ingest、query、lint 与 update/writeback 循环持续维护。这个定义是对 Karpathy `LLM Wiki` idea file 的归纳，不是产品定义、成熟度判断或经验效果证明。[^1][^2]

**来源支持的核心结构。** Gist 直接把 LLM Wiki 放在三层结构里：raw sources、wiki、schema。raw sources 是用户策展的来源集合，LLM 读取但不修改，承担 source of truth 的角色；wiki 是 LLM 生成和维护的 markdown 目录，包含摘要、实体页、概念页、比较、概览和综合；schema 则告诉 LLM 目录结构、约定以及 ingest、answering/query、maintenance 工作流。这里可观察到的事实是“三层结构被明确描述”；本节点的综合是把它概括为“来源保留 + 生成性知识层 + 操作规约”。[^1]

**与一次性检索的差异。** Gist 的中心对比不是“是否使用 retrieval”，而是“知识是否会积累成可复用 artifact”。普通文件上传或许能在查询时检索 raw chunks；LLM Wiki 的模式则要求 LLM 在新来源进入时读取、抽取、整合、修订既有页面，并把矛盾、交叉引用和新的综合沉淀在 wiki 中。这个节点只把该差异写成工作边界：LLM Wiki 至少需要一个持久、可检查、可被后续 agent 继续读取和修改的知识层；它不能仅等同于一次性回答、无来源的聊天记忆，或单纯向量库。[^1][^3]

**操作循环。** Gist 明确列出 `ingest`、`query`、`lint` 三类操作。`ingest` 把新来源纳入 raw collection，并让 LLM 更新摘要页、索引、日志以及相关实体/概念页；`query` 让 LLM 基于 wiki 检索和综合，且有价值的回答可以被写回 wiki；`lint` 用来检查矛盾、过时声明、孤立页面、缺失概念、缺失交叉引用和仍需检索的数据缺口。因此，本节点把 LLM Wiki 理解为一个维护循环，而不是只在建库时生成一批摘要页的静态过程。[^1]

**人的角色。** Gist 反复把 human role 限定在来源选择、探索方向、问题提出、重点强调和审阅上；summarizing、cross-referencing、filing、bookkeeping 这类维护劳动由 LLM 承担。这个说法支持一种分工式定义：人不是完全退出，也不是亲自写完整个 wiki；人主要控制输入、问题和判断，LLM 负责把知识层写出来并保持可用。[^1]

**导航支架。** `index.md` 与 `log.md` 在 gist 中不是知识本体本身，而是帮助人和 LLM 导航与追踪演化的支架：index 面向内容目录，log 面向时间顺序的 ingest、query 和 lint 记录。可选搜索工具、Obsidian、Marp、Dataview、MCP 或 CLI 工具在 gist 中都处于 modular tooling 位置，所以它们不能被写成 LLM Wiki 的必要条件。[^1]

**证据边界。** 已采用的 origin/canon 节点把 Karpathy gist 锚定为当前本地语料批次中的 bounded canon，同时明确 HN 只能作为早期公开讨论，X capture 只能作为 launch context/source inventory。这个工作定义继承该边界：它可以说明 LLM Wiki 被如何提出、如何抽象成 idea file，以及当前项目为什么可以先生成定义节点；它不能推出广泛采用、企业可用、实现生态完整、或相对 RAG 的测量优势。[^2][^4][^5]

**早期话语位置。** HN 原始讨论可以说明该 idea file 周围很快出现了“这是 RAG 吗”、raw source/backlink/staleness 如何处理、是否会导致质量退化等争论；X launch capture 可以说明 gist 是作为一个可交给 agent 的 idea file 被发布和链接。二者都只在这里作为话语和上下文边界使用，不作为技术证明、采用率证明或效果证明。[^4][^5]

**非目标。** 本节点没有建立 LLM Wiki 的完整思想史，没有给出严谨的 RAG/GraphRAG/PKM/knowledge graph/agent memory 比较，也没有评估 scale、citation accuracy、long-term drift、privacy/security、legal/compliance 或 enterprise governance。source-gap review 记录这些是后续候选节点或检索批次的任务，而不是当前定义节点的隐含结论。[^6]

## References

### [R1] Karpathy LLM Wiki idea file

target: data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt
target_version: raw_snapshot
pinned_version: data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt
citation_role: primary_definitional_source
why_cited: Provides the direct evidence for the node's working definition, architecture, operations, human/LLM role division, navigation files, and optional-tooling boundary.
evidence_summary: The local gist text frames LLM Wiki as an abstract pattern where immutable raw sources feed an LLM-maintained persistent markdown wiki governed by schema/instructions and maintained through ingest, query, lint, and writeback.

### [R2] Adopted bounded origin/canon node

target: kb/20260524_062000_llm_wiki_origin_and_canon.md
target_version: "1.0"
pinned_version: nodes/20260524_062000_llm_wiki_origin_and_canon/versions/1.0/card.md
citation_role: prior_kb_dependency
why_cited: Provides the adopted KB anchor for the local canon and preserves the boundary that this definition should not become adoption, enterprise, empirical, ecosystem, or full-lineage evidence.
evidence_summary: The adopted node records the Karpathy gist as bounded canon and treats HN and X as limited discourse or launch context rather than technical or adoption proof.

### [R3] HN original thread capture

target: data/raw/hacker_news/hacker-news-original-thread/text.txt
target_version: raw_snapshot
pinned_version: data/raw/hacker_news/hacker-news-original-thread/text.txt
citation_role: bounded_discourse_source
why_cited: Gives limited early-discourse context for public reactions and boundary concerns without supporting technical correctness or adoption claims.
evidence_summary: The capture includes the HN story and comments around RAG comparisons, source preservation, backlinks, staleness, quality, and maintenance concerns.

### [R4] Karpathy X launch capture

target: data/raw/webpage/karpathy-x-launch-post/text.txt
target_version: raw_snapshot
pinned_version: data/raw/webpage/karpathy-x-launch-post/text.txt
citation_role: bounded_launch_source
why_cited: Documents the local launch/source-inventory context for the gist as an idea file intended for agent customization.
evidence_summary: The capture contains the gist link and the launch framing that sharing an idea file lets another person's agent customize and build an LLM wiki for specific needs.

### [R5] LLM Wiki coverage framework

target: reports/coverage_framework.md
target_version: report_snapshot
pinned_version: reports/coverage_framework.md
citation_role: secondary_boundary_framework
why_cited: Supplies project-level boundary tests for future comparison and audit, while remaining secondary to the gist for the definition itself.
evidence_summary: The framework describes criteria such as source preservation, compiled persistent artifacts, provenance/auditability, maintenance, and limits of vector retrieval alone or chat memory alone.

### [R6] Source gap review

target: reports/source_gap_review.md
target_version: report_snapshot
pinned_version: reports/source_gap_review.md
citation_role: secondary_gap_report
why_cited: Keeps unresolved evidence gaps visible so the first version does not overclaim beyond the allowed source batch.
evidence_summary: The report says origin/definition coverage is strong but broader historical, empirical, enterprise, ecosystem, adoption, risk, governance, and comparison claims need separate evidence.

## Footnotes

[^1]:
    target: data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt
    target_version: raw_snapshot
    pinned_version: data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt
    citation_role: primary_definition_support
    why_cited: Supports the working definition's core claims about raw sources, LLM-generated wiki, schema/instructions, ingest/query/lint operations, index/log navigation, optional tooling, and human/LLM role division.
    evidence_summary: The gist describes LLM Wiki as an abstract pattern for LLM-built personal knowledge bases with immutable raw sources, a persistent maintained markdown wiki, schema-governed workflows, compounding writeback, and modular implementation choices.

[^2]:
    target: kb/20260524_062000_llm_wiki_origin_and_canon.md
    target_version: "1.0"
    pinned_version: nodes/20260524_062000_llm_wiki_origin_and_canon/versions/1.0/card.md
    citation_role: prior_kb_anchor
    why_cited: Anchors this working-definition node to the adopted bounded origin/canon node and carries forward the boundary that the gist is the current canonical source while HN and X remain bounded context.
    evidence_summary: The adopted node states that the Karpathy idea file is the bounded canon for the local corpus and that broader adoption, enterprise, ecosystem, empirical, and historical-lineage claims require separate evidence.

[^3]:
    target: reports/coverage_framework.md
    target_version: report_snapshot
    pinned_version: reports/coverage_framework.md
    citation_role: secondary_boundary_framing
    why_cited: Helps frame the boundary tests that distinguish a persistent source-backed artifact from vector retrieval alone, chat memory alone, or human-only PKM, without treating the framework as Karpathy's original wording.
    evidence_summary: The framework defines a strong LLM Wiki description around source preservation, knowledge compilation, persistent representation, provenance/auditability, and maintenance over time.

[^4]:
    target: data/raw/hacker_news/hacker-news-original-thread/text.txt
    target_version: raw_snapshot
    pinned_version: data/raw/hacker_news/hacker-news-original-thread/text.txt
    citation_role: bounded_discourse_context
    why_cited: Supports only the observation that early public discussion included RAG comparison, source/backlink/staleness framing, and quality concerns; it is not used as authoritative technical proof.
    evidence_summary: The captured HN thread includes the story title and comments debating whether the idea is RAG, how raw sources/backlinks relate to staleness and correctness, and possible risks such as quality degradation or maintenance scale.

[^5]:
    target: data/raw/webpage/karpathy-x-launch-post/text.txt
    target_version: raw_snapshot
    pinned_version: data/raw/webpage/karpathy-x-launch-post/text.txt
    citation_role: bounded_launch_context
    why_cited: Supports only launch-context and source-inventory claims about the gist being shared as an idea file that agents can customize, not adoption, social-metric, ecosystem, or empirical claims.
    evidence_summary: The local X capture links the gist and states that the idea file is intentionally abstract so another person's agent can customize and build a version for specific needs.

[^6]:
    target: reports/source_gap_review.md
    target_version: report_snapshot
    pinned_version: reports/source_gap_review.md
    citation_role: secondary_gap_framing
    why_cited: Identifies non-blocking gaps that should remain outside this first working-definition node, including enterprise, empirical, adoption, ecosystem, comparison, risk, and governance claims.
    evidence_summary: The source-gap review marks origin/definition coverage as strong while noting missing or under-covered evidence for historical lineage, independent empirical validation, scale boundaries, citation accuracy, governance, and adoption analysis.
