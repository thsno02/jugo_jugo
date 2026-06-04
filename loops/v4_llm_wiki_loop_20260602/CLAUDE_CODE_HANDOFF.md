---
loop_id: v4_llm_wiki_loop_20260602
created: 2026-06-02
status: setup
---

# v4 Handoff

v4 是 questioning-loop-based 知识卡片生产管线。

## 管线

```
collect --> extract (questioning loop) --> ingest --> evolve/governance
```

- **collect**: 获取 raw material（本轮暂手动）
- **extract**: questioner<-->reader 对话 exhaust 材料 --> Q&A --> draft cards + justification
- **ingest**: 脚本移动 draft --> active KB（无 LLM body 复制）
- **evolve/governance**: dedup + canonical 归一化 + distinction linking

## 设计文档

设计在 v3 capsule 的 `future_plans/` 中完成。关键文件：

| 文件 | 内容 |
|---|---|
| `pipeline_spec.md` | 完整管线规格——阶段定义、I/O schema、全局约束。**先读这个。** |
| `questioning_loop_design.md` | Mode A/B 设计——对话协议、5 阶段提问策略、收敛机制 |
| `card_metadata_template.md` | 卡片完整格式参考——所有字段规则、typed footnote 用法 |
| `jj_template.md` | Justification Journal 模板——6 种事件类型 + rollup 机制 |

路径：`../v3_llm_wiki_loop_20260525/future_plans/`

## 执行约束

- **执行模式**: parallel (A), `--permission-mode bypassPermissions`
- **输出语言**: 中文为主；schema key / path / code / id 英文
- **git**: 无 Co-Authored-By trailer
- **KB 独立**: 只用本 loop 自己的 cards；不比较/引用外部 loop
- **Zettelkasten**: 原子卡、无 taxonomy；结构靠 link + governance 涌现
- **grep-only recall**: 不引入 embedding/jieba/向量；zh/en/同义词多轮 grep
- **无 tentative/stable**: 卡出生即终态；KB 通过 governance + consumption 成熟

## 目录结构

```
v4_llm_wiki_loop_20260602/
+-- skills/questioning/SKILL.md     # questioner SOP
+-- skills/reader/PROMPT.md         # reader 应答契约
+-- tools/                          # 脚本（待开发）
+-- outputs/llm_wiki/
|   +-- drafts/{cards,justification}  # Stage 2 output
|   +-- kb/{cards,archive,justification,indexes}  # Stage 3+4
+-- run/                            # per-material run-record
+-- queue.jsonl                     # work queue
+-- loop_state.json                 # loop state
+-- status.json                     # loop status
+-- task.md                         # v4 task checklist
```
