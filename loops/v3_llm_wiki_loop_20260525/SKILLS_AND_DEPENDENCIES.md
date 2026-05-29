# Skills And Dependencies V3

Claude Code does not inherit Codex skills. V3 must run from local files only.

## Assumptions

- No `agent-loop-runner` skill is installed.
- No `llmwiki-*` skills are installed.
- No hidden prompt memory is available.
- The v3 capsule is the source of truth for process, card contract, provenance, and role boundaries.

## Required Local Skill Contracts

These are not installed packages. They are role contracts defined by local files.

### loop_controller

Source files:

- `CLAUDE_CODE_HANDOFF.md`
- `RUNBOOK.md`
- `loop_manifest.json`
- `loop_state.json`
- `CONTEXT_BOUNDARY.md`
- `SUBAGENT_RUNTIME_CONSTRAINTS.md`

Responsibilities:

- maintain loop state;
- enforce phase-specific read/write boundaries;
- create task packets and queue entries;
- update reports and delivery notes;
- avoid becoming the production worker unless explicitly recorded as an exception.

### material_to_draft

Source files:

- `CARD_CONTRACT_V3.md`
- `DRAFT_FIRST_PIPELINE_V3.md`
- `CONTEXT_BOUNDARY.md`

Responsibilities:

- read only the current material task and named source files;
- write knowledge-dense draft cards;
- write draft provenance;
- avoid reading accepted-card bodies or v2 process history.

### title_similarity_top3

Source files:

- `SIMILARITY_MECHANISM_V3.md`
- `CONTEXT_BOUNDARY.md`

Responsibilities:

- tokenize draft and accepted card titles with Jieba;
- compute Jaccard set similarity;
- write top 3 candidate results;
- avoid reading card bodies or provenance in this phase.

### comparison_provenance

Source files:

- `PROVENANCE_CONTRACT_V3.md`
- `DRAFT_FIRST_PIPELINE_V3.md`
- `CONTEXT_BOUNDARY.md`

Responsibilities:

- read only the draft and top 3 candidate cards/provenance needed for the decision;
- answer the three comparison questions;
- classify the next action as `new_card`, `merge_candidate`, `provenance_delta`, `duplicate_skip`, or `revise_before_gate`.

### publication_gate

Source files:

- `CARD_CONTRACT_V3.md`
- `PROVENANCE_CONTRACT_V3.md`

Responsibilities:

- decide whether a `new_card` draft has enough knowledge value and source support;
- reject title restatement;
- adopt only passing cards into `outputs/llm_wiki/kb/cards/`.

### fusion_audit

Source files:

- `PROVENANCE_CONTRACT_V3.md`
- `CONTEXT_BOUNDARY.md`

Responsibilities:

- audit `merge_candidate` and `provenance_delta`;
- verify comparison provenance answered the three questions;
- verify target card scope is preserved;
- require links from accepted-card provenance back to comparison provenance.

### mailbox_ops

Source files:

- `BRAIN_MAILBOX_PROTOCOL.md`
- `RUNBOOK.md`

Responsibilities:

- keep `brains/*` inbox/outbox/queue/wake files coherent;
- update `queues/`;
- keep `reports/loop_report.md` and `loop_state.json` current.

## Runtime Dependencies

Required:

- `git`
- `rg` if available, otherwise `find`/`grep`
- `python3`
- Python package `jieba` for `title_similarity_top3`

No dependency is required for Markdown authoring or JSON/JSONL validation beyond Python standard library.

## Dependency Preflight

Run from repository root:

```bash
pwd
git status --short --branch
python3 --version
python3 - <<'PY'
import json
print("json ok")
PY
python3 - <<'PY'
import jieba
print("jieba ok", getattr(jieba, "__version__", "unknown"))
PY
```

If `jieba` is missing, install it only if the environment permits package installation:

```bash
bash loops/v3_llm_wiki_loop_20260525/tools/bootstrap_dependencies.sh
```

If `jieba` cannot be installed, block `title_similarity_top3` and report `LOOP_BLOCKED`. Do not silently replace Jieba with another tokenizer.

## Validation Commands

Run after structural edits:

```bash
git diff --check
python3 -m json.tool loops/v3_llm_wiki_loop_20260525/loop_manifest.json >/dev/null
python3 -m json.tool loops/v3_llm_wiki_loop_20260525/loop_state.json >/dev/null
python3 -m json.tool loops/v3_llm_wiki_loop_20260525/status.json >/dev/null
python3 - <<'PY'
import json, pathlib
for path in pathlib.Path("loops/v3_llm_wiki_loop_20260525").rglob("*.jsonl"):
    with path.open() as f:
        for lineno, line in enumerate(f, 1):
            if line.strip():
                json.loads(line)
print("jsonl ok")
PY
```

## Important Non-Dependencies

Do not assume:

- Codex custom skills;
- browser tools;
- MCP tools;
- prior conversation summaries;
- root-level stable `llm_wiki/`;
- automatic mailbox wake hooks.
- nested subagent support.

Process-level nested Claude calls are allowed only when the prompt is self-contained. See `SUBAGENT_RUNTIME_CONSTRAINTS.md`.
