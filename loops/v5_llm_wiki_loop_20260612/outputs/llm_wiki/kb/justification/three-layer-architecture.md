# Justification: three-layer-architecture

## Extraction rationale
材料明确提出三层架构作为系统结构基础，权责边界清晰（immutable/LLM-owned/co-evolved），是独立的架构知识单元。

## Evidence quality
- 材料以列表形式明确列出三层
- 每层的权责有直接引文支撑
- 实践者视角，无 hedge

## Atomicity check
仅覆盖架构分层及各层权责。具体操作（ingest/query/lint）分卡处理。
