# Change: genesis -> 1.0

node_id:: 20260524_062000_llm_wiki_origin_and_canon
from_version:: genesis
to_version:: 1.0
change_scale:: major
propagation_required:: false
created_at:: 2026-05-24T06:40:00+08:00
run_id:: run_20260524_064000_worker_generation_origin_canon
adoption_status:: pending_audit

## Why this node was created

This node was created because `cand_001_origin_and_canon` is the current ready-to-build frontier candidate for the LLM Wiki topic. It provides a bounded anchor for later working-definition, architecture, workflow, comparison, risk, and evaluation nodes.

## Why this first version is acceptable

The first version is acceptable as a candidate because it stays inside the repaired generation packet:

- primary canonical claims are supported by the Karpathy gist;
- early discourse claims are supported only by the HN text capture;
- X launch material is limited to bounded launch-context/source-inventory evidence and does not support adoption, ecosystem, enterprise, or empirical-effectiveness claims;
- root adopted metadata is not written.

It is not acceptable for adoption until citation/adoption audit passes.

## Evidence basis

Primary evidence:

- `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt`

Secondary early-discourse evidence:

- `data/raw/hacker_news/hacker-news-original-thread/text.txt`

Gap/inventory evidence:

- non-empty `data/raw/webpage/karpathy-x-launch-post/text.txt`
- non-empty `data/raw/webpage/karpathy-x-launch-post/raw.txt`
- non-empty `data/raw/webpage/karpathy-x-launch-post/raw.json`
- non-empty `data/raw/hacker_news/hacker-news-original-thread/item.json`

Process authority:

- `.llmwiki/runs/run_20260524_063500_worker_node_planning_repair_origin_canon/next_task_packet.md`
- `.llmwiki/runs/run_20260524_063000_worker_node_planning_origin_canon/evidence_scope.yaml`
- `.llmwiki/runs/run_20260524_065000_worker_repair_origin_canon/repair_report.md`

## Known limits

- This version does not claim complete historical origin before the bounded source batch.
- This version does not claim broad adoption, enterprise readiness, empirical effectiveness, or mature implementation ecosystem.
- This version does not cite exact X wording, timestamps, quoted-post text, or metrics.
- This version treats HN comments as early discourse rather than settled technical conclusions.

## Expected future changes

- Add or revise X launch details if a later source audit finds material conflicts or broader source mining authorizes wider claims.
- Refine the working definition after a dedicated working-definition node is generated.
- Split architecture, workflow, comparison, risk, governance, and evaluation claims into dedicated nodes after their own source mining.
- If adopted later, create root `nodes/20260524_062000_llm_wiki_origin_and_canon/node.yaml` and any `kb/` view only through the adoption gate.
