"""
Eclipse II Prompt Extraction Script
Extracts prompts P199-P245 from the Eclipse II source file
"""

import re
import os
from datetime import datetime

# Configuration
SOURCE_FILE = r"C:/Users/Xavier/Desktop/Personal/Vaults/X-Writing/Writing/Archive/Gemini AI Exports/Formatted/Formatted_With_Thoughts - The Eclipse of the ATM AU II.md"
OUTPUT_DIR = r"C:/Users/Xavier/Desktop/Personal/Vaults/X-Writing/Writing/ATM/70 Extracted/"
START_PROMPT = 199
END_PROMPT = 245

def read_file(filepath):
    """Read the entire source file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def split_into_prompts(content):
    """Split content by ## User markers and return list of prompts with line numbers"""
    lines = content.split('\n')
    prompts = []
    current_prompt = []
    current_start_line = 1
    prompt_count = 0

    for i, line in enumerate(lines, 1):
        if line.strip() == '## User':
            if current_prompt:
                prompts.append({
                    'number': prompt_count,
                    'start_line': current_start_line,
                    'end_line': i - 1,
                    'content': '\n'.join(current_prompt)
                })
            prompt_count += 1
            current_prompt = [line]
            current_start_line = i
        else:
            current_prompt.append(line)

    # Add the last prompt
    if current_prompt:
        prompts.append({
            'number': prompt_count,
            'start_line': current_start_line,
            'end_line': len(lines),
            'content': '\n'.join(current_prompt)
        })

    return prompts

def extract_user_content(prompt_content):
    """Extract the user's content from a prompt (between ## User and ## Model or next marker)"""
    lines = prompt_content.split('\n')
    user_lines = []
    in_user_section = False
    in_thoughts = False

    for line in lines:
        if line.strip() == '## User':
            in_user_section = True
            continue
        elif line.strip().startswith('## Model'):
            in_user_section = False
            break
        elif line.strip().startswith("### Model's Thought Process"):
            in_thoughts = True
            continue
        elif in_thoughts and line.strip().startswith('## Model'):
            in_thoughts = False
            break

        if in_user_section and not in_thoughts:
            user_lines.append(line)

    return '\n'.join(user_lines).strip()

def extract_model_response(prompt_content):
    """Extract the model's response from a prompt (after ## Model)"""
    lines = prompt_content.split('\n')
    model_lines = []
    in_model_section = False
    in_thoughts = False

    for line in lines:
        if line.strip() == '## Model':
            in_model_section = True
            continue
        elif line.strip().startswith("### Model's Thought Process"):
            in_thoughts = True
            continue
        elif in_thoughts and line.strip() == '---':
            in_thoughts = False
            continue

        if in_model_section and not in_thoughts:
            # Skip blockquote thought sections
            if line.strip().startswith('>'):
                continue
            model_lines.append(line)

    return '\n'.join(model_lines).strip()

def generate_title(user_content, prompt_number):
    """Generate a descriptive title from user content"""
    # Look for headings first
    heading_match = re.search(r'^##?\s+(.+)$', user_content, re.MULTILINE)
    if heading_match:
        title = heading_match.group(1).strip()
        # Clean up the title
        title = re.sub(r'[^\w\s\-]', '', title)
        title = title.strip()[:60]
        return title if title else f"Prompt-{prompt_number}"

    # Otherwise use first significant line
    lines = [l.strip() for l in user_content.split('\n') if l.strip() and not l.startswith('#')]
    if lines:
        title = lines[0][:60]
        title = re.sub(r'[^\w\s\-]', '', title)
        return title.strip() if title.strip() else f"Prompt-{prompt_number}"

    return f"Prompt-{prompt_number}"

def determine_category(content):
    """Determine category based on content keywords"""
    content_lower = content.lower()

    if any(kw in content_lower for kw in ['krátos', 'kratos', 'atomic amplification', 'aa', 'stride', 'mantle', 'ability', 'power']):
        return 'Mechanics'
    elif any(kw in content_lower for kw in ['godric', 'maria', 'mothra', 'godzilla', 'rodan', 'battra', 'relationship']):
        return 'Character Development'
    elif any(kw in content_lower for kw in ['titanus', 'species', 'titan', 'history', 'world']):
        return 'Worldbuilding'
    elif any(kw in content_lower for kw in ['scene', 'plot', 'arc', 'story']):
        return 'Plot'
    else:
        return 'Worldbuilding'

def extract_entities(content):
    """Extract character/entity names from content"""
    entities = []

    # Common entities to look for
    entity_patterns = [
        'Godric', 'Maria', 'Godzilla', 'Mothra', 'Battra', 'Rodan',
        'Kong', 'Anguirus', 'Ghidorah', 'Ichi', 'Scylla', 'Dagon',
        'Madison', 'Mark', 'Rick', 'Monarch', 'Leo', 'Lora', 'Junior'
    ]

    for entity in entity_patterns:
        if entity.lower() in content.lower():
            entities.append(entity)

    return entities[:5]  # Limit to 5 entities

def sanitize_filename(title):
    """Create a safe filename from title"""
    # Remove/replace unsafe characters
    safe_title = re.sub(r'[<>:"/\\|?*]', '', title)
    safe_title = re.sub(r'\s+', ' ', safe_title).strip()
    return safe_title[:80]  # Limit length

def create_output_file(prompt_data, prompt_number):
    """Create the output markdown file for a prompt"""
    user_content = extract_user_content(prompt_data['content'])
    model_response = extract_model_response(prompt_data['content'])

    # Skip if both are empty
    if not user_content.strip() and not model_response.strip():
        return None

    title = generate_title(user_content, prompt_number)
    category = determine_category(user_content + model_response)
    entities = extract_entities(user_content + model_response)

    safe_title = sanitize_filename(title)
    filename = f"{safe_title} (Eclipse-II-P{prompt_number}).md"

    # Create frontmatter
    content = f"""---
source: Eclipse-II-P{prompt_number}
lines: {prompt_data['start_line']}-{prompt_data['end_line']}
prompt: {prompt_number}
extracted: {datetime.now().strftime('%Y-%m-%d')}
category: {category}
entities: [{', '.join(entities)}]
status: extracted
contradictions: []
---

# {title}
> **Source:** `Formatted_With_Thoughts - The Eclipse of the ATM AU II.md` - Prompt {prompt_number}

## Your Notes
{user_content if user_content else '[No user content in this prompt]'}

## Analysis
{model_response if model_response else '[No model response in this prompt]'}

---
^extract-{re.sub(r'[^a-z0-9-]', '-', title.lower())[:30]}-p{prompt_number}
"""

    return {
        'filename': filename,
        'content': content,
        'title': title
    }

def main():
    print(f"Reading source file: {SOURCE_FILE}")
    content = read_file(SOURCE_FILE)

    print("Splitting into prompts...")
    prompts = split_into_prompts(content)
    print(f"Found {len(prompts)} total prompts")

    # Extract prompts 199-245 (0-indexed: 198-244)
    target_prompts = []
    for i, prompt in enumerate(prompts):
        prompt_num = i + 1  # 1-indexed prompt number
        if START_PROMPT <= prompt_num <= END_PROMPT:
            prompt['number'] = prompt_num
            target_prompts.append(prompt)

    print(f"Extracting prompts {START_PROMPT}-{END_PROMPT} ({len(target_prompts)} prompts)")

    # Ensure output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Process each prompt
    created_files = []
    for prompt_data in target_prompts:
        prompt_num = prompt_data['number']

        result = create_output_file(prompt_data, prompt_num)
        if result:
            filepath = os.path.join(OUTPUT_DIR, result['filename'])
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(result['content'])
            created_files.append(result['filename'])
            print(f"  Created: {result['filename']}")
        else:
            print(f"  Skipped P{prompt_num}: Empty content")

    print(f"\nExtraction complete! Created {len(created_files)} files.")
    return created_files

if __name__ == "__main__":
    main()
