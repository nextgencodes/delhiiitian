import os
import re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by '---'
    parts = content.split('---')
    if len(parts) < 3:
        # Not a valid front matter, skip
        return

    # parts[0] is empty (since starts with ---)
    front_matter = parts[1]
    rest = '---'.join(parts[2:])

    # Find the tags line
    lines = front_matter.split('\n')
    tags_line_index = -1
    for i, line in enumerate(lines):
        if line.strip().startswith('tags:'):
            tags_line_index = i
            break

    if tags_line_index == -1:
        # No tags line, skip
        return

    tags_line = lines[tags_line_index]
    # Extract the part between [ and ]
    match = re.search(r'\[(.*?)\]', tags_line)
    if not match:
        # No brackets, skip
        return

    tags_str = match.group(1)
    # Split by commas and clean
    raw_tags = [tag.strip().strip('\"\'') for tag in tags_str.split(',')]
    # Remove empty strings
    raw_tags = [tag for tag in raw_tags if tag]
    # Remove duplicates while preserving order
    seen = set()
    unique_tags = []
    for tag in raw_tags:
        if tag not in seen:
            seen.add(tag)
            unique_tags.append(tag)
    # Limit to 5
    limited_tags = unique_tags[:5]

    # Build new tags line
    new_tags_str = ', '.join(limited_tags)
    new_tags_line = f'tags: [{new_tags_str}]'

    # Replace the line
    lines[tags_line_index] = new_tags_line
    new_front_matter = '\n'.join(lines)

    # Rebuild content
    new_content = f'---{new_front_matter}---{rest}'

    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

def main():
    posts_dir = '/mnt/d/Projects/Mywebpage/delhiiitian/_posts'
    for filename in os.listdir(posts_dir):
        if filename.endswith('.md'):
            filepath = os.path.join(posts_dir, filename)
            process_file(filepath)
            print(f'Processed: {filename}')

if __name__ == '__main__':
    main()