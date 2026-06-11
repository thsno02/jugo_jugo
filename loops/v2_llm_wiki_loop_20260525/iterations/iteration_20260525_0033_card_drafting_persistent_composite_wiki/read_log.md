# read_log

- path: `~/.codex/skills/agent-loop-runner/SKILL.md`
  reason: 开发者环境要求在 loop / agent loop 任务中使用该技能。
  use: 只读取与磁盘状态、交付物和循环执行约束相关的最低限度说明；不作为事实来源。
- path: `llm_wiki/loop/iterations/iteration_20260525_0033_card_drafting_persistent_composite_wiki/task.md`
  reason: 当前任务包是本轮唯一任务来源。
  use: 确认候选、允许输入、允许写入、成功门禁和最终回复格式。
- path: `llm_wiki/loop/iterations/iteration_20260525_0002_source_mining_karpathy_gist/artifacts/fact_candidates.md`
  reason: 任务允许用该文件核对候选 4 字段。
  use: 使用第 36-42 行的候选 4 字段；一次关键词定位返回了其它候选的命中行，但未用于知识卡或出处论证。
- path: `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt`
  reason: 任务指定第 13 行为候选 4 的来源证据。
  use: 只使用第 13 行支撑事实陈述。
- path: `llm_wiki/loop/iterations/iteration_20260525_0033_card_drafting_persistent_composite_wiki/`
  reason: 确认允许写入目标文件是否已存在。
  use: 只查看文件名；未读取额外文件内容。
- path: `llm_wiki/loop/iterations/iteration_20260525_0033_card_drafting_persistent_composite_wiki/loop_status.md`
  reason: 结束前验证状态文件存在并包含完成标记。
  use: 只用于成功门禁检查。
- path: `llm_wiki/loop/iterations/iteration_20260525_0033_card_drafting_persistent_composite_wiki/loop_delivery.md`
  reason: 结束前验证交付文件存在并包含 `LOOP_DONE`。
  use: 只用于成功门禁检查。
- path: `llm_wiki/loop/iterations/iteration_20260525_0033_card_drafting_persistent_composite_wiki/read_log.md`
  reason: 结束前验证读日志存在。
  use: 只用于成功门禁检查。
- path: `llm_wiki/loop/iterations/iteration_20260525_0033_card_drafting_persistent_composite_wiki/artifacts/draft_card.md`
  reason: 结束前验证知识卡字段齐全、`References` 在 `Footnotes` 前且 `Footnotes` 为最后一个 section。
  use: 只用于成功门禁检查。
- path: `llm_wiki/loop/iterations/iteration_20260525_0033_card_drafting_persistent_composite_wiki/artifacts/provenance.md`
  reason: 结束前验证出处论证文件存在。
  use: 只用于成功门禁检查。
