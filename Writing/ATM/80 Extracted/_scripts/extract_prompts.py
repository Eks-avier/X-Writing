#!/usr/bin/env python3
"""
ATM Corpus Extraction Script
Extracts prompts from Gemini conversation exports into individual markdown files.

Usage:
    python extract_prompts.py <source_file> <abbreviation> <output_dir> [--start N] [--end N]

Example:
    python extract_prompts.py "source.md" "BSaga-TG" "./BSaga-TG" --start 301 --end 399
"""

import argparse
import re
import os
from pathlib import Path
from datetime import date
from typing import List, Tuple, Optional


def parse_source_file(filepath: str) -> List[Tuple[int, int]]:
    """
    Parse source file and return list of (line_number, prompt_index) for each ## User marker.
    Line numbers are 1-indexed to match editor display.
    """
    markers = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f, start=1):
            if line.strip() == '## User':
                markers.append(i)
    return markers


def extract_prompt_content(lines: List[str], start_line: int, end_line: int) -> Tuple[str, str]:
    """
    Extract user notes and model response from a prompt block.

    Args:
        lines: All lines from source file (0-indexed)
        start_line: Line number of ## User (1-indexed)
        end_line: Line number of next ## User or EOF (1-indexed)

    Returns:
        (user_notes, model_response)
    """
    # Convert to 0-indexed
    start_idx = start_line - 1
    end_idx = end_line - 1 if end_line else len(lines)

    block = lines[start_idx:end_idx]

    user_notes = []
    model_response = []
    in_user = False
    in_model = False
    in_thoughts = False

    for line in block:
        stripped = line.rstrip('\n')

        # State transitions
        if stripped == '## User':
            in_user = True
            in_model = False
            in_thoughts = False
            continue
        elif stripped == '## Model':
            in_user = False
            in_model = True
            in_thoughts = False
            continue
        elif stripped == "### Model's Thought Process":
            in_thoughts = True
            continue

        # Skip thought blocks entirely
        if in_thoughts:
            # Thoughts end when we hit ## Model or another major section
            if stripped.startswith('## '):
                in_thoughts = False
                if stripped == '## Model':
                    in_model = True
                    continue
            else:
                continue

        # Collect content
        if in_user:
            user_notes.append(stripped)
        elif in_model:
            # Skip lines that are model thoughts (start with >)
            if stripped.startswith('> '):
                continue
            model_response.append(stripped)

    # Clean up: remove leading/trailing empty lines
    user_text = '\n'.join(user_notes).strip()
    model_text = '\n'.join(model_response).strip()

    # Remove separator lines at start/end
    user_text = re.sub(r'^---\s*\n*', '', user_text)
    user_text = re.sub(r'\n*---\s*$', '', user_text)
    model_text = re.sub(r'^---\s*\n*', '', model_text)
    model_text = re.sub(r'\n*---\s*$', '', model_text)

    return user_text.strip(), model_text.strip()


def generate_title(user_notes: str, max_words: int = 6) -> str:
    """
    Generate a placeholder title from user notes.
    Takes first meaningful line and truncates to max_words.
    """
    if not user_notes:
        return "Empty Prompt"

    # Get first non-empty line
    lines = [l.strip() for l in user_notes.split('\n') if l.strip()]
    if not lines:
        return "Empty Prompt"

    first_line = lines[0]

    # Remove markdown formatting
    first_line = re.sub(r'^[#>*-]+\s*', '', first_line)
    first_line = re.sub(r'\*+|_+|`+', '', first_line)

    # Take first N words
    words = first_line.split()[:max_words]
    title = ' '.join(words)

    # Clean up for filename
    title = re.sub(r'[^\w\s-]', '', title)
    title = title.strip()

    if len(title) < 3:
        return "Short Prompt Content"

    # Capitalize words
    title = ' '.join(word.capitalize() for word in title.split())

    return title[:60]  # Max 60 chars


def create_frontmatter(
    source_abbrev: str,
    prompt_num: int,
    start_line: int,
    end_line: int
) -> str:
    """Create YAML frontmatter for extracted file."""
    today = date.today().isoformat()

    return f"""---
source: {source_abbrev}-P{prompt_num:03d}
lines: {start_line}-{end_line}
prompt: {prompt_num}
extracted: {today}
category: Uncategorized
entities: []
status: extracted
contradictions: []
---"""


def sanitize_filename(title: str) -> str:
    """Make title safe for use as filename."""
    # Remove/replace problematic characters
    sanitized = re.sub(r'[<>:"/\\|?*]', '', title)
    sanitized = re.sub(r'\s+', ' ', sanitized).strip()
    return sanitized[:80]  # Reasonable filename length


def extract_prompts(
    source_file: str,
    abbreviation: str,
    output_dir: str,
    start_prompt: int = 1,
    end_prompt: Optional[int] = None
) -> int:
    """
    Main extraction function.

    Args:
        source_file: Path to source markdown file
        abbreviation: Source abbreviation (e.g., "BSaga-TG")
        output_dir: Output directory path
        start_prompt: First prompt number to extract
        end_prompt: Last prompt number to extract (inclusive), or None for all

    Returns:
        Number of files extracted
    """
    # Ensure output directory exists
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    # Read source file
    with open(source_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Find all ## User markers
    markers = parse_source_file(source_file)
    total_prompts = len(markers)

    print(f"Found {total_prompts} prompts in source file")

    # Validate range
    if start_prompt < 1 or start_prompt > total_prompts:
        print(f"Error: start_prompt {start_prompt} out of range (1-{total_prompts})")
        return 0

    if end_prompt is None:
        end_prompt = total_prompts
    elif end_prompt > total_prompts:
        print(f"Warning: end_prompt {end_prompt} exceeds total ({total_prompts}), using {total_prompts}")
        end_prompt = total_prompts

    extracted_count = 0

    for prompt_num in range(start_prompt, end_prompt + 1):
        # Get line boundaries (0-indexed into markers list)
        marker_idx = prompt_num - 1
        start_line = markers[marker_idx]

        # End line is start of next prompt, or EOF
        if marker_idx + 1 < len(markers):
            end_line = markers[marker_idx + 1] - 1
        else:
            end_line = len(lines)

        # Extract content
        user_notes, model_response = extract_prompt_content(lines, start_line, end_line)

        # Generate title
        title = generate_title(user_notes)

        # Create frontmatter
        frontmatter = create_frontmatter(abbreviation, prompt_num, start_line, end_line)

        # Build file content
        safe_title = sanitize_filename(title)
        filename = f"P{prompt_num:03d} - {safe_title} ({abbreviation}).md"
        filepath = Path(output_dir) / filename

        content = f"""{frontmatter}

# {title}
> **Source:** `{Path(source_file).name}` — Prompt {prompt_num}

## Your Notes

{user_notes if user_notes else "(No user content in this prompt)"}

## Analysis

{model_response if model_response else "(No model response in this prompt)"}

---
^extract-p{prompt_num:03d}
"""

        # Write file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        extracted_count += 1

        if extracted_count % 10 == 0:
            print(f"  Extracted {extracted_count} files...")

    print(f"\nExtraction complete: {extracted_count} files created in {output_dir}")
    return extracted_count


def main():
    parser = argparse.ArgumentParser(
        description='Extract prompts from Gemini conversation exports',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Extract all prompts:
    python extract_prompts.py "source.md" "BSaga-TG" "./output"

  Extract prompts 301-399:
    python extract_prompts.py "source.md" "BSaga-TG" "./output" --start 301 --end 399

  Extract from prompt 50 onwards:
    python extract_prompts.py "source.md" "MySource" "./output" --start 50
"""
    )

    parser.add_argument('source_file', help='Path to source markdown file')
    parser.add_argument('abbreviation', help='Source abbreviation (e.g., BSaga-TG)')
    parser.add_argument('output_dir', help='Output directory for extracted files')
    parser.add_argument('--start', type=int, default=1, help='First prompt number to extract (default: 1)')
    parser.add_argument('--end', type=int, default=None, help='Last prompt number to extract (default: all)')

    args = parser.parse_args()

    if not os.path.exists(args.source_file):
        print(f"Error: Source file not found: {args.source_file}")
        return 1

    extract_prompts(
        args.source_file,
        args.abbreviation,
        args.output_dir,
        args.start,
        args.end
    )

    return 0


if __name__ == '__main__':
    exit(main())
