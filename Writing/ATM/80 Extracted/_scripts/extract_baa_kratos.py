#!/usr/bin/env python3
"""Extract prompts P199-P284 from BAA-Kratos source file."""

import re
import os
from datetime import datetime

# Line numbers for P199-P284 (from grep output)
PROMPT_LINES = {
    199: 15776, 200: 15822, 201: 15930, 202: 16015, 203: 16078,
    204: 16145, 205: 16206, 206: 16258, 207: 16328, 208: 16380,
    209: 16432, 210: 16489, 211: 16552, 212: 16630, 213: 16713,
    214: 16775, 215: 16841, 216: 16892, 217: 16946, 218: 17006,
    219: 17074, 220: 17168, 221: 17246, 222: 17319, 223: 17418,
    224: 17507, 225: 17555, 226: 17573, 227: 17654, 228: 17718,
    229: 17787, 230: 17843, 231: 17916, 232: 17971, 233: 18012,
    234: 18061, 235: 18082, 236: 18146, 237: 18211, 238: 18250,
    239: 18326, 240: 18398, 241: 18445, 242: 18508, 243: 18558,
    244: 18648, 245: 18751, 246: 18828, 247: 18901, 248: 18977,
    249: 19057, 250: 19136, 251: 19206, 252: 19317, 253: 19375,
    254: 19462, 255: 19530, 256: 19584, 257: 19631, 258: 19694,
    259: 19762, 260: 19861, 261: 19948, 262: 20021, 263: 20071,
    264: 20171, 265: 20224, 266: 20282, 267: 20332, 268: 20382,
    269: 20421, 270: 20495, 271: 20548, 272: 20599, 273: 20663,
    274: 20713, 275: 20774, 276: 20822, 277: 20891, 278: 20943,
    279: 20973, 280: 21013, 281: 21052, 282: 21087, 283: 21121,
    284: 21317,
}

# End of file
END_OF_FILE = 21462

SOURCE_FILE = r"C:/Users/Xavier/Desktop/Personal/Vaults/X-Writing/Writing/Archive/Gemini AI Exports/Formatted/Formatted_With_Thoughts - Branch of AA - The Kratos of Kings.md"
OUTPUT_DIR = r"C:/Users/Xavier/Desktop/Personal/Vaults/X-Writing/Writing/ATM/80 Extracted/BAA-Kratos"

def slugify(text):
    """Create a URL-friendly slug from text."""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-')[:50]

def derive_title(user_content, model_content):
    """Derive a topic title from user content or model headers."""
    # First try to find a ### header in the model content
    header_match = re.search(r'^###\s*\**(.+?)\**\s*$', model_content, re.MULTILINE)
    if header_match:
        title = header_match.group(1).strip()
        title = re.sub(r'[*_#>`]', '', title).strip()
        if title and len(title) > 5:
            if len(title) > 60:
                title = title[:57] + "..."
            return title

    # Fall back to first meaningful line of user content
    lines = [l.strip() for l in user_content.split('\n') if l.strip() and not l.startswith('---')]
    if not lines:
        return "Untitled"

    first_line = lines[0]
    # Clean up markdown
    first_line = re.sub(r'[*_#>`]', '', first_line)
    first_line = first_line.strip()

    # Truncate if too long
    if len(first_line) > 60:
        first_line = first_line[:57] + "..."

    return first_line if first_line else "Untitled"

def detect_category(content):
    """Detect category based on content keywords."""
    content_lower = content.lower()

    if any(kw in content_lower for kw in ['accent', 'language', 'voice', 'speech', 'english', 'japanese']):
        return "Worldbuilding"
    if any(kw in content_lower for kw in ['maria', 'mothra', 'relationship', 'love', 'attraction', 'heart']):
        return "Character Development"
    if any(kw in content_lower for kw in ['atomic', 'power', 'ability', 'kratos', 'arsenal', 'edict', 'injection', 'fortification', 'gravity', 'tempest', 'ego', 'constructs']):
        return "Mechanics"
    if any(kw in content_lower for kw in ['battle', 'fight', 'invasion', 'event', 'arc', 'story']):
        return "Plot"
    if any(kw in content_lower for kw in ['ghidorah', 'ichi', 'arthur', 'scylla', 'battra', 'profile']):
        return "Character Development"

    return "Worldbuilding"

def extract_entities(content):
    """Extract main entities mentioned in content."""
    entities = []
    entity_map = {
        r'\bGodric\b': 'Godric',
        r'\bGodzilla\b': 'Godzilla',
        r'\bMaria\b': 'Maria',
        r'\bMothra\b': 'Mothra',
        r'\bBattra\b': 'Battra',
        r'\bRodan\b': 'Rodan',
        r'\bAnguirus\b': 'Anguirus',
        r'\bKong\b': 'Kong',
        r'\bDagon\b': 'Dagon',
        r'\bMonarch\b': 'Monarch',
        r'\bGhidorah\b': 'Ghidorah',
        r'\bIchi\b': 'Ichi',
        r'\bArthur\b': 'Arthur',
        r'\bScylla\b': 'Scylla',
        r'\bExif\b': 'Exif',
    }

    for pattern, entity in entity_map.items():
        if re.search(pattern, content, re.IGNORECASE):
            if entity not in entities:
                entities.append(entity)

    return entities[:5]  # Max 5 entities

def strip_thoughts(model_content):
    """Remove blockquote thoughts from model response."""
    lines = model_content.split('\n')
    result = []
    in_thought_block = False

    for line in lines:
        # Check for thought process markers
        if "### Model's Thought Process" in line or "Model's Thought Process" in line:
            in_thought_block = True
            continue
        if line.strip().startswith('> **') and ('Thought' in line or 'thought' in line):
            in_thought_block = True
            continue
        # Also detect blockquote lines that start a thought
        if line.strip().startswith('> **') and any(kw in line for kw in ['Defining', 'Analyzing', 'Exploring', 'Focusing', 'Developing', 'Integrating', 'Synthesizing', 'Considering', 'Deconstructing', 'Simulating', 'Dissecting']):
            in_thought_block = True
            continue
        if line.strip().startswith('> '):
            # Skip all blockquote lines
            continue
        if in_thought_block:
            if line.strip() == '---':
                in_thought_block = False
                continue
            elif line.strip() == '':
                continue
            elif line.strip() and not line.strip().startswith('>'):
                in_thought_block = False

        result.append(line)

    # Clean up multiple blank lines
    cleaned = '\n'.join(result)
    cleaned = re.sub(r'\n{3,}', '\n\n', cleaned)
    return cleaned.strip()

def strip_thought_section(content):
    """Remove Model's Thought Process sections entirely."""
    content = re.sub(r"---\s*\n+### Model's Thought Process.*?---\s*\n+(?=## Model)", '\n---\n\n', content, flags=re.DOTALL)
    content = re.sub(r"### Model's Thought Process.*?---\s*\n+(?=## Model)", '\n', content, flags=re.DOTALL)
    return content

def extract_prompt(lines, start_line, end_line, prompt_num):
    """Extract a single prompt and its response."""
    # Get the content between start and end (1-indexed in file, 0-indexed in list)
    content = '\n'.join(lines[start_line-1:end_line-1])

    # First, strip thought process sections from the raw content
    content = strip_thought_section(content)

    # Split into user and model sections
    parts = re.split(r'^## Model', content, maxsplit=1, flags=re.MULTILINE)

    if len(parts) < 2:
        return None

    user_part = parts[0]
    model_part = parts[1] if len(parts) > 1 else ""

    # Clean user part (remove "## User" header)
    user_content = re.sub(r'^## User\s*\n?', '', user_part, flags=re.MULTILINE).strip()

    # Clean model part and strip any remaining thoughts
    model_content = strip_thoughts(model_part.strip())

    # Remove leading/trailing ---
    user_content = user_content.strip().strip('-').strip()
    model_content = model_content.strip().strip('-').strip()

    return {
        'user': user_content,
        'model': model_content,
        'start': start_line,
        'end': end_line - 1
    }

def create_file(prompt_num, data, output_dir):
    """Create the extraction file."""
    title = derive_title(data['user'], data['model'])
    category = detect_category(data['user'] + data['model'])
    entities = extract_entities(data['user'] + data['model'])
    slug = slugify(title)

    # Build frontmatter
    frontmatter = f"""---
source: BAA-Kratos-P{prompt_num}
lines: {data['start']}-{data['end']}
prompt: {prompt_num}
extracted: {datetime.now().strftime('%Y-%m-%d')}
category: {category}
entities: [{', '.join(entities)}]
status: extracted
contradictions: []
---"""

    # Build content
    content = f"""{frontmatter}

# {title}

> **Source:** `Formatted_With_Thoughts - Branch of AA - The Kratos of Kings.md` — Prompt {prompt_num}

## Your Notes

{data['user']}

## Analysis

{data['model']}

---
^extract-{slug}-p{prompt_num}
"""

    # Create filename
    safe_title = re.sub(r'[<>:"/\\|?*]', '', title)[:50]
    filename = f"P{prompt_num} - {safe_title} (BAA-Kratos).md"
    filepath = os.path.join(output_dir, filename)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return filename

def main():
    # Read source file
    with open(SOURCE_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Create output directory if needed
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Get sorted prompt numbers
    prompt_nums = sorted(PROMPT_LINES.keys())

    extracted = []

    for i, pnum in enumerate(prompt_nums):
        start_line = PROMPT_LINES[pnum]

        # End line is the next prompt's start, or END_OF_FILE
        if i + 1 < len(prompt_nums):
            end_line = PROMPT_LINES[prompt_nums[i + 1]]
        else:
            end_line = END_OF_FILE

        data = extract_prompt(lines, start_line, end_line, pnum)

        if data:
            filename = create_file(pnum, data, OUTPUT_DIR)
            extracted.append((pnum, filename))
            print(f"Extracted P{pnum}: {filename}")
        else:
            print(f"FAILED to extract P{pnum}")

    print(f"\nTotal extracted: {len(extracted)} prompts")

if __name__ == "__main__":
    main()
