# Source Mining: Origin And Canon Worker Rerun

run_id:: run_20260524_062000_worker_source_mining_origin_canon
executor_role:: worker_executor
phase:: source_mining
skill:: llmwiki-source-mining
status:: LOOP_DONE

## Structure Pass

### `karpathy-gist-llm-wiki`

- Type: canonical idea file.
- Title: `LLM Wiki`.
- Declared purpose: communicate the high-level pattern so an LLM agent can instantiate a specific version with the user.
- Sections mined: core idea, architecture, operations, indexing/logging, optional CLI tools, tips and tricks, why this works, note.

### `karpathy-x-launch-post`

- Type: X API mirror source record.
- Current worker-readable state: `text.txt`, `raw.txt`, and `raw.json` are empty.
- Manifest/digest state: source is recorded as `status: ok` and digest summary indicates launch-context content, but the raw source cannot be independently verified from the allowed files in this run.
- Mining decision: do not use X raw text as direct evidence; record a retrieval/recapture gap.

### `hacker-news-original-thread`

- Type: Hacker News story and comments.
- Story title in text: `LLM Wiki - example of an "idea file"`.
- Story metadata in text: `296 points`, `95 comments`, story by `tamnd`, and links to the gist and X mirror.
- Sections mined: early comments about model collapse, raw-source/backlink discipline, RAG comparison, write-loop distinction, scale concerns, personal workflow reports, AI de-skilling concerns, and similar-system references.

## Source-Backed Observations

### Observed facts

- `karpathy-gist-llm-wiki` presents LLM Wiki as a pattern for building personal knowledge bases using LLMs and explicitly calls the document an idea file rather than a complete implementation.
- The gist contrasts ordinary RAG/file-upload workflows with an incremental wiki-building workflow: raw documents are not only retrieved at query time; the LLM compiles and maintains a durable intermediate wiki.
- The gist defines three layers: immutable raw sources, an LLM-generated markdown wiki, and a schema/instructions document such as `CLAUDE.md` or `AGENTS.md`.
- The gist assigns different roles to human and LLM: the human curates sources, explores, and asks questions; the LLM writes summaries, cross-references, filing updates, and maintenance edits.
- The gist names three core operations: ingest, query, and lint.
- The gist describes `index.md` as content-oriented navigation and `log.md` as a chronological append-only record.
- The gist frames optional tooling such as local markdown search, hybrid BM25/vector search, and MCP integration as modular enhancements rather than requirements.
- The HN capture records immediate public discussion around the gist, including story metadata and links to both the gist and X mirror.
- HN comments include both supportive and skeptical reactions, including claims that the pattern resembles RAG or assistant memory, and counterclaims that the write/maintenance loop is the distinctive part.

### Interpretations

- The most defensible first-version canonical abstraction is: LLM Wiki is a source-preserving, LLM-compiled, schema-governed, persistent markdown/wiki knowledge layer maintained over time.
- The core distinction from transient chat memory or simple file upload is the durable writeback/maintenance loop, not the absence of retrieval.
- The idea file deliberately leaves implementation details open, so downstream KB generation should avoid treating Obsidian, `index.md`, `log.md`, qmd, MCP, or any specific directory layout as mandatory.
- Because the allowed X raw files are empty, this worker run can mention X only as a recorded but currently unreadable launch-context source; exact X wording and metrics must not be treated as direct evidence here.

### Discourse notes

- HN discussion raised the "just RAG" objection and also surfaced a counter-position: a static retrieval corpus differs from a maintained wiki that files outputs and updates pages.
- HN discussion raised risks around model collapse, second-order information, stale or overgeneralized claims, context bloat, quality assurance, and whether humans lose the thinking benefits of writing notes themselves.
- HN comments also identify adjacent lineages and systems, including Obsidian/PKM, instruction files, assistant memory, structured markdown/DB hybrids, and existing wiki/documentation systems.
- One HN defense emphasizes raw source files and backlinks as a guardrail for staleness, correctness, and drift.

### Gaps

- Exact X launch-post text and quantitative social metrics cannot be independently verified from the current allowed X raw files.
- `hacker-news-original-thread/item.json` is empty, so structured HN metadata must not be claimed beyond what appears in `text.txt`.
- Pre-Karpathy historical lineage is not established by this batch; HN mentions older analogues but does not settle origin history.
- Early implementations, enterprise use, empirical effectiveness, and governance claims require separate mining.

## Candidate Knowledge Mined

1. `cand_001_origin_and_canon`
   - Candidate statement: LLM Wiki's local canonical origin can be anchored to Karpathy's idea file and immediate HN discussion; the first node should describe the idea-file pattern, its architecture/operations, and early discourse while marking the X raw recapture gap.
   - Evidence state: enough for first version with bounded claims.
   - Suggested status: `ready_to_build`.

2. `cand_010_vs_rag_write_loop`
   - Candidate statement: The important comparison with RAG centers on durable writeback, maintained intermediate artifacts, and filed-back outputs.
   - Evidence state: promising but needs dedicated comparison mining.
   - Suggested status: `needs_more_mining`.

3. `cand_011_initial_risk_discourse`
   - Candidate statement: Early discourse already contains risk terms around drift, staleness, cognitive offloading, and scale/maintenance failure.
   - Evidence state: discourse-only seed; needs risk/governance mining.
   - Suggested status: `needs_more_mining`.

## Citation Feasibility

| candidate | direct support in this worker run | citation feasibility |
| --- | --- | --- |
| `cand_001_origin_and_canon` | gist text for canonical pattern; HN text for immediate discussion and controversy; manifests/claims/coverage for local source inventory and corpus-level mapping | Strong enough for a first-version origin/canon node if X-specific claims are avoided or marked as unverified. |
| `cand_010_vs_rag_write_loop` | gist RAG contrast and HN comparison debate | Not enough for a full comparison node; mine RAG/GraphRAG/agent-memory sources first. |
| `cand_011_initial_risk_discourse` | HN comments about model collapse, second-order information, quality assurance, scale, and cognitive offloading | Not enough for a full risk node; mine governance and empirical sources first. |

