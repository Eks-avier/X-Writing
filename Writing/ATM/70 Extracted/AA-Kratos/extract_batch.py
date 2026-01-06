#!/usr/bin/env python3
"""Extract prompts P199-P248 from AA-Kratos source file."""

import re
import os
from datetime import datetime

# Line numbers for P199-P248 (0-indexed from grep output)
# P199=line 15776, P200=15822, ..., P248=19851
PROMPT_LINES = {
    199: 15776, 200: 15822, 201: 15930, 202: 16015, 203: 16078,
    204: 16145, 205: 16206, 206: 16258, 207: 16328, 208: 16380,
    209: 16432, 210: 16489, 211: 16552, 212: 16630, 213: 16713,
    214: 16775, 215: 16841, 216: 16892, 217: 16946, 218: 17006,
    219: 17074, 220: 17168, 221: 17246, 222: 17319, 223: 17418,
    224: 17562, 225: 17655, 226: 17730, 227: 17811, 228: 17875,
    229: 17944, 230: 18000, 231: 18073, 232: 18128, 233: 18169,
    234: 18218, 235: 18239, 236: 18303, 237: 18368, 238: 18407,
    239: 18483, 240: 18555, 241: 18602, 242: 18665, 243: 18715,
    244: 18805, 245: 18908, 246: 18985, 247: 19058, 248: 19134,
}

# Next prompt line for end boundary (P249=19214)
NEXT_AFTER_248 = 19214

SOURCE_FILE = r"C:/Users/Xavier/Desktop/Personal/Vaults/X-Writing/Writing/Archive/Gemini AI Exports/Formatted/Formatted_With_Thoughts - AA - The Kratos of Kings.md"
OUTPUT_DIR = r"C:/Users/Xavier/Desktop/Personal/Vaults/X-Writing/Writing/ATM/70 Extracted/AA-Kratos"

def slugify(text):
    """Create a URL-friendly slug from text."""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-')[:50]

def derive_title(user_content):
    """Derive a topic title from user content."""
    # Take first meaningful line
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
    if any(kw in content_lower for kw in ['atomic', 'power', 'ability', 'kratos', 'arsenal']):
        return "Mechanics"
    if any(kw in content_lower for kw in ['battle', 'fight', 'invasion', 'event']):
        return "Plot"

    return "Worldbuilding"

def extract_entities(content):
    """Extract main entities mentioned in content."""
    entities = []
    entity_patterns = [
        r'\bGodric\b', r'\bGodzilla\b', r'\bMaria\b', r'\bMothra\b',
        r'\bBattra\b', r'\bRodan\b', r'\bAnguirus\b', r'\bKong\b',
        r'\bDagon\b', r'\bMonarch\b', r'\bMadison\b', r'\bMark\b',
        r'\bRick\b', r'\bStanton\b', r'\bYamamoto\b'
    ]

    for pattern in entity_patterns:
        if re.search(pattern, content, re.IGNORECASE):
            match = re.search(pattern, content, re.IGNORECASE)
            entity = match.group(0)
            # Normalize
            if entity.lower() in ['godric', 'godzilla']:
                entity = 'Godric/Godzilla'
            elif entity.lower() in ['maria', 'mothra']:
                entity = 'Maria/Mothra'
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
        # Also detect blockquote lines that start a thought (e.g., "> **Defining...")
        if line.strip().startswith('> **') and any(kw in line for kw in ['Defining', 'Analyzing', 'Exploring', 'Focusing', 'Developing', 'Integrating', 'Synthesizing', 'Considering', 'Deconstructing', 'Simulating', 'Dissecting']):
            in_thought_block = True
            continue
        if in_thought_block:
            if line.strip().startswith('>'):
                continue
            elif line.strip() == '---':
                in_thought_block = False
                continue
            elif line.strip() == '':
                continue  # Skip blank lines in thought blocks
            elif line.strip() and not line.strip().startswith('>'):
                in_thought_block = False

        result.append(line)

    # Clean up multiple blank lines
    cleaned = '\n'.join(result)
    cleaned = re.sub(r'\n{3,}', '\n\n', cleaned)
    return cleaned.strip()

def strip_thought_section(content):
    """Remove Model's Thought Process sections entirely."""
    # Remove everything from "### Model's Thought Process" to the next "## Model" or end
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
    title = derive_title(data['user'])
    category = detect_category(data['user'] + data['model'])
    entities = extract_entities(data['user'] + data['model'])
    slug = slugify(title)

    # Build frontmatter
    frontmatter = f"""---
source: AA-Kratos-P{prompt_num}
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
> **Source:** `Formatted_With_Thoughts - AA - The Kratos of Kings.md` - Prompt {prompt_num}

## Your Notes
{data['user']}

## Analysis
{data['model']}

---
^extract-{slug}-p{prompt_num}
"""

    # Create filename
    safe_title = re.sub(r'[<>:"/\\|?*]', '', title)[:50]
    filename = f"P{prompt_num} - {safe_title} (AA-Kratos).md"
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

        # End line is the next prompt's start, or NEXT_AFTER_248
        if i + 1 < len(prompt_nums):
            end_line = PROMPT_LINES[prompt_nums[i + 1]]
        else:
            end_line = NEXT_AFTER_248

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
