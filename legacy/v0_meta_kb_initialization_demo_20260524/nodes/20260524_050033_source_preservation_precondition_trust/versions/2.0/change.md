# Change: 1.0 -> 2.0

node_id:: 20260524_050033_source_preservation_precondition_trust
from_version:: 1.0
to_version:: 2.0
change_scale:: major
propagation_required:: true
created_at:: 2026-05-24T05:06:34+08:00
run_id:: .llmwiki/runs/run_20260524_050634_major_impact_simulation/

## 为什么变化

这个 candidate 把 support contract 从“source preservation 是信任前提”改成“source preservation 加 provenance 才能支撑信任”。

## 旧含义

1.0 强调 preserved local source material 是后续 audit 的主要前提。

## 新含义

2.0 认为 preservation 仍然必要，但如果没有 provenance 记录 source use、synthesis rationale、rejection decisions、audit trail 和 revision triggers，就不足以支撑信任。

## Semantic delta

Candidate 把 provenance 从 supporting downstream concept 提升为 trust contract 的必要组成部分。

## 为什么这是 major

下游 nodes 如果把 source preservation 当作充分背景，就可能需要把 provenance requirements 一起纳入 claim。

## 预期影响

所有通过 footnotes 或 references 引用 1.0 的 nodes 都应进入 impact review。Impact analysis 不应自动重写它们。
