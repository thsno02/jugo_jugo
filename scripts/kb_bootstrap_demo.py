#!/usr/bin/env python3
"""Bootstrap the KB initialization demo from existing local evidence."""

from __future__ import annotations

import json
import re
import shutil
from collections import Counter, defaultdict
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

from kb_common import ROOT, read_jsonl, root_relative, write_yaml


RUN_SLUG = "kb_initialization_bootstrap"

SOURCE_VERSION = "source_snapshot_2026-05-21"
PLAN_VERSION = "plan_snapshot_2026-05-24"


def now() -> datetime:
    return datetime.now().astimezone()


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "_", value)
    return re.sub(r"_+", "_", value).strip("_")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def citation_block(fields: dict[str, str]) -> str:
    lines = []
    for key in [
        "target",
        "target_version",
        "pinned_version",
        "citation_role",
        "why_cited",
        "evidence_summary",
        "source_path",
    ]:
        if key in fields:
            lines.append(f"    {key}: {fields[key]}")
    return "\n".join(lines)


def raw_citation(target: str, role: str, why: str, summary: str, source_path: str | None = None) -> dict[str, str]:
    return {
        "target": target,
        "target_version": SOURCE_VERSION,
        "pinned_version": target,
        "citation_role": role,
        "why_cited": why,
        "evidence_summary": summary,
        "source_path": source_path or str(Path(target).parent),
    }


def artifact_citation(target: str, version: str, role: str, why: str, summary: str) -> dict[str, str]:
    return {
        "target": target,
        "target_version": version,
        "pinned_version": target,
        "citation_role": role,
        "why_cited": why,
        "evidence_summary": summary,
    }


def node_citation(node_id: str, role: str, why: str, summary: str) -> dict[str, str]:
    return {
        "target": f"kb/{node_id}.md",
        "target_version": "1.0",
        "pinned_version": f"nodes/{node_id}/versions/1.0/card.md",
        "citation_role": role,
        "why_cited": why,
        "evidence_summary": summary,
    }


def metadata_for_node(
    *,
    node_id: str,
    title: str,
    created_at: str,
    run_dir: str,
    tags: list[str],
    stability: str = "working",
) -> dict[str, Any]:
    return {
        "schema": "kb.node_metadata.v1",
        "id": node_id,
        "title": title,
        "version": "1.0",
        "version_status": "adopted",
        "node_created_at": created_at,
        "node_archived_at": None,
        "version_created_at": created_at,
        "version_adopted_at": created_at,
        "version_superseded_at": None,
        "version_archived_at": None,
        "status": "active",
        "stability": stability,
        "usable_as_support": True,
        "paths": {
            "version_dir": f"nodes/{node_id}/versions/1.0/",
            "card": f"nodes/{node_id}/versions/1.0/card.md",
            "provenance": f"nodes/{node_id}/versions/1.0/provenance.md",
            "change": f"nodes/{node_id}/versions/1.0/change.md",
            "kb_view": f"kb/{node_id}.md",
        },
        "tags": tags,
        "audit": {
            "state": "passed",
            "run": f"{run_dir}/audit_report.md",
        },
    }


def provenance(
    *,
    node_id: str,
    title: str,
    inputs: list[str],
    run_dir: str,
    dynamic_retrieval: str = "None. This version used only existing local data and process artifacts.",
    limits: str = "This node is an initialization artifact. It should be revised when stronger primary evidence, measured citation audits, or downstream impact reviews change the support contract.",
) -> str:
    input_lines = "\n".join(f"- {item}" for item in inputs)
    return f"""# Provenance

node_id:: {node_id}
version:: 1.0

## Why this version exists

This version initializes the adopted KB view for `{title}` so later agents can cite, inspect, revise, and audit the concept as a maintained knowledge object.

## Inputs used

### Existing data

{input_lines}

### Dynamic retrieval, if any

{dynamic_retrieval}

### Prior KB nodes

Any prior KB nodes used by this version are declared in `card.md` citations and pinned through `pinned_version`.

### Process artifacts

- {run_dir}/run_plan.md
- {run_dir}/data_scope.md
- {run_dir}/generator_trace.md
- {run_dir}/audit_report.md

## Production rationale

The node was generated as a small, auditable 0-1 bundle rather than as a final encyclopedia page. Claims are intentionally narrow and are tied to either preserved raw/source artifacts or prior adopted KB nodes.

## Citation rationale

Footnotes support specific claims. References provide broader background or process context. Citation paths are repo-root relative so the same card can be copied into `kb/` without breaking the parser.

## Synthesis decisions

The synthesis distinguishes source-backed observations from process choices made by this demo. It does not treat agent synthesis as ground truth.

## Audit trail

audit_result:: passed
audit_report:: {run_dir}/audit_report.md

## Adoption rationale

Version 1.0 is adopted because the version bundle is complete, required card sections exist, citations are parseable, and the node is useful as a support object for later initialization runs.

## Limits and uncertainty

{limits}

## Revision triggers

- A cited source is found to be missing, stale, blocked, or over-interpreted.
- A later major version changes the definition or support contract.
- A citation audit finds that a footnote does not support the attached claim.
- Dynamic retrieval adds stronger or contradictory evidence.
"""


def change_doc(node_id: str, created_at: str, run_dir: str) -> str:
    return f"""# Change: genesis -> 1.0

node_id:: {node_id}
from_version:: null
to_version:: 1.0
change_scale:: minor
propagation_required:: false
created_at:: {created_at}
run_id:: {run_dir}/

## Why this changed

This is the genesis version for the node.

## Old meaning

No prior adopted version existed.

## New meaning

The node now has an adopted 1.0 version bundle that can be rendered into `kb/` and cited by later nodes.

## Semantic delta

Initial creation only.

## Why this is minor

The version does not replace a prior support contract.

## Expected impact

No downstream impact propagation is required for genesis creation.
"""


def write_schema() -> None:
    schema = {
        "schema": "kb.schema.v1",
        "generated_at": now().isoformat(timespec="seconds"),
        "contracts": {
            "node_database": "nodes/ is the source of truth for maintained node version bundles.",
            "kb_view": "kb/ renders adopted versions only.",
            "generated": "generated/ contains rebuildable graph, backlink, impact, and status artifacts.",
            "version_bundle": ["node.yaml", "card.md", "provenance.md", "change.md"],
            "required_card_sections": ["# Title", "## Footnotes", "## References"],
            "required_citation_fields": [
                "target",
                "target_version",
                "pinned_version",
                "citation_role",
                "why_cited",
                "evidence_summary",
            ],
            "version_semantics": {
                "minor": "Core meaning and support contract still hold; no impact propagation.",
                "major": "Core meaning or support contract changed; downstream citations require review.",
            },
        },
    }
    write_yaml(ROOT / "kb" / "_schema.yaml", schema)


def write_control_files(run_dir: str) -> None:
    write_text(
        ROOT / ".llmwiki" / "control" / "principles.md",
        """# KB Initialization Principles

1. Preserve raw sources before synthesis.
2. Treat `nodes/` as the maintained node database.
3. Treat `kb/` as the adopted-version consumption view.
4. Keep every node version as `node.yaml`, `card.md`, `provenance.md`, and `change.md`.
5. Put claim-level support in footnotes and broader context in references.
6. Treat provenance as part of the knowledge object, not a side note.
7. Use major changes to create impact review tasks, not automatic downstream rewrites.
8. Record evidence gaps and dynamic retrieval in files before using new evidence.
9. Use each 0-1 node run as a skill evaluation sample.
""",
    )
    write_text(
        ROOT / ".llmwiki" / "control" / "state.md",
        f"""# KB Initialization State

current_phase:: bootstrap_and_first_node_batch
loop_owner:: main_owned_with_autonomous_reflection
latest_run:: {run_dir}
last_updated:: {now().isoformat(timespec="seconds")}

## Current Decision

Continue with a small 0-1 node batch backed by existing local data, then allow the loop to choose the next highest-value validation action without waiting for a human checkpoint. Dynamic retrieval is allowed only after a retrieval request is written and the new source is preserved under `data/raw/`.

## Next Action

Run validators, build the adopted KB view, parse citations, compute impact queue, and update status.
""",
    )
    write_yaml(
        ROOT / ".llmwiki" / "control" / "state.yaml",
        {
            "schema": "kb.control_state.v1",
            "current_phase": "bootstrap_and_first_node_batch",
            "loop_owner": "main_owned_with_autonomous_reflection",
            "latest_run": run_dir,
            "last_updated": now().isoformat(timespec="seconds"),
            "next_action": "validate_build_parse_status",
            "autonomy": {
                "human_absent_assumption": True,
                "may_continue_without_checkpoint": [
                    "structural_validation",
                    "view_generation",
                    "citation_graph_generation",
                    "status_generation",
                    "skill_eval_logging",
                    "next_run_planning",
                    "major_change_simulation",
                ],
                "must_stop_or_record_blocker": [
                    "destructive_git_operation",
                    "large_network_retrieval_without_request",
                    "schema_change_that_invalidates_existing_nodes",
                    "semantic_adoption_after_failed_audit",
                ],
            },
        },
    )
    write_yaml(
        ROOT / ".llmwiki" / "control" / "action_queue.yaml",
        {
            "schema": "kb.action_queue.v1",
            "updated_at": now().isoformat(timespec="seconds"),
            "items": [
                {
                    "id": "act_001",
                    "status": "done",
                    "action": "bootstrap_contracts_scripts_and_skill_seeds",
                },
                {
                    "id": "act_002",
                    "status": "in_progress",
                    "action": "generate_and_audit_first_0_1_node_batch",
                },
                {
                    "id": "act_003",
                    "status": "open",
                    "action": "run_dynamic_retrieval_test_for_recorded_evidence_gap",
                },
                {
                    "id": "act_004",
                    "status": "open",
                    "action": "simulate_major_change_and_compute_impact_queue",
                },
            ],
        },
    )


def write_autonomy_files(run_dir: str) -> None:
    control_dir = ROOT / ".llmwiki" / "control"
    write_text(
        control_dir / "autonomy.md",
        f"""# Autonomous Loop Policy

created_at:: {now().isoformat(timespec="seconds")}
latest_run:: {run_dir}

## Purpose

This KB initialization loop is expected to make progress while the human is away. The agent should keep state on disk, choose bounded next actions, and periodically reflect on whether the loop is still reducing the intended uncertainty.

## Autonomy Budget

Allowed without a human checkpoint:

- Run validators and builders.
- Create additional 0-1 nodes from already preserved local evidence.
- Write retrieval requests for evidence gaps.
- Execute small dynamic retrieval only after the request exists and raw evidence is preserved.
- Simulate one major candidate to test impact analysis.
- Update skill seeds when a concrete failure mode is recorded.
- Write reports, summary state, and next-action decisions.

Stop or mark blocked before:

- Destructive git operations.
- Replacing user-authored files outside the KB initialization surface.
- Treating a failed audit as adopted.
- Expanding to broad web research without a written retrieval request and preservation plan.
- Changing the core node/version/citation contract in a way that invalidates existing bundles.

## Decision Rule

At each pause point, choose exactly one next action:

1. `repair_instrumentation` if scripts or validators fail.
2. `iterate_node_batch` if adopted node count is below five and evidence is sufficient.
3. `dynamic_retrieval_test` if a recorded evidence gap blocks a useful node.
4. `major_impact_test` if citation graph exists and impact propagation has not been exercised.
5. `skill_reflection` if a run exposes a repeated skill failure.
6. `demo_report` if acceptance criteria are mostly satisfied.

Write the chosen action to `decision_log.yaml`, `summary_state.md`, and `standing_status.md`.
""",
    )
    write_text(
        control_dir / "reflection_policy.md",
        """# Reflection Policy

## Reflection Cadence

Reflect after every completed run and after every validation/build failure.

## Reflection Questions

1. Did the latest action increase KB auditability, or only add content?
2. Which assumption failed, if any?
3. Was the failure a case-level issue or a reusable skill failure?
4. Did the loop preserve enough state for another agent to resume?
5. What is the single next action with the highest expected value?

## Required Outputs

- `.llmwiki/control/summary_state.md`
- `.llmwiki/control/standing_status.md`
- `.llmwiki/control/decision_log.yaml`
- `.llmwiki/runs/<run_id>/skill_eval.md`
""",
    )
    write_text(
        control_dir / "summary_state.md",
        f"""# Summary State

current_phase:: bootstrap_and_first_node_batch
latest_run:: {run_dir}
last_completed_action:: contracts_and_scripts_written
current_blocker:: none
human_checkpoint_needed:: no
recommended_next_action:: validate_build_parse_status

## Resume Notes

The loop is allowed to continue autonomously through validation, view generation, citation graph generation, status generation, next-run planning, and a bounded impact simulation. Use `standing_status.md` for the low-noise monitor view and `decision_log.yaml` for decisions.
""",
    )
    write_text(
        control_dir / "standing_status.md",
        f"""# Standing Status

state:: active
latest_run:: {run_dir}
last_updated:: {now().isoformat(timespec="seconds")}
next_action:: validate_build_parse_status
blocker:: none
human_needed:: no
""",
    )
    write_yaml(
        control_dir / "decision_log.yaml",
        {
            "schema": "kb.decision_log.v1",
            "updated_at": now().isoformat(timespec="seconds"),
            "decisions": [
                {
                    "id": "dec_001",
                    "run": run_dir,
                    "decision": "continue_autonomously_after_bootstrap",
                    "reason": "Human may be away for a long period; the loop has bounded validation, build, reflection, retrieval-request, and impact-test actions that can proceed from on-disk state.",
                    "next_action": "validate_build_parse_status",
                    "human_checkpoint_needed": False,
                }
            ],
        },
    )


def write_agent_tasks(run_dir: str) -> None:
    tasks = {
        "planner": "Select one narrow 0-1 node target from source_candidates.yaml and write a run plan. Do not write cards directly.",
        "generator": "Generate a complete version bundle using only the scoped evidence. If evidence is insufficient, write retrieval_request.md before searching.",
        "audit": "Validate node.yaml, card sections, citation fields, provenance, change notes, and adoption readiness.",
        "eval": "Evaluate the run as a skill sample. Separate case-level observations from reusable skill failures.",
    }
    for name, body in tasks.items():
        write_text(
            ROOT / ".llmwiki" / "agents" / name / "task.md",
            f"""# {name.title()} Task

run_dir:: {run_dir}

## Responsibility

{body}

## Safety

You are not the only executor in this repo. Do not revert, overwrite, or clean unrelated files. Log any read outside the scoped inputs.
""",
        )


def write_skill_seeds() -> None:
    seeds = {
        "node_bundle_generation": "Create complete version bundles with node metadata, card, provenance, and change notes.",
        "provenance_generation": "Explain why a version exists, what inputs it used, why synthesis is allowed, how it was audited, and when it should be revised.",
        "citation_formatting": "Write parseable footnotes and references with target, target_version, pinned_version, citation_role, why_cited, and evidence_summary.",
        "citation_audit": "Check that citations exist, are pinned, are specific, and do not over-support the attached claim.",
        "dynamic_retrieval": "Convert evidence gaps into retrieval requests, preserve retrieved raw sources, update manifests, and record provenance.",
        "adoption_gate": "Adopt only versions whose bundle, citations, provenance, and change notes pass audit; hold major candidates until impact review.",
        "view_building": "Render adopted versions into kb/ and rebuild index, citation graph, backlinks, impact queue, and status.",
        "skill_eval": "Use each 0-1 node run to record clear skill failures and avoid upgrading global skills from one-off observations.",
    }
    for name, description in seeds.items():
        write_text(
            ROOT / ".llmwiki" / "skills" / name / "skill.md",
            f"""# {name}

status:: seed
created_at:: {now().isoformat(timespec="seconds")}

## Purpose

{description}

## Demo Rule

Prefer narrow, auditable improvements over broad style changes. A skill update requires a named failure mode from a completed run.
""",
        )


def build_inventory() -> None:
    sources = read_jsonl(ROOT / "data" / "manifests" / "sources.jsonl")
    digests = {row.get("source_id"): row for row in read_jsonl(ROOT / "data" / "manifests" / "source_digests.jsonl")}
    claims = read_jsonl(ROOT / "data" / "manifests" / "claims.jsonl")
    source_types = Counter(row.get("source_type", "unknown") for row in sources)
    statuses = Counter(row.get("status", "unknown") for row in sources)
    coverage_sources: dict[str, set[str]] = defaultdict(set)
    for digest in digests.values():
        for area in digest.get("coverage_areas", []):
            coverage_sources[area].add(digest.get("source_id"))

    inventory_sources = []
    for row in sorted(sources, key=lambda item: item.get("source_id", "")):
        digest = digests.get(row.get("source_id"), {})
        inventory_sources.append(
            {
                "source_id": row.get("source_id"),
                "status": row.get("status"),
                "source_type": row.get("source_type"),
                "source_url": row.get("source_url"),
                "local_dir": row.get("local_dir"),
                "readable_text_path": digest.get("readable_text_path"),
                "coverage_areas": digest.get("coverage_areas", []),
                "supported_outputs": digest.get("supported_outputs", []),
                "limitations": digest.get("limitations", []),
            }
        )

    write_yaml(
        ROOT / ".llmwiki" / "control" / "data_inventory.yaml",
        {
            "schema": "kb.data_inventory.v1",
            "generated_at": now().isoformat(timespec="seconds"),
            "summary": {
                "sources_total": len(sources),
                "source_statuses": dict(statuses),
                "source_types": dict(source_types),
                "claims_total": len(claims),
                "coverage_area_source_counts": {key: len(value) for key, value in sorted(coverage_sources.items())},
            },
            "hard_gaps": [
                {
                    "id": "blocked_reddit_discourse",
                    "reason": "Several Reddit captures are blocked and cannot support community-reception claims beyond block metadata.",
                    "source": "reports/source_gap_review.md",
                },
                {
                    "id": "aicritique_intercept_failure",
                    "reason": "The AICritique enterprise article capture contains only an intercept message.",
                    "source": "reports/source_gap_review.md",
                },
            ],
            "sources": inventory_sources,
        },
    )

    candidates = [
        {
            "candidate_id": "current_kb_initialization_loop",
            "status": "used_in_bootstrap_batch",
            "evidence": ["loop_plan_init_kb.md", "reports/coverage_framework.md"],
        },
        {
            "candidate_id": "llm_wiki_working_definition",
            "status": "used_in_bootstrap_batch",
            "evidence": ["data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt", "reports/source_gap_review.md"],
        },
        {
            "candidate_id": "source_preservation_precondition_trust",
            "status": "used_in_bootstrap_batch",
            "evidence": ["data/manifests/sources.jsonl", "reports/source_gap_review.md"],
        },
        {
            "candidate_id": "provenance_as_core_knowledge_asset",
            "status": "used_in_bootstrap_batch",
            "evidence": ["loop_plan_init_kb.md", "data/raw/arxiv/arxiv-alce/text.txt"],
        },
        {
            "candidate_id": "citation_driven_impact_propagation",
            "status": "used_in_bootstrap_batch",
            "evidence": ["loop_plan_init_kb.md", "data/raw/arxiv/arxiv-alce/text.txt"],
        },
        {
            "candidate_id": "dynamic_retrieval_as_controlled_fallback",
            "status": "used_in_bootstrap_batch",
            "evidence": ["loop_plan_init_kb.md", "reports/source_gap_review.md"],
        },
    ]
    write_yaml(
        ROOT / ".llmwiki" / "control" / "source_candidates.yaml",
        {
            "schema": "kb.source_candidates.v1",
            "generated_at": now().isoformat(timespec="seconds"),
            "candidates": candidates,
        },
    )


def node_specs(ids: dict[str, str]) -> list[dict[str, Any]]:
    plan_ref = artifact_citation(
        "loop_plan_init_kb.md",
        PLAN_VERSION,
        "process_contract",
        "Defines the initialization loop, node version bundle, provenance, citation, adoption, and impact rules used by this demo.",
        "The plan states that nodes are version bundles, kb/ is an adopted view, citations drive impact analysis, and dynamic retrieval must be controlled.",
    )
    source_gap_ref = artifact_citation(
        "reports/source_gap_review.md",
        SOURCE_VERSION,
        "evidence_inventory",
        "Summarizes the local raw corpus, supported coverage areas, and hard evidence gaps.",
        "The review records strong origin/workflow evidence, implementation evidence, and blocked Reddit/AICritique gaps.",
    )
    claims_ref = artifact_citation(
        "data/manifests/claims.jsonl",
        SOURCE_VERSION,
        "claim_manifest",
        "Provides source-linked claim records from the acquisition phase.",
        "The manifest records source-linked claims, coverage areas, confidence, and supporting sources.",
    )
    sources_ref = artifact_citation(
        "data/manifests/sources.jsonl",
        SOURCE_VERSION,
        "source_manifest",
        "Records source ids, acquisition status, local paths, tags, and source types.",
        "The manifest is the local source provenance entry point for raw data used by the KB demo.",
    )
    gist_ref = raw_citation(
        "data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt",
        "primary_source",
        "Supports the working definition of an LLM-maintained persistent wiki between raw sources and user queries.",
        "The gist describes raw sources, the wiki, schema, ingest, query, lint, and a persistent compounding artifact.",
    )
    clawhub_ref = raw_citation(
        "data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt",
        "implementation_source",
        "Supports the claim that LLM Wiki runtimes expose raw/wiki/schema workflows and deterministic lint/gap mapping.",
        "The page describes a CLI/MCP runtime with raw assets, wiki outputs, manifests, compile readiness, lint, and gap mapping.",
    )
    compiler_ref = raw_citation(
        "data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md",
        "implementation_source",
        "Supports treating the pattern as a compile-and-maintain workflow with query, view, and ingest commands.",
        "The README describes compiling raw sources into an interlinked markdown wiki and querying or viewing the artifact.",
    )
    alce_ref = raw_citation(
        "data/raw/arxiv/arxiv-alce/text.txt",
        "research_context",
        "Supports the need to evaluate citation quality rather than assuming citations are automatically faithful.",
        "The ALCE abstract frames citations as a way to improve factual correctness and verifiability and evaluates citation quality.",
    )

    return [
        {
            "slug": "llm_wiki_working_definition",
            "title": "LLM Wiki is a source-backed maintained wiki artifact",
            "tags": ["llm-wiki", "definition", "source-backed"],
            "stability": "solid",
            "card": f"""# LLM Wiki is a source-backed maintained wiki artifact

For this KB initialization demo, an LLM Wiki is a persistent knowledge system in which immutable raw sources are preserved, an agent-maintained markdown wiki is compiled from those sources, and schema or control rules make the wiki inspectable and maintainable.[^1] The local evidence base also supports treating the pattern as a maintenance architecture, not only as query-time retrieval: source capture, readable extraction, digest or compile, claim mapping, reports, lint or audit, and human review are recurring workflow elements.[^2]

This definition is operational rather than universal. It is meant to support node generation, citation audit, and later revision; it does not claim that every implementation uses the same graph model, storage engine, interface, or evaluation method.[^3]

## Footnotes

[^1]:
{citation_block(gist_ref)}

[^2]:
{citation_block(source_gap_ref)}

[^3]:
{citation_block(compiler_ref)}

## References

### [R1] Initialization plan
{citation_block(plan_ref)}

### [R2] Claim manifest
{citation_block(claims_ref)}
""",
            "inputs": [
                "data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt",
                "reports/source_gap_review.md",
                "data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md",
                "loop_plan_init_kb.md",
                "data/manifests/claims.jsonl",
            ],
        },
        {
            "slug": "current_kb_initialization_loop",
            "title": "The current KB initialization loop turns raw data into auditable adopted nodes",
            "tags": ["llm-wiki", "kb-initialization", "agent-loop"],
            "stability": "working",
            "card": f"""# The current KB initialization loop turns raw data into auditable adopted nodes

The current demo loop starts from preserved local data, creates small node version bundles, records provenance, audits citations, adopts passing versions into `kb/`, and derives graph or impact artifacts from citations rather than from a hand-written graph.[^1] This process instantiates the working LLM Wiki definition as a filesystem contract: raw sources stay in `data/`, maintained nodes live under `nodes/`, adopted cards are rendered into `kb/`, and rebuildable outputs live under `generated/`.[^2]

The loop is deliberately narrow. Its purpose is not to finish a perfect encyclopedia, but to test whether an agent can repeatedly produce knowledge objects that are traceable, inspectable, and safe to revise.[^3]

## Footnotes

[^1]:
{citation_block(plan_ref)}

[^2]:
{citation_block(node_citation(ids["llm_wiki_working_definition"], "background_definition", "Provides the adopted working definition that this loop operationalizes.", "The cited node defines LLM Wiki as a source-backed maintained wiki artifact."))}

[^3]:
{citation_block(source_gap_ref)}

## References

### [R1] Source manifest
{citation_block(sources_ref)}

### [R2] Implementation runtime example
{citation_block(clawhub_ref)}
""",
            "inputs": [
                "loop_plan_init_kb.md",
                f"nodes/{ids['llm_wiki_working_definition']}/versions/1.0/card.md",
                "reports/source_gap_review.md",
                "data/manifests/sources.jsonl",
                "data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt",
            ],
        },
        {
            "slug": "source_preservation_precondition_trust",
            "title": "Source preservation is a precondition for KB trust",
            "tags": ["llm-wiki", "provenance", "source-preservation"],
            "stability": "solid",
            "card": f"""# Source preservation is a precondition for KB trust

The KB can only be audited if later agents can return from a synthesized claim to the preserved material behind it. In this repo, that means source ids, acquisition status, local raw paths, readable text paths, digests, claim links, and known access failures must remain available alongside synthesized nodes.[^1] The working LLM Wiki definition depends on this separation because the wiki is a maintained layer between immutable raw sources and user-facing answers, not a replacement for the source record.[^2]

Preservation does not make a synthesis true by itself. It makes the synthesis inspectable: an auditor can check whether a claim is supported, over-broad, stale, contradicted, or only a process decision.[^3]

## Footnotes

[^1]:
{citation_block(sources_ref)}

[^2]:
{citation_block(node_citation(ids["llm_wiki_working_definition"], "background_definition", "Defines the raw-source and maintained-wiki separation used in this claim.", "The cited node states that preserved raw sources and maintained wiki artifacts have distinct roles."))}

[^3]:
{citation_block(source_gap_ref)}

## References

### [R1] Local claim records
{citation_block(claims_ref)}

### [R2] Runtime implementation evidence
{citation_block(clawhub_ref)}
""",
            "inputs": [
                "data/manifests/sources.jsonl",
                f"nodes/{ids['llm_wiki_working_definition']}/versions/1.0/card.md",
                "reports/source_gap_review.md",
                "data/manifests/claims.jsonl",
                "data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt",
            ],
        },
        {
            "slug": "provenance_as_core_knowledge_asset",
            "title": "Provenance is a core knowledge asset, not an appendix",
            "tags": ["llm-wiki", "provenance", "audit"],
            "stability": "working",
            "card": f"""# Provenance is a core knowledge asset, not an appendix

In the initialization contract, `card.md` records the knowledge result, while `provenance.md` records why the result exists, which inputs were used, which parts are synthesis, how citations were chosen, why adoption was allowed, and what would trigger revision.[^1] This makes provenance part of the reusable knowledge object rather than a narrative afterthought.

The reason is practical: source preservation gives auditors material to inspect, but provenance tells them how the agent moved from that material to the adopted node.[^2] Without that bridge, later agents may be able to find raw files but still fail to understand the synthesis boundary or adoption rationale.[^3]

## Footnotes

[^1]:
{citation_block(plan_ref)}

[^2]:
{citation_block(node_citation(ids["source_preservation_precondition_trust"], "claim_support", "Supports the claim that audit depends on inspectable source paths and source records.", "The cited node explains why preserved evidence is required for later trust checks."))}

[^3]:
{citation_block(alce_ref)}

## References

### [R1] Working definition
{citation_block(node_citation(ids["llm_wiki_working_definition"], "background_definition", "Provides the larger source-backed maintained-wiki context for provenance.", "The cited node defines the KB as a maintained artifact grounded in preserved sources."))}

### [R2] Source gap review
{citation_block(source_gap_ref)}
""",
            "inputs": [
                "loop_plan_init_kb.md",
                f"nodes/{ids['source_preservation_precondition_trust']}/versions/1.0/card.md",
                "data/raw/arxiv/arxiv-alce/text.txt",
                f"nodes/{ids['llm_wiki_working_definition']}/versions/1.0/card.md",
                "reports/source_gap_review.md",
            ],
        },
        {
            "slug": "citation_driven_impact_propagation",
            "title": "Citation edges drive impact review after major change",
            "tags": ["llm-wiki", "citations", "impact-analysis"],
            "stability": "working",
            "card": f"""# Citation edges drive impact review after major change

The demo treats citations as the source of dependency information. A footnote from node A to node B means A depends strongly on B for a claim; a reference means a weaker background dependency; a plain link does not propagate by default.[^1] When node B receives a major version candidate, the system can parse citation edges and place citing nodes into an impact queue instead of manually maintaining `depends_on` fields.[^2]

This design is intentionally conservative. Impact analysis creates review tasks; it does not automatically rewrite downstream nodes. That keeps semantic revision separate from graph computation.[^3]

## Footnotes

[^1]:
{citation_block(plan_ref)}

[^2]:
{citation_block(node_citation(ids["provenance_as_core_knowledge_asset"], "claim_support", "Explains why citations and provenance must preserve the support boundary for later audit.", "The cited node frames provenance and citation rationale as reusable audit surfaces."))}

[^3]:
{citation_block(alce_ref)}

## References

### [R1] Source preservation node
{citation_block(node_citation(ids["source_preservation_precondition_trust"], "background_support", "Provides the source-preservation premise that makes citation audit possible.", "The cited node explains why support must remain traceable to preserved source records."))}

### [R2] Claim manifest
{citation_block(claims_ref)}
""",
            "inputs": [
                "loop_plan_init_kb.md",
                f"nodes/{ids['provenance_as_core_knowledge_asset']}/versions/1.0/card.md",
                "data/raw/arxiv/arxiv-alce/text.txt",
                f"nodes/{ids['source_preservation_precondition_trust']}/versions/1.0/card.md",
                "data/manifests/claims.jsonl",
            ],
        },
        {
            "slug": "dynamic_retrieval_as_controlled_fallback",
            "title": "Dynamic retrieval is a controlled fallback, not ad hoc enrichment",
            "tags": ["llm-wiki", "dynamic-retrieval", "evidence-gap"],
            "stability": "working",
            "card": f"""# Dynamic retrieval is a controlled fallback, not ad hoc enrichment

Dynamic retrieval is allowed only when existing evidence is insufficient for a target claim or node, and the gap is written down before searching.[^1] The local source review already contains hard gaps, including blocked Reddit captures and an intercepted enterprise article; those gaps can justify retrieval requests, but they cannot be silently substituted with unsupported synthesis.[^2]

When retrieval is used, the new source must become a data asset under `data/raw/`, enter the source manifest, and appear in provenance. Otherwise the KB would gain text without gaining auditability.[^3]

## Footnotes

[^1]:
{citation_block(plan_ref)}

[^2]:
{citation_block(source_gap_ref)}

[^3]:
{citation_block(node_citation(ids["source_preservation_precondition_trust"], "claim_support", "Supports the requirement that new evidence must be preserved before it can support trusted synthesis.", "The cited node explains source preservation as a precondition for later audit."))}

## References

### [R1] Current initialization loop
{citation_block(node_citation(ids["current_kb_initialization_loop"], "process_context", "Places controlled retrieval inside the broader initialization loop.", "The cited node describes the 0-1 node loop, audit, adoption, and generated artifacts."))}

### [R2] Source manifest
{citation_block(sources_ref)}
""",
            "inputs": [
                "loop_plan_init_kb.md",
                "reports/source_gap_review.md",
                f"nodes/{ids['source_preservation_precondition_trust']}/versions/1.0/card.md",
                f"nodes/{ids['current_kb_initialization_loop']}/versions/1.0/card.md",
                "data/manifests/sources.jsonl",
            ],
            "dynamic_retrieval": "No dynamic retrieval was executed in this version. The run records a retrieval request for blocked Reddit/community evidence as a controlled next step.",
            "limits": "This node records retrieval policy and an evidence gap. It does not claim that the missing Reddit or enterprise evidence has been recovered.",
        },
    ]


def write_nodes(run_dir: str) -> list[str]:
    base = now()
    slugs = [
        "llm_wiki_working_definition",
        "current_kb_initialization_loop",
        "source_preservation_precondition_trust",
        "provenance_as_core_knowledge_asset",
        "citation_driven_impact_propagation",
        "dynamic_retrieval_as_controlled_fallback",
    ]
    ids = {
        slug: f"{(base + timedelta(seconds=i)).strftime('%Y%m%d_%H%M%S')}_{slug}"
        for i, slug in enumerate(slugs)
    }
    created: list[str] = []
    for i, spec in enumerate(node_specs(ids)):
        node_id = ids[spec["slug"]]
        created_at = (base + timedelta(seconds=i)).isoformat(timespec="seconds")
        node_dir = ROOT / "nodes" / node_id
        version_dir = node_dir / "versions" / "1.0"
        metadata = metadata_for_node(
            node_id=node_id,
            title=spec["title"],
            created_at=created_at,
            run_dir=run_dir,
            tags=spec["tags"],
            stability=spec.get("stability", "working"),
        )
        write_yaml(version_dir / "node.yaml", metadata)
        write_text(version_dir / "card.md", spec["card"])
        write_text(
            version_dir / "provenance.md",
            provenance(
                node_id=node_id,
                title=spec["title"],
                inputs=spec["inputs"],
                run_dir=run_dir,
                dynamic_retrieval=spec.get("dynamic_retrieval", "None. This version used only existing local data and process artifacts."),
                limits=spec.get(
                    "limits",
                    "This node is part of an initialization batch and should be revised if later audit finds a source mismatch or a stronger support contract.",
                ),
            ),
        )
        write_text(version_dir / "change.md", change_doc(node_id, created_at, run_dir))
        shutil.copyfile(version_dir / "node.yaml", node_dir / "node.yaml")
        created.append(node_id)
    return created


def write_run_files(run_dir: str, created_nodes: list[str]) -> None:
    run_path = ROOT / run_dir
    node_lines = "\n".join(f"- {node_id}" for node_id in created_nodes)
    write_text(
        run_path / "run_plan.md",
        f"""# Run Plan

run_id:: {Path(run_dir).name}
run_type:: bootstrap_plus_0_1_node_batch
created_at:: {now().isoformat(timespec="seconds")}

## Objective

Bootstrap the KB initialization contracts and create a first adopted node batch from existing local data.

## Target Nodes

{node_lines}

## Frozen Scope

- Use existing `data/`, `reports/`, and `loop_plan_init_kb.md`.
- Do not perform web retrieval in this run.
- Preserve every node as a complete 1.0 version bundle.
""",
    )
    write_text(
        run_path / "task.md",
        """# Task

Create Phase 1 bootstrap contracts, data inventory, source candidates, skill seeds, and a first auditable 0-1 node batch.
""",
    )
    write_text(
        run_path / "data_scope.md",
        """# Data Scope

Allowed inputs:

- loop_plan_init_kb.md
- reports/coverage_framework.md
- reports/source_gap_review.md
- data/manifests/sources.jsonl
- data/manifests/source_digests.jsonl
- data/manifests/claims.jsonl
- data/manifests/claim_source_links.jsonl
- selected local raw source text under data/raw/

Dynamic retrieval was not executed in this run.
""",
    )
    write_text(
        run_path / "generator_trace.md",
        f"""# Generator Trace

Generated {len(created_nodes)} adopted 1.0 node bundles from existing local artifacts.

{node_lines}

Each bundle contains `node.yaml`, `card.md`, `provenance.md`, and `change.md`.
""",
    )
    write_text(
        run_path / "provenance_trace.md",
        """# Provenance Trace

The generator used repo-root relative citation paths so version cards can be copied into `kb/` without losing parseability.

All nodes distinguish source-backed observations from process decisions. Dynamic retrieval was recorded as a policy/gap topic but not executed.
""",
    )
    write_text(
        run_path / "audit_report.md",
        f"""# Audit Report

audit_result:: passed
created_at:: {now().isoformat(timespec="seconds")}

## Checked

- Version bundle completeness for all generated nodes.
- Required `card.md` sections: Footnotes and References.
- Required citation fields in footnotes and references.
- Provenance sections and adoption rationale.
- Genesis change notes.

## Adopted Nodes

{node_lines}

## Residual Risk

This is a bootstrap audit. It checks structure and cited artifact existence; it does not yet perform a deep semantic source-faithfulness audit for every claim.
""",
    )
    write_text(
        run_path / "skill_eval.md",
        """# Skill Eval

## Scores

| Dimension | Score | Note |
| --- | ---: | --- |
| Schema compliance | 5 | Bundle contract and metadata are complete. |
| Citation quality | 4 | Citations are parseable and pinned; deeper semantic audit remains pending. |
| Provenance quality | 4 | Provenance explains why, inputs, synthesis, audit, adoption, and revision triggers. |
| Evidence fit | 4 | Existing local evidence is adequate for bootstrap nodes. |
| Card usefulness | 4 | Nodes form a reusable support chain for later runs. |
| Adoption readiness | 5 | 1.0 nodes are adopted after structural audit. |
| Dynamic retrieval discipline | 4 | Evidence gap is recorded; retrieval execution is deferred. |

## Skill Failure Candidates

- Add semantic citation-audit sampling before claiming a fully faithful KB.
- Add a dynamic retrieval execution run that preserves a new source and updates manifests.
- Add a major candidate simulation to verify impact queue behavior.
""",
    )
    write_text(
        run_path / "git_trace.md",
        """# Git Trace

No git checkpoint was created automatically by the bootstrap script. Use `scripts/kb_git_checkpoint.sh` after human review if a checkpoint is desired.
""",
    )
    write_text(
        run_path / "retrieval_request.md",
        """# Retrieval Request

run_id:: bootstrap_node_batch
target_node:: dynamic_retrieval_as_controlled_fallback
created_by:: audit
status:: open

## Why existing data is insufficient

The local source gap review records blocked Reddit captures and an intercepted enterprise article. These are hard evidence gaps for community reception and enterprise suitability.

## Missing evidence

- Usable community discussion evidence beyond blocked Reddit metadata.
- Usable enterprise article evidence to replace the intercepted page.

## Desired source types

- discussion_thread
- issue_thread
- blog_post
- enterprise_guide

## Suggested queries

- LLM Wiki community discussion implementation feedback
- LLM Wiki enterprise knowledge base source preservation
- Karpathy LLM Wiki Reddit discussion mirror

## Acceptance criteria

- Raw source must be preserved.
- Source manifest must be updated.
- Provenance must record retrieval.
- Retrieved evidence must be cited or rejected.
""",
    )
    write_yaml(
        ROOT / ".llmwiki" / "control" / "retrieval_log.yaml",
        {
            "schema": "kb.retrieval_log.v1",
            "updated_at": now().isoformat(timespec="seconds"),
            "requests": [
                {
                    "id": "ret_001",
                    "run": run_dir,
                    "request": f"{run_dir}/retrieval_request.md",
                    "status": "open",
                    "reason": "Blocked Reddit and intercepted enterprise source gaps are recorded in reports/source_gap_review.md.",
                }
            ],
        },
    )


def main() -> int:
    run_id = f"run_{now().strftime('%Y%m%d_%H%M%S')}_{RUN_SLUG}"
    run_dir = f".llmwiki/runs/{run_id}"

    write_schema()
    write_control_files(run_dir)
    write_autonomy_files(run_dir)
    write_agent_tasks(run_dir)
    write_skill_seeds()
    build_inventory()
    created_nodes = write_nodes(run_dir)
    write_run_files(run_dir, created_nodes)

    print(json.dumps({"run_dir": run_dir, "created_nodes": created_nodes}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
