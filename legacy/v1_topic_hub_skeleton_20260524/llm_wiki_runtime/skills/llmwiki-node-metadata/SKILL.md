---
name: llmwiki-node-metadata
description: Create and maintain node.yaml metadata for LLM Wiki KB version bundles and adopted root nodes. Use when writing IDs, version status, paths, tags, audit fields, stability, and adoption metadata.
---

# LLM Wiki Node Metadata

## Purpose

Use this skill whenever writing `node.yaml` inside `nodes/<node_id>/versions/<version>/` or the adopted root `nodes/<node_id>/node.yaml`.

## Node ID Rules

- First-version timestamp IDs should use `YYYYMMDD_HHMMSS_semantic_slug` when creating new nodes from protocol.
- Do not add category prefixes, levels, or `zk_`.
- Keep node IDs stable even if titles later change.
- If an earlier planner candidate uses a semantic placeholder, normalize it before adopted version creation.

## Required Metadata Intent

Metadata must support:

- Version lookup.
- Adopted view rendering.
- Audit status.
- Stability and support eligibility.
- Paths to `version_dir`, `card`, `provenance`, `change`, and `kb_view`.
- Tags for topic discovery, not taxonomy enforcement.

## Hard Rules

- Do not adopt a root `node.yaml` until audit passes.
- Keep version bundle metadata and adopted root metadata consistent.
- When a root `node.yaml` points to an adopted version, the selected `versions/<version>/node.yaml` must also mark that version adopted and record the audit/adoption run; otherwise node validation must fail before view completion.
- Make path fields resolvable from repo root or the metadata file.
- Do not hide candidate status as adopted.

## Skill Evolution Notes

Patch this skill when validators fail due to missing fields, path drift, version mismatch, or unstable ID conventions.
