# Similarity Mechanism V3

V3 uses a deliberately simple similarity mechanism.

## Goal

Similarity is only a fast pre-check. It narrows the comparison set for a new draft card so agents do not repeatedly read the whole KB.

It does not decide truth, duplication, fusion, or publication.

## Algorithm

Input:

- draft card title;
- accepted card title index;
- optional aliases from accepted cards when available.

Steps:

1. Normalize title text by lowercasing ASCII and trimming punctuation.
2. Use Jieba to tokenize Chinese text.
3. Keep token sets rather than token counts.
4. Compute Jaccard similarity:

```text
score = |tokens(draft_title) intersection tokens(existing_title)| / |tokens(draft_title) union tokens(existing_title)|
```

5. Sort descending by score.
6. Keep top 3 candidates.

## Output Schema

```json
{
  "draft_card": "outputs/llm_wiki/drafts/cards/example.md",
  "draft_title": "Example title",
  "tokenizer": "jieba",
  "metric": "jaccard_set_similarity",
  "candidates": [
    {
      "rank": 1,
      "card_id": "existing-card-id",
      "card_path": "path/to/existing-card.md",
      "title": "Existing title",
      "score": 0.42,
      "shared_tokens": ["token"]
    }
  ],
  "created_time": "2026-05-25T20:54:47+08:00"
}
```

## Interpretation

- High score means "read this candidate first."
- Low score does not prove the draft is new.
- Top 3 comparison is enough for the first v3 experiment.
- If repeated misses appear in audit, improve the mechanism later instead of expanding manual reading now.
