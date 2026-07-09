#!/usr/bin/env python3
"""
yaml_lint.py — 卡片 frontmatter 格式验证。

用法:
    python yaml_lint.py <card_file.md>
    python yaml_lint.py --dir <cards_directory>

检查项:
1. related 字段无双格式（行内 [] 与缩进 - 互斥）
2. 所有 frontmatter key 可被标准 YAML 解析器正确读取
3. slug 引用在 index 中存在（无悬空引用）——需传 --index 参数
"""

import sys
import re
import yaml
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]


def extract_frontmatter(text: str) -> tuple[str | None, int]:
    """提取 --- 包围的 frontmatter 原文。返回 (raw_yaml, end_line)。"""
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return None, 0
    end = -1
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end == -1:
        return None, 0
    return "\n".join(lines[1:end]), end


def check_related_dual_format(raw_yaml: str) -> list[str]:
    """检测 related 字段是否同时存在行内 [] 和缩进 - 两种格式。"""
    errors = []
    lines = raw_yaml.split("\n")
    in_related = False
    has_inline = False
    has_block_items = False
    related_line = -1

    for i, line in enumerate(lines):
        if line.startswith("related:"):
            in_related = True
            related_line = i
            rest = line[len("related:"):].strip()
            if rest.startswith("["):
                has_inline = True
        elif in_related:
            if line.startswith("  - ") or line.startswith("- "):
                has_block_items = True
            elif line and not line.startswith(" "):
                in_related = False

    if has_inline and has_block_items:
        errors.append(
            f"related 字段双格式冲突（行内 [] + 缩进 -）at line {related_line + 1}"
        )
    return errors


def check_yaml_parseable(raw_yaml: str) -> list[str]:
    """检查 frontmatter 是否可被标准 YAML 解析器正确读取。"""
    errors = []
    try:
        data = yaml.safe_load(raw_yaml)
        if not isinstance(data, dict):
            errors.append("frontmatter 解析结果不是字典")
    except yaml.YAMLError as e:
        errors.append(f"YAML 解析失败: {e}")
    return errors


def check_slug_references(raw_yaml: str, valid_slugs: set[str]) -> list[str]:
    """检查 related 字段中的 slug 引用是否存在于 index 中。"""
    errors = []
    if not valid_slugs:
        return errors
    try:
        data = yaml.safe_load(raw_yaml)
    except yaml.YAMLError:
        return errors

    if not isinstance(data, dict):
        return errors

    related = data.get("related", [])
    if isinstance(related, list):
        for slug in related:
            if isinstance(slug, str) and slug not in valid_slugs:
                errors.append(f"悬空引用: related 包含不存在的 slug '{slug}'")
    return errors


def lint_card(filepath: Path, valid_slugs: set[str] | None = None) -> list[str]:
    """对单张卡片执行全部检查。返回错误列表。"""
    text = filepath.read_text(encoding="utf-8")
    raw_yaml, end_line = extract_frontmatter(text)
    if raw_yaml is None:
        return [f"{filepath.name}: 无 frontmatter"]

    errors = []
    errors.extend(check_related_dual_format(raw_yaml))
    errors.extend(check_yaml_parseable(raw_yaml))
    if valid_slugs is not None:
        errors.extend(check_slug_references(raw_yaml, valid_slugs))

    return [f"{filepath.name}: {e}" for e in errors]


def load_index_slugs(index_path: Path) -> set[str]:
    """从 cards.md index 加载有效 slug 集合。"""
    slugs = set()
    if not index_path.exists():
        return slugs
    for line in index_path.read_text(encoding="utf-8").split("\n"):
        line = line.strip()
        if line.startswith("- ") or line.startswith("* "):
            slug_match = re.match(r"[-*]\s+\[?([a-z0-9-]+)", line)
            if slug_match:
                slugs.add(slug_match.group(1))
        elif line and not line.startswith("#") and not line.startswith(">"):
            parts = line.split("|")
            for part in parts:
                slug_match = re.search(r"([a-z][a-z0-9-]+[a-z0-9])", part.strip())
                if slug_match:
                    slugs.add(slug_match.group(1))
    return slugs


def main():
    import argparse
    parser = argparse.ArgumentParser(description="YAML lint gate for card frontmatter")
    parser.add_argument("file", nargs="?", help="Single card .md file to lint")
    parser.add_argument("--dir", help="Directory of card .md files to lint")
    parser.add_argument("--index", help="Path to cards.md index for slug validation")
    args = parser.parse_args()

    valid_slugs = None
    if args.index:
        valid_slugs = load_index_slugs(Path(args.index))

    files = []
    if args.dir:
        d = Path(args.dir)
        files = sorted(d.glob("*.md"))
    elif args.file:
        files = [Path(args.file)]
    else:
        parser.print_help()
        sys.exit(1)

    all_errors = []
    for f in files:
        errors = lint_card(f, valid_slugs)
        all_errors.extend(errors)

    if all_errors:
        print(f"YAML Lint: {len(all_errors)} error(s) found in {len(files)} file(s)")
        for e in all_errors:
            print(f"  ✗ {e}")
        sys.exit(1)
    else:
        print(f"YAML Lint: {len(files)} file(s) OK")
        sys.exit(0)


if __name__ == "__main__":
    main()
