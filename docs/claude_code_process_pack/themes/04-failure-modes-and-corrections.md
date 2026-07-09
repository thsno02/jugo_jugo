---
schema: claude_code_theme.v1
theme: failure_modes_and_corrections
publish_status: sanitized
---

# Failure Modes And Corrections

Claude Code 的 session 价值之一，是暴露了 agent loop 的失败模式。这些失败模式比单次输出更值得发布。

## Failure Modes

| Failure Mode | Symptom | Correction |
| --- | --- | --- |
| objective drift | 从“生成 KB”漂移到“讨论如何生成 KB” | 用 loop task 和 process provenance 锚定 source-grounded production |
| top-down relapse | 先做 hub/topic，再补 atomic | 强制 bottom-up：atomic card -> later hub |
| defensive truncation | paper 后半段丢失 | 大上下文下优先 full read |
| schema overgrowth | card 变成机器中间态 | schema 保持简单，provenance 另存 |
| cluster damage | 过度合并损坏原子性 | anti-merge bias |
| manual YAML edits | related/frontmatter 格式错误 | script-based governance |
| shallow extraction | 覆盖变广但论证变浅 | EXTRACT_PROMPT v2 要求 Phase 3、boundary、tradeoff、distinction footnotes |

## Post-v5 Diagnosis

v5 的问题不是没有产出，而是信息密度（information density）下降：广度提高，论证层次降低。这个失败模式已经被记录为后验诊断，并成为 v6 的管线输入。

## Reusable Rule

高质量 agent loop 不应只记录成功结果，也要记录为什么某次成功仍然不够好。failure mode 是下一轮 loop 的原材料。
