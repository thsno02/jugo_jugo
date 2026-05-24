# Goal Satisfaction Audit

Generated: 2026-05-21

## Current Status

The prior completion judgment was too weak. It treated "the control loop exists and a local audit ran" as equivalent to "the research loop has satisfied the coverage objective." That is not the intended task.

The active stop condition is now:

```text
python3 scripts/run_loop.py satisfaction
```

The loop is satisfied only when that command returns `SATISFACTION PASS`.

## Corrected Task Definition

The task is to repeatedly use the coverage framework to:

```text
select gap -> plan discovery -> discover sources -> triage candidates -> acquire raw material -> extract readable content -> digest sources -> extract claims -> map claims to coverage -> update reports -> audit -> update state -> repeat
```

The loop may not stop after one local pass unless all gates and queues satisfy the stop condition.

## Corrected Stop Condition

The result is satisfied only when:

- `research_paper` gate is passed.
- `descriptive`, `technical`, `empirical`, and `strategic` gates are passed.
- Every coverage area has latest audit status `pass`.
- Every required output is `supported`, not `weak`, `partial`, `missing`, or `blocked`.
- All active discovery, triage, acquisition, digest, claim, and audit queues are empty.
- Every inaccessible desired source is recorded in `data/logs/inaccessible_sources.xml`.
- Blocked sources are not counted as evidence.

## Current Evidence

Current state is not satisfied. The loop still has open search tasks and non-passing empirical/strategic/research-paper gates. The next work should continue gap-driven source discovery and acquisition, starting with `evaluation_and_evidence`, `comparison_space`, and `risks_governance_ethics`.
