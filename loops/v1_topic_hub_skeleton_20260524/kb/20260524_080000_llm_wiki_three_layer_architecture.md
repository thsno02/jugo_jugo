# LLM Wiki 的三层架构

**来源支持的架构事实。** 在当前证据边界内，LLM Wiki 的核心架构可以先写成三层：`raw sources`、`the wiki`、`the schema`。这是 Karpathy idea file 在 `Architecture` 小节中直接给出的分层，而不是本节点新增的分类法。这个节点的对象范围只限于这三层及其必要支撑设施，不把 LLM Wiki 扩写成实现生态、企业方案或经验效果结论。[^1][^2]

**第一层：raw source layer。** Raw sources 是用户策展的来源材料集合，例如文章、论文、图片和数据文件。来源支持的观察是：LLM 读取这些材料，但不修改它们；它们承担 source of truth 的角色。因此，本节点把 raw source layer 理解为“保留可回查原始依据”的层，而不是一个由 LLM 生成知识的层。这个说法继承了已采用 working definition 中的 source-preserving 边界。[^1][^3]

**第二层：compiled wiki layer。** The wiki 是由 LLM 生成和维护的 markdown 文件目录，可以包含摘要、实体页、概念页、比较、概览和综合。来源支持的观察是：LLM 负责创建页面、在新来源进入时更新页面、维护交叉引用并保持一致性；用户主要阅读这个层。由此可作出的 worker synthesis 是：这个层是 raw sources 与后续查询之间的持久、可检查、可继续编辑的 compiled knowledge artifact。[^1][^3]

**第三层：schema/instruction layer。** The schema 是约束 LLM 如何维护 wiki 的 instruction 文档或 schema 文档，例如 gist 中举的 `CLAUDE.md` 或 `AGENTS.md`。来源支持的观察是：它告诉 LLM wiki 如何组织、采用什么约定，以及 ingest、answering/query、maintenance 时遵循哪些流程。本节点把它称为 schema/instruction layer，是为了强调它的作用是操作规约和结构约束，而不是又一份内容 wiki。[^1]

**层间关系。** 这三层可以被综合为：raw source layer 保存依据，compiled wiki layer 保存可复用知识表示，schema/instruction layer 约束 agent 如何从前者维护后者。这是对 gist 三个命名层的归纳，不应被读作通用架构标准。它与已采用 origin/canon 节点保持一致：Karpathy gist 是当前本地语料批次的 bounded canon，HN、X 或其他话语材料不能在这里升级为采用率、成熟度或效果证据。[^2][^3]

**支撑基础设施，而非第四层。** Gist 还描述了 `index.md` 和 `log.md`：前者是内容导向目录，帮助人和 LLM 找到页面；后者是时间顺序记录，追踪 ingest、query 和 lint pass。它们在本节点中属于导航和历史支架，不构成第四个核心层。类似地，搜索工具、CLI、MCP、viewer、review queue、lint、citation/provenance 标记、representation storage 等都只能写成实现支持或实现变体；它们可以帮助三层架构运转，但不能被说成抽象 LLM Wiki 必须具备的固定工具。[^1][^4][^5]

**实现味道。** `llm-wiki-compiler` README 把这个模式落成一个从 `sources/` 到 hash check、concept extraction、wiki page generation、wikilink resolution、`index.md` 的编译流程，并给出 `wiki/concepts`、`wiki/queries`、`.llmwiki/schema.json`、candidate review、source markers、line-range citation、lint、viewer 和 MCP server 等实现细节。ClawHub listing 则把一个 runtime 描述为 raw/wiki/schema operating model，并列出 generated `wiki/index.md`、`wiki/log.md`、deterministic lint、CLI、MCP、representation storage 等能力。它们支持“这些基础设施在实现中常见或可见”，但不支持“这些工具是抽象架构的必要条件”。[^4][^5]

**边界和非目标。** 本节点不展开 ingest、compile、query、lint 的详细工作流；这些操作只作为连接三层的背景存在。它也不比较 RAG、GraphRAG、PKM、knowledge graph 或 agent memory，不评价 scale、citation accuracy、privacy/security、governance 或 enterprise readiness。source gap review 和 coverage framework 可以作为边界提醒：当前证据足以写一个 bounded architecture first version，但中立架构 taxonomy、独立效果评估、长期维护可靠性和广泛生态/采用分析仍是后续工作。[^6][^7]

## References

### [R1] Karpathy LLM Wiki idea file

target: data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt
target_version: raw_snapshot
pinned_version: data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt
citation_role: primary_architecture_source
why_cited: Provides the direct source for the three-layer architecture and for index/log/tooling boundary claims.
evidence_summary: The source names raw sources, the wiki, and the schema, then separately describes operations, index.md, log.md, optional tools, and modular implementation choices.

### [R2] Adopted origin/canon node

target: kb/20260524_062000_llm_wiki_origin_and_canon.md
target_version: "1.0"
pinned_version: nodes/20260524_062000_llm_wiki_origin_and_canon/versions/1.0/card.md
citation_role: prior_kb_dependency
why_cited: Preserves the adopted canon boundary that keeps this node from becoming adoption, enterprise, empirical, ecosystem, or historical-lineage evidence.
evidence_summary: The adopted node treats the Karpathy gist as bounded canon and explicitly limits broader public context to discourse or launch inventory.

### [R3] Adopted working definition node

target: kb/20260524_072000_llm_wiki_working_definition.md
target_version: "1.0"
pinned_version: nodes/20260524_072000_llm_wiki_working_definition/versions/1.0/card.md
citation_role: prior_kb_dependency
why_cited: Supplies the adopted definition that this architecture node refines into a bounded three-layer description.
evidence_summary: The adopted node states that LLM Wiki preserves raw sources, compiles them into a persistent interlinked markdown/wiki layer, and governs maintenance through schema or instruction files.

### [R4] llm-wiki-compiler README

target: data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md
target_version: raw_snapshot
pinned_version: data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md
citation_role: implementation_variant_source
why_cited: Provides directly mined implementation-flavored examples of how the raw/wiki/schema pattern can be instantiated with compiler, review, citation, lint, viewer, and MCP features.
evidence_summary: The README describes a source-to-wiki compiler, output directories, schema.json, candidate review, paragraph and line-range source markers, lint checks, local web viewer, query/save, watch, and MCP server.

### [R5] ClawHub LLM Wiki Karpathy listing

target: data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt
target_version: raw_snapshot
pinned_version: data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt
citation_role: implementation_variant_source
why_cited: Provides a second implementation-flavored source for raw/wiki/schema operating language and supporting runtime infrastructure.
evidence_summary: The listing describes a runtime with raw/wiki/schema operating model, generated index/log, deterministic lint, CLI and MCP wrappers, OpenClaw compatibility, and representation storage for multimodal materials.

### [R6] Source gap review

target: reports/source_gap_review.md
target_version: report_snapshot
pinned_version: reports/source_gap_review.md
citation_role: secondary_gap_report
why_cited: Records why broader taxonomy, empirical, ecosystem, scale, governance, and comparison claims remain out of scope for this first version.
evidence_summary: The report marks workflow architecture coverage as strong but records missing neutral architecture taxonomy and several evidence gaps outside this node.

### [R7] LLM Wiki coverage framework

target: reports/coverage_framework.md
target_version: report_snapshot
pinned_version: reports/coverage_framework.md
citation_role: secondary_boundary_framework
why_cited: Provides project-level vocabulary for evidence types and boundary tests, without replacing primary source evidence from the gist.
evidence_summary: The framework distinguishes observed facts, interpretations, hypotheses, and evaluation results, and lists source preservation, persistent representation, provenance, and maintenance as coverage dimensions.

## Footnotes

[^1]:
    target: data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt
    target_version: raw_snapshot
    pinned_version: data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt
    citation_role: primary_architecture_support
    why_cited: Supports the direct three-layer architecture claim, including raw sources as immutable source of truth, the LLM-generated markdown wiki layer, schema/instructions, index.md/log.md support, and optional/modular tooling boundaries.
    evidence_summary: The gist names raw sources, the wiki, and the schema as the architecture layers; it also describes index.md, log.md, ingest/query/lint operations, and notes that exact structure and tooling depend on domain and preference.

[^2]:
    target: kb/20260524_062000_llm_wiki_origin_and_canon.md
    target_version: "1.0"
    pinned_version: nodes/20260524_062000_llm_wiki_origin_and_canon/versions/1.0/card.md
    citation_role: prior_kb_anchor
    why_cited: Anchors this architecture node to the adopted bounded canon and preserves the prohibition against adoption, ecosystem, enterprise, empirical, and broad historical claims.
    evidence_summary: The adopted node records the Karpathy idea file as the local bounded canon and treats broader public-discourse and launch-context materials as limited context rather than technical proof.

[^3]:
    target: kb/20260524_072000_llm_wiki_working_definition.md
    target_version: "1.0"
    pinned_version: nodes/20260524_072000_llm_wiki_working_definition/versions/1.0/card.md
    citation_role: prior_kb_anchor
    why_cited: Provides the adopted working definition that this architecture node builds on: source preservation, LLM-maintained compiled wiki, schema/instruction governance, and maintenance loops.
    evidence_summary: The adopted node defines LLM Wiki as a source-preserving, LLM/agent-maintained knowledge pattern with immutable raw sources, a persistent markdown/wiki artifact, and schema-governed ingest/query/lint/update behavior.

[^4]:
    target: data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md
    target_version: raw_snapshot
    pinned_version: data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md
    citation_role: implementation_detail_support
    why_cited: Supports implementation-flavored details such as sources, hash checks, concept extraction, wiki generation, wikilinks, index, schema, candidates, provenance markers, lint, viewer, query/save, watch, and MCP.
    evidence_summary: The README maps Karpathy's pattern into a compiler with source ingest, incremental compile, wiki output directories, schema file, review queue, claim-level provenance, local viewer, lint checks, and MCP tooling.

[^5]:
    target: data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt
    target_version: raw_snapshot
    pinned_version: data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt
    citation_role: implementation_detail_support
    why_cited: Supports only directly present runtime details around a raw/wiki/schema operating model, generated index/log, representation storage, deterministic lint, CLI, MCP, and OpenClaw host entry.
    evidence_summary: The ClawHub listing describes an installable runtime with raw/wiki/schema language, runtime-owned structure, agent-owned synthesis, generated wiki navigation, representation storage, lint, CLI commands, MCP tools, and out-of-scope items.

[^6]:
    target: reports/source_gap_review.md
    target_version: report_snapshot
    pinned_version: reports/source_gap_review.md
    citation_role: secondary_gap_framing
    why_cited: Keeps non-blocking gaps visible so this architecture node does not claim neutral taxonomy, empirical reliability, ecosystem maturity, scale boundaries, enterprise suitability, or broad comparison conclusions.
    evidence_summary: The report says workflow architecture coverage is strong, but notes missing neutral architecture taxonomy, independent validation, long-term maintenance evidence, scale evidence, citation audits, governance coverage, and broader comparison evidence.

[^7]:
    target: reports/coverage_framework.md
    target_version: report_snapshot
    pinned_version: reports/coverage_framework.md
    citation_role: secondary_boundary_framing
    why_cited: Supplies project-level distinction terms such as observed facts, interpretations, hypotheses, source preservation, persistent representation, provenance, and maintenance without treating the framework as primary architecture evidence.
    evidence_summary: The framework defines evidence-oriented categories and boundary tests for LLM Wiki coverage, including source preservation, knowledge compilation, persistent representation, auditability, and maintenance over time.
