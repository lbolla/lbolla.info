#!/usr/bin/env python3
import re
import sys
from pathlib import Path

def convert_wikilinks_in_file(file_path: Path):
    if not file_path.suffix == ".md":
        return

    content = file_path.read_text(encoding="utf-8")

    # Regex matches [[Some words]] or [[Some words|Custom Label]]
    pattern = r"\[\[([^\|\]]+)(?:\|([^\]]+))?\]\]"

    def replace_wikilink(match):
        raw_target = match.group(1).strip()
        custom_label = match.group(2)

        # Use custom label if provided (e.g. [[Target|Label]]);
        # otherwise title-case the target name for the display text.
        if custom_label:
            display_text = custom_label.strip()
        else:
            display_text = raw_target.title()

        # Build the Hugo relref string pointing to "blog/<target>.md"
        return f'[{display_text}]({{{{< relref "blog/{raw_target}.md" >}}}})'

    new_content = re.sub(pattern, replace_wikilink, content)

    if new_content != content:
        file_path.write_text(new_content, encoding="utf-8")
        print(f"Updated: {file_path.name}")

def process_target(target_path: str):
    target = Path(target_path)

    if target.is_file():
        convert_wikilinks_in_file(target)
    elif target.is_dir():
        for md_file in target.glob("**/*.md"):
            convert_wikilinks_in_file(md_file)
    else:
        print(f"Error: '{target_path}' is not a valid file or directory.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert_links.py <file_or_directory_path>")
        sys.exit(1)

    process_target(sys.argv[1])
