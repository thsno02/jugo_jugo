---
id: openkb-skill-factory
title: OpenKB Skill Factory——Wiki 蒸馏为可分发 Agent 技能
status: draft
card_type: feature-module
tags: [skill-factory, anthropic-skill, agent-skill, knowledge-distillation, openkb]
created_time: 2026-06-12T18:00:00+08:00
edited_time: 2026-06-12T18:00:00+08:00
edited_entity: llm
source_ids: [repo-vectifyai-openkb]
evidence_basis: code_implementation
justification: ../justification/openkb-skill-factory.md
canonical_concept: openkb-skill-factory
aliases: [Skill Factory, openkb skill new, openkb skill, skill compilation, marketplace.json]
summary: >-
  OpenKB openkb-skill-factory Skill-Factory 将wiki蒸馏为可分发Anthropic-Skill;
  产出SKILL.md+references/+可选scripts/文件夹; 自动更新marketplace.json;
  Claude-Code/Codex-CLI/Gemini-CLI/Cursor原生加载; 质量保障validate结构lint/eval触发精度评估/history+rollback迭代管理;
  chat中可交互式迭代refinement
related: [openkb-two-layer-architecture, openkb-compiled-wiki-over-rag]
---

Skill Factory 是 OpenKB 的 generator 之一，将编译后的 wiki 子集蒸馏为可分发的 Anthropic Skill——一个 Claude Code、Codex CLI、Gemini CLI 和 Cursor 均可原生安装加载的便携文件夹。据材料描述："Drop in a book's worth of papers; out comes a specialist that other agents can call on."[^src-1] [^card-1]

**产出结构**：SKILL.md（YAML frontmatter + when-to-use + approach）、references/（深度参考材料）、可选 scripts/（仅当 intent 暗示需要计算时生成）。编译同时自动更新 `marketplace.json`，使整个 KB 可一行安装。[^src-2]

**分发方式**：本地安装复制至 `~/.claude/skills/`；远程分享推至 GitHub 后他人执行 `npx skills@latest add <org>/<repo>`。[^src-3]

**质量保障三件套**：1) `skill validate`——结构 lint（frontmatter、文件大小、wikilinks、scripts/ stdlib 检查），编译结束自动执行；2) `skill eval`——触发精度评估，LLM 生成评估提示，grader LLM 评分激活；3) `skill history` / `skill rollback`——每次覆写保存前一版本至 iteration-N/ 目录，可回滚任意迭代。[^src-4]

在 `openkb chat` 中可交互式迭代 skill 编译，无需重新运行整个管线。[^src-5]

[^card-1]: 参见 [[openkb-two-layer-architecture]] 关于 generators 在双层架构中的定位
[^src-1]: `data/raw/github_repo/repo-vectifyai-openkb/repo/README.md` -- "Skill Factory" P1 -- "Drop in a book's worth of papers; out comes a specialist that other agents can call on."
[^src-2]: `data/raw/github_repo/repo-vectifyai-openkb/repo/README.md` -- "Skill Factory" P2 -- "SKILL.md # YAML frontmatter + when-to-use + approach / references/ / (scripts/)"
[^src-3]: `data/raw/github_repo/repo-vectifyai-openkb/repo/README.md` -- "Skill Factory" P3 -- "npx skills@latest add <your-org>/<your-repo>"
[^src-4]: `data/raw/github_repo/repo-vectifyai-openkb/repo/README.md` -- "Quality gates" P1 -- "structural validation, trigger-accuracy + body-coverage evaluation, and full history/rollback"
[^src-5]: `data/raw/github_repo/repo-vectifyai-openkb/repo/README.md` -- "Iterate from chat" P1 -- "compilation is one-shot, but follow-up edits aren't"
