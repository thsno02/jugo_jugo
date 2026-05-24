# Process Findings

## Controller Boundary

status:: maintained_with_watch

The cand_006 chain was worker-attributed from source mining through adoption/view. The main/controller role remained packet/review/next-decision oriented in the artifacts reviewed. No new controller-authored concrete KB artifact was found in this cand_006 chain.

Residual risk remains because replacement-audit dispatch happened after an earlier audit startup stall, and the replacement task packet was described as user/controller instruction rather than a reusable run packet. That did not contaminate the KB evidence chain, but it makes startup/status contracts more important.

## Evidence Chain

status:: closed_for_bounded_v1

Source mining, planning, generation, audit, and adoption all used local implementation evidence as the primary layer: repository READMEs, repository metadata snapshots, PyPI captures, ClawHub/plugin pages, `llm-wiki.net`, and clearly bounded adjacent implementation sources. The adopted node describes implementation families, feature surfaces, metadata signals, and limitations. It does not claim real adoption scale, quality, maturity, usage, market rank, downloads, enterprise readiness, or community consensus.

Deferred retrieval was recorded in the source-mining run and did not block v1 because the local corpus was sufficient for descriptive implementation-ecosystem coverage.

## Worker Startup Finding

status:: skill_patch_made

The replacement audit history indicates a practical process failure: an audit worker can stall at an initialized state without durable `task.md`, `loop_status.md`, or `LOOP_BLOCKED` output. Because this prevents the controller from deciding repair/replacement cleanly, it is a high-risk orchestration failure. I patched `llmwiki-loop-orchestration` so workers must create `task.md` and initial `loop_status.md` before long-running work, and must write `LOOP_BLOCKED` with a minimal unblock condition on timeout or no-progress startup.

## Audit Overreach Finding

status:: skill_patch_made_and_recovered

The replacement audit worker self-reported running `kb_parse_citations.py`, mutating `generated/backlinks.yaml` and `generated/citation_graph.yaml` without generated-write authority. This is a hard boundary break for audit workers, although it did not require rejecting the cand_006 bundle because the adoption/view worker later refreshed generated outputs inside its legal write scope and made that refresh authoritative.

I patched `llmwiki-loop-orchestration`, `llmwiki-citation-audit`, and `llmwiki-adoption-audit` to state that audit workers must not run view-building or generated-mutating scripts unless explicitly granted adoption/view authority. Accidental mutation must be disclosed as audit overreach and followed by an adoption/view refresh before generated state is authoritative.

## Footnote Layout Contract

status:: stable

The cand_006 generation, audit, and adoption/view artifacts all show the footnote layout gate passing: `## References` precedes the final `## Footnotes`, and `## Footnotes` is the last top-level section. The contract was present in the generation packet, checked by audit, and verified again during adoption/view for both the selected-version card and KB view.

## Selected-Version Adoption Metadata

status:: stable

The adoption/view worker synchronized root node metadata and selected `versions/1.0/node.yaml` adoption fields. The delivery lists exact selected-version field changes, and target/all node validators passed after view rendering. No metadata repair is needed for cand_006.

## Control-State Caveat

status:: recorded_not_repaired_here

`generated/status.yaml` reports adopted_nodes=7, citation_edges=148, impact_queue_open=0, while `knowledge_frontier.yaml` still contains stale lifecycle fields for some already adopted candidates, including cand_006 showing `status: ready_to_build` / `next_action: generation`. This run's allowed writes did not include `knowledge_frontier.yaml`, so no frontier lifecycle sync was performed here. The next source-mining/frontier worker should treat the adopted KB/status/action queue as authoritative for completed nodes and may include a control-sync note if granted frontier write authority.

