# V4 入库机制证据审计

## 1. 审计范围与证据口径

本文审计 V4 从原始材料到知识库发布后的完整入库链，固定映射到八个稳定阶段：`source-route/acquisition`、`questioning-extraction`、`reframe-drafts`、`scripted-ingest/promotion`、`fusion-decision`、`graph-governance`、`publish-kb`、`failure-feedback`。

「入库（ingestion）」在本文中包含两层含义：

1. 广义生产链：材料读取、提问、回答、重构、融合、治理和发布。
2. 窄义 promotion：draft 的状态翻转、文件搬运和索引重建。

两者不可混用。特别是，V4 全量阶段把 extraction agent 直接写入 `kb/cards/`，不能因为终态存在 `accepted` cards，就倒推存在过独立的 draft gate 或 script-only promotion。

### 1.1 事实状态

| 标签 | 含义 | 可接受证据 |
|---|---|---|
| `specified` | 设计或规范要求 | start prompt、task、skill、pipeline spec |
| `executed` | 可直接证明发生过 | Claude V4 primary 原始执行 prompt/命令、primary event、Git diff、落盘 artifact |
| `retrospective` | 运行后形成的解释或总结 | V4 learnings、审计报告、Codex retrospective |
| `contradicted` | 同一事实存在明确反证或不兼容口径 | primary prompt vs learnings、Git/产物 vs 状态文件、报告间冲突 |

证据优先级为：Claude V4 primary 原始会话与对应 event window > Git 中的原始变更 > 同期产物 > V4 learnings/后验审计 > 跨版本 retrospective。

下文用 `H001` 等短名指完整 event_id，例如 `H010` = `claude_code:claude-primary-v4:H010`。`codex:codex-retro-v4-v5-research:H001` 只证明后续做过 V4/V5 风格归因研究；它明确认为差异更可能来自管线、prompt、schema、来源和后处理，不能证明 V4 的原始执行顺序。本文也不依据任何 V5 primary 会话中的初次回答单独判定 V4 执行方式。

### 1.2 核心证据

- 设计合同：`loops/v3_llm_wiki_loop_20260525/future_plans/pipeline_spec.md`
- V4 启动与任务：`loops/v4_llm_wiki_loop_20260602/LOOP_START_PROMPT.md`、`task.md`
- 四份技能：`loops/v4_llm_wiki_loop_20260602/skills/{questioning,reader,reframing,reviewer}/`
- Claude primary 回放：`docs/claude_interaction_replay/events/events.claude.primary-v4.v2.jsonl`
- V4 后验总结：`loops/v4_llm_wiki_loop_20260602/learnings/`
- 审计与修复：`loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/`
- Git 主序列：`2df61ddb`、`d36f6f7a`、`f4ec89b6`、`b26dafc3`、`fb7b4060`、`4ec3b45d`、`d2ebcf41`、`044312a2`、`5f2824e9`

## 2. 总体判定

V4 不是一条从头到尾保持同一编排合同的管线，而是至少三种运行形态的叠加：

1. **种子实验（15→19 cards）**：reader、questioner、reviewer 是分离的 sub-agent 调用，主 agent 负责消息中继和写卡；存在真实多轮问答与 quit-audit，但执行节点收到的是 skill 摘要，不是完整 skill 文件，reframing 也没有独立 agent 节点。
2. **全量批次（19→259 cards）**：43 个并行 extraction agents 各自同时扮演 questioner 和 reader，按固定 2-4 轮自问自答，直接写 `status: accepted` 到 KB；没有 reviewer、严格 SATISFIED、独立 reframe、draft gate、inline fusion 或 script promotion。
3. **发布后补救（259→280→295→328 cards）**：先做全库 governance、cluster-based comparison、related 派生和 FSJS，再修 source route、局部 repo/webpage 缺口；这些动作改善终态，但不能改写原始 240 张卡的生产合同。

因此，V4 的可靠结论是：**questioning-loop 设计在种子阶段被部分真实执行，在规模化阶段被压缩成单-agent 自问自答；卡片和 JJ 大量产出成功，但入库、fusion、graph governance 和 reviewer gate 没有按规范保持阶段边界，后来依靠审计与补救恢复了部分结构质量。**

三个最重要的 `contradicted` 结论：

- `learnings/pipeline_actual.md` 称四角色模型“实际运行”且 Ingest “完全按 spec 实施”；原始 H010 workflow 明确显示全量节点合并 questioner/reader、无 reviewer、直接写 accepted KB，只把“重建索引”命名为 Ingest。
- `task.md`/commit 曾把 Phase 0-4 标为完成；H013-H015 随后确认顺序 ingest、fusion 和 card governance 实际被跳过。
- `status.json` 仍为 `setup`，`loop_state.json` 仍为 0 materials / 0 cards；Git 和 KB 证明实际执行到 328 cards。状态文件不能单独代表完成度。

## 3. 八阶段证据总表

| 稳定阶段 | V4 实际形态 | 状态 | 关键 event_id | 主要 artifact / Git | 核心缺口 |
|---|---|---|---|---|---|
| `source-route/acquisition` | 初始按 `text.txt > 2KB` 扁平筛选 43 源；后补 arXiv bundle、webpage markdown 和有限 repo demo | `executed` + `contradicted` | `H004-H010`, `H042-H053` | `loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/pipeline_gaps_report.md`; Git `d2ebcf41`, `044312a2` | source type 未进入初始 router；30 phantom sources；结构丢失；repo/reddit 缺口 |
| `questioning-extraction` | 种子阶段角色分离；全量阶段单 agent 自问自答 | `executed` + `contradicted` | `H001`, `H010` | `loops/v4_llm_wiki_loop_20260602/skills/`; Git `2df61ddb`, `d36f6f7a` | 完整 skills 未注入节点；全量无 reviewer/严格 SATISFIED；无 per-source run record |
| `reframe-drafts` | 种子由主 agent 写 draft；全量 extraction agent 直接写 accepted KB | `executed` + `contradicted` | `H001`, `H010`, `H053` | `loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/{drafts,kb}/` | 全量无独立 reframe 节点；hedge 被压平；JJ 不能证明问答和审查 |
| `scripted-ingest/promotion` | 种子用 shell copy + status flip；全量不存在 promotion，仅重建 index | `executed`（种子）/ `contradicted`（全量） | `H001`, `H010`, `H014-H015` | `2df61ddb`; `d36f6f7a` | 无专用 ingest tool、无 gate ledger、无 one-by-one promotion |
| `fusion-decision` | 初始 inline fusion 缺席；发布后 cluster governance 才补候选和 comparison | `contradicted` + `retrospective` | `H013-H018` | `loops/v4_llm_wiki_loop_20260602/learnings/operational_lessons.md`; Git `b26dafc3` | 并行卡彼此不可见；无逐卡/逐对 fusion ledger；merge candidate 几乎无效 |
| `graph-governance` | 先弱治理，再 37-cluster 补链，再 FSJS 修图 | `executed` + `retrospective` + `contradicted` | `H011`, `H015-H018`, `H031`, `H036-H038` | `loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/`; Git `f4ec89b6`, `b26dafc3`, `fb7b4060` | 固定 cluster 数量锚；YAML 双格式 bug；孤岛、跨域桥梁和单向边问题 |
| `publish-kb` | 卡片进入 `kb/cards`、index 与 Git；全量是 direct publish | `executed` + `contradicted` | `H001`, `H010-H011`, `H053` | `loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/indexes/cards.md`; Git 259→280→295→328 | publish 与 quality gate 混同；状态文件陈旧；后增 48 卡未完整重治理 |
| `failure-feedback` | 用户触发多轮纠错、FSJS、语义复核、source pipeline 审计和 learnings | `executed` + `retrospective` | `H012-H055` | `loops/v4_llm_wiki_loop_20260602/{outputs/llm_wiki/kb/audits,learnings}/`; Git `fb7b4060`, `5f2824e9` | 很多修复改善终态，但无法补证原始执行；部分“修复”仍仅改路径或做 demo |

## 4. 分阶段证据审计

### 4.1 `source-route/acquisition`

**`specified`**：V3 spec 把 Collect 定义为 source spec → `data/raw/<source_type>/<source_id>/`，但标记为 parked/manual；Extract 的边界读取却统一写成 `text.txt`。V4 start prompt 没有实现 source router，只要求处理现有材料。

**`executed`**：H010 原始 workflow 在启动前遍历 `data/raw`，只选择存在 `text.txt` 且大于 2,000 bytes 的目录，排除已处理 Karpathy gist，然后把 43 个来源全部以显式 `.../text.txt` 路径传给 extraction agents。GitHub repos 因没有 `text.txt` 被排除；这不是按 source type 路由。

**`retrospective`**：`pipeline_gaps_report.md` 和 `learnings/pipeline_actual.md` 后来量化出：

- 74 个 source 目录中约 44 个有可靠阅读面，30 个为 phantom/零卡来源。
- 17 个 arXiv 的 `text.txt` 是摘要页；62/626 条 arXiv citations（10%）落在错误读取面，7 个源受影响。
- 20 个 GitHub repos 初始没有进入全量 extraction；6 个 Reddit 全被拦截。
- webpage HTML→text 丢失 1,261 个结构元素，包括 table/code/image/SVG。

**`contradicted`**：后验文档把读取形态描述为“逐源类型路由”，但这只是 V4 结束后形成的目标形态。初始 H010 的真实 router 是 flat `text.txt` filter。即使部分 agent 自主发现 `agent_source_bundle.txt`，也不能把这种不稳定行为称为 source router。

**版本变化**：

- `d36f6f7a`：43 源按 flat text 路径进入全量 extraction。
- `4ec3b45d`：确认 arXiv、repo、webpage、cross-link 四类 pipeline gaps。
- `d2ebcf41`：批量改 arXiv footnote 路径、补两个 repo bundle 和 15 张实践卡、记录 scrape flags。
- `044312a2`：23 个有效 webpage 生成 `markdown.md`，19 源增量重提取 33 张卡。

**未闭合缺口**：`d2ebcf41` 对 arXiv 主要执行 `text.txt → agent_source_bundle.txt` 路径替换；审计报告却称部分卡只有摘要深度。路径替换本身不能证明正文曾由 bundle 生成，也不能替代重新 extraction。H046 进一步确认直接 repo bundle→card 只是 demo，正确方向应是 repo→doc→card；V4 没有完成通用 repo2doc。

### 4.2 `questioning-extraction`

**`specified`**：coordinator 不读原文，只中继 reader、questioner、reviewer；reader 先产 digest，questioner 看全文+digest，按 Phase 1-5 追问，round 间即时 reframe，SATISFIED 后 reviewer quit-audit。

**`executed`：种子阶段**：H001 的原始工具序列可见：

1. `Reader: produce digest`
2. `Questioner: Round 1`
3. `Reader: Answer Round 1`
4. `Questioner: Round 2-3`
5. `Reader: Answer Round 2-3`
6. `Questioner: Phase 5 coverage`
7. `Reviewer: quit-audit`

这证明种子实验存在真实的角色分离和消息中继。Git `2df61ddb` 报告 4 轮、16 questions、9 answers、15 cards、quit-audit pass；随后 `1b92f941` 基于质量审查扩为 19 cards。

**完整 skill 是否进入执行节点：否。** 种子 reader/questioner/reviewer prompt 只内嵌了各 skill 的摘要条款；没有把完整 `SKILL.md`/`PROMPT.md` 原文注入节点。reviewer prompt 甚至只给出 raw source 的节选和 key passages。reframing 没有独立 Agent 调用，主 agent根据 Q&A 直接写文件。因此种子阶段是“角色结构真实、合同注入不完整”。

**`executed`：全量阶段**：H010 的 `buildExtractPrompt` 明确写着“你同时是 questioner 和 reader”，固定 Round 1 breadth、Round 2 depth、Round 3 evaluative，短材料允许 2 轮，长材料 3-4 轮。它没有 Phase 4 internal tension、Phase 5 coverage、自适应 SATISFIED、独立 reader、独立 reviewer 或补问回路。

全量 workflow 虽在启动前由主 agent读取 questioning、reader、reframing 三个文件，但执行 agent 收到的是约化后的单体 prompt，不是三份完整内容；reviewer skill 没进入该 workflow。读取 skill 文件发生在 coordinator context，不等于 skill 被传递给 execution node。

**`contradicted`**：`learnings/pipeline_actual.md` 把 coordinator+reader+questioner+reviewer、round 间 reframe、SATISFIED 后 reviewer 描述为 V4 全量“实际运行”。这对种子阶段大体成立，对 `d36f6f7a` 的 240 张新增卡不成立。

**证据缺口**：`run/` 没有 per-material 文件；digest、逐轮 Q&A、SATISFIED、reviewer verdict 都未落盘。全量结果只能证明 agent 产出了 cards/JJ，不能逐源重放它实际问了什么、在哪一轮停止。

### 4.3 `reframe-drafts`

**`specified`**：独立 reframing step 将 Q&A 转为原子卡，先 grep canonical，再写 `status: draft` card 和 append-only JJ；每轮把 canonical 列表反馈给 questioner。

**`executed`：种子阶段**：主 agent根据问答写入 `drafts/cards/` 和 `drafts/justification/`，之后再 promotion。Git `2df61ddb` 同时保留 15 份 draft 和 15 份 accepted 副本。

**`executed`：全量阶段**：同一个 extraction agent 同时负责 digest、自问自答、reframe 和写文件，目标目录直接是 `kb/cards/`、`kb/justification/`，模板状态直接为 `accepted`。不存在独立 draft artifact，也不存在 canonical 列表回传给另一个 questioner 节点。

**Justification Journal（JJ）实况**：当前 KB 有 328 份 JJ；313 份含标准 `## creation |` 事件，0 份含 `## review |` 事件。大量 JJ 写有“Mode A questioning loop”，这能证明生成者声明了 extraction mode 和源证据，不能证明真实角色拓扑、轮次、reviewer 或 append-only event lifecycle。审计曾修复 13 份 JJ 的 creation 格式，后续新增/比较卡仍留下非标准项。

**`retrospective` 缺陷**：

- 280 卡中 174 张（62%）没有认识论限定词，表明 dialogue→assertion 的 reframing 系统性压平 hedge。
- comparison 卡集中缺直接 source footnote、标准 JJ 和跨卡归因。
- 1 个 true context leakage、1 个 provenance gap，说明治理阶段读取 footnote narrative 后可能把外部概念写入新卡。

### 4.4 `scripted-ingest/promotion`

**`specified`**：script-only；`draft → accepted`、物理移动 card/JJ、重建 active index，禁止 LLM 复制或改写 body。

**`executed`：仅种子阶段**：H001 原始 Bash 命令对每个 draft 执行 `cp`，再用 `sed` 将 `status: draft` 改为 `accepted`，复制 JJ 并计数。这是可证实的窄义 script promotion，虽是临时 shell loop，不是落盘的可复用 ingest tool。

**`contradicted`：全量阶段**：H010 的 43 agents 直接写 accepted KB。workflow 的 `Ingest` phase 只启动一个 agent 重建 index；没有读取 drafts、status flip、move/copy 或 fusion verdict gate。H014-H015 随后由用户和助手共同确认顺序 ingest、inline fusion 和治理被跳过。

因此 `learnings/pipeline_actual.md` 的“完全按 spec 实施、280 张卡经主批次入库”不能作为全量执行事实。更准确的说法是：种子 15 张经过 shell promotion；全量 240 张和后续大多数增量卡直接发布到 KB。

**证据缺口**：没有 `tools/ingest.py`、promotion ledger、每卡 verdict、失败清单或幂等运行记录；也没有证据证明一张 accepted card 必然通过 reviewer/fusion。

### 4.5 `fusion-decision`

**`specified`**：每张通过 review 的 draft 应对 active+archive 做多轮 zh/en/同义词 grep，随后由 LLM 读候选正文，判定 `keep / skip duplicate / link related-but-distinct`。grep 只负责候选召回，不负责语义裁决。

**`executed`：初始全量缺席**：H010 的 43 agents 同批并发，彼此看不到新增 cards；240 张新卡的 timestamp 高度聚集。H013-H015 明确认定 inline fusion 和顺序 card governance 没有落实。`merge_candidate=0` 不能解释为无重复，只能解释为没有有效比较基。

**`executed`：发布后补救**：H016 的 workflow 对近义、反义/张力和跨域 cluster 做 agent judgment，新增 card/distinction footnotes、21 张 comparison cards，并报告一组 merge candidate。它是 post-publication governance，不是 pre-promotion fusion。

**`contradicted`**：H017 追查出 workflow prompt 带有“20-40 clusters”的数量锚；H018 用户明确否定 cluster count target。后续 cluster damage audit 确认孤儿遗漏、跨域链接稀疏和 footnote narrative leakage，说明 cluster 从候选压缩手段漂移成了 exploration boundary。

**证据缺口**：没有完整 candidate pair ledger、逐对判定理由、skip/archive 记录或真实 merge 执行记录。最终图边数量不能反推出 fusion 判定过程。

### 4.6 `graph-governance`

**`specified`**：grep-only recall；canonical normalization、dedup、distinction linking；`related` 必须从有事实/观点支撑的 typed card/dist footnotes 派生，不能把 grep 命中直接当关系。

**`executed`**：

- `f4ec89b6`：259 cards 中 1 个 canonical 修正，117 cards 有 links，8-card source spot-check。
- H013-H015：确认 45% link coverage 和缺失 fusion，用户纠正“related ≠ grep similarity”。
- `b26dafc3`：37 clusters，295 card footnotes、54 distinction footnotes、21 comparison cards；280 cards 中 264 有 links。
- `fb7b4060`：FSJS 后修复 YAML、断裂引用、孤儿卡、跨域桥梁、comparison source footnotes 和 leakage/provenance 问题。

**grep-only governance 的准确边界**：没有证据显示 V4 使用 embedding/vector clustering，候选召回主要是 grep、canonical、aliases、summary 和类别分组；但关系判定仍由 agent 读卡完成。把“grep-only”理解为“grep 自动决定 related”是错误的，H015 已明确反驳。

**`contradicted`**：derive-related 补救通过正则/单行替换修改 YAML，产生 69/280 张 dual-format `related`，其中 11 张链接被 parser 完全忽略。设计要求脚本派生关系确实执行了，但实现违反结构化 YAML 写入原则。

**终态限制**：328-card 快照中的 1,022 links 和 94.3% linked ratio仍以 280-card governance pass 为主要分母；后增 48 cards 没有证据证明完整重跑同级 fusion/governance。

### 4.7 `publish-kb`

**`executed`**：V4 的发布面是 `outputs/llm_wiki/kb/cards/`、对应 JJ、`kb/indexes/cards.md` 和 Git snapshot：

- `2df61ddb`：15 accepted seed cards。
- `1b92f941`：19 cards。
- `d36f6f7a`：259 cards。
- `b26dafc3`：280 cards。
- `d2ebcf41`：约 295 cards。
- `044312a2`：328 cards。

**`contradicted`**：全量阶段 publish 是 extraction agent 直接写 KB，不是 promotion 后 publish。Git `d36f6f7a` 的提交消息报告 240 新卡，workflow completion payload 却汇总 235 cards；终态文件计数和提交 diff 支持 240 新卡/259 总卡，但该计数冲突说明 workflow 汇总不可无条件当账本。

**状态冲突**：`task.md` 后验标为 `phase4b_complete`，但根 `status.json` 仍为 `setup`，`loop_state.json` 仍记录 0 materials/0 cards。发布完成度必须以 primary+Git+artifact 交叉判断，不能选一个状态文件覆盖其他证据。

**质量边界**：进入 KB、被索引、被 Git 提交只证明可见性和版本化，不证明通过了 questioning、reviewer、fusion 或 source-quality gate。

### 4.8 `failure-feedback`

V4 的 failure-feedback 是最充分落盘的阶段，也是很多真实机制被发现的地方：

1. `H012-H018`：绝对路径、低链接、缺失 fusion、related 语义边界、cluster count target。
2. `H019-H031`：多次失败的 audit workflow 调整后形成 FSJS，并完成 22-agent 综合审计。
3. `H032-H034`：grep 未命中被证明可能是假阳性；加入 full-text semantic verification。
4. `H035-H038`：cluster damage 专项审计、fix plan、修复与验证。
5. `H040-H044`：authority flattening、phantom sources、scrape loss、repo gap、arXiv route 和 cross-family bridge 被量化并部分修复。
6. `H045-H053`：repo bundle demo 被否定为最终方案；Reddit 暂缓；webpage 全量转 markdown 并增量提取。
7. `H054-H055`：讨论→workflow 执行→审计→修复→独立总结，形成 7 份 learnings。

#### FSJS 的真实演化

**`specified`/讨论形成**：H029 把全量机械遍历与语义阅读分开，形成 Filter-Shard-Judge-Synthesize。

**`executed`**：H031 报告 22 agents、196 findings、8 个设计不变量中 5 PASS / 3 PARTIAL；产物包括 `mechanical_report.json`、`suspect_lists.json`、`v4_comprehensive_audit.md`。

**`retrospective`**：`learnings/audit_methodology.md` 固化为：机械规则可全量，语义判断按 source/card affinity 控制在 5-15 cards，结构化输出后再 synthesize。

**`contradicted`/自我修正**：FSJS 首轮把「参与程度谱系」判成 leakage；H033 全文复核后翻转为 false positive，同时保留 1 true leakage 和 1 provenance gap。故 grep 未命中只能进入 suspect，不能直接判 unsupported/leakage。

## 5. 专项结论

### 5.1 真实 questioner / reader / agent 编排

| 批次 | reader | questioner | reviewer | reframe | coordinator |
|---|---|---|---|---|---|
| Karpathy seed | 独立 Agent，digest 与 answer 分次调用 | 独立 Agent，多轮调用 | 独立 Agent，一次 quit-audit | 主 agent 直接写 draft，无独立 reframe Agent | 主 agent 实际读了源并做知识性写卡，不是严格“只看 metadata” |
| 43-source full batch | 与 questioner 合并为每源一个 extraction agent | 同一 agent 内部自问自答 | 缺席 | 同一 agent 直接写 accepted KB | 主 agent 构建 prompt、并行调度、计数和 commit |
| repo/webpage later repair | extraction agent 直接读 bundle/markdown 并写卡 | 无可重放的分离问答证据 | 缺席 | 直接写 KB/JJ | workflow 调度与验证 |

结论：V4 不能被概括为单一的“四角色多 agent 管线”。最准确的描述是“种子角色分离、全量角色折叠、后期 agent/workflow 补救”。

### 5.2 完整 skills 是否进入执行节点

**否。** 文件存在且 coordinator 读取过，只能证明设计可访问。

- seed：execution prompt 内嵌 skill 摘要，未注入完整文件；reframing 无独立节点。
- full batch：只传一个压缩的 extraction prompt，遗漏 reviewer、Phase 4-5、严格 SATISFIED、round 间 canonical feedback、完整 JJ review contract。
- 产物：无 per-source run records，0 个 JJ review event，无法用 artifact 补证完整合同。

因此“skills developed”是 `executed`，“skills fully injected and obeyed at scale”是 `contradicted`。

### 5.3 Justification Journal

JJ 的成功之处是 per-card 文件和 creation reason 大规模存在，保留 source path、quote 和 scope rationale；它确实比无 provenance 强。

JJ 的失败之处是没有形成设计中的 append-only lifecycle：当前 328 files / 313 standard creation headers / 0 review events；comparison 和后增卡模板继续漂移。JJ 不能作为 reviewer gate 或 fusion decision ledger 的替代品。

### 5.4 grep-only governance

可证实的是“没有 embedding/vector，使用 grep-friendly metadata 做候选召回”；不可证实也不应声称的是“grep 足以决定关系与忠实性”。V4 自身给出两个反例：

- H015：related 必须由读卡后的事实/观点关系支撑。
- H033：grep miss 可能只是意译，必须全文语义复核。

### 5.5 后来发现的 V4 缺陷

| 缺陷 | 首次或关键证据 | 影响 | V4 内状态 |
|---|---|---|---|
| flat `text.txt` route | `H010`, `H042-H049`, `pipeline_gaps_report.md` | arXiv 摘要误读、repo 静默跳过、HTML 结构损失 | 部分修复，通用 router 未落地 |
| questioner/reader 折叠、reviewer 缺席 | H010 原始 workflow | 240 张全量卡不满足四角色合同 | 未回溯重跑 |
| direct accepted publish | H010, `d36f6f7a` | 跳过 draft/promotion/fusion gate | 未回溯修复 |
| 并行 extraction 破坏 fusion | `H013-H016`, `operational_lessons.md` | 同批 cards 不可互见，merge_candidate=0 失真 | 后置补救，非原位修复 |
| 240 张绝对路径 | `H012-H015`, `b26dafc3` | 不可移植 | 已规则替换 |
| cluster target / exploration boundary | `H017-H018`, `H035-H038` | 过度分组、孤岛、跨域桥梁不足 | 审计与补链后部分修复 |
| YAML dual-format related | `fb7b4060`, `v4_comprehensive_audit.md` | 69/280 parser 缺陷，11 张全损 links | 已修复 |
| authority flattening | `H040-H043`, deep audit | 174/280 零 hedge，源权威被扁平化 | V4 未系统性重写 |
| context leakage / provenance gap | `H032-H034` | comparison 卡吸收未归因跨卡概念 | 个案修复，机制仅记录 |
| grep false positive | `H033-H034` | supported/unsupported 二元审计不可靠 | 方法论已修正 |
| phantom sources | `H043-H053` | 30/74 零卡；实践层和社区层缺失 | webpage 部分补回；repo/reddit 未完整覆盖 |
| stale state | `H011`, registry source map | setup/0 与 328-card 终态冲突 | 未修复 |

## 6. Git 版本变化账本

| Git | 版本变化 | 可证明事实 | 不能证明 |
|---|---|---|---|
| `bc81cafa` / `39d57d16` | scaffold + start prompt | V4 合同和目录出现 | 管线已执行 |
| `2df61ddb` | skills + seed 15 | 角色分离实验、draft/JJ、shell promotion、reviewer 调用 | 完整 skills 被原样注入；全量会保持同形态 |
| `1b92f941` | 15→19 | cross-link、拆卡、缺失卡补充 | 原始问答重新执行 |
| `d36f6f7a` | 19→259 | 43-agent direct-to-KB 批次、240 新文件 | reviewer、fusion、draft promotion 已执行 |
| `f4ec89b6` | 首轮 governance | canonical 修正、117/259 linked、8-card spot-check | 全库 fusion 和语义治理完成 |
| `b26dafc3` | 259→280 | post-hoc cluster governance、comparison、related 派生、路径替换 | pre-ingest fusion；无 cluster damage |
| `fb7b4060` / `5d7586fc` | FSJS + 修复 | YAML/JJ/ref/orphan/leakage 等补救 | 原始 production contract 被追溯满足 |
| `a13d02ff` / `4ec3b45d` | 深审与 pipeline gaps | 缺陷被量化和解释 | 缺陷已修复 |
| `d2ebcf41` | 280→约295 | path/cross-link/repo demo 增量 | arXiv 全文重提取；20 repo 完整处理 |
| `044312a2` | 295→328 | webpage markdown 化、19 源增量 33 cards | 新卡完整 reviewer/fusion/governance |
| `5f2824e9` | learnings capsule | 后验经验固化 | 文档中的 as-built claim 自动等同 primary 执行事实 |

## 7. 可安全进入 Module Recall 的结论

1. V4 首次把 questioning、reader、reframing、reviewer 写成独立技能合同，并在单一 seed 上真实试验了分离角色。
2. V4 规模化时为吞吐量把角色折叠为一 agent/源，直接写 accepted KB；这是设计到执行的关键断裂。
3. V4 的窄义 script ingest 只在 seed 可直接证明；全量的所谓 Ingest 实际只是 index rebuild。
4. 初始 fusion 缺席，graph governance 在 publish 后补做；cluster 补救又制造 YAML、孤岛和探索边界问题。
5. FSJS 是 V4 最可靠的后验机制贡献：机械全量、语义分片、结构化裁决、集中综合；同时必须保留 grep false-positive 的自我修正。
6. V4 最终 328-card KB 是多轮修复后的终态，不是一次严格执行原始 pipeline spec 的结果。

## 8. 仍需保留为未知或冲突的事项

- 43-source workflow payload 汇总 235 cards，而 Git/终态支持 240 新卡；缺少逐 agent immutable run ledger。
- 无法逐源确认全量 agent 实际完成了几轮、自主读取了哪个文件、是否内部执行过未落盘的 coverage check。
- arXiv path-only repair 是否把部分摘要生成卡错误地重新指向 bundle，尚无逐卡重提取证据闭合。
- 328-card 终态的全部 JJ、fusion、reviewer、graph coverage 没有统一分母；280-card 治理指标不应外推到后增 48 cards。
- comparison sink、单向边中哪些是语义正确、哪些是遗漏，只完成了抽样和局部修复，不能由边方向机械判断。
