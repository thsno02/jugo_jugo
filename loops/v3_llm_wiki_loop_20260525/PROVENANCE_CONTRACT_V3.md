# Provenance Contract V3

V3 separates card provenance from comparison provenance.

## Card Provenance

Card provenance explains where the card's knowledge came from. It is linked by the card metadata field `provenance_card`.

It should include:

- source material ids;
- evidence fragments or locators;
- why the card scope is valid;
- publication gate result.

## Comparison Provenance

Comparison provenance explains a decision between a new draft card and an existing A card.

Required fields:

```yaml
---
schema: comparison_provenance.v3
draft_card:
existing_card:
similarity_result:
decision:
audit_required:
created_time:
edited_time:
edited_entity: llm
---
```

Required questions:

1. Why does the draft appear to share something with A?
2. Where is the draft different from A?
3. What is the core basis for the next action?

## Audit Requirement

`merge_candidate` and `provenance_delta` require audit before adoption.

The audit checks:

- whether the three questions were actually answered;
- whether the existing A card was read rather than inferred from title only;
- whether the proposed body/provenance change preserves A's scope;
- whether the new provenance link is incremental and recoverable.

## Link Rule

If a fusion or provenance-delta action passes audit, the accepted A card provenance must link to the comparison provenance. The comparison artifact is part of A's provenance history.

For `new_card`, comparison provenance can remain linked from the new card provenance when top 3 candidates were reviewed.
