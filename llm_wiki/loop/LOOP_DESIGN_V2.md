# Loop Design V2

`status`: active design

V2 replaces the old single-main-agent draft-first control plane with a
brain-mailbox loop. The goal is higher throughput without losing auditability:
first turn material into scoped draft cards, then do lightweight similarity,
then route only the expensive cases into audit or fusion.

## Main Shift

V1 optimized around `atomic_fact_card`. V2 optimizes around
`scoped_knowledge_card`.

A card may still be small, but it must contain knowledge. For example, "beam
search" is usually not a thing to split mechanically into isolated title facts;
useful cards may instead capture how `N` behaves, why the search is approximate,
or what boundary separates beam search from exhaustive search.

## Control Model

```text
main-agent
-> ops brain / hook
-> brain mailbox
-> lane brain wakes, claims one message, writes artifacts, replies
-> main-agent or ops brain updates state and queues
```

Brain responsibilities:

- `production`: material intake, draft card creation, draft provenance.
- `similarity`: title-token top-3 similarity and comparison provenance.
- `audit`: publication audit, fusion audit, and process audit.
- `ops`: routing, lifecycle hygiene, queue status, wake markers.

The main-agent should stay out of the production loop unless there is a design
or policy problem. It owns charter, skill updates, stop logic, and human
checkpoint decisions.

All cross-brain requests go through mailbox files in `llm_wiki/loop/brains/`.
A brain does not silently write another brain's state; it writes an outbox
message, the hook routes it, and the target brain claims it.

## Production Pipeline

```text
material / exhausted source
-> production brain creates scoped draft card + draft provenance
-> similarity brain runs title similarity top 3
-> similarity brain reads top candidates and writes comparison provenance
-> route by decision
   -> new_card: publication audit
   -> merge_candidate: fusion audit, then fusion adoption
   -> provenance_delta: fusion/provenance audit, then link into A provenance
   -> duplicate_skip: retain comparison provenance, do not publish
   -> revise_before_gate: return to production
-> public adoption updates card, provenance, and index
```

## Similarity Mechanism

Similarity is intentionally lightweight in V2.

For every new draft card:

1. Read the draft title and the accepted-card index.
2. Tokenize titles with Jieba word segmentation.
3. Normalize tokens by trimming whitespace and dropping empty/common tokens.
4. Compute Jaccard set similarity:

```text
jaccard(A, B) = |tokens(A) intersect tokens(B)| / |tokens(A) union tokens(B)|
```

5. Rank by Jaccard score, then by shared-token count as tie-breaker.
6. Return the top 3 accepted cards.
7. Read only those top candidates, then write comparison provenance.

This mechanism is a candidate selector, not a semantic oracle and not a fact
audit. A low score can still be overridden by a clear title synonym, but the
override must be written into the comparison provenance.

## Comparison Provenance

For every draft/A-card comparison that affects routing, write a provenance file
with this shape:

```yaml
draft_card:
existing_card_a:
similarity:
  tokenizer: jieba
  jaccard:
  shared_tokens: []
commonality:
difference:
next_action_basis:
recommended_action:
audit_required:
links_to_write:
```

It must answer three questions:

- Why does the draft have commonality with A?
- How is the draft different from A?
- What is the core basis for the next action?

`merge_candidate` and `provenance_delta` always require audit. Their comparison
provenance must later be linked from A card provenance if the audit passes.

## Card Contract

Cards follow `CARD_CONTRACT_V2.md`.

The fixed metadata block exists for processing. The body remains flexible
because knowledge does not always fit one template. A publication audit should
reject cards that merely restate the title, lack operational content, or hide
the actual knowledge only in provenance.

## Efficiency Claim

V2 should be faster than the earlier flow because:

- material-to-draft work can run in batches without reading the KB;
- similarity is a cheap title-index pass before deeper reading;
- only top-3 candidates are read for comparison;
- new-card publication audit is separated from heavier fusion audit;
- provenance is incremental and linked, rather than repeatedly rewriting old
  cards.

## Guardrails

- Draft backlog is not public KB.
- Similarity output is not fact audit.
- Fusion/provenance-delta decisions must be audited before touching accepted A
  card provenance.
- Duplicate skips still keep comparison provenance.
- Legacy docs are not recovery inputs unless the task explicitly asks for
  historical analysis.
- Main-agent should repair prompts, tools, and state when it repeatedly has to
  do a lane brain's work by hand.
