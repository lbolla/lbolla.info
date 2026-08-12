#!/usr/bin/env python3
import sys
import re
from pathlib import Path

def add_tag_standalone(file_path: Path, tag_to_add: str):
    if not file_path.suffix == ".md":
        return

    content = file_path.read_text(encoding="utf-8")

    # Split by front matter delimiters
    parts = re.split(r"^---\s*$", content, flags=re.MULTILINE)
    if len(parts) < 3:
        print(f"No valid front matter found in {file_path.name}")
        return

    front_matter = parts[1]
    body = "---".join(parts[2:])

    # Check if 'tags:' already exists
    tags_match = re.search(r"^tags:\s*(.*)$", front_matter, re.MULTILINE)

    if tags_match:
        raw_val = tags_match.group(1).strip()
        # Handle inline array syntax like tags: ["a", "b"]
        if raw_val.startswith("[") and raw_val.endswith("]"):
            items = [item.strip(' "\'') for item in raw_val[1:-1].split(",") if item.strip()]
            if tag_to_add not in items:
                items.append(tag_to_add)
            new_tags_line = f"tags: {items}"
        # Handle string or list
        else:
            new_tags_line = f"tags:\n  - {tag_to_add}" if not raw_val else f"tags:\n  {raw_val}\n  - {tag_to_add}"

        front_matter = re.sub(r"^tags:\s*.*$", new_tags_line, front_matter, flags=re.MULTILINE)
    else:
        # Append tags field if not present
        front_matter += f"\ntags:\n  - {tag_to_add}\n"

    new_content = f"---{front_matter}---{body}"
    file_path.write_text(new_content, encoding="utf-8")
    print(f"Updated {file_path.name}")

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        add_tag_standalone(Path(sys.argv[1]), sys.argv[2])
