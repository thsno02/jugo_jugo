# Validation Trace

executor_role:: independent_reaudit_worker
status:: completed

## Python Discovery

Default Python interpreters:

- `python3` -> `~/miniforge3/bin/python3`; `import yaml` failed with `ModuleNotFoundError`.
- `python` -> `~/miniforge3/bin/python`; `import yaml` failed with `ModuleNotFoundError`.

Repository-local/system interpreters found that can import PyYAML:

- `/opt/homebrew/bin/python3`; resolved executable `/opt/homebrew/opt/python@3.14/bin/python3.14`; PyYAML `6.0.3`.
- `/usr/bin/python3`; resolved executable `/Library/Developer/CommandLineTools/usr/bin/python3`; PyYAML `6.0.3`.
- `/opt/homebrew/opt/python@3.14/libexec/bin/python`; resolved executable `/opt/homebrew/opt/python@3.14/bin/python3.14`; PyYAML `6.0.3`.

## Official Card Validator

Command:

```sh
/opt/homebrew/bin/python3 scripts/kb_validate_card.py nodes/20260524_062000_llm_wiki_origin_and_canon/versions/1.0/card.md
```

Result:

```text
card validation passed: 1 cards
```

Exit status: `0`.

## Citation Parser Check

Using `scripts.kb_common.parse_card_citations`, the card produced 9 parseable citation blocks:

- Footnotes: `1`, `2`, `3`, `4`, `5`
- References: `R1`, `R2`, `R3`, `R4`

All parsed `pinned_version` paths resolved to existing files.

## Node Validator Boundary Check

Command:

```sh
/opt/homebrew/bin/python3 scripts/kb_validate_node.py nodes/20260524_062000_llm_wiki_origin_and_canon
```

Result:

```text
nodes/20260524_062000_llm_wiki_origin_and_canon: missing root node.yaml
node validation failed: 1 errors across 1 nodes
```

Exit status: `1`.

Interpretation: this is expected before adoption because root node metadata has not been written. It is not a card-citation failure and was not treated as a blocker for recommending adoption.

## Source-State Spot Checks

Command:

```sh
wc -c data/raw/webpage/karpathy-x-launch-post/text.txt data/raw/webpage/karpathy-x-launch-post/raw.txt data/raw/webpage/karpathy-x-launch-post/raw.json data/raw/hacker_news/hacker-news-original-thread/item.json
```

Result:

```text
11825 data/raw/webpage/karpathy-x-launch-post/text.txt
11825 data/raw/webpage/karpathy-x-launch-post/raw.txt
11825 data/raw/webpage/karpathy-x-launch-post/raw.json
 1018 data/raw/hacker_news/hacker-news-original-thread/item.json
36493 total
```

The repaired bundle's non-empty source-state statements match the current checkout.
