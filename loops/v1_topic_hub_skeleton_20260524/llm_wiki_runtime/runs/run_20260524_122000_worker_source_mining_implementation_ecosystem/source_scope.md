# Source Scope

## Source Batch

Primary implementation evidence:

- `data/raw/github_repo/*/repo/README.md` for local cloned implementation descriptions.
- `data/raw/github_repo/*/github_repo.json` for preserved GitHub metadata snapshot: stars, forks, open issues, language, license, created/updated/pushed timestamps.
- `data/raw/pypi/pypi-my-llm-wiki/text.txt` and `data/raw/pypi/pypi-my-llm-wiki/pypi.json`.
- `data/raw/pypi/pypi-llm-wiki-mcp/text.txt` and `data/raw/pypi/pypi-llm-wiki-mcp/pypi.json`.
- `data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt`.
- `data/raw/webpage/obsidian-community-plugin/text.txt`.
- `data/raw/webpage/aillm-wiki-directory/text.txt`.
- `data/raw/webpage/llm-wiki-net/text.txt`.

Secondary/process context:

- `data/manifests/source_digests_index.md`.
- `reports/source_gap_review.md`.
- `reports/coverage_framework.md`.
- `reports/evidence_matrix.md`.

Prior KB anchors, used only for continuity/boundary control:

- `kb/20260524_062000_llm_wiki_origin_and_canon.md`
- `kb/20260524_072000_llm_wiki_working_definition.md`
- `kb/20260524_080000_llm_wiki_three_layer_architecture.md`
- `kb/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow.md`
- `kb/20260524_094000_llm_wiki_vs_rag_write_loop.md`
- `kb/20260524_104000_llm_wiki_risks_governance_and_provenance.md`

## Readability Checks

Representative source files were byte-checked and readable. Examples:

- `repo-nashsu-llm-wiki/repo/README.md`: 26143 bytes.
- `repo-samuraigpt-llm-wiki-agent/repo/README.md`: 12653 bytes.
- `repo-sdyckjq-llm-wiki-skill/repo/README.md`: 10893 bytes.
- `repo-atomicstrata-llm-wiki-compiler/repo/README.md`: 23143 bytes.
- `repo-kytmanov-obsidian-local/repo/README.md`: 34490 bytes.
- `repo-vectifyai-openkb/repo/README.md`: 16751 bytes.
- `repo-ngmeyer-librarian-mcp/repo/README.md`: 9278 bytes.
- `pypi-my-llm-wiki/text.txt`: 7183 bytes.
- `pypi-llm-wiki-mcp/text.txt`: 12071 bytes.
- `clawhub-llm-wiki-karpathy/text.txt`: 8201 bytes.
- `obsidian-community-plugin/text.txt`: 24193 bytes.
- `aillm-wiki-directory/text.txt`: 7963 bytes.
- `llm-wiki-net/text.txt`: 31464 bytes.

No scoped source file was treated as empty.

## Why This Batch

The current frontier marks `cand_006_implementation_ecosystem` as `needs_more_mining` because it lacked a curated implementation taxonomy and adoption-signal boundary. The local corpus now contains enough repo/package/plugin captures to mine a bounded first-version landscape node without broad retrieval.

