"""
Extract specific prompts from Eclipse II to fill gaps.
Handles file uploads and empty prompts appropriately.
"""

import re
from pathlib import Path
from datetime import date

SOURCE_FILE = Path(r"C:/Users/Xavier/Desktop/Personal/Vaults/X-Writing/Writing/Archive/Gemini AI Exports/Formatted/Formatted_With_Thoughts - The Eclipse of the ATM AU II.md")
OUTPUT_DIR = Path(r"C:/Users/Xavier/Desktop/Personal/Vaults/X-Writing/Writing/ATM/70 Extracted")

# Target prompts to extract
TARGET_PROMPTS = [196, 233, 235, 236, 237, 238]

def find_all_user_markers(content: str) -> list[tuple[int, int]]:
    """Find all ## User markers with their line numbers and positions."""
    markers = []
    lines = content.split('\n')
    pos = 0
    for i, line in enumerate(lines, 1):
        if line.strip() == '## User':
            markers.append((i, pos))
        pos += len(line) + 1  # +1 for newline
    return markers

def get_next_section_start(content: str, start_pos: int) -> int:
    """Find where the next major section starts (## User or ## Model or end)."""
    next_user = content.find('\n## User\n', start_pos + 1)
    next_model = content.find('\n## Model', start_pos + 1)

    # Find the closest one
    candidates = [len(content)]  # default to end
    if next_user != -1:
        candidates.append(next_user)
    if next_model != -1:
        candidates.append(next_model)

    return min(candidates)

def extract_prompt_content(content: str, markers: list, prompt_num: int) -> dict:
    """Extract a specific prompt's content."""
    if prompt_num < 1 or prompt_num > len(markers):
        return None

    start_line, start_pos = markers[prompt_num - 1]

    # Find end of user section
    user_section_end = get_next_section_start(content, start_pos)

    # Extract user content (skip the "## User" header)
    user_content_start = content.find('\n', start_pos) + 1
    user_text = content[user_content_start:user_section_end].strip()

    # Check if next section is Model response
    model_text = ""
    end_line = start_line

    # Count lines to end of user section
    user_section = content[start_pos:user_section_end]
    end_line = start_line + user_section.count('\n')

    # Look for Model response
    if content[user_section_end:user_section_end+10].strip().startswith('## Model'):
        model_start = content.find('\n', user_section_end) + 1

        # Find where Model section ends
        model_end = get_next_section_start(content, user_section_end + 1)
        model_text = content[model_start:model_end].strip()

        # Update end line
        model_section = content[user_section_end:model_end]
        end_line += model_section.count('\n')

    return {
        'prompt_num': prompt_num,
        'start_line': start_line,
        'end_line': end_line,
        'user_content': user_text,
        'model_content': model_text
    }

def strip_thought_blockquotes(text: str) -> str:
    """Remove the Model's Thought Process section and blockquote thoughts."""
    # First, find and remove the entire Model's Thought Process section
    # Pattern: ### Model's Thought Process followed by blockquotes until ---
    text = re.sub(
        r'###\s*Model\'s Thought Process\s*\n+(?:>.*?\n|\s*\n)*---',
        '',
        text,
        flags=re.MULTILINE
    )

    # Remove any remaining standalone blockquote sections
    lines = text.split('\n')
    filtered_lines = []
    in_blockquote_section = False

    for line in lines:
        stripped = line.strip()

        # Skip Model's Thought Process header
        if '### Model\'s Thought Process' in stripped:
            in_blockquote_section = True
            continue

        # Check if line starts with blockquote
        if stripped.startswith('> ') or stripped == '>':
            in_blockquote_section = True
            continue

        # If we hit a non-blockquote, non-empty line after blockquotes, stop skipping
        if in_blockquote_section:
            if stripped == '':
                continue  # Skip empty lines after blockquotes
            elif stripped == '---':
                in_blockquote_section = False
                continue  # Skip the closing ---
            else:
                in_blockquote_section = False

        filtered_lines.append(line)

    result = '\n'.join(filtered_lines).strip()

    # Remove any leftover "## Model" header
    result = re.sub(r'^##\s*Model\s*\n+', '', result)

    # Clean up multiple consecutive empty lines
    result = re.sub(r'\n{3,}', '\n\n', result)

    return result

def strip_thought_from_user_content(text: str) -> str:
    """Remove thought blockquotes from user content section too."""
    # The user content sometimes contains the thought process section
    # Remove it entirely
    text = re.sub(
        r'---\s*\n+###\s*Model\'s Thought Process.*',
        '',
        text,
        flags=re.DOTALL
    )
    return text.strip()

def classify_content(user_text: str, model_text: str) -> tuple[str, list, str]:
    """Determine category, entities, and topic from content."""
    combined = (user_text + ' ' + model_text).lower()

    # Entity extraction
    entities = []
    entity_patterns = [
        (r'\bgodric\b', 'Godric'),
        (r'\bgodzilla\b', 'Godzilla'),
        (r'\bmaria\b', 'Maria'),
        (r'\bmothra\b', 'Mothra'),
        (r'\bbattra\b', 'Battra'),
        (r'\bghidorah\b', 'Ghidorah'),
        (r'\bscylla\b', 'Scylla'),
        (r'\bjunior\b', 'Junior'),
        (r'\bleo\b', 'Leo'),
        (r'\bkong\b', 'Kong'),
        (r'\brodan\b', 'Rodan'),
        (r'\bdagon\b', 'Dagon'),
    ]

    for pattern, name in entity_patterns:
        if re.search(pattern, combined):
            if name not in entities:
                entities.append(name)

    # Category classification
    if re.search(r'dormant|hair|beard|physique|appearance|look|season', combined):
        category = 'Character Development'
    elif re.search(r'atomic|stride|amplification|aura|coating', combined):
        category = 'Mechanics'
    elif re.search(r'relationship|marriage|confession|love', combined):
        category = 'Character Development'
    elif re.search(r'arc|timeline|story|plot', combined):
        category = 'Plot'
    else:
        category = 'Worldbuilding'

    return category, entities, ''

def generate_topic_title(user_text: str, model_text: str, prompt_num: int) -> str:
    """Generate a descriptive topic title from content."""
    combined = user_text.lower()

    # File upload detection
    if '*[user uploaded file:' in combined:
        return 'File Upload Reference'

    # Empty/divider detection
    if not user_text.strip() or user_text.strip() == '---':
        return 'Image Upload Separator'

    # Content-based titles
    if 'dormant' in combined and ('period' in combined or 'look' in combined or 'style' in combined or 'post-marriage' in combined):
        return 'Godric Post-Marriage Dormant Period Look'

    if 'active season' in combined and ('flavor' in combined or 'flavors' in combined):
        return 'Godric Active Season Appearance Flavors'

    if 'active season' in combined:
        return 'Godric Active Season Reference Images'

    # Default
    return f'Prompt {prompt_num} Content'

def create_extraction(data: dict) -> str:
    """Create the formatted extraction file content."""
    # Clean user text - remove thought sections
    user_text = strip_thought_from_user_content(data['user_content'])

    # Clean model text - remove thought sections
    model_text = strip_thought_blockquotes(data['model_content'])

    category, entities, _ = classify_content(user_text, model_text)
    topic = generate_topic_title(user_text, model_text, data['prompt_num'])

    # Handle special cases
    is_file_upload = '*[user uploaded file:' in user_text.lower()
    is_empty = not user_text.strip() or user_text.strip() == '---'

    if is_file_upload:
        status = 'file-upload'
        category = 'Reference'
    elif is_empty:
        status = 'separator'
        category = 'Reference'
    else:
        status = 'extracted'

    slug = topic.lower().replace(' ', '-').replace("'", '')
    slug = re.sub(r'[^a-z0-9-]', '', slug)

    extraction = f"""---
source: Eclipse-II-P{data['prompt_num']:03d}
lines: {data['start_line']}-{data['end_line']}
prompt: {data['prompt_num']}
extracted: {date.today().isoformat()}
category: {category}
entities: [{', '.join(entities)}]
status: {status}
contradictions: []
---

# {topic}
> **Source:** `Formatted_With_Thoughts - The Eclipse of the ATM AU II.md` — Prompt {data['prompt_num']}

## Your Notes
{user_text if user_text else '*[Empty or divider prompt - likely image upload]*'}

## Analysis
{model_text if model_text else '*[No model response for this prompt]*'}

---
^extract-{slug}-p{data['prompt_num']:03d}
"""
    return extraction, topic

def main():
    print(f"Reading source file: {SOURCE_FILE}")
    content = SOURCE_FILE.read_text(encoding='utf-8')

    print("Finding all User markers...")
    markers = find_all_user_markers(content)
    print(f"Found {len(markers)} User prompts total")

    for prompt_num in TARGET_PROMPTS:
        print(f"\n--- Extracting P{prompt_num} ---")

        data = extract_prompt_content(content, markers, prompt_num)
        if not data:
            print(f"  ERROR: Could not extract prompt {prompt_num}")
            continue

        print(f"  Lines: {data['start_line']}-{data['end_line']}")
        print(f"  User content length: {len(data['user_content'])} chars")
        print(f"  Model content length: {len(data['model_content'])} chars")

        extraction, topic = create_extraction(data)

        # Generate filename
        filename = f"{topic} (Eclipse-II-P{prompt_num:03d}).md"
        filename = filename.replace(':', ' -').replace('/', '-')
        output_path = OUTPUT_DIR / filename

        print(f"  Writing: {filename}")
        output_path.write_text(extraction, encoding='utf-8')
        print(f"  Done!")

if __name__ == '__main__':
    main()
