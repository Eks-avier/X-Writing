# ATM Gemini Export Extraction Manifesto

> **Purpose:** This document enables any Claude instance to continue the extraction work on this project. Read this entire file before taking any action.

> **Last Updated:** 2026-01-03
> **Created By:** Claude Opus 4.5

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [Source Material](#2-source-material)
3. [Branch Genealogy](#3-branch-genealogy)
4. [Output Specifications](#4-output-specifications)
5. [Agent Architecture](#5-agent-architecture)
6. [Extraction Workflow](#6-extraction-workflow)
7. [Quality Standards](#7-quality-standards)
8. [Known Entities](#8-known-entities)
9. [Progress Tracking](#9-progress-tracking)
10. [File Templates](#10-file-templates)
11. [Troubleshooting](#11-troubleshooting)

---

## 1. Project Overview

### What Is This Project?

The user (Xavier) has 9 large conversation exports from Google AI Studio (Gemini) containing stream-of-consciousness worldbuilding discussions about their **Antitheriomorphosis (ATM) Alternate Universe** - a Monsterverse/Godzilla fanfiction with elaborate power systems, character development, and lore.

### Goal

Extract discrete topics from these conversations into fine-grained Obsidian markdown files that can be:
- Studied in isolation
- Cross-referenced via Obsidian's linking features
- Validated for contradictions
- Organized into the existing ATM vault structure

### Key Principles

1. **Preserve User's Voice:** User's original phrasing must be kept exactly as written
2. **Clean Model Response:** Strip Gemini's internal thoughts (blockquotes), clean up formatting
3. **Fine-Grained Extraction:** One file per `###` section (lowest-level headers)
4. **Traceability:** Every file must reference its source location
5. **Flag Contradictions:** When the same topic has conflicting information across prompts, flag it
6. **Track Evolution:** Same topic discussed multiple times = separate files, linked chronologically

---

## 2. Source Material

### Source Directory
```
C:\Users\Xavier\Desktop\Personal\Vaults\X-Writing\Writing\Archive\Gemini AI Exports\Formatted\
```

### Source Files (9 total)

| File | Prompts | Lines | Status |
|------|---------|-------|--------|
| `Formatted_With_Thoughts - AA - The Kratos of Kings.md` | 344 | 27,171 | Pending |
| `Formatted_With_Thoughts - Branch of AA - The Kratos of Kings.md` | 284 | 21,461 | Pending |
| `Formatted_With_Thoughts - The Kratos of Kings.md` | 263 | 20,182 | Pending |
| `Formatted_With_Thoughts - The _Titanus gojira_.md` | 276 | 21,100 | Pending |
| `Formatted_With_Thoughts - Branch of The _Titanus gojira_.md` | 263 | 19,655 | Pending |
| `Formatted_With_Thoughts - The Saga of the _Titanus gojira_.md` | 300 | 22,742 | Pending |
| `Formatted_With_Thoughts - The Eclipse of the ATM AU I.md` | 260 | 19,652 | Pending |
| `Formatted_With_Thoughts - The Eclipse of the ATM AU II.md` | 245 | 18,315 | **IN PROGRESS** |
| `Formatted_With_Thoughts - The Antitheriomorphosis - Standing Hierarchy.md` | 294 | 21,709 | Pending |

**Total:** 2,529 prompts, ~192,000 lines, ~18 MB

### File Structure

Each source file follows this pattern:

```markdown
# Conversation: [Title]

## User

[User's input - PRESERVE EXACTLY]

> [Gemini's internal thoughts - STRIP THESE]
> [More thoughts in blockquotes - STRIP]

---

## Model

[Gemini's response - CLEAN UP]

## Section Header

[Content organized by headers]

### Subsection Header

[More detailed content - THIS IS THE EXTRACTION UNIT]

---

## User

[Next prompt...]
```

### Key Parsing Rules

1. **Prompt Delimiter:** `## User` marks start of a new prompt
2. **Model Response:** `## Model` marks start of Gemini's response
3. **Thoughts to Strip:** Lines starting with `> ` within Model sections are internal thoughts - REMOVE THEM
4. **Section Boundaries:** Use `###` headers as topic extraction units; fall back to `##` if no `###` exists
5. **Horizontal Rules:** `---` are separators, not content

---

## 3. Branch Genealogy

### Critical Finding

**All 9 files share a common trunk of 198 prompts.** This means ~15,700 lines are duplicated across all files.

### Branch Tree

```
                        COMMON TRUNK (Prompts 1-198)
                        [Process ONCE from any file]
                                    |
      +-----------------------------+-----------------------------+
      |                             |                             |
   KRATOS TRUNK                TITANUS TRUNK              ECLIPSE II
   (Prompts 199-213)           (Prompts 199-202)          (Diverges ~198)
   [15 shared prompts]         [4 shared prompts]         [47 unique]
      |                             |
      +--+--+                  +----+----+----+
      |  |  |                  |    |    |    |
     AA BAA TK               TG  STG  BTG  SH  EI
   [344][284][263]         [276][300][263][294][260]

LEGEND:
AA  = AA - The Kratos of Kings (130 unique prompts after trunk)
BAA = Branch of AA - The Kratos of Kings (70 unique)
TK  = The Kratos of Kings (49 unique)
TG  = The _Titanus gojira_ (71 unique)
STG = The Saga of the _Titanus gojira_ (95 unique)
BTG = Branch of The _Titanus gojira_ (58 unique)
SH  = The Antitheriomorphosis - Standing Hierarchy (86 unique)
EI  = The Eclipse of the ATM AU I (46 unique)
EII = The Eclipse of the ATM AU II (47 unique)
```

### Deduplication Strategy

1. **Process common trunk ONCE** (from Eclipse II, the pilot file)
2. **Process Kratos trunk extension** (prompts 199-213) from AA file
3. **Process Titanus trunk extension** (prompts 199-202) from any Titanus file
4. **Process unique tails** of each branch

### Optimal Processing Order

1. Eclipse II (Prompts 1-245) - PILOT, covers common trunk + unique tail
2. AA - The Kratos of Kings (Prompts 214-344) - skip common trunk
3. The Saga of the _Titanus gojira_ (Prompts 203-300) - most unique content
4. Standing Hierarchy (Prompts 203-294)
5. Branch of AA (Prompts 214-284)
6. The _Titanus gojira_ (Prompts 203-276)
7. Eclipse I (Prompts 214-260)
8. Branch of Titanus gojira (Prompts 203-263)
9. The Kratos of Kings (Prompts 214-263)

---

## 4. Output Specifications

### Output Directory
```
C:\Users\Xavier\Desktop\Personal\Vaults\X-Writing\Writing\ATM\70 Extracted\
```

### File Naming Convention

```
[Topic Title] ([Source]-P[NNN]).md
```

**Rules:**
- Topic title: Max 60 characters, truncate if longer
- Source abbreviation: `Eclipse-II`, `AA-Kratos`, `Saga-TG`, etc.
- Prompt number: 3-digit zero-padded (P001, P042, P198)

**Examples:**
- `Kratos Core Metaphor - The Ruler (Eclipse-II-P005).md`
- `Aura Irrepressibility and Thresholds (Eclipse-II-P002).md`
- `Godzilla Combat Style - Judo Influence (AA-Kratos-P220).md`

### Source Abbreviations

| Full Name | Abbreviation |
|-----------|--------------|
| The Eclipse of the ATM AU II | `Eclipse-II` |
| The Eclipse of the ATM AU I | `Eclipse-I` |
| AA - The Kratos of Kings | `AA-Kratos` |
| Branch of AA - The Kratos of Kings | `BAA-Kratos` |
| The Kratos of Kings | `Kratos` |
| The _Titanus gojira_ | `TG` |
| Branch of The _Titanus gojira_ | `BTG` |
| The Saga of the _Titanus gojira_ | `Saga-TG` |
| The Antitheriomorphosis - Standing Hierarchy | `Standing` |

### File Format (Full Specification)

```markdown
---
source: [Source-Abbreviation]-P[NNN]
lines: [start]-[end]
prompt: [N]
extracted: [YYYY-MM-DD]
category: [suggested category or "Uncategorized"]
entities: [list of detected entities]
evolution_chain: [list of related topic files if detected]
related: [list of related topics if detected]
status: [extracted | validated | linked]
---

# [Full Topic Title]

> **Source:** `[Full Source Filename]` — Prompt [N] (Lines [start]-[end])

## Your Notes

[User's original input that relates to this topic - PRESERVE EXACT PHRASING]

## Analysis

[Model's response for this section - cleaned, thoughts stripped]

## Detected Entities

- **Characters:** [list]
- **Concepts:** [list]
- **Locations:** [list]

---
^extract-[short-kebab-case-id]
```

### Block ID Format

```
^extract-[topic-keyword]-p[nnn]
```

**Examples:**
- `^extract-kratos-metaphor-p005`
- `^extract-aura-irrepressible-p002`

### Metadata Files

| File | Purpose |
|------|---------|
| `_MANIFESTO.md` | This file - workflow documentation |
| `_Branch_Map.md` | Branch genealogy visualization |
| `_Index.md` | Master topic inventory with links |
| `_Contradictions.md` | Flagged contradictions for review |
| `_Progress.md` | Extraction progress tracking |
| `_QA_Report.md` | Quality assurance findings |
| `_Entity_Registry.md` | All detected entities across files |

---

## 5. Agent Architecture

### Agent Roster

```
┌──────────────────────────────────────────────────────────────────────────┐
│                          ORCHESTRATOR (Claude)                           │
│  • Coordinates all agents                                                │
│  • Tracks progress                                                       │
│  • Handles errors and edge cases                                         │
│  • Updates _Progress.md                                                  │
└──────────────────────────────────────────────────────────────────────────┘
                                    │
    ┌───────────────┬───────────────┼───────────────┬───────────────┐
    ▼               ▼               ▼               ▼               ▼
┌─────────┐   ┌───────────┐   ┌───────────┐   ┌───────────┐   ┌─────────┐
│  SCOUT  │   │ EXTRACTOR │   │ VALIDATOR │   │  LINKER   │   │ INDEXER │
└─────────┘   └───────────┘   └───────────┘   └───────────┘   └─────────┘
                    │
    ┌───────────────┼───────────────┐
    ▼               ▼               ▼
┌───────────┐ ┌───────────┐   ┌───────────┐
│CHRONICLER │ │    QA     │   │  WRITER   │
└───────────┘ └───────────┘   └───────────┘
```

### Agent Specifications

#### SCOUT Agent
**Purpose:** Analyze source files and map branch genealogy
**Input:** Source file paths
**Output:** `_Branch_Map.md`, divergence point data
**When to Use:** At project start, or when new source files are added
**Status:** COMPLETED

#### EXTRACTOR Agent
**Purpose:** Parse chunks of prompts and extract discrete topics
**Input:**
- Source file path
- Start line number
- End line number (or prompt count)
- Chunk identifier
**Output:** Individual topic markdown files
**Chunk Size:** 5-10 prompts per chunk recommended
**Key Responsibilities:**
1. Read the specified chunk
2. Parse into User/Model pairs
3. Strip Gemini thoughts (blockquotes)
4. Identify `###` headers as topic boundaries
5. Extract each topic to its own file
6. Apply file format specification
7. Generate unique block IDs

**Prompt Template for Extractor:**
```
You are an Extractor agent. Process prompts [X] through [Y] from [Source File].

Source: [full path]
Output directory: C:\Users\Xavier\Desktop\Personal\Vaults\X-Writing\Writing\ATM\70 Extracted\
Start line: [N]
Approximate end line: [M]

Follow the extraction rules in the manifesto:
1. Strip lines starting with "> " (Gemini thoughts)
2. Use ### headers as topic boundaries
3. Preserve User's exact phrasing in "Your Notes"
4. Clean Model's response in "Analysis"
5. Use naming convention: [Topic] ([Source-Abbrev]-P[NNN]).md
6. Include YAML frontmatter
7. Add block ID: ^extract-[keyword]-p[nnn]

Report: files created, any issues encountered.
```

#### VALIDATOR Agent
**Purpose:** Detect contradictions across extracted files
**Input:** All extracted files for a given entity/topic
**Output:** Entries in `_Contradictions.md`
**When to Run:** After extraction batches complete
**Key Responsibilities:**
1. Group files by topic/entity
2. Compare statements about same subject
3. Identify conflicts (different values, opposing claims)
4. Rate severity (minor inconsistency vs major contradiction)
5. Log to `_Contradictions.md` with file references

**Contradiction Format:**
```markdown
## [Topic/Entity Name]

**Files Involved:**
- [[File A (Source-P001)]]
- [[File B (Source-P150)]]

**Conflict:**
- File A states: "[quote]"
- File B states: "[quote]"

**Severity:** [Minor | Moderate | Major]
**Resolution:** [Pending user review]

---
```

#### LINKER Agent
**Purpose:** Detect entity mentions and add cross-references
**Input:** All extracted files
**Output:** Updated files with `[[wikilinks]]`, updated `related` metadata
**When to Run:** After extraction complete, before final indexing
**Key Responsibilities:**
1. Scan file content for known entity names
2. Add `[[wikilinks]]` where appropriate
3. Update `entities` field in frontmatter
4. Update `related` field with connected topics
5. Avoid over-linking (don't link every mention)

**Linking Rules:**
- Link first mention of an entity per file
- Don't link within headers
- Don't link within the entity's own file
- Prioritize linking to existing ATM vault files when they exist

#### CHRONICLER Agent
**Purpose:** Track topic evolution across prompts
**Input:** All extracted files grouped by topic
**Output:** Updated `evolution_chain` metadata, evolution summary
**When to Run:** After extraction, alongside or after Linker
**Key Responsibilities:**
1. Identify files discussing the same concept
2. Determine chronological order (by prompt number)
3. Identify which version is "latest/canonical"
4. Update `evolution_chain` in frontmatter
5. Add notes about what changed between versions

#### INDEXER Agent
**Purpose:** Build master topic inventory
**Input:** All extracted files
**Output:** `_Index.md`
**When to Run:** After all other agents complete
**Key Responsibilities:**
1. Catalog all extracted files
2. Group by category (Power Systems, Characters, Lore, etc.)
3. Count topics per category
4. Create navigable index with links
5. Note files needing review (contradictions, incomplete)

**Index Format:**
```markdown
# ATM Extraction Index

> Generated: [date]
> Total Files: [N]
> Categories: [N]

## By Category

### Power Systems ([N] files)
- [[Kratos Overall Impression (Eclipse-II-P001)]]
- [[Aura Mechanics (Eclipse-II-P002)]]
- ...

### Characters ([N] files)
- [[Godzilla Combat Style (AA-Kratos-P220)]]
- ...

## Needs Review
- [[File with contradiction]]
- [[Incomplete extraction]]
```

#### QA Agent
**Purpose:** Validate extraction quality
**Input:** All extracted files
**Output:** `_QA_Report.md`
**When to Run:** After extraction batches, before final delivery
**Key Responsibilities:**
1. Verify each file has both "Your Notes" and "Analysis" sections
2. Check for empty or very short sections (<50 chars)
3. Verify frontmatter is complete
4. Check block IDs are unique
5. Flag malformed files

---

## 6. Extraction Workflow

### Phase 1: Scout (COMPLETED)
```
1. Analyze all 9 source files
2. Map branch genealogy
3. Identify common trunk (Prompts 1-198)
4. Determine divergence points
5. Output: _Branch_Map.md
```

### Phase 2: Extract
```
For each source file (in optimal order):
    1. Determine start prompt (skip common trunk if already processed)
    2. Divide remaining prompts into chunks of 5-10
    3. For each chunk:
        a. Spawn Extractor agent
        b. Process chunk
        c. Write topic files
        d. Update _Progress.md
    4. Mark file as extracted in progress tracker
```

**Chunking Guidelines:**
- 5 prompts per chunk for complex content
- 10 prompts per chunk for simpler content
- Aim for chunks that produce 20-50 files each
- Don't split a prompt across chunks

### Phase 3: Validate
```
1. Group extracted files by topic/entity
2. Spawn Validator agent
3. Compare files for contradictions
4. Output findings to _Contradictions.md
5. Mark files with contradiction flags in frontmatter
```

### Phase 4: Link
```
1. Load entity registry
2. Spawn Linker agent
3. Scan all files for entity mentions
4. Add [[wikilinks]]
5. Update frontmatter metadata
```

### Phase 5: Chronicle
```
1. Group files by topic
2. Spawn Chronicler agent
3. Determine evolution chains
4. Update frontmatter with evolution_chain
5. Identify canonical versions
```

### Phase 6: Index
```
1. Spawn Indexer agent
2. Catalog all extracted files
3. Group by category
4. Generate _Index.md
```

### Phase 7: QA
```
1. Spawn QA agent
2. Validate all files
3. Generate _QA_Report.md
4. Flag issues for human review
```

---

## 7. Quality Standards

### Extraction Quality Checklist

- [ ] User's phrasing preserved exactly (no paraphrasing)
- [ ] Gemini thoughts (blockquotes) fully stripped
- [ ] Topic title accurately reflects content
- [ ] Source reference is correct (file, prompt, lines)
- [ ] YAML frontmatter is complete
- [ ] Block ID is unique and follows convention
- [ ] "Your Notes" section is not empty
- [ ] "Analysis" section is not empty
- [ ] File naming follows convention

### Contradiction Severity Levels

| Level | Definition | Example |
|-------|------------|---------|
| Minor | Phrasing difference, same meaning | "25 meters" vs "approximately 25m" |
| Moderate | Different details, potentially reconcilable | Different timeline dates |
| Major | Directly opposing claims | "X can do Y" vs "X cannot do Y" |

### What NOT to Extract

- Pure pleasantries ("Great question!", "Thanks!")
- Repetitive acknowledgments
- Off-topic tangents
- Gemini's internal reasoning (thoughts in blockquotes)
- Formatting artifacts

### Merge vs Split Guidelines

**Merge into parent section if:**
- Subsection is <3 sentences
- Subsection has no distinct topic identity
- Subsection is just an example of parent topic

**Split into separate files if:**
- Subsection has its own `###` header
- Subsection discusses a distinct concept
- Subsection could stand alone as reference material

---

## 8. Known Entities

### Characters (Titans)

| Name      | Aliases                    | Notes                                        |
| --------- | -------------------------- | -------------------------------------------- |
| Godzilla  | Godric, Godzilla, The King | Main protagonist, Northern Gojira            |
| Mothra    | Maria                      | Queen of the Monsters, Divine Moth           |
| Battra    | -                          | Dark counterpart to Mothra, Cosmic Architect |
| Ghidorah  | King Ghidorah              | Three-headed dragon, antagonist              |
| Kong      | -                          | King of Hollow Earth                         |
| Rodan     | -                          | Fire demon, aerial titan                     |
| Scylla    | -                          | Cardinal Warden, ice wielder                 |
| Dagon     | -                          | Godzilla's father, Northern Patriarch        |
| Biollante | -                          | Rose of the North                            |
| Baragon   | -                          | Liminal Sentinel                             |
| Junior    | -                          | Godzilla's son                               |
| Leo       | -                          | Godzilla's son (twin of Junior)              |

### Characters (Humans)

| Name | Role |
|------|------|
| Madison Russell | Monarch personnel |
| Mark Russell | Monarch personnel |
| Various Monarch staff | See character files |

### Power Systems

| System | Core Principle | Key Terms |
|--------|----------------|-----------|
| Krátos | "What exists through will" - Ontological | Kráton, Koinon, Krator, Manifestation, Aura, Coating, Themelion, Horme, Symphonia |
| Psionics | "What is felt through emotion" - Aesthetical | Telepathy, emotional resonance |
| Magic | "What is known through logic" - Epistemological | Spells, incantations, Primus |

### Krátos-Specific Terms

| Term | Definition |
|------|------------|
| Kráton | A wielder of Krátos |
| Koinon | "Commoner" - inherits power stably via Themelion |
| Krator | "Conqueror" - achieves power through Horme alignment |
| Manifestation | The specific phenomenon a Kráton wields |
| Themelion | Will + Resolve (Koinon's stable foundation) |
| Horme | Desire (Krator's driving force) |
| Symphonia | Alignment (Krator's ideal state) |
| Diaphonia | Misalignment (Krator's weakened state) |
| Lanthaneia | Latency (Krator's dormant state) |
| Kataklisis | Repose (Krator's rest state) |
| Aura | Passive emission of Manifestation |
| Coating (Epichrisis) | Sheathing oneself/objects with Aura |
| Flaring | Intensifying Aura effects |
| Expansion | Enlarging Aura radius |
| Suppression | Minimizing Aura effects |

### Species

| Species | Notable Members |
|---------|-----------------|
| Titanus gojira | Godzilla, Dagon, Junior, Leo |
| Titanus mosura | Mothra, Battra |
| Titanus ghidorah | King Ghidorah |
| Titanus kong | Kong |
| Titanus scylla | Scylla |

### Locations

| Location | Description |
|----------|-------------|
| Hollow Earth | Subterranean realm, Kong's domain |
| Castle Bravo | Monarch facility |
| Monster Island | Titan sanctuary |

---

## 9. Progress Tracking

### Progress File Location
```
C:\Users\Xavier\Desktop\Personal\Vaults\X-Writing\Writing\ATM\70 Extracted\_Progress.md
```

### Progress Format

```markdown
# Extraction Progress

> Last Updated: [timestamp]

## Overall Status

| Metric | Value |
|--------|-------|
| Files Processed | X / 9 |
| Prompts Extracted | X / 2529 |
| Topics Generated | X |
| Contradictions Found | X |

## File Status

| File | Status | Prompts Done | Last Chunk | Notes |
|------|--------|--------------|------------|-------|
| Eclipse II | In Progress | 5/245 | Chunk 1 | Pilot file |
| AA-Kratos | Pending | 0/344 | - | - |
| ... | ... | ... | ... | ... |

## Recent Activity

- [timestamp] Extracted Eclipse II Chunk 1 (P001-P005): 26 files
- [timestamp] Created _Branch_Map.md
- ...

## Next Steps

1. Continue Eclipse II extraction (Chunk 2: P006-P010)
2. ...
```

### Resume Procedure

When resuming work:

1. **Read this manifesto** completely
2. **Check `_Progress.md`** for current status
3. **Identify next chunk** to process
4. **Spawn appropriate agent** with correct parameters
5. **Update `_Progress.md`** after each chunk

### Checkpoint System

After each chunk:
1. Verify files were created successfully
2. Update `_Progress.md` with:
   - Files created
   - Prompts processed
   - Any issues encountered
3. Commit checkpoint before proceeding

---

## 10. File Templates

### Topic File Template

```markdown
---
source: [Source-Abbrev]-P[NNN]
lines: [start]-[end]
prompt: [N]
extracted: [YYYY-MM-DD]
category: Uncategorized
entities: []
evolution_chain: []
related: []
status: extracted
---

# [Topic Title]

> **Source:** `[Full Filename]` — Prompt [N] (Lines [start]-[end])

## Your Notes

[Exact user input for this topic]

## Analysis

[Cleaned model response]

## Detected Entities

- **Characters:**
- **Concepts:**
- **Locations:**

---
^extract-[keyword]-p[nnn]
```

### Contradiction Entry Template

```markdown
## [Topic/Entity]: [Brief Description]

**Detected:** [date]
**Severity:** [Minor | Moderate | Major]
**Status:** Pending Review

### Files Involved

1. [[File A (Source-P001)]]
2. [[File B (Source-P150)]]

### Conflicting Statements

**From File A:**
> "[exact quote]"

**From File B:**
> "[exact quote]"

### Context

[Brief explanation of why this is a contradiction]

### Suggested Resolution

[If obvious, suggest which version is likely correct; otherwise "Requires author decision"]

---
```

### Index Section Template

```markdown
## [Category Name] ([N] files)

| Topic | Source | Prompt | Status |
|-------|--------|--------|--------|
| [[Topic Title (Source-P001)]] | Eclipse-II | 1 | Extracted |
| ... | ... | ... | ... |
```

---

## 11. Troubleshooting

### Common Issues

#### Issue: Empty "Your Notes" section
**Cause:** User prompt was very short or just a continuation marker
**Solution:** Merge with previous prompt's context or note as "continuation"

#### Issue: Very long topic (>500 lines)
**Cause:** Model gave extensive response without subheaders
**Solution:** Split manually by logical topic breaks, or keep as single file with note

#### Issue: No `###` headers in Model response
**Cause:** Model gave unstructured response
**Solution:** Use `##` headers as boundaries; if none, treat entire response as one topic

#### Issue: Duplicate topic titles
**Cause:** Same topic discussed in multiple prompts
**Solution:** The `(Source-PNNN)` suffix ensures uniqueness; this is expected behavior

#### Issue: Blockquotes that aren't Gemini thoughts
**Cause:** User or Model used blockquotes for other purposes (quotes, emphasis)
**Solution:** Check context - if it's within Model section AND looks like internal reasoning, strip it; otherwise preserve

#### Issue: Prompt spans page boundary in source
**Cause:** Very long user input
**Solution:** Ensure entire User section (from `## User` to next `## Model`) is captured

### Error Recovery

If extraction fails mid-chunk:
1. Check `_Progress.md` for last successful checkpoint
2. Identify which files were created
3. Resume from the prompt after the last successfully extracted one
4. Note the gap in progress log

### Validation Failures

If QA agent finds issues:
1. Check `_QA_Report.md` for specifics
2. Re-extract affected files if fixable
3. Flag for human review if ambiguous

---

## Appendix: Quick Reference

### Command Snippets

**Count prompts in a file:**
```bash
grep -c "^## User$" "[filepath]"
```

**Find line numbers of User markers:**
```bash
grep -n "^## User$" "[filepath]"
```

**Count extracted files:**
```bash
ls -1 "C:/Users/Xavier/Desktop/Personal/Vaults/X-Writing/Writing/ATM/70 Extracted/" | wc -l
```

### Key Paths

| Purpose | Path |
|---------|------|
| Source files | `Writing\Archive\Gemini AI Exports\Formatted\` |
| Output files | `Writing\ATM\70 Extracted\` |
| Existing ATM vault | `Writing\ATM\` |
| This manifesto | `Writing\ATM\70 Extracted\_MANIFESTO.md` |

### Agent Spawn Template

```
Task tool parameters:
- description: "[Agent Type]: [Brief task]"
- prompt: "[Detailed instructions referencing manifesto]"
- subagent_type: "general-purpose"
```

---

## Changelog

| Date | Change |
|------|--------|
| 2026-01-03 | Initial manifesto created |
| 2026-01-03 | Branch analysis completed |
| 2026-01-03 | Pilot extraction started (Eclipse II, Chunk 1) |

---

*End of Manifesto*
