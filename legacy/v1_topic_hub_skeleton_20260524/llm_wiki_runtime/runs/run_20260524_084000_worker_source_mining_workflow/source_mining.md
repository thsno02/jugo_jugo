# Source Mining

run_id:: run_20260524_084000_worker_source_mining_workflow
executor_role:: worker_executor
candidate_id:: cand_004_workflow

## Source-Backed Observations

| type | observation | support | use for candidate |
|---|---|---|---|
| observed fact | The primary gist frames LLM Wiki as an abstract idea file for agents, not a fixed implementation. | `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` lines 3-5, 73-75 | The workflow node must describe a pattern, not a single product or CLI contract. |
| observed fact | The core maintenance loop starts when a new source enters the raw collection; the LLM reads it, discusses takeaways with the user, writes a summary page, updates index, updates relevant entity/concept pages, and appends to the log. | gist lines 35-38 | Direct support for ingest/update/file-back/index/log phases. |
| observed fact | Querying is against the wiki: the LLM searches relevant pages, reads them, synthesizes cited answers, and valuable answers can be filed back into the wiki as pages. | gist lines 39-40 | Direct support for query plus writeback/file-back as a workflow phase. |
| observed fact | Lint is a periodic health-check for contradictions, stale claims, orphan pages, missing concepts, missing cross-references, and data gaps that may need web search. | gist lines 41-42 | Direct support for lint/health-check and gap-discovery phase. |
| observed fact | `index.md` is content-oriented and updated on every ingest; query uses it first to find pages. | gist lines 43-48 | Direct support for log/index maintenance loop and index-first query at moderate scale, bounded to gist's own wording. |
| observed fact | `log.md` is chronological and append-only for ingests, queries, and lint passes; consistent prefixes make it parseable by simple tools. | gist lines 49-50 | Direct support for operation history/log maintenance. |
| observed fact | The gist leaves tooling optional and modular; directory structure, schema conventions, page formats, and tooling depend on domain/preference/LLM. | gist lines 51-53, 73-75 | Prevents the workflow node from requiring a particular CLI, MCP, Obsidian, search, or output format. |
| observed fact | The atomicstrata README gives an implementation pipeline: `sources/` to SHA-256 hash check, LLM concept extraction, wiki page generation, wikilink resolution, and `index.md`. | `data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md` lines 195-203 | Implementation support for compile pipeline and incremental change detection. |
| implementation evidence | Atomicstrata describes `query --save` as writing an answer as a page and rebuilding the index; saved answers become future query context. | README lines 205, 259-260 | Implementation support for query/writeback/index-refresh phase. |
| implementation evidence | Atomicstrata CLI commands cover ingest, compile, compile with review, review approve/reject, schema init/show, query, query save, view, lint, watch, and serve. | README lines 244-265 | Directly present process details for workflow tooling, with "implementation variant" status. |
| implementation evidence | Atomicstrata review mode writes candidates outside `wiki/`; approve writes into `wiki/` and refreshes index/MOC/embeddings, while reject archives. It also serializes review operations with a lock and defers source state/deletion bookkeeping in review mode. | README lines 293-310 | Support for bounded human review and write safety, not for broad governance claims. |
| implementation evidence | Atomicstrata lint validates low confidence, contradiction metadata, inferred paragraphs, source markers, malformed claim citations, impossible ranges, and ranges past source length. | README lines 331-352 | Support for lint/health-check and provenance-oriented failure handling in one implementation. |
| implementation evidence | Atomicstrata MCP server exposes automated pipeline tools for ingest, compile, query, search/read, lint, and wiki status; read-only tools and ingest do not require LLM credentials, while compile/query/search check provider availability. | README lines 408-452 | Support for agent interface details, not for ecosystem maturity. |
| limitation | Atomicstrata calls the software early and best for small, high-signal corpora; query routing is index-based. | README lines 474-478 | Keep first version from making scale or reliability claims. |
| implementation evidence | Atomicstrata explicitly maps Karpathy concepts to implemented commands: data ingest, compile wiki, Q&A, output filing, auto-recompile, lint/health-check, agent integration, and image support. | README lines 480-493 | Strong support for bounded workflow mapping as an implementation instantiation. |
| implementation evidence | ClawHub describes a runtime with raw/wiki/schema operating model, standalone CLI, stdio MCP server, config generator, and OpenClaw host entry. | `data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt` lines 27-39, 47-75 | Secondary implementation/runtime support for agent-facing workflow. |
| implementation evidence | ClawHub lists representation-first ingest for PDFs/images via asset inspection, compile readiness, stored OCR/vision/page notes/metadata/profiles, and final source-note compile after representation trail exists. | ClawHub lines 77-92 | Support for compile-readiness/representation path as implementation detail only. |
| implementation evidence | ClawHub CLI/MCP surfaces `kb_prepare_source`, `kb_prepare_source_bundle`, representation upsert/read, source/output/derived-note upserts, gap mapping/promotion, source-id repair, index rebuild, search/read, and lint. | ClawHub lines 94-144 | Supports phase/tooling substructure without turning it into required abstract architecture. |
| method | ClawHub splits runtime-owned canonical paths/IDs/validation/deterministic writes/manifest tracking/navigation from agent-owned summarization/OCR/vision/profiling/synthesis and deciding output kind. | ClawHub lines 146-174 | Useful boundary for runtime-vs-agent responsibilities in workflow node. |
| gap | ClawHub explicitly does not implement embeddings/vector search, database-backed indexing, rename tracking, built-in OCR/vision/PDF parsing, or autonomous background agents. | ClawHub lines 176-189 | Prevents overclaiming implementation completeness or autonomy. |
| prior KB anchor | Adopted origin/canon, working definition, and architecture nodes already bound the gist as canon, define source-preserving agent-maintained wiki, and reserve detailed ingest/compile/query/lint workflow for cand_004. | `kb/20260524_062000...`, `kb/20260524_072000...`, `kb/20260524_080000...` | Lets cand_004 build on established boundaries without re-litigating origin/definition/architecture. |
| secondary coverage note | Source gap review says workflow architecture coverage is strong and names gist, repo READMEs, and ClawHub listing as relevant, but also says neutral architecture taxonomy, measurement, scale, governance, and comparison remain gaps. | `reports/source_gap_review.md` lines 75-115, 181-214 | Supports `ready_to_build` for bounded workflow while preserving non-blocking gaps. |
| secondary framework | Coverage framework distinguishes observed facts, interpretations, hypotheses, evaluation results, and strategic judgments; it treats source preservation, knowledge compilation, persistent representation, provenance/auditability, and maintenance as boundary tests. | `reports/coverage_framework.md` lines 31-74 | Helps node planner enforce evidence labels and avoid unsupported conclusions. |

## Candidate Synthesis

The bounded first-version workflow candidate is ready to build as a process node with this shape:

1. **Ingest/source intake**: human-curated raw sources enter the raw collection; LLM/agent reads and processes them without modifying raw sources.
2. **Compile/wiki update**: source information is compiled into markdown/wiki pages, summaries, entity/concept pages, links, index, and log; implementation variants may add hash checks, two-phase compile, candidate review, representation readiness, and deterministic writes.
3. **Query/synthesis**: questions are answered against the compiled wiki by using index/search/page reads; cited outputs may be saved back as new pages.
4. **Lint/health-check**: periodic checks surface contradictions, stale claims, orphan pages, missing concepts/links, citation/provenance issues, unsupported or high-inference content, and gaps.
5. **Update/file-back/log maintenance**: valuable outputs, approved candidates, repaired IDs, rebuilt indexes, promoted gaps, and lint/query/ingest events update the durable wiki and operation history.

## Evidence Sufficiency Decision

`cand_004_workflow` has enough evidence for a bounded first version. The gist directly supports the abstract operations and index/log/writeback loop. Atomicstrata and ClawHub provide directly present implementation/process details for compile, review, lint, MCP/CLI, representation readiness, gap mapping, and deterministic runtime responsibilities. The candidate should remain bounded and must not claim empirical effectiveness, scale reliability, enterprise readiness, or ecosystem convergence.

