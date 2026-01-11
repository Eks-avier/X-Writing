# ATM Extraction Quick Reference

> **Purpose:** Quick reference for Claude instances continuing extraction work.
> **Full Documentation:** [[_MANIFESTO]]

---

## Project Overview

Extract discrete topics from 9 Gemini conversation exports (stream-of-consciousness worldbuilding for the ATM Monsterverse AU) into fine-grained Obsidian markdown files. All 9 files share a common trunk (P001-P198); only extract unique prompts from each branch.

---

## Source Abbreviations

| Abbreviation | Full Name | Prompts | Unique Start |
|--------------|-----------|---------|--------------|
| Eclipse-II | The Eclipse of the ATM AU II | 245 | P001 (pilot) |
| AA-Kratos | AA - The Kratos of Kings | 344 | P199 |
| Saga-TG | The Saga of the Titanus gojira | 300 | P199 |
| Standing | Standing Hierarchy | 294 | P199 |
| BAA-Kratos | Branch of AA - Kratos | 284 | P199 |
| TG | The Titanus gojira | 276 | P199 |
| Kratos | The Kratos of Kings | 263 | P199 |
| BTG | Branch of Titanus gojira | 263 | P199 |
| Eclipse-I | Eclipse of ATM AU I | 260 | P199 |

---

## Key Parsing Rules

1. **Prompt Delimiter:** `## User` marks start of a new prompt
2. **Model Response:** `## Model` marks start of Gemini's response
3. **Strip Thoughts:** Lines starting with `> ` in Model sections are internal thoughts - REMOVE THEM
4. **Extraction Unit:** `###` headers define topic boundaries
5. **Preserve User Voice:** User input must be kept exactly as written

---

## File Naming

```
PXXX - [Topic Title] (Source).md
```

- Topic title: Max 60 characters
- Prompt number: 3-digit (P001, P199, P344)
- Example: `P205 - Zuko Principle and Tangibility Theme (TG).md`

---

## Extraction Template

```markdown
---
source: [Source]-P[NNN]
lines: [start]-[end]
prompt: [N]
extracted: [YYYY-MM-DD]
category: [Worldbuilding|Character Development|Plot|Mechanics]
entities: []
status: extracted
contradictions: []
---

# [Topic Title]

> **Source:** `Formatted_With_Thoughts - [Filename].md` — Prompt [N]

## Your Notes

[User's exact input - PRESERVE VERBATIM]

## Analysis

[Model's cleaned response - thoughts stripped]

---
^extract-[topic-slug]-p[nnn]
```

---

## Agent Types

| Agent | Purpose | When to Use |
|-------|---------|-------------|
| EXTRACTOR | Create topic files | Main extraction work |
| VALIDATOR | Check contradictions | After extraction complete |
| LINKER | Cross-reference entities | Build entity registry |
| CHRONICLER | Track topic evolution | Identify multi-prompt topics |
| INDEXER | Build indexes | Generate indexes |
| QA | Validate format | Check file structure |

---

## Metadata Files

| File | Purpose |
|------|---------|
| [[_MANIFESTO]] | Full workflow documentation |
| [[_Progress]] | Extraction progress tracking |
| [[_Index]] | Master topic inventory |
| [[_QA_Report]] | Quality assurance validation |
| [[_Entity_Registry]] | Named entities across sources |
| [[_Evolution_Chronicles]] | Topic evolution chains |

---

## Current Status

Check [[_Progress]] for:
- Completed sources
- Next source to process
- Pending tasks

---

## Critical Rules

1. **Never modify user's original phrasing** in "## Your Notes" section
2. **Strip all blockquote lines** (`> `) from model responses
3. **One file per ### section** (topic extraction granularity)
4. **Check _Progress.md** before starting any extraction work
5. **Update _Progress.md** after completing extraction batches
