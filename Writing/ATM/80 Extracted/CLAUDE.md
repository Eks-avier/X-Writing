# ATM Corpus Reference

> **Purpose:** Quick reference for Claude instances working with the ATM extracted corpus.
> **Project:** Monsterverse AU worldbuilding - 12 Gemini conversation exports converted to Obsidian knowledge base.
> **Full Documentation:** [[_MANIFESTO]]

---

## Project Status

| Phase | Status |
|-------|--------|
| **Extraction** | COMPLETE |
| **Duplicate Archival** | COMPLETE |
| **Contradiction Resolution** | COMPLETE |
| **Current Phase** | Content Processing |

**Quality Score:** 96/100

---

## Corpus Overview

The ATM corpus contains **1,158 active topic files** extracted from 12 Gemini AI conversation exports. All sources share a common trunk (P001-P198 in Eclipse-II); branches diverge at P199 with unique content.

For current statistics, see: [[_Progress]]

### Source Reference

| Abbreviation | Full Name | Active Files |
|--------------|-----------|--------------|
| Eclipse-II | The Eclipse of the ATM AU II | 183 |
| AA-Kratos | AA - The Kratos of Kings | 142 |
| KOTM | The Antitheriomorphosis - KOTM Rewrite | 131 |
| Saga-TG | The Saga of the Titanus gojira | 100 |
| BSaga-TG | Branch of Saga of Titanus gojira | 99 |
| Standing | Standing Hierarchy | 89 |
| BAA-Kratos | Branch of AA - Kratos | 86 |
| Pacific | The Antitheriomorphosis AU | 79 |
| TG | The Titanus gojira | 70 |
| Kratos | The Kratos of Kings | 64 |
| Eclipse-I | Eclipse of ATM AU I | 62 |
| BTG | Branch of Titanus gojira | 53 |

---

## Live Metadata (Wikilinks)

These files contain current project state - reference them directly rather than duplicating content:

| File | Purpose |
|------|---------|
| [[_Progress]] | Current status, file counts, completed phases |
| [[_Index]] | Master topic inventory with all source indexes |
| [[_Contradictions]] | Worldbuilding contradictions (3 flagged, all resolved) |
| [[_Duplicates]] | Duplicate detection analysis (36 archived) |
| [[_Entity_Registry]] | Named entities cross-referenced across sources |
| [[_Evolution_Chronicles]] | Topic evolution chains (16 major chains) |
| [[_QA_Report]] | Quality assurance validation results |

### Source-Specific Indexes

| Index | Prompts |
|-------|---------|
| [[_Index_Eclipse-II]] | P001-P245 |
| [[_Index_AA-Kratos]] | P199-P344 |
| [[_Index_KOTM]] | P199-P329 |
| [[_Index_BSaga-TG]] | P301-P399 |
| [[_Index_Saga-TG]] | P199-P300 |
| [[_Index_Standing]] | P199-P294 |
| [[_Index_BAA-Kratos]] | P199-P284 |
| [[_Index_Pacific]] | P199-P277 |
| [[_Index_TG]] | P199-P276 |
| [[_Index_Kratos]] | P199-P263 |
| [[_Index_BTG]] | P199-P263 |
| [[_Index_Eclipse-I]] | P199-P260 |

---

## Content Processing Roadmap

### Phase A: Query & Explore (Active)

Use the corpus as a knowledge base to answer questions about the ATM universe:
* Search for specific lore details on demand
* Find character information across sources
* Look up power system mechanics
* Navigate via [[_Entity_Registry]] and [[_Evolution_Chronicles]]

**No file creation needed** - navigation and retrieval only.

### Phase B: Synthesize Lore Docs

Merge related topics into unified reference documents:
* Complete Kratos Power System Guide
* Atomic Amplification Arsenal Reference
* Ghidorah Abilities Compendium
* Titan Species Encyclopedia

**Target Location:** `Writing/ATM/30 Lore/`

### Phase C: Build Character Profiles

Compile scattered character information into comprehensive profiles:
* **Priority:** Godric/Godzilla (most content), Maria/Mothra, Dagon
* **Secondary:** Ichi/Ni/San (Ghidorah heads), Nordson children
* **Supporting:** Scylla, Rodan, Anguirus, Kong

**Target Location:** `Writing/ATM/20 Characters/` or similar

### Phase D: Create Timeline (IN PROGRESS)

Extract chronological references and build master timeline:
* Era I: Prehistoric (Dagon, Astraea, young Godric)
* Era II: Dormancy Period
* Era III-VI: Modern Era (2014-2024)
* Era VII: Antitheriomorphosis (2024+)

**Target Location:** `Writing/ATM/10 Timeline/`
**Master File:** [[Master_Timeline]] (created, being populated)

---

## Creative Writing Skills

Auto-applied guidance for creative work, located in `.claude/skills/`:

| Skill | Domain | Use For |
|-------|--------|---------|
| `choreographer` | Fight scenes | Combat design, action sequences |
| `dialogue-crafter` | Character voice | Speech patterns, authenticity |
| `emotion-mapper` | Emotional beats | Reaction timing, intensity |
| `naming-consultant` | Onomancy | Character/place naming principles |
| `scene-architect` | Setting/atmosphere | Environmental description, mood |

**Usage:** These skills are automatically referenced when writing creative content.

---

## Processing Agents

Custom subagents for corpus work, defined in `.claude/agents/`:

### Corpus Processing

| Agent | Description |
|-------|-------------|
| `chronologist` | Temporal extraction, timeline building |
| `continuity-sentinel` | Contradiction detection, canon validation |
| `character-synthesizer` | Profile compilation, character data |
| `lore-compiler` | Worldbuilding documentation |
| `arc-weaver` | Narrative structure, scene inventory |
| `entity-cartographer` | Cross-referencing, relationship mapping |
| `theme-analyst` | Thematic patterns, symbolism |
| `merger` | Content integration, extracted → existing |

### Research Consultants

| Agent | Description |
|-------|-------------|
| `mythology-consultant` | Myth/folklore research (web search) |
| `science-consultant` | Science/math validation (web search) |
| `franchise-consultant` | Godzilla franchise canon (web search) |

**Usage:** Spawn via Task tool with appropriate `subagent_type`.

---

## Key Content Areas

### Power Systems

* **Kratos:** Willpower-based combat system (see [[_Evolution_Chronicles#Kratos Power System]])
* **Psionics:** Mental/spiritual powers - five disciplines
* **Magic:** Soul-based sorcery - Fourfold Doctrine
* **Atomic Amplification:** Godzilla's human-form enhancement (see [[_Evolution_Chronicles#Atomic Amplification]])

### Character Development

* **Godric-Maria Romance:** Tangible/Intangible dynamic
* **Ghidorah/Ichi Arc:** From villain to Arthur symbiosis
* **Nordson Children:** Junior, Leo, Lora hybrid abilities
* **Scylla:** Ice Weaver + Krator synthesis

### Worldbuilding

* **Standing Hierarchy:** Titan political structure
* **Burning Form:** Transformation mechanics
* **Titan Linguistics:** Language acquisition, accents
* **Naming Philosophy:** Onomancy across characters

---

## File Structure

### Topic File Format

```
PXXX - [Topic Title] (Source).md
```

### Frontmatter Fields

```yaml
source: [Source]-P[NNN]
lines: [start]-[end]
prompt: [N]
extracted: [YYYY-MM-DD]
category: [Worldbuilding|Character Development|Plot|Mechanics]
entities: []
status: extracted
```

### Sections

* **Your Notes:** User's original input (preserved verbatim)
* **Analysis:** Model's response (thoughts stripped)

---

## Navigation Tips

1. **By Entity:** Start with [[_Entity_Registry]] to find all mentions of a character/concept
2. **By Evolution:** Use [[_Evolution_Chronicles]] to trace how concepts developed
3. **By Source:** Check source-specific indexes (e.g., [[_Index_Saga-TG]]) for that conversation's topics
4. **By Category:** Files are categorized as Worldbuilding, Character Development, Plot, or Mechanics

---

## Archived Content

| Directory | Contents |
|-----------|----------|
| `_Duplicates_Archive/` | 36 duplicate files preserved by source |
| `_Archive/` | Historical metadata files (e.g., Eclipse-II evolution report) |

See [[_Duplicates]] for the complete duplicate cluster analysis.
See [[_MANIFESTO]] for detailed extraction specifications and complete changelog.

---

## Extraction Script

**Location:** `_scripts/extract_prompts.py`

Automated extraction tool for converting Gemini conversation exports to individual markdown files.

### Usage

```bash
python extract_prompts.py <source_file> <abbreviation> <output_dir> [--start N] [--end N]

# Example: Extract prompts 301-399 from BSaga-TG
python extract_prompts.py "source.md" "BSaga-TG" "./BSaga-TG" --start 301 --end 399
```

### What the Script Does

1. Parses source file, finds all `## User` boundaries
2. Extracts user content (between `## User` and `## Model`)
3. Extracts model response (stripping `> ` thought lines and `### Model's Thought Process` blocks)
4. Generates placeholder titles (first ~5 words of user content)
5. Creates proper frontmatter with line numbers
6. Writes files in standard format

### What Requires Human/AI Processing

* **Meaningful titles:** Script generates placeholders like “Its Now Time To Introduce The”
* **Categories:** Default is “Uncategorized”
* **Entities:** Default is empty `[]`
* **Empty prompts:** Usually indicate file uploads (images, attachments)

### Two-Phase Workflow

1. **Script (seconds):** Mechanical extraction - fast, consistent, no off-by-N errors
2. **Claude (valuable):** Batch-rename with meaningful titles, populate categories/entities, cross-reference

---

## Historical Reference

<details>
<summary>Extraction Phase Details (Completed 2026-01-16)</summary>

### Parsing Rules (Historical)

1. **Prompt Delimiter:** `## User` marked start of new prompt
2. **Model Response:** `## Model` marked Gemini's response
3. **Thought Stripping:** Lines starting with `> ` were internal thoughts - removed
4. **Extraction Unit:** `###` headers defined topic boundaries

### Repairs Completed

* Saga-TG: 45 files re-extracted (P233-P266, P290-P300)
* TG: 7 files re-extracted (P230-P236)
* Standing: 1 file re-extracted (P230)
* BAA-Kratos: 86 files re-extracted (P199-P284)
* BSaga-TG: 99 files extracted (P301-P399) - NEW SOURCE

Total: 139 files repaired/extracted across 5 sources.

</details>
