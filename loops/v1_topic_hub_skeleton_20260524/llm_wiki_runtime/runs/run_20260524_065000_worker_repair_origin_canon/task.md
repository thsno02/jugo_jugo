# Repair Task

executor_role:: repair_worker
status:: completed
target_node_id:: 20260524_062000_llm_wiki_origin_and_canon
target_version:: 1.0
run_id:: run_20260524_065000_worker_repair_origin_canon

## Objective

Repair the origin/canon candidate bundle and current frontier boundary after audit found false empty-file claims for:

- `data/raw/webpage/karpathy-x-launch-post/text.txt`
- `data/raw/webpage/karpathy-x-launch-post/raw.txt`
- `data/raw/webpage/karpathy-x-launch-post/raw.json`
- `data/raw/hacker_news/hacker-news-original-thread/item.json`

## Required Boundaries

- Do not adopt the node.
- Preserve `version_status: candidate_pending_audit`.
- Do not write root `nodes/20260524_062000_llm_wiki_origin_and_canon/node.yaml`.
- Do not write `kb/` or `generated/`.
- Do not perform network retrieval.
- Keep HN discourse as discourse, not technical proof.
- Do not overclaim adoption, implementation ecosystem, enterprise suitability, or empirical effectiveness.

## Allowed Repair Outputs

- Candidate version bundle files under `nodes/20260524_062000_llm_wiki_origin_and_canon/versions/1.0/`
- `.llmwiki/control/knowledge_frontier.yaml` because it contained the false empty-file claim
- This repair run's `task.md`, `repair_report.md`, `skill_failure_note.md`, `loop_status.md`, and `loop_delivery.md`
- Minimal skill patches requiring file-size/content verification before declaring files empty
