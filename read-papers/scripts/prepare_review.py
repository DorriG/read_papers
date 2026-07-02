#!/usr/bin/env python3
"""Inventory local paper files and prepare a deterministic review workspace."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from pathlib import Path


SUPPORTED_EXTENSIONS = {".pdf", ".md", ".txt", ".html", ".htm", ".docx", ".tex"}


def slugify(value: str) -> str:
    value = value.strip().lower().replace("_", "-")
    value = re.sub(r"[^\w\-\u4e00-\u9fff]+", "-", value, flags=re.UNICODE)
    value = re.sub(r"-+", "-", value).strip("-")
    return value[:80] or "paper"


def is_within(path: Path, directory: Path) -> bool:
    try:
        path.relative_to(directory)
        return True
    except ValueError:
        return False


def discover(inputs: list[Path], recursive: bool, excluded_directory: Path) -> list[Path]:
    found: dict[str, Path] = {}
    for item in inputs:
        path = item.expanduser().resolve()
        if path.is_file() and not is_within(path, excluded_directory) and path.suffix.lower() in SUPPORTED_EXTENSIONS:
            found[str(path).casefold()] = path
        elif path.is_dir():
            iterator = path.rglob("*") if recursive else path.glob("*")
            for candidate in iterator:
                if candidate.is_file() and candidate.suffix.lower() in SUPPORTED_EXTENSIONS:
                    resolved = candidate.resolve()
                    if not is_within(resolved, excluded_directory):
                        found[str(resolved).casefold()] = resolved
    return sorted(found.values(), key=lambda p: str(p).casefold())


def unique_slug(path: Path, used: set[str]) -> str:
    base = slugify(path.stem)
    if base not in used:
        used.add(base)
        return base
    suffix = hashlib.sha1(str(path).encode("utf-8")).hexdigest()[:8]
    candidate = f"{base}-{suffix}"
    used.add(candidate)
    return candidate


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("inputs", nargs="+", type=Path, help="Paper files or directories")
    parser.add_argument("--output", type=Path, default=Path("paper-notes"))
    parser.add_argument("--recursive", action="store_true", help="Search directories recursively")
    parser.add_argument("--force", action="store_true", help="Replace an existing generated manifest/index")
    args = parser.parse_args()

    output = args.output.expanduser().resolve()
    papers = discover(args.inputs, args.recursive, output)
    if not papers:
        parser.error("no supported paper files found")

    output.mkdir(parents=True, exist_ok=True)
    manifest_path = output / "manifest.json"
    index_path = output / "index.md"
    if not args.force and (manifest_path.exists() or index_path.exists()):
        parser.error("output already contains manifest.json or index.md; use --force to replace generated files")

    skill_root = Path(__file__).resolve().parents[1]
    index_template = skill_root / "assets" / "batch-index-template.md"
    note_template = skill_root / "assets" / "single-paper-template.md"
    shutil.copyfile(index_template, index_path)

    used: set[str] = set()
    records = []
    for position, paper in enumerate(papers, start=1):
        slug = unique_slug(paper, used)
        note_name = f"{slug}.md"
        note_path = output / note_name
        if not note_path.exists():
            shutil.copyfile(note_template, note_path)
        records.append(
            {
                "position": position,
                "source": str(paper),
                "note": note_name,
                "status": "pending",
            }
        )

    manifest = {
        "schema_version": 1,
        "paper_count": len(records),
        "output_directory": str(output),
        "papers": records,
    }
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Prepared {len(records)} paper(s) in {output}")
    print(f"Manifest: {manifest_path}")
    print(f"Batch index: {index_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
