# KB Initialization Knowledge Mining Protocol

## 0. Why This Document Exists

This document describes **how to build the first version of the KB from raw papers, web pages, and existing data**.

It is not a blueprint of the final KB shape. The final shape has already been defined elsewhere:

- `nodes/` is a flat node database.
- Each node folder contains version bundles.
- A version bundle is `node.yaml + card.md + provenance.md + change.md`.
- `kb/` is the adopted-version consumption view.
- Citations inside cards define directional dependency.
- Generated graphs, backlinks, and impact queues are post-processing artifacts.

This document focuses on the missing part:

> How agents dynamically mine knowledge from raw papers and web pages, create first-version nodes, audit them, adopt them, and use every 0-1 run to improve the skills that created them.

The core assumption is that **knowledge is not statically generated**. It is mined, proposed, tested, adopted, revised, and expanded through loops.

---

## 1. Core Principle

The initialization loop is not:

```text
raw data -> static cards
```

It is:

```text
raw data
-> source mining
-> candidate knowledge frontier
-> 0-1 node build
-> provenance and citation audit
-> adopted KB view
-> skill evaluation
-> next mining decision
```

Knowledge grows through three interacting processes:

1. **Data-driven mining**  
   Raw papers and web pages are read to discover facts, definitions, distinctions, mechanisms, risks, methods, disagreements, and gaps.

2. **Demand-driven extension**  
   The agent loop may discover that a candidate card requires new information, so it triggers dynamic retrieval and turns retrieved information into durable data assets.

3. **Skill-driven iteration**  
   Every 0-1 node build is treated as a test case for the skills used to build it. Failures update skills, not just cards.

---

## 2. What Counts As Success

A successful initialization run does not merely create a card.

It creates a **versioned knowledge object** with:

```text
nodes/<node_id>/
  node.yaml                     # adopted version metadata presentation
  versions/
    1.0/
      node.yaml                 # same schema as root metadata
      card.md                   # content + footnotes + references
      provenance.md             # why/how this version exists
      change.md                 # genesis or version transition rationale
```

For a first version:

```text
versions/1.0/change.md = genesis rationale
```

The version may be adopted only if:

1. `node.yaml` is valid.
2. `card.md` has valid footnotes and references.
3. `provenance.md` explains why the card exists and why it can be trusted.
4. `change.md` explains why version `1.0` was created.
5. Audit passes.
6. The adopted version is rendered into `kb/`.

---

## 3. Agent Hierarchy

The system uses multiple agent layers.

```text
L0 Outer Controller          GPT-5.5
L1 Run Orchestrator          Codex
L2 Specialist Agents         Codex sub-agents
L3 Micro Sub-Agents          optional nested sub-agents
```

### 3.1 L0 Outer Controller

Responsibilities:

- Choose the next loop type.
- Decide whether the current priority is mining, node building, dynamic retrieval, audit, or skill evolution.
- Read `kb/_index.yaml`, generated status files, and recent run artifacts.
- Keep the system focused on initialization rather than final taxonomy construction.

The controller does not normally write cards.

### 3.2 L1 Run Orchestrator

Responsibilities:

- Create `.llmwiki/runs/<run_id>/`.
- Assign tasks to sub-agents.
- Execute scripts.
- Ensure required artifacts are written.
- Build `kb/` views and generated indexes.
- Produce git checkpoints.

### 3.3 L2 Specialist Agents

| Agent | Responsibility |
|---|---|
| Source Profiler | Select and inspect raw papers/webpages. |
| Source Miner | Extract source-backed observations and candidate knowledge. |
| Candidate Curator | Maintain the knowledge frontier. |
| Dynamic Retriever | Search for missing information when current data is insufficient. |
| Node Planner | Choose one candidate for a 0-1 node build. |
| Card Generator | Write `card.md`. |
| Provenance Builder | Write `provenance.md`. |
| Change Writer | Write `change.md`. |
| Metadata Writer | Write `node.yaml`. |
| Citation Auditor | Validate footnotes, references, and pinned versions. |
| Adoption Auditor | Decide whether a version can be adopted. |
| Skill Evaluator | Evaluate skill performance after the run. |
| View Builder | Build `kb/` and generated files. |

### 3.4 L3 Micro Sub-Agents

Examples:

```text
Source Miner
  -> term miner
  -> claim miner
  -> definition miner
  -> disagreement miner
  -> gap miner

Provenance Builder
  -> input trace writer
  -> synthesis rationale writer
  -> audit trail writer
  -> revision trigger writer

Citation Auditor
  -> footnote parser
  -> reference parser
  -> pinned version checker
  -> why-cited checker
```

---

## 4. Core Runtime Files

### 4.1 Source Mining Artifacts

Each mining run writes:

```text
.llmwiki/runs/<run_id>/
  source_scope.md
  source_mining.md
  candidate_frontier_delta.yaml
  evidence_gaps.md
  retrieval_requests.md
  mining_trace.md
```

These artifacts are not final KB nodes. They are the evidence of how raw data was mined.

### 4.2 Candidate Knowledge Frontier

The system keeps a frontier file:

```text
.llmwiki/control/knowledge_frontier.yaml
```

This file tracks candidate nodes discovered from sources.

Example:

```yaml
schema: kb.knowledge_frontier.v1
updated_at: "2026-05-22T00:00:00-07:00"

candidates:
  - candidate_id: cand_001
    proposed_node_id: 20260522_143012_source_preservation_precondition_trust
    status: ready_to_build
    discovered_from:
      - src_000001
      - src_000002
    candidate_statement: "Source preservation is a precondition for trustworthy LLM Wiki synthesis."
    why_it_matters: "This idea supports later cards about provenance, auditability, and agent reuse."
    evidence_state: enough_for_first_version
    missing_evidence: []
    suggested_first_version: "1.0"

  - candidate_id: cand_002
    proposed_node_id: 20260522_160000_llm_wiki_beats_raw_rag
    status: needs_retrieval
    discovered_from:
      - src_000003
    candidate_statement: "LLM Wiki improves repeated research tasks over raw RAG."
    why_it_matters: "This would support empirical judgment."
    evidence_state: insufficient
    missing_evidence:
      - "benchmark or case study against raw RAG baseline"
```

Candidate statuses:

```text
discovered
needs_more_mining
ready_to_build
needs_retrieval
built
rejected
deferred
```

---

## 5. Source Mining Loop

Purpose:

> Convert raw papers and web pages into candidate knowledge, not immediately into cards.

### 5.1 Inputs

```text
data/raw/
data/manifests/sources.jsonl
existing kb/_index.yaml
existing nodes/
```

### 5.2 Source Selection

The Source Profiler chooses a source or source batch.

Selection criteria:

```text
1. Source relevance to LLM Wiki framework.
2. Source freshness or canonical value.
3. Source diversity.
4. Whether the source can support first-version nodes.
5. Whether the source fills a known gap.
6. Whether the source tests an important skill.
```

### 5.3 Source Reading Passes

The Source Miner does several passes.

These are **mining lenses**, not rigid knowledge categories.

#### Pass A: Source Structure

For papers:

```text
title
abstract
introduction
method
results
discussion
related work
limitations
appendix
```

For web pages:

```text
title
author/org
date
main claim
context
docs/examples
comments/discussion
links
limitations
```

Output:

```text
source_scope.md
```

#### Pass B: Source-Backed Observations

Extract statements that can be traced to the source.

Examples:

```text
Source X defines Y as Z.
Source X claims Y.
Repo X implements feature Y.
Paper X evaluates method Y against baseline Z.
Thread X contains disagreement about Y.
```

Output:

```text
source_mining.md
```

#### Pass C: Candidate Knowledge

Mine possible nodes:

```text
working definitions
source observations
process ideas
risks
mechanisms
comparisons
methods
evidence gaps
hub seeds
```

Do not force a taxonomy. These are only candidate shapes.

Output:

```text
candidate_frontier_delta.yaml
```

#### Pass D: Citation Feasibility

For each candidate, determine:

```text
Can the candidate be supported by current sources?
Which raw source paths support it?
Would it need a footnote or reference?
Is the evidence direct, indirect, weak, or missing?
```

Output:

```text
source_mining.md
candidate_frontier_delta.yaml
```

#### Pass E: Gap Detection

If evidence is insufficient, write:

```text
evidence_gaps.md
retrieval_requests.md
```

---

## 6. Dynamic Retrieval Loop

Dynamic retrieval is allowed, but it must become part of the data layer.

It is not allowed to search, use the answer, and disappear.

### 6.1 Triggers

Dynamic retrieval may be triggered when:

```text
1. A candidate is important but current data is insufficient.
2. Audit rejects a citation.
3. A working definition lacks source diversity.
4. A claim requires empirical support.
5. A source gap blocks a first-version node.
```

### 6.2 Retrieval Request

```markdown
# Retrieval Request

run_id:: run_...
target_candidate:: cand_...
status:: open
created_by:: source_miner | generator | auditor

## Why current data is insufficient

...

## Missing evidence

...

## Desired source types

- paper
- repo
- docs
- benchmark
- case study
- thread
- governance document

## Suggested queries

...

## Acceptance criteria

- Raw source must be preserved under `data/raw/`.
- Source manifest must be updated.
- Source must be mined before being used in a card.
- Provenance must record dynamic retrieval.
```

### 6.3 Retrieval Output

```text
data/raw/<source_id>/
data/manifests/sources.jsonl
.llmwiki/runs/<run_id>/retrieval_log.md
.llmwiki/runs/<run_id>/source_mining.md
```

After retrieval, return to Source Mining Loop.

---

## 7. 0-1 Node Build Loop

Purpose:

> Turn one ready candidate into a first-version node.

Each run builds one new node from zero to adopted version `1.0`, unless audit blocks it.

This is intentional. During initialization, every 0-1 node is also a skill evaluation sample.

### 7.1 Inputs

```text
knowledge_frontier.yaml
candidate_frontier_delta.yaml
source_mining.md
data/raw/
data/manifests/
existing kb/_index.yaml
existing nodes/
```

### 7.2 Candidate Selection

Node Planner selects a candidate using:

```text
1. Evidence readiness.
2. Usefulness for current KB initialization.
3. Whether it unlocks future nodes.
4. Whether it tests an important skill.
5. Whether it can be built without overclaiming.
6. Whether dynamic retrieval has resolved blocking gaps.
```

### 7.3 Create Node ID

Node ID format:

```text
YYYYMMDD_HHMMSS_semantic_slug
```

Example:

```text
20260522_143012_source_preservation_precondition_trust
```

Rules:

```text
1. No `zk_` prefix.
2. No category prefix.
3. No level.
4. Timestamp + semantic slug only.
5. The ID remains stable even if the title later changes.
```

### 7.4 Write Version Bundle

Create:

```text
nodes/<node_id>/versions/1.0/node.yaml
nodes/<node_id>/versions/1.0/card.md
nodes/<node_id>/versions/1.0/provenance.md
nodes/<node_id>/versions/1.0/change.md
```

Then, if adopted:

```text
nodes/<node_id>/node.yaml
kb/<node_id>.md
kb/_index.yaml
```

---

## 8. Card Build Rules

`card.md` is not a rigid template.

It may be a definition, observation, comparison, hub-like aggregation, method note, process note, or demand-oriented explanation.

However, it must satisfy a Markdown schema.

### 8.1 Required Sections

```text
# Title

free body

## Footnotes

## References
```

Tags may live only in `node.yaml`. The renderer may optionally show them in `kb/`.

### 8.2 Footnotes

Footnotes support specific body claims.

Example:

```markdown
Source preservation is necessary for later audit because future agents need access to the material behind synthesized claims.[^1]

## Footnotes

[^1]:
    target: ../../kb/20260522_150012_karpathy_llm_wiki_source_observation.md
    target_version: 1.0
    pinned_version: ../../nodes/20260522_150012_karpathy_llm_wiki_source_observation/versions/1.0/card.md
    citation_role: claim_support
    why_cited: Supports the claim that preserved source material is required for audit and reuse.
    evidence_summary: The cited card records a source-backed observation from preserved raw material.
```

Required footnote fields:

```text
target
target_version
pinned_version
citation_role
why_cited
evidence_summary
```

### 8.3 References

References support broader context, background definitions, or page-level ideas.

Example:

```markdown
## References

### [R1] Working definition of LLM Wiki

target: ../../kb/20260522_151044_llm_wiki_working_definition.md
target_version: 1.0
pinned_version: ../../nodes/20260522_151044_llm_wiki_working_definition/versions/1.0/card.md
citation_role: background_definition
why_cited: This card uses the KB working definition of LLM Wiki as background.
evidence_summary: The cited card explains the current operational definition and its boundaries.
```

Required reference fields:

```text
target
target_version
pinned_version
citation_role
why_cited
evidence_summary
```

### 8.4 Citation Direction

Citation is the dependency direction.

```text
A cites B
=> A depends on B
=> B major update triggers impact review for A
```

No separate `supports` / `depends_on` graph is maintained.

---

## 9. Provenance Build Rules

`provenance.md` is a first-class artifact.

It may be more important than `card.md` because it explains why the card can be trusted or adopted.

Required sections:

```markdown
# Provenance

node_id:: ...
version:: 1.0

## Why this version exists

## Inputs used

### Existing data

### Dynamic retrieval, if any

### Prior KB nodes

### Process artifacts

## Production rationale

## Citation rationale

## Synthesis decisions

## Audit trail

## Adoption rationale

## Limits and uncertainty

## Revision triggers
```

The provenance must explicitly distinguish:

```text
source-backed observation
current project fact
working definition
interpretation
synthesis
hypothesis
evidence gap
process rationale
```

The provenance must not claim that synthesis is ground truth.

---

## 10. Change Build Rules

For first version:

```text
versions/1.0/change.md = genesis change
```

Required structure:

```markdown
# Change: genesis → 1.0

node_id:: ...
from_version:: genesis
to_version:: 1.0
change_scale:: major
propagation_required:: false
created_at:: ...
run_id:: ...

## Why this node was created

## Why this first version is acceptable

## Evidence basis

## Known limits

## Expected future changes
```

For later major versions:

```markdown
# Change: 1.1 → 2.0

## Why this changed

## Old meaning

## New meaning

## Semantic delta

## Why this is major

## Expected impact
```

Major change files feed impact analysis.

---

## 11. Audit And Adoption Loop

### 11.1 Audit Inputs

```text
versions/<version>/node.yaml
versions/<version>/card.md
versions/<version>/provenance.md
versions/<version>/change.md
source_mining.md
retrieval_log.md, if any
```

### 11.2 Audit Checks

Schema checks:

```text
1. All four version bundle files exist.
2. node.yaml is valid.
3. card.md has Footnotes and References sections.
4. provenance.md has required provenance sections.
5. change.md has required change sections.
```

Citation checks:

```text
1. Every footnote has required fields.
2. Every reference has required fields.
3. target path exists.
4. pinned_version path exists.
5. why_cited is specific.
6. evidence_summary is relevant.
7. cited target can support the claim or background role.
```

Provenance checks:

```text
1. Existing data and dynamic retrieval are separated.
2. Synthesis decisions are explicit.
3. Uncertainty is not hidden.
4. Adoption rationale is clear.
5. Revision triggers exist.
```

Epistemic checks:

```text
1. Card does not present synthesis as ground truth.
2. Current project facts are scoped.
3. Working definitions are not universalized.
4. Evidence gaps are not hidden.
```

### 11.3 Adoption Rules

For version `1.0`:

```text
If audit passes, adopt.
```

For minor version:

```text
If audit passes, adopt.
```

For major version:

```text
Do not adopt until impact analysis and required downstream review are complete.
```

---

## 12. Impact Loop

Impact analysis runs when a major version candidate is created.

### 12.1 Inputs

```text
major version change.md
kb/_index.yaml
parsed citation graph from adopted kb cards
```

### 12.2 Process

```text
1. Parse major change.
2. Parse footnotes and references in adopted KB.
3. Find cards citing the changed node/version.
4. Classify impact:
   - footnote = high
   - reference = medium
   - plain link = low / ignored by default
5. Generate impact queue.
```

### 12.3 Output

```text
generated/impact_queue.yaml
```

Impact analysis does not automatically rewrite downstream nodes.

---

## 13. Skill Evolution Loop

Every 0-1 node build is also a skill evaluation sample.

### 13.1 Skill Evaluation Inputs

```text
run artifacts
version bundle
audit report
failure modes
retrieval usage
adoption result
```

### 13.2 Skills Being Evaluated

```text
source_mining
candidate_frontier_management
node_planning
card_generation
citation_formatting
provenance_generation
change_generation
citation_audit
adoption_audit
dynamic_retrieval
view_building
impact_analysis
```

### 13.3 Skill Eval Output

```text
.llmwiki/runs/<run_id>/skill_eval.md
.llmwiki/control/skill_eval_log.yaml
```

Skill eval does not ask “is this better?” in the abstract.

It asks:

```text
Which failure mode appeared?
Which skill caused or failed to prevent it?
Does this require a local case note or a general skill patch?
```

### 13.4 Skill Patch Rule

Patch a skill only if:

```text
1. The failure is repeated.
2. The failure is high-risk.
3. The failure breaks a hard contract.
4. The patch is specific and testable.
```

Do not patch global skills for one low-risk local observation.

---

## 14. Initialization Loop Structure

The full initialization process is a nested loop.

```text
System Bootstrap Loop
  -> Data Inventory Loop
    -> Source Mining Loop
      -> Candidate Frontier Loop
        -> 0-1 Node Build Loop
          -> Audit and Adoption Loop
            -> View Build Loop
              -> Skill Evolution Loop
                -> Next Source / Candidate / Retrieval Decision
```

Dynamic retrieval can interrupt the Source Mining or Node Build loop:

```text
evidence insufficient
  -> retrieval request
    -> web search
      -> raw source preservation
        -> source mining
          -> candidate update
            -> node build resumes
```

Major changes trigger impact loop:

```text
major candidate
  -> impact analysis
    -> impact queue
      -> downstream review runs
        -> adoption decision
```

---

## 15. First Demo Execution Plan

### Phase 1: Bootstrap Contracts

Create:

```text
kb/_schema.yaml
.llmwiki/control/principles.md
.llmwiki/control/state.md
scripts/kb_build_index.py
scripts/kb_build_view.py
scripts/kb_parse_citations.py
scripts/kb_status.py
skill seeds
```

### Phase 2: Inventory Existing Data

Create:

```text
.llmwiki/control/data_inventory.yaml
.llmwiki/control/source_candidates.yaml
```

### Phase 3: Mine First Source Batch

Create:

```text
source_scope.md
source_mining.md
candidate_frontier_delta.yaml
knowledge_frontier.yaml
```

### Phase 4: Build First Node 0-1

Create one first-version node:

```text
nodes/<node_id>/versions/1.0/node.yaml
nodes/<node_id>/versions/1.0/card.md
nodes/<node_id>/versions/1.0/provenance.md
nodes/<node_id>/versions/1.0/change.md
nodes/<node_id>/node.yaml
kb/<node_id>.md
```

### Phase 5: Repeat 0-1 Builds

Build 3-5 more nodes from different source/candidate types.

### Phase 6: Dynamic Retrieval Test

Force or encounter one evidence gap.

Run retrieval and preserve the new source.

### Phase 7: Impact Test

Create or simulate one major candidate version.

Generate impact queue.

### Phase 8: Skill Eval Report

Produce:

```text
.llmwiki/control/skill_eval_log.yaml
reports/kb_initialization_demo_report.md
```

---

## 16. Demo Acceptance Criteria

The initialization demo is successful if:

```text
1. At least 5 adopted nodes exist.
2. Every adopted node has a complete version bundle.
3. Every adopted node has provenance.md.
4. Every adopted card has Footnotes and References sections.
5. kb/_index.yaml can be generated.
6. generated/citation_graph.yaml can be generated.
7. At least one dynamic retrieval case is recorded and preserved.
8. At least one evidence gap is recorded.
9. At least one skill_eval.md exists.
10. At least one major candidate or simulated major change creates impact_queue.yaml.
```

---

## 17. Operating Principle

The KB initialization loop is not a static card factory.

It is a dynamic knowledge mining system:

```text
raw papers/webpages
-> mined observations
-> candidate knowledge frontier
-> 0-1 node build
-> provenance and citation audit
-> adopted KB view
-> skill evaluation
-> next mining decision
```

The output of each run is not just a card.

The output is:

```text
knowledge
+ provenance
+ citation direction
+ adoption decision
+ skill feedback
+ next frontier state
```

That is what makes the KB grow.
