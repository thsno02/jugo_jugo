# Adoption Report

run_id:: run_20260524_074500_worker_adoption_view_working_definition
executor_role:: adoption_view_worker
task_packet:: user_direct_adoption_view_request_2026-05-24
status:: LOOP_DONE

## Adoption decision

adopted_node:: 20260524_072000_llm_wiki_working_definition
adopted_version:: 1.0
source_audit:: .llmwiki/runs/run_20260524_074000_worker_audit_working_definition/audit_report.md
source_audit_decision:: adopt_recommended
version_adopted_at:: 2026-05-24T07:07:58+08:00

The root node metadata now points to version `1.0` with `version_status: adopted`, `status: active`, and `usable_as_support: true`.

## Metadata written

- `nodes/20260524_072000_llm_wiki_working_definition/node.yaml`: created as root adopted node metadata.
- `nodes/20260524_072000_llm_wiki_working_definition/versions/1.0/node.yaml`: updated only for adopted metadata consistency, including `id`, `version_status: adopted`, `adoption_status: adopted`, `adopted: true`, `adoption_gate`, `version_adopted_at`, and passed audit pointers.

## Content changes

No changes were made to:

- `nodes/20260524_072000_llm_wiki_working_definition/versions/1.0/card.md`
- `nodes/20260524_072000_llm_wiki_working_definition/versions/1.0/provenance.md`
- `nodes/20260524_072000_llm_wiki_working_definition/versions/1.0/change.md`

## View/generated artifacts

Official view build commands wrote:

- `kb/20260524_072000_llm_wiki_working_definition.md`
- `kb/_index.yaml`
- `generated/citation_graph.yaml`
- `generated/backlinks.yaml`
- `generated/impact_queue.yaml`
- `generated/status.yaml`

## Result

- Adopted nodes after build: 2.
- KB view cards after build: 2.
- Citation edges after build: 21.
- Impact queue open items: 0.
