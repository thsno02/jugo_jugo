# LLM Wiki 的 ingest/compile/query/lint 维护工作流

这个节点描述的是 LLM Wiki 的有界维护工作流：人类策展 raw sources 并指导问题与重点，LLM/agent 在 schema 或 instruction 约束下，把来源纳入、编译成 wiki、基于 wiki 回答问题、执行健康检查，并把有价值的输出或修复写回持久知识层。这里的说法是对当前证据的工作性综合，不是企业成熟度、经验效果、规模可靠性或实现生态判断。[^1][^2][^3]

**来源支持的观察：ingest/source intake。** Karpathy gist 把 `ingest` 写成新来源进入 raw collection 后的维护动作：LLM 读取来源，与用户讨论要点，写 summary page，更新 index，更新相关 entity/concept pages，并向 log 追加记录。这个阶段的关键边界是 raw sources 仍作为来源真值存在；LLM 读取和转写它们，但不把原始依据替换成无来源的聊天记忆。[^1][^3]

**来源支持的观察：compile/wiki update。** 在已采纳三层架构中，workflow 的 compile 部分连接 raw source layer 与 compiled wiki layer：来源信息被整理成 markdown/wiki 页面、摘要、实体页、概念页、比较、概览或综合，并通过 schema/instruction layer 约束目录、约定和维护动作。这个节点把“compile”理解为持续 wiki update，而不是一次性摘要生成；它要求结果能被后续人或 agent 读取、检查、链接和修订。[^1][^4]

**来源支持的观察：query/synthesis 与 file-back。** Gist 中的 `query` 是对 wiki 提问：LLM 搜索相关页面、读取页面、综合带 citation 的答案；重要答案可以作为新页面 filed back into the wiki。因而 query 不是纯粹的末端消费动作，而是维护循环的一部分：一次问答如果产生了可复用分析、比较或连接，就可以进入 compiled wiki，成为后续查询的上下文。[^1][^2]

**来源支持的观察：lint/health-check。** Gist 把 `lint` 写成周期性 wiki 健康检查，用来寻找页面间矛盾、被新来源 supersede 的 stale claims、无入链 orphan pages、被提到却没有独立页面的重要概念、缺失 cross-references，以及仍需检索的数据缺口。这里可支持的是“检查项与维护意图”；不能据此推出任一实现已经具备充分可靠的自动质量保证。[^1]

**导航与操作历史。** `index.md` 和 `log.md` 在该工作流中分别承担导航与历史记录：index 是面向内容的目录，帮助人和 LLM 先定位相关页面；log 是按时间追加的 ingest、query 和 lint pass 记录，帮助追踪 wiki 的演化。它们是维护循环的基础设施，而不是独立的第四层架构。[^1][^4]

**实现变体：compiler 风格。** `llm-wiki-compiler` README 提供了一个实现过程例子：`sources/` 经过 hash check、LLM concept extraction、wiki page generation、wikilink resolution 到 `index.md`；`query --save` 会把答案写成 wiki page 并重建 index；`compile --review`、approve/reject、source markers、line-range citations、lint、watch、viewer 和 MCP tools 进一步把 compile、review、query、lint 和 agent interface 工具化。这个证据只能说明一种实现如何支撑抽象工作流，不能把 hash check、review queue、viewer、MCP 或某个目录布局写成 LLM Wiki 的普遍必要条件。[^5]

**实现变体：runtime 风格。** ClawHub listing 描述了另一个 runtime：raw/wiki/schema operating model、representation-first ingest、compile-readiness tracking、stored representations、source-note validation、gap mapping/promotion、generated index/log、deterministic lint、CLI/MCP tools，以及 runtime 与 agent 的责任分割。这个来源支持“实现可把路径、ID、验证、确定性写入和导航交给 runtime，把 summarization、OCR/vision/profiling 和 synthesis 留给 agent”的过程边界；它不支持采用率、生态成熟度、经验效果或自主后台 agent 之类外推。[^6]

**工作流综合。** 因此，首版可以把 LLM Wiki 的维护工作流写成一个循环：`curated raw sources -> ingest/source intake -> compile/wiki update -> query/synthesis -> file-back/update -> lint/health-check -> index/log maintenance -> 下一轮 ingest 或 query`。这个循环依赖已采用的工作定义和三层架构：raw sources 保存依据，compiled wiki 保存可复用知识，schema/instructions 约束 agent 如何维护。实现可以增加 CLI、MCP、review queue、representation storage、source validation、deterministic writes 或 gap promotion，但这些都是实现选择，不是抽象定义的硬性条件。[^2][^3][^4][^5][^6]

**人的角色与边界。** Gist 对人的角色给出的是来源选择、探索方向、问题提出、重点强调和审阅；LLM 承担 summarizing、cross-referencing、filing、bookkeeping 等维护劳动。这个节点据此把 workflow 写成 human-in-the-loop 的维护循环：人类并未退出判断，agent 也不是无约束自治；schema、review、citation、lint、log 和 index 都是在不同实现中帮助保持可检查性的机制。[^1][^2]

**证据缺口。** 当前证据足够生成一个 bounded first version，但仍不足以说明 ingest 质量、compile 可靠性、citation accuracy、长期 drift、scale behavior、企业治理、隐私安全、采用情况或与 RAG/PKM/knowledge graph/agent memory 的系统比较。source gap review 和 coverage framework 只作为边界与标签词汇使用，不作为 primary workflow authority。[^7][^8]

## References

### [R1] Karpathy LLM Wiki idea file

target: data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt
target_version: raw_snapshot
pinned_version: data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt
citation_role: primary_workflow_source
why_cited: Provides the direct source for the abstract ingest, query, lint, index/log, human role, and modular-tooling workflow claims.
evidence_summary: The local gist text describes LLM Wiki as an idea file whose operations include ingesting sources into wiki updates, answering against the wiki with citations and file-back, linting for health issues, and maintaining index/log files.

### [R2] Adopted LLM Wiki working definition

target: kb/20260524_072000_llm_wiki_working_definition.md
target_version: "1.0"
pinned_version: nodes/20260524_072000_llm_wiki_working_definition/versions/1.0/card.md
citation_role: prior_kb_dependency
why_cited: Supplies the adopted definition that the workflow operationalizes as a source-preserving, agent-maintained knowledge pattern.
evidence_summary: The adopted node ties LLM Wiki to immutable raw sources, persistent compiled wiki artifacts, schema/instruction governance, and ingest/query/lint/update maintenance.

### [R3] Adopted bounded origin/canon node

target: kb/20260524_062000_llm_wiki_origin_and_canon.md
target_version: "1.0"
pinned_version: nodes/20260524_062000_llm_wiki_origin_and_canon/versions/1.0/card.md
citation_role: prior_kb_dependency
why_cited: Preserves the local canon and overclaim boundaries for this workflow node.
evidence_summary: The adopted node identifies the Karpathy gist as bounded canon and blocks broader adoption, enterprise, ecosystem, empirical, or full-historical claims without separate evidence.

### [R4] Adopted LLM Wiki three-layer architecture

target: kb/20260524_080000_llm_wiki_three_layer_architecture.md
target_version: "1.0"
pinned_version: nodes/20260524_080000_llm_wiki_three_layer_architecture/versions/1.0/card.md
citation_role: prior_kb_dependency
why_cited: Provides the adopted raw/wiki/schema architecture that this node turns into a bounded maintenance workflow.
evidence_summary: The adopted node distinguishes raw source layer, compiled wiki layer, schema/instruction layer, and supporting index/log/tooling infrastructure.

### [R5] llm-wiki-compiler README

target: data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md
target_version: raw_snapshot
pinned_version: data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md
citation_role: implementation_variant_source
why_cited: Gives directly mined process and tooling details for one compiler-style implementation of the workflow.
evidence_summary: The README describes ingest, incremental compile, review candidates, query save, index rebuild, source markers, line-range citations, lint diagnostics, local viewer, watch mode, and MCP server tools.

### [R6] ClawHub LLM Wiki Karpathy listing

target: data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt
target_version: raw_snapshot
pinned_version: data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt
citation_role: implementation_variant_source
why_cited: Gives directly mined runtime details for a representation-first CLI/MCP implementation of the workflow.
evidence_summary: The listing describes raw/wiki/schema runtime responsibilities, representation storage, compile-readiness states, source validation, gap mapping and promotion, generated index/log, deterministic lint, and runtime-agent responsibility boundaries.

### [R7] Source gap review

target: reports/source_gap_review.md
target_version: report_snapshot
pinned_version: reports/source_gap_review.md
citation_role: secondary_gap_report
why_cited: Keeps unresolved evidence gaps visible and prevents this first version from overclaiming beyond the scoped workflow.
evidence_summary: The report says workflow architecture coverage is strong but flags gaps around neutral taxonomy, independent validation, scale, citation accuracy, long-term maintenance, governance, and comparison.

### [R8] LLM Wiki coverage framework

target: reports/coverage_framework.md
target_version: report_snapshot
pinned_version: reports/coverage_framework.md
citation_role: secondary_boundary_framework
why_cited: Provides evidence-label and boundary vocabulary for distinguishing observed facts from synthesis and hypotheses.
evidence_summary: The framework describes source preservation, knowledge compilation, persistent representation, provenance/auditability, and maintenance as boundary tests for LLM Wiki coverage.

## Footnotes

[^1]:
    target: data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt
    target_version: raw_snapshot
    pinned_version: data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt
    citation_role: primary_workflow_support
    why_cited: Supports the abstract workflow claims about ingest, query, lint, index.md, log.md, human guidance, and optional/modular tooling.
    evidence_summary: The gist describes new-source ingest into wiki pages, index, entity/concept updates and log; wiki-based query with cited synthesis and file-back; periodic lint for contradictions, stale claims, orphans, missing concepts, missing links and gaps; and index/log maintenance.

[^2]:
    target: kb/20260524_072000_llm_wiki_working_definition.md
    target_version: "1.0"
    pinned_version: nodes/20260524_072000_llm_wiki_working_definition/versions/1.0/card.md
    citation_role: prior_kb_anchor
    why_cited: Carries forward the adopted definition of LLM Wiki as a source-preserving, agent-maintained pattern with ingest/query/lint/update loops.
    evidence_summary: The adopted working-definition node defines LLM Wiki around immutable raw sources, persistent markdown/wiki artifacts, schema-governed maintenance, and human source/question steering.

[^3]:
    target: kb/20260524_062000_llm_wiki_origin_and_canon.md
    target_version: "1.0"
    pinned_version: nodes/20260524_062000_llm_wiki_origin_and_canon/versions/1.0/card.md
    citation_role: prior_kb_anchor
    why_cited: Anchors the workflow to the adopted bounded canon and preserves prohibitions against adoption, ecosystem, enterprise, empirical, and broad historical claims.
    evidence_summary: The adopted origin/canon node treats the Karpathy gist as the local bounded canon and limits broader discourse or launch context to non-authoritative context.

[^4]:
    target: kb/20260524_080000_llm_wiki_three_layer_architecture.md
    target_version: "1.0"
    pinned_version: nodes/20260524_080000_llm_wiki_three_layer_architecture/versions/1.0/card.md
    citation_role: prior_kb_anchor
    why_cited: Provides the adopted raw/wiki/schema architecture that this workflow node operationalizes without re-opening architecture scope.
    evidence_summary: The adopted architecture node describes raw sources, compiled wiki, and schema/instruction layers, and treats index/log and tooling as supporting infrastructure rather than core layers.

[^5]:
    target: data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md
    target_version: raw_snapshot
    pinned_version: data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md
    citation_role: implementation_variant_support
    why_cited: Supports directly mined implementation details for source-to-wiki compile, review, query save, lint, watch, viewer, source markers, line-range citations, and MCP tools.
    evidence_summary: The README describes a pipeline from sources through hash checks, concept extraction, page generation, wikilink resolution and index; query --save; review candidates; citation/provenance markers; lint checks; and CLI/MCP surfaces.

[^6]:
    target: data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt
    target_version: raw_snapshot
    pinned_version: data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt
    citation_role: implementation_variant_support
    why_cited: Supports directly mined runtime details for representation-first ingest, compile readiness, source validation, gap mapping, index/log generation, deterministic lint, CLI/MCP tools, and runtime-agent responsibility split.
    evidence_summary: The listing describes raw/wiki/schema runtime structure, stored representations, readiness states, source-note validation, generated navigation, deterministic lint, CLI and MCP tool surfaces, and explicit out-of-scope items.

[^7]:
    target: reports/source_gap_review.md
    target_version: report_snapshot
    pinned_version: reports/source_gap_review.md
    citation_role: secondary_gap_framing
    why_cited: Records non-blocking gaps so the workflow node does not overclaim quality, reliability, scale, governance, adoption, ecosystem maturity, or broad comparison conclusions.
    evidence_summary: The report marks workflow architecture coverage as strong while noting missing neutral taxonomy, independent validation, long-term maintenance evidence, scale evidence, citation audits, governance coverage, and comparison evidence.

[^8]:
    target: reports/coverage_framework.md
    target_version: report_snapshot
    pinned_version: reports/coverage_framework.md
    citation_role: secondary_boundary_framing
    why_cited: Supplies project vocabulary for evidence labels and boundary tests without replacing the gist as primary workflow authority.
    evidence_summary: The framework distinguishes observed facts, interpretations, hypotheses, evaluation results, and strategic judgments, and lists source preservation, compilation, persistent representation, provenance, and maintenance as boundary dimensions.
