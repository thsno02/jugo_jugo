---
schema: v5_learnings
loop_id: v5_llm_wiki_loop_20260612
created: 2026-06-12
topic: execution_summary
purpose: retrospective
---

# v5 执行总结

---

## 1. 各阶段产出

| 阶段 | 输入 | 输出 | 关键指标 |
|------|------|------|---------|
| Phase 0 Setup | v4 learnings x7, queue.jsonl | tools/ x6, skills/ 更新 | source_router/yaml_lint/ingest/batch_link/backward_backlink/fusion_candidates |
| Phase 1 Skills | v4 skills 复制 | reframing(+hedge 保留 +evidence_basis), questioning(+原子性), reader(+位置格式) | evidence_basis 字段上线 |
| Phase 2 Extraction | 74 源 → 63 有效 + 11 死源 | 487 张 draft cards | 4 waves parallel, 7.7 卡/有效源 |
| Phase 2b Fusion | 487 drafts pairwise scan | 163 候选对 → 9 dup + 1 merge + 153 link → 477 活跃卡 | anti-merge bias 生效: 仅 10/163 (6%) 判为 merge/dup |
| Phase 3 Governance | 477 卡 | batch_link(151 对) + orphan(81 张补链) + backward(423 条) | 0% 孤儿, 0.5% 不对称 |
| Phase 4 Audit | 477 卡全量 | FSJS 审计报告 | 零伪造, 权威扁平化 conditional-pass |

### 死源排除清单 (11 源)

- Reddit x6: 反爬拦截（继承 v4 问题）
- aicritique x2: Alibaba 403 拦截
- obsidian-help-link-notes: SPA 无法抓取
- arxiv-knowledge-compounding: PDF-only 无 TeX bundle
- langchain-long-term-memory-docs: SSR 压缩（v5 成功用 markdown.md 替代，实际有效）

修正: 实际死源 10 个（langchain 在 v5 成功重抓为 markdown.md），最终有效源 63。

---

## 2. 与 v4 对比

| 维度 | v4 | v5 | 变化 |
|------|-----|-----|------|
| 活跃卡片 | 328 | 477 | +45% |
| 有效源 | ~50 | 63 | +26% |
| 孤儿率 | 6.8% | 0% | 消除 |
| 反向链接不对称 | 40.3% | 0.5% | -99% |
| 平均链接密度 | 3.3/卡 | 3.8/卡 | +15% |
| 源忠实性 | 零伪造 | 零伪造 | 持平 |
| 权威扁平化 | 62% 零限定词 | 79.8% 零限定词 | 指标设计问题（见下文） |
| repo 消化 | 2/20 有 bundle | 18 repo README 消化 | 从 10% → 100% 覆盖 |
| 新字段 | — | evidence_basis | v5 新增 |

### 关键改善归因

1. **孤儿率 6.8% → 0%**: 归因于三层保障——fusion scan 的 distinct_link 判定 + batch_link 脚本化 + orphan governance 独立 pass + backward_backlink 补全
2. **不对称率 40.3% → 0.5%**: 归因于 backward_backlink.py 作为独立 pass 扫描全量 related 图并补写反向链接
3. **卡片数 +45%**: 归因于有效源增加（source_router 正确路由 + 死源排除减少误读）+ evidence_basis 促进原子性拆卡
4. **权威扁平化无改善**: 根因为源构成——94% 的源（arxiv + practitioner）本身断言体写作，hedge 保留规则在这类源上无施展空间

---

## 3. Workflow 编排模式

### 3.1 Four-Wave Parallel Extraction

**方案**: 将 63 有效源按 token 量均衡分为 4 waves，每 wave ~16 源。

**分配逻辑**:
- 按 `source_text_path()` 文件大小排序
- 交替分配（第 1 大 → wave 1, 第 2 大 → wave 2, ... 循环）
- 确保每 wave 总 token 量差异 < 20%

**效果**: 4 waves 近似同时完成，无明显瓶颈 agent。

### 3.2 Orphan Governance（独立 pass）

**流程**:
1. batch_link 完成后，扫描全量 KB 找 `related: []` 且入站链接 = 0 的卡
2. 对每张孤儿卡执行全局 grep（canonical_concept + aliases + key_terms）
3. 对 grep 命中卡 Read 全文 → 判断关系 → 写入 related

**v5 数据**: 81 张卡进入 orphan governance，全部成功补链。

### 3.3 FSJS 审计

**四阶段**:
1. **FILTER**: 机械 grep 验证（431 脚注 → 413 verified + 18 suspect）
2. **SHARD**: 按源类型分片（arxiv / webpage / github_repo / 其他）
3. **JUDGE**: 对 18 suspect 做语义验证（全部 pass）
4. **SYNTHESIZE**: 汇总各指标，生成 audit_report.md

**均衡部署**: JUDGE 阶段 18 条 suspect 分配给 3 个 agent（每 agent 6 条），耗时均衡。

### 3.4 backward_backlink 独立 pass

**设计**: 在 batch_link 和 orphan governance 之后，独立扫描全量 related 图:
- 对每条 A→B 链接，检查 B→A 是否存在
- 若不存在且关系为 symmetric，自动补写
- v5 补写 423 条反向链接

**效果**: 不对称率从 batch_link 后的 ~15% 降至 0.5%。剩余 9 条不对称为 comparison sink 的 by-design 单向链接。

---

## 4. 设计决策记录

### 4.1 Fusion Scan Anti-Merge Bias

**决策**: fusion scan 对候选对的判定偏向 `distinct_link` 而非 `duplicate`/`overlap_merge`。

**理由**: 过度合并（cluster damage）比轻微冗余更有害——合并会丢失原子性和源追溯，而冗余通过 related 链接可自然暴露。

**效果**: 163 候选对中仅 10 对判为 dup/merge (6%)，153 对判为 distinct_link (94%)。审计未发现漏判 duplicate 的情况。

**验证**: 10 对 dup/merge 全部合理:
- 9 对 duplicate: canonical_concept 完全相同（同义词/翻译变体）
- 1 对 overlap_merge: 70%+ 内容重叠，合并后信息无损

### 4.2 batch_link 脚本化

**决策**: governance 链接写入由 `batch_link.py` 脚本执行（非 LLM 手动编辑 frontmatter）。

**理由**: LLM 手动编辑 YAML frontmatter 容易引入格式错误（v4 曾出现 related 字段双格式问题）。脚本化保证:
- YAML 格式一致性（行内 [] 格式）
- 双向写入原子性（A→B 和 B→A 同步完成）
- 幂等性（重复运行不产生重复链接）

**效果**: 151 对链接零格式错误，yaml_lint.py 验证全量通过。

### 4.3 evidence_basis 字段

**决策**: frontmatter 必填 `evidence_basis` 字段，取值枚举: experimental_paper / theoretical_paper / practitioner_report / community_discussion / documentation / code_implementation。

**效果**:
- 审计可按 evidence_basis 分层设定指标阈值
- reader/reframing 根据 evidence_basis 调整限定词保留策略
- 未来可按 evidence_basis 加权卡片置信度

### 4.4 Source Router 逐类型 Dispatch

**决策**: 取代 v4 的扁平 fallback 优先级链，按源类型路由阅读面:

```
arxiv:       agent_source_bundle.txt
webpage:     markdown.md > text.txt
github_repo: material_bundle.txt > repo/README.md
reddit:      text.txt
hacker_news: text.txt
pypi:        text.txt
gist_raw:    text.txt
```

**效果**: 63 源全部正确路由，无 v4 的 "arxiv text.txt 误读" 问题。质量门控（<500 字节 / captcha 关键词）成功拦截死源。

---

## 5. 遗留问题（移交 v6）

| 问题 | 严重度 | 根因 | v6 方案 |
|------|--------|------|--------|
| 权威扁平化 79.8% | 设计缺陷 | 指标假设源含 hedge，实际 94% 源为断言体 | 分层条件检测（见 next_loop_prep #1） |
| repo 信息密度低 | 中 | repo2doc 未实施，仅消化 README | 实施 repo2doc.py（见 next_loop_prep #2） |
| Reddit 6 源 blocked | 低 | 反爬拦截 | old.reddit.com/.json 重抓（见 next_loop_prep #3） |
| FILTER grep 假阴性 14/431 | 低 | LaTeX/Markdown 格式干扰 | 格式剥离预处理（见 next_loop_prep #4） |
| hacker_news 桥梁 1 条差距 | 极低 | 单源 6 卡闭环 | 可选补 1 条对外 related |
