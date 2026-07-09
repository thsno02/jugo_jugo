---
loop_id: v5_llm_wiki_loop_20260612
created: 2026-06-12
status: complete
note: v5 全部阶段完成。477 卡产出，审计通过。
---

# v5 Task List

> questioning-loop-based 知识卡片生产管线第五次迭代。逐阶段推进，每阶段验证后才进入下一阶段。

---

## Phase 0 -- Setup（脚手架）

- [ ] 读 v4 learnings（7 份文档）理解全貌
- [ ] 实现 source_router.py（逐类型 boundary-read dispatch）
- [ ] 实现 repo2doc.py（repo -> material_bundle.txt，Tier-1 前 3 个 repo 验证）
- [ ] 实现 yaml_lint.py（frontmatter 格式验证 + YAML parser 读写验证）
- [ ] 更新 reframing skill（hedge 保留 + evidence_basis）
- [ ] 验证 bypassPermissions + model:opus 工作正常

---

## Phase 1 -- Build/Update Skills（构建核心技能）

- [ ] 从 v4 skills 复制并更新 questioning/reader/reframing/reviewer
  - v4 路径：`loops/v4_llm_wiki_loop_20260602/skills/{questioning/SKILL.md, reader/PROMPT.md, reframing/PROMPT.md, reviewer/PROMPT.md}`
  - 合并 checklist（参考 v4 skill_iteration_log.md 每项具体修改）：
    - questioning: Phase 5 次要节覆盖规则 + 原子性自检 + canonical 反馈 + 大材料衰减启发式
    - reader: 统一位置格式 'Section Title PN' + 三级不确定性分类 + 分点标记
    - reframing: hedge 保留规则 + evidence_basis 字段 + cross-link 规则5 + 拆卡信号强化
    - reviewer: 附加检查（源节覆盖/链接密度/重叠检测）+ quit-audit 角色定位
- [ ] 增加 evidence_basis 字段到 card schema
- [ ] 测试 skills 在 karpathy-gist 上的改进效果

---

## Phase 2 -- Full Extraction（全量提取）

- [ ] 按材料 token 量估算 agent 负载，若某 agent >2x 平均值则拆分 sub-task；全量 grep 和深读抽样拆成独立 agent
- [ ] 处理全部有效材料（parallel extraction）
- [ ] 确保 footnote 路径使用仓库根相对路径（`data/raw/...` 格式，与 source_router 输出一致）
- [ ] Extraction 完成后 intra-loop pairwise fusion scan（须在全部并行 extraction 完成后 sequential 执行，不可与 extraction 并行；boundary-read = `outputs/llm_wiki/drafts/cards/*.md`）

---

## Phase 3 -- Sequential Governance（逐卡治理）

- [ ] 逐卡全局 grep -> 读命中卡 -> 判断关系 -> 写 footnote（无 cluster 分组）
  - 遍历顺序：`sorted(cards, key=(source_id, created_time))`
- [ ] derive-related 脚本使用 YAML parser（非 regex）
- [ ] 双向 backlink 强制 + 孤儿补链 pass（不仅检测，对孤儿卡 + 前 1/3 处理的卡执行反向全局 grep 补建 backlink）
- [ ] 验证零断裂引用、零 YAML 格式错误（yaml_lint.py gate）

---

## Phase 4 -- Audit（审计验收）

- [ ] FSJS 审计（Filter-Shard-Judge-Synthesize）
- [ ] 深层审计（authority flattening, says-vs-implies 等）
  - 审计方法论：grep 未命中标记 suspect（非 leakage）；suspect 项 dispatch agent 读原文语义验证；findings 区分 grep-verified / semantic-verified 两级置信度
- [ ] 验收标准：
  - 源忠实性（一级）：text-extractable 源零伪造引用（grep-verified + semantic-verified）
  - 源忠实性（二级）：text_extractable: partial/false 源零摘要级不一致（caveat-pass 允许但必须标注）；审计报告显式披露不可验证子集占比
  - 权威扁平化（分层）：
    - experimental/theoretical/practitioner/community 类卡片：零限定词比例 < 35%
    - documentation/code_implementation 类卡片：不设硬性比例要求，抽查确认「如果源含 hedge 则卡片保留」
    - 限定词 grep 词表（中文）：据材料推测/证据有限/源暗示/尚未证实/可能/或许/似乎/初步/有限证据/观察到/某些情况下
    - 限定词 grep 词表（英文）：suggests/implies/appears/may/might/possibly/preliminary
    - 判定规则：正文 body（不含 frontmatter、不含 footnote 区域）中词表命中次数 = 0 即为零限定词卡片
    - 分母：排除 comparison 卡
  - 反向链接不对称率 < 25%（v4 为 40.3%）
    - 公式：仅在 A.related 中出现 B 但 B.related 中不出现 A 的边对数 / 全部 related 边对数
    - 排除：comparison/distinction 卡的入边不计入（by-design sink）
    - see_also 不纳入 related graph 计算
  - 孤儿卡（非 comparison）< 5%
    - 定义：related:[] AND 入站 related 链接 = 0（完全孤立）
  - 跨域桥梁（informational，非 hard gate）：每个 domain 至少 2 条对外链接

---

## Phase 5 -- Documentation（文档固化）

- [ ] 写 v5 learnings capsule
- [ ] 更新 next_loop_prep（v6 inputs）
