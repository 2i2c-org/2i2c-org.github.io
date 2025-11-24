#!/usr/bin/env python3
"""
Add 'slug' field to blog post front matter based on folder name.
This allows permalinks to use the folder name instead of the title.
"""
import re
from pathlib import Path

def add_slug_to_post(post_path):
    """Add slug field to front matter if not already present."""
    # Get the parent folder name (e.g., "repo2docker-docs")
    folder_name = post_path.parent.name

    # Skip special folders
    if folder_name in ["blog", "drafts", "idea"]:
        return False

    # Read the file
    content = post_path.read_text()

    # Check if slug already exists in front matter
    if re.search(r'^slug:', content, re.MULTILINE):
        print(f"  ⏭️  {post_path.parent}: slug already exists")
        return False

    # Find the front matter block (between --- markers)
    # Handle files with and without content after front matter, and optional trailing spaces
    match = re.match(r'^---\n(.*?\n)---\s*(?:\n|$)', content, re.DOTALL)
    if not match:
        print(f"  ⚠️  {post_path.parent}: no front matter found")
        return False

    front_matter = match.group(1)

    # Add slug field after the title line (or at the end if no title)
    title_match = re.search(r'^title:.*\n', front_matter, re.MULTILINE)
    if title_match:
        # Insert after title
        new_front_matter = front_matter[:title_match.end()] + f'slug: "{folder_name}"\n' + front_matter[title_match.end():]
    else:
        # Add at the end of front matter
        new_front_matter = front_matter.rstrip('\n') + f'\nslug: "{folder_name}"\n'

    # Replace the front matter in the content
    # Preserve any content after front matter (or just end with --- if none)
    remaining_content = content[match.end():]
    if remaining_content:
        new_content = f'---\n{new_front_matter}---\n' + remaining_content
    else:
        new_content = f'---\n{new_front_matter}---\n'

    # Write back
    post_path.write_text(new_content)
    print(f"  ✅ {post_path.parent}: added slug='{folder_name}'")
    return True

def main():
    blog_dir = Path("content/blog")

    # Find all index.md files in blog subdirectories
    index_files = sorted(blog_dir.glob("*/*/index.md"))

    print(f"Found {len(index_files)} blog posts\n")

    updated_count = 0
    for index_file in index_files:
        if add_slug_to_post(index_file):
            updated_count += 1

    print(f"\n✨ Updated {updated_count} posts")

    # Exit with error code if any files were modified
    if updated_count > 0:
        print(f"\n❌ ERROR: {updated_count} blog posts were missing slugs!")
        print("The slugs have been added automatically.")
        print("Please review and commit the changes.")
        return 1
    else:
        print("\n✅ All blog posts have slugs")
        return 0

if __name__ == "__main__":
    exit(main())
