Use your current tree as a **research-control repo**. The Markdown framework should remain mostly static; the loop should enforce it through machine-readable state, manifests, logs, and audit gates.

The core design is:

```text
reports/coverage_framework.md      = static objective / specification
loop_manifest.json                 = compiled acceptance tests from the objective
loop_state.json                    = mutable runtime state
data/discovery/*                   = search plans, candidates, triage queues
data/raw/*                         = preserved source material
data/manifests/*                   = source, claim, digest, and coverage records
data/logs/*                        = event log, failures, audits
reports/*                          = human-readable status and synthesis outputs
scripts/*                          = deterministic utilities agents call
```

Your framework already says each item should eventually be backed by raw sources in `data/raw/`, a source manifest row in `data/manifests/sources.jsonl`, and a claim-to-source note. It also defines the required coverage areas, evidence matrix, and judgment levels, so the loop should convert those into enforceable gates rather than treating the Markdown as a passive checklist. 

---

# 1. The Main Principle

The agent loop should not optimize for “doing research.” It should optimize for **making framework requirements pass objective tests**.

A coverage area is not “done” when the agent writes a nice paragraph.

It is done only when:

```text
raw source exists
+ manifest record exists
+ source digest exists
+ claim records exist
+ claims are mapped to coverage requirements
+ report/wiki section is updated
+ audit passes
+ judgment gate criteria are satisfied
```

That is how the static Markdown objective becomes operationally true.

---

# 2. Keep Your Current Folder Structure

Your current tree is good enough. I would not add a large new structure yet. I would only add a few missing JSONL files inside the folders you already have.

## Current folder roles

| Path                               | Role in the loop                                                                                             |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| `reports/coverage_framework.md`    | Static objective document. Do not treat this as mutable state.                                               |
| `docs/RESEARCH_PROTOCOL.md`        | Human-readable operating procedure for agents.                                                               |
| `loop_manifest.json`               | Machine-readable version of the objective. Contains coverage areas, required outputs, gates, and invariants. |
| `loop_state.json`                  | Runtime progress state. Contains current target, open gaps, gate status, and next actions.                   |
| `data/discovery/`                  | Search plans, candidate URLs, triage decisions, blocked-source notes.                                        |
| `data/raw/`                        | Preserved raw sources: HTML, PDFs, repos, screenshots, text dumps, metadata.                                 |
| `data/manifests/`                  | Source records, claim records, digest records, source-to-claim mappings.                                     |
| `data/logs/`                       | Loop events, fetch failures, audit failures, model/tool actions.                                             |
| `reports/acquisition_status.md`    | Human-readable source acquisition report.                                                                    |
| `reports/initial_gap_checklist.md` | Bootstrap gap report generated from the framework.                                                           |
| `reports/source_gap_review.md`     | Recurring report showing what evidence is still missing.                                                     |
| `scripts/fetch_sources.py`         | Acquisition utility. Should fetch/preserve sources, not synthesize conclusions.                              |

## Add these files

```text
data/discovery/search_tasks.jsonl
data/discovery/candidate_sources.jsonl
data/discovery/triage_decisions.jsonl

data/manifests/sources.jsonl
data/manifests/source_digests.jsonl
data/manifests/claims.jsonl
data/manifests/claim_source_links.jsonl
data/manifests/coverage_records.jsonl

data/logs/loop_events.jsonl
data/logs/acquisition_failures.jsonl
data/logs/audit_events.jsonl

reports/coverage_status.md
reports/evidence_matrix.md
reports/judgment_status.md
```

The important point: **the agent should never rely on memory to know what has been collected**. It should read the manifests and state files every loop.

---

# 2A. Active Task And Stop Condition

The active task is not merely to create loop-control files or run one local audit. The task is:

```text
Continuously use the coverage framework to find missing evidence, discover candidate sources, acquire raw materials, digest them, extract claims, map claims to coverage requirements, audit the result, and repeat until the coverage framework is actually satisfied.
```

In this repo, "SATISFY THE RESULTS" means all of the following are true:

```text
1. The research_paper judgment gate is passed.
2. All prerequisite gates are passed: descriptive, technical, empirical, and strategic.
3. Every coverage area has latest audit_status=pass.
4. Every required output has status=supported from output-specific, source-backed claims.
5. No required output is merely weak, partial, missing, or blocked.
6. All open discovery/acquisition/digest/claim/audit queues are empty.
7. Any desired source that could not be accessed is recorded in data/logs/inaccessible_sources.xml with reason and retry path.
8. Blocked sources do not substitute for evidence; they only explain why a source was not acquired. If a blocked source matters to a required output, the loop must find replacement evidence or keep the gate not_ready.
```

The command `python scripts/run_loop.py verify` is a structural health check only. It must not be used as the stop condition. The stop condition is `python scripts/run_loop.py satisfaction` returning `SATISFACTION PASS`.

The command `once` means one bounded iteration. It must not imply completion unless the subsequent `satisfaction` check passes.

---

# 3. Make `loop_manifest.json` The Compiled Objective

The Markdown framework is for humans. The loop needs a strict manifest.

Recommended structure:

```json
{
  "objective_name": "LLM Wiki Coverage Framework",
  "objective_doc": "reports/coverage_framework.md",
  "objective_version": "2026-05-21",
  "objective_hash": "sha256:TO_BE_FILLED",
  "default_loop_policy": {
    "source_first": true,
    "raw_preservation_required": true,
    "claim_source_mapping_required": true,
    "audit_required_before_completion": true,
    "unsupported_claim_policy": "downgrade_to_hypothesis_or_remove"
  },
  "coverage_areas": [
    {
      "id": "origin_and_canon",
      "title": "Origin And Canon",
      "framework_section": "Facts That Must Be Covered > Origin And Canon",
      "judgment_gate": "descriptive",
      "required_outputs": [
        "original_karpathy_statement_exact_text",
        "original_date",
        "original_context",
        "examples_and_intended_workflow",
        "stated_or_implied_non_goals",
        "immediate_discussion_context",
        "early_forks_or_implementations",
        "minimal_example"
      ],
      "minimum_evidence": {
        "primary_sources": 1,
        "discussion_sources": 1,
        "implementation_sources": 1,
        "source_diversity": 3
      },
      "preferred_source_types": [
        "primary_post",
        "gist",
        "x_mirror",
        "hacker_news_thread",
        "reddit_thread",
        "github_repo",
        "blog_post"
      ],
      "acceptance_tests": [
        "exact_origin_claim_has_primary_or_near_primary_source",
        "date_and_context_are_recorded",
        "early_discussion_is_preserved_or_blocked_with_reason",
        "minimal_example_is_described_from_sources",
        "audit_passed"
      ]
    },
    {
      "id": "problem_and_motivation",
      "title": "Problem And Motivation",
      "framework_section": "Facts That Must Be Covered > Problem And Motivation",
      "judgment_gate": "descriptive",
      "required_outputs": [
        "workflow_failures_addressed",
        "user_groups",
        "definition_of_better",
        "current_alternatives"
      ],
      "minimum_evidence": {
        "user_reports_or_discussions": 3,
        "implementation_sources": 3,
        "source_diversity": 4
      },
      "preferred_source_types": [
        "discussion_thread",
        "blog_post",
        "repo_readme",
        "case_study",
        "issue_thread"
      ],
      "acceptance_tests": [
        "each_motivation_has_at_least_one_source",
        "user_groups_are_not_invented",
        "benefit_claims_are_marked_as_observed_or_hypothetical",
        "audit_passed"
      ]
    },
    {
      "id": "architecture_and_data_model",
      "title": "Architecture And Data Model",
      "framework_section": "Facts That Must Be Covered > Architecture And Data Model",
      "judgment_gate": "technical",
      "required_outputs": [
        "source_acquisition_model",
        "compilation_model",
        "storage_model",
        "link_model",
        "update_model",
        "query_model"
      ],
      "minimum_evidence": {
        "implementation_sources": 10,
        "code_or_docs_sources": 5,
        "source_diversity": 5
      },
      "preferred_source_types": [
        "github_repo",
        "readme",
        "documentation",
        "demo",
        "code"
      ],
      "acceptance_tests": [
        "at_least_ten_implementations_classified",
        "each_architecture_dimension_has_evidence",
        "source_preservation_and_query_models_are_distinguished",
        "audit_passed"
      ]
    },
    {
      "id": "workflow_and_operations",
      "title": "Workflow And Operations",
      "framework_section": "Facts That Must Be Covered > Workflow And Operations",
      "judgment_gate": "technical",
      "required_outputs": [
        "end_to_end_lifecycle",
        "human_in_loop_boundaries",
        "agent_interfaces",
        "failure_handling"
      ],
      "minimum_evidence": {
        "workflow_examples": 5,
        "failure_examples": 3,
        "source_diversity": 4
      },
      "preferred_source_types": [
        "repo",
        "docs",
        "issue_thread",
        "blog_post",
        "demo"
      ],
      "acceptance_tests": [
        "agent_permissions_are_described",
        "failure_handling_is_not_purely_speculative",
        "blocked_sources_are_logged",
        "audit_passed"
      ]
    },
    {
      "id": "evaluation_and_evidence",
      "title": "Evaluation And Evidence",
      "framework_section": "Facts That Must Be Covered > Evaluation And Evidence",
      "judgment_gate": "empirical",
      "required_outputs": [
        "answer_quality_metrics",
        "maintenance_quality_metrics",
        "agent_usability_metrics",
        "robustness_metrics",
        "benchmark_or_case_study_inventory"
      ],
      "minimum_evidence": {
        "benchmark_or_eval_sources": 3,
        "case_studies": 2,
        "baseline_comparisons": 3
      },
      "preferred_source_types": [
        "paper",
        "benchmark",
        "case_study",
        "issue_thread",
        "evaluation_report"
      ],
      "acceptance_tests": [
        "raw_rag_baseline_is_defined",
        "chat_memory_baseline_is_defined",
        "no_empirical_claim_without_method",
        "audit_passed"
      ]
    },
    {
      "id": "ecosystem_and_implementations",
      "title": "Ecosystem And Implementations",
      "framework_section": "Facts That Must Be Covered > Ecosystem And Implementations",
      "judgment_gate": "technical",
      "required_outputs": [
        "tool_family_inventory",
        "implementation_taxonomy",
        "adoption_signals",
        "interoperability_notes"
      ],
      "minimum_evidence": {
        "implementation_sources": 15,
        "tool_families": 5,
        "adoption_signal_sources": 5
      },
      "preferred_source_types": [
        "github_repo",
        "plugin_listing",
        "package_registry",
        "docs",
        "community_post"
      ],
      "acceptance_tests": [
        "implementations_are_not_all_same_family",
        "adoption_signals_are_separated_from_quality_claims",
        "repo_metadata_is_recorded",
        "audit_passed"
      ]
    },
    {
      "id": "comparison_space",
      "title": "Comparison Space",
      "framework_section": "Facts That Must Be Covered > Comparison Space",
      "judgment_gate": "strategic",
      "required_outputs": [
        "rag_comparison",
        "pkm_comparison",
        "knowledge_graph_comparison",
        "agent_memory_comparison",
        "documentation_systems_comparison"
      ],
      "minimum_evidence": {
        "comparison_sources": 10,
        "adjacent_system_categories": 5,
        "source_diversity": 5
      },
      "preferred_source_types": [
        "paper",
        "docs",
        "blog_post",
        "tool_docs",
        "benchmark"
      ],
      "acceptance_tests": [
        "each_adjacent_system_has_advantages_and_limitations",
        "claims_about_difference_are_source_backed",
        "simpler_alternatives_are_not dismissed_without_evidence",
        "audit_passed"
      ]
    },
    {
      "id": "risks_governance_ethics",
      "title": "Risks Governance And Ethics",
      "framework_section": "Facts That Must Be Covered > Risks, Governance, And Ethics",
      "judgment_gate": "strategic",
      "required_outputs": [
        "provenance_risk",
        "maintenance_risk",
        "privacy_security_risk",
        "governance_model",
        "epistemic_risk"
      ],
      "minimum_evidence": {
        "risk_sources": 5,
        "failure_or_issue_sources": 3,
        "governance_sources": 3
      },
      "preferred_source_types": [
        "issue_thread",
        "security_note",
        "governance_doc",
        "paper",
        "case_study"
      ],
      "acceptance_tests": [
        "risk_claims_are_tied_to_failure_or_threat_model",
        "privacy_and_license_risks_are_separated",
        "governance_requirements_are_actionable",
        "audit_passed"
      ]
    }
  ],
  "judgment_gates": {
    "descriptive": {
      "required_coverage_areas": [
        "origin_and_canon",
        "problem_and_motivation"
      ],
      "minimum_status": "audited"
    },
    "technical": {
      "required_coverage_areas": [
        "architecture_and_data_model",
        "workflow_and_operations",
        "ecosystem_and_implementations"
      ],
      "minimum_status": "audited"
    },
    "empirical": {
      "required_coverage_areas": [
        "evaluation_and_evidence"
      ],
      "minimum_status": "audited"
    },
    "strategic": {
      "required_coverage_areas": [
        "comparison_space",
        "risks_governance_ethics"
      ],
      "minimum_status": "audited"
    },
    "research_paper": {
      "required_gates": [
        "descriptive",
        "technical",
        "empirical",
        "strategic"
      ],
      "minimum_status": "passed"
    }
  },
  "global_invariants": [
    "no_claim_without_source_id",
    "no_source_without_manifest_record",
    "no_source_counted_without_raw_path_or_logged_failure",
    "no_coverage_area_completed_without_audit",
    "no_empirical_claim_without_baseline_or_method",
    "no_strategic_judgment_without_cost_risk_and_comparison",
    "contradictions_must_be_preserved",
    "blocked_sources_must_be_logged"
  ]
}
```

This file is the agent’s contract.

---

# 4. Make `loop_state.json` The Runtime State

`loop_manifest.json` should say **what must be true**.

`loop_state.json` should say **what is currently true**.

Recommended shape:

```json
{
  "run_id": "run_2026_05_21_001",
  "objective_doc": "reports/coverage_framework.md",
  "objective_hash": "sha256:TO_BE_FILLED",
  "last_updated": "2026-05-21T00:00:00-07:00",
  "current_phase": "select_gap",
  "current_target": null,
  "coverage_state": {
    "origin_and_canon": {
      "status": "partial",
      "evidence_count": 0,
      "source_count": 0,
      "claim_count": 0,
      "digest_count": 0,
      "audit_status": "not_run",
      "missing_outputs": [
        "original_karpathy_statement_exact_text",
        "original_date",
        "early_forks_or_implementations",
        "minimal_example"
      ],
      "next_action": "search_for_primary_origin_sources"
    },
    "evaluation_and_evidence": {
      "status": "weak",
      "evidence_count": 0,
      "source_count": 0,
      "claim_count": 0,
      "digest_count": 0,
      "audit_status": "not_run",
      "missing_outputs": [
        "answer_quality_metrics",
        "maintenance_quality_metrics",
        "benchmark_or_case_study_inventory"
      ],
      "next_action": "collect_benchmark_and_case_study_sources"
    }
  },
  "gate_state": {
    "descriptive": {
      "status": "not_ready",
      "blocking_coverage_areas": [
        "origin_and_canon",
        "problem_and_motivation"
      ]
    },
    "technical": {
      "status": "not_ready",
      "blocking_coverage_areas": [
        "architecture_and_data_model",
        "workflow_and_operations",
        "ecosystem_and_implementations"
      ]
    },
    "empirical": {
      "status": "not_ready",
      "blocking_coverage_areas": [
        "evaluation_and_evidence"
      ]
    },
    "strategic": {
      "status": "not_ready",
      "blocking_coverage_areas": [
        "comparison_space",
        "risks_governance_ethics"
      ]
    },
    "research_paper": {
      "status": "not_ready",
      "blocking_gates": [
        "descriptive",
        "technical",
        "empirical",
        "strategic"
      ]
    }
  },
  "queues": {
    "search_tasks_open": 0,
    "candidate_sources_pending_triage": 0,
    "sources_pending_acquisition": 0,
    "sources_pending_digest": 0,
    "digests_pending_claim_extraction": 0,
    "claims_pending_audit": 0
  },
  "last_completed_loop": null,
  "next_recommended_action": "bootstrap_or_refresh_coverage_state"
}
```

Important: do **not** put everything in `loop_state.json`. It should hold status and pointers, not detailed evidence. Detailed evidence belongs in JSONL manifests.

---

# 5. The Agent Loop State Machine

Use this state machine:

```text
BOOTSTRAP_OBJECTIVE
→ SELECT_GAP
→ PLAN_DISCOVERY
→ DISCOVER_SOURCES
→ TRIAGE_CANDIDATES
→ ACQUIRE_RAW_SOURCES
→ EXTRACT_READABLE_CONTENT
→ DIGEST_SOURCES
→ EXTRACT_CLAIMS
→ MAP_CLAIMS_TO_OBJECTIVE
→ UPDATE_REPORTS
→ AUDIT
→ UPDATE_LOOP_STATE
→ SELECT_GAP
```

The loop repeats until the relevant judgment gates pass.

---

# 6. Step-By-Step Loop Design

## Step 0: Bootstrap Objective

Purpose:

```text
Convert reports/coverage_framework.md into loop_manifest.json and initial loop_state.json.
```

Reads:

```text
reports/coverage_framework.md
docs/RESEARCH_PROTOCOL.md
```

Writes:

```text
loop_manifest.json
loop_state.json
reports/initial_gap_checklist.md
data/logs/loop_events.jsonl
```

Agent instruction:

```text
Read the static framework.
Extract every coverage area, required output, evidence requirement, and judgment gate.
Create or refresh loop_manifest.json.
Initialize loop_state.json if missing.
Do not collect web sources yet.
Do not synthesize conclusions yet.
```

Completion test:

```text
Every major framework section has a coverage_area id.
Every coverage_area has required_outputs.
Every coverage_area has minimum_evidence.
Every judgment gate has pass conditions.
```

---

## Step 1: Select Highest-Priority Gap

Purpose:

```text
Choose the next coverage area that most improves the objective.
```

Reads:

```text
loop_manifest.json
loop_state.json
data/manifests/sources.jsonl
data/manifests/claims.jsonl
data/manifests/source_digests.jsonl
reports/source_gap_review.md
```

Writes:

```text
loop_state.json
data/logs/loop_events.jsonl
```

Priority formula:

```text
priority_score =
  50 * judgment_gate_importance
+ 20 * missing_required_output_count
+ 15 * evidence_shortfall
+ 15 * source_diversity_shortfall
+ 10 * no_primary_source_penalty
+ 10 * audit_failure_penalty
+ 10 * stale_or_blocked_penalty
+  5 * contradiction_unresolved_penalty
```

Recommended first targets based on your framework’s own matrix:

```text
1. evaluation_and_evidence
2. risks_governance_ethics
3. comparison_space
4. origin_and_canon, if exact primary origin evidence is still missing
5. architecture_and_data_model, if implementation evidence has not been fully digested
```

Your framework already marks evaluation, risks, and comparisons as weak or mostly missing, while some origin, HN, and implementation acquisition has apparently begun. That makes those areas natural high-priority targets for the next loops. 

---

## Step 2: Plan Discovery

Purpose:

```text
Turn one gap into specific web search tasks.
```

Reads:

```text
loop_manifest.json
loop_state.json
data/manifests/sources.jsonl
```

Writes:

```text
data/discovery/search_tasks.jsonl
```

Example record:

```json
{
  "search_task_id": "search_000001",
  "created_at": "2026-05-21T00:00:00-07:00",
  "coverage_id": "evaluation_and_evidence",
  "missing_outputs": [
    "answer_quality_metrics",
    "maintenance_quality_metrics",
    "benchmark_or_case_study_inventory"
  ],
  "queries": [
    "\"LLM wiki\" benchmark",
    "\"agent memory\" \"RAG\" benchmark",
    "\"source-backed\" \"agent memory\" evaluation",
    "\"citation fidelity\" \"RAG\" benchmark",
    "\"knowledge base\" \"LLM agents\" \"case study\""
  ],
  "target_source_types": [
    "paper",
    "benchmark",
    "case_study",
    "evaluation_report",
    "issue_thread"
  ],
  "success_criteria": [
    "Find sources with explicit baselines",
    "Find maintenance or citation-fidelity metrics",
    "Find at least one concrete workflow case study"
  ],
  "status": "open"
}
```

Rule:

```text
Every search task must be linked to a missing required output.
```

No generic browsing.

---

## Step 3: Discover Sources

Purpose:

```text
Search the web and collect candidate URLs.
```

Reads:

```text
data/discovery/search_tasks.jsonl
data/manifests/sources.jsonl
```

Writes:

```text
data/discovery/candidate_sources.jsonl
data/logs/loop_events.jsonl
```

Example candidate:

```json
{
  "candidate_id": "cand_000001",
  "search_task_id": "search_000001",
  "coverage_id": "evaluation_and_evidence",
  "url": "https://example.com/paper-or-report",
  "title": "Example Evaluation Report",
  "snippet": "Mentions benchmark comparison between retrieval and memory-backed agent.",
  "discovered_at": "2026-05-21T00:00:00-07:00",
  "discovery_method": "web_search",
  "possible_source_type": "paper",
  "duplicate_of_source_id": null,
  "status": "pending_triage"
}
```

Rule:

```text
Discovery does not count as evidence.
```

A URL is not evidence until it is acquired, preserved, digested, and mapped.

---

## Step 4: Triage Candidates

Purpose:

```text
Decide which candidate sources are worth acquiring.
```

Reads:

```text
data/discovery/candidate_sources.jsonl
data/manifests/sources.jsonl
loop_manifest.json
```

Writes:

```text
data/discovery/triage_decisions.jsonl
```

Example triage decision:

```json
{
  "triage_id": "triage_000001",
  "candidate_id": "cand_000001",
  "coverage_id": "evaluation_and_evidence",
  "decision": "acquire",
  "priority": 9,
  "expected_value": "high",
  "source_type": "paper",
  "reason": "Likely contains benchmark methodology and baseline comparison.",
  "risks": [
    "May not discuss LLM Wiki directly",
    "May only cover adjacent agent memory systems"
  ],
  "required_acquisition_mode": "html_or_pdf",
  "status": "queued_for_acquisition"
}
```

Triage decisions:

```text
acquire
skip_duplicate
skip_low_relevance
defer
blocked
needs_manual_review
```

Rule:

```text
Skipped and blocked sources must be logged.
```

This prevents the agent from repeatedly rediscovering the same inaccessible source.

---

## Step 5: Acquire Raw Sources

Purpose:

```text
Fetch and preserve source material before using it.
```

Reads:

```text
data/discovery/triage_decisions.jsonl
```

Writes:

```text
data/raw/<source_id>/*
data/manifests/sources.jsonl
data/logs/acquisition_failures.jsonl
reports/acquisition_status.md
```

Your existing `scripts/fetch_sources.py` should own this step.

For each acquired source, create:

```text
data/raw/src_000001/
  metadata.json
  source.html            # if web page
  source.pdf             # if PDF
  source.txt             # extracted readable text if available
  screenshot.png         # if visual layout matters
  repo/                  # if repository
```

Example `sources.jsonl` row:

```json
{
  "source_id": "src_000001",
  "candidate_id": "cand_000001",
  "title": "Example Evaluation Report",
  "url": "https://example.com/paper-or-report",
  "source_type": "paper",
  "coverage_areas": [
    "evaluation_and_evidence"
  ],
  "author_or_org": "Unknown",
  "date_published": "unknown",
  "date_accessed": "2026-05-21",
  "raw_path": "data/raw/src_000001/",
  "readable_text_path": "data/raw/src_000001/source.txt",
  "license": "unknown",
  "content_hash": "sha256:...",
  "acquisition_status": "success",
  "trust_level": "unknown",
  "notes": "Needs digest and claim extraction."
}
```

Acquisition invariant:

```text
A source cannot support a claim unless it has a source_id and raw_path.
```

---

## Step 6: Extract Readable Content

Purpose:

```text
Convert raw material into text the digest agent can read.
```

Reads:

```text
data/raw/<source_id>/*
data/manifests/sources.jsonl
```

Writes:

```text
data/raw/<source_id>/source.txt
data/logs/loop_events.jsonl
```

Extraction should be source-type specific:

| Source type         | Extraction method                                             |
| ------------------- | ------------------------------------------------------------- |
| HTML                | Save raw HTML and readable text.                              |
| PDF                 | Save PDF and extracted text.                                  |
| GitHub repo         | Save README, docs, file tree, selected code snippets.         |
| Discussion thread   | Save thread text, metadata, comment structure where possible. |
| Package/plugin page | Save metadata, description, install stats if available.       |
| Blocked page        | Save failure record, not a fake summary.                      |

Rule:

```text
If extraction fails, log it and keep the source in pending or failed state.
```

---

## Step 7: Digest Sources

Purpose:

```text
Turn one source into a structured note.
```

Reads:

```text
data/raw/<source_id>/source.txt
data/manifests/sources.jsonl
loop_manifest.json
```

Writes:

```text
data/manifests/source_digests.jsonl
```

Example digest record:

```json
{
  "digest_id": "digest_000001",
  "source_id": "src_000001",
  "created_at": "2026-05-21T00:00:00-07:00",
  "coverage_areas": [
    "evaluation_and_evidence"
  ],
  "source_summary": "This source discusses evaluation methods for memory-backed or retrieval-backed LLM agents.",
  "key_observations": [
    {
      "observation": "The source defines a baseline comparison against retrieval-only systems.",
      "local_evidence": "Section 3 or extracted text span TBD",
      "relevance": "Supports empirical judgment gate."
    }
  ],
  "supported_outputs": [
    "baseline_comparisons",
    "answer_quality_metrics"
  ],
  "possible_claims": [
    {
      "claim": "Evaluation of LLM Wiki-like systems requires baselines such as raw RAG, chat memory, or no memory.",
      "claim_type": "interpretation",
      "confidence": "medium"
    }
  ],
  "limitations": [
    "Source may discuss adjacent memory systems rather than LLM Wikis directly."
  ],
  "digest_status": "complete"
}
```

Digest invariant:

```text
An acquired source does not count toward coverage until it has a digest.
```

---

## Step 8: Extract Claims

Purpose:

```text
Convert digests into auditable claim records.
```

Reads:

```text
data/manifests/source_digests.jsonl
data/manifests/sources.jsonl
loop_manifest.json
```

Writes:

```text
data/manifests/claims.jsonl
data/manifests/claim_source_links.jsonl
```

Example claim:

```json
{
  "claim_id": "claim_000001",
  "claim": "LLM Wiki evaluation should compare against raw RAG, chat memory, and no-memory baselines.",
  "claim_type": "judgment",
  "coverage_areas": [
    "evaluation_and_evidence"
  ],
  "required_outputs_supported": [
    "baseline_comparisons"
  ],
  "supporting_sources": [
    "src_000001"
  ],
  "contradicting_sources": [],
  "confidence": "medium",
  "evidence_grade": "B",
  "status": "source_linked",
  "limitations": "Supported as an evaluation design principle; not yet backed by direct LLM Wiki benchmark results."
}
```

Claim types should be constrained:

```text
observed_fact
interpretation
hypothesis
evaluation_result
strategic_judgment
```

Claim invariant:

```text
No substantive report sentence should be introduced unless it can point to a claim_id.
```

---

## Step 9: Map Claims To Objective

Purpose:

```text
Show which exact framework requirement each claim helps satisfy.
```

Reads:

```text
data/manifests/claims.jsonl
loop_manifest.json
```

Writes:

```text
data/manifests/coverage_records.jsonl
loop_state.json
```

Example coverage record:

```json
{
  "coverage_record_id": "covrec_000001",
  "coverage_id": "evaluation_and_evidence",
  "required_output": "baseline_comparisons",
  "claim_ids": [
    "claim_000001"
  ],
  "source_ids": [
    "src_000001"
  ],
  "status": "partially_supported",
  "remaining_gap": "Need direct examples or benchmark results comparing LLM Wiki to raw RAG or chat memory.",
  "updated_at": "2026-05-21T00:00:00-07:00"
}
```

Coverage statuses:

```text
missing
candidate_sources_found
sources_acquired
digested
partially_supported
supported
audited
blocked
```

Rule:

```text
A coverage item can be supported only through claims, not through vibes or summaries.
```

---

## Step 10: Update Reports

Purpose:

```text
Update human-readable artifacts from manifests and claims.
```

Reads:

```text
loop_state.json
data/manifests/sources.jsonl
data/manifests/source_digests.jsonl
data/manifests/claims.jsonl
data/manifests/coverage_records.jsonl
```

Writes:

```text
reports/acquisition_status.md
reports/source_gap_review.md
reports/coverage_status.md
reports/evidence_matrix.md
reports/judgment_status.md
```

Important: these should be generated or semi-generated from the manifests.

Suggested report roles:

| Report                  | Role                                                                  |
| ----------------------- | --------------------------------------------------------------------- |
| `acquisition_status.md` | What was fetched, failed, blocked, or queued.                         |
| `source_gap_review.md`  | Which framework areas still lack evidence.                            |
| `coverage_status.md`    | Coverage area by coverage area status.                                |
| `evidence_matrix.md`    | Claim-to-source and output-to-source matrix.                          |
| `judgment_status.md`    | Descriptive, technical, empirical, strategic, paper-readiness status. |

Report invariant:

```text
Reports may summarize, but they may not invent new claims outside claims.jsonl.
```

---

## Step 11: Audit

Purpose:

```text
Reject unsupported synthesis and prevent false completion.
```

Reads:

```text
loop_manifest.json
loop_state.json
data/manifests/sources.jsonl
data/manifests/source_digests.jsonl
data/manifests/claims.jsonl
data/manifests/coverage_records.jsonl
reports/*.md
```

Writes:

```text
data/logs/audit_events.jsonl
loop_state.json
reports/source_gap_review.md
```

Audit checks:

```text
Source audit:
- Does every source_id have a raw_path?
- Does every source have date_accessed?
- Does every source have source_type?
- Are blocked sources logged?

Digest audit:
- Does every counted source have a digest?
- Does the digest identify relevance and limitations?
- Does the digest distinguish source facts from interpretation?

Claim audit:
- Does every claim have at least one source_id?
- Is the claim type valid?
- Is confidence justified?
- Is the evidence grade plausible?
- Are broad claims supported by multiple sources?

Coverage audit:
- Does every required output have support?
- Are weak areas still marked weak?
- Are missing areas still marked missing?
- Were contradictions preserved?

Judgment audit:
- Did the agent try to pass a gate prematurely?
- Are empirical claims backed by baselines or methods?
- Are strategic claims backed by cost, risk, and comparison evidence?
```

Example audit event:

```json
{
  "audit_id": "audit_000001",
  "created_at": "2026-05-21T00:00:00-07:00",
  "target_type": "coverage_area",
  "target_id": "evaluation_and_evidence",
  "status": "fail",
  "failures": [
    {
      "type": "insufficient_empirical_evidence",
      "message": "Baseline comparisons are proposed but not yet supported by direct LLM Wiki benchmark or case-study evidence."
    },
    {
      "type": "overbroad_claim",
      "claim_id": "claim_000001",
      "message": "Claim should be framed as evaluation design guidance, not evidence that LLM Wikis outperform RAG."
    }
  ],
  "required_fixes": [
    "Downgrade claim confidence to medium or low.",
    "Add direct benchmark or case-study source.",
    "Keep empirical gate as not_ready."
  ]
}
```

The auditor should have veto power.

---

# 7. What `scripts/fetch_sources.py` Should And Should Not Do

Your existing script should be narrow.

It should do:

```text
read acquisition queue
fetch raw source
save raw artifact
extract basic readable text when possible
write metadata
append/update sources.jsonl
log failures
```

It should not do:

```text
decide final conclusions
write synthesized reports
mark coverage complete
pass judgment gates
```

Recommended CLI shape:

```bash
python scripts/fetch_sources.py --queue data/discovery/triage_decisions.jsonl
python scripts/fetch_sources.py --source-url "https://example.com/source"
python scripts/fetch_sources.py --source-id src_000001 --refresh
```

Recommended output contract:

```text
On success:
  - creates data/raw/<source_id>/
  - appends data/manifests/sources.jsonl
  - logs event to data/logs/loop_events.jsonl

On failure:
  - appends data/logs/acquisition_failures.jsonl
  - marks candidate as blocked or failed
```

---

# 8. Add A Top-Level `run_loop.py`

Add one orchestration script:

```text
scripts/run_loop.py
```

Example commands:

```bash
python scripts/run_loop.py bootstrap
python scripts/run_loop.py next
python scripts/run_loop.py plan
python scripts/run_loop.py discover
python scripts/run_loop.py triage
python scripts/run_loop.py acquire
python scripts/run_loop.py digest
python scripts/run_loop.py claims
python scripts/run_loop.py synthesize
python scripts/run_loop.py audit
python scripts/run_loop.py once
python scripts/run_loop.py status
```

The command `once` should run a single bounded loop:

```text
select gap
→ plan discovery
→ discover or consume candidates
→ triage
→ acquire
→ digest
→ extract claims
→ update reports
→ audit
→ update state
```

Do not let the loop run unbounded at first. Single-iteration loops are easier to debug.

---

# 9. The Loop In Pseudocode

```python
def run_once():
    manifest = load_json("loop_manifest.json")
    state = load_json("loop_state.json")

    ensure_objective_hash_is_current(manifest, state)

    target = select_highest_priority_gap(manifest, state)

    write_loop_event("selected_gap", {
        "coverage_id": target["id"],
        "reason": target["selection_reason"]
    })

    search_tasks = plan_discovery(manifest, state, target)
    append_jsonl("data/discovery/search_tasks.jsonl", search_tasks)

    candidates = discover_sources(search_tasks)
    append_jsonl("data/discovery/candidate_sources.jsonl", candidates)

    triage_decisions = triage_candidates(
        candidates=candidates,
        manifest=manifest,
        existing_sources=load_jsonl("data/manifests/sources.jsonl")
    )
    append_jsonl("data/discovery/triage_decisions.jsonl", triage_decisions)

    acquired_sources = acquire_sources(triage_decisions)
    append_or_update_sources_manifest(acquired_sources)

    extracted_sources = extract_readable_content(acquired_sources)

    digests = digest_sources(
        sources=extracted_sources,
        manifest=manifest,
        target=target
    )
    append_jsonl("data/manifests/source_digests.jsonl", digests)

    claims = extract_claims(
        digests=digests,
        manifest=manifest
    )
    append_jsonl("data/manifests/claims.jsonl", claims)

    coverage_records = map_claims_to_coverage(
        claims=claims,
        manifest=manifest
    )
    append_jsonl("data/manifests/coverage_records.jsonl", coverage_records)

    update_reports(
        manifest=manifest,
        state=state,
        sources=load_jsonl("data/manifests/sources.jsonl"),
        digests=load_jsonl("data/manifests/source_digests.jsonl"),
        claims=load_jsonl("data/manifests/claims.jsonl"),
        coverage_records=load_jsonl("data/manifests/coverage_records.jsonl")
    )

    audit = audit_loop_outputs(
        manifest=manifest,
        state=state,
        target=target
    )
    append_jsonl("data/logs/audit_events.jsonl", [audit])

    new_state = update_loop_state(
        manifest=manifest,
        old_state=state,
        target=target,
        audit=audit
    )
    save_json("loop_state.json", new_state)
```

---

# 10. Completion Logic

A coverage area passes only if this function returns true:

```python
def coverage_area_passes(area_id, manifest, state, sources, digests, claims, coverage_records, audits):
    area = manifest["coverage_areas"][area_id]

    required_outputs = area["required_outputs"]

    for output in required_outputs:
        if not has_supported_coverage_record(area_id, output, coverage_records):
            return False

    if not minimum_evidence_satisfied(area, sources, claims):
        return False

    if not all_counted_sources_have_raw_paths(area_id, sources):
        return False

    if not all_counted_sources_have_digests(area_id, sources, digests):
        return False

    if not all_supported_claims_have_sources(area_id, claims):
        return False

    if latest_audit_status(area_id, audits) != "pass":
        return False

    return True
```

A judgment gate passes only if all its required coverage areas pass.

```python
def judgment_gate_passes(gate_id, manifest, state):
    gate = manifest["judgment_gates"][gate_id]

    for area_id in gate["required_coverage_areas"]:
        if state["coverage_state"][area_id]["status"] != "audited":
            return False

    return True
```

---

# 11. Enforcement Invariants

These are the rules that make the objective real.

## Source invariants

```text
No source can support a claim unless it appears in data/manifests/sources.jsonl.
No source can count toward evidence unless raw_path exists or a failure is logged.
No historical source can count unless date_accessed is present.
No implementation source can count unless repo/docs/demo/code evidence is preserved.
No blocked source can disappear from the system; it must be logged.
```

## Digest invariants

```text
No acquired source counts toward coverage until it has a digest.
No digest can claim more than the source supports.
No digest can hide limitations.
No digest can silently resolve contradictions.
```

## Claim invariants

```text
No substantive claim without claim_id.
No claim_id without source_id.
No empirical claim without method, baseline, or explicit limitation.
No broad ecosystem claim from a single weak source.
No unsupported claim may be upgraded beyond hypothesis.
```

## Report invariants

```text
No report may introduce claims absent from claims.jsonl.
No report may mark a coverage area complete before audit.
No judgment report may pass a gate while required outputs are missing.
No report may erase blocked sources or acquisition failures.
```

## Gate invariants

```text
No descriptive judgment without origin, terminology, workflow, and implementation evidence.
No technical judgment without architecture, workflow, and implementation evidence.
No empirical judgment without evaluation methods, baselines, or case-study evidence.
No strategic judgment without comparisons, risks, use cases, and cost/complexity evidence.
No research-paper judgment without all prior gates and explicit limitations.
```

---

# 12. Recommended Agent Prompt

Use this as the standing loop objective for the agent:

```text
You are operating a research-control loop for an LLM Wiki evidence repository.

The static objective is reports/coverage_framework.md.
The machine-readable objective is loop_manifest.json.
The mutable runtime state is loop_state.json.

Your job is to make the objective true by converting every framework requirement into preserved sources, source manifests, source digests, auditable claims, coverage records, reports, and judgment-gate statuses.

On every loop:

1. Read loop_manifest.json and loop_state.json.
2. Select the highest-priority missing or weak coverage area.
3. Generate targeted discovery tasks tied to missing required outputs.
4. Search for candidate web sources.
5. Triage candidate sources for relevance, novelty, trust, and acquisition feasibility.
6. Acquire raw source material before using it.
7. Write or update data/manifests/sources.jsonl.
8. Digest each acquired source into data/manifests/source_digests.jsonl.
9. Extract claims into data/manifests/claims.jsonl.
10. Map claims to framework requirements in data/manifests/coverage_records.jsonl.
11. Update reports from manifests and claims.
12. Audit all updates for source fidelity, unsupported claims, overgeneralization, missing metadata, and premature judgment.
13. Update loop_state.json with the new status and next action.

Never treat browsing alone as progress.
Never treat acquisition alone as coverage.
Never treat synthesis alone as evidence.
Never mark a coverage area complete without an audit pass.
Never pass a judgment gate while required outputs are missing.

When evidence is weak, mark it weak.
When sources conflict, preserve the conflict.
When a source is blocked, log the block.
When a claim is unsupported, downgrade it to a hypothesis or remove it.
When a gate fails, write the exact missing evidence needed to pass.
```

---

# 13. First Five Concrete Loops For Your Repo

Given your current framework, I would run the first five loops like this.

## Loop 1: Bootstrap And Normalize

Goal:

```text
Make sure loop_manifest.json and loop_state.json faithfully reflect reports/coverage_framework.md.
```

Outputs:

```text
loop_manifest.json
loop_state.json
reports/initial_gap_checklist.md
reports/coverage_status.md
```

Completion condition:

```text
Every framework section has a coverage area, required outputs, evidence minimums, and gate assignment.
```

---

## Loop 2: Audit Existing Acquisition

Goal:

```text
Inspect what has already been fetched or cloned.
```

Outputs:

```text
data/manifests/sources.jsonl
reports/acquisition_status.md
reports/source_gap_review.md
```

Completion condition:

```text
Every existing raw source has a source_id, path, type, coverage mapping, and acquisition status.
```

This prevents the loop from re-fetching what you already have.

---

## Loop 3: Digest Existing Sources

Goal:

```text
Turn existing raw sources into structured source digests.
```

Outputs:

```text
data/manifests/source_digests.jsonl
data/manifests/claims.jsonl
data/manifests/coverage_records.jsonl
reports/evidence_matrix.md
```

Completion condition:

```text
Previously acquired sources are either digested, marked failed, or marked pending with reason.
```

This is crucial. Your objective is not only to collect information; it is to collect and digest it.

---

## Loop 4: Fill Weak Empirical Evidence

Goal:

```text
Collect benchmark, evaluation, baseline, citation-fidelity, and case-study evidence.
```

Target coverage area:

```text
evaluation_and_evidence
```

Outputs:

```text
data/discovery/search_tasks.jsonl
data/discovery/candidate_sources.jsonl
data/manifests/sources.jsonl
data/manifests/source_digests.jsonl
reports/evidence_matrix.md
reports/judgment_status.md
```

Completion condition:

```text
The empirical gate has concrete source-backed benchmark or case-study candidates, or it remains explicitly not_ready with missing evidence listed.
```

---

## Loop 5: Fill Risks And Comparisons

Goal:

```text
Collect evidence for provenance risk, maintenance risk, privacy/security risk, RAG comparison, PKM comparison, knowledge graph comparison, and agent-memory comparison.
```

Target coverage areas:

```text
risks_governance_ethics
comparison_space
```

Outputs:

```text
reports/source_gap_review.md
reports/evidence_matrix.md
reports/judgment_status.md
```

Completion condition:

```text
Strategic judgment is either source-backed or explicitly blocked by listed evidence gaps.
```

---

# 14. Minimal Viable Loop

For v1, keep it simple:

```bash
python scripts/run_loop.py bootstrap
python scripts/run_loop.py status
python scripts/run_loop.py once
python scripts/run_loop.py audit
```

The first version does not need autonomous multi-agent orchestration. It only needs to reliably enforce this sequence:

```text
gap → search → candidate → triage → acquire → digest → claim → coverage → report → audit → state
```

Once that works, split the roles into specialized agents.

---

# 15. The Cleanest Definition Of "Objective Is True"

Your objective is true when this condition holds:

```text
For every coverage area in loop_manifest.json:

1. Every required output is either:
   a. supported by output-specific, source-backed claims, and
   b. linked to raw material, source manifests, source digests, claim records, coverage records, and a passing audit.

2. Every supporting source has:
   a. source_id,
   b. raw_path,
   c. source_type,
   d. date_accessed,
   e. digest_id.

3. Every substantive claim has:
   a. claim_id,
   b. source_id,
   c. claim_type,
   d. confidence,
   e. evidence grade,
   f. limitation note.

4. Every report section is generated from claims and sources.

5. Every judgment gate has passed audit.

6. Discovery/acquisition queues are empty:
   a. no open search task,
   b. no candidate pending triage,
   c. no source queued for acquisition,
   d. no acquired source pending digest,
   e. no digest pending claim extraction,
   f. no claim pending audit.

7. The XML inaccessible-source log is current for every desired source that could not be accessed.
```

That last clause matters. A truthful loop does not pretend everything is solved. It makes the difference between **supported**, **partial**, **weak**, **blocked**, and **unknown** explicit, but only **supported + audited + all gates passed** is a stop condition.

The shortest operational version:

```text
The framework is satisfied only when the repo can prove, from manifests and raw sources, that every coverage requirement is supported and audited, all judgment gates pass, all active queues are empty, and inaccessible desired sources are logged without being counted as evidence.
```
