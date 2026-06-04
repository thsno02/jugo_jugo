---
status: placeholder
skill: questioning
loop_id: v4_llm_wiki_loop_20260602
created: 2026-06-02
note: TO BE DEVELOPED. 完整设计见 ../../../v3_llm_wiki_loop_20260525/future_plans/questioning_loop_design.md
---

# Questioning Skill (Mode A) -- PLACEHOLDER

> 本文件是占位结构。完整设计见 `questioning_loop_design.md`（v3 future_plans）。
> 待 Phase 1 开发时填入具体 SOP。

## Trigger

per-material extract 阶段。coordinator 分派 questioner 时加载本 skill。

## Purpose

系统性提问 exhaust 单源材料的知识内容。从 digest + 全文出发，通过 5 阶段推进，产出覆盖完整、层次递进的 Q&A 对。

## Workflow Phases

### Phase 1 -- 广度扫描
对材料每个主要章节/主张提开放性问题。最少轮次触碰全域。

### Phase 2 -- 深度追问
识别"提到但未展开的机制/区分/条件"，逐一追问。每追问链 1-3 层。

### Phase 3 -- 评判性提问
对已有回答提评估性问题——局限、假设、与主流理解的差异。

### Phase 4 -- 批判性/对比性提问
追问材料**内部**张力。不引入材料外知识。

### Phase 5 -- 覆盖率自检
回顾 digest，逐条核对 TOC/core_claims/terms 是否均被问过。遗漏项补问。

## Output

Q&A pairs（含 source_refs, round）。每轮对话间即时 reframe 为 draft cards，使下一轮可见已产出 canonical_concept 列表。

## Done Criteria (SATISFIED)

三个条件同时满足：
- (a) digest 每个 core_claim 有至少一个 Q&A 覆盖
- (b) 无 Phase 2 追问链在"未展开新概念"状态下终止
- (c) 再问不会产生新的原子 idea

## 参考

- `questioning_loop_design.md` S1.2: 五阶段策略详细定义
- `pipeline_spec.md` S2.2: questioning dialogue I/O schema
- `pipeline_spec.md` S2.0.1: 角色定义与边界
