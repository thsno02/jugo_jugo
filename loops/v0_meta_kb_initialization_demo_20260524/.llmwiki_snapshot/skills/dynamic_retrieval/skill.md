# dynamic_retrieval

status:: seed
created_at:: 2026-05-24T05:10:00+08:00
language:: zh-CN

## 目的

把 evidence gap 转化为 retrieval request，保存 retrieved raw source，更新 manifest，并写入 provenance。

## Demo 规则

优先减少明确 failure mode，而不是追求抽象意义上的“更好”。只有 completed run 暴露出可命名 failure mode，才升级 skill。
