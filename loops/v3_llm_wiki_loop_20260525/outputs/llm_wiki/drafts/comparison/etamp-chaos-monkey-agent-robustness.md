---
schema: comparison_provenance.v3
draft_card: ../cards/etamp-chaos-monkey-agent-robustness.md
draft_provenance: ../provenance/etamp-chaos-monkey-agent-robustness.md
similarity_result: ../similarity/etamp-chaos-monkey-agent-robustness.json
existing_cards:
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0
  - card_id: idea-file-share-the-idea
    card_path: llm_wiki/kb/cards/idea-file-share-the-idea.md
    score: 0.0
  - card_id: llm-wiki-health-checks
    card_path: llm_wiki/kb/cards/llm-wiki-health-checks.md
    score: 0.0
decision: new_card
audit_required: false
created_time: 2026-05-26T16:06:00+08:00
edited_time: 2026-05-26T16:06:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三个 top 候选与 draft "Chaos Monkey for Agents：用概率性扰动模拟真实 web 环境压力" **完全无 token 共享**（score 全部 0.000、`shared_tokens: []`）。这三张 v2 卡都来自同一条 Karpathy "llm wiki" launch 推文，是 v2 仅 15 张卡时被算法兜底排进 top 3，与本 draft 无实质邻近。

## 2. draft 与候选在哪里不同

- draft 主题：ETAMP 借 Netflix Chaos Monkey 思路设计的 web agent 动作层概率扰动器（Click Drop / Scroll Swap / Type Transform），关键约束是"扰动后任务仍可完成"，目的在于隔离"压力下安全性"与"任务难度"。论据轴属于 chaos engineering + agent evaluation。
- 候选 1：Karpathy 推文对 idea file 抽象性表述。
- 候选 2：Karpathy 推文对 idea file 分享逻辑表述。
- 候选 3：LLM 对 wiki 的 `health checks` 清理（这是唯一一个名字里含 "checks/检查" 字面的卡，但语义是"找不一致数据/补全缺失/找连接"，与 chaos monkey 的"概率性破坏"完全不同——前者是 wiki 维护，后者是 agent runtime 压测）。

draft 与三个候选无任何论据共享，也不是"同主题不同视角"。

## 3. 下一步的核心依据

(1) 无 token 共享 + (2) 即便 `llm-wiki-health-checks` 字面有"检查"色彩，bodies 上一个谈 wiki 数据清理 / 一个谈 agent action 层扰动，主题不同 → `new_card`。draft 给出了完整操作定义、参数默认值、设计 rationale、步数补偿规则、边界，证据完整不需 revise；v2 也无可反向链接的近邻 → 不是 `provenance_delta`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进入 publication_gate；与 ETAMP 系列内的 `etamp-environment-injected-memory-poisoning`、`etamp-capability-vs-security` 在 v3 related 字段挂连。

## 5. 备注

`llm-wiki-health-checks` 是常见"误中"候选——名字含"检查"但 score 仍然是 0；这恰好说明 jieba 不会把"health checks"与"chaos monkey 扰动"对齐。
