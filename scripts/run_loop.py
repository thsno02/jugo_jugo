#!/usr/bin/env python3
"""Deterministic research-control loop for the LLM Wiki evidence repo."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]

OBJECTIVE_DOC = ROOT / "reports" / "coverage_framework.md"
LOOP_PLAN = ROOT / "loop_plan.md"
LOOP_MANIFEST = ROOT / "loop_manifest.json"
LOOP_STATE = ROOT / "loop_state.json"

SOURCES = ROOT / "data" / "manifests" / "sources.jsonl"
SOURCE_DIGESTS = ROOT / "data" / "manifests" / "source_digests.jsonl"
CLAIMS = ROOT / "data" / "manifests" / "claims.jsonl"
CLAIM_SOURCE_LINKS = ROOT / "data" / "manifests" / "claim_source_links.jsonl"
COVERAGE_RECORDS = ROOT / "data" / "manifests" / "coverage_records.jsonl"
SOURCE_DIGEST_INDEX = ROOT / "data" / "manifests" / "source_digests_index.md"

SEARCH_TASKS = ROOT / "data" / "discovery" / "search_tasks.jsonl"
CANDIDATES = ROOT / "data" / "discovery" / "candidate_sources.jsonl"
TRIAGE = ROOT / "data" / "discovery" / "triage_decisions.jsonl"

LOOP_EVENTS = ROOT / "data" / "logs" / "loop_events.jsonl"
ACQUISITION_FAILURES = ROOT / "data" / "logs" / "acquisition_failures.jsonl"
AUDIT_EVENTS = ROOT / "data" / "logs" / "audit_events.jsonl"
INACCESSIBLE_XML = ROOT / "data" / "logs" / "inaccessible_sources.xml"

ACQUISITION_STATUS = ROOT / "reports" / "acquisition_status.md"
COVERAGE_STATUS = ROOT / "reports" / "coverage_status.md"
EVIDENCE_MATRIX = ROOT / "reports" / "evidence_matrix.md"
JUDGMENT_STATUS = ROOT / "reports" / "judgment_status.md"
SOURCE_GAP_REVIEW = ROOT / "reports" / "source_gap_review.md"


COVERAGE_AREAS: list[dict[str, Any]] = [
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
            "minimal_example",
        ],
        "minimum_evidence": {
            "primary_sources": 1,
            "discussion_sources": 1,
            "implementation_sources": 1,
            "source_diversity": 3,
        },
        "preferred_source_types": [
            "primary_post",
            "gist",
            "x_mirror",
            "hacker_news_thread",
            "reddit_thread",
            "github_repo",
            "blog_post",
        ],
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
            "current_alternatives",
        ],
        "minimum_evidence": {
            "user_reports_or_discussions": 3,
            "implementation_sources": 3,
            "source_diversity": 4,
        },
        "preferred_source_types": [
            "discussion_thread",
            "blog_post",
            "repo_readme",
            "case_study",
            "issue_thread",
        ],
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
            "query_model",
        ],
        "minimum_evidence": {
            "implementation_sources": 10,
            "code_or_docs_sources": 5,
            "source_diversity": 5,
        },
        "preferred_source_types": ["github_repo", "readme", "documentation", "demo", "code"],
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
            "failure_handling",
        ],
        "minimum_evidence": {
            "workflow_examples": 5,
            "failure_examples": 3,
            "source_diversity": 4,
        },
        "preferred_source_types": ["repo", "docs", "issue_thread", "blog_post", "demo"],
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
            "benchmark_or_case_study_inventory",
        ],
        "minimum_evidence": {
            "benchmark_or_eval_sources": 3,
            "case_studies": 2,
            "baseline_comparisons": 3,
        },
        "preferred_source_types": [
            "paper",
            "benchmark",
            "case_study",
            "issue_thread",
            "evaluation_report",
        ],
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
            "interoperability_notes",
        ],
        "minimum_evidence": {
            "implementation_sources": 15,
            "tool_families": 5,
            "adoption_signal_sources": 5,
        },
        "preferred_source_types": [
            "github_repo",
            "plugin_listing",
            "package_registry",
            "docs",
            "community_post",
        ],
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
            "documentation_systems_comparison",
        ],
        "minimum_evidence": {
            "comparison_sources": 10,
            "adjacent_system_categories": 5,
            "source_diversity": 5,
        },
        "preferred_source_types": ["paper", "docs", "blog_post", "tool_docs", "benchmark"],
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
            "epistemic_risk",
        ],
        "minimum_evidence": {
            "risk_sources": 5,
            "failure_or_issue_sources": 3,
            "governance_sources": 3,
        },
        "preferred_source_types": [
            "issue_thread",
            "security_note",
            "governance_doc",
            "paper",
            "case_study",
        ],
    },
]


JUDGMENT_GATES: dict[str, dict[str, Any]] = {
    "descriptive": {
        "required_coverage_areas": ["origin_and_canon", "problem_and_motivation"],
        "minimum_status": "audited",
    },
    "technical": {
        "required_coverage_areas": [
            "architecture_and_data_model",
            "workflow_and_operations",
            "ecosystem_and_implementations",
        ],
        "minimum_status": "audited",
    },
    "empirical": {
        "required_coverage_areas": ["evaluation_and_evidence"],
        "minimum_status": "audited",
    },
    "strategic": {
        "required_coverage_areas": ["comparison_space", "risks_governance_ethics"],
        "minimum_status": "audited",
    },
    "research_paper": {
        "required_gates": ["descriptive", "technical", "empirical", "strategic"],
        "minimum_status": "passed",
    },
}


GLOBAL_INVARIANTS = [
    "no_claim_without_source_id",
    "no_source_without_manifest_record",
    "no_source_counted_without_raw_path_or_logged_failure",
    "no_coverage_area_completed_without_audit",
    "no_empirical_claim_without_baseline_or_method",
    "no_strategic_judgment_without_cost_risk_and_comparison",
    "contradictions_must_be_preserved",
    "blocked_sources_must_be_logged",
]


CLAIM_TEMPLATES: dict[str, dict[str, Any]] = {
    "origin_and_canon": {
        "required_outputs": [
            "original_karpathy_statement_exact_text",
            "original_date",
            "original_context",
            "examples_and_intended_workflow",
            "stated_or_implied_non_goals",
            "immediate_discussion_context",
            "early_forks_or_implementations",
            "minimal_example",
        ],
        "claim": (
            "The LLM Wiki pattern originates as a source-backed, LLM-maintained wiki workflow: immutable raw "
            "sources feed persistent Markdown/wiki artifacts governed by schema instructions and discussed in "
            "early social/community threads."
        ),
        "claim_type": "observed_fact",
        "confidence": "high",
        "evidence_grade": "A",
        "limitations": "Historical lineage before the viral Karpathy post remains only partially covered.",
    },
    "problem_and_motivation": {
        "required_outputs": [
            "workflow_failures_addressed",
            "user_groups",
            "definition_of_better",
            "current_alternatives",
        ],
        "claim": (
            "LLM Wiki sources frame the problem as repeated rediscovery in RAG/chat workflows, weak persistent "
            "memory, scattered PKM notes, and high human maintenance cost for long-lived knowledge bases."
        ),
        "claim_type": "interpretation",
        "confidence": "medium",
        "evidence_grade": "B",
        "limitations": "User pain is represented by launch discussion and implementation docs, not by a broad user study.",
    },
    "architecture_and_data_model": {
        "required_outputs": [
            "source_acquisition_model",
            "compilation_model",
            "storage_model",
            "link_model",
            "update_model",
            "query_model",
        ],
        "claim": (
            "Representative implementations converge on a raw-source layer, generated wiki/graph artifacts, "
            "metadata/index/log files, source-linked claims, and query/search interfaces via files, CLIs, apps, or MCP."
        ),
        "claim_type": "interpretation",
        "confidence": "high",
        "evidence_grade": "A",
        "limitations": "The taxonomy is derived from current repos and may change as the ecosystem matures.",
    },
    "workflow_and_operations": {
        "required_outputs": [
            "end_to_end_lifecycle",
            "human_in_loop_boundaries",
            "agent_interfaces",
            "failure_handling",
        ],
        "claim": (
            "The operational loop is source capture, raw preservation, readable extraction, digest/compile, "
            "claim mapping, report update, lint/audit, and human review where writes or uncertain claims matter."
        ),
        "claim_type": "interpretation",
        "confidence": "medium",
        "evidence_grade": "B",
        "limitations": "Failure handling is documented unevenly; blocked Reddit and network-intercepted sources remain explicit gaps.",
    },
    "evaluation_and_evidence": {
        "required_outputs": [
            "answer_quality_metrics",
            "maintenance_quality_metrics",
            "agent_usability_metrics",
            "robustness_metrics",
            "benchmark_or_case_study_inventory",
        ],
        "claim": (
            "Current empirical evidence is promising but weak: WiCER and knowledge-compounding papers provide "
            "benchmark-style claims, while most implementation outcomes remain author-reported or anecdotal."
        ),
        "claim_type": "evaluation_result",
        "confidence": "medium",
        "evidence_grade": "C",
        "limitations": "Independent replication, broader baselines, citation-fidelity audits, and longitudinal maintenance metrics are missing.",
    },
    "ecosystem_and_implementations": {
        "required_outputs": [
            "tool_family_inventory",
            "implementation_taxonomy",
            "adoption_signals",
            "interoperability_notes",
        ],
        "claim": (
            "The local corpus shows a fast-forming ecosystem across desktop apps, Obsidian/Claude/Codex skills, "
            "MCP servers, compilers, local-first projects, PyPI packages, and GitHub repositories with visible adoption signals."
        ),
        "claim_type": "observed_fact",
        "confidence": "high",
        "evidence_grade": "A",
        "limitations": "Stars and forks are adoption signals, not quality or sustained usage evidence.",
    },
    "comparison_space": {
        "required_outputs": [
            "rag_comparison",
            "pkm_comparison",
            "knowledge_graph_comparison",
            "agent_memory_comparison",
            "documentation_systems_comparison",
        ],
        "claim": (
            "LLM Wiki is best treated as a compilation-and-maintenance pattern adjacent to RAG, PKM, knowledge "
            "graphs, agent memory, and documentation systems rather than as a replacement for all of them."
        ),
        "claim_type": "strategic_judgment",
        "confidence": "medium",
        "evidence_grade": "C",
        "limitations": "Primary-source comparison coverage for modern RAG, graph RAG, and agent-memory systems remains incomplete.",
    },
    "risks_governance_ethics": {
        "required_outputs": [
            "provenance_risk",
            "maintenance_risk",
            "privacy_security_risk",
            "governance_model",
            "epistemic_risk",
        ],
        "claim": (
            "The main risks are provenance drift, stale or overgeneralized claims, privacy/security exposure, "
            "licensing ambiguity, prompt/source poisoning, and premature confidence in synthesized wiki pages."
        ),
        "claim_type": "strategic_judgment",
        "confidence": "medium",
        "evidence_grade": "C",
        "limitations": "Security, license, access-control, and enterprise governance evidence is not yet strong enough for a paper-level judgment.",
    },
}


COVERAGE_SOURCE_RULES: dict[str, list[str]] = {
    "origin_and_canon": ["karpathy", "hacker-news", "x-launch", "repo-astro", "repo-ss1024"],
    "problem_and_motivation": ["hacker-news", "guide", "blog", "repo-", "directory"],
    "architecture_and_data_model": ["repo-", "llm-wiki-net", "clawhub", "pypi", "arxiv-wicer"],
    "workflow_and_operations": ["repo-", "guide", "plugin", "clawhub", "obsidian"],
    "evaluation_and_evidence": [
        "arxiv",
        "evaluation",
        "benchmark",
        "ragas",
        "ares",
        "ragchecker",
        "longmemeval",
        "locomo",
        "openaitoolshub",
        "repo-atomicstrata",
        "repo-vectifyai",
        "repo-astro",
    ],
    "ecosystem_and_implementations": ["repo-", "pypi", "plugin", "directory", "clawhub", "obsidian"],
    "comparison_space": [
        "karpathy",
        "hacker-news",
        "arxiv",
        "robin",
        "guide",
        "repo-",
        "rag",
        "graphrag",
        "agent_memory",
        "knowledge_graph",
        "pkm",
        "docs_as_code",
        "wikibase",
    ],
    "risks_governance_ethics": [
        "hacker-news",
        "arxiv-memory",
        "source_gap_review",
        "repo-atomicstrata",
        "repo-kytmanov",
        "risk",
        "security",
        "governance",
        "poison",
        "owasp",
        "nist",
        "provenance",
        "privacy",
        "audit",
    ],
}


INACCESSIBLE_SOURCES = [
    {
        "id": "reddit-claudecode-plugin",
        "coverage_area": "ecosystem_and_implementations",
        "priority": "P0",
        "url": "https://www.reddit.com/r/ClaudeCode/comments/1sm374u/turned_andrej_karpathys_llm_wiki_gist_into_a/",
        "title": "Turned Andrej Karpathy's LLM Wiki gist into a Claude Code plugin",
        "attempted_method": "requests, Reddit JSON endpoint, old.reddit, browser capture",
        "failure_type": "blocked",
        "reason": "Reddit returned block/403 pages in local terminal and browser capture paths.",
        "impact": "Missing practitioner discussion around Claude Code plugin reception.",
        "next_retry_path": "Approved Reddit export/API, manual user export, or alternate network.",
    },
    {
        "id": "reddit-openkb-long-pdf",
        "coverage_area": "evaluation_and_evidence",
        "priority": "P0",
        "url": "https://www.reddit.com/r/LLMDevs/comments/1syz0b8/openkb_karpathys_idea_of_llm_wiki_but_with_the/",
        "title": "OpenKB: Karpathy's idea of LLM wiki, but with the long-PDF problem solved",
        "attempted_method": "requests, Reddit JSON endpoint, old.reddit, browser capture",
        "failure_type": "blocked",
        "reason": "Reddit returned block/403 pages in local terminal and browser capture paths.",
        "impact": "Missing evidence on long-PDF handling and OpenKB claims.",
        "next_retry_path": "Approved Reddit export/API, manual user export, or alternate network.",
    },
    {
        "id": "reddit-braindb",
        "coverage_area": "comparison_space",
        "priority": "P0",
        "url": "https://www.reddit.com/r/LLMDevs/comments/1sv5cl1/braindb_karpathys_llm_wiki_idea_but_as_a_real_db/",
        "title": "BrainDB: Karpathy's LLM wiki idea, but as a real DB",
        "attempted_method": "requests, Reddit JSON endpoint, old.reddit, browser capture",
        "failure_type": "blocked",
        "reason": "Reddit returned block/403 pages in local terminal and browser capture paths.",
        "impact": "Missing database-framing comparison evidence.",
        "next_retry_path": "Approved Reddit export/API, manual user export, or alternate network.",
    },
    {
        "id": "reddit-openwebui-llm-wiki",
        "coverage_area": "workflow_and_operations",
        "priority": "P1",
        "url": "https://www.reddit.com/r/OpenWebUI/comments/1sy0mf8/llm_wiki/",
        "title": "LLM Wiki discussion in OpenWebUI",
        "attempted_method": "requests, Reddit JSON endpoint, old.reddit, browser capture",
        "failure_type": "blocked",
        "reason": "Reddit returned block/403 pages in local terminal and browser capture paths.",
        "impact": "Missing OpenWebUI integration discussion.",
        "next_retry_path": "Approved Reddit export/API, manual user export, or alternate network.",
    },
    {
        "id": "reddit-obsidian-plugin",
        "coverage_area": "ecosystem_and_implementations",
        "priority": "P1",
        "url": "https://www.reddit.com/r/ObsidianMD/comments/1shntdn/new_plugin_llm_wiki_turn_your_vault_into_a/",
        "title": "New plugin: LLM Wiki - turn your vault into a queryable knowledge base",
        "attempted_method": "requests, Reddit JSON endpoint, old.reddit, browser capture",
        "failure_type": "blocked",
        "reason": "Reddit returned block/403 pages in local terminal and browser capture paths.",
        "impact": "Missing Obsidian community feedback.",
        "next_retry_path": "Approved Reddit export/API, manual user export, or alternate network.",
    },
    {
        "id": "reddit-visuals-pdfs-question",
        "coverage_area": "workflow_and_operations",
        "priority": "P1",
        "url": "https://www.reddit.com/r/ClaudeCode/comments/1so9gbt/does_the_karpathystyle_llm_wiki_actually_handle/",
        "title": "Does the Karpathy-style LLM Wiki handle visuals/PDFs/PowerPoints?",
        "attempted_method": "requests, Reddit JSON endpoint, old.reddit, browser capture",
        "failure_type": "blocked",
        "reason": "Reddit returned block/403 pages in local terminal and browser capture paths.",
        "impact": "Missing multimodal/PDF/PPT handling discussion.",
        "next_retry_path": "Approved Reddit export/API, manual user export, or alternate network.",
    },
    {
        "id": "aicritique-enterprise-knowledge",
        "coverage_area": "risks_governance_ethics",
        "priority": "P1",
        "url": "https://www.aicritique.org/us/2026/05/08/andrej-karpathys-latest-concept-llm-wiki-and-the-future-of-enterprise-knowledge/",
        "title": "Andrej Karpathy's latest concept LLM Wiki and the future of enterprise knowledge",
        "attempted_method": "requests and curl fallback",
        "failure_type": "network_intercepted",
        "reason": "Local network intercepted the URL with an office-sec block page.",
        "impact": "Missing enterprise-knowledge article body.",
        "next_retry_path": "Alternate network, web archive, or replacement enterprise primary source.",
    },
]


P0_SEARCH_TASKS = [
    {
        "search_task_id": "search_evaluation_000001",
        "coverage_id": "evaluation_and_evidence",
        "missing_outputs": [
            "answer_quality_metrics",
            "maintenance_quality_metrics",
            "benchmark_or_case_study_inventory",
        ],
        "queries": [
            "\"LLM Wiki\" benchmark evaluation",
            "\"wiki memory\" \"RAG\" benchmark LLM",
            "\"citation fidelity\" \"agent memory\" evaluation",
            "\"LLM-maintained wiki\" case study",
        ],
        "target_source_types": ["paper", "benchmark", "case_study", "evaluation_report"],
        "success_criteria": [
            "Find explicit baselines against RAG or no-memory systems.",
            "Find maintenance or citation-fidelity metrics.",
            "Find at least one reproducible case study.",
        ],
        "status": "open",
    },
    {
        "search_task_id": "search_comparison_000001",
        "coverage_id": "comparison_space",
        "missing_outputs": [
            "rag_comparison",
            "knowledge_graph_comparison",
            "agent_memory_comparison",
        ],
        "queries": [
            "\"agent memory\" RAG comparison",
            "\"GraphRAG\" \"agent memory\" evaluation",
            "\"MemGPT\" \"RAG\" memory comparison",
            "\"Zep\" \"Mem0\" \"agent memory\" benchmark",
        ],
        "target_source_types": ["paper", "docs", "benchmark", "tool_docs"],
        "success_criteria": [
            "Cover modern RAG, GraphRAG, and agent memory systems.",
            "Preserve advantages and limitations of simpler alternatives.",
        ],
        "status": "open",
    },
    {
        "search_task_id": "search_risks_000001",
        "coverage_id": "risks_governance_ethics",
        "missing_outputs": [
            "privacy_security_risk",
            "governance_model",
            "epistemic_risk",
        ],
        "queries": [
            "\"agent memory\" privacy risk",
            "\"RAG\" source poisoning prompt injection",
            "\"LLM\" knowledge base provenance governance",
            "\"AI memory\" enterprise governance audit log",
        ],
        "target_source_types": ["paper", "security_note", "governance_doc", "case_study"],
        "success_criteria": [
            "Find actionable governance requirements.",
            "Find concrete poisoning, privacy, or provenance failure modes.",
        ],
        "status": "open",
    },
]


CANDIDATE_SOURCE_SEEDS: list[dict[str, Any]] = [
    {
        "source_id": "arxiv-ragas",
        "coverage_id": "evaluation_and_evidence",
        "task_ids": ["search_evaluation_000001"],
        "type": "arxiv",
        "title": "RAGAS: Automated Evaluation of Retrieval Augmented Generation",
        "url": "https://arxiv.org/abs/2309.15217",
        "arxiv_id": "2309.15217",
        "priority": "p0",
        "tags": ["paper", "rag", "evaluation", "metrics", "output:answer_quality_metrics", "output:robustness_metrics", "output:benchmark_or_case_study_inventory"],
        "relevance_reason": "Defines reference-free metrics for evaluating RAG context relevance, faithfulness, and answer quality.",
    },
    {
        "source_id": "arxiv-alce",
        "coverage_id": "evaluation_and_evidence",
        "task_ids": ["search_evaluation_000001", "search_risks_000001"],
        "type": "arxiv",
        "title": "Enabling Large Language Models to Generate Text with Citations",
        "url": "https://arxiv.org/abs/2305.14627",
        "arxiv_id": "2305.14627",
        "priority": "p0",
        "tags": ["paper", "citation", "evaluation", "provenance", "output:answer_quality_metrics", "output:robustness_metrics", "output:provenance_risk", "output:epistemic_risk"],
        "relevance_reason": "Provides ALCE citation-quality metrics and evidence for citation-support failure modes.",
    },
    {
        "source_id": "arxiv-ares",
        "coverage_id": "evaluation_and_evidence",
        "task_ids": ["search_evaluation_000001"],
        "type": "arxiv",
        "title": "ARES: An Automated Evaluation Framework for Retrieval-Augmented Generation Systems",
        "url": "https://arxiv.org/abs/2311.09476",
        "arxiv_id": "2311.09476",
        "priority": "p0",
        "tags": ["paper", "rag", "evaluation", "benchmark", "output:answer_quality_metrics", "output:robustness_metrics", "output:benchmark_or_case_study_inventory"],
        "relevance_reason": "Evaluates RAG context relevance, answer faithfulness, answer relevance, and domain shift.",
    },
    {
        "source_id": "repo-stanford-ares",
        "coverage_id": "evaluation_and_evidence",
        "task_ids": ["search_evaluation_000001"],
        "type": "github_repo",
        "title": "ARES replication code and datasets",
        "url": "https://github.com/stanford-futuredata/ARES",
        "repo": "stanford-futuredata/ARES",
        "priority": "p0",
        "tags": ["github_repo", "evaluation", "benchmark", "reproducibility", "output:benchmark_or_case_study_inventory", "output:robustness_metrics"],
        "relevance_reason": "Implementation and datasets for a RAG evaluation framework.",
    },
    {
        "source_id": "arxiv-ragchecker",
        "coverage_id": "evaluation_and_evidence",
        "task_ids": ["search_evaluation_000001"],
        "type": "arxiv",
        "title": "RAGChecker: A Fine-grained Framework for Diagnosing Retrieval-Augmented Generation",
        "url": "https://arxiv.org/abs/2408.08067",
        "arxiv_id": "2408.08067",
        "priority": "p0",
        "tags": ["paper", "rag", "evaluation", "benchmark", "diagnostics", "output:answer_quality_metrics", "output:robustness_metrics", "output:benchmark_or_case_study_inventory"],
        "relevance_reason": "Fine-grained diagnostic metrics for retrieval and generation modules, with human-correlation evidence.",
    },
    {
        "source_id": "repo-amazon-ragchecker",
        "coverage_id": "evaluation_and_evidence",
        "task_ids": ["search_evaluation_000001"],
        "type": "github_repo",
        "title": "RAGChecker source code",
        "url": "https://github.com/amazon-science/RAGChecker",
        "repo": "amazon-science/RAGChecker",
        "priority": "p0",
        "tags": ["github_repo", "evaluation", "benchmark", "diagnostics", "output:benchmark_or_case_study_inventory", "output:robustness_metrics"],
        "relevance_reason": "Open-source code for reproducing RAGChecker diagnostics.",
    },
    {
        "source_id": "arxiv-longmemeval",
        "coverage_id": "evaluation_and_evidence",
        "task_ids": ["search_evaluation_000001", "search_comparison_000001"],
        "type": "arxiv",
        "title": "LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory",
        "url": "https://arxiv.org/abs/2410.10813",
        "arxiv_id": "2410.10813",
        "priority": "p0",
        "tags": ["paper", "agent_memory", "benchmark", "long_term_memory", "output:agent_usability_metrics", "output:maintenance_quality_metrics", "output:benchmark_or_case_study_inventory", "output:agent_memory_comparison"],
        "relevance_reason": "Benchmark for long-term chat memory abilities: extraction, multi-session reasoning, temporal reasoning, updates, and abstention.",
    },
    {
        "source_id": "repo-longmemeval",
        "coverage_id": "evaluation_and_evidence",
        "task_ids": ["search_evaluation_000001", "search_comparison_000001"],
        "type": "github_repo",
        "title": "LongMemEval benchmark repository",
        "url": "https://github.com/xiaowu0162/LongMemEval",
        "repo": "xiaowu0162/LongMemEval",
        "priority": "p0",
        "tags": ["github_repo", "agent_memory", "benchmark", "long_term_memory", "output:agent_usability_metrics", "output:benchmark_or_case_study_inventory", "output:agent_memory_comparison"],
        "relevance_reason": "Benchmark data and code for long-term memory evaluation.",
    },
    {
        "source_id": "arxiv-locomo",
        "coverage_id": "evaluation_and_evidence",
        "task_ids": ["search_evaluation_000001", "search_comparison_000001"],
        "type": "arxiv",
        "title": "Evaluating Very Long-Term Conversational Memory of LLM Agents",
        "url": "https://arxiv.org/abs/2402.17753",
        "arxiv_id": "2402.17753",
        "priority": "p0",
        "tags": ["paper", "agent_memory", "benchmark", "locomo", "output:agent_usability_metrics", "output:benchmark_or_case_study_inventory", "output:agent_memory_comparison"],
        "relevance_reason": "Introduces LoCoMo-style evaluation for long-term conversational memory.",
    },
    {
        "source_id": "arxiv-mem0",
        "coverage_id": "comparison_space",
        "task_ids": ["search_evaluation_000001", "search_comparison_000001"],
        "type": "arxiv",
        "title": "Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory",
        "url": "https://arxiv.org/abs/2504.19413",
        "arxiv_id": "2504.19413",
        "priority": "p0",
        "tags": ["paper", "agent_memory", "benchmark", "baseline", "output:agent_usability_metrics", "output:maintenance_quality_metrics", "output:benchmark_or_case_study_inventory", "output:agent_memory_comparison"],
        "relevance_reason": "Compares memory approaches against RAG, full-context, and memory-system baselines on LOCOMO.",
    },
    {
        "source_id": "arxiv-zep",
        "coverage_id": "comparison_space",
        "task_ids": ["search_evaluation_000001", "search_comparison_000001"],
        "type": "arxiv",
        "title": "Zep: A Temporal Knowledge Graph Architecture for Agent Memory",
        "url": "https://arxiv.org/abs/2501.13956",
        "arxiv_id": "2501.13956",
        "priority": "p0",
        "tags": ["paper", "agent_memory", "knowledge_graph", "benchmark", "output:agent_usability_metrics", "output:benchmark_or_case_study_inventory", "output:agent_memory_comparison", "output:knowledge_graph_comparison"],
        "relevance_reason": "Primary source for temporal knowledge graph memory and DMR/LongMemEval comparisons.",
    },
    {
        "source_id": "arxiv-lightmem",
        "coverage_id": "comparison_space",
        "task_ids": ["search_evaluation_000001", "search_comparison_000001"],
        "type": "arxiv",
        "title": "LightMem: Lightweight and Efficient Memory-Augmented Generation",
        "url": "https://arxiv.org/abs/2510.18866",
        "arxiv_id": "2510.18866",
        "priority": "p0",
        "tags": ["paper", "agent_memory", "efficiency", "benchmark", "output:agent_usability_metrics", "output:maintenance_quality_metrics", "output:benchmark_or_case_study_inventory", "output:agent_memory_comparison"],
        "relevance_reason": "Adds efficiency and cost metrics for memory-augmented generation on LongMemEval.",
    },
    {
        "source_id": "arxiv-memgpt",
        "coverage_id": "comparison_space",
        "task_ids": ["search_comparison_000001"],
        "type": "arxiv",
        "title": "MemGPT: Towards LLMs as Operating Systems",
        "url": "https://arxiv.org/abs/2310.08560",
        "arxiv_id": "2310.08560",
        "priority": "p0",
        "tags": ["paper", "agent_memory", "baseline", "output:agent_memory_comparison", "output:rag_comparison"],
        "relevance_reason": "Canonical memory-tier design and baseline for later agent-memory systems.",
    },
    {
        "source_id": "arxiv-graphrag",
        "coverage_id": "comparison_space",
        "task_ids": ["search_comparison_000001"],
        "type": "arxiv",
        "title": "From Local to Global: A Graph RAG Approach to Query-Focused Summarization",
        "url": "https://arxiv.org/abs/2404.16130",
        "arxiv_id": "2404.16130",
        "priority": "p0",
        "tags": ["paper", "rag", "graphrag", "knowledge_graph", "output:rag_comparison", "output:knowledge_graph_comparison"],
        "relevance_reason": "Primary GraphRAG paper comparing graph-based global sensemaking against naive RAG.",
    },
    {
        "source_id": "repo-microsoft-graphrag",
        "coverage_id": "comparison_space",
        "task_ids": ["search_comparison_000001"],
        "type": "github_repo",
        "title": "Microsoft GraphRAG implementation",
        "url": "https://github.com/microsoft/graphrag",
        "repo": "microsoft/graphrag",
        "priority": "p0",
        "tags": ["github_repo", "rag", "graphrag", "knowledge_graph", "output:rag_comparison", "output:knowledge_graph_comparison"],
        "relevance_reason": "Implementation source for graph-based RAG pipeline and documentation.",
    },
    {
        "source_id": "langchain-long-term-memory-docs",
        "coverage_id": "comparison_space",
        "task_ids": ["search_comparison_000001"],
        "type": "webpage",
        "title": "LangChain long-term memory documentation",
        "url": "https://docs.langchain.com/oss/python/langchain/long-term-memory",
        "priority": "p0",
        "tags": ["documentation", "agent_memory", "langgraph", "output:agent_memory_comparison"],
        "relevance_reason": "Primary docs for mainstream agent long-term memory implementation patterns.",
    },
    {
        "source_id": "writethedocs-docs-as-code",
        "coverage_id": "comparison_space",
        "task_ids": ["search_comparison_000001"],
        "type": "webpage",
        "title": "Docs as Code - Write the Docs",
        "url": "https://www.writethedocs.org/guide/docs-as-code.html",
        "priority": "p0",
        "tags": ["documentation", "docs_as_code", "workflow", "output:documentation_systems_comparison"],
        "relevance_reason": "Canonical docs-as-code comparison point for source-control, review, CI, and publishing workflows.",
    },
    {
        "source_id": "obsidian-help-link-notes",
        "coverage_id": "comparison_space",
        "task_ids": ["search_comparison_000001"],
        "type": "webpage",
        "title": "Obsidian Help: Link notes",
        "url": "https://help.obsidian.md/link-notes",
        "priority": "p0",
        "tags": ["documentation", "pkm", "obsidian", "backlinks", "output:pkm_comparison"],
        "relevance_reason": "Primary PKM documentation for note links/backlinks as an adjacent knowledge-base model.",
    },
    {
        "source_id": "wikibase-data-model",
        "coverage_id": "comparison_space",
        "task_ids": ["search_comparison_000001"],
        "type": "webpage",
        "title": "Wikibase DataModel",
        "url": "https://www.mediawiki.org/wiki/Wikibase/DataModel",
        "priority": "p0",
        "tags": ["documentation", "knowledge_graph", "provenance", "output:knowledge_graph_comparison", "output:provenance_risk"],
        "relevance_reason": "Primary source for statements, references, and provenance in Wikibase-style knowledge graphs.",
    },
    {
        "source_id": "arxiv-poisonedrag",
        "coverage_id": "risks_governance_ethics",
        "task_ids": ["search_risks_000001"],
        "type": "arxiv",
        "title": "PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models",
        "url": "https://arxiv.org/abs/2402.07867",
        "arxiv_id": "2402.07867",
        "priority": "p0",
        "tags": ["paper", "security", "poisoning", "rag", "output:privacy_security_risk", "output:provenance_risk", "output:epistemic_risk"],
        "relevance_reason": "Primary RAG knowledge-poisoning attack paper and concrete threat model.",
    },
    {
        "source_id": "arxiv-graph-poisoning",
        "coverage_id": "risks_governance_ethics",
        "task_ids": ["search_risks_000001", "search_comparison_000001"],
        "type": "arxiv",
        "title": "A Few Words Can Distort Graphs: Knowledge Poisoning Attacks on Graph-based RAG",
        "url": "https://arxiv.org/abs/2508.04276",
        "arxiv_id": "2508.04276",
        "priority": "p0",
        "tags": ["paper", "security", "poisoning", "graphrag", "knowledge_graph", "output:privacy_security_risk", "output:provenance_risk", "output:knowledge_graph_comparison"],
        "relevance_reason": "GraphRAG-specific poisoning evidence for graph construction and downstream reasoning risks.",
    },
    {
        "source_id": "arxiv-etamp-memory-poisoning",
        "coverage_id": "risks_governance_ethics",
        "task_ids": ["search_risks_000001"],
        "type": "arxiv",
        "title": "Poison Once, Exploit Forever: Environment-Injected Memory Poisoning Attacks on Web Agents",
        "url": "https://arxiv.org/abs/2604.02623",
        "arxiv_id": "2604.02623",
        "priority": "p0",
        "tags": ["paper", "security", "memory_poisoning", "agent_memory", "output:privacy_security_risk", "output:maintenance_risk", "output:epistemic_risk"],
        "relevance_reason": "Recent agent-memory poisoning attack showing persistent cross-session compromise.",
    },
    {
        "source_id": "owasp-llm-top10-2025",
        "coverage_id": "risks_governance_ethics",
        "task_ids": ["search_risks_000001"],
        "type": "webpage",
        "title": "OWASP Top 10 for LLM Applications 2025",
        "url": "https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/",
        "priority": "p0",
        "tags": ["governance", "security", "owasp", "prompt_injection", "data_poisoning", "output:privacy_security_risk", "output:governance_model", "output:epistemic_risk"],
        "relevance_reason": "Vendor-neutral security taxonomy for prompt injection, data/model poisoning, supply chain, and excessive agency.",
    },
    {
        "source_id": "owasp-agentic-top10-2026",
        "coverage_id": "risks_governance_ethics",
        "task_ids": ["search_risks_000001"],
        "type": "webpage",
        "title": "OWASP Top 10 for Agentic Applications 2026",
        "url": "https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/",
        "priority": "p0",
        "tags": ["governance", "security", "owasp", "agentic", "memory_poisoning", "output:privacy_security_risk", "output:governance_model", "output:maintenance_risk"],
        "relevance_reason": "Agent-specific security taxonomy including memory/context poisoning and autonomous tool-use risks.",
    },
    {
        "source_id": "nist-gai-profile",
        "coverage_id": "risks_governance_ethics",
        "task_ids": ["search_risks_000001"],
        "type": "webpage",
        "title": "NIST AI RMF Generative AI Profile",
        "url": "https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence",
        "priority": "p0",
        "tags": ["governance", "risk_management", "nist", "provenance", "output:governance_model", "output:provenance_risk", "output:privacy_security_risk"],
        "relevance_reason": "Primary governance framework for generative AI lifecycle risk management.",
    },
    {
        "source_id": "microsoft-agent-governance-toolkit-docs",
        "coverage_id": "risks_governance_ethics",
        "task_ids": ["search_risks_000001"],
        "type": "webpage",
        "title": "Microsoft Agent Governance Toolkit documentation",
        "url": "https://microsoft.github.io/agent-governance-toolkit/",
        "priority": "p0",
        "tags": ["governance", "security", "agent", "audit_log", "output:governance_model", "output:maintenance_risk", "output:privacy_security_risk"],
        "relevance_reason": "Operational governance reference for policy checks, identity, sandboxing, SRE, and audit logging.",
    },
    {
        "source_id": "repo-microsoft-agent-governance-toolkit",
        "coverage_id": "risks_governance_ethics",
        "task_ids": ["search_risks_000001"],
        "type": "github_repo",
        "title": "Microsoft Agent Governance Toolkit repository",
        "url": "https://github.com/microsoft/agent-governance-toolkit",
        "repo": "microsoft/agent-governance-toolkit",
        "priority": "p0",
        "tags": ["github_repo", "governance", "security", "audit_log", "output:governance_model", "output:maintenance_risk", "output:privacy_security_risk"],
        "relevance_reason": "Implementation source for an agent governance layer and audit/compliance controls.",
    },
]


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def sha256_text(text: str) -> str:
    return "sha256:" + hashlib.sha256(text.encode("utf-8")).hexdigest()


def sha256_file(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def read_text(path: Path, limit: int | None = None) -> str:
    data = path.read_text(encoding="utf-8", errors="replace")
    return data if limit is None else data[:limit]


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows), encoding="utf-8")


def append_jsonl(path: Path, row: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def ensure_empty_jsonl(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text("", encoding="utf-8")


def load_sources() -> list[dict[str, Any]]:
    rows = read_jsonl(SOURCES)
    normalized = []
    for row in rows:
        source_id = row["source_id"]
        local_dir = ROOT / row.get("local_dir", "")
        raw_path = row.get("local_dir") if local_dir.exists() else None
        row = dict(row)
        row.setdefault("source_id", source_id)
        row["raw_path"] = raw_path
        row["date_accessed"] = row.get("fetched_at", "")[:10] or "unknown"
        row["acquisition_status"] = "success" if row.get("status") == "ok" else row.get("status", "unknown")
        row["content_hash"] = digest_source_dir(local_dir) if local_dir.exists() else None
        normalized.append(row)
    return normalized


def digest_source_dir(path: Path) -> str | None:
    if not path.exists():
        return None
    hasher = hashlib.sha256()
    count = 0
    for file_path in sorted(p for p in path.rglob("*") if p.is_file()):
        if ".git" in file_path.parts:
            continue
        try:
            hasher.update(str(file_path.relative_to(path)).encode("utf-8"))
            hasher.update(file_path.read_bytes()[:2_000_000])
            count += 1
        except OSError:
            continue
    return "sha256:" + hasher.hexdigest() if count else None


def compile_manifest() -> dict[str, Any]:
    objective_text = OBJECTIVE_DOC.read_text(encoding="utf-8") if OBJECTIVE_DOC.exists() else ""
    loop_plan_text = LOOP_PLAN.read_text(encoding="utf-8") if LOOP_PLAN.exists() else ""
    return {
        "objective_name": "LLM Wiki Coverage Framework",
        "objective_doc": rel(OBJECTIVE_DOC),
        "objective_version": "2026-05-21",
        "objective_hash": sha256_text(objective_text),
        "loop_plan": rel(LOOP_PLAN),
        "loop_plan_hash": sha256_text(loop_plan_text),
        "default_loop_policy": {
            "source_first": True,
            "raw_preservation_required": True,
            "claim_source_mapping_required": True,
            "audit_required_before_completion": True,
            "unsupported_claim_policy": "downgrade_to_hypothesis_or_remove",
            "inaccessible_sources_xml_required": True,
            "verify_is_structural_only": True,
            "satisfaction_command_required_to_stop": True,
            "blocked_sources_do_not_count_as_evidence": True,
            "completion_requires_research_paper_gate": True,
        },
        "completion_policy": {
            "stop_command": "python3 scripts/run_loop.py satisfaction",
            "required_gate": "research_paper",
            "required_area_status": "supported",
            "required_audit_status": "pass",
            "required_output_status": "supported",
            "queue_policy": "all_empty",
            "inaccessible_source_policy": "must_be_logged_but_must_not_substitute_for_evidence",
        },
        "coverage_areas": [
            {
                **area,
                "acceptance_tests": acceptance_tests(area["id"]),
            }
            for area in COVERAGE_AREAS
        ],
        "judgment_gates": JUDGMENT_GATES,
        "global_invariants": GLOBAL_INVARIANTS,
        "required_files": [
            rel(SOURCE_DIGESTS),
            rel(CLAIMS),
            rel(CLAIM_SOURCE_LINKS),
            rel(COVERAGE_RECORDS),
            rel(INACCESSIBLE_XML),
            rel(AUDIT_EVENTS),
            rel(COVERAGE_STATUS),
            rel(EVIDENCE_MATRIX),
            rel(JUDGMENT_STATUS),
        ],
        "generated_at": now(),
    }


def acceptance_tests(area_id: str) -> list[str]:
    common = ["all_claims_have_source_links", "blocked_sources_logged", "audit_passed_or_not_ready_with_reason"]
    tests = {
        "origin_and_canon": [
            "exact_origin_claim_has_primary_or_near_primary_source",
            "date_and_context_are_recorded",
            "early_discussion_is_preserved_or_blocked_with_reason",
            "minimal_example_is_described_from_sources",
        ],
        "problem_and_motivation": [
            "each_motivation_has_at_least_one_source",
            "user_groups_are_not_invented",
            "benefit_claims_are_marked_as_observed_or_hypothetical",
        ],
        "architecture_and_data_model": [
            "at_least_ten_implementations_classified",
            "each_architecture_dimension_has_evidence",
            "source_preservation_and_query_models_are_distinguished",
        ],
        "workflow_and_operations": [
            "agent_permissions_are_described",
            "failure_handling_is_not_purely_speculative",
            "blocked_sources_are_logged",
        ],
        "evaluation_and_evidence": [
            "raw_rag_baseline_is_defined",
            "chat_memory_baseline_is_defined",
            "no_empirical_claim_without_method",
        ],
        "ecosystem_and_implementations": [
            "implementations_are_not_all_same_family",
            "adoption_signals_are_separated_from_quality_claims",
            "repo_metadata_is_recorded",
        ],
        "comparison_space": [
            "each_adjacent_system_has_advantages_and_limitations",
            "claims_about_difference_are_source_backed",
            "simpler_alternatives_are_not_dismissed_without_evidence",
        ],
        "risks_governance_ethics": [
            "risk_claims_are_tied_to_failure_or_threat_model",
            "privacy_and_license_risks_are_separated",
            "governance_requirements_are_actionable",
        ],
    }
    return tests.get(area_id, []) + common


def source_text_path(source: dict[str, Any]) -> Path | None:
    files = source.get("files", {})
    for key in [
        "agent_source_bundle.txt",
        "text.txt",
        "browser_text.txt",
        "README.remote",
        "raw.txt",
    ]:
        if key in files:
            path = ROOT / files[key]
            if path.exists():
                return path
    local_dir = ROOT / source.get("local_dir", "")
    candidates = [
        local_dir / "agent_source_bundle.txt",
        local_dir / "text.txt",
        local_dir / "browser_text.txt",
        local_dir / "repo" / "README.md",
        local_dir / "README.remote",
        local_dir / "raw.txt",
    ]
    for path in candidates:
        if path.exists():
            return path
    return None


def source_title(source: dict[str, Any]) -> str:
    source_id = source["source_id"]
    seed_path = ROOT / "data" / "manifests" / "seed_sources.json"
    if seed_path.exists():
        for item in read_json(seed_path):
            if item.get("id") == source_id:
                return item.get("title") or source_id
    return source_id


def source_digest(source: dict[str, Any]) -> dict[str, Any]:
    path = source_text_path(source)
    local_dir = ROOT / source.get("local_dir", "")
    text = read_text(path, 24_000) if path else ""
    coverage = map_source_to_coverage(source)
    limitations = []
    if source.get("status") != "ok":
        limitations.append(f"Acquisition status is {source.get('status')}: {source.get('error') or 'no error detail'}")
    if not path:
        limitations.append("No readable local text path found; source is retained as raw/pending.")
    if source.get("source_type") == "github_repo":
        limitations.append("Digest uses README/metadata-level evidence; full source-code audit remains pending.")
    if source.get("source_type") == "arxiv" and "source.pdf" in source.get("files", {}):
        limitations.append("arXiv e-print returned PDF-only source; TeX bundle unavailable locally.")

    observations = observations_for_source(source, text)
    return {
        "digest_id": "digest_" + source["source_id"],
        "source_id": source["source_id"],
        "created_at": now(),
        "coverage_areas": coverage,
        "title": source_title(source),
        "source_type": source.get("source_type"),
        "raw_path": source.get("raw_path") or source.get("local_dir"),
        "readable_text_path": rel(path) if path else None,
        "content_hash": source.get("content_hash"),
        "source_summary": summarize_text(text, source),
        "key_observations": observations,
        "supported_outputs": source_supported_outputs(source, coverage),
        "possible_claims": possible_claims_for_coverage(coverage, source),
        "limitations": limitations or ["No major limitation recorded at digest granularity."],
        "digest_status": "complete" if path and source.get("status") == "ok" else "pending_or_blocked",
    }


def summarize_text(text: str, source: dict[str, Any]) -> str:
    if not text:
        return f"No readable text available for {source['source_id']}; use raw files and failure metadata."
    clean = re.sub(r"\s+", " ", text).strip()
    return clean[:900] + ("..." if len(clean) > 900 else "")


def observations_for_source(source: dict[str, Any], text: str) -> list[dict[str, str]]:
    source_id = source["source_id"]
    lowered = text.lower()
    observations: list[dict[str, str]] = []
    signals = [
        ("raw sources", "Mentions raw source preservation or source-first workflow."),
        ("wiki", "Mentions persistent wiki artifacts or wiki-style storage."),
        ("rag", "Mentions RAG as comparison or baseline."),
        ("citation", "Mentions citations, provenance, or source-backed claims."),
        ("benchmark", "Mentions benchmark or evaluation evidence."),
        ("risk", "Mentions risk, limitation, drift, privacy, or governance."),
        ("mcp", "Mentions MCP or tool interface integration."),
        ("obsidian", "Mentions Obsidian or PKM workflow."),
        ("graph", "Mentions graph, backlinks, or concept linking."),
    ]
    for needle, observation in signals:
        if needle in lowered:
            observations.append(
                {
                    "observation": observation,
                    "local_evidence": source_id,
                    "relevance": "Supports one or more mapped coverage areas.",
                }
            )
    if not observations:
        observations.append(
            {
                "observation": "Source preserved for coverage review; no keyword-level observation extracted.",
                "local_evidence": source_id,
                "relevance": "Pending deeper manual or targeted digest.",
            }
        )
    return observations[:6]


def map_source_to_coverage(source: dict[str, Any]) -> list[str]:
    source_id = source["source_id"]
    haystack = " ".join(
        [
            source_id,
            source.get("source_type", ""),
            " ".join(source.get("tags", [])),
            source_title(source),
        ]
    ).lower()
    mapped: list[str] = []
    for coverage_id, needles in COVERAGE_SOURCE_RULES.items():
        if any(needle in haystack for needle in needles):
            mapped.append(coverage_id)
    if source.get("source_type") == "github_repo":
        for coverage_id in [
            "architecture_and_data_model",
            "workflow_and_operations",
            "ecosystem_and_implementations",
        ]:
            if coverage_id not in mapped:
                mapped.append(coverage_id)
    if source.get("source_type") in {"arxiv"}:
        for coverage_id in ["evaluation_and_evidence", "comparison_space", "risks_governance_ethics"]:
            if coverage_id not in mapped:
                mapped.append(coverage_id)
    if not mapped:
        mapped.append("problem_and_motivation")
    return mapped


def supported_outputs_for_coverage(coverage: list[str]) -> list[str]:
    outputs: list[str] = []
    by_id = {area["id"]: area for area in COVERAGE_AREAS}
    for coverage_id in coverage:
        outputs.extend(by_id[coverage_id]["required_outputs"])
    return sorted(set(outputs))


def source_supported_outputs(source: dict[str, Any], coverage: list[str]) -> list[str]:
    explicit_outputs = [
        tag.split(":", 1)[1]
        for tag in source.get("tags", [])
        if isinstance(tag, str) and tag.startswith("output:")
    ]
    if explicit_outputs:
        valid_outputs = {output for area in COVERAGE_AREAS for output in area["required_outputs"]}
        return sorted({output for output in explicit_outputs if output in valid_outputs})
    return supported_outputs_for_coverage(coverage)


def possible_claims_for_coverage(coverage: list[str], source: dict[str, Any]) -> list[dict[str, Any]]:
    claims = []
    for coverage_id in coverage:
        template = CLAIM_TEMPLATES[coverage_id]
        claims.append(
            {
                "claim": template["claim"],
                "claim_type": template["claim_type"],
                "confidence": template["confidence"],
                "coverage_area": coverage_id,
                "source_id": source["source_id"],
            }
        )
    return claims


def claim_evidence_grade(coverage_id: str, source_ids: list[str]) -> str:
    count = len(set(source_ids))
    if coverage_id in {"evaluation_and_evidence", "comparison_space", "risks_governance_ethics"}:
        if count >= 10:
            return "A"
        if count >= 5:
            return "B"
        if count >= 2:
            return "C"
        return "D"
    if count >= 5:
        return "A"
    if count >= 2:
        return "B"
    if count == 1:
        return "C"
    return "D"


def claim_confidence_for_grade(template: dict[str, Any], grade: str) -> str:
    if grade in {"A", "B"}:
        return template["confidence"]
    if grade == "C":
        return "medium"
    return "low"


def claim_text_for_output(area: dict[str, Any], output: str, template: dict[str, Any]) -> str:
    readable = output.replace("_", " ")
    return f"{area['title']} has source-backed evidence for `{readable}`. Area-level synthesis: {template['claim']}"


def build_claims(digests: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    source_ids_by_area_output: dict[tuple[str, str], list[str]] = defaultdict(list)
    area_by_id = {area["id"]: area for area in COVERAGE_AREAS}
    output_to_area = {
        output: area["id"]
        for area in COVERAGE_AREAS
        for output in area["required_outputs"]
    }
    for digest in digests:
        if digest.get("digest_status") != "complete":
            continue
        coverage_ids = digest.get("coverage_areas", [])
        supported_outputs = digest.get("supported_outputs") or supported_outputs_for_coverage(coverage_ids)
        for output in supported_outputs:
            coverage_id = output_to_area.get(output)
            if coverage_id in coverage_ids:
                source_ids_by_area_output[(coverage_id, output)].append(digest["source_id"])

    claims: list[dict[str, Any]] = []
    links: list[dict[str, Any]] = []
    claim_index = 0
    for area in COVERAGE_AREAS:
        coverage_id = area["id"]
        template = CLAIM_TEMPLATES[coverage_id]
        for output in area["required_outputs"]:
            claim_index += 1
            source_ids = sorted(set(source_ids_by_area_output.get((coverage_id, output), [])))
            grade = claim_evidence_grade(coverage_id, source_ids)
            claim_id = f"claim_{claim_index:06d}_{coverage_id}_{output}"
            claim = {
                "claim_id": claim_id,
                "claim": claim_text_for_output(area_by_id[coverage_id], output, template),
                "claim_type": template["claim_type"],
                "coverage_areas": [coverage_id],
                "required_outputs_supported": [output],
                "supporting_sources": source_ids[:30],
                "contradicting_sources": [],
                "confidence": claim_confidence_for_grade(template, grade) if source_ids else "low",
                "evidence_grade": grade,
                "status": "source_linked" if source_ids else "missing_source_support",
                "limitations": template["limitations"],
                "created_at": now(),
            }
            claims.append(claim)
            for source_id in source_ids[:30]:
                links.append(
                    {
                        "link_id": f"link_{claim_id}_{source_id}",
                        "claim_id": claim_id,
                        "source_id": source_id,
                        "coverage_area": coverage_id,
                        "required_output": output,
                        "support_type": "supports",
                        "created_at": now(),
                    }
                )
    return claims, links


def output_status(output: str, source_count: int, blocked: bool, output_claims: list[dict[str, Any]]) -> tuple[str, str]:
    if not output_claims:
        if blocked:
            return "blocked", "Relevant desired sources are inaccessible and logged in XML, but no replacement evidence supports this output."
        return "missing", "No output-specific source-backed claim currently supports this output."

    claim_grades = {claim.get("evidence_grade", "D") for claim in output_claims}
    if not claim_grades <= {"A", "B"}:
        return "weak", "This output has source-linked claims, but the claim evidence grade is below the stop-condition threshold."
    if source_count >= 5:
        return "supported", "Multiple local sources and adequate claim evidence support this output."
    if source_count >= 2:
        return "partially_supported", "Local support exists but diversity or depth is still limited."
    if source_count == 1:
        return "weak", "Only one local source currently supports this output."
    if blocked:
        return "blocked", "Relevant desired sources are inaccessible and logged in XML."
    return "missing", "No local source-backed claim currently supports this output."


def build_coverage_records(
    manifest: dict[str, Any],
    claims: list[dict[str, Any]],
    links: list[dict[str, Any]],
    inaccessible: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    claims_by_area: dict[str, list[dict[str, Any]]] = defaultdict(list)
    source_ids_by_area: dict[str, set[str]] = defaultdict(set)
    claims_by_area_output: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    source_ids_by_area_output: dict[tuple[str, str], set[str]] = defaultdict(set)
    for claim in claims:
        for area_id in claim["coverage_areas"]:
            claims_by_area[area_id].append(claim)
            for source_id in claim.get("supporting_sources", []):
                source_ids_by_area[area_id].add(source_id)
            for output in claim.get("required_outputs_supported", []):
                claims_by_area_output[(area_id, output)].append(claim)
                for source_id in claim.get("supporting_sources", []):
                    source_ids_by_area_output[(area_id, output)].add(source_id)

    blocked_areas = {item["coverage_area"] for item in inaccessible}
    records: list[dict[str, Any]] = []
    for area in manifest["coverage_areas"]:
        area_id = area["id"]
        area_claims = claims_by_area.get(area_id, [])
        source_ids = sorted(source_ids_by_area.get(area_id, set()))
        for output in area["required_outputs"]:
            output_claims = claims_by_area_output.get((area_id, output), [])
            output_source_ids = sorted(source_ids_by_area_output.get((area_id, output), set()))
            status, remaining_gap = output_status(output, len(output_source_ids), area_id in blocked_areas, output_claims)
            records.append(
                {
                    "coverage_record_id": f"covrec_{area_id}_{output}",
                    "coverage_id": area_id,
                    "required_output": output,
                    "claim_ids": [claim["claim_id"] for claim in output_claims],
                    "source_ids": output_source_ids[:30],
                    "status": status,
                    "remaining_gap": remaining_gap,
                    "updated_at": now(),
                }
            )
    return records


def build_inaccessible_xml(sources: list[dict[str, Any]]) -> None:
    blocked_by_id = {source["source_id"]: source for source in sources if source.get("status") != "ok"}
    root = ET.Element("inaccessible_sources", generated_at=now())
    for item in INACCESSIBLE_SOURCES:
        source = blocked_by_id.get(item["id"], {})
        node = ET.SubElement(
            root,
            "source",
            {
                "id": item["id"],
                "coverage_area": item["coverage_area"],
                "priority": item["priority"],
            },
        )
        fields = {
            "url": item["url"],
            "title": item["title"],
            "attempted_method": item["attempted_method"],
            "failure_type": item["failure_type"] if source.get("error") == "HTTP 200" else (source.get("status") or item["failure_type"]),
            "reason": item["reason"] if source.get("error") == "HTTP 200" else (source.get("error") or item["reason"]),
            "impact": item["impact"],
            "next_retry_path": item["next_retry_path"],
            "last_attempted_at": source.get("fetched_at") or "unknown",
            "local_failure_path": source.get("local_dir") or "",
        }
        for tag, value in fields.items():
            child = ET.SubElement(node, tag)
            child.text = str(value)
    INACCESSIBLE_XML.parent.mkdir(parents=True, exist_ok=True)
    tree = ET.ElementTree(root)
    ET.indent(tree, space="  ")
    tree.write(INACCESSIBLE_XML, encoding="utf-8", xml_declaration=True)


def bootstrap() -> None:
    manifest = compile_manifest()
    write_json(LOOP_MANIFEST, manifest)
    for path in [
        SEARCH_TASKS,
        CANDIDATES,
        TRIAGE,
        SOURCE_DIGESTS,
        CLAIMS,
        CLAIM_SOURCE_LINKS,
        COVERAGE_RECORDS,
        LOOP_EVENTS,
        ACQUISITION_FAILURES,
        AUDIT_EVENTS,
    ]:
        ensure_empty_jsonl(path)

    sources = load_sources()
    if not SEARCH_TASKS.read_text(encoding="utf-8").strip():
        rows = []
        for item in P0_SEARCH_TASKS:
            row = dict(item)
            row["created_at"] = now()
            rows.append(row)
        write_jsonl(SEARCH_TASKS, rows)

    build_inaccessible_xml(sources)
    append_jsonl(LOOP_EVENTS, {"event": "bootstrap", "created_at": now(), "manifest": rel(LOOP_MANIFEST)})
    update_state(manifest, sources, read_jsonl(SOURCE_DIGESTS), read_jsonl(CLAIMS), read_jsonl(COVERAGE_RECORDS), [])


def digest_existing() -> None:
    sources = load_sources()
    digests = [source_digest(source) for source in sources]
    write_jsonl(SOURCE_DIGESTS, digests)
    write_digest_index(digests)
    append_jsonl(LOOP_EVENTS, {"event": "digest_existing", "created_at": now(), "digest_count": len(digests)})


def write_digest_index(digests: list[dict[str, Any]]) -> None:
    lines = ["# Source Digests Index", "", "| Digest | Source | Type | Status | Coverage | Readable text |", "|---|---|---|---|---|---|"]
    for digest in digests:
        lines.append(
            "| {digest} | {source} | {stype} | {status} | {coverage} | {text} |".format(
                digest=digest["digest_id"],
                source=digest["source_id"],
                stype=digest.get("source_type") or "",
                status=digest["digest_status"],
                coverage=", ".join(digest.get("coverage_areas", [])),
                text=digest.get("readable_text_path") or "",
            )
        )
    SOURCE_DIGEST_INDEX.write_text("\n".join(lines) + "\n", encoding="utf-8")


def extract_claims() -> None:
    digests = read_jsonl(SOURCE_DIGESTS)
    claims, links = build_claims(digests)
    write_jsonl(CLAIMS, claims)
    write_jsonl(CLAIM_SOURCE_LINKS, links)
    append_jsonl(LOOP_EVENTS, {"event": "extract_claims", "created_at": now(), "claim_count": len(claims), "link_count": len(links)})


def map_coverage() -> None:
    manifest = read_json(LOOP_MANIFEST)
    claims = read_jsonl(CLAIMS)
    links = read_jsonl(CLAIM_SOURCE_LINKS)
    records = build_coverage_records(manifest, claims, links, INACCESSIBLE_SOURCES)
    write_jsonl(COVERAGE_RECORDS, records)
    append_jsonl(LOOP_EVENTS, {"event": "map_coverage", "created_at": now(), "coverage_record_count": len(records)})


def candidate_to_seed_source(candidate: dict[str, Any]) -> dict[str, Any]:
    source = {
        "id": candidate["source_id"],
        "type": candidate.get("type", "webpage"),
        "title": candidate.get("title", candidate["source_id"]),
        "url": candidate["url"],
        "priority": candidate.get("priority", "p1"),
        "tags": candidate.get("tags", []),
    }
    for key in ["canonical_url", "arxiv_id", "repo", "package"]:
        if candidate.get(key):
            source[key] = candidate[key]
    return source


def discover() -> None:
    bootstrap()
    tasks = read_jsonl(SEARCH_TASKS)
    candidates = read_jsonl(CANDIDATES)
    candidate_ids = {row.get("source_id") for row in candidates}
    acquired_ids = {row["source_id"] for row in load_sources()}
    added = 0
    updated_tasks: list[dict[str, Any]] = []

    for task in tasks:
        task = dict(task)
        if task.get("status") != "open":
            updated_tasks.append(task)
            continue
        matched: list[str] = []
        for seed in CANDIDATE_SOURCE_SEEDS:
            if task["search_task_id"] not in seed.get("task_ids", []) and task.get("coverage_id") != seed.get("coverage_id"):
                continue
            matched.append(seed["source_id"])
            if seed["source_id"] in candidate_ids or seed["source_id"] in acquired_ids:
                continue
            row = {
                **seed,
                "candidate_id": f"candidate_{seed['source_id']}",
                "created_at": now(),
                "status": "pending_triage",
                "discovery_method": "coverage_gap_seed",
                "search_task_id": task["search_task_id"],
                "supports_outputs": [
                    tag.split(":", 1)[1]
                    for tag in seed.get("tags", [])
                    if isinstance(tag, str) and tag.startswith("output:")
                ],
            }
            candidates.append(row)
            candidate_ids.add(seed["source_id"])
            added += 1
        if matched:
            task["status"] = "candidate_generated"
            task["candidate_source_ids"] = sorted(set(matched))
            task["updated_at"] = now()
        updated_tasks.append(task)

    write_jsonl(CANDIDATES, candidates)
    write_jsonl(SEARCH_TASKS, updated_tasks)
    append_jsonl(LOOP_EVENTS, {"event": "discover", "created_at": now(), "candidate_count_added": added})
    print(json.dumps({"discover_added": added, "candidate_total": len(candidates)}, indent=2))


def triage() -> None:
    candidates = read_jsonl(CANDIDATES)
    triage_rows = read_jsonl(TRIAGE)
    triaged_ids = {row.get("source_id") for row in triage_rows}
    acquired_ids = {row["source_id"]: row for row in load_sources()}
    accepted = 0
    skipped = 0
    updated_candidates: list[dict[str, Any]] = []

    for candidate in candidates:
        candidate = dict(candidate)
        source_id = candidate["source_id"]
        if candidate.get("status") != "pending_triage":
            updated_candidates.append(candidate)
            continue
        if source_id in acquired_ids and acquired_ids[source_id].get("status") == "ok":
            candidate["status"] = "already_acquired"
            candidate["updated_at"] = now()
            skipped += 1
            updated_candidates.append(candidate)
            continue
        if source_id in triaged_ids:
            candidate["status"] = "already_triaged"
            candidate["updated_at"] = now()
            skipped += 1
            updated_candidates.append(candidate)
            continue
        decision = {
            "triage_id": f"triage_{source_id}",
            "source_id": source_id,
            "candidate_id": candidate.get("candidate_id"),
            "coverage_id": candidate.get("coverage_id"),
            "status": "queued_for_acquisition",
            "decision": "accept",
            "reason": candidate.get("relevance_reason", "Relevant to an open coverage gap."),
            "seed_source": candidate_to_seed_source(candidate),
            "created_at": now(),
        }
        triage_rows.append(decision)
        triaged_ids.add(source_id)
        candidate["status"] = "accepted"
        candidate["updated_at"] = now()
        updated_candidates.append(candidate)
        accepted += 1

    write_jsonl(CANDIDATES, updated_candidates)
    write_jsonl(TRIAGE, triage_rows)
    append_jsonl(LOOP_EVENTS, {"event": "triage", "created_at": now(), "accepted": accepted, "skipped": skipped})
    print(json.dumps({"triage_accepted": accepted, "triage_skipped": skipped}, indent=2))


def acquire() -> int:
    triage_rows = read_jsonl(TRIAGE)
    queued = [
        row
        for row in triage_rows
        if row.get("status") in {"queued_for_acquisition", "acquisition_failed"}
    ]
    if not queued:
        print(json.dumps({"acquire_queued": 0}, indent=2))
        return 0

    manifest_sources = [row["seed_source"] for row in queued]
    with tempfile.TemporaryDirectory(prefix="llm_wiki_acquire_") as temp_dir:
        manifest_path = Path(temp_dir) / "sources.json"
        manifest_path.write_text(json.dumps(manifest_sources, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        cmd = [sys.executable, str(ROOT / "scripts" / "fetch_sources.py"), "--manifest", str(manifest_path)]
        completed = subprocess.run(
            cmd,
            cwd=str(ROOT),
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=1800,
        )
    if completed.stdout:
        print(completed.stdout)

    source_by_id = {row["source_id"]: row for row in load_sources()}
    updated_triage: list[dict[str, Any]] = []
    acquired = 0
    failed = 0
    for row in triage_rows:
        row = dict(row)
        if row.get("status") not in {"queued_for_acquisition", "acquisition_failed"}:
            updated_triage.append(row)
            continue
        source = source_by_id.get(row["source_id"])
        if source and source.get("status") == "ok":
            row["status"] = "acquired"
            row["acquired_at"] = now()
            row["local_dir"] = source.get("local_dir")
            acquired += 1
        elif source:
            row["status"] = "acquisition_failed"
            row["updated_at"] = now()
            row["failure_status"] = source.get("status")
            row["failure_error"] = source.get("error")
            append_jsonl(
                ACQUISITION_FAILURES,
                {
                    "source_id": row["source_id"],
                    "created_at": now(),
                    "status": source.get("status"),
                    "error": source.get("error"),
                    "url": source.get("source_url"),
                    "coverage_id": row.get("coverage_id"),
                },
            )
            failed += 1
        else:
            row["status"] = "acquisition_failed"
            row["updated_at"] = now()
            row["failure_error"] = "fetcher did not write a sources.jsonl row"
            failed += 1
        updated_triage.append(row)

    write_jsonl(TRIAGE, updated_triage)
    append_jsonl(
        LOOP_EVENTS,
        {
            "event": "acquire",
            "created_at": now(),
            "queued": len(queued),
            "acquired": acquired,
            "failed": failed,
            "fetch_exit_code": completed.returncode,
        },
    )
    return completed.returncode


def plan_next() -> None:
    if not LOOP_STATE.exists():
        bootstrap()
    state = read_json(LOOP_STATE)
    print(json.dumps(
        {
            "current_target": state.get("current_target"),
            "next_recommended_action": state.get("next_recommended_action"),
            "blocking_items": state.get("satisfaction", {}).get("blocking_items", [])[:20],
            "queues": state.get("queues"),
        },
        indent=2,
    ))


def area_record_status(records: list[dict[str, Any]], area_id: str) -> str:
    statuses = [record["status"] for record in records if record["coverage_id"] == area_id]
    if not statuses:
        return "missing"
    if all(status == "supported" for status in statuses):
        return "supported"
    if any(status == "missing" for status in statuses):
        return "missing"
    if any(status == "blocked" for status in statuses):
        return "blocked"
    if any(status == "weak" for status in statuses):
        return "weak"
    return "partial"


def reports() -> None:
    manifest = read_json(LOOP_MANIFEST)
    sources = load_sources()
    digests = read_jsonl(SOURCE_DIGESTS)
    claims = read_jsonl(CLAIMS)
    links = read_jsonl(CLAIM_SOURCE_LINKS)
    records = read_jsonl(COVERAGE_RECORDS)
    audits = read_jsonl(AUDIT_EVENTS)
    write_coverage_status(manifest, sources, digests, claims, records)
    write_evidence_matrix(manifest, claims, links, records)
    write_judgment_status(manifest, records, audits)
    write_acquisition_status(sources)
    append_jsonl(LOOP_EVENTS, {"event": "reports", "created_at": now()})


def write_coverage_status(
    manifest: dict[str, Any],
    sources: list[dict[str, Any]],
    digests: list[dict[str, Any]],
    claims: list[dict[str, Any]],
    records: list[dict[str, Any]],
) -> None:
    source_count_by_area = Counter()
    digest_count_by_area = Counter()
    claim_count_by_area = Counter()
    for digest in digests:
        for area in digest.get("coverage_areas", []):
            source_count_by_area[area] += 1
            if digest.get("digest_status") == "complete":
                digest_count_by_area[area] += 1
    for claim in claims:
        for area in claim.get("coverage_areas", []):
            claim_count_by_area[area] += 1

    lines = [
        "# Coverage Status",
        "",
        f"Generated: {now()}",
        "",
        "| Coverage area | Status | Sources | Digests | Claims | Required output status |",
        "|---|---:|---:|---:|---:|---|",
    ]
    for area in manifest["coverage_areas"]:
        area_id = area["id"]
        status = area_record_status(records, area_id)
        output_bits = [
            f"{record['required_output']}={record['status']}"
            for record in records
            if record["coverage_id"] == area_id
        ]
        lines.append(
            f"| {area_id} | {status} | {source_count_by_area[area_id]} | {digest_count_by_area[area_id]} | {claim_count_by_area[area_id]} | {'; '.join(output_bits)} |"
        )
    COVERAGE_STATUS.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_evidence_matrix(
    manifest: dict[str, Any],
    claims: list[dict[str, Any]],
    links: list[dict[str, Any]],
    records: list[dict[str, Any]],
) -> None:
    source_by_claim: dict[str, list[str]] = defaultdict(list)
    for link in links:
        source_by_claim[link["claim_id"]].append(link["source_id"])
    lines = [
        "# Evidence Matrix",
        "",
        f"Generated: {now()}",
        "",
        "## Claims",
        "",
        "| Claim ID | Coverage | Type | Confidence | Grade | Sources | Limitation |",
        "|---|---|---|---|---|---|---|",
    ]
    for claim in claims:
        lines.append(
            "| {claim_id} | {coverage} | {ctype} | {confidence} | {grade} | {sources} | {limitations} |".format(
                claim_id=claim["claim_id"],
                coverage=", ".join(claim["coverage_areas"]),
                ctype=claim["claim_type"],
                confidence=claim["confidence"],
                grade=claim["evidence_grade"],
                sources=", ".join(source_by_claim.get(claim["claim_id"], [])),
                limitations=claim["limitations"].replace("|", "/"),
            )
        )
    lines.extend(["", "## Required Outputs", "", "| Coverage | Required output | Status | Claims | Sources | Gap |", "|---|---|---|---|---|---|"])
    for record in records:
        lines.append(
            "| {coverage} | {output} | {status} | {claims} | {sources} | {gap} |".format(
                coverage=record["coverage_id"],
                output=record["required_output"],
                status=record["status"],
                claims=", ".join(record["claim_ids"]),
                sources=", ".join(record["source_ids"]),
                gap=record["remaining_gap"].replace("|", "/"),
            )
        )
    EVIDENCE_MATRIX.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_judgment_status(manifest: dict[str, Any], records: list[dict[str, Any]], audits: list[dict[str, Any]]) -> None:
    area_status = {area["id"]: area_record_status(records, area["id"]) for area in manifest["coverage_areas"]}
    latest_audit = latest_audit_by_target(audits)
    lines = ["# Judgment Status", "", f"Generated: {now()}", ""]
    lines.extend(["## Coverage Areas", "", "| Area | Coverage status | Latest audit | Gate |", "|---|---|---|---|"])
    for area in manifest["coverage_areas"]:
        audit_status = latest_audit.get(area["id"], {}).get("status", "not_run")
        lines.append(f"| {area['id']} | {area_status[area['id']]} | {audit_status} | {area['judgment_gate']} |")

    lines.extend(["", "## Judgment Gates", "", "| Gate | Status | Blocking items |", "|---|---|---|"])
    gate_statuses = compute_gate_state(manifest, records, audits)
    for gate, state in gate_statuses.items():
        blockers = ", ".join(state.get("blocking_coverage_areas", state.get("blocking_gates", [])))
        lines.append(f"| {gate} | {state['status']} | {blockers} |")
    queues = compute_queue_counts(load_sources(), read_jsonl(SOURCE_DIGESTS), read_jsonl(CLAIMS), audits)
    failures = satisfaction_failures(manifest, records, audits, gate_statuses, queues)
    lines.extend(
        [
            "",
            "## Stop Condition",
            "",
            "`verify` is a structural health check only. The loop may stop only when `python3 scripts/run_loop.py satisfaction` returns `SATISFACTION PASS`.",
            "",
            f"Current satisfaction status: {'PASS' if not failures else 'FAIL'}",
            "",
            "Blocking items:",
        ]
    )
    if failures:
        lines.extend([f"- {failure}" for failure in failures[:25]])
        if len(failures) > 25:
            lines.append(f"- ... {len(failures) - 25} additional blocker(s)")
    else:
        lines.append("- none")
    lines.extend(
        [
            "",
            "## Current Paper-Readiness Judgment",
            "",
            (
                "The repository satisfies the current coverage-driven stop condition and is ready for an evidence-backed landscape memo."
                if not failures
                else "The repository is ready for an evidence-backed landscape memo. It is not ready to stop the research loop until the stop-condition check passes."
            ),
        ]
    )
    JUDGMENT_STATUS.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_acquisition_status(sources: list[dict[str, Any]]) -> None:
    counter = Counter(source.get("status") for source in sources)
    type_counter = Counter(source.get("source_type") for source in sources)
    lines = [
        "# LLM Wiki Resource Acquisition Status",
        "",
        f"Last updated: {now()}",
        "",
        "## Snapshot",
        "",
        f"- Seed sources: {len(sources)}",
        f"- Successful acquisitions: {counter.get('ok', 0)}",
        f"- Blocked sources: {counter.get('blocked', 0)}",
        f"- HTTP/network-intercept failures: {counter.get('http_error', 0)}",
        f"- Source types: {dict(type_counter)}",
        "",
        "## Inaccessible Sources",
        "",
        f"See `{rel(INACCESSIBLE_XML)}` for XML-tagged inaccessible source records.",
    ]
    ACQUISITION_STATUS.write_text("\n".join(lines) + "\n", encoding="utf-8")


def latest_audit_by_target(audits: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    latest: dict[str, dict[str, Any]] = {}
    for audit in audits:
        latest[audit["target_id"]] = audit
    return latest


def compute_gate_state(manifest: dict[str, Any], records: list[dict[str, Any]], audits: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    area_status = {area["id"]: area_record_status(records, area["id"]) for area in manifest["coverage_areas"]}
    latest_audit = latest_audit_by_target(audits)
    gate_state: dict[str, dict[str, Any]] = {}
    for gate_id, gate in manifest["judgment_gates"].items():
        if "required_coverage_areas" in gate:
            blockers = []
            for area_id in gate["required_coverage_areas"]:
                audit_status = latest_audit.get(area_id, {}).get("status")
                if area_status.get(area_id) != "supported" or audit_status != "pass":
                    blockers.append(area_id)
            gate_state[gate_id] = {
                "status": "passed" if not blockers else "not_ready",
                "blocking_coverage_areas": blockers,
            }
    for gate_id, gate in manifest["judgment_gates"].items():
        if "required_gates" not in gate:
            continue
        blockers = [
            required_gate
            for required_gate in gate["required_gates"]
            if gate_state.get(required_gate, {}).get("status") != "passed"
        ]
        gate_state[gate_id] = {
            "status": "passed" if not blockers else "not_ready",
            "blocking_gates": blockers,
        }
    return gate_state


def compute_queue_counts(
    sources: list[dict[str, Any]],
    digests: list[dict[str, Any]],
    claims: list[dict[str, Any]],
    audits: list[dict[str, Any]],
) -> dict[str, int]:
    digested_source_ids = {digest["source_id"] for digest in digests}
    return {
        "search_tasks_open": len([row for row in read_jsonl(SEARCH_TASKS) if row.get("status") == "open"]),
        "candidate_sources_pending_triage": len([row for row in read_jsonl(CANDIDATES) if row.get("status") == "pending_triage"]),
        "sources_pending_acquisition": len([row for row in read_jsonl(TRIAGE) if row.get("status") == "queued_for_acquisition"]),
        "sources_failed_acquisition": len([row for row in read_jsonl(TRIAGE) if row.get("status") == "acquisition_failed"]),
        "sources_pending_digest": len([source for source in sources if source["source_id"] not in digested_source_ids]),
        "digests_pending_claim_extraction": 0 if claims else len(digests),
        "claims_pending_audit": 0 if audits else len(claims),
    }


def satisfaction_failures(
    manifest: dict[str, Any],
    records: list[dict[str, Any]],
    audits: list[dict[str, Any]],
    gate_state: dict[str, dict[str, Any]],
    queues: dict[str, int],
) -> list[str]:
    failures: list[str] = []
    if gate_state.get("research_paper", {}).get("status") != "passed":
        blockers = gate_state.get("research_paper", {}).get("blocking_gates", [])
        failures.append("research_paper gate is not passed" + (f": {', '.join(blockers)}" if blockers else ""))

    latest_audit = latest_audit_by_target(audits)
    for area in manifest.get("coverage_areas", []):
        area_id = area["id"]
        area_status = area_record_status(records, area_id)
        audit_status = latest_audit.get(area_id, {}).get("status", "not_run")
        if area_status != "supported":
            failures.append(f"{area_id} coverage status is {area_status}, not supported")
        if audit_status != "pass":
            failures.append(f"{area_id} latest audit is {audit_status}, not pass")
        by_output = {record["required_output"]: record for record in records if record["coverage_id"] == area_id}
        for output in area["required_outputs"]:
            output_status = by_output.get(output, {}).get("status", "missing")
            if output_status != "supported":
                failures.append(f"{area_id}.{output} is {output_status}, not supported")

    for queue_name, count in queues.items():
        if count:
            failures.append(f"{queue_name} has {count} open item(s)")

    return failures


def audit() -> None:
    manifest = read_json(LOOP_MANIFEST)
    sources = load_sources()
    digests = read_jsonl(SOURCE_DIGESTS)
    claims = read_jsonl(CLAIMS)
    records = read_jsonl(COVERAGE_RECORDS)
    source_ids = {source["source_id"] for source in sources}
    digest_source_ids = {digest["source_id"] for digest in digests}
    existing_paths = {source["source_id"]: (ROOT / source.get("local_dir", "")).exists() for source in sources}

    audit_rows: list[dict[str, Any]] = []
    for area in manifest["coverage_areas"]:
        area_id = area["id"]
        failures: list[dict[str, str]] = []
        area_records = [record for record in records if record["coverage_id"] == area_id]
        area_claims = [claim for claim in claims if area_id in claim.get("coverage_areas", [])]
        area_sources = sorted({source_id for claim in area_claims for source_id in claim.get("supporting_sources", [])})

        missing_outputs = [
            output
            for output in area["required_outputs"]
            if not any(record["required_output"] == output for record in area_records)
        ]
        if missing_outputs:
            failures.append({"type": "missing_coverage_records", "message": ", ".join(missing_outputs)})
        for source_id in area_sources:
            if source_id not in source_ids:
                failures.append({"type": "unknown_source_id", "message": source_id})
            if not existing_paths.get(source_id, False):
                failures.append({"type": "missing_raw_path", "message": source_id})
            if source_id not in digest_source_ids:
                failures.append({"type": "missing_digest", "message": source_id})
        for claim in area_claims:
            if not claim.get("supporting_sources"):
                failures.append({"type": "claim_without_source", "message": claim["claim_id"]})
            if claim["claim_type"] == "evaluation_result" and claim["evidence_grade"] not in {"A", "B"}:
                failures.append(
                    {
                        "type": "empirical_not_ready",
                        "message": f"{claim['claim_id']} has insufficient empirical grade for a paper-level gate.",
                    }
                )
            if claim["claim_type"] == "strategic_judgment" and claim["evidence_grade"] not in {"A", "B"}:
                failures.append(
                    {
                        "type": "strategic_not_ready",
                        "message": f"{claim['claim_id']} lacks enough comparison/risk evidence for a paper-level strategic gate.",
                    }
                )

        output_statuses = {record["status"] for record in area_records}
        if "missing" in output_statuses:
            failures.append({"type": "required_output_missing", "message": "One or more required outputs remain missing."})
        status = "pass" if not failures and output_statuses and output_statuses <= {"supported"} else "not_ready"
        if output_statuses & {"weak", "blocked", "partially_supported"}:
            status = "not_ready"

        audit_rows.append(
            {
                "audit_id": f"audit_{area_id}_{datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S')}",
                "created_at": now(),
                "target_type": "coverage_area",
                "target_id": area_id,
                "status": status,
                "failures": failures,
                "required_fixes": required_fixes(area_id, failures, output_statuses),
            }
        )

    write_jsonl(AUDIT_EVENTS, audit_rows)
    append_jsonl(LOOP_EVENTS, {"event": "audit", "created_at": now(), "audit_count": len(audit_rows)})
    update_state(manifest, sources, digests, claims, records, audit_rows)


def required_fixes(area_id: str, failures: list[dict[str, str]], output_statuses: set[str]) -> list[str]:
    fixes = []
    if any(failure["type"] == "empirical_not_ready" for failure in failures):
        fixes.append("Acquire independent benchmark/case-study evidence with explicit baselines and methods.")
    if any(failure["type"] == "strategic_not_ready" for failure in failures):
        fixes.append("Acquire primary-source comparison, cost, risk, governance, and negative-case evidence.")
    if "blocked" in output_statuses:
        fixes.append("Retry or replace blocked sources and keep inaccessible source XML current.")
    if "weak" in output_statuses:
        fixes.append("Add more diverse source-backed claims for weak outputs.")
    if "partially_supported" in output_statuses:
        fixes.append("Add enough diverse, output-specific evidence to upgrade partial outputs to supported.")
    if not fixes:
        fixes.append("No required fix; keep area under periodic re-audit.")
    return fixes


def update_state(
    manifest: dict[str, Any],
    sources: list[dict[str, Any]],
    digests: list[dict[str, Any]],
    claims: list[dict[str, Any]],
    records: list[dict[str, Any]],
    audits: list[dict[str, Any]],
) -> None:
    coverage_state: dict[str, Any] = {}
    source_count_by_area = Counter()
    digest_count_by_area = Counter()
    claim_count_by_area = Counter()
    for digest in digests:
        for area_id in digest.get("coverage_areas", []):
            source_count_by_area[area_id] += 1
            if digest.get("digest_status") == "complete":
                digest_count_by_area[area_id] += 1
    for claim in claims:
        for area_id in claim.get("coverage_areas", []):
            claim_count_by_area[area_id] += 1

    latest_audit = latest_audit_by_target(audits or read_jsonl(AUDIT_EVENTS))
    for area in manifest["coverage_areas"]:
        area_id = area["id"]
        area_records = [record for record in records if record["coverage_id"] == area_id]
        missing_outputs = [
            record["required_output"]
            for record in area_records
            if record["status"] in {"missing", "weak", "blocked", "partially_supported"}
        ]
        if not area_records:
            missing_outputs = area["required_outputs"]
        coverage_state[area_id] = {
            "status": area_record_status(records, area_id),
            "evidence_count": source_count_by_area[area_id],
            "source_count": source_count_by_area[area_id],
            "claim_count": claim_count_by_area[area_id],
            "digest_count": digest_count_by_area[area_id],
            "audit_status": latest_audit.get(area_id, {}).get("status", "not_run"),
            "missing_outputs": missing_outputs,
            "next_action": next_action_for_area(area_id),
        }

    effective_audits = audits or read_jsonl(AUDIT_EVENTS)
    gate_state = compute_gate_state(manifest, records, effective_audits)
    queues = compute_queue_counts(sources, digests, claims, effective_audits)
    stop_failures = satisfaction_failures(manifest, records, effective_audits, gate_state, queues)
    state = {
        "run_id": "run_2026_05_21_local",
        "objective_doc": rel(OBJECTIVE_DOC),
        "objective_hash": manifest.get("objective_hash"),
        "last_updated": now(),
        "current_phase": "satisfied" if not stop_failures else ("audit_complete_not_satisfied" if effective_audits else "bootstrap_or_update"),
        "current_target": select_target(coverage_state),
        "coverage_state": coverage_state,
        "gate_state": gate_state,
        "queues": queues,
        "satisfaction": {
            "status": "pass" if not stop_failures else "fail",
            "stop_command": "python3 scripts/run_loop.py satisfaction",
            "blocking_items": stop_failures[:50],
        },
        "last_completed_loop": now() if audits else None,
        "next_recommended_action": "stop" if not stop_failures else "continue_gap_discovery_acquisition_digest_audit",
        "latest_manifest": rel(SOURCES),
        "latest_report": rel(JUDGMENT_STATUS) if JUDGMENT_STATUS.exists() else rel(SOURCE_GAP_REVIEW),
    }
    write_json(LOOP_STATE, state)


def next_action_for_area(area_id: str) -> str:
    actions = {
        "evaluation_and_evidence": "Acquire reproducible benchmarks, case studies, and baseline comparisons.",
        "comparison_space": "Acquire primary-source RAG, GraphRAG, PKM, and agent-memory comparison materials.",
        "risks_governance_ethics": "Acquire security, privacy, governance, poisoning, and provenance-risk evidence.",
        "workflow_and_operations": "Deep-digest representative repo workflows and failure handling.",
        "architecture_and_data_model": "Deep-classify implementation architecture from selected repos.",
        "ecosystem_and_implementations": "Add issue/release/plugin usage evidence beyond stars and forks.",
        "origin_and_canon": "Recover blocked Reddit launch-adjacent sources if possible.",
        "problem_and_motivation": "Add more independent user reports and negative cases.",
    }
    return actions.get(area_id, "Continue evidence acquisition.")


def select_target(coverage_state: dict[str, Any]) -> str:
    priority = [
        "evaluation_and_evidence",
        "risks_governance_ethics",
        "comparison_space",
        "workflow_and_operations",
        "architecture_and_data_model",
        "problem_and_motivation",
        "origin_and_canon",
        "ecosystem_and_implementations",
    ]
    for area_id in priority:
        status = coverage_state.get(area_id, {}).get("status")
        audit_status = coverage_state.get(area_id, {}).get("audit_status")
        if status in {"missing", "weak", "blocked", "partial"} or audit_status != "pass":
            return area_id
    return "none"


def status() -> None:
    if not LOOP_STATE.exists():
        print("loop_state.json missing; run bootstrap")
        return
    state = read_json(LOOP_STATE)
    print(json.dumps(
        {
            "current_phase": state.get("current_phase"),
            "current_target": state.get("current_target"),
            "queues": state.get("queues"),
            "gate_state": state.get("gate_state"),
            "satisfaction": state.get("satisfaction"),
        },
        indent=2,
    ))


def once() -> None:
    bootstrap()
    discover()
    triage()
    acquire()
    digest_existing()
    extract_claims()
    map_coverage()
    reports()
    audit()
    reports()


def verify() -> int:
    required = [
        LOOP_MANIFEST,
        LOOP_STATE,
        SOURCE_DIGESTS,
        CLAIMS,
        CLAIM_SOURCE_LINKS,
        COVERAGE_RECORDS,
        INACCESSIBLE_XML,
        AUDIT_EVENTS,
        COVERAGE_STATUS,
        EVIDENCE_MATRIX,
        JUDGMENT_STATUS,
    ]
    failures = []
    for path in required:
        if not path.exists():
            failures.append(f"missing {rel(path)}")
    for path in [LOOP_MANIFEST, LOOP_STATE]:
        if path.exists():
            try:
                read_json(path)
            except Exception as exc:  # noqa: BLE001
                failures.append(f"invalid json {rel(path)}: {exc}")
    for path in [SOURCE_DIGESTS, CLAIMS, CLAIM_SOURCE_LINKS, COVERAGE_RECORDS, AUDIT_EVENTS]:
        try:
            read_jsonl(path)
        except Exception as exc:  # noqa: BLE001
            failures.append(f"invalid jsonl {rel(path)}: {exc}")
    if INACCESSIBLE_XML.exists():
        try:
            ET.parse(INACCESSIBLE_XML)
        except ET.ParseError as exc:
            failures.append(f"invalid xml {rel(INACCESSIBLE_XML)}: {exc}")
    claims = read_jsonl(CLAIMS) if CLAIMS.exists() else []
    for claim in claims:
        if not claim.get("supporting_sources"):
            failures.append(f"claim without source {claim.get('claim_id')}")
    records = read_jsonl(COVERAGE_RECORDS) if COVERAGE_RECORDS.exists() else []
    manifest = read_json(LOOP_MANIFEST) if LOOP_MANIFEST.exists() else {"coverage_areas": []}
    expected_records = sum(len(area["required_outputs"]) for area in manifest.get("coverage_areas", []))
    if len(records) != expected_records:
        failures.append(f"coverage record count {len(records)} != expected {expected_records}")
    if failures:
        print("VERIFY FAIL")
        for failure in failures:
            print("-", failure)
        return 1
    print("VERIFY PASS")
    return 0


def satisfaction() -> int:
    missing_required = [
        path
        for path in [
            LOOP_MANIFEST,
            LOOP_STATE,
            SOURCE_DIGESTS,
            CLAIMS,
            CLAIM_SOURCE_LINKS,
            COVERAGE_RECORDS,
            INACCESSIBLE_XML,
            AUDIT_EVENTS,
            COVERAGE_STATUS,
            EVIDENCE_MATRIX,
            JUDGMENT_STATUS,
        ]
        if not path.exists()
    ]
    if missing_required:
        print("SATISFACTION FAIL")
        for path in missing_required:
            print(f"- missing {rel(path)}")
        return 1

    manifest = read_json(LOOP_MANIFEST)
    sources = load_sources()
    digests = read_jsonl(SOURCE_DIGESTS)
    claims = read_jsonl(CLAIMS)
    records = read_jsonl(COVERAGE_RECORDS)
    audits = read_jsonl(AUDIT_EVENTS)
    gate_state = compute_gate_state(manifest, records, audits)
    queues = compute_queue_counts(sources, digests, claims, audits)
    failures = satisfaction_failures(manifest, records, audits, gate_state, queues)
    if failures:
        print("SATISFACTION FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("SATISFACTION PASS")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "command",
        choices=[
            "bootstrap",
            "status",
            "next",
            "plan",
            "discover",
            "triage",
            "acquire",
            "digest-existing",
            "claims",
            "coverage",
            "reports",
            "audit",
            "once",
            "verify",
            "satisfaction",
        ],
    )
    args = parser.parse_args()
    if args.command == "bootstrap":
        bootstrap()
    elif args.command == "status":
        status()
    elif args.command in {"next", "plan"}:
        plan_next()
    elif args.command == "discover":
        discover()
    elif args.command == "triage":
        triage()
    elif args.command == "acquire":
        return acquire()
    elif args.command == "digest-existing":
        digest_existing()
    elif args.command == "claims":
        extract_claims()
    elif args.command == "coverage":
        map_coverage()
    elif args.command == "reports":
        reports()
    elif args.command == "audit":
        audit()
    elif args.command == "once":
        once()
    elif args.command == "verify":
        return verify()
    elif args.command == "satisfaction":
        return satisfaction()
    return 0


if __name__ == "__main__":
    sys.exit(main())
