# Validation Trace

run_id:: run_20260524_074000_worker_audit_working_definition
executor_role:: independent_audit_worker
target_bundle:: nodes/20260524_072000_llm_wiki_working_definition/versions/1.0

## Official card validator

command:: `/opt/homebrew/bin/python3 scripts/kb_validate_card.py nodes/20260524_072000_llm_wiki_working_definition/versions/1.0/card.md`
result:: pass
output:: `card validation passed: 1 cards`

## YAML parse checks

- `.llmwiki/control/orchestration_gates.yaml`: pass
- `nodes/20260524_072000_llm_wiki_working_definition/versions/1.0/node.yaml`: pass

## Path checks

- `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt`: exists
- `kb/20260524_062000_llm_wiki_origin_and_canon.md`: exists
- `nodes/20260524_062000_llm_wiki_origin_and_canon/versions/1.0/card.md`: exists
- `reports/coverage_framework.md`: exists
- `data/raw/hacker_news/hacker-news-original-thread/text.txt`: exists
- `data/raw/webpage/karpathy-x-launch-post/text.txt`: exists
- `reports/source_gap_review.md`: exists
- `nodes/20260524_072000_llm_wiki_working_definition/versions/1.0/node.yaml`: exists
- `nodes/20260524_072000_llm_wiki_working_definition/versions/1.0/card.md`: exists
- `nodes/20260524_072000_llm_wiki_working_definition/versions/1.0/provenance.md`: exists
- `nodes/20260524_072000_llm_wiki_working_definition/versions/1.0/change.md`: exists

## Adoption-gate state checks

- Root node metadata path `nodes/20260524_072000_llm_wiki_working_definition/node.yaml`: absent
- Candidate KB view path `kb/20260524_072000_llm_wiki_working_definition.md`: absent
- Candidate `node.yaml` status: `candidate_pending_audit`
- Candidate `node.yaml` adopted flag: `false`
- Candidate `node.yaml` audit state: `pending`

## Source support spot checks

- Karpathy gist supports raw sources as immutable source of truth, LLM-generated markdown wiki, schema/instruction governance, ingest/query/lint, index/log navigation, optional tooling, and human/LLM role separation.
- HN capture supports only early discourse around RAG framing, raw-source/backlink/staleness/correctness concerns, and quality/maintenance concerns.
- X launch capture supports the gist as an idea file intended for agent customization and does not need to support adoption, ecosystem, or empirical claims.
- Coverage framework supports secondary boundary framing for source preservation, persistent artifacts, provenance/auditability, maintenance, and comparison questions.
- Source-gap review supports non-blocking gap framing around historical lineage, empirical validation, scale, citation accuracy, governance, adoption, ecosystem, and comparison gaps.
