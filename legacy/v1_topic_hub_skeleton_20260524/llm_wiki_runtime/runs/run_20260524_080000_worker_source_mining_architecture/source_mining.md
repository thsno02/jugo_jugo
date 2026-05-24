# Source Mining

run_id:: run_20260524_080000_worker_source_mining_architecture
executor_role:: worker_executor
candidate_id:: cand_003_architecture

## Observations

| id | type | source | observation | architecture relevance | citation feasibility |
| --- | --- | --- | --- | --- | --- |
| obs_001 | observed_fact | `karpathy-gist-llm-wiki` | The gist has an `Architecture` section that explicitly says there are three layers: raw sources, the wiki, and the schema. | Directly supports the candidate's core three-layer architecture. | Strong; cite `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt`. |
| obs_002 | observed_fact | `karpathy-gist-llm-wiki` | Raw sources are described as a curated collection of source documents, including articles, papers, images, and data files; they are immutable and the LLM reads but does not modify them. | Supports raw source layer as source-of-truth layer. | Strong. |
| obs_003 | observed_fact | `karpathy-gist-llm-wiki` | The wiki is described as a directory of LLM-generated markdown files: summaries, entity pages, concept pages, comparisons, an overview, and a synthesis. The LLM owns the layer by creating, updating, cross-referencing, and keeping it consistent. | Supports compiled wiki layer as persistent generated knowledge artifact. | Strong. |
| obs_004 | observed_fact | `karpathy-gist-llm-wiki` | The schema is described as a document such as `CLAUDE.md` or `AGENTS.md` that tells the LLM how the wiki is structured, what conventions apply, and which workflows to follow for ingesting, answering, or maintaining. | Supports schema/instruction layer as operational discipline/configuration. | Strong. |
| obs_005 | interpretation | `karpathy-gist-llm-wiki` | The three layers can be synthesized as source-of-truth preservation, generated knowledge representation, and instruction-governed maintenance. | Safe architecture synthesis for first version, as long as it is labeled as worker synthesis from the gist's three named layers. | Strong if phrased as synthesis, not a verbatim source term. |
| obs_006 | observed_fact | `karpathy-gist-llm-wiki` | `index.md` is content-oriented and helps the LLM find pages before drilling into them; `log.md` is chronological and records ingests, queries, and lint passes. | Supports index/log as supporting infrastructure, not a fourth required core layer. | Strong. |
| obs_007 | observed_fact | `karpathy-gist-llm-wiki` | Optional CLI/search tools are described as useful later; the note says exact directory structure, schema conventions, page formats, and tooling depend on domain, preference, and LLM choice. | Supports a modular tooling boundary: tooling can support the layers but is not required by the abstract architecture. | Strong. |
| obs_008 | observed_fact | `karpathy-gist-llm-wiki` | Operations named in the gist are ingest, query, and lint. Ingest updates summary/index/log/relevant pages; query can file useful answers back into the wiki; lint checks contradictions, stale claims, orphans, missing pages, missing cross-references, and data gaps. | Supports the architecture's maintenance flows while leaving detailed workflow for `cand_004_workflow`. | Strong. |
| obs_009 | prior_kb_anchor | `kb/20260524_062000_llm_wiki_origin_and_canon.md` | The adopted origin/canon node already records the three-layer structure and says optional tools are modular, while forbidding broad adoption, enterprise, ecosystem, and empirical claims. | Confirms architecture candidate inherits a stable bounded-canon anchor. | Strong as prior KB anchor. |
| obs_010 | prior_kb_anchor | `kb/20260524_072000_llm_wiki_working_definition.md` | The adopted working-definition node states that the LLM Wiki pattern preserves raw sources, compiles them into a persistent markdown/wiki layer, and is governed by schema/instruction files and maintenance loops. | Confirms the architecture node can build on the adopted definition without redefining the whole pattern. | Strong as prior KB anchor. |
| obs_011 | implementation_evidence | `repo-atomicstrata-llm-wiki-compiler` | The README maps the pattern into `sources/`, hash checking, LLM concept extraction, wiki page generation, wikilink resolution, `index.md`, `wiki/`, `.llmwiki/schema.json`, review candidates, query/save, view, lint, watch, and MCP server. | Supports implementation-flavored examples of raw/source acquisition, compiled wiki output, schema, provenance, review, navigation, and tooling. | Strong for implementation details; keep secondary. |
| obs_012 | implementation_evidence | `repo-atomicstrata-llm-wiki-compiler` | The README describes source attribution in frontmatter and paragraph markers, plus line-range claim citations and lint validation for missing/malformed/impossible citations. | Supports provenance as supporting infrastructure around compiled pages, not a separate core layer. | Strong for implementation detail. |
| obs_013 | implementation_evidence | `repo-atomicstrata-llm-wiki-compiler` | The README's output model includes `wiki/concepts`, `wiki/queries`, `wiki/index.md`, `.llmwiki/schema.json`, and `.llmwiki/candidates` review queues. | Supports a concrete instantiation of compiled wiki layer, schema layer, index, and review workflow. | Strong for implementation detail. |
| obs_014 | implementation_evidence | `clawhub-llm-wiki-karpathy` | The listing describes a representation-first multimodal Markdown wiki runtime with a raw/wiki/schema operating model, runtime-owned structure, agent-owned synthesis, generated `wiki/index.md` and `wiki/log.md`, and deterministic lint. | Supports the same architectural vocabulary in an implementation/plugin context. | Strong for implementation detail; not primary. |
| obs_015 | gap | `reports/source_gap_review.md` | Source gap review says workflow architecture coverage is strong but notes there is no neutral architecture taxonomy and implementation evidence often comes from project authors. | Non-blocking gap: first version should be implementation-neutral and transparent about author-source bias. | Strong as gap report, but secondary. |

## Candidate Synthesis

The first architecture node can safely state that LLM Wiki has a bounded three-layer architecture:

1. Raw source layer: immutable curated source materials that the LLM reads but should not mutate.
2. Compiled wiki layer: persistent LLM-generated markdown/wiki pages that store summaries, entities, concepts, comparisons, overviews, syntheses, cross-links, and updates.
3. Schema/instruction layer: a project-specific instruction document or schema that tells the agent how the wiki is structured and which workflows to follow.

Supporting infrastructure can include:

- `index.md` for content navigation.
- `log.md` for chronological maintenance history.
- provenance/source markers, citations, candidate review queues, lint checks, viewers, search, CLI, MCP, and representation storage as implementation supports.

The node should avoid broad claims about ecosystem convergence, enterprise suitability, empirical benefits, scale limits, or superiority over RAG. It can cite repo and ClawHub only to show concrete implementations that instantiate or extend the three-layer pattern.

## Readiness Judgment

Evidence is enough for first-version node planning. The gist directly supports the core architecture, and the implementation sources give enough secondary support to describe common supporting infrastructure without turning the node into an ecosystem survey.
