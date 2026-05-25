# status

`status`: `AUDIT_DONE`

# audit_result

`audit_result`: `concern`

Atomic Draft First 的方向正确，应该成为下一版主流程，但当前控制面还需要一次小修正再进入稳定执行：把“轻量 title similarity top3”和“三问 comparison”拆成两个清楚阶段，或明确由主控/工具先生成 top3 再派发 comparison worker；同时把卡片质量门从“atomic fact”改成“scoped knowledge card”。

本审计明确区分：

- 已提交历史：单卡串行链路已经稳定产出 15 张 accepted cards；已提交的 Draft First 粗流程已经把方向改成 batch draft、similarity gate、后置 audit/publication。
- 当前未提交控制面草稿：`DRAFT_FIRST_PIPELINE.md`、`RUNBOOK.md`、`draft_backlog.md`、`card_similarity_gate_*` 的三问 comparison / fusion provenance 细化仍是工作区修改；`card_fusion_audit_*` 与 `card_fusion_adoption_*` 还是未跟踪新文件，不能当作已稳定落地的历史规则。

# evidence_read

## allowed evidence read so far

- `llm_wiki/loop/DRAFT_FIRST_PIPELINE.md`
- `llm_wiki/loop/RUNBOOK.md`
- `llm_wiki/loop/loop_state.json`
- `llm_wiki/loop/queues/task_queue.md`
- `llm_wiki/loop/reports/loop_report.md`
- `llm_wiki/kb/indexes/cards.md`
- `llm_wiki/kb/cards/*`
- `llm_wiki/kb/provenance/*`
- `llm_wiki/loop/task_templates/card_drafting_task.md`
- `llm_wiki/loop/system_prompts/card_drafting_worker.md`
- `llm_wiki/loop/audits/20260525-subagent-lifecycle-session-audit/*`

## additional read reasons

- Need to read git status, git diff, and HEAD snapshots of selected allowed control-plane files to distinguish committed history from current uncommitted control-plane draft, as requested by this audit task.
- Need to read `llm_wiki/loop/queues/draft_backlog.md` because current `task_queue.md`, `loop_state.json`, and `loop_report.md` all claim candidate 11 has been moved into draft backlog, but the backlog file itself was not in the allowed list.
- Need to read batch/similarity task templates and system prompts if present because the requested audit centers on whether the next flow should become `material -> draft card -> similarity top3 -> three-question comparison -> decision -> merge/publication audit`, while the explicitly allowed single-card drafting prompt only describes the old one-card worker.

## additional evidence read

- `git status --short`
- `git diff --name-status`
- `git diff -- llm_wiki/loop/DRAFT_FIRST_PIPELINE.md llm_wiki/loop/RUNBOOK.md llm_wiki/loop/queues/draft_backlog.md llm_wiki/loop/task_templates/card_similarity_gate_task.md llm_wiki/loop/system_prompts/card_similarity_gate_worker.md`
- `git show HEAD:llm_wiki/loop/DRAFT_FIRST_PIPELINE.md`
- `git show HEAD:llm_wiki/loop/RUNBOOK.md`
- `git show HEAD:llm_wiki/loop/queues/draft_backlog.md`
- `git show HEAD:llm_wiki/loop/task_templates/card_similarity_gate_task.md`
- `llm_wiki/loop/queues/draft_backlog.md`
- `llm_wiki/loop/task_templates/card_batch_drafting_task.md`
- `llm_wiki/loop/system_prompts/card_batch_drafting_worker.md`
- `llm_wiki/loop/task_templates/card_similarity_gate_task.md`
- `llm_wiki/loop/system_prompts/card_similarity_gate_worker.md`
- `llm_wiki/loop/task_templates/card_fusion_audit_task.md`
- `llm_wiki/loop/system_prompts/card_fusion_audit_worker.md`
- `llm_wiki/loop/task_templates/card_fusion_adoption_task.md`
- `llm_wiki/loop/system_prompts/card_fusion_adoption_worker.md`

## committed vs current draft evidence

- `git status --short` shows modified current-control-plane files: `llm_wiki/loop/DRAFT_FIRST_PIPELINE.md`, `llm_wiki/loop/RUNBOOK.md`, `llm_wiki/loop/queues/draft_backlog.md`, `llm_wiki/loop/system_prompts/card_similarity_gate_worker.md`, and `llm_wiki/loop/task_templates/card_similarity_gate_task.md`.
- `git status --short` also shows untracked fusion control-plane drafts: `card_fusion_adoption_worker.md`, `card_fusion_audit_worker.md`, `card_fusion_adoption_task.md`, and `card_fusion_audit_task.md`.
- `loop_state.json`, `queues/task_queue.md`, `reports/loop_report.md`, `kb/cards/*`, `kb/provenance/*`, and `kb/indexes/cards.md` were not listed as dirty. The current KB state and queue/report snapshot are therefore not part of this uncommitted refinement.
- HEAD version of `DRAFT_FIRST_PIPELINE.md` already contains the coarse Atomic Draft First idea: `已挖掘来源 / exhausted 来源 -> 批量 atomic draft -> 相似卡门禁 -> draft backlog -> 批量 audit -> public adoption`.
- Current working tree refines that into: `material / exhausted 来源 -> atomic draft card + draft provenance -> 快速相似候选列举 -> 阅读相似卡并回答三问 -> draft backlog -> 融合审计或发布审计 -> public adoption`.
- HEAD version of `card_similarity_gate_task.md` only required a classification and an existing-card pointer. Current working tree adds comparison provenance, three questions, and `audit_required`.
- Current KB card/provenance/index files contain no frontmatter-style `tags`, `created_time`, `edited_time`, `edited_entity`, `references`, or `footnotes` fields. References and Footnotes exist as markdown sections, not metadata schema.

# current_flow_diagnosis

## why single-card serial throughput is low

The old stable chain was safe but expensive:

```text
source mining
-> choose one candidate
-> card_drafting_worker
-> card_audit_worker
-> card_adoption_worker
-> state/report/queue/decision updates
-> repeat
```

For each accepted card, the loop paid the fixed cost of task creation, dispatch rendering, worker startup, `loop_status.md`, `read_log.md`, `loop_delivery.md`, delivery inspection, decision recording, state/report updates, and sub-agent lifecycle cleanup. The report records 24 fact candidates, 16 valid drafting artifacts, 15 accepted cards, one audit revise, and several prompt/tool repair loops. That is good safety evidence, but it explains why 15 accepted cards took many hours.

The throughput problem is therefore not primarily that an individual draft is slow. It is that every candidate immediately enters the expensive audit/adoption/publication lane before the system has amortized source reading, drafting, and similarity identity checks across a batch.

## why Atomic Draft First is directionally right

Drafting is source-local: a worker can transform several candidates from the same exhausted/material source into draft cards and draft provenance without reading accepted KB cards. That is the cheapest place to batch work.

Identity, duplicate, merge, and provenance-delta decisions are KB-global: they should happen after draft creation and should read only a small set of likely similar accepted cards. Moving those decisions into a similarity/comparison gate preserves safety while avoiding “write one, audit one, adopt one” thrash.

The current draft-first design also keeps an important safety line: draft backlog is not public KB, and similarity gate is not fact audit.

## where the current understanding is biased

The phrase `atomic fact` is now doing too much work. Existing accepted cards are not bare single facts; they are small, scoped knowledge cards with a statement, support, scope, provenance, references, and sometimes one compact explanatory paragraph. That is the right shape. If the next loop interprets “atomic” too literally, it will fragment useful cards into context-free crumbs and increase merge pressure.

The better gate is: one scoped claim boundary per card, not one microscopic sentence per card.

## current uncommitted control-plane gap

The current working tree correctly adds three-question comparison and fusion/provenance-delta audit concepts, but the similarity gate template still mixes two actions:

```text
list likely similar accepted cards
read listed accepted cards and write comparison provenance
```

The template both says the worker should first list possible similar accepted cards and requires `similar_existing_card_paths` in the task packet. That is ambiguous. Either the main-agent/tool must precompute title-similarity top3 and put those paths into the comparison task, or the flow must split into a top3 listing task followed by a comparison task.

# findings

## P0

No P0 blocker found. The current design does not authorize public KB writes without audit, and it keeps draft backlog separate from accepted KB.

## P1

- Single-card serial is structurally low-throughput. It made every candidate pay the full worker/audit/adoption/control-plane fixed cost. It is reliable but cannot scale without batching.
- The next-flow draft is directionally correct but not yet internally crisp: title-similarity top3 and three-question comparison should be separate stages or explicitly assigned to different actors. Current `card_similarity_gate_task.md` asks for prelisted similar paths while also making the worker responsible for first listing candidates.
- The quality gate should be changed from `atomic fact card` to `scoped knowledge card`. Current accepted cards already behave this way; the drafting/batch prompts still risk over-narrowing by repeating “atomic fact”.
- Fusion/provenance-delta flow is not part of committed stable history yet. The RUNBOOK working tree references `card_fusion_audit_worker` and fusion adoption actions, while their templates/prompts are untracked draft files.

## P2

- Metadata should remain out of the card drafting gate for now. `tags`, `created_time`, `edited_time`, and `edited_entity` would add coordination cost and invite taxonomy/coverage drift before there is failure evidence that the loop needs them.
- Current accepted cards have small formatting variation: some use bullet-form fields, some plain `statement:` lines, some include a `Provenance` section and some rely on separate provenance files. This is not blocking, but a lightweight normalizer would help title/statement similarity.
- `draft_backlog.md` has the right recovery purpose but should grow artifact columns for `top3_candidates`, `comparison_provenance`, `decision`, `fusion_audit`, `publication_audit`, and `final_adoption` so the next run can resume without reading chats.

# proposed_next_flow

Yes: the next version should become:

```text
material / exhausted source
-> batch scoped draft cards + draft provenance
-> register draft backlog
-> lightweight title/statement similarity top3 from kb index
-> three-question comparison against top3 accepted cards
-> decision
   -> new_atomic_card / new_scoped_card: publication audit
   -> merge_candidate: fusion audit, then fusion adoption
   -> provenance_delta: provenance-delta audit, then fusion/provenance adoption
   -> duplicate_skip: close backlog with comparison provenance
   -> revise_before_gate: return only that draft to revision
-> accepted KB only after audit_result pass
```

Implementation shape:

- `batch_drafting_worker` reads only the source candidate set and source evidence. It writes draft cards, draft provenance, and `batch_manifest.md`.
- `similarity_top3` should be tool-like or a tiny worker: read draft title/statement plus `kb/indexes/cards.md`, output top3 accepted card paths with a short lexical/semantic reason. It should not read accepted card bodies.
- `comparison_gate_worker` reads each draft, draft provenance, and top3 accepted card bodies. It answers:
  - Why do the draft and A card have commonality?
  - What is different?
  - What is the basis for next action?
- `decision` writes a durable artifact, not only chat text. The decision should update backlog status and link comparison provenance.
- `publication_audit_worker` audits only drafts classified as new cards.
- `card_fusion_audit_worker` audits `merge_candidate` and `provenance_delta` before any accepted card/provenance write.
- `card_fusion_adoption_worker` updates only the accepted A card provenance by default; A card body edits require explicit task authorization and audit approval.

# card_quality_gate

Replace `atomic fact` with `scoped knowledge card`.

A scoped knowledge card passes when:

- It has one clear claim boundary.
- The claim is supported by the specified source evidence.
- It includes `statement`, `fact_type`, `support`, `scope`, and `status`.
- It is readable as a small zet-style card, not a task log or intermediate artifact.
- It may include a compact explanatory paragraph if needed for understanding.
- It does not become a hub, cluster, topic overview, or coverage page.
- It keeps `References` before `Footnotes`, and `Footnotes` is the final section.
- It has a separate provenance artifact explaining source, support, explicit-vs-organized wording, scope, and draft/accepted status.

It should fail or revise when:

- The card is so atomic that it loses the useful knowledge unit and would need immediate merging to be readable.
- The card combines multiple unrelated claims under a topic heading.
- The support/scope boundary depends on agent synthesis rather than source evidence.
- The card requires new metadata or tags to be understandable.

Schema impact:

- `metadata`: keep control-plane metadata in backlog/provenance/audit artifacts, not in every card body.
- `tags`: defer. Tags create taxonomy work and can pull the loop back toward topic coverage.
- `created_time`: if needed, set deterministically at adoption/publication, not by drafting workers.
- `edited_time`: only update during accepted-card/provenance adoption, ideally by a tool or adoption worker.
- `edited_entity`: useful for fusion/provenance-delta audit trails, but should live in provenance/adoption logs unless a proven reader need appears.
- `references`: keep as card markdown section and provenance link, not only metadata.
- `footnotes`: keep as final markdown section; allow `无` / empty note when no extra note is needed.

# next_actions

- Revise the uncommitted Draft First control-plane draft before treating it as stable: explicitly split `similarity_top3` from `comparison_gate`, or state that main-agent/tool computes top3 and passes `similar_existing_card_paths` to the worker.
- Rename the drafting quality language from `atomic fact card` to `scoped knowledge card` in batch/single drafting prompts and templates while preserving the anti-hub/anti-cluster guardrail.
- Keep the fusion audit/adoption files as draft until reviewed; do not let RUNBOOK references imply those untracked files are already stable history.
- Add backlog columns or linked artifacts for top3 candidates, comparison provenance, decision, fusion audit, publication audit, and final adoption.
- Do not add tags/created/edited metadata to card drafting. If timestamps/editor records become necessary, add them at adoption/fusion-adoption or provenance-audit layer.
