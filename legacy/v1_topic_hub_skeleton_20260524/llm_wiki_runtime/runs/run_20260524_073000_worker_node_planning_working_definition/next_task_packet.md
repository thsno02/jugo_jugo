# Next Task Packet

run_id:: run_20260524_073000_worker_node_planning_working_definition
executor_role:: worker_executor
handoff_to:: generator_worker
candidate_id:: cand_002_working_definition
target_node_id:: 20260524_072000_llm_wiki_working_definition
version_target:: 1.0
source_mining_run:: .llmwiki/runs/run_20260524_072000_worker_source_mining_working_definition
frontier_status:: ready_to_build

## Task

Generate the first version bundle for the LLM Wiki working definition node.

Do not adopt the node. Do not update `kb/_index.yaml`. Do not write root `nodes/20260524_072000_llm_wiki_working_definition/node.yaml`.

## Required Output Paths

Write only these version-bundle files:

- `nodes/20260524_072000_llm_wiki_working_definition/versions/1.0/node.yaml`
- `nodes/20260524_072000_llm_wiki_working_definition/versions/1.0/card.md`
- `nodes/20260524_072000_llm_wiki_working_definition/versions/1.0/provenance.md`
- `nodes/20260524_072000_llm_wiki_working_definition/versions/1.0/change.md`

No other node, KB, generated, or root metadata output is requested.

## Allowed Inputs

Primary definitional source:

- `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt`
- `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt`

Prior KB anchor:

- `nodes/20260524_062000_llm_wiki_origin_and_canon/versions/1.0/card.md`
- `nodes/20260524_062000_llm_wiki_origin_and_canon/versions/1.0/provenance.md`
- `kb/20260524_062000_llm_wiki_origin_and_canon.md`

Bounded discourse/context sources:

- `data/raw/hacker_news/hacker-news-original-thread/text.txt`
- `data/raw/hacker_news/hacker-news-original-thread/item.json`
- `data/raw/webpage/karpathy-x-launch-post/text.txt`
- `data/raw/webpage/karpathy-x-launch-post/raw.txt`
- `data/raw/webpage/karpathy-x-launch-post/raw.json`

Secondary framing sources:

- `reports/source_gap_review.md`
- `reports/coverage_framework.md`

Planning artifacts:

- `.llmwiki/control/knowledge_frontier.yaml`
- `.llmwiki/runs/run_20260524_072000_worker_source_mining_working_definition/source_mining.md`
- `.llmwiki/runs/run_20260524_072000_worker_source_mining_working_definition/candidate_frontier_delta.yaml`
- `.llmwiki/runs/run_20260524_072000_worker_source_mining_working_definition/evidence_gaps.md`
- `.llmwiki/runs/run_20260524_072000_worker_source_mining_working_definition/retrieval_requests.md`
- `.llmwiki/runs/run_20260524_073000_worker_node_planning_working_definition/evidence_scope.yaml`

## Forbidden Inputs And Actions

- No network retrieval.
- No new source acquisition.
- Do not use unlisted raw sources for substantive claims.
- Do not write `nodes/20260524_072000_llm_wiki_working_definition/node.yaml`.
- Do not write `kb/20260524_072000_llm_wiki_working_definition.md`.
- Do not update `kb/_index.yaml`.
- Do not write `generated/`.
- Do not adopt or mark the node as adopted.

## Content Requirements

Define LLM Wiki operationally. The node should describe it as a source-preserving, LLM/agent-maintained knowledge pattern where immutable raw sources are compiled into a persistent, inspectable, interlinked markdown/wiki artifact governed by schema or instruction files and maintained through ingest, query, lint, and update/writeback loops. Human roles should be limited to source selection, question direction, emphasis, and review.

Separate source-backed observations from worker synthesis.

Use the gist as the primary source for definitional claims. Use the adopted origin/canon node only as a prior KB anchor and boundary support. Use HN and X only within the Hume/source-mining boundaries recorded in the evidence scope: HN for bounded early discourse and X for bounded launch context/source inventory. Use coverage framework and source-gap reports only as secondary framing.

## Boundary Requirements

Do not claim:

- enterprise readiness;
- empirical proof or measured superiority;
- broad adoption;
- full implementation ecosystem completeness;
- complete historical lineage;
- rigorous comparison against RAG, graph RAG, PKM, knowledge graphs, documentation systems, or agent memory;
- X social metrics as adoption evidence;
- HN discussion as authoritative technical proof.

## Audit Gates To Prepare For

The generated bundle must be ready for later audit against:

- object topic gate;
- source scope gate;
- citation gate;
- provenance gate;
- overclaim gate;
- retrieval gate;
- language gate;
- root metadata/adoption gate.

Completion marker for the generator should be `LOOP_DONE` only after all four version-bundle files above are written and no forbidden paths are written.

