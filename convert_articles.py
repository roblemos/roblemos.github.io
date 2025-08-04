import os
import re
import yaml
from pathlib import Path
from textwrap import indent

SOURCE_DIR = "content/articles"
OUTPUT_DIR = "content/converted"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def prompt_user_approval(metadata, path):
    print(f"\n📄 File: {path}")
    print("Parsed Metadata:")
    for key, value in metadata.items():
        print(f"  {key}: {value}")
    confirm = input("\nConvert this file? [y/N] ").strip().lower()
    return confirm == 'y'

def convert_file(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)", content, re.DOTALL)
    if not match:
        print(f"❌ Skipping {path}: no valid YAML frontmatter found.")
        return

    yaml_text, body = match.groups()
    try:
        metadata = yaml.safe_load(yaml_text)
    except yaml.YAMLError as e:
        print(f"⚠️ YAML parsing error in {path}: {e}")
        return

    if not metadata or not isinstance(metadata, dict):
        print(f"❌ Skipping {path}: frontmatter is not a valid dict.")
        return

    required = ['title', 'date']
    for key in required:
        if key not in metadata:
            print(f"❌ Skipping {path}: missing required field '{key}'")
            return

    if not prompt_user_approval(metadata, path):
        print("⏭️ Skipped.")
        return

    pelican_meta = [
        f"Title: {metadata['title']}",
        f"Date: {metadata['date']}"
    ]

    # Handle category
    if 'category' in metadata:
        pelican_meta.append(f"Category: {metadata['category']}")
    elif 'categories' in metadata:
        cat = metadata['categories']
        if isinstance(cat, list):
            pelican_meta.append(f"Category: {cat[0]}")
        else:
            pelican_meta.append(f"Category: {cat}")

    # Handle tags
    if 'tags' in metadata:
        tags = metadata['tags']
        if isinstance(tags, list):
            pelican_meta.append("Tags: " + ", ".join(tags))
        else:
            pelican_meta.append(f"Tags: {tags}")

    pelican_header = "\n".join(pelican_meta) + "\n\n"

    output_path = Path(OUTPUT_DIR) / Path(path).name
    with open(output_path, "w", encoding="utf-8") as out:
        out.write(pelican_header + body.strip() + "\n")

    print(f"✅ Converted: {path} → {output_path}")

def convert_all():
    for root, _, files in os.walk(SOURCE_DIR):
        for file in files:
            if file.endswith(".md"):
                convert_file(os.path.join(root, file))

if __name__ == "__main__":
    convert_all()
