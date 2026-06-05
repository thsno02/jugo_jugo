---
loop_id: v4_llm_wiki_loop_20260602
created: 2026-06-02
status: phase4b_complete
note: v4 任务清单。实验迭代式推进：build --> test on gist --> refine --> expand。
---

# v4 Task List

> questioning-loop-based 知识卡片生产管线。逐阶段推进，每阶段验证后才进入下一阶段。

---

## Phase 0 -- Setup（脚手架）

- [x] 创建 v4 capsule 目录结构
- [x] 链接 v3 `future_plans/` 设计文档（确认 pipeline_spec / questioning_loop_design / card_metadata_template / jj_template 可访问）
- [x] 验证 `--permission-mode bypassPermissions` + git 权限可正常工作

---

## Phase 1 -- Build Core Skills（构建核心技能）

- [x] 开发 questioning skill (`skills/questioning/SKILL.md`) -- questioner 的 5 阶段 SOP，含 SATISFIED 判据、boundary、提问策略细则
- [x] 开发 reader/answerer prompt (`skills/reader/PROMPT.md`) -- 被动应答者契约，四标准（源忠实、定位精确、卡片就绪、显式不确定性）+ digest production SOP
- [x] 开发 digest production prompt -- 集成在 reader/PROMPT.md 中（scope + toc + core_claims + terms）
- [x] 开发 Q&A --> card reframing 逻辑 (`skills/reframing/PROMPT.md`) -- 对话体转知识陈述体 + metadata 填写 + typed footnote 锚定 + jj creation 事件
- [x] 开发 reviewer prompt (`skills/reviewer/PROMPT.md`) -- quit-audit rubric（覆盖率检查 + 源忠实抽查 + verdict 输出格式）

---

## Phase 2 -- Test on Seed Material（种子材料验证）

- [x] 在 karpathy-gist-llm-wiki（原始基础材料）上运行完整 questioning loop（15 张卡片，reviewer pass）
- [x] 审查产出卡片 -- 17 项问题发现（链接密度、原子性、footnote 格式一致性、摘要 alias 覆盖）
- [x] 基于审查结果迭代 skills -- reframing（cross-link 规则、拆卡信号、alias-in-summary）; reader（统一 footnote 位置格式）; questioning（覆盖率含次要节、原子性检查）; reviewer（链接密度、重叠检测、源节覆盖）
- [x] 迭代改进 -- cross-links 添加到全部卡片、拆分 index-based-navigation（+log-file）、新增 3 张缺失卡（use-case-domains/wiki-as-git-repo/obsidian-tooling）、KB 总计 19 张卡

---

## Phase 3 -- Expand to Small Batch（小批量扩展）

- [x] 处理 3-5 份额外材料（混合 paper / blog / repo 类型） -- 已被 Phase 4 全量处理取代
- [x] 审查卡片 -- 特别关注 inline fusion check（grep KB 查重叠） -- 已被 Phase 4 全量处理取代
- [x] 迭代 skills + reframing 逻辑 -- 已被 Phase 4 全量处理取代
- [x] 测试 justification journal (jj) 创建流程是否完整 -- 已被 Phase 4 全量处理取代

---

## Phase 4 -- Full Init KB（完整初始 KB 构建）

- [x] 处理剩余材料（parallel, wave-based 分批） -- 43 材料全量处理，259 张卡
- [x] 运行 governance pass（dedup + canonical 归一化 + distinction linking） -- canonical 归一化 1 处 + cross-link + 质量抽检 pass
- [x] 人工抽检 5-10 张卡（源忠实性 + 原子性 + metadata 质量） -- 8 张卡源忠实抽检
- [x] 构建 KB index（`kb/indexes/cards.md`，active-only view） -- 259 张 active 卡索引已构建

---

## Phase 4b -- Governance Remediation

- [x] 从 footnotes 派生 related 字段 -- 扫描全部 280 张卡的 `[^card-*]` / `[^dist-*]` 脚注，提取链接目标 slug，union 合并至 related 字段；245 张卡被更新
- [x] 重建 KB index (`kb/indexes/cards.md`) -- 280 张 active 卡，6 种 card_type（mechanism 108 / distinction 65 / source_claim 48 / concept 40 / operational_rule 11 / example_pattern 8）
- [x] 链接统计 -- 861 条 related links，264/280 张卡有链接（94.3%），平均每卡 3.3 条链接

---

## Phase 5 -- Evolve（演化，未来）

- [ ] Mode B synthesis（deferred -- 仅在 v4 Mode A 结果满意后考虑）
- [ ] collect-request 机制（知识缺口 --> 新 source spec）
