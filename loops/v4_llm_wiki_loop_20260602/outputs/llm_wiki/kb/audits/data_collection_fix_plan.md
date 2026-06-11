---
report_type: data_collection_fix_plan
loop: v4_llm_wiki_loop_20260602
date: 2026-06-08
audits_consumed: 6
source_types_audited: [arxiv, webpage, github_repo, reddit, hacker_news, pypi, gist_raw]
total_sources: 74
sources_with_valid_reading_surface: 44
sources_broken_or_empty: 12
sources_needing_repo2doc: 18
priority: critical
---

# 数据采集管线修复计划

## 1. 执行摘要

v4 管线的 74 个原始源中，仅 44 个（59%）具有可靠的 agent 阅读面。12 个源完全失败（Reddit 6 + 空壳 webpage 3 + arxiv PDF-only 1 + GitHub API 全部 403），18 个 github_repo 源缺少 material_bundle.txt 导致知识被锁死在代码仓库中。

核心问题是**逐类型的阅读路由不一致**：

| 源类型 | 期望阅读面 | 现状 | 缺口率 |
|--------|-----------|------|--------|
| arxiv (17) | agent_source_bundle.txt | 15 有效, 1 bloated (46MB), 1 PDF-only | 12% |
| webpage (27) | text.txt (markdown 格式) | 21 有效, 3 空壳, 3 高损耗 | 22% |
| github_repo (20) | material_bundle.txt | 仅 2 有 bundle | 90% |
| reddit (6) | thread.json + text.txt | 全部 blocked | 100% |
| hacker_news (1) | text.txt | 完美 | 0% |
| pypi (2) | pypi.json + text.txt | 完美 | 0% |
| gist_raw (1) | text.txt | 完美 | 0% |

**修复优先级**：github_repo bundle 生成 > arxiv bundle 修复 > Reddit 重抓 > webpage 增强提取。

---

## 2. 逐类型诊断

### 2.1 arxiv（17 源）

**现状**：
- 16/17 有 agent_source_bundle.txt（TeX 全文拼接），1 个仅 PDF
- text.txt 对所有源**完全无用**（仅 arXiv 摘要页 HTML chrome，~5KB）
- agent_source_bundle.txt 大小范围 66KB-279KB（正常），arxiv-ragas 为异常 46MB

**正确的 boundary-read**：
```
优先级链：agent_source_bundle.txt > source.pdf (需 PDF2text) > [跳过 text.txt]
```

**问题清单**：

| 源 | 问题 | 严重度 |
|----|------|--------|
| arxiv-ragas | bundle 含 anthology.bib (44MB ACL 全量书目) | HIGH |
| arxiv-knowledge-compounding | 无 TeX 源，仅 source.pdf (1.2MB)，无 bundle | HIGH |
| 所有 17 个 | text.txt 被 run_loop.py 路由逻辑 fallback 误选 | CRITICAL (已识别) |
| 所有 16 个 bundle | 含 .sty/.bst/.cls 噪声文件浪费 token | LOW |

**路径**：
- bundle 目录：`data/raw/arxiv/<slug>/agent_source_bundle.txt`
- 异常源：`data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt`
- PDF-only：`data/raw/arxiv/arxiv-knowledge-compounding/source.pdf`

---

### 2.2 webpage（27 源）

**现状**：
- 21/27 的 text.txt 含有效内容（质量参差）
- 3 个空壳（aicritique x2 被 Alibaba office-sec 拦截，obsidian-help 为 SPA 无 SSR）
- 3 个高损耗（langchain 233x 压缩比，OWASP 两源 124-135x）

**正确的 boundary-read**：
```
优先级链：text.txt（需升级为 markdown 格式）> raw.html（仅 fallback，需 readability 提取）
```

**问题清单**：

| 源 | 问题 | text.txt 大小 | 严重度 |
|----|------|--------------|--------|
| aicritique-enterprise-knowledge | Alibaba 域名拦截，零内容 | 13B | DEAD |
| aicritique-enterprise-knowledge-dynamic-20260524 | 同上（重复 dead 源） | 13B | DEAD |
| obsidian-help-link-notes | SPA，仅 JS loader | 27B | DEAD |
| langchain-long-term-memory-docs | Next.js SSR 但 extractor 丢失正文 | 11KB (nav only) | HIGH |
| owasp-agentic-top10-2026 | 内容在 PDF link 中，页面仅摘要 | ~12KB | MEDIUM |
| owasp-llm-top10-2025 | 同上 | ~12KB | MEDIUM |

**路径**：
- 有效源：`data/raw/webpage/<slug>/text.txt`
- raw HTML：`data/raw/webpage/<slug>/raw.html`

---

### 2.3 github_repo（20 源）

**现状**：
- 所有 20 个 clone 成功（git_exit_code=0）
- 仅 2/20 有 material_bundle.txt（microsoft-graphrag 143KB, nvk-llm-wiki 438KB）
- 所有 20 个的 github_repo.json 和 README.remote 为 403 rate-limit 错误
- 无 text.txt（设计上不存在此文件）

**正确的 boundary-read**：
```
优先级链：material_bundle.txt > repo/README.md（仅临时 fallback）
```

**问题清单**：

| 优先级 | 源 | .py/.md 文件数 | 唯一知识 | 状态 |
|--------|---|---------------|---------|------|
| T1-#1 | repo-microsoft-agent-governance-toolkit | 1791py/729md | policy DSL, runtime enforcement | 无 bundle |
| T1-#2 | repo-microsoft-graphrag | 570py/56md | indexing pipeline, community detection | 有 bundle (143KB) |
| T1-#3 | repo-nvk-llm-wiki | 0py/722md | thesis research, parallel agent | 有 bundle (438KB) |
| T1-#4 | repo-kytmanov-obsidian-local | 81py/16md | local-first Ollama, rejection loop | 无 bundle |
| T1-#5 | repo-ar9av-obsidian-wiki | 10py/58md | 15+ agent skill framework | 无 bundle |
| T1-#6 | repo-ngmeyer-librarian-mcp | Rust | trigram, BFS, community detect | 无 bundle |
| T1-#7 | repo-vectifyai-openkb | 65py/5md | vectorless PageIndex | 无 bundle |
| T1-#8 | repo-atomicstrata-llm-wiki-compiler | TS/Node | multi-provider compilation | 无 bundle |

**路径**：
- 仓库根：`data/raw/github_repo/<slug>/repo/`
- 现有 bundle：`data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt`

---

### 2.4 reddit（6 源）

**现状**：全部失败。所有文件（text.txt, page.html, thread.json, browser.html, browser_text.txt）均为 Reddit 反爬拦截页面的 HTML。thread.json 不是 JSON 而是 HTML。metadata.json 标记 `blocked: true`。

**正确的 boundary-read（修复后）**：
```
优先级链：thread.json (结构化评论树) > text.txt (纯文本提取)
```

**路径**：`data/raw/reddit/<slug>/`

---

### 2.5 hacker_news / pypi / gist_raw（4 源）

**现状**：全部完美，无需修复。

| 类型 | 阅读面 | 内容质量 |
|------|--------|---------|
| hacker_news (1) | text.txt 50KB, 95 comments | 完整社区讨论 |
| pypi (2) | pypi.json + text.txt | 结构化包元数据 |
| gist_raw (1) | text.txt 12KB | Karpathy 原始 gist 全文 |

---

## 3. 新管线架构：逐类型路由

### 3.1 架构总览

```
seed_sources.json
       |
       v
fetch_sources.py  ──────────────────────── 原始抓取（保持不变）
       |
       v
data/raw/<type>/<slug>/  ──── 原始字节（raw preservation，不变）
       |
       v
[NEW] source_router.py  ──── 逐类型路由 + 质量门控
       |
       ├── arxiv:     直读 agent_source_bundle.txt（过滤 .bib noise）
       ├── webpage:   raw.html → trafilatura/readability → markdown.md
       ├── github_repo: repo/ → repo2doc → material_bundle.txt
       ├── reddit:    [需重抓] → thread.json parse → text.txt
       ├── hacker_news: 直读 text.txt
       ├── pypi:      直读 pypi.json['info']['description']
       └── gist_raw:  直读 text.txt
       |
       v
reading_surface/<slug>.txt  ──── 统一阅读面（每源一个文件）
       |
       v
run_loop.py source_digest()  ──── 替换现有 source_text_path()
```

### 3.2 source_text_path() 路由修复

**当前代码** (`scripts/run_loop.py:1146-1171`)：

```python
def source_text_path(source: dict[str, Any]) -> Path | None:
    # 问题：text.txt 优先级太高，arxiv 误命中
    for key in [
        "agent_source_bundle.txt",
        "text.txt",          # <-- arxiv 的 text.txt 仅含摘要！
        "browser_text.txt",
        "README.remote",     # <-- 全部 403 错误
        "raw.txt",
    ]:
```

**修复后路由**（逐类型 dispatch）：

```python
def source_text_path(source: dict[str, Any]) -> Path | None:
    source_type = source.get("source_type", "webpage")
    local_dir = ROOT / source.get("local_dir", "")

    # 逐类型优先级链
    TYPE_PRIORITY = {
        "arxiv": [
            "agent_source_bundle.txt",
            # text.txt 永远不用于 arxiv（仅含摘要页 chrome）
        ],
        "github_repo": [
            "material_bundle.txt",
            "repo/README.md",
        ],
        "reddit": [
            "text.txt",
            "browser_text.txt",
        ],
        "webpage": [
            "text.txt",       # 未来升级为 markdown.md
            "raw.txt",
        ],
        "hacker_news": ["text.txt"],
        "pypi": ["text.txt"],
        "gist_raw": ["text.txt", "raw.txt"],
    }

    candidates = TYPE_PRIORITY.get(source_type, ["text.txt", "raw.txt"])
    for filename in candidates:
        path = local_dir / filename
        if path.exists() and path.stat().st_size > 50:  # 跳过空壳文件
            return path
    return None
```

### 3.3 repo2doc 阶段设计

**输入**：`data/raw/github_repo/<slug>/repo/`（已 clone 的仓库）

**输出**：`data/raw/github_repo/<slug>/material_bundle.txt`

**生成策略**（按文件类型拼接，优先级排序）：

```
1. README.md（项目定位 + 用法）
2. docs/ 目录下所有 .md（架构文档、ADR）
3. CLAUDE.md / CONTRIBUTING.md / ARCHITECTURE.md（设计约束）
4. 核心入口文件（main.py / index.ts / lib.rs 前 500 行）
5. 配置 schema（*.toml / *.yaml / settings.* 中的注释型配置）
6. 测试 fixtures 目录列表（不含内容，仅文件名 → 暗示边界条件）
```

**大小约束**：单个 bundle 上限 500KB。超出时按优先级截断。

**特殊处理**：
- `repo-microsoft-agent-governance-toolkit`（3871 文件）：拆为 3 个子 bundle（docs/, python-sdk/, examples/）
- `repo-stanford-ares`（1.8GB）：排除 checkpoint/ 和 data/ 目录

---

## 4. 具体实施步骤（按影响排序）

### Phase 1: 路由修复 + 立即可修的数据问题（1-2 天）

| # | 动作 | 影响 | 文件路径 | 具体改动 |
|---|------|------|---------|---------|
| 1.1 | 修复 `source_text_path()` 路由 | 消除 arxiv text.txt 误读 | `scripts/run_loop.py:1146-1171` | 替换为逐类型 dispatch（见 3.2） |
| 1.2 | 重建 arxiv-ragas bundle | 46MB→~34KB | `data/raw/arxiv/arxiv-ragas/` | 重新运行 `write_agent_source_bundle()` 加 `.bib` 过滤 |
| 1.3 | 修复 `write_agent_source_bundle()` | 防止未来 .bib 膨胀 | `scripts/fetch_sources.py:180-195` | 添加文件大小上限 (1MB) + 排除 `anthology*.bib` |
| 1.4 | 标记 3 个死源 | 避免空数据进入提取 | `data/raw/webpage/aicritique-*/metadata.json`, `obsidian-help-link-notes/metadata.json` | 添加 `"status": "dead", "exclude_from_pipeline": true` |

### Phase 2: repo2doc 批量生成（3-5 天，高影响）

| # | 动作 | 影响 | 优先级 |
|---|------|------|--------|
| 2.1 | 编写 `scripts/repo2doc.py` | 为 18 个 repo 生成 bundle | CRITICAL |
| 2.2 | 运行 repo2doc: microsoft-agent-governance-toolkit | +policy enforcement 知识（~20 张卡） | T1 |
| 2.3 | 运行 repo2doc: kytmanov-obsidian-local | +local-first pipeline 知识（~8 张卡） | T1 |
| 2.4 | 运行 repo2doc: ar9av-obsidian-wiki | +multi-agent skill 知识（~8 张卡） | T1 |
| 2.5 | 运行 repo2doc: ngmeyer-librarian-mcp | +MCP productionization（~5 张卡） | T1 |
| 2.6 | 运行 repo2doc: vectifyai-openkb | +vectorless retrieval（~5 张卡） | T1 |
| 2.7 | 运行 repo2doc: atomicstrata-llm-wiki-compiler | +TS 编译策略（~4 张卡） | T1 |
| 2.8 | 运行 repo2doc: 剩余 12 个 repo | 长尾知识 | T2-T3 |

**repo2doc.py 核心逻辑**：

```python
# scripts/repo2doc.py 伪代码
INCLUDE_PATTERNS = [
    "README.md", "CLAUDE.md", "CONTRIBUTING.md", "ARCHITECTURE.md",
    "docs/**/*.md", "doc/**/*.md",
    "*.toml", "*.yaml", "*.yml",  # 配置 schema
]
ENTRY_POINTS = ["main.py", "cli.py", "index.ts", "src/lib.rs", "app.py"]
MAX_BUNDLE_SIZE = 500_000  # 500KB

def build_bundle(repo_dir: Path) -> str:
    sections = []
    # 1. README
    # 2. docs/*.md (sorted by depth)
    # 3. architecture files
    # 4. entry points (前 500 行)
    # 5. config schemas (带注释)
    # 6. test fixture listing
    return "\n\n".join(sections)[:MAX_BUNDLE_SIZE]
```

### Phase 3: 重抓失败源（2-3 天）

| # | 动作 | 方法 | 源 |
|---|------|------|---|
| 3.1 | Reddit 全量重抓 | 使用 `old.reddit.com/<url>.json` endpoint + 自定义 User-Agent | 6 个 reddit-* 源 |
| 3.2 | obsidian-help-link-notes 重抓 | 直接 fetch Obsidian Publish API: `https://publish-01.obsidian.md/access/f786db9fac45774fa4f0d8112e232d67/Getting%20started/Link%20notes.md` | 1 源 |
| 3.3 | aicritique 替代获取 | 尝试 web.archive.org 快照或 Google Cache | 2 源 |
| 3.4 | langchain 增强提取 | 从 raw.html 内 `<script>` JSON payload 提取 Next.js hydration data | 1 源 |
| 3.5 | arxiv-knowledge-compounding PDF 提取 | `pymupdf` 或 `pdftotext` 生成 agent_source_bundle.txt | 1 源 |

**Reddit 重抓具体实现**：

```python
# 添加到 fetch_sources.py 的 reddit handler
def fetch_reddit_json(url: str) -> dict:
    """使用 old.reddit.com JSON API 绕过反爬"""
    json_url = url.rstrip("/") + ".json"
    headers = {
        "User-Agent": "llm-wiki-research:v0.1 (academic research)",
        "Accept": "application/json",
    }
    resp = requests.get(json_url, headers=headers, timeout=30)
    return resp.json()  # 返回完整评论树
```

### Phase 4: 网页提取质量升级（可选，长期）

| # | 动作 | 影响 |
|---|------|------|
| 4.1 | 集成 `trafilatura` 替代 TextExtractor | 保留文章结构（标题、列表、代码块） |
| 4.2 | 输出格式从 text.txt 升级为 markdown.md | 下游 reader 可利用结构 |
| 4.3 | 为代码重源保留 `<pre>/<code>` 块 | 恢复 581 个代码元素语义 |
| 4.4 | OWASP 源补充 PDF 下载 | 获取实际 Top-10 文档内容 |

---

## 5. `scripts/fetch_sources.py` 具体改动

### 5.1 agent_source_bundle 生成：过滤大文件

**位置**：`scripts/fetch_sources.py:180-195`

**改动**：

```python
def write_agent_source_bundle(source_root: Path, bundle_path: Path) -> tuple[str | None, int, list[str]]:
    READABLE_EXTS = {".tex", ".bib", ".bbl", ".sty", ".cls", ".md", ".txt", ".json", ".ltx"}
    # [NEW] 排除规则
    EXCLUDE_PATTERNS = {"anthology.bib", "anthology"}
    MAX_SINGLE_FILE = 1_000_000  # 单文件 1MB 上限
    NOISE_EXTS = {".sty", ".cls", ".bst"}  # 标记为低优先级

    parts = []
    files_included = []
    # ... 遍历时添加过滤：
    for f in sorted_files:
        if f.name in EXCLUDE_PATTERNS:
            continue
        if f.stat().st_size > MAX_SINGLE_FILE:
            continue  # 跳过异常大文件
        if f.suffix in NOISE_EXTS:
            continue  # 跳过排版样式文件
        # ... 正常拼接
```

### 5.2 Reddit fetcher 修复

**位置**：`scripts/fetch_sources.py`（reddit handler）

**改动**：增加 `old.reddit.com/.json` 路径作为首选，带学术 User-Agent。

---

## 6. 现有 295 张 KB 卡处理策略

### 6.1 分类评估

| 卡片来源 | 数量（估） | 质量 | 处理 |
|----------|-----------|------|------|
| 从 2 个 repo bundle 提取（graphrag + nvk-llm-wiki） | ~60 | 高（bundle 质量好） | **保留** |
| 从 arxiv bundle 正确提取 | ~160 | 高 | **保留** |
| 从 arxiv text.txt 误读提取 | ~42 (62 citations) | 低（仅摘要深度） | **重新提取** |
| 从 webpage text.txt 提取 | ~30 | 中等 | **保留，Phase 4 后增强** |
| 从 hacker_news/pypi/gist 提取 | ~3 | 高 | **保留** |

### 6.2 具体决策

**保留（不动）**：
- 所有从 agent_source_bundle.txt 正确提取的 arxiv 卡片（~160 张）
- 所有从 material_bundle.txt 提取的 repo 卡片（graphrag + nvk-llm-wiki，~60 张）
- 所有 webpage/HN/pypi/gist 来源卡片（~33 张）

**标记待重提取**：
- 来自 arxiv-graph-poisoning (15 citations)、arxiv-lightmem (11)、arxiv-wicer (16) 的卡片
- 识别方法：检查卡片 `source` 字段是否指向上述 3 个 source_id，且 `footnotes` 中引用路径含 `text.txt`
- 执行：在路由修复（Phase 1.1）后，从 agent_source_bundle.txt 重新提取这些卡片
- 旧卡片移至 `kb/archive/shallow_extract/` 保留溯源

**新增（Phase 2 后）**：
- 18 个 repo 生成 bundle 后，预计新增 60-80 张卡片
- 6 个 Reddit 重抓后，预计新增 6-10 张卡片
- arxiv-knowledge-compounding PDF 提取后，预计新增 3-5 张卡片

### 6.3 重提取流程

```
1. Phase 1.1 路由修复 → source_text_path() 不再返回 arxiv text.txt
2. 识别受影响卡片：
   grep -l "arxiv-graph-poisoning\|arxiv-lightmem\|arxiv-wicer" kb/cards/*.md
3. 移至归档：
   mv kb/cards/<affected>.md kb/archive/shallow_extract/
4. 重新运行 reader-worker 对这 3 个源
5. 新卡片经 governance pass（dedup + cross-link）后入库
```

---

## 7. 验收标准

| 阶段 | 完成标志 |
|------|---------|
| Phase 1 | `source_text_path()` 对所有 17 个 arxiv 源返回 bundle 路径（非 text.txt） |
| Phase 1 | arxiv-ragas bundle < 500KB |
| Phase 2 | 20/20 github_repo 均有 material_bundle.txt 且 > 10KB |
| Phase 3 | 6/6 reddit 源的 thread.json 为有效 JSON 且 > 1KB |
| Phase 3 | arxiv-knowledge-compounding 有 agent_source_bundle.txt |
| Phase 4 | 27 个 webpage 中 24+ 个的 text.txt > 5KB（排除 3 个 dead） |
| 整体 | KB 卡片数从 295 增至 370+（repo bundle 带来增量） |

---

## 8. 风险与约束

| 风险 | 影响 | 缓解 |
|------|------|------|
| Reddit API 也 block 学术 UA | Phase 3.1 失败 | 备选：PRAW OAuth2 或 Pushshift 存档 |
| repo2doc 对大 repo 生成低质量 bundle | 卡片提取噪声 | 设 500KB 上限 + 人工抽检 top-3 |
| 重提取后卡片 ID 变化导致 cross-link 断裂 | 链接完整性回退 | 重提取后立即运行 governance cross-link pass |
| trafilatura 依赖引入 (Phase 4) | 环境复杂度增加 | 可选：纯 Python readability port (readabilipy) |

---

## 9. 文件索引

| 需修改的文件 | 修改内容 |
|-------------|---------|
| `scripts/run_loop.py:1146-1171` | source_text_path() 逐类型路由 |
| `scripts/fetch_sources.py:180-195` | write_agent_source_bundle() .bib 过滤 |
| `scripts/fetch_sources.py` (reddit handler) | old.reddit.com JSON API 路径 |
| `scripts/repo2doc.py` [NEW] | repo→material_bundle 生成器 |
| `scripts/source_router.py` [NEW, optional] | 统一阅读面路由 + 质量门控 |
| `data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt` | 重建（排除 anthology.bib） |
| `data/raw/arxiv/arxiv-knowledge-compounding/` | 新增 PDF→text 提取 |
| `data/raw/github_repo/*/material_bundle.txt` x18 | 新增 repo2doc 产物 |
| `data/raw/reddit/*/` x6 | 重抓全部内容 |
| `data/raw/webpage/aicritique-*/metadata.json` | 标记 dead |
| `data/raw/webpage/obsidian-help-link-notes/metadata.json` | 标记 dead |
