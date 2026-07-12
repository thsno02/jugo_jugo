# 07. 证据索引

## 7.1 使用说明

本索引不公开原始 session UUID 或本机绝对路径。Local-only process records 使用语义 alias、原始 JSONL 行号、UTC 时间和 line SHA256 定位。

`line_sha256` 的计算口径为：对该 JSONL 记录的 UTF-8 字节去掉单个 trailing newline 后计算 SHA256。授权复核者可以在本机相应 session 中按 timestamp 搜索，再核对 line number 和 digest。

证据等级：

- `D`：direct evidence
- `P`：process record
- `I`：inference，仅由其他证据推导

## 7.2 Local-only 来源别名

| Alias | 描述 | 关键边界 |
|---|---|---|
| `S-PARENT` | 人类发起的 plugin 开发父任务 | `thread_source=user`；包含 Planner、Executors 和 sibling gate notifications |
| `S-E6` | full-corpus readiness E6 worker | `thread_source=subagent`；父任务派发的窄任务包 |
| `S-V23` | v2/v3 semantic extraction worker | `thread_source=subagent`、`fork_context:false`；后续承接用户安全追问 |

## 7.3 人类目标与 Planner 合同

### E-HUMAN-001

- Source: `S-PARENT`, line `6071`
- UTC: `2026-07-12T00:32:11.892Z`
- Level: `D`
- Summary: 人类要求把完整 LLM Wiki 开发链路做成 plugin；未列安全扫描细节。
- line_sha256: `5f13e897d88a739b7e0ec3c00ac274c66741dbaa4e353e4bbc33a2e3c22486ce`

### E-HUMAN-002

- Source: `S-PARENT`, line `6094`
- UTC: `2026-07-12T00:36:28.825Z`
- Level: `D`
- Summary: 人类指定在 `plugins/` 开发，并用 loops 逐模块、逐阶段验证。
- line_sha256: `39be1783a496e907b308e5351bb817781bac0372cfa243ec3596f89491d8e767`

### E-HUMAN-003

- Source: `S-PARENT`, line `6359`
- UTC: `2026-07-12T00:58:49.901Z`
- Level: `D`
- Summary: 人类要求 Planner-Executor-Reviewer 和并行 sub-agents。
- line_sha256: `941034872e8c247898848a48dd4ea40cb0bb5542367a60b949d50cc687268c70`

### E-PLAN-001

- Source: `S-PARENT`, line `6372`
- UTC: `2026-07-12T00:59:15.452Z`
- Level: `P`
- Summary: 父代理要求 Planner 阅读 plugin 与 v0-v5 事实源，自行制定 DoD、loop 验收和 deterministic/semantic boundary。
- line_sha256: `e193e2e52b742bd914b949cfe30b41e9a7a8e1d4bb0d387cb855223c4a180169`

### E-PLAN-002

- Source: `S-PARENT`, line `6490`
- UTC: `2026-07-12T01:05:54.767Z`
- Level: `P`
- Summary: Planner 输出 plugin 级隐私/密钥/path 阻断门、v0-v5 disposition、无未审敏感项和 script/Skill 分工。
- line_sha256: `eb85894429169669439ea78e069359c45f2a26d630fd9a82e4453f78f44cba5b`

### E-CONTRACT-001

- Source: `S-PARENT`, line `6858`
- UTC: `2026-07-12T01:25:40.471Z`
- Level: `P`
- Summary: 父代理创建 Completion Contract，将 Planner 推导固化为 agent-authored explicit contract。
- line_sha256: `05d01f13f089f20909a56c486d1ef883516c41e161523e8aa199fea809db1a97`

## 7.4 E6 职能产生

### E-DISPATCH-E6

- Source: `S-PARENT`, line `7148`; mirrored in `S-E6`, line `7`
- UTC: `2026-07-12T01:43:25.183Z` / worker receipt `01:43:29.100Z`
- Level: `D/P`
- Summary: 明确要求 `full_corpus.py` 覆盖事实源、hash、disposition、parallel parse、secret/PII/path scan、cross-reference 和 semantic work ledger。
- parent_line_sha256: `d3ceb1449c62244762dfd066008914afefa529324118230cc888e8d71b472c0f`
- worker_line_sha256: `a870f39be6835c2a102b9e0db8dbd5050c9593c34a7fa8a0ca4dfd8773bbb6e0`

### E-E6-READ-ARCHIVE

- Source: `S-E6`, line `41`
- UTC: `2026-07-12T01:44:30.236Z`
- Level: `D`
- Summary: E6 在补丁前读取 archive schemas、publication runtime 和 `validate_archive.py`。
- line_sha256: `74d7e5f2671c646df3b281df108c116251b56d2e7ed33161822f7db46e392913`

### E-E6-DESIGN

- Source: `S-E6`, line `94`
- UTC: `2026-07-12T01:46:32.937Z`
- Level: `P`
- Summary: E6 声明产出 readiness、status、semantic 三类 ledger；敏感命中只记录类别/行，不复制原文或绝对路径。
- line_sha256: `558cdd7459d1fab8f11850505084fbf9e1977717eb3d812a8e47852fa6b4498d`

### E-E6-PATCH

- Source: `S-E6`, line `115`
- UTC: `2026-07-12T01:53:39.656Z`
- Level: `D`
- Summary: E6 创建 `full_corpus.py`；首次可证写入扩展 `PATTERNS` 和 `sensitivity_decisions`。
- line_sha256: `bee100f04fb3132b9b2b519b0f1ed5381350d16556452d3d8e6e6130d48ca44d`

## 7.5 v2/v3 任务与额外扫描

### E-DISPATCH-V23

- Source: `S-PARENT`, line `7567`; worker prompt `S-V23`, line `7`
- UTC: `2026-07-12T02:12:30.578Z` / worker receipt `02:12:37.958Z`
- Level: `D/P`
- Summary: 父代理以 `fork_context:false` 派发 v2/v3 extraction，要求 `sensitivity_decisions` 和不复制 secrets/personal data。
- parent_line_sha256: `689a487f8021c3025e06763a2ac2bfe01a54be00b180badddb8a98f147a118c0`
- worker_line_sha256: `a3945c91b795d27116217e304e536721d4c66af4d85fcb5a9ddc3ce424a58783`

### E-V23-INITIAL

- Source: `S-V23`, line `10`
- UTC: `2026-07-12T02:12:41.169Z`
- Level: `P`
- Summary: worker 最初正确说明“仅记录处置结论，不复制原值”。
- line_sha256: `b8cfb0f633dfc8285379852e646f265876026cbc63af2817b869f3a9117d8b0f`

### E-V23-REGEX-CONTEXT

- Source: `S-V23`, line `141`
- UTC: `2026-07-12T02:17:49.782Z`
- Level: `D`
- Summary: worker 读取 `full_corpus.py` 输出，近邻上下文中出现完整 PATTERNS。
- line_sha256: `2900fa9bde342d47bd85435ccd29f889c09c1ab94333c8fc3bee3da071d02139`

### E-V23-SCAN-PARSE-ERROR

- Source: `S-V23`, lines `163-164`
- UTC: `2026-07-12T02:22:43.010Z`
- Level: `D`
- Summary: 首次 ad-hoc sensitive scan command 因 shell unmatched quote 失败；不是 policy block。
- call_line_sha256: `a9140f446b64a5acfda7d957479fea95a8ce975f3b742b2bf0f709670660ab28`
- result_line_sha256: `dc6c7a769dcf2de8e17cd1f4f058bbc0e78952b6a82ff8bcfba714bf83216201`

### E-V23-QA-DECLARATION

- Source: `S-V23`, line `192`
- UTC: `2026-07-12T02:24:16.587Z`
- Level: `P`
- Summary: worker 明确宣布“只剩来源哈希与敏感模式终检”；这是执行边界漂移的直接定位点。
- line_sha256: `cc2839b6a095e21574a88acb1742aac6c66b9fab0c94614be924ad6443d83b38`

### E-V23-SCAN

- Source: `S-V23`, lines `196-197`
- UTC: `2026-07-12T02:24:32.469Z`
- Level: `D`
- Summary: 有效扫描 extraction v2/v3；返回只涉及 `sha256` 字段。
- call_line_sha256: `e547865fe8ec936b9ac776241e773f84684ad121b00211088ff211637e3ea846`
- result_line_sha256: `f48c30e899e8275a51ef0f23bc1ed656c6c33a7ba754e957d6d9368e7d12ea19`

### E-V23-SHA-FALSE-POSITIVE

- Source: `S-V23`, lines `200-201`
- UTC: `2026-07-12T02:24:43.000Z`
- Level: `D`
- Summary: 命中形状被定位为 SHA256 中的 18 位数字片段；专题不复制该片段。
- call_line_sha256: `b00e3159d39eb1590640908cba851e3efb02f74c5cb6c760968697d5706fe763`
- result_line_sha256: `852c0c71ca5569d83c45bd40c7a5f0b268b7043716469d7763fc17c30d4c3e97`

### E-V23-SCAN-CLEAN

- Source: `S-V23`, lines `205-206`
- UTC: `2026-07-12T02:24:57.872Z`
- Level: `D`
- Summary: 删除所有 `sha256` 字段后复检，无 semantic content 命中。
- call_line_sha256: `4bcb892b33858160f877fb8e08a32ec449cf3a1c055261a166177dc189318033`
- result_line_sha256: `84d922904826fe6272522f3261022af9e16c60ce481e033ad0d28d7239e36c25`

### E-V23-COMPLETE

- Source: `S-V23`, line `216`
- UTC: `2026-07-12T02:25:09.943Z`
- Level: `D`
- Summary: 原 extraction 任务正常 `task_complete`，没有该线程安全阻断。
- line_sha256: `be4f743918ccc16d4bb9057e772022448236bf76c278759f527e969e0a34d1e7`

## 7.6 真实 Gate 与事后归因

### E-GATE-001

- Source: `S-PARENT`, line `9684`
- UTC: `2026-07-12T03:52:33.338Z`
- Level: `D`
- Summary: sibling sub-agent 返回第一次可见 `possible cybersecurity risk` error。
- line_sha256: `9932e4c29832ef522535260ccdbfa38e6b8b7797f899d9ed8c4c9ef40fd3ab94`

### E-GATE-002

- Source: `S-PARENT`, line `11578`
- UTC: `2026-07-12T05:33:25.710Z`
- Level: `D`
- Summary: 第二个不同 agent path 返回同类 gate。
- line_sha256: `be9a9899f99166064c146a236addc8df87532c104941be9bf56318f86e3e5ad4`

### E-GATE-003

- Source: `S-PARENT`, line `12612`
- UTC: `2026-07-12T08:26:08.086Z`
- Level: `D`
- Summary: 第三个 agent path 返回同类 gate。
- line_sha256: `34dbd9fa3f5b2ddbea1332c3c26641aa90a33351b0344bb566e16b264f8f3fa4`

### E-GATE-004

- Source: `S-PARENT`, line `13686`
- UTC: `2026-07-12T11:08:47.727Z`
- Level: `D`
- Summary: runtime integrity reviewer 相关 sub-agent 返回同类 gate。
- line_sha256: `53e669a706814cc41bdc38a5a15ed934bc8ce902696653a834cb143b4b2a1d55`

### E-GATE-005

- Source: `S-PARENT`, line `13882`
- UTC: `2026-07-12T11:30:00.188Z`
- Level: `D`
- Summary: 最近一次 reviewer gate；初始任务已说明本地授权/只读/无网络，但要求检查 hardlink/TOCTOU 和 fresh mutation。
- line_sha256: `5e0fcd3317ec16d56ea41a1d9e1e0e273ea9f3103edf50e11992d57ab618f1d9`

### E-USER-GATE-QUESTION

- Source: `S-V23`, line `223`
- UTC: `2026-07-12T11:42:14.648Z`
- Level: `D`
- Summary: 用户在旧 v2/v3 worker 中首次询问“为什么会触发网络安全审计”。
- line_sha256: `2b51a20bf4c04cced21fedf7fefd086063b345ffca96de9de17dca84c5fefd86`

### E-ATTRIBUTION-HYPOTHESIS

- Source: `S-V23`, line `229`
- Level: `P`
- Summary: 初次回答仍以“更可能”描述 regex/classifier 误报。
- line_sha256: `00cf75e5f6b183ca75499618fb813bf1dde870170eab79f4e0a6e75816585dde`

### E-ATTRIBUTION-OVERCLAIM

- Source: `S-V23`, line `270`
- Level: `P`
- Summary: 后续回答在无新增 classifier 证据时断言上层分类器已由这些特征触发；不确定性丢失。
- line_sha256: `d5007f84d127864926c9777af41413462d5e8d4f80dd0157bab4733e87f92535`

## 7.7 Repository Evidence Snapshot

以下 SHA256 是本专题取证时的文件快照，不代表首次创建版本。`full_corpus.py`、Completion Contract 等 plugin 文件当时仍未进入 Git 基线；出生历史以 process record 为准。

| Locator | Relevant lines | Snapshot SHA256 | 用途 |
|---|---:|---|---|
| `docs/claude_interaction_replay/README.md` | 65-75, 94-101 | `41476bc7f5046affd9690f9f73952b3448332a5285ec065255143619acb7d5e6` | local-only 与 publication privacy invariant |
| `docs/claude_interaction_replay/archive.json` | 508-517 | `afd2e92977fac50af6996c10659131d455aac1b5eee9de02a196ecaf433e9858` | machine scan + human review gate |
| `docs/claude_interaction_replay/content/privacy-audit.md` | 14-40 | `04b4827f67e72d4c680e5bbf2f19b83776df91c3d7a0ba50a34241a696ff799e` | 原始脱敏与公开边界 |
| `docs/claude_interaction_replay/tools/validate_archive.py` | 19-29, 163-176 | `c874085952bc7f61f778a31dd7b1a2d2b8132b7ccbfe6329a9a343576cede248` | 旧 archive scanner 先例 |
| `plugins/llm-wiki-builder/development/COMPLETION_CONTRACT.md` | 11-16, 28 | `33f0e18af1f54ed147024b592737f221027f5cfee206d5408e0bb23a1a61669e` | agent-authored plugin contract |
| `plugins/llm-wiki-builder/scripts/integration/full_corpus.py` | 22-33, 61-117, 130-155, 303-321 | `f6e83b44c9cd97c59203f8e15c0bffc4d43f75030975f1a8c713e0cab4408cee` | pattern scan、status、semantic handoff |
| `plugins/llm-wiki-builder/scripts/integration/semantic_corpus.py` | 515-527, 632-705 | `fb37a02cd4e892502628d3cb28622462f0d7b974e84d94b6eb5b8608c4899532` | 后续 schema 固化；晚于 v2/v3 scan |
| `plugins/llm-wiki-builder/development/loops/loop-050-v0-v5-full-corpus/outputs/corpus-status-ledger.jsonl` | full file | `9cad837a23a85a0d125d13522e824b19bc096f3eaff22bd76c66c9719301dc1c` | 当前 finding 类别；无 `secret.*` |

## 7.8 完整性与限制

- JSONL line hashes 能证明本专题引用的本地记录未被转述替换，但不能证明平台侧没有额外未落盘事件。
- 当前 repository file hashes 只描述取证快照；并行 worker 可能继续修改未跟踪 plugin 文件。
- 本索引不复制 scan 命中的 18 位数字片段，也不保存任何疑似 credential 原值。
- `E-ATTRIBUTION-*` 是事后回答的过程证据，不能反向证明扫描当时的隐藏动机。
- classifier rule id、detector stage 和 UI event binding 仍缺失，统一标为 unknown。
