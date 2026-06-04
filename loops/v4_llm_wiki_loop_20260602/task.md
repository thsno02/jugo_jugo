---
loop_id: v4_llm_wiki_loop_20260602
created: 2026-06-02
status: active
note: v4 任务清单。实验迭代式推进：build --> test on gist --> refine --> expand。
---

# v4 Task List

> questioning-loop-based 知识卡片生产管线。逐阶段推进，每阶段验证后才进入下一阶段。

---

## Phase 0 -- Setup（脚手架）

- [x] 创建 v4 capsule 目录结构
- [ ] 链接 v3 `future_plans/` 设计文档（确认 pipeline_spec / questioning_loop_design / card_metadata_template / jj_template 可访问）
- [ ] 验证 `--permission-mode bypassPermissions` + git 权限可正常工作

---

## Phase 1 -- Build Core Skills（构建核心技能）

- [ ] 开发 questioning skill (`skills/questioning/SKILL.md`) -- questioner 的 5 阶段 SOP，含 SATISFIED 判据、boundary、提问策略细则
- [ ] 开发 reader/answerer prompt (`skills/reader/PROMPT.md`) -- 被动应答者契约，四标准（源忠实、定位精确、卡片就绪、显式不确定性）
- [ ] 开发 digest production prompt -- reader 的首遍产出（scope + toc + core_claims + terms），供 reviewer 做覆盖率检查
- [ ] 开发 Q&A --> card reframing 逻辑 -- 对话体转知识陈述体 + metadata 填写 + typed footnote 锚定 + jj creation 事件
- [ ] 开发 reviewer prompt -- quit-audit rubric（覆盖率检查 + 源忠实抽查 + verdict 输出格式）

---

## Phase 2 -- Test on Seed Material（种子材料验证）

- [ ] 在 karpathy-gist-llm-wiki（原始基础材料）上运行完整 questioning loop
- [ ] 审查产出卡片 -- 质量、颗粒度、metadata 完整性、typed footnotes 锚定准确性
- [ ] 基于审查结果迭代 skills（questioning / reader / reframing）
- [ ] 在 gist 上重新运行 -- 验证改进效果

---

## Phase 3 -- Expand to Small Batch（小批量扩展）

- [ ] 处理 3-5 份额外材料（混合 paper / blog / repo 类型）
- [ ] 审查卡片 -- 特别关注 inline fusion check（grep KB 查重叠）
- [ ] 迭代 skills + reframing 逻辑
- [ ] 测试 justification journal (jj) 创建流程是否完整

---

## Phase 4 -- Full Init KB（完整初始 KB 构建）

- [ ] 处理剩余材料（parallel, wave-based 分批）
- [ ] 运行 governance pass（dedup + canonical 归一化 + distinction linking）
- [ ] 人工抽检 5-10 张卡（源忠实性 + 原子性 + metadata 质量）
- [ ] 构建 KB index（`kb/indexes/cards.md`，active-only view）

---

## Phase 5 -- Evolve（演化，未来）

- [ ] Mode B synthesis（deferred -- 仅在 v4 Mode A 结果满意后考虑）
- [ ] collect-request 机制（知识缺口 --> 新 source spec）
