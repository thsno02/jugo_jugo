---
name: llmwiki-dynamic-retrieval
description: Turn evidence gaps into controlled retrieval requests and preserved data assets for LLM Wiki KB initialization. Use when local data is insufficient, audit rejects a citation, or a candidate needs new papers, docs, repos, benchmarks, threads, or governance sources.
---

# LLM Wiki Dynamic Retrieval

## Purpose

Use this skill only when local evidence is insufficient. Retrieval must become durable data before it can support a card.

## Trigger Conditions

- Important candidate lacks enough evidence.
- Audit rejects a citation.
- Working definition lacks source diversity.
- Empirical claim needs benchmark or case support.
- Source gap blocks a first-version node.

## Request Contract

Write a retrieval request with:

- `run_id`
- `target_candidate`
- `status`
- `created_by`
- Why current data is insufficient.
- Missing evidence.
- Desired source types.
- Suggested queries.
- Acceptance criteria.

## Retrieval Rules

- Preserve raw source under `data/raw/<source_id>/`.
- Update `data/manifests/sources.jsonl`.
- Mine the new source before using it in a card.
- Record retrieval in provenance.
- On company machines, make only limited normal attempts; record blocked/intercepted results and defer deeper retrieval.

## Skill Evolution Notes

Patch this skill when agents use search answers without preservation, over-attempt blocked web pages, or retrieval requests are too vague to execute later.
