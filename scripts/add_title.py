#!/usr/bin/env python3
import sys
from pathlib import Path

def add_title_to_md(file_path: Path):
    if not file_path.suffix == ".md":
        return

    # Extract file name without extension (e.g., "my-post.md" -> "my-post")
    title_text = file_path.stem
    title_line = f"title: \"{title_text}\"\n"

    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Insert at index 1 (the second line of the file)
    lines.insert(1, title_line)

    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(lines)
    print(f"Updated: {file_path.name}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python add_title.py <file_or_directory>")
        sys.exit(1)

    target = Path(sys.argv[1])
    if target.is_file():
        add_title_to_md(target)
    elif target.is_dir():
        for md_file in target.glob("*.md"):
            add_title_to_md(md_file)
    else:
        print(f"Error: {target} is not a valid file or directory.")