# Source Mining

run_id:: run_20260524_072000_worker_source_mining_working_definition
executor_role:: worker_executor
candidate_id:: cand_002_working_definition

## Mining Lens

This pass asks whether the local source batch can support a first-version working-definition node. It does not attempt to build the node and does not adopt a card.

## Source-Backed Observations

| Type | Observation | Source Support | Candidate Relevance |
| --- | --- | --- | --- |
| observed_fact | The gist frames LLM Wiki as a pattern for building personal knowledge bases using LLMs and as an abstract idea file meant to communicate the pattern rather than prescribe a fixed implementation. | `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` | Supports a working definition rather than an implementation-specific definition. |
| observed_fact | The core idea contrasts one-shot retrieval from raw documents with a persistent wiki that sits between the user and raw sources. | `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` | Supports “persistent intermediate knowledge artifact” as central to the definition. |
| observed_fact | New sources are read, key information is extracted, and existing wiki pages are updated, including entity pages, topic summaries, contradictions, and evolving syntheses. | `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` | Supports LLM/agent-compiled and maintained knowledge artifacts. |
| observed_fact | The gist describes three layers: immutable raw sources, an LLM-generated markdown wiki, and a schema/instructions document such as `CLAUDE.md` or `AGENTS.md`. | `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` | Directly supports the raw/wiki/schema definition boundary. |
| observed_fact | The raw-source layer is described as a curated collection of source documents that the LLM reads but does not modify, and as the source of truth. | `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` | Supports “source-preserved raw layer.” |
| observed_fact | The wiki layer is described as LLM-generated markdown containing summaries, entity pages, concept pages, comparisons, an overview, and synthesis; the LLM creates and updates pages and maintains cross-references. | `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` | Supports “LLM/agent-compiled wiki artifact.” |
| observed_fact | The schema layer tells the LLM how the wiki is structured, which conventions to follow, and what workflows apply when ingesting sources, answering questions, or maintaining the wiki. | `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` | Supports “schema/instruction maintenance rules.” |
| observed_fact | The gist names three operations: `ingest`, `query`, and `lint`; `ingest` updates pages/index/log, `query` synthesizes answers from the wiki and may file valuable answers back, and `lint` checks contradictions, stale claims, orphan pages, missing concepts, missing links, and source gaps. | `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` | Supports the ingest/query/lint/update loop. |
| observed_fact | The human role is to curate sources, direct analysis, ask good questions, review summaries, check updates, and guide what to emphasize; the LLM does summarizing, cross-referencing, filing, and bookkeeping. | `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` | Supports “human source/question steering.” |
| observed_fact | The note section explicitly says the document is abstract, describes the idea rather than a specific implementation, and leaves directory structure, schema conventions, page formats, tooling, and output formats to the user/domain/LLM. | `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` | Supports keeping the first definition bounded and non-prescriptive. |
| observed_fact | The adopted origin/canon node states that a later working-definition node still needs independent generation and audit, while the origin node already anchors the gist as bounded canon. | `nodes/20260524_062000_llm_wiki_origin_and_canon/versions/1.0/card.md`; `kb/20260524_062000_llm_wiki_origin_and_canon.md` | Clears the prior `needs_origin_anchor_first` blocker without replacing this mining pass. |
| coverage_status | The source-gap review marks origin/definition coverage as strong and says the corpus is enough to describe immutable raw sources, LLM-authored wiki, schema/instructions, index/log, ingest/query/lint, and compounding writeback. | `reports/source_gap_review.md` | Confirms readiness for a preliminary definition, but is not used as primary topic evidence. |
| coverage_status | The coverage framework asks for a clear definition and boundary tests distinguishing LLM Wiki from vector retrieval alone, ordinary chat memory alone, and human-only PKM. | `reports/coverage_framework.md` | Helps bound node-planning scope; should not be cited as Karpathy’s own claim. |
| gap | Reports and the adopted origin/canon node both warn against enterprise, empirical effectiveness, full ecosystem, adoption, and broad comparison claims without separate mining. | `reports/source_gap_review.md`; adopted origin/canon node | These limits become build constraints rather than blockers for a bounded working-definition node. |

## Candidate Synthesis

The source batch is enough for a first-version working-definition candidate:

> LLM Wiki is a source-preserving, LLM/agent-maintained knowledge pattern in which immutable raw sources feed a persistent, inspectable, interlinked markdown/wiki layer governed by schema or instruction files; the system compounds through ingest, query, lint, and update loops while humans steer source selection, questions, emphasis, and review.

This is a working definition, not a final ecosystem definition. It is source-backed by the gist and bounded by the adopted origin/canon node and coverage reports.

## Citation Feasibility

Citation feasibility is strong for a bounded first version:

- primary definition claims can cite `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt`;
- the prior origin/canon anchor can cite the adopted node/card/provenance only for process and boundary context;
- HN and X can be omitted or used only for discourse/source-inventory boundaries;
- reports/manifests can be cited only for coverage status or planning gaps, not as primary definitional authority.

## Frontier Recommendation

Set `cand_002_working_definition` to `ready_to_build` with `evidence_state: enough_for_first_version`, `retrieval_required_before_build: false`, and build constraints that keep the node bounded to a working definition.
