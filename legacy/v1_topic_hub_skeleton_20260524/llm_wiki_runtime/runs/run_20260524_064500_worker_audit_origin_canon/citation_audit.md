# Citation Audit

executor_role:: worker_executor
status:: completed_with_repair_required
target_card:: nodes/20260524_062000_llm_wiki_origin_and_canon/versions/1.0/card.md

## Validator result

Required command:

```sh
python3 scripts/kb_validate_card.py nodes/20260524_062000_llm_wiki_origin_and_canon/versions/1.0/card.md
```

Result: validator command failed before validating the card.

Observed error:

```text
ModuleNotFoundError: No module named 'yaml'
```

Audit interpretation: this is an environment/tooling failure, not a demonstrated card-format failure. It still blocks claiming a clean official parser pass until `PyYAML` is available or the validator is run in the intended environment.

## Independent parser check

Because the official validator could not import `yaml`, a small local parser check was run against the same field contract visible in `scripts/kb_common.py`.

Result:

- `## Footnotes`: present
- `## References`: present
- parseable citation blocks: 7
- required fields present for all parsed blocks: pass
- `target` paths exist for all parsed blocks: pass
- `pinned_version` paths exist for all parsed blocks: pass

Required fields checked:

- `target`
- `target_version`
- `pinned_version`
- `citation_role`
- `why_cited`
- `evidence_summary`

## Citation support review

### Karpathy gist citation

Status: pass.

The gist text supports the card's bounded canonical claims about:

- idea-file framing;
- persistent markdown/wiki layer between raw sources and queries;
- raw sources / wiki / schema structure;
- ingest, query, and lint workflows;
- index/log navigation;
- optional/modular tooling such as search, MCP, Obsidian, Marp, and Dataview.

The card appropriately avoids treating optional tooling as mandatory.

### Hacker News citation

Status: pass.

The HN text supports the card's discourse-only claims about:

- visible story metadata in the text capture;
- RAG / persistent memory / wiki comparisons;
- arguments that the writeback, backlinks, source files, and linting are distinctive;
- concerns about model collapse, second-order information, stale claims, context bloat, quality assurance, maintenance scale, and cognitive offloading.

The card explicitly frames these as early discourse notes and does not use them to settle the technical classification question.

### Evidence-boundary and gap citations

Status: fail, repair required.

The card cites process artifacts to support evidence-boundary and gap claims. The boundary role is appropriate in principle, but the candidate states that local X raw files and HN `item.json` are empty. Current filesystem checks contradict that:

- `data/raw/webpage/karpathy-x-launch-post/text.txt`: 11825 bytes, contains JSON with tweet text, metrics, created_at, and quoted tweet text.
- `data/raw/webpage/karpathy-x-launch-post/raw.txt`: 11825 bytes, same apparent JSON capture.
- `data/raw/webpage/karpathy-x-launch-post/raw.json`: 11825 bytes, same apparent JSON capture.
- `data/raw/hacker_news/hacker-news-original-thread/item.json`: 1018 bytes, contains structured HN story metadata including `score`, `descendants`, `time`, `title`, and `url`.

This does not mean the candidate must use X claims, and the card correctly does not rely on X for exact X wording. But the claim that those files are empty is false in the current checkout and must be repaired before adoption.

## Overclaim review

- Gist-backed technical observations: pass.
- Working definition: pass with stated interpretation boundary.
- HN discourse notes: pass.
- HN risk vocabulary: pass as discourse seed only.
- X/HN JSON empty-file gap: fail due current file contents.
- Broad adoption, enterprise readiness, empirical effectiveness, historical lineage: pass, explicitly out of scope.

## Citation audit decision

Decision: repair_before_adoption.

Repair items:

1. Re-run the official card validator in an environment with `yaml`/`PyYAML` available and record a real pass/fail.
2. Repair all candidate statements that say X raw files or HN `item.json` are empty. Either update the source-boundary language to reflect that these files now contain local captures, or explain why they are disallowed despite containing data.
3. If X/HN JSON data remains excluded by task scope rather than by emptiness, state that as a process-boundary decision instead of an empty-file evidence claim.
