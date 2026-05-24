# Mining Trace

run_id:: run_20260524_094000_worker_source_mining_vs_rag_write_loop
executor_role:: cand_010_vs_rag_write_loop source-mining worker
task_packet:: current user/controller packet
status:: LOOP_DONE

## Allowed Inputs

Required control files and skill docs, `generated/status.yaml`, source manifests, local `data/raw/` files, adopted KB anchors, and prior worker delivery files.

## Commands / Checks

- Read required control and skill files with `sed`.
- Located candidate and comparison sources with `rg` and `find`.
- Verified byte size and readability with `wc -c`, `sed`, and `rg`.
- Mined local source text only.
- No network retrieval attempted.

## Outputs Written

- `task.md`
- `source_inventory.md`
- `source_notes.md`
- `evidence_matrix.yaml`
- `frontier_update.md`
- `next_task_packet.md`
- `loop_status.md`
- `loop_delivery.md`
- `source_scope.md`
- `source_mining.md`
- `candidate_frontier_delta.yaml`
- `evidence_gaps.md`
- `retrieval_requests.md`
- `mining_trace.md`
- `frontier_trace.md`

LOOP_DONE

