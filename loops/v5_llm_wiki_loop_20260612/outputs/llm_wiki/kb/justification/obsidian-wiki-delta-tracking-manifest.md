# Justification: obsidian-wiki-delta-tracking-manifest

## 为什么产出此卡
Delta tracking 是该框架在 Karpathy 原始模式上最核心的增强之一，解决了重复摄入的效率问题，材料在 "How it works" 和 "What we added" 两处均突出强调。

## Evidence basis 判定
选择 `code_implementation`：`.manifest.json` 是框架实际使用的数据文件，README 描述的行为对应 wiki-ingest skill 的实现逻辑。

## 原子性
本卡聚焦于 manifest + delta tracking 这一具体机制，不涉及四阶段流水线的其他阶段细节。
