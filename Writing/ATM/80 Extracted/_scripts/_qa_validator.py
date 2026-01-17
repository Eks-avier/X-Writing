"""
QA Validator for Extracted Files
Validates YAML frontmatter, sections, block IDs, and content
"""

import os
import re
from pathlib import Path
from collections import defaultdict

# Directory to check
EXTRACT_DIR = Path(r"C:/Users/Xavier/Desktop/Personal/Vaults/X-Writing/Writing/ATM/70 Extracted")

# Required and optional YAML fields
REQUIRED_FIELDS = ['source', 'lines', 'prompt', 'extracted', 'category', 'entities', 'status']
OPTIONAL_FIELDS = ['contradictions', 'evolution_chain', 'related']

# Results storage
issues = defaultdict(list)
passing_files = []
all_block_ids = {}
files_checked = 0

def extract_yaml_frontmatter(content):
    """Extract YAML frontmatter from content"""
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if match:
        return match.group(1), True
    return None, False

def parse_yaml_fields(yaml_text):
    """Simple YAML field parser"""
    fields = {}
    current_field = None
    current_value = []

    for line in yaml_text.split('\n'):
        # Check for new field
        field_match = re.match(r'^(\w+):\s*(.*)', line)
        if field_match:
            # Save previous field
            if current_field:
                fields[current_field] = '\n'.join(current_value).strip()
            current_field = field_match.group(1)
            current_value = [field_match.group(2)] if field_match.group(2) else []
        elif current_field and line.startswith('  '):
            current_value.append(line)

    # Save last field
    if current_field:
        fields[current_field] = '\n'.join(current_value).strip()

    return fields

def check_section_exists(content, section_name, min_chars=50):
    """Check if a section exists and has sufficient content"""
    # Handle variations like "## Your Notes (P100)" for combined files
    pattern = rf'^## {re.escape(section_name)}(?:\s*\([^)]+\))?\s*\n(.*?)(?=^## Analysis|\Z)'
    match = re.search(pattern, content, re.MULTILINE | re.DOTALL)
    if not match:
        return False, "Section missing"

    section_content = match.group(1).strip()

    # Remove horizontal rules from the count
    cleaned_content = re.sub(r'^---+\s*$', '', section_content, flags=re.MULTILINE).strip()

    if len(cleaned_content) < min_chars:
        return False, f"Section too short ({len(cleaned_content)} chars)"

    return True, section_content

def check_analysis_section(content):
    """Check if Analysis section exists and has sufficient content"""
    pattern = r'^## Analysis\s*\n(.*?)(?=^---\s*$|\^extract|\Z)'
    match = re.search(pattern, content, re.MULTILINE | re.DOTALL)
    if not match:
        return False, "Section missing"

    section_content = match.group(1).strip()

    # Remove horizontal rules from the count
    cleaned_content = re.sub(r'^---+\s*$', '', section_content, flags=re.MULTILINE).strip()

    if len(cleaned_content) < 50:
        return False, f"Section too short ({len(cleaned_content)} chars)"

    return True, section_content

def check_source_reference(content):
    """Check if source reference block exists after title"""
    # Look for pattern: # Title\n(optional blank line)\n> **Source:** ...
    # Allow for 0-2 blank lines between title and source
    pattern = r'^# .+\n\n?> \*\*Source:\*\*'
    return bool(re.search(pattern, content, re.MULTILINE))

def check_block_id(content, filename):
    """Check if file ends with valid block ID"""
    lines = content.strip().split('\n')
    if not lines:
        return False, None

    last_line = lines[-1].strip()
    # Pattern: ^extract-[keyword]-p[nnn] or ^extract-[keyword]-p[nnn-nnn]
    match = re.match(r'^\^extract-[\w-]+-p\d{3}(?:-p?\d{3})?$', last_line)
    if match:
        return True, last_line
    return False, last_line

def check_gemini_thoughts(content):
    """Check for remaining Gemini thought blockquotes in Analysis section"""
    # Find Analysis section
    analysis_match = re.search(r'^## Analysis\s*\n(.*?)(?=^## |\Z)', content, re.MULTILINE | re.DOTALL)
    if not analysis_match:
        return []

    analysis_content = analysis_match.group(1)

    # Look for blockquotes that look like internal reasoning
    thought_patterns = [
        r'^> .*(?:I think|I believe|Let me|This seems|Perhaps|Maybe|I\'m not sure|Hmm|thinking about).*$',
        r'^> .*(?:should I|could be|might be|I wonder|considering).*$',
    ]

    found_thoughts = []
    for line in analysis_content.split('\n'):
        if line.startswith('> '):
            for pattern in thought_patterns:
                if re.search(pattern, line, re.IGNORECASE):
                    found_thoughts.append(line[:100])
                    break

    return found_thoughts

def categorize_file_type(filename, content):
    """Categorize the file type for reporting purposes"""
    if "File Upload" in filename or "Image Upload" in filename:
        return "upload_placeholder"
    if "Separator" in filename:
        return "separator"
    return "standard"

def validate_file(filepath):
    """Validate a single file"""
    global files_checked

    filename = filepath.name
    file_issues = []

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        issues['read_error'].append((filename, str(e)))
        return False

    files_checked += 1
    file_type = categorize_file_type(filename, content)

    # 1. YAML Frontmatter Validation
    yaml_text, has_yaml = extract_yaml_frontmatter(content)
    if not has_yaml:
        file_issues.append("No YAML frontmatter found")
        issues['no_yaml'].append(filename)
    else:
        fields = parse_yaml_fields(yaml_text)
        missing_required = [f for f in REQUIRED_FIELDS if f not in fields or not fields[f]]
        if missing_required:
            file_issues.append(f"Missing required fields: {', '.join(missing_required)}")
            issues['missing_yaml_fields'].append((filename, missing_required))

    # 2. Section Validation
    # Check "Your Notes" section - with relaxed requirements for special file types
    notes_ok, notes_result = check_section_exists(content, "Your Notes")
    if not notes_ok:
        # Check for variant headers like "## Your Notes (P100)"
        variant_pattern = r'^## Your Notes \([^)]+\)\s*\n'
        if re.search(variant_pattern, content, re.MULTILINE):
            notes_ok = True  # Accept variant headers
        else:
            # Relaxed check for upload/separator files
            if file_type in ["upload_placeholder", "separator"]:
                # These files may have minimal notes - just check section exists
                if "## Your Notes" in content:
                    notes_ok = True
                else:
                    file_issues.append(f"Your Notes section: {notes_result}")
                    issues['your_notes_issue'].append((filename, notes_result))
            else:
                file_issues.append(f"Your Notes section: {notes_result}")
                issues['your_notes_issue'].append((filename, notes_result))

    # Check "Analysis" section
    analysis_ok, analysis_result = check_analysis_section(content)
    if not analysis_ok:
        # Relaxed check for upload/separator files
        if file_type in ["upload_placeholder", "separator"]:
            if "## Analysis" in content:
                analysis_ok = True
            else:
                file_issues.append(f"Analysis section: {analysis_result}")
                issues['analysis_issue'].append((filename, analysis_result))
        else:
            file_issues.append(f"Analysis section: {analysis_result}")
            issues['analysis_issue'].append((filename, analysis_result))

    # Check source reference block
    if not check_source_reference(content):
        file_issues.append("Source reference block missing or malformed")
        issues['source_reference_missing'].append(filename)

    # 3. Block ID Validation
    block_id_ok, block_id = check_block_id(content, filename)
    if not block_id_ok:
        file_issues.append(f"Invalid block ID format: {block_id}")
        issues['invalid_block_id'].append((filename, block_id))
    else:
        # Check for duplicate block IDs
        if block_id in all_block_ids:
            file_issues.append(f"Duplicate block ID: {block_id} (also in {all_block_ids[block_id]})")
            issues['duplicate_block_id'].append((filename, block_id, all_block_ids[block_id]))
        else:
            all_block_ids[block_id] = filename

    # 4. Content Validation - Gemini thoughts
    gemini_thoughts = check_gemini_thoughts(content)
    if gemini_thoughts:
        file_issues.append(f"Possible Gemini thought blockquotes: {len(gemini_thoughts)} found")
        issues['gemini_thoughts'].append((filename, gemini_thoughts))

    if file_issues:
        issues['all_issues'].append((filename, file_issues))
        return False
    else:
        passing_files.append(filename)
        return True

def generate_report():
    """Generate QA report"""
    report = []
    report.append("# QA Validation Report")
    report.append("")
    report.append(f"**Generated:** {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append("")

    # Summary
    report.append("## Summary")
    report.append("")
    report.append(f"- **Total files checked:** {files_checked}")
    report.append(f"- **Files passing all checks:** {len(passing_files)}")
    report.append(f"- **Files with issues:** {len(issues['all_issues'])}")
    report.append("")

    # Issue breakdown
    report.append("## Issue Breakdown")
    report.append("")

    issue_counts = {
        'no_yaml': 'No YAML frontmatter',
        'missing_yaml_fields': 'Missing required YAML fields',
        'your_notes_issue': 'Your Notes section issues',
        'analysis_issue': 'Analysis section issues',
        'source_reference_missing': 'Source reference missing',
        'invalid_block_id': 'Invalid block ID format',
        'duplicate_block_id': 'Duplicate block IDs',
        'gemini_thoughts': 'Possible Gemini thought blockquotes',
        'read_error': 'File read errors'
    }

    for key, label in issue_counts.items():
        if issues[key]:
            report.append(f"- **{label}:** {len(issues[key])}")

    if not any(issues[key] for key in issue_counts):
        report.append("*No issues found!*")

    report.append("")

    # Detailed issues by category
    report.append("## Detailed Issues")
    report.append("")

    # No YAML
    if issues['no_yaml']:
        report.append("### Files Without YAML Frontmatter")
        report.append("")
        report.append("These 26 files (P001-P005) need YAML frontmatter added:")
        report.append("")
        for f in issues['no_yaml']:
            report.append(f"- `{f}`")
        report.append("")
        report.append("**Suggested Fix:** Add YAML frontmatter block at the start of each file:")
        report.append("```yaml")
        report.append("---")
        report.append("source: Eclipse-II-PXXX")
        report.append("lines: [start-end]")
        report.append("prompt: XXX")
        report.append("extracted: 2026-01-05")
        report.append("category: [category]")
        report.append("entities: []")
        report.append("status: extracted")
        report.append("---")
        report.append("```")
        report.append("")

    # Missing YAML fields
    if issues['missing_yaml_fields']:
        report.append("### Files Missing Required YAML Fields")
        report.append("")

        # Group by missing fields for cleaner reporting
        fields_to_files = defaultdict(list)
        for f, fields in issues['missing_yaml_fields']:
            key = tuple(sorted(fields))
            fields_to_files[key].append(f)

        for missing_fields, files in fields_to_files.items():
            report.append(f"**Missing `{', '.join(missing_fields)}` ({len(files)} files):**")
            report.append("")
            for f in files:
                report.append(f"- `{f}`")
            report.append("")

        report.append("**Suggested Fix:** Add the missing fields to each file's YAML frontmatter.")
        report.append("For `lines` field, use format: `lines: start-end` (e.g., `lines: 3-278`)")
        report.append("")

    # Your Notes issues
    if issues['your_notes_issue']:
        report.append("### Your Notes Section Issues")
        report.append("")
        for f, issue in issues['your_notes_issue']:
            report.append(f"- `{f}`: {issue}")
        report.append("")

    # Analysis issues
    if issues['analysis_issue']:
        report.append("### Analysis Section Issues")
        report.append("")
        for f, issue in issues['analysis_issue']:
            report.append(f"- `{f}`: {issue}")
        report.append("")

    # Source reference missing
    if issues['source_reference_missing']:
        report.append("### Files Missing Source Reference Block")
        report.append("")
        for f in issues['source_reference_missing']:
            report.append(f"- `{f}`")
        report.append("")

    # Invalid block IDs
    if issues['invalid_block_id']:
        report.append("### Files With Invalid Block ID Format")
        report.append("")
        report.append("Expected format: `^extract-[keyword]-p[nnn]`")
        report.append("")
        for f, block_id in issues['invalid_block_id']:
            report.append(f"- `{f}`: Found `{block_id}`")
        report.append("")

    # Duplicate block IDs
    if issues['duplicate_block_id']:
        report.append("### Duplicate Block IDs")
        report.append("")
        for f, block_id, other_file in issues['duplicate_block_id']:
            report.append(f"- `{block_id}` in both:")
            report.append(f"  - `{f}`")
            report.append(f"  - `{other_file}`")
        report.append("")

    # Gemini thoughts
    if issues['gemini_thoughts']:
        report.append("### Possible Gemini Thought Blockquotes")
        report.append("")
        for f, thoughts in issues['gemini_thoughts']:
            report.append(f"- `{f}`:")
            for t in thoughts[:3]:  # Show first 3
                report.append(f"  - `{t[:80]}...`")
        report.append("")

    # Read errors
    if issues['read_error']:
        report.append("### File Read Errors")
        report.append("")
        for f, err in issues['read_error']:
            report.append(f"- `{f}`: {err}")
        report.append("")

    # Specific Fixes Needed section
    report.append("## Specific Fixes Needed")
    report.append("")

    if issues['no_yaml']:
        report.append("### 1. Add YAML Frontmatter to P001-P005 Files")
        report.append("")
        report.append("The first 26 files (Prompts 1-5) were extracted without YAML frontmatter.")
        report.append("Each needs the standard frontmatter block added at the very beginning of the file.")
        report.append("")

    if not issues['no_yaml'] and not issues['missing_yaml_fields'] and not issues['your_notes_issue'] and not issues['analysis_issue'] and not issues['source_reference_missing'] and not issues['invalid_block_id'] and not issues['duplicate_block_id'] and not issues['gemini_thoughts'] and not issues['read_error']:
        report.append("*All files pass validation! No fixes needed.*")

    report.append("")

    return '\n'.join(report)

def main():
    """Main validation function"""
    print(f"Scanning directory: {EXTRACT_DIR}")

    # Get all markdown files, excluding underscore-prefixed files
    md_files = [f for f in EXTRACT_DIR.glob("*.md") if not f.name.startswith('_')]
    md_files = sorted(md_files)

    print(f"Found {len(md_files)} files to check")

    for filepath in md_files:
        validate_file(filepath)

    # Generate report
    report = generate_report()

    # Write report
    report_path = EXTRACT_DIR / "_QA_Report.md"
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report)

    print(f"\nReport written to: {report_path}")
    print(f"Files checked: {files_checked}")
    print(f"Passing: {len(passing_files)}")
    print(f"With issues: {len(issues['all_issues'])}")

if __name__ == "__main__":
    main()
