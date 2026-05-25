# Empty Next Loop Workspace Placeholder

`status`: `retired_transition_artifact`

This directory was the temporary root `llm_wiki/loop/` placeholder created before the repository adopted the loop-capsule model.

The previous loop's active products now live in:

`loops/v2_llm_wiki_loop_20260525/`

## Recovery Rule

Do not recover a current loop from this placeholder.

A new loop should first define:

- loop objective and non-goals;
- active state schema;
- run / task / audit layout;
- where run-scoped audits should live;
- which old artifacts, if any, are intentionally imported from older loop capsules.

Until that charter exists, `loops/current_loop.json` should keep `active_loop_id` as `null`.
