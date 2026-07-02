#!/usr/bin/env python3
"""Validate the required structure of generated paper-reading Markdown notes."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


REQUIRED_NOTE_HEADINGS = [
    "## 1. 文献信息",
    "## 2. 背景与任务",
    "## 3. 方法梳理与核心推导",
    "## 4. 创新点",
    "## 5. 实验设计",
    "## 6. 存在的问题与局限",
    "## 7. 阅读结论",
    "## 8. 证据与完整性说明",
]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, help="Review output directory or a single note")
    args = parser.parse_args()
    target = args.output.expanduser().resolve()

    if target.is_file():
        notes = [target]
    else:
        manifest_path = target / "manifest.json"
        if manifest_path.exists():
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            notes = [target / item["note"] for item in manifest.get("papers", [])]
        else:
            notes = sorted(path for path in target.glob("*.md") if path.name.casefold() != "index.md")

    if not notes:
        print("ERROR: no paper note files found")
        return 2

    errors = 0
    for note in notes:
        if not note.exists():
            print(f"FAIL {note}: file is missing")
            errors += 1
            continue
        text = note.read_text(encoding="utf-8")
        missing = [heading for heading in REQUIRED_NOTE_HEADINGS if heading not in text]
        unresolved = text.count("{{")
        if missing or unresolved:
            print(f"FAIL {note}")
            for heading in missing:
                print(f"  missing heading: {heading}")
            if unresolved:
                print(f"  unresolved template markers: {unresolved}")
            errors += 1
        else:
            print(f"OK   {note}")

    print(f"Checked {len(notes)} note(s); failures: {errors}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

