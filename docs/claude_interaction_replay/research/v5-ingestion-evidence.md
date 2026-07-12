# V5 入库机制证据审计

## 1. 审计口径

本文把「入库（ingestion）」拆成两种含义：一是原始材料进入知识卡的完整生产链，二是 `tools/ingest.py` 将 draft 发布到 KB 的窄义发布步骤。两者不可混用；后者不读取 raw material，也不生成卡片正文。【证据：`claude_code:claude-primary-v5:H010`；`loops/v5_llm_wiki_loop_20260612/tools/ingest.py`】

证据标签分为三类：**设计要求（design contract）** 指 prompt、task、skill 中规定的目标流程；**已执行（observed execution）** 指 primary event、产物或原始提交可直接证明的动作；**后验推断（retrospective inference）** 指质量问题出现后才形成的解释，不得倒写成初始执行事实。【证据：`docs/claude_interaction_replay/registry/source-registry.json`；`docs/claude_interaction_replay/events/events.claude.primary-v5.v2.jsonl`】

下文用 `H002` 等短名指向完整 event_id，例如 `H002` = `claude_code:claude-primary-v5:H002`。primary session 是执行顺序主证据；sub-agent 记录只可证明动作/效果，repo capsule 只可验证产物与后验纠偏，Git 时间只证明进入版本控制的时间。【证据：`docs/claude_interaction_replay/registry/source-registry.json`】

## 2. 审计结论

V5 可证实的主链是：**source router 选择读取面 → 四波并行 extraction → 直接落 draft card/JJ → 全量 draft 后做 fusion candidate scan 与判定 → `ingest.py` 发布 accepted cards 并重建 index → batch link / orphan pass / backward backlink → FSJS citation/evidence audit**。【证据：`H002`；`loops/v5_llm_wiki_loop_20260612/learnings/execution_summary.md`】

V5 不是「完全没有问答」。后验核查确认 extraction agent 读取了全文并做过浅层 QA；但运行时仅收到约 50 行骨架，没有收到 questioning、reader、reframing、reviewer 四份完整合同，因此不能认定五阶段 questioning、严格 SATISFIED 和 reviewer quit-audit 在原始全量 extraction 中完整执行。【证据：`H010`；`loops/v5_llm_wiki_loop_20260612/skills/questioning/SKILL.md`；`loops/v5_llm_wiki_loop_20260612/skills/reader/PROMPT.md`；`loops/v5_llm_wiki_loop_20260612/skills/reframing/PROMPT.md`；`loops/v5_llm_wiki_loop_20260612/skills/reviewer/PROMPT.md`】

`tools/ingest.py` 不是内容质量门（quality gate）：它对任何非 `superseded` 卡改成 `accepted`、复制正文/JJ，并按第一个 `source_id` 生成索引；它不验证 schema 完整性、citation 支撑、questioning 阶段或正文信息密度。【证据：`loops/v5_llm_wiki_loop_20260612/tools/ingest.py`】

V5 的工程治理确实落地，包括 typed source paths、`evidence_basis`、YAML parser 写入、fusion、related graph 和 audit artifacts；但「工程完整」不等于「内容充分」。用户在 `H014` 指出的“四环层级”案例证明 citation 可以存在而概念仍未解释，`H008`、`H010`、`H011` 又证明首轮审计合同没有覆盖论证深度与 questioning 阶段完成度。【证据：`H008`；`H010`；`H011`；`H014`；`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/drafts/cards/agt-four-privilege-ring-execution-sandbox.md`】

## 3. 用户触发时间线

| 首次触发 event_id | 用户触发 | 对流程的证据意义 |
|---|---|---|
| `claude_code:claude-primary-v5:H002` | 启动 V5 goal，要求读取 handoff/task/start prompt/v4 input，并约束独立 0→1、中文、Opus、提交格式 | 首次触发 source router、skills、extraction、draft、fusion、ingest、governance、audit、documentation 的整条生产链；同一 event window 报告 63 个有效源、487 draft、477 active。【证据：`H002`；`loops/v5_llm_wiki_loop_20260612/MINIMAL_START.md`】 |
| `claude_code:claude-primary-v5:H003` | 询问是否有专门审计流程 | 首次触发对已执行 audit 是否完整的复核；回答承认首轮只完整覆盖 FILTER/SYNTHESIZE，SHARD/JUDGE 主要为抽样。【证据：`H003`】 |
| `claude_code:claude-primary-v5:H004` | 指出「没做完」，要求 agent team 区分脚本化与语义审计 | 首次触发专业审计项和 script/agent 边界盘点，得到 26 子项中 17 已覆盖、9 缺失的当时判断。【证据：`H004`】 |
| `claude_code:claude-primary-v5:H005` | 要求补全审计方案、历史问题和解决思路 | 首次触发 `v5_audit_methodology.md`、`audit_mechanical.py` 和机械报告的补建。【证据：`H005`；`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/kb/audits/v5_audit_methodology.md`；`loops/v5_llm_wiki_loop_20260612/tools/audit_mechanical.py`】 |
| `claude_code:claude-primary-v5:H006` | `/goal` 要求设计 workflow 并完成审计 | 首次触发四个 source-affinity shard、跨源泄漏检查和综合 JUDGE；当时报告 848 条脚注、26 子项覆盖、0 Critical。【证据：`H006`；`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/kb/audits/v5_final_audit_report.md`】 |
| `claude_code:claude-primary-v5:H007` | 要求 sub-agent 固化内容 | 首次触发原始全量提交 `ca3865b7`；该提交一次性包含 tools、skills、draft、KB、audit 和 learnings，不能证明内部阶段的精确 Git 顺序。【证据：`H007`；Git `ca3865b75f133eb97ca342a79d0da2ffa76af74c`；`docs/claude_interaction_replay/registry/source-registry.json`】 |
| `claude_code:claude-primary-v5:H008` | 要求多节点 probe「V5 card 为何比 V4 贫乏」 | 首次触发信息密度后验诊断；产出 `v5_info_density_diagnosis.md`。【证据：`H008`；`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/kb/audits/v5_info_density_diagnosis.md`】 |
| `claude_code:claude-primary-v5:H010` | 追问 raw-material pipeline、全文 QA 与提问机制是否消失 | 首次触发对实际 Workflow prompt 的直接核查；结论从「skills 已完整传递」修正为「只传入骨架 prompt」。【证据：`H009`；`H010`】 |
| `claude_code:claude-primary-v5:H012` | 将 V5 定义为失败样本，要求设计实验达到/超过 V4 | 首次触发修正版 `extract_prompt_v2.md` 和 MemGPT 27-card 实验；它是 post-V5 experiment，不属于原始 487 draft 的生产合同。【证据：`H012`；`loops/v5_llm_wiki_loop_20260612/tools/extract_prompt_v2.md`；`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/drafts/cards/experiment/`】 |
| `claude_code:claude-primary-v5:H014` | 指出「四环层级」有 citation 但未解释 | 首次把 citation-present / explanation-absent 的质量缺陷落实到单卡证据。【证据：`H014`；`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/drafts/cards/agt-four-privilege-ring-execution-sandbox.md`】 |

## 4. 真实流程阶段：输入、动作、输出

| 阶段 | 实际输入 | 可证实动作 | 实际输出 / artifact | 首次触发 |
|---|---|---|---|---|
| 0. Setup / contract | V4 learnings、V5 task/handoff/start prompt、raw source tree | 建立 tools 与四份 skills；设计 `evidence_basis`、hedge、YAML lint、source dispatch。【证据：`loops/v5_llm_wiki_loop_20260612/LOOP_START_PROMPT.md`；`loops/v5_llm_wiki_loop_20260612/CLAUDE_CODE_HANDOFF.md`】 | `loops/v5_llm_wiki_loop_20260612/tools/`、`loops/v5_llm_wiki_loop_20260612/skills/`。【证据：Git `ca3865b7`；Git `226b2913`】 | `H002`。【证据：`H002`】 |
| 1. Source router | `data/raw/{source_type}/{slug}/` | 按类型选择文件；检查文件存在、>=500 bytes、头 2048 bytes 不含 blocked/captcha/403 等词。【证据：`loops/v5_llm_wiki_loop_20260612/tools/source_router.py`】 | repo-relative `paths` JSON；运行期报告 74 total / 63 OK / 11 failed。【证据：`H002`；`loops/v5_llm_wiki_loop_20260612/tools/source_router.py`】 | `H002`。【证据：`H002`】 |
| 2. Questioner / reader extraction | router 选出的全文读取面、source slug、evidence basis | 四波并行 sub-agent extraction；实际 agent 读全文并做浅层 QA，但没有完整四-skill runtime contract。【证据：`H002`；`H010`；`loops/v5_llm_wiki_loop_20260612/learnings/execution_summary.md`】 | 未落盘 digest/Q&A/SATISFIED/quit-audit transcript；落盘结果直接进入 draft card 与 JJ。【证据：`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/drafts/`；`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/kb/audits/v5_info_density_diagnosis.md`】 | `H002`；缺口首次被用户触发核查于 `H010`。【证据：`H002`；`H010`】 |
| 3. Reframe → draft/card | 浅层 QA 的回答与 source evidence | extraction agent 直接写 Markdown frontmatter/body/typed footnotes，并写 per-card justification；初始报告为 487 drafts。【证据：`H002`；`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/drafts/cards/`；`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/drafts/justification/`】 | 原始 487 cards + 后续 1 fusion card = draft 根目录 488；11 标记 `superseded`，剩余 477 被发布。【证据：`loops/v5_llm_wiki_loop_20260612/learnings/execution_summary.md`；Git `ca3865b7`；`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/drafts/cards/`】 | `H002`。【证据：`H002`】 |
| 4. Fusion | 全部 `drafts/cards/*.md` 的 `canonical_concept`、aliases、source_ids | `fusion_candidates.py` 只输出跨来源共享 normalized term 的候选对；后续 agent/LLM 判定被报告为 163 对：9 duplicate、1 merge、153 distinct link。【证据：`loops/v5_llm_wiki_loop_20260612/tools/fusion_candidates.py`；`loops/v5_llm_wiki_loop_20260612/learnings/execution_summary.md`】 | 11 张 superseded drafts；1 张双来源 fusion card `agt-four-privilege-ring-execution-sandbox.md` 及其 fusion justification。【证据：`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/drafts/cards/agent-runtime-four-privilege-rings.md`；`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/drafts/cards/agt-privilege-ring-sandboxing.md`；`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/drafts/cards/agt-four-privilege-ring-execution-sandbox.md`；`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/drafts/justification/agt-four-privilege-ring-execution-sandbox.md`】 | `H002`。【证据：`H002`】 |
| 5. Narrow ingest / publish | draft cards、draft justifications | 对 `superseded` 复制到 archive；其余状态一律改 `accepted` 并复制到 `kb/cards`；复制 JJ；按第一个 source_id 重建 index。【证据：`loops/v5_llm_wiki_loop_20260612/tools/ingest.py`】 | 477 accepted KB cards、原始提交中的 11 archive cards、488 KB justifications、`kb/indexes/cards.md`。【证据：Git `ca3865b7`；`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/kb/cards/`；`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/kb/indexes/cards.md`】 | `H002`。【证据：`H002`】 |
| 6. Link governance | 477 accepted cards 的 canonical/aliases/source_ids/related | `batch_link.py` 对所有跨来源同词候选自动双向写 `related`；orphan pass 对 81 卡做全局 grep/读卡/判断；`backward_backlink.py` 再补缺失反向 related。【证据：`loops/v5_llm_wiki_loop_20260612/tools/batch_link.py`；`loops/v5_llm_wiki_loop_20260612/tools/backward_backlink.py`；`loops/v5_llm_wiki_loop_20260612/learnings/execution_summary.md`】 | 总结记录 batch_link 151 对、81 orphan 全部补链、423 条 backward fixes；初版报告称 0 orphan / 0.5% asymmetry。【证据：`loops/v5_llm_wiki_loop_20260612/learnings/execution_summary.md`；`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/kb/audits/audit_report.md`】 | `H002`。【证据：`H002`】 |
| 7. Citation / evidence audit | accepted card body、typed footnotes、raw source、related graph、evidence_basis | 先随机每卡一条脚注 FILTER（431），后补机械全量格式匹配（848）与 source-shard semantic JUDGE；另做 YAML、dangling、orphan、asymmetry、leakage 等检查。【证据：`H003`；`H004`；`H005`；`H006`；`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/kb/audits/filter_report.md`；`loops/v5_llm_wiki_loop_20260612/tools/audit_mechanical.py`】 | `filter_report.md`、`judge_faithfulness.md`、`v5_mechanical_audit_report.json`、`v5_judge_results.md`、`v5_final_audit_report.md`。【证据：`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/kb/audits/`】 | 专门复核首次为 `H003`；补全为 `H005`；深审完成为 `H006`。【证据：`H003`；`H005`；`H006`】 |
| 8. Post-hoc diagnosis / experiment | V4/V5 cards、原始 V5 audit、MemGPT source | 多 probe 诊断信息密度；设计强制 Phase 3、边界句和 distinction 的 `extract_prompt_v2`；重跑单源实验。【证据：`H008`；`H012`；`loops/v5_llm_wiki_loop_20260612/tools/extract_prompt_v2.md`】 | `v5_info_density_diagnosis.md` 与 `drafts/{cards,justification}/experiment/`；不回写原始 477 active KB。【证据：`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/kb/audits/v5_info_density_diagnosis.md`；`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/drafts/cards/experiment/`】 | `H008` / `H012`。【证据：`H008`；`H012`】 |

## 5. 专项机制审计

### 5.1 Source router

**设计要求（design）**：arXiv 读 `agent_source_bundle.txt`；webpage 读 `markdown.md > text.txt`；GitHub repo 读 `material_bundle*.txt > repo/README.md`；文本类读 `text.txt`；多 sub-bundle 应分别调度 extraction；失败源应进入 `scrape_status: failed` 语义。【证据：`loops/v5_llm_wiki_loop_20260612/CLAUDE_CODE_HANDOFF.md`；`loops/v5_llm_wiki_loop_20260612/LOOP_START_PROMPT.md`】

**已执行（observed）**：代码实现了上述路径优先级、repo-relative path 和 500-byte/blocked-keyword gate；GitHub 多 bundle 返回列表。失败时只返回 JSON `status: failed` 与统一的 `no_valid_reading_surface`，没有写回 source metadata，也没有保留具体 quality-gate reason。【证据：`loops/v5_llm_wiki_loop_20260612/tools/source_router.py`】

**缺口**：Phase 0 要求的 `repo2doc.py` 在 V5 tools 中不存在，execution summary 明确承认 repo2doc 未实施、repo 主要消化 README；因此「18 repo 全覆盖」是 README-level coverage，不是 repository corpus coverage。【证据：`loops/v5_llm_wiki_loop_20260612/task.md`；`loops/v5_llm_wiki_loop_20260612/tools/`；`loops/v5_llm_wiki_loop_20260612/learnings/execution_summary.md`】

**冲突**：`H002`/router 运行记录为 74/63/11；execution summary 同一文档先写 11、后改 10；`loop_state.json` 写 12 并列 12 IDs；version source map 将该 claim 标为 `confidence: conflicting`，不得静默选一个数字。【证据：`H002`；`loops/v5_llm_wiki_loop_20260612/learnings/execution_summary.md`；`loops/v5_llm_wiki_loop_20260612/loop_state.json`；`docs/claude_interaction_replay/registry/source-map.json`】

### 5.2 Questioner / reader

**设计要求（design）**：reader 首轮产 digest；questioner 执行 Phase 1-5；每轮 Q&A 即时 reframe；SATISFIED 要求 core claims 全覆盖、无开放 chase-chain、再问不产生新原子概念；reviewer 在退出后做 core-claim coverage 与 source grep quit-audit。【证据：`loops/v5_llm_wiki_loop_20260612/skills/questioning/SKILL.md`；`loops/v5_llm_wiki_loop_20260612/skills/reader/PROMPT.md`；`loops/v5_llm_wiki_loop_20260612/skills/reviewer/PROMPT.md`】

**已执行（observed）**：可以确认全文读取和浅层 QA，不能确认完整五阶段。`H010` 明确记录运行时 Workflow prompt 未注入四份完整 skills，Phase 3-4、严格 SATISFIED 与 quit-audit 实际缺席。【证据：`H010`】

**不可反推项**：原始 V5 artifact 没有 per-source digest、逐轮问题/答案、SATISFIED 自检或 reviewer 结果；信息密度报告也明确写「round/phase 未落盘，无法精确量化」。因此 skills 文件存在只能证明设计，不证明运行时执行。【证据：`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/`；`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/kb/audits/v5_info_density_diagnosis.md`】

**后验修复（post-hoc）**：`extract_prompt_v2.md` 强制 Phase 3、边界条件句、SATISFIED hard gate 和 round-bearing JJ；它由 `H012` 的实验触发，不能用来证明原始 477 cards 的 extraction 合同。【证据：`H012`；`loops/v5_llm_wiki_loop_20260612/tools/extract_prompt_v2.md`；`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/drafts/justification/experiment/`】

### 5.3 Draft / card 与 narrow ingest

**设计要求（design）**：一 Q&A 默认一卡，多 idea 拆卡；卡片含 source_ids、evidence_basis、canonical/aliases/summary/related、typed footnotes 与 append-only JJ；ingest 必须 script-only，禁止 LLM 复制 body。【证据：`loops/v5_llm_wiki_loop_20260612/skills/reframing/PROMPT.md`；`loops/v5_llm_wiki_loop_20260612/LOOP_START_PROMPT.md`；`loops/v5_llm_wiki_loop_20260612/learnings/next_loop_prep.md`】

**已执行（observed）**：初始 extraction 报告 487 drafts；fusion 新建 1 card 后根目录为 488，11 superseded，477 accepted。原始 `ca3865b7` 同时保存 488 drafts、477 KB cards 和 11 archive cards。【证据：`H002`；`loops/v5_llm_wiki_loop_20260612/learnings/execution_summary.md`；Git `ca3865b7`；`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/drafts/cards/`】

**ingest 的真实边界**：`ingest.py` 只解析 frontmatter、状态翻转、复制与索引；它没有调用 `yaml_lint.py`，也不检查 source file、quote、JJ、body 或 accepted target 的旧文件。因而「被 ingest」只等价于通过状态分支，不等价于内容验收。【证据：`loops/v5_llm_wiki_loop_20260612/tools/ingest.py`；`loops/v5_llm_wiki_loop_20260612/tools/yaml_lint.py`】

**内容缺口实例**：用户在 `H014` 指定的 fusion card 有 source footnote 和四个 ring 名称，但未说明 kernel/supervisor/user/untrusted 各层职责和权限边界；助手当时确认「citation 存在不等于概念已解释」。【证据：`H014`；`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/drafts/cards/agt-four-privilege-ring-execution-sandbox.md`】

### 5.4 Fusion

**设计要求（design）**：所有 extraction 完成后再 sequential fusion scan；读取边界是 `drafts/cards/*.md`；采用 anti-merge bias，尽量以 distinct link 保留原子性与 provenance。【证据：`loops/v5_llm_wiki_loop_20260612/task.md`；`loops/v5_llm_wiki_loop_20260612/LOOP_START_PROMPT.md`；`loops/v5_llm_wiki_loop_20260612/learnings/execution_summary.md`】

**实际脚本（observed code）**：`fusion_candidates.py` 仅对 canonical + aliases 做字符归一化倒排，输出不同 source_ids 的共享 term pairs；它不读取正文、不判 duplicate/merge、不写 superseded、不生成 fusion card。【证据：`loops/v5_llm_wiki_loop_20260612/tools/fusion_candidates.py`】

**实际决策结果（observed artifacts）**：总结报告 163 candidates → 9 duplicate + 1 merge + 153 distinct link；11 张 superseded card 的 frontmatter 仍在 drafts，唯一 merge 的两张源卡都指向 `agt-four-privilege-ring-execution-sandbox`，fusion JJ 说明两来源互补内容。【证据：`loops/v5_llm_wiki_loop_20260612/learnings/execution_summary.md`；`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/drafts/cards/agent-runtime-four-privilege-rings.md`；`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/drafts/cards/agt-privilege-ring-sandboxing.md`；`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/drafts/justification/agt-four-privilege-ring-execution-sandbox.md`】

**证据缺口**：工作区未保留完整 163-candidate 清单、逐对判定 ledger、判定 agent prompt 或 153 distinct-link 的语义理由；因此只能验证汇总数字与最终 superseded/fusion 状态，不能重放全部 fusion decisions。【证据：`loops/v5_llm_wiki_loop_20260612/tools/fusion_candidates.py`；`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/`；`docs/claude_interaction_replay/registry/source-registry.json`】

### 5.5 Citation / evidence

**设计要求（design）**：四类 typed footnotes 为 `src/card/dist/url`；source footnote 指向 router 实际阅读的 repo-relative path、section/paragraph 和 quote；`evidence_basis` 必填；源含 hedge 时必须保留。【证据：`loops/v5_llm_wiki_loop_20260612/LOOP_START_PROMPT.md`；`loops/v5_llm_wiki_loop_20260612/skills/reframing/PROMPT.md`】

**已执行（observed）**：cards 确实使用 `data/raw/...` source paths 和 `evidence_basis`；fusion card 同时保留 webpage 与 repo README 两组 source footnotes。【证据：`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/kb/cards/agt-four-privilege-ring-execution-sandbox.md`；`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/kb/cards/`】

**审计范围冲突**：初版 FILTER 是「431 张有脚注卡各随机抽 1 条」，不是全脚注；后续机械报告称 848 条，但 parser 只对严格 regex `SRC_FOOTNOTE_RE` 增加 total，`SRC_FOOTNOTE_RE2` 分支没有增加或验证总数。故 `v5_final_audit_report.md` 的「全部 848 条」只能解释为符合该 regex 的子集，不能证明 card corpus 中每个 source footnote definition 都被验证。【证据：`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/kb/audits/filter_report.md`；`loops/v5_llm_wiki_loop_20260612/tools/audit_mechanical.py`；`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/kb/audits/v5_final_audit_report.md`】

**质量维度缺口**：`H006` 的深审可以支持「当时审计合同下未确认 fabrication/extrapolation」，但 `H011` 明确承认合同没有检查论证深度或 questioning 是否到达 Phase 3-4；`H014` 又给出 citation-present / explanation-absent 的反例。【证据：`H006`；`H011`；`H014`】

**distinction 缺失**：后验信息密度报告记录 V5 distinction footnotes 完全缺失、card footnotes 退化为简单指针；因此设计中的四类 typed footnote 没有全部形成有效 artifact。【证据：`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/kb/audits/v5_info_density_diagnosis.md`】

### 5.6 Index / backlink

**Index 实际行为**：`ingest.py` 只取 `source_ids[0]` 分组，索引只列 source heading 与 slug，不含 title、aliases、evidence basis、第二来源或 backlink；双来源 fusion card 只出现在 `microsoft-agent-governance-toolkit-docs` 分组，不会同时出现在 repo 分组。【证据：`loops/v5_llm_wiki_loop_20260612/tools/ingest.py`；`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/kb/indexes/cards.md`；`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/kb/cards/agt-four-privilege-ring-execution-sandbox.md`】

**Batch link 实际行为**：`batch_link.py` 重新运行 canonical/aliases 同词候选逻辑，对每个跨来源候选无语义判定地写双向 `related`，且明确保持 body 不变；所以 `related` graph edge 不是 typed `[^card-N]` citation，也不携带 distinction reason。【证据：`loops/v5_llm_wiki_loop_20260612/tools/batch_link.py`】

**Backward backlink 实际行为**：代码对每条 A→B 均补 B→A，只检查 target 是否存在，不判断关系是否 symmetric；这比 execution summary 所写「若关系为 symmetric」更强，也可能把方向性关系强制对称化。【证据：`loops/v5_llm_wiki_loop_20260612/tools/backward_backlink.py`；`loops/v5_llm_wiki_loop_20260612/learnings/execution_summary.md`】

**Orphan pass 证据边界**：execution summary 记录 81 张孤儿逐卡 grep/Read 并全部补链，但没有独立脚本、逐卡 decision ledger 或 before/after snapshot；只能验证总结与终态报告，不能重放 81 次语义判断。【证据：`loops/v5_llm_wiki_loop_20260612/learnings/execution_summary.md`；`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/kb/audits/audit_report.md`】

**终态冲突**：初版 `audit_report.md` 写 0 orphan / 9 of 1813 asymmetric；最终报告与机械 JSON 写 2 orphans / 9 of 1815 asymmetric；`loop_state.json` 仍写 0% orphan。三者是不同审计时点/口径，档案未提供统一的 snapshot id，不能合并成单一终态数字。【证据：`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/kb/audits/audit_report.md`；`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/kb/audits/v5_final_audit_report.md`；`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/kb/audits/v5_mechanical_audit_report.json`；`loops/v5_llm_wiki_loop_20260612/loop_state.json`】

## 6. 设计要求 vs 已执行 vs 后验推断

| 机制 | 设计要求（design） | 已执行（observed） | 后验推断（retrospective） |
|---|---|---|---|
| Source routing | 类型分流、质量门、sub-bundle、repo2doc。【证据：`loops/v5_llm_wiki_loop_20260612/LOOP_START_PROMPT.md`；`loops/v5_llm_wiki_loop_20260612/task.md`】 | 类型分流与质量门已编码；repo2doc 未落地，repo 多为 README。【证据：`loops/v5_llm_wiki_loop_20260612/tools/source_router.py`；`loops/v5_llm_wiki_loop_20260612/learnings/execution_summary.md`】 | source router 改善读取面，但不能证明 repo 深度消化。【证据：`docs/claude_interaction_replay/content/versions/v5.md`；`loops/v5_llm_wiki_loop_20260612/learnings/execution_summary.md`】 |
| Questioning | 五阶段、逐轮 reframe、SATISFIED 三条件、quit-audit。【证据：`loops/v5_llm_wiki_loop_20260612/skills/questioning/SKILL.md`；`loops/v5_llm_wiki_loop_20260612/skills/reviewer/PROMPT.md`】 | 全文 + 浅层 QA；完整 skills 未进入 runtime prompt。【证据：`H010`】 | 信息贫乏被归因于 Phase 3-4 缺失、过早停止和 reframing 损失；这是 `H008`、`H009`、`H010` 后形成的解释。【证据：`H008`；`H009`；`H010`；`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/kb/audits/v5_info_density_diagnosis.md`】 |
| Draft/JJ | 原子卡、typed evidence、append-only decision journal。【证据：`loops/v5_llm_wiki_loop_20260612/skills/reframing/PROMPT.md`】 | 487 初始 drafts、JJ 与 1 fusion card 已落盘；原始 round/phase 未系统落盘。【证据：`H002`；`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/drafts/`；`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/kb/audits/v5_info_density_diagnosis.md`】 | `extract_prompt_v2` 的 hard gates 是 `H012` 后的实验修复，不属于原始执行。【证据：`H012`；`loops/v5_llm_wiki_loop_20260612/tools/extract_prompt_v2.md`】 |
| Fusion | post-extraction sequential、anti-merge、语义判定。【证据：`loops/v5_llm_wiki_loop_20260612/task.md`；`loops/v5_llm_wiki_loop_20260612/learnings/execution_summary.md`】 | 脚本只发现候选；最终状态支持 9 duplicate + 1 merge + links 的汇总，但无完整 ledger。【证据：`loops/v5_llm_wiki_loop_20260612/tools/fusion_candidates.py`；`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/drafts/cards/`；`loops/v5_llm_wiki_loop_20260612/learnings/execution_summary.md`】 | 「anti-merge 有效」是总结层评价，不能替代逐对 decision evidence。【证据：`loops/v5_llm_wiki_loop_20260612/learnings/execution_summary.md`】 |
| Ingest | script-only publish，避免 LLM 复制 body。【证据：`loops/v5_llm_wiki_loop_20260612/learnings/next_loop_prep.md`】 | status flip、copy、first-source index 已编码并产出 477 accepted。【证据：`loops/v5_llm_wiki_loop_20260612/tools/ingest.py`；`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/kb/cards/`；`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/kb/indexes/cards.md`】 | 把 ingest 成功等同于卡片质量通过，是不受代码支持的推断。【证据：`loops/v5_llm_wiki_loop_20260612/tools/ingest.py`；`H014`】 |
| Citation/evidence | typed footnotes、quote/location、hedge、evidence basis。【证据：`loops/v5_llm_wiki_loop_20260612/skills/reframing/PROMPT.md`】 | source paths/evidence basis 已落盘；审计覆盖格式子集，distinction 未形成。【证据：`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/kb/cards/`；`loops/v5_llm_wiki_loop_20260612/tools/audit_mechanical.py`；`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/kb/audits/v5_info_density_diagnosis.md`】 | 「0 fabrication」只在已检查范围内成立，不覆盖概念解释充分性。【证据：`H006`；`H011`；`H014`】 |
| Index/backlink | 顺序治理、双向 backlink、孤儿补链、YAML parser。【证据：`loops/v5_llm_wiki_loop_20260612/task.md`】 | index、batch_link、orphan pass、backward pass 均有终态/总结证据。【证据：`loops/v5_llm_wiki_loop_20260612/tools/ingest.py`；`loops/v5_llm_wiki_loop_20260612/tools/batch_link.py`；`loops/v5_llm_wiki_loop_20260612/tools/backward_backlink.py`；`loops/v5_llm_wiki_loop_20260612/learnings/execution_summary.md`】 | 0 orphan 与 0.5% asymmetry 受 snapshot/口径冲突限制，不能作为无条件单值事实。【证据：`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/kb/audits/audit_report.md`；`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/kb/audits/v5_final_audit_report.md`；`loops/v5_llm_wiki_loop_20260612/loop_state.json`】 |

## 7. Git 证据与版本映射

原始执行分支只给出三个关键提交：`624e52d0` 初始化 V5 capsule，`f0a7ed17` 做配置审计，`ca3865b7` 在 `H007` 后一次性固化全量产物。`ca3865b7` 能证明 2026-06-12 21:01+08:00 时产物已进入 Git，不能证明 source router、extraction、fusion、ingest、audit 的精确内部提交顺序。【证据：`H007`；Git `624e52d0`、`f0a7ed17`、`ca3865b7`；`docs/claude_interaction_replay/registry/source-registry.json`】

2026-07-09 的 `226b2913 → 9e954607 → ba6d5a56 → 2251069b → 57dd21e2` 把 toolchain、draft extraction、KB publish、governance/audit、density diagnosis 拆成逻辑 commits；该链从另一分支接回 `624e52d0`，不以 `ca3865b7` 为祖先，因此是后续发布/整理历史，不是原始执行时间线。【证据：Git 上述 commits；`docs/claude_interaction_replay/registry/source-registry.json`】

原始 `ca3865b7` 含 `kb/archive/` 的 11 张 superseded cards；后续发布链 `ba6d5a56` 与当前 HEAD 未保留该 archive 目录，但 drafts 仍保留 superseded cards。这是 publication state 与原始 archive state 的差异，不应解释为 fusion 从未归档。【证据：Git `ca3865b7`；Git `ba6d5a56`；`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/drafts/cards/`；`loops/v5_llm_wiki_loop_20260612/tools/ingest.py`】

`version-registry.json` 将 V5 定义为 retrospective，核心是 source router、evidence basis、顺序治理和 backlink/orphan；`source-map.json` 唯一 V5 mapping 明确标记 dead-source 与信息密度为 conflicting，但其 `evidence_refs` 只列 learnings 与初始化 commit `624e52d0`，没有直接列 `ca3865b7` 或 primary event file，证据映射仍不完整。【证据：`docs/claude_interaction_replay/registry/version-registry.json`；`docs/claude_interaction_replay/registry/source-map.json`；`docs/claude_interaction_replay/content/versions/v5.md`】

## 8. 已知冲突与缺口清单

| ID | 冲突 / 缺口 | 可安全采用的表述 |
|---|---|---|
| G1 | 死源为 10/11/12 三种数字。【证据：`H002`；`loops/v5_llm_wiki_loop_20260612/learnings/execution_summary.md`；`loops/v5_llm_wiki_loop_20260612/loop_state.json`】 | 「运行期 router 报告 11；其他 capsule 字段冲突，未裁决。」【证据：`docs/claude_interaction_replay/registry/source-map.json`】 |
| G2 | `task.md` 全部 checkbox 仍为未勾选，但 frontmatter 和 loop_state 声称 complete。【证据：`loops/v5_llm_wiki_loop_20260612/task.md`；`loops/v5_llm_wiki_loop_20260612/loop_state.json`】 | 以 artifact/event 逐项证明，不以 checkbox 或 `complete` 字段代替执行证据。【证据：`H002`；`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/`】 |
| G3 | 完整 skills 在 repo 中存在，但未进入原始 Workflow runtime context。【证据：`H010`；`loops/v5_llm_wiki_loop_20260612/skills/`】 | 「设计完整、运行时注入不完整。」【证据：`H010`】 |
| G4 | 原始 QA 过程无 digest/Q&A/SATISFIED/quit-audit 落盘。【证据：`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/`；`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/kb/audits/v5_info_density_diagnosis.md`】 | 只能确认全文 + 浅层 QA，不能宣称五阶段完整执行。【证据：`H010`】 |
| G5 | 163 fusion decisions 无逐对 ledger。【证据：`loops/v5_llm_wiki_loop_20260612/tools/fusion_candidates.py`；`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/`】 | 可报告汇总与最终状态，不可重放每一判定。【证据：`loops/v5_llm_wiki_loop_20260612/learnings/execution_summary.md`；`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/drafts/cards/`】 |
| G6 | 初版 431 是抽样；后版 848 是严格 regex 子集，机械 parser 未覆盖所有格式。【证据：`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/kb/audits/filter_report.md`；`loops/v5_llm_wiki_loop_20260612/tools/audit_mechanical.py`；`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/kb/audits/v5_final_audit_report.md`】 | 「已检查范围内未确认 fabrication」，不写「所有 citation 均验证」。【证据：`H006`；`H011`】 |
| G7 | Citation 可存在但解释不足；四环卡是明确案例。【证据：`H014`；`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/drafts/cards/agt-four-privilege-ring-execution-sandbox.md`】 | citation provenance 与 knowledge sufficiency 分开验收。【证据：`H014`】 |
| G8 | 初版 0 orphan/1813 edges，后版 2 orphan/1815 edges，loop_state 仍为 0%。【证据：`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/kb/audits/audit_report.md`；`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/kb/audits/v5_final_audit_report.md`；`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/kb/audits/v5_mechanical_audit_report.json`；`loops/v5_llm_wiki_loop_20260612/loop_state.json`】 | 报告时注明 artifact 与 snapshot，不给无来源的统一终值。【证据：`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/kb/audits/audit_report.md`；`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/kb/audits/v5_final_audit_report.md`】 |
| G9 | `backward_backlink.py` 无 relation type，却把所有 related 边强制对称。【证据：`loops/v5_llm_wiki_loop_20260612/tools/backward_backlink.py`】 | 该 pass 保证图对称，不保证关系语义正确。【证据：`loops/v5_llm_wiki_loop_20260612/tools/backward_backlink.py`】 |
| G10 | Index 只登记 first source，多来源 fusion card 丢失第二来源入口。【证据：`loops/v5_llm_wiki_loop_20260612/tools/ingest.py`；`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/kb/indexes/cards.md`；`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/kb/cards/agt-four-privilege-ring-execution-sandbox.md`】 | `cards.md` 是 first-source derived index，不是完整 provenance index。【证据：`loops/v5_llm_wiki_loop_20260612/tools/ingest.py`】 |
| G11 | 原始提交有 11 archive cards，当前发布 HEAD 无 `kb/archive/`。【证据：Git `ca3865b7`；Git `ba6d5a56`；`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/drafts/cards/`】 | 区分 original execution snapshot 与 published HEAD。【证据：`docs/claude_interaction_replay/registry/source-registry.json`】 |
| G12 | `extract_prompt_v2.md` 与 27-card experiment 是 `H012` 后产物。【证据：`H012`；`loops/v5_llm_wiki_loop_20260612/tools/extract_prompt_v2.md`；`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/drafts/cards/experiment/`】 | 不得用实验修正版规则为原始 477 cards 背书。【证据：`H012`】 |

## 9. 可复述的最小事实集

1. V5 首次由 `H002` 启动，原始执行报告 63 个有效源、487 初始 drafts；fusion 后发布 477 active cards。【证据：`H002`；`loops/v5_llm_wiki_loop_20260612/learnings/execution_summary.md`】
2. Source router 已真实实现类型分流与质量门，但 repo2doc 未实现，GitHub repo 主要停留在 README 阅读面。【证据：`loops/v5_llm_wiki_loop_20260612/tools/source_router.py`；`loops/v5_llm_wiki_loop_20260612/learnings/execution_summary.md`】
3. 原始 extraction 有全文读取和浅层 QA，没有证据证明完整五阶段 questioner/reader/reviewer contract 被执行；`H010` 反而记录 runtime prompt 注入断路。【证据：`H010`】
4. `ingest.py` 是发布脚本，不是 raw-material reasoning pipeline，也不是内容质量门。【证据：`loops/v5_llm_wiki_loop_20260612/tools/ingest.py`】
5. Fusion candidate discovery 是脚本化的，duplicate/merge/distinct 判定不是该脚本完成；最终状态可见，但完整决策 ledger 缺失。【证据：`loops/v5_llm_wiki_loop_20260612/tools/fusion_candidates.py`；`loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/drafts/cards/`】
6. Citation/evidence 工程化已落地，但审计覆盖存在 parser/口径边界，且 citation presence 不保证概念解释充分。【证据：`loops/v5_llm_wiki_loop_20260612/tools/audit_mechanical.py`；`H014`】
7. Index/backlink 显著改善图的机械完整性，但 first-source index、无语义的自动双向 related、缺失 orphan ledger 仍限制其 provenance 与语义可审计性。【证据：`loops/v5_llm_wiki_loop_20260612/tools/ingest.py`；`loops/v5_llm_wiki_loop_20260612/tools/batch_link.py`；`loops/v5_llm_wiki_loop_20260612/tools/backward_backlink.py`；`loops/v5_llm_wiki_loop_20260612/learnings/execution_summary.md`】
