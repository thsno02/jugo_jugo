---
schema: v4_learnings
loop_id: v4_llm_wiki_loop_20260602
created: 2026-06-12
topic: audit_methodology
purpose: forward_prep
---

# FSJS 审计模式（可复用配方）

## 模式总览

Filter-Shard-Judge-Synthesize 是本轮 v4 KB 审计中提炼的四阶段审计配方。核心假设：机械检查可以单 agent 完成，但语义判断必须分片——否则单一 agent 的上下文窗口既无法容纳 280 张卡，也无法保持判断一致性。

完整实例见 ../outputs/llm_wiki/kb/audits/v4_comprehensive_audit.md

## 阶段详解

### 1. FILTER：机械扫描

- **单 agent 即可**——不涉及主观判断，只需脚本或 grep
- 输入：全部 N 张卡片（本轮 280 张）
- 输出：defect manifest（结构缺陷清单）+ suspect lists（疑似问题卡列表）
- 本轮实例：
  - YAML `related` 双格式检测（发现 69/280 = 24.6% 缺陷）
  - 断裂引用扫描（3 条悬空 slug）
  - 孤儿卡检测（5 张零出入站链接）
  - JJ 文件格式校验（13 个缺 `## creation` 头）
- **关键教训**：grep false positive 率不可忽视——grep 未命中不等于 leakage，需后续语义验证

### 2. SHARD：分片策略

两种互补的分片维度：

**源亲和分片（source-affinity）**：按来源分组，每组含同源的所有卡片
- 优势：agent 只需加载 1 份源材料即可验证该组全部脚注
- 本轮实例：21 个源审计 agent，每个 agent 负责 1-2 个源的全部卡片（5-15 张/组）

**数量分片（count-based）**：按 suspect 列表均分
- 优势：负载均衡，避免单一 mega-agent
- 本轮实例：comparison 卡审计分为 2 批（11 + 10 张）

**选择原则**：
- 需要源材料对照时 → 源亲和分片
- 纯卡片内部检查时 → 数量分片
- 两者可混用：FILTER 和源亲和分片可并行（无依赖关系）

### 3. JUDGE：控制上下文的语义判断

- 每个 agent 的上下文严格控制在 5-15 张卡
- 输出格式为结构化 JSON（不允许自由文本报告）
- 判断维度在 prompt 中预定义（如 DIRECT / REASONABLE-INFERENCE / EXTRAPOLATION 三级）
- 本轮实例：
  - 源忠实性判断：逐条脚注对照源文本，输出 finding + severity + evidence
  - 不确定性洗白检测：逐对引用关系，输出 hedge-drop 分数
  - 静默分歧裁决检测：逐张 comparison 卡，输出 NEUTRAL / FRAMED / ADJUDICATED

### 4. SYNTHESIZE：汇聚与去重

- 输入：全部 agent 的 JSON 输出
- 单一 synthesis agent 负责：
  1. topic grouping（按问题类型聚类，非按来源）
  2. 去重（同一问题被多个 agent 独立发现时合并）
  3. severity 校准（跨 agent 统一判定标准）
  4. 生成最终审计报告 + fix plan
- **关键约束**：synthesis agent 不做新判断，只做元分析

## 核心原则

### 机械检查单 agent 足矣，语义判断必须分片

- 280 张卡的 YAML 格式扫描：1 个 agent + 脚本，10 分钟
- 280 张卡的源忠实性验证：21 个 agent 并行，各 5-15 张卡

### 源亲和 agent 与 FILTER 可并行

- FILTER 输出的 suspect list 供 JUDGE 使用，但源亲和 agent 不依赖 FILTER 结果
- 并行执行节省约 40% 总耗时

### grep false positive 需全文语义验证

- 本轮案例：「参与程度谱系」被 grep 判为 leakage，实际是 Karpathy gist 第 37 行的合理意译
- 修正协议：grep 未命中 → 标记 suspect → 派 agent 读完整源文本 → 语义级验证
- 审计 findings 必须区分 grep-verified 和 semantic-verified 两个置信度

### 审计不等于缺陷发现；审计等于不确定性削减

认知盲点审计见 ../outputs/llm_wiki/kb/audits/v4_deep_audit_blind_spots.md

- 目标不是「找 bug」而是「消除认知盲点」
- 本轮最有价值的发现不是个别错误卡，而是系统性模式：
  - 62% 零限定词（源权威扁平化）
  - 40.5% 幽灵源（认知空白）
  - 40.3% 单向边（结构不对称）
- 这些模式级发现只有通过 SYNTHESIZE 阶段的跨 agent 元分析才能浮现

### 负载均衡：无 mega-agent 瓶颈

集群损伤评估见 ../outputs/llm_wiki/kb/audits/cluster_damage_assessment.md

- 本轮 Phase 3 的 agent 分配：4 个 agent，80K-120K token 各
- 拆分依据：工作量估算（需读源材料的 agent 给更少卡片，纯编辑 agent 给更多）
- 反模式：1 个 agent 处理全部 21 张 comparison 卡的脚注补全（~240K token，超出有效上下文范围）

## 适用边界

- **适用**：KB 规模 > 50 张卡的审计；多源多类型的知识库
- **不适用**：< 20 张卡可直接单 agent 通审；纯格式问题可直接脚本修，不需 FSJS
- **扩展方向**：FILTER 阶段可加入嵌入相似度预筛（当前纯 grep），但需权衡复杂度与 best-effort 原则
