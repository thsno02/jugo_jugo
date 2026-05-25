# Validation Trace

decision:: repair_validated

## Validators

Command:

```bash
/opt/homebrew/bin/python3 scripts/kb_validate_card.py nodes/20260524_104000_llm_wiki_risks_governance_and_provenance/versions/1.0/card.md
```

Result:

```text
card validation passed: 1 cards
```

Command:

```bash
/opt/homebrew/bin/python3 scripts/kb_validate_card.py --all
```

Result:

```text
card validation passed: 11 cards
```

## Footnote Layout Gate

Target gate:

```text
nodes/20260524_104000_llm_wiki_risks_governance_and_provenance/versions/1.0/card.md: PASS refs=[25] footnotes=[216] last=(216, '## Footnotes')
```

All-card layout audit:

```text
TOTAL 11 checked; PASS 1; FAIL 10
```

The 10 failures are existing adopted legacy cards or their `kb/` views and were not modified in this repair scope.

