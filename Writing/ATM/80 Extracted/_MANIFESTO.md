# ATM Gemini Export Manifesto

> **Purpose:** This document provides comprehensive documentation for the ATM extraction project and content processing workflow.
> **Status:** EXTRACTION COMPLETE | CONTENT PROCESSING ACTIVE

> **Last Updated:** 2026-01-16
> **Created By:** Claude Opus 4.5
> **Quick Reference:** [[CLAUDE]] (for working document)

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [Source Material](#2-source-material)
3. [Branch Genealogy](#3-branch-genealogy)
4. [Output Specifications](#4-output-specifications)
5. [Agent Architecture](#5-agent-architecture)
6. [Extraction Workflow](#6-extraction-workflow) *(COMPLETE)*
7. [Quality Standards](#7-quality-standards)
8. [Known Entities](#8-known-entities)
9. [Progress Tracking](#9-progress-tracking)
10. [File Templates](#10-file-templates)
11. [Troubleshooting](#11-troubleshooting)
12. [Content Processing Roadmap](#12-content-processing-roadmap) *(CURRENT PHASE)*

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

| File | Abbrev | Prompts | Files | Status |
|------|--------|---------|-------|--------|
| `Formatted_With_Thoughts - The Eclipse of the ATM AU II.md` | Eclipse-II | 245 | 208 | **COMPLETE** |
| `Formatted_With_Thoughts - AA - The Kratos of Kings.md` | AA-Kratos | 344 | 142 | **COMPLETE** |
| `Formatted_With_Thoughts - The Saga of the _Titanus gojira_.md` | Saga-TG | 300 | 88 | **COMPLETE** (repaired) |
| `Formatted_With_Thoughts - The Antitheriomorphosis - Standing Hierarchy.md` | Standing | 294 | 89 | **COMPLETE** (repaired) |
| `Formatted_With_Thoughts - Branch of AA - The Kratos of Kings.md` | BAA-Kratos | 284 | 86 | **COMPLETE** (repaired) |
| `Formatted_With_Thoughts - The _Titanus gojira_.md` | TG | 276 | 71 | **COMPLETE** (repaired) |
| `Formatted_With_Thoughts - The Kratos of Kings.md` | Kratos | 263 | 66 | **COMPLETE** |
| `Formatted_With_Thoughts - Branch of The _Titanus gojira_.md` | BTG | 263 | 62 | **COMPLETE** |
| `Formatted_With_Thoughts - The Eclipse of the ATM AU I.md` | Eclipse-I | 260 | 61 | **COMPLETE** |

**Totals:** 2,529 prompts processed → 873 active topic files (36 archived duplicates)

**Repairs Completed (2026-01-15):**
- Saga-TG: 34 files re-extracted (P233-P266)
- TG: 7 files re-extracted (P230-P236)
- Standing: 1 file re-extracted (P230)
- BAA-Kratos: 86 files re-extracted (P199-P284)

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
C:\Users\Xavier\Desktop\Personal\Vaults\X-Writing\Writing\ATM\80 Extracted\
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

> **Status:** Extraction agents COMPLETE. Content processing agents now active.

### Extraction Agent Roster (HISTORICAL)

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
Output directory: C:\Users\Xavier\Desktop\Personal\Vaults\X-Writing\Writing\ATM\80 Extracted\
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

### Content Processing Agent Roster (CURRENT)

#### SYNTHESIZER Agent
**Purpose:** Merge related topic files into unified reference documents
**Input:** Topic files grouped by subject (e.g., all Kratos files)
**Output:** Comprehensive lore documents in `Writing/ATM/30 Lore/`
**Key Responsibilities:**
1. Identify all files related to a topic via [[_Evolution_Chronicles]]
2. Determine canonical version vs superseded versions
3. Synthesize into coherent reference document
4. Preserve source citations for traceability
5. Resolve any minor inconsistencies during merge

#### PROFILER Agent
**Purpose:** Build comprehensive character profiles from scattered topic files
**Input:** All files mentioning a specific character
**Output:** Character profile documents in `Writing/ATM/20 Characters/`
**Key Responsibilities:**
1. Search [[_Entity_Registry]] for all character mentions
2. Gather physical descriptions, abilities, relationships, arcs
3. Organize chronologically by narrative timeline
4. Flag any unresolved character contradictions
5. Create navigable profile with section links

#### TIMELINE Agent
**Purpose:** Build master chronological timeline from extracted content
**Input:** All topic files with temporal references
**Output:** Timeline documents in `Writing/ATM/10 Timeline/`
**Key Responsibilities:**
1. Extract all date/era references from topic files
2. Organize into coherent timeline (Prehistoric → Modern → Future)
3. Cross-reference character arcs with events
4. Identify any timeline inconsistencies
5. Create navigable timeline with era sections

---

## 6. Extraction Workflow

> **Status:** ALL PHASES COMPLETE (2026-01-15)

### Phase 1: Scout ✓
Analyzed all 9 source files, mapped branch genealogy, identified common trunk (P001-P198).
**Output:** `_Branch_Map.md`

### Phase 2: Extract ✓
Extracted all 9 sources with chunk-based processing. 909 raw topic files generated.
**Completed:** 2026-01-08

### Phase 3: Validate ✓
Detected contradictions across sources. 3 contradictions flagged.
**Output:** `_Contradictions.md`

### Phase 4: Link ✓
Entity mentions detected and catalogued.
**Output:** `_Entity_Registry.md`

### Phase 5: Chronicle ✓
Topic evolution chains identified across sources. 16 major chains documented.
**Output:** `_Evolution_Chronicles.md`

### Phase 6: Index ✓
All files catalogued with source-specific indexes.
**Output:** `_Index.md` + 9 source indexes

### Phase 7: QA ✓
File format validation complete.
**Output:** `_QA_Report.md`

### Phase 8: Integrity Audit & Repairs ✓
**Completed:** 2026-01-15

4 sources required repairs due to extraction misalignment:
| Source | Issue | Files Repaired |
|--------|-------|----------------|
| Saga-TG | Off-by-21 error (P233-P266) | 34 |
| TG | Off-by-3 error (P230-P236) | 7 |
| Standing | Single file misalignment (P230) | 1 |
| BAA-Kratos | Chaotic extraction | 86 |

**Total:** 128 files re-extracted

### Phase 9: Duplicate Detection & Archival ✓
**Completed:** 2026-01-15

- 32 duplicate clusters identified
- 36 files archived to `_Duplicates_Archive/`
- See [[_Duplicates]] for full analysis

### Phase 10: Contradiction Resolution ✓
**Completed:** 2026-01-15

All 3 flagged contradictions resolved:
1. Dagon's Age Math → Resolved via Gojira Growth Rate system (P237)
2. Dagon + Godzilla Duration → Approximations within tolerance
3. San's Head Mexico 2019 → Naming convention clarification (Godzilla=Titan, Godric=human)

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

> **Live Data:** See [[_Entity_Registry]] for the complete, current entity catalog with cross-references.

### Quick Reference: Key Characters

| Titan Form | Human Form | Role |
|------------|------------|------|
| Godzilla | Godric Nordson | Main protagonist, King of the Monsters |
| Mothra | Maria Lepidiel | Queen of the Monsters, Divine Moth |
| Battra | - | Lord of Mystic Arts, Cosmic Architect |
| King Ghidorah | Ichi/Arthur (vessel) | Former antagonist, blood-vowed ally |
| Dagon | - | Godzilla's father, Northern Patriarch |

### Quick Reference: Power Systems

| System | Philosophy | Core Concept |
|--------|------------|--------------|
| Krátos | "What exists through will" | Ontological - being over doing |
| Psionics | "What is felt through emotion" | Aesthetical - emotional resonance |
| Magic | "What is known through logic" | Epistemological - knowledge-based |

### Naming Convention

**Critical for timeline references:**
- **Titan name** (Godzilla, Mothra) = Titan form / pre-2020 events
- **Human name** (Godric, Maria) = Human form / post-Antitheriomorphosis

See [[_Evolution_Chronicles]] for how concepts evolved across sources.

---

## 9. Progress Tracking

> **Live Data:** See [[_Progress]] for current project status.

### Current Status Summary

| Metric | Value |
|--------|-------|
| Sources Processed | 9 / 9 |
| Active Topic Files | 873 |
| Archived Duplicates | 36 |
| Contradictions | 0 (3 resolved) |
| Quality Score | 96/100 |

### Key Metadata Files

| File | Purpose |
|------|---------|
| [[_Progress]] | Overall project status and file counts |
| [[_Index]] | Master topic inventory |
| [[_Contradictions]] | Worldbuilding contradictions (all resolved) |
| [[_Duplicates]] | Duplicate cluster analysis |
| [[_Entity_Registry]] | Named entities cross-references |
| [[_Evolution_Chronicles]] | Topic evolution chains |
| [[_QA_Report]] | Quality assurance results |

### Resume Procedure (For Content Processing)

When continuing work:

1. **Read [[CLAUDE]]** for quick reference
2. **Check [[_Progress]]** for current phase
3. **Review [[_Evolution_Chronicles]]** to understand topic relationships
4. **Use [[_Entity_Registry]]** to find character/concept mentions

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

## 12. Content Processing Roadmap

> **Current Phase:** Content Processing (Extraction Complete)

With 873 topic files extracted and validated, the corpus is ready for content processing. Four phases are available:

### Phase A: Query & Explore (ACTIVE)

Use the corpus as a knowledge base to answer questions about the ATM universe:
- Search for specific lore details on demand
- Find character information across sources
- Look up power system mechanics
- Navigate via [[_Entity_Registry]] and [[_Evolution_Chronicles]]

**No file creation needed** - navigation and retrieval only.

### Phase B: Synthesize Lore Docs

Merge related topics into unified reference documents:

| Target Document | Source Evolution Chain | Output Location |
|-----------------|------------------------|-----------------|
| Complete Kratos Power System Guide | [[_Evolution_Chronicles#Kratos Power System]] | `Writing/ATM/30 Lore/` |
| Atomic Amplification Arsenal Reference | [[_Evolution_Chronicles#Atomic Amplification]] | `Writing/ATM/30 Lore/` |
| Ghidorah Abilities Compendium | [[_Evolution_Chronicles#Ghidorah/Ichi Development]] | `Writing/ATM/30 Lore/` |
| Titan Species Encyclopedia | Multiple chains | `Writing/ATM/30 Lore/` |

**Agent:** SYNTHESIZER

### Phase C: Build Character Profiles

Compile scattered character information into comprehensive profiles:

| Priority | Characters | Notes |
|----------|------------|-------|
| High | Godric/Godzilla | Most content (~200 mentions) |
| High | Maria/Mothra | Divine Moth arsenal, relationship dynamics |
| High | Dagon | Origin story, Burning Form connection |
| Medium | Ichi/Ni/San | Ghidorah heads, Arthur symbiosis |
| Medium | Nordson children | Junior, Leo, Lora abilities and arcs |
| Supporting | Scylla, Rodan, Anguirus, Kong | Secondary characters |

**Agent:** PROFILER
**Output Location:** `Writing/ATM/20 Characters/` or similar

### Phase D: Create Timeline

Extract chronological references and build master timeline:

| Era | Coverage | Key Events |
|-----|----------|------------|
| Prehistoric | Dagon, Astraea, young Godric | Origin stories, Fallen Star tradition |
| Dormancy | - | Gap period |
| Modern (2014-2024) | Film adaptations | KOTM 2019, GvK 2021, GxK 2024 |
| Antitheriomorphosis (2020+) | Human forms | Castle Bravo, Meadowvale |
| Future Arcs | Planned content | Character development trajectories |

**Agent:** TIMELINE
**Output Location:** `Writing/ATM/10 Timeline/` or similar

### Suggested Processing Order

1. Query & Explore as needed (immediate, ongoing)
2. Character profiles (most requested content type)
3. Lore synthesis (builds on profiles)
4. Timeline (requires cross-referencing)

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
ls -1 "C:/Users/Xavier/Desktop/Personal/Vaults/X-Writing/Writing/ATM/80 Extracted/" | wc -l
```

### Key Paths

| Purpose | Path |
|---------|------|
| Source files | `Writing\Archive\Gemini AI Exports\Formatted\` |
| Output files | `Writing\ATM\80 Extracted\` |
| Existing ATM vault | `Writing\ATM\` |
| This manifesto | `Writing\ATM\80 Extracted\_MANIFESTO.md` |

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
| 2026-01-05 | Eclipse-II extraction complete (208 files) |
| 2026-01-06 | AA-Kratos extraction complete (146 files) |
| 2026-01-07 | Title standardization complete |
| 2026-01-08 | All 9 sources extracted (909 raw files) |
| 2026-01-15 | Source integrity audit complete |
| 2026-01-15 | Saga-TG repaired (34 files re-extracted) |
| 2026-01-15 | TG repaired (7 files re-extracted) |
| 2026-01-15 | Standing repaired (1 file re-extracted) |
| 2026-01-15 | BAA-Kratos repaired (86 files re-extracted) |
| 2026-01-15 | Duplicate detection complete (32 clusters) |
| 2026-01-15 | Duplicate archival complete (36 files) |
| 2026-01-15 | Contradiction resolution complete (3 resolved) |
| 2026-01-15 | All metadata files synchronized |
| 2026-01-16 | CLAUDE.md updated for content processing |
| 2026-01-16 | Manifesto comprehensive update (this revision) |
| 2026-01-16 | `_Topic_Evolution_Report.md` archived |
| 2026-01-16 | `_Session.md` deleted (obsolete) |

---

*End of Manifesto - Extraction Phase Complete*
*Content Processing Phase Active*
