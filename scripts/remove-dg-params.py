#!/usr/bin/env python3
import sys
import re
from pathlib import Path
import yaml

def clean_frontmatter_in_file(file_path: Path):
    if file_path.suffix != ".md":
        return

    content = file_path.read_text(encoding="utf-8")

    # Regex to split front matter (between opening and closing ---) from the body
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", content, re.DOTALL)
    if not match:
        return

    raw_yaml, body = match.groups()

    try:
        data = yaml.safe_load(raw_yaml)
    except yaml.YAMLError as e:
        print(f"Skipping {file_path.name}: Invalid YAML front matter ({e})")
        return

    if not isinstance(data, dict):
        return

    # Identify and remove keys starting with 'dg-'
    keys_to_remove = [key for key in data.keys() if str(key).startswith("dg-")]
    if not keys_to_remove:
        return

    for key in keys_to_remove:
        del data[key]

    # Re-serialize front matter back to YAML
    new_yaml = yaml.dump(
        data,
        default_flow_style=False,
        allow_unicode=True,
        sort_keys=False
    ).strip()

    # Reconstruct document
    new_content = f"---\n{new_yaml}\n---\n{body}"

    file_path.write_text(new_content, encoding="utf-8")
    print(f"Cleaned {file_path.name}: Removed {keys_to_remove}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python remove_dg_params.py <file_or_directory_path>")
        sys.exit(1)

    target_path = Path(sys.argv[1])

    if target_path.is_file():
        clean_frontmatter_in_file(target_path)
    elif target_path.is_dir():
        for md_file in target_path.glob("**/*.md"):
            clean_frontmatter_in_file(md_file)
    else:
        print(f"Error: '{target_path}' is not a valid file or directory.")

if __name__ == "__main__":
    main()
