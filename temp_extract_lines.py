#!/usr/bin/env python3
"""Find line numbers for prompts 171-198"""

source_file = r"C:\Users\Xavier\Desktop\Personal\Vaults\X-Writing\Writing\Archive\Gemini AI Exports\Formatted\Formatted_With_Thoughts - The Eclipse of the ATM AU II.md"

with open(source_file, 'r', encoding='utf-8') as f:
    prompt_count = 0
    for line_num, line in enumerate(f, 1):
        if line.strip() == "## User":
            prompt_count += 1
            if 171 <= prompt_count <= 199:
                print(f"P{prompt_count}: line {line_num}")
