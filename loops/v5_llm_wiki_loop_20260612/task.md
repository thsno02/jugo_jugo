---
loop_id: v5_llm_wiki_loop_20260612
created: 2026-06-12
status: setup
note: v5 任务清单。吸收 v4 全部经验，独立 0->1 执行。
---

# v5 Task List

> questioning-loop-based 知识卡片生产管线第五次迭代。逐阶段推进，每阶段验证后才进入下一阶段。

---

## Phase 0 -- Setup（脚手架）

- [ ] 读 v4 learnings（7 份文档）理解全貌
- [ ] 实现 source_router.py（逐类型 boundary-read dispatch）
- [ ] 更新 reframing skill（hedge 保留 + evidence_basis）
- [ ] 验证 bypassPermissions + model:opus 工作正常

---

## Phase 1 -- Build/Update Skills（构建核心技能）

- [ ] 从 v4 skills 复制并更新 questioning/reader/reframing/reviewer
- [ ] 增加 evidence_basis 字段到 card schema
- [ ] 测试 skills 在 karpathy-gist 上的改进效果

---

## Phase 2 -- Full Extraction（全量提取）

- [ ] 处理全部有效材料（parallel extraction）
- [ ] 确保 footnote 路径使用相对路径
- [ ] Extraction 完成后 intra-loop pairwise fusion scan

---

## Phase 3 -- Sequential Governance（逐卡治理）

- [ ] 逐卡全局 grep -> 读命中卡 -> 判断关系 -> 写 footnote（无 cluster 分组）
- [ ] derive-related 脚本使用 YAML parser（非 regex）
- [ ] 双向 backlink 强制 + 孤儿检测 gate
- [ ] 验证零断裂引用、零 YAML 格式错误

---

## Phase 4 -- Audit（审计验收）

- [ ] FSJS 审计（Filter-Shard-Judge-Synthesize）
- [ ] 深层审计（authority flattening, says-vs-implies 等）
- [ ] 验收标准：
  - 源忠实性：零伪造引用
  - 权威扁平化：零限定词比例 < 40%（v4 为 62%，目标改善 1/3）
  - 反向链接不对称率 < 25%（v4 为 40.3%）
  - 孤儿卡（非 comparison）< 5%

---

## Phase 5 -- Documentation（文档固化）

- [ ] 写 v5 learnings capsule
- [ ] 更新 next_loop_prep（v6 inputs）
