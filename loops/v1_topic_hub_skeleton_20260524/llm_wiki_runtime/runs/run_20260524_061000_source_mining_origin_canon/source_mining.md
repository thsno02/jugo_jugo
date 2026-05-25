# Source Mining: Origin And Canon Batch

run_id:: run_20260524_061000_source_mining_origin_canon
phase:: source_mining
skill:: llmwiki-source-mining
main_language:: zh-CN
status:: LOOP_DONE

## Source structure pass

### `karpathy-gist-llm-wiki`

- Type: canonical idea file.
- Title: `LLM Wiki`.
- Declared purpose: communicate a high-level pattern that a user's LLM agent can instantiate collaboratively.
- Sections mined: core idea, architecture, operations, indexing/logging, optional CLI tools, tips, why this works, note.

### `karpathy-x-launch-post`

- Type: X API mirror / launch context.
- Contains a 2026-04-04 post saying the earlier tweet went viral and that the gist is an idea-file version.
- Contains a quoted 2026-04-02 original post titled `LLM Knowledge Bases`.
- Provides public propagation signals: replies, reposts, likes, bookmarks, quotes, views.

### `hacker-news-original-thread`

- Type: Hacker News story and comments.
- Story title: `LLM Wiki - example of an "idea file"`.
- Story metadata: 296 points, 95 comments, posted by `tamnd`, linking to the gist and X mirror.
- Comments include early comparison, support, skepticism, risk framing, and scale concerns.

## Source-backed observations

### Observed facts

- `karpathy-gist-llm-wiki` defines LLM Wiki as a pattern for building personal knowledge bases using LLMs; it explicitly frames the file as an idea file rather than a concrete implementation.
- The gist contrasts the pattern with common RAG-like file-upload workflows: raw documents are not only retrieved at query time; they are compiled into a persistent wiki that accumulates synthesis.
- The gist defines three architecture layers: raw sources, the wiki, and a schema/configuration document that tells the LLM how to maintain the wiki.
- The gist describes operations: ingest sources, query against the wiki, file useful outputs back into the wiki, and lint for contradictions, stale claims, orphan pages, missing links, and gaps.
- The gist names `index.md` and `log.md` as navigation/state files that help both the LLM and human understand the KB.
- The gist describes optional tools such as local markdown search or MCP integration as later efficiency improvements, not as required components.
- `karpathy-x-launch-post` records the 2026-04-04 idea-file publication context and links the gist to the earlier 2026-04-02 X post.
- The quoted 2026-04-02 X post describes `LLM Knowledge Bases`, raw source indexing, an LLM-compiled markdown wiki, Obsidian as frontend, Q&A over the wiki, filing outputs back, linting, extra tools, and possible future synthetic-data/finetuning explorations.
- `hacker-news-original-thread` records early public discussion of the idea file with 296 points and 95 comments.

### Interpretations

- The canonical pattern is not just "RAG without vectors"; it is a source-preserving, compilation-and-maintenance loop where the LLM writes a durable intermediate artifact.
- The most stable first-version abstraction is: raw sources remain immutable; the LLM-maintained wiki is compiled and updated; schema/instructions discipline future maintenance.
- The idea file intentionally leaves implementation specifics open, so a KB node should not overfit one filesystem layout or one editor/tool.

### Early discourse and skepticism

- HN discussion immediately questioned whether the pattern is "just RAG" or a distinct write/maintenance loop.
- HN discussion raised model-collapse, stale-claim, second-order-information, and wiki-scale maintenance risks.
- HN discussion also contained support for the raw-source/backlink discipline as a guard against drift and staleness.
- HN discussion questioned whether long-context models might reduce the need for this pattern, while other commenters argued queryable memory and maintained intermediate artifacts still have value.

### Evidence gaps

- Pre-Karpathy historical lineage is only partially covered in this batch. HN commenters mention older intellectual ancestors, but this run does not treat those as canonical origin evidence.
- Reddit reception and several community captures remain blocked in local data and should not support substantive claims until retrieved or exported later.
- Enterprise-scale claims require separate sources; the intercepted AICritique source is not usable for this node.

## Candidate knowledge mined

1. `llm_wiki_origin_and_canon`
   - Candidate statement: LLM Wiki's local canonical origin can be anchored to Karpathy's idea file, the launch/viral X post, and early HN discussion.
   - Evidence state: enough for first version.
   - Suggested status: `ready_to_build`.

2. `llm_wiki_working_definition`
   - Candidate statement: LLM Wiki can be operationally defined as source-preserved, LLM-compiled, schema-governed, maintained markdown/wiki knowledge.
   - Evidence state: needs first origin node as prior anchor, then ready for a separate node.
   - Suggested status: keep `discovered`.

3. `llm_wiki_vs_rag_write_loop`
   - Candidate statement: The distinction from RAG centers on durable write/maintenance and filed-back outputs, not on whether retrieval exists.
   - Evidence state: promising, but should be mined with comparison sources and not overloaded into the origin node.
   - Suggested status: `needs_more_mining`.

4. `llm_wiki_risk_discourse_initial`
   - Candidate statement: Early discourse already raised maintenance drift, second-order-information, and scale risks.
   - Evidence state: enough as discourse note inside origin node, not enough for full risk node.
   - Suggested status: `needs_more_mining`.

## Citation feasibility

| candidate | current support | citation feasibility |
| --- | --- | --- |
| `llm_wiki_origin_and_canon` | `karpathy-gist-llm-wiki`, `karpathy-x-launch-post`, `hacker-news-original-thread`, `claim_000001` to `claim_000008`, `covrec_origin_and_canon_*` | Strong enough for first-version node. |
| `llm_wiki_working_definition` | `karpathy-gist-llm-wiki`, `karpathy-x-launch-post`, `reports/coverage_framework.md` | Defer until origin node can be cited as prior KB anchor. |
| `llm_wiki_vs_rag_write_loop` | gist + HN discussion + comparison claims | Needs adjacent RAG/comparison mining before full node. |
| `llm_wiki_risk_discourse_initial` | HN thread + risk-related claim links | Needs risk source mining before full node. |

