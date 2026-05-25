# skill_eval

status:: seed
created_at:: 2026-05-24T05:10:00+08:00
language:: zh-CN

## 目的

用每个 0-1 node run 记录明确 skill failure，避免从一次性观察升级全局 skill。

## Demo 规则

优先减少明确 failure mode，而不是追求抽象意义上的“更好”。只有 completed run 暴露出可命名 failure mode，才升级 skill。
