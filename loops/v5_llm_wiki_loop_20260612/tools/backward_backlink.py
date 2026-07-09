#!/usr/bin/env python3
"""
backward_backlink.py — 双向对称性修复：强制 related 反向链接。

对每张卡 A 的 related 列表中的每个 target B:
  - 如果 A 不在 B 的 related 中 → append A 到 B 的 related

使用 YAML parser 读写 frontmatter，body 不变。
"""

import sys
import yaml
from pathlib import Path


CARDS_DIR = Path(__file__).resolve().parents[1] / "outputs" / "llm_wiki" / "kb" / "cards"


def extract_frontmatter_and_body(text: str) -> tuple[dict | None, str]:
    """解析 --- 分隔的 frontmatter 和 body。"""
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return None, text
    end = -1
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end == -1:
        return None, text
    raw_yaml = "\n".join(lines[1:end])
    body = "\n".join(lines[end + 1:])
    try:
        data = yaml.safe_load(raw_yaml)
        if not isinstance(data, dict):
            return None, text
        return data, body
    except yaml.YAMLError:
        return None, text


def write_card(filepath: Path, frontmatter: dict, body: str):
    """将 frontmatter + body 写回卡片文件。"""
    yaml_str = yaml.dump(
        frontmatter,
        default_flow_style=False,
        allow_unicode=True,
        sort_keys=False,
        width=200,
    )
    # 去掉 yaml.dump 末尾多余换行
    yaml_str = yaml_str.rstrip("\n")
    content = f"---\n{yaml_str}\n---{body}"
    filepath.write_text(content, encoding="utf-8")


def main():
    cards_dir = CARDS_DIR
    if not cards_dir.exists():
        print(f"ERROR: cards directory not found: {cards_dir}")
        sys.exit(1)

    # Phase 1: 读取所有卡片的 related 数据
    card_files = sorted(cards_dir.glob("*.md"))
    print(f"读取 {len(card_files)} 张卡片...")

    # slug -> { 'related': list, 'file': Path, 'frontmatter': dict, 'body': str }
    cards = {}
    parse_errors = 0

    for f in card_files:
        text = f.read_text(encoding="utf-8")
        fm, body = extract_frontmatter_and_body(text)
        if fm is None:
            parse_errors += 1
            continue
        slug = fm.get("id", f.stem)
        related = fm.get("related", [])
        if not isinstance(related, list):
            related = []
        cards[slug] = {
            "related": related,
            "file": f,
            "frontmatter": fm,
            "body": body,
        }

    if parse_errors:
        print(f"  警告: {parse_errors} 张卡片解析失败，已跳过")

    # Phase 2: 检测单向链接并修复
    fixes = 0
    modified_slugs = set()

    for slug_a, data_a in cards.items():
        for target_b in data_a["related"]:
            if not isinstance(target_b, str):
                continue
            if target_b not in cards:
                # target 不存在（悬空引用），跳过
                continue
            data_b = cards[target_b]
            if slug_a not in data_b["related"]:
                data_b["related"].append(slug_a)
                modified_slugs.add(target_b)
                fixes += 1

    # Phase 3: 写回修改过的卡片
    for slug in modified_slugs:
        data = cards[slug]
        data["frontmatter"]["related"] = data["related"]
        write_card(data["file"], data["frontmatter"], data["body"])

    print(f"\n=== backward_backlink 完成 ===")
    print(f"总卡片: {len(cards)}")
    print(f"修复单向链接: {fixes} 条（向 {len(modified_slugs)} 张卡片添加了反向链接）")
    if parse_errors:
        print(f"解析失败跳过: {parse_errors}")


if __name__ == "__main__":
    main()
