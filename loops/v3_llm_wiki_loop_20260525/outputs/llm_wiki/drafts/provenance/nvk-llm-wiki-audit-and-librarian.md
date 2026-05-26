---
schema: draft_card_provenance.v3
draft_card: ../cards/nvk-llm-wiki-audit-and-librarian.md
material_id: llm-wiki-net
digest_id: digest_llm-wiki-net
source_paths:
  - data/raw/webpage/llm-wiki-net/text.txt
created_time: 2026-05-26T11:27:00+08:00
edited_time: 2026-05-26T11:27:00+08:00
edited_entity: llm
---

## 源证据

- Librarian 段（行 52–54）：
  > "Score every article for staleness and quality. Two-tier scan: fast metadata check, then deep content read for flagged articles. Checkpoint recovery. Machine-readable JSON + human-readable report."
- Audit 段（行 56–58）：
  > "Answer the broader trust question. Reuse the librarian pass, trace outputs across raw/ , wiki/ , and output/ , detect drift, inspect provenance, and do fresh research when local evidence is not enough."
- Commands 表里相应行（行 222–228）：
  > "/wiki:audit Truth-seeking audit across wiki, outputs, provenance, and fresh research when needed."
  > "/wiki:librarian Score articles for staleness and quality. Checkpoint recovery. --article <path> for single article."
  > "/wiki:lint Health checks. --fix auto-repairs. --deep web-verifies facts."
  > "/wiki:retract Remove a source and clean up downstream references."
- audit `--artifact` / `--project` 用法（行 256–257）：
  > "/wiki:audit --wiki nutrition / /wiki:audit --artifact output/report-gut-brain.md"
  > "/wiki:audit --project nutrition-playbook"

## 卡片范围是否成立

卡片只组合 librarian / audit / lint / retract 四条命令的源材料描述。"与 git 仓库 CI 类比"是合理的认知工具，把命令映射到工程师熟悉的 CI 概念，未引入源材料外的事实。"操作规则"段从源材料"Checkpoint recovery"、"two-tier scan"、"do fresh research when local evidence is not enough"等明文要素引申。"audit 触发 fresh research 的预算上限"是边界警告，超出源材料显式描述但属于合理的工程提醒。

## 发表门控结果

本轮未运行。

## 备注

- 与 `agents-md-as-schema-layer` 形成"schema 是写合同 / audit 是验合同"的呼应。
- 与 `docs-as-code-merge-block-incentive` 在"机器化的 trust check"上同源——可作为 cross-link 候选。
