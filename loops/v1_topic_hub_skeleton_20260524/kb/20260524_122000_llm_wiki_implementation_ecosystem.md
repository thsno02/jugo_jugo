# LLM Wiki Implementation Ecosystem

这个节点只描述本地语料中可观察到的 LLM Wiki implementation ecosystem：实现家族、工程表面、文件/数据形态、包与插件分发线索，以及证据边界。它不是市场地图、成熟度排名、采用规模判断，也不把 README 或目录页自述当成独立验证。[^15][^16]

**观察到的实现家族。** 本地语料支持一个有限的描述性 landscape：`nashsu/llm_wiki` README 自述为 UI/desktop/web app，包含 two-step ingest、multimodal input、graph/vector/search、persistent queue、review、web clipper 和 local API 等表面；`SamurAIGPT/llm-wiki-agent` 自述为 coding-agent skill/template，并列出 `raw/`、`wiki/`、`index.md`、`log.md`、`overview.md`、`sources/`、`entities/`、`concepts/`、`syntheses/`、`graph/` 等结构；`sdyckjq-lab/llm-wiki-skill` 则提供 skill/plugin UX、graph、confidence labels、cache、hooks、reports、comparison 和 timeline 输出线索。这里的稳妥结论是“本地捕获中存在这些实现形态”，不是它们代表全部生态或已被广泛采用。[^1][^2][^3]

**CLI、MCP 与本地工作流表面。** `llm-wiki-compiler` README 是较强的工程实现证据：它自述 npm CLI/MCP compiler，覆盖 ingest、compile、query、view、lint、watch、candidate review、source markers、source-range citations、confidence/contradiction metadata、retrieval/reranking 等操作。`obsidian-local-wiki` README 则把 LLM Wiki 放进 local-first Obsidian runtime：`olw` 命令、ingest/compile/review/query/lint/watch、provider switching、source hashes、rejection feedback、draft annotations、hand-edit protection 和 no-vector query mode 都是 source-specific 实现线索。[^4][^5]

**包、插件和多运行时分发线索。** PyPI 页可作为 registry metadata：`my-llm-wiki` 记录为 0.9.0、beta、MIT、Python >=3.10，并以 folder-to-queryable-knowledge-graph 方式自述；`llm-wiki-mcp` 记录为 0.1.1、alpha、MIT、Python >=3.11，并自述 MCP server、Claude Code skills、local filesystem storage、atomic writes、etag checks、log integrity 和 path containment。ClawHub 页是 plugin-directory 自述，描述 standalone CLI、stdio MCP server、config generator、OpenClaw host entry、raw/wiki/schema runtime、multimodal raw kinds、source-id repair、compile-readiness、gap mapping 和 deterministic lint；`llm-wiki.net` 项目页则自述 Claude Code、Codex、OpenCode、Pi 与 AGENTS.md 等多运行时命令/插件表面，以及 topic hubs、raw sources、compiled articles、audit、outputs、archive/inventory/dataset manifests。[^8][^9][^10][^11]

**相邻但不能并入核心的实现。** `OpenKB` README 可作为 long-document/OpenKB-like adjacent evidence：它自述 long-PDF/PageIndex-style handling、MarkItDown conversion、multimodality、wiki foundation、query/chat generators 和 skill factory；这只能说明本地语料中有相邻长文档/wiki generator 实现，不能推出所有 LLM Wiki 都支持长 PDF 或多模态。`librarian-mcp` README 可作为 MCP/graph-vault adjacent evidence：它面向 Markdown/Obsidian vault，提供 graph traversal、auto-wikilinks、trigram search、Louvain community detection、D3 graph view 和 slash-command wrappers；这说明 graph-vault/MCP 邻近实现存在，不等于 LLM Wiki 核心定义必须包含这些算法或图 UI。[^6][^7]

**共同工程表面应写成“在若干例子中复现”。** 跨这些直接实现来源，可以观察到若干反复出现的表面：raw/wiki/schema 或 vault-like storage，ingest/compile/query/lint/watch 操作，review 或 candidate queue，source citations/provenance/metadata，graph/search/view 层，MCP/plugin/API/local-provider 集成，以及 reports/logs/manifests 等生成物。这个句子的证据强度是 synthesis：它由多个 README、包页、插件页和项目页共同支持，但不能改写成“所有 LLM Wiki 实现都具备这些能力”。[^2][^4][^5][^9][^10][^11]

**GitHub metadata 只能作为快照元数据。** 本地 `github_repo.json` 可记录 stars、forks、open issues、language、license、created/updated/pushed timestamps 等 snapshot fields。例如 source mining 记录了 `nashsu/llm_wiki`、`SamurAIGPT/llm-wiki-agent`、`VectifyAI/OpenKB`、`sdyckjq-lab/llm-wiki-skill`、`atomicstrata/llm-wiki-compiler` 等仓库的本地快照字段。它们可以说明“本地语料保存了 repository surface metadata”，但不能证明 usage、quality、maturity、community consensus、production deployment 或 adoption scale。[^12][^15]

**证据缺口是节点的一部分。** 当前语料足以生成 bounded implementation landscape，但不支持 package downloads、plugin installs、active-user counts、traffic/clones、issue/PR outcome analysis、release-health/security posture、真实部署报告、独立质量评估，或 Reddit/community trend。`source_gap_review.md` 明确将 UX/tooling/ecosystem 覆盖视为足够做 preliminary landscape，同时把 adoption/community/deployment metrics 标为弱项；`coverage_framework.md` 要求 implementation survey 具有代表性、实现 claim 用 repo/docs citation，并避免把单一实现写成 definitive implementation。[^15][^16]

**可采用的窄结论。** LLM Wiki implementation ecosystem 在本地语料中已经不是单一 gist 或单一 repo，而是一组可观察的 implementation surfaces：应用、agent skill、CLI/MCP compiler、Obsidian/local-first runtime、Python package、plugin/runtime listing、multi-runtime project page，以及 OpenKB/graph-vault 等相邻系统。这个结论的强度停留在“本地来源显示了实现多样性和工程主题重复出现”；任何关于采用规模、市场成熟、可靠性、企业可用性或最佳实现的判断，都需要新一轮 source mining，而不是从这些 self-descriptions 外推。[^13][^14][^15][^16]

## References

### [R1] nashsu/llm_wiki README

target: data/raw/github_repo/repo-nashsu-llm-wiki/repo/README.md
target_version: raw_snapshot
pinned_version: data/raw/github_repo/repo-nashsu-llm-wiki/repo/README.md
citation_role: primary_implementation_source
why_cited: Provides direct README self-description for the UI/desktop/web-app implementation family and its ingest, multimodal, graph/search, queue, review, clipper, and API surfaces.
evidence_summary: The README supports source-specific claims about one app-oriented LLM Wiki implementation.

### [R2] SamurAIGPT/llm-wiki-agent README

target: data/raw/github_repo/repo-samuraigpt-llm-wiki-agent/repo/README.md
target_version: raw_snapshot
pinned_version: data/raw/github_repo/repo-samuraigpt-llm-wiki-agent/repo/README.md
citation_role: primary_implementation_source
why_cited: Provides direct README evidence for coding-agent skill/template structure and raw/wiki/index/log/graph file motifs.
evidence_summary: The README supports claims about file layout and ingest/query/lint/graph workflows in a coding-agent implementation.

### [R3] sdyckjq-lab/llm-wiki-skill README

target: data/raw/github_repo/repo-sdyckjq-llm-wiki-skill/repo/README.md
target_version: raw_snapshot
pinned_version: data/raw/github_repo/repo-sdyckjq-llm-wiki-skill/repo/README.md
citation_role: primary_implementation_source
why_cited: Provides README self-description for skill/plugin UX, confidence labels, cache, hooks, reports, comparisons, and timeline outputs.
evidence_summary: The README is used as project self-description, not as independent effectiveness or adoption evidence.

### [R4] atomicstrata/llm-wiki-compiler README

target: data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md
target_version: raw_snapshot
pinned_version: data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md
citation_role: primary_implementation_source
why_cited: Provides direct implementation evidence for a CLI/MCP compiler with ingest, compile, query, view, lint, watch, review, citations, provenance, confidence, contradiction metadata, and retrieval/reranking.
evidence_summary: The README is a strong engineering source for compiler and provenance/control surfaces.

### [R5] kytmanov/obsidian-local README

target: data/raw/github_repo/repo-kytmanov-obsidian-local/repo/README.md
target_version: raw_snapshot
pinned_version: data/raw/github_repo/repo-kytmanov-obsidian-local/repo/README.md
citation_role: primary_implementation_source
why_cited: Provides direct implementation evidence for local-first Obsidian runtime commands, provider switching, source hashes, review feedback, draft annotations, and hand-edit protection.
evidence_summary: The README supports source-specific claims about an Obsidian/local-first LLM Wiki workflow.

### [R6] VectifyAI/OpenKB README

target: data/raw/github_repo/repo-vectifyai-openkb/repo/README.md
target_version: raw_snapshot
pinned_version: data/raw/github_repo/repo-vectifyai-openkb/repo/README.md
citation_role: adjacent_implementation_source
why_cited: Provides adjacent long-document/OpenKB-like evidence for PageIndex-style long-PDF handling, MarkItDown conversion, multimodality, wiki foundation, query/chat generators, and skill factory.
evidence_summary: The README is used only for source-specific adjacent implementation breadth and not to generalize capabilities to all LLM Wiki implementations.

### [R7] ngmeyer/librarian-mcp README

target: data/raw/github_repo/repo-ngmeyer-librarian-mcp/repo/README.md
target_version: raw_snapshot
pinned_version: data/raw/github_repo/repo-ngmeyer-librarian-mcp/repo/README.md
citation_role: adjacent_implementation_source
why_cited: Provides adjacent MCP/graph-vault evidence for Markdown/Obsidian vault graph traversal, auto-wikilinks, trigram search, Louvain community detection, D3 graph view, and slash-command wrappers.
evidence_summary: The README supports graph-vault and MCP adjacency, not a universal LLM Wiki requirement.

### [R8] my-llm-wiki PyPI page

target: data/raw/pypi/pypi-my-llm-wiki/text.txt
target_version: raw_snapshot
pinned_version: data/raw/pypi/pypi-my-llm-wiki/text.txt
citation_role: package_registry_source
why_cited: Provides registry metadata and package self-description for the Python package/library family.
evidence_summary: The local PyPI capture supports version, maturity classifier, license, Python requirement, and package summary claims, not downloads or usage.

### [R9] llm-wiki-mcp PyPI page

target: data/raw/pypi/pypi-llm-wiki-mcp/text.txt
target_version: raw_snapshot
pinned_version: data/raw/pypi/pypi-llm-wiki-mcp/text.txt
citation_role: package_registry_source
why_cited: Provides registry metadata and package self-description for the MCP package family and local storage mechanics.
evidence_summary: The local PyPI capture supports version, alpha classifier, license, Python requirement, MCP/skills, local filesystem, atomic write, etag, log-integrity, and path-containment claims.

### [R10] ClawHub LLM Wiki Karpathy page

target: data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt
target_version: raw_snapshot
pinned_version: data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt
citation_role: plugin_directory_source
why_cited: Provides plugin-directory self-description for a CLI/MCP/OpenClaw-compatible runtime and raw/wiki/schema implementation surfaces.
evidence_summary: The page is treated as distribution-listing evidence, not usage or install evidence.

### [R11] llm-wiki.net project page

target: data/raw/webpage/llm-wiki-net/text.txt
target_version: raw_snapshot
pinned_version: data/raw/webpage/llm-wiki-net/text.txt
citation_role: project_page_source
why_cited: Provides project-page self-description for multi-runtime command/plugin support and implementation artifacts such as topic hubs, raw sources, compiled articles, audit, outputs, archive, inventory, and dataset manifests.
evidence_summary: The page supports source-specific multi-runtime implementation claims and is not used as independent adoption evidence.

### [R12] GitHub repository metadata snapshots

target: data/raw/github_repo/repo-nashsu-llm-wiki/github_repo.json
target_version: raw_snapshot
pinned_version: data/raw/github_repo/repo-nashsu-llm-wiki/github_repo.json
citation_role: metadata_snapshot_source
why_cited: Provides an example of local GitHub metadata fields and anchors the rule that stars, forks, issues, language, license, and timestamps are metadata only.
evidence_summary: The metadata snapshot is used only for repository surface fields and not for adoption, ranking, quality, or maturity claims.

### [R13] Source evidence matrix for implementation ecosystem

target: .llmwiki/runs/run_20260524_122000_worker_source_mining_implementation_ecosystem/evidence_matrix.yaml
target_version: source_mining_snapshot
pinned_version: .llmwiki/runs/run_20260524_122000_worker_source_mining_implementation_ecosystem/evidence_matrix.yaml
citation_role: process_evidence_map
why_cited: Pins the source-to-claim mapping, source quality notes, and local-complete retrieval state used for generation.
evidence_summary: The matrix separates primary implementation sources, metadata snapshots, package/plugin pages, adjacent implementations, and process/gap notes.

### [R14] Evidence scope for implementation ecosystem

target: .llmwiki/runs/run_20260524_123000_worker_node_planning_implementation_ecosystem/evidence_scope.md
target_version: planning_snapshot
pinned_version: .llmwiki/runs/run_20260524_123000_worker_node_planning_implementation_ecosystem/evidence_scope.md
citation_role: process_scope_source
why_cited: Pins allowed inputs, forbidden claim types, prior-KB limits, and the footnote layout contract for this candidate.
evidence_summary: The scope is used to keep generation inside a bounded implementation landscape.

### [R15] Source gap review

target: reports/source_gap_review.md
target_version: process_snapshot
pinned_version: reports/source_gap_review.md
citation_role: process_gap_source
why_cited: Provides gap framing for missing adoption, package download, plugin install, deployment, quality, and community-discourse evidence.
evidence_summary: The report supports caution around adoption and implementation-quality claims while recognizing enough tooling/ecosystem coverage for a preliminary landscape.

### [R16] Coverage framework

target: reports/coverage_framework.md
target_version: process_snapshot
pinned_version: reports/coverage_framework.md
citation_role: process_framework_source
why_cited: Provides evidence discipline requiring representative implementation survey, repo/docs citations, and avoidance of a single definitive implementation.
evidence_summary: The framework supplies process constraints for claim types and source quality.

### [R17] Adopted origin/canon node

target: kb/20260524_062000_llm_wiki_origin_and_canon.md
target_version: "1.0"
pinned_version: nodes/20260524_062000_llm_wiki_origin_and_canon/versions/1.0/card.md
citation_role: prior_kb_anchor
why_cited: Provides continuity around the LLM Wiki origin and canon boundary without serving as new implementation evidence.
evidence_summary: Used only as a boundary anchor.

### [R18] Adopted working definition node

target: kb/20260524_072000_llm_wiki_working_definition.md
target_version: "1.0"
pinned_version: nodes/20260524_072000_llm_wiki_working_definition/versions/1.0/card.md
citation_role: prior_kb_anchor
why_cited: Provides continuity around what counts as LLM Wiki while leaving implementation facts to primary sources.
evidence_summary: Used only as a vocabulary and boundary anchor.

### [R19] Adopted three-layer architecture node

target: kb/20260524_080000_llm_wiki_three_layer_architecture.md
target_version: "1.0"
pinned_version: nodes/20260524_080000_llm_wiki_three_layer_architecture/versions/1.0/card.md
citation_role: prior_kb_anchor
why_cited: Provides continuity around raw/wiki/schema layer language without supporting new implementation facts.
evidence_summary: Used only to keep layer vocabulary stable.

### [R20] Adopted ingest/compile/query/lint workflow node

target: kb/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow.md
target_version: "1.0"
pinned_version: nodes/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow/versions/1.0/card.md
citation_role: prior_kb_anchor
why_cited: Provides continuity around ingest, compile, query, lint, and writeback vocabulary.
evidence_summary: Used only as workflow terminology anchor.

### [R21] Adopted LLM Wiki vs RAG/write-loop node

target: kb/20260524_094000_llm_wiki_vs_rag_write_loop.md
target_version: "1.0"
pinned_version: nodes/20260524_094000_llm_wiki_vs_rag_write_loop/versions/1.0/card.md
citation_role: prior_kb_anchor
why_cited: Provides continuity around adjacent-system boundaries and prevents collapsing every retrieval or memory system into LLM Wiki.
evidence_summary: Used only as boundary anchor.

### [R22] Adopted risks/governance/provenance node

target: kb/20260524_104000_llm_wiki_risks_governance_and_provenance.md
target_version: "1.0"
pinned_version: nodes/20260524_104000_llm_wiki_risks_governance_and_provenance/versions/1.0/card.md
citation_role: prior_kb_anchor
why_cited: Provides continuity around provenance and citation-audit boundary language without serving as implementation ecosystem evidence.
evidence_summary: Used only as a boundary anchor for provenance wording.

## Footnotes

[^1]:
    target: data/raw/github_repo/repo-nashsu-llm-wiki/repo/README.md
    target_version: raw_snapshot
    pinned_version: data/raw/github_repo/repo-nashsu-llm-wiki/repo/README.md
    citation_role: primary_implementation_support
    why_cited: Supports source-specific claims that one local capture describes a UI/desktop/web-app implementation with two-step ingest, multimodal input, graph/vector/search, persistent queue, review, web clipper, and local API surfaces.
    evidence_summary: The README is used as project self-description for this implementation family, not as validation of adoption or quality.

[^2]:
    target: data/raw/github_repo/repo-samuraigpt-llm-wiki-agent/repo/README.md
    target_version: raw_snapshot
    pinned_version: data/raw/github_repo/repo-samuraigpt-llm-wiki-agent/repo/README.md
    citation_role: primary_implementation_support
    why_cited: Supports source-specific claims about the coding-agent skill/template family and raw/wiki/index/log/overview/sources/entities/concepts/syntheses/graph file structure.
    evidence_summary: The README documents file layout and ingest/query/lint/graph workflows for one agent-skill implementation.

[^3]:
    target: data/raw/github_repo/repo-sdyckjq-llm-wiki-skill/repo/README.md
    target_version: raw_snapshot
    pinned_version: data/raw/github_repo/repo-sdyckjq-llm-wiki-skill/repo/README.md
    citation_role: primary_implementation_support
    why_cited: Supports source-specific claims about skill/plugin UX, graph visualization, confidence labels, cache, hooks, reports, comparison tables, and timeline outputs.
    evidence_summary: The README is treated as project self-description and not as independent effectiveness evidence.

[^4]:
    target: data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md
    target_version: raw_snapshot
    pinned_version: data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md
    citation_role: primary_implementation_support
    why_cited: Supports claims about CLI/MCP compiler operations, review, source markers, source-range citations, confidence and contradiction metadata, and retrieval/reranking.
    evidence_summary: The README documents ingest, compile, query, view, lint, watch, candidate review, citations, provenance controls, and retrieval mechanics.

[^5]:
    target: data/raw/github_repo/repo-kytmanov-obsidian-local/repo/README.md
    target_version: raw_snapshot
    pinned_version: data/raw/github_repo/repo-kytmanov-obsidian-local/repo/README.md
    citation_role: primary_implementation_support
    why_cited: Supports claims about Obsidian/local-first commands, provider switching, source hashes, rejection feedback, draft annotations, hand-edit protection, and no-vector query mode.
    evidence_summary: The README documents an Obsidian-oriented local workflow and human-review/provenance controls.

[^6]:
    target: data/raw/github_repo/repo-vectifyai-openkb/repo/README.md
    target_version: raw_snapshot
    pinned_version: data/raw/github_repo/repo-vectifyai-openkb/repo/README.md
    citation_role: adjacent_implementation_support
    why_cited: Supports source-specific adjacent OpenKB/long-document claims while preserving the boundary that these features are not universal LLM Wiki capabilities.
    evidence_summary: The README documents long-PDF handling, MarkItDown conversion, multimodality, wiki foundation, query/chat generators, and skill factory for OpenKB.

[^7]:
    target: data/raw/github_repo/repo-ngmeyer-librarian-mcp/repo/README.md
    target_version: raw_snapshot
    pinned_version: data/raw/github_repo/repo-ngmeyer-librarian-mcp/repo/README.md
    citation_role: adjacent_implementation_support
    why_cited: Supports source-specific adjacent MCP/graph-vault claims while preserving the boundary that these capabilities are not required by all LLM Wiki implementations.
    evidence_summary: The README documents Markdown/Obsidian vault graph traversal, auto-wikilinks, trigram search, Louvain community detection, D3 graph view, and slash-command wrappers.

[^8]:
    target: data/raw/pypi/pypi-my-llm-wiki/text.txt
    target_version: raw_snapshot
    pinned_version: data/raw/pypi/pypi-my-llm-wiki/text.txt
    citation_role: package_registry_support
    why_cited: Supports package metadata and package self-description for the Python package/library family.
    evidence_summary: The PyPI page records version, beta classifier, MIT license, Python version requirement, and a summary about turning folders into queryable knowledge graphs.

[^9]:
    target: data/raw/pypi/pypi-llm-wiki-mcp/text.txt
    target_version: raw_snapshot
    pinned_version: data/raw/pypi/pypi-llm-wiki-mcp/text.txt
    citation_role: package_registry_support
    why_cited: Supports package metadata and package self-description for an MCP package with Claude Code skills and local storage safeguards.
    evidence_summary: The PyPI page records version, alpha classifier, MIT license, Python requirement, MCP server and skills, local filesystem storage, atomic writes, etag checks, log integrity, and path containment.

[^10]:
    target: data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt
    target_version: raw_snapshot
    pinned_version: data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt
    citation_role: plugin_directory_support
    why_cited: Supports plugin/runtime distribution claims for standalone CLI, stdio MCP server, config generator, OpenClaw host entry, raw/wiki/schema runtime, multimodal raw kinds, source-id repair, compile-readiness, gap mapping, and deterministic lint.
    evidence_summary: The directory page is used as self-description and not as install or usage evidence.

[^11]:
    target: data/raw/webpage/llm-wiki-net/text.txt
    target_version: raw_snapshot
    pinned_version: data/raw/webpage/llm-wiki-net/text.txt
    citation_role: project_page_support
    why_cited: Supports multi-runtime command/plugin self-description and claims about topic hubs, raw sources, compiled articles, audit, outputs, archive, inventory, and dataset manifests.
    evidence_summary: The project page is used as source-specific implementation evidence, not independent adoption evidence.

[^12]:
    target: data/raw/github_repo/repo-nashsu-llm-wiki/github_repo.json
    target_version: raw_snapshot
    pinned_version: data/raw/github_repo/repo-nashsu-llm-wiki/github_repo.json
    citation_role: metadata_snapshot_support
    why_cited: Supports the use of local GitHub metadata only as snapshot fields and anchors the warning against adoption or quality inference.
    evidence_summary: The JSON file records repository metadata fields such as stars, forks, open issues, language, license, and timestamps.

[^13]:
    target: .llmwiki/runs/run_20260524_122000_worker_source_mining_implementation_ecosystem/evidence_matrix.yaml
    target_version: source_mining_snapshot
    pinned_version: .llmwiki/runs/run_20260524_122000_worker_source_mining_implementation_ecosystem/evidence_matrix.yaml
    citation_role: process_evidence_support
    why_cited: Supports the overall source-to-claim mapping and evidence-quality distinctions used in this card.
    evidence_summary: The matrix separates primary implementation evidence, metadata snapshots, package/plugin pages, adjacent implementations, and process/gap notes.

[^14]:
    target: .llmwiki/runs/run_20260524_123000_worker_node_planning_implementation_ecosystem/evidence_scope.md
    target_version: planning_snapshot
    pinned_version: .llmwiki/runs/run_20260524_123000_worker_node_planning_implementation_ecosystem/evidence_scope.md
    citation_role: process_scope_support
    why_cited: Supports allowed claim types, forbidden claim types, source boundaries, prior-KB limits, and the requirement to keep References before final Footnotes.
    evidence_summary: The scope defines this node as a bounded implementation landscape and excludes adoption, ranking, quality, maturity, and broad trend claims.

[^15]:
    target: reports/source_gap_review.md
    target_version: process_snapshot
    pinned_version: reports/source_gap_review.md
    citation_role: process_gap_support
    why_cited: Supports the evidence-gap claims around package downloads, plugin installs, active users, deployment reports, issue/PR analysis, and independent quality evaluation.
    evidence_summary: The report says tooling/ecosystem coverage is enough for a preliminary landscape while adoption/community/deployment metrics remain weak or missing.

[^16]:
    target: reports/coverage_framework.md
    target_version: process_snapshot
    pinned_version: reports/coverage_framework.md
    citation_role: process_framework_support
    why_cited: Supports the representative-survey discipline and the rule that implementation claims need repo/docs citation and no single implementation should be definitive.
    evidence_summary: The framework distinguishes observed facts, interpretations, hypotheses, evaluation results, and strategic judgments.
