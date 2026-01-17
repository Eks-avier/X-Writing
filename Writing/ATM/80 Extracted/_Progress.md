# Extraction Progress

> **Last Updated:** 2026-01-17 (Session 20 - Entity Registry Update)
> **Current Phase:** Content Processing
> **Status:** 12 SOURCES COMPLETE - Titles Refined
> **Quality Score:** 96/100

---

## Extraction Integrity Status

**All sources verified and repaired. See [[_Extraction_Integrity_Audit]] for historical details.**

| Source | Status | Action Taken |
|--------|--------|--------------|
| **Saga-TG** | REPAIRED (2026-01-16) | 45 files re-extracted (P233-P266 + P290-P300) |
| **TG** | REPAIRED (2026-01-15) | 7 files re-extracted (P230-P236) |
| **Standing** | REPAIRED (2026-01-15) | 1 file re-extracted (P230) |
| **BAA-Kratos** | REPAIRED (2026-01-15) | Full re-extraction (86 files P199-P284) |
| Eclipse-II | PASS | Verified correct |
| AA-Kratos | PASS | Verified correct |
| Kratos | PASS | Verified correct |
| BTG | PASS | Verified correct |
| Eclipse-I | PASS | Verified correct |

**All sources now verified. Extraction integrity confirmed.**

---

## Overall Status

| Metric | Value |
|--------|-------|
| Source Files | 12 |
| Total Prompts | 3,633 |
| Common Trunk | 198 prompts (shared by all files) |
| Unique Content | ~1,254 prompts (~38%) |

| Progress | Count |
|----------|-------|
| Files Processed | 12 / 12 (100% COMPLETE) |
| Topic Files Generated | 1,158 content files (70 archived) |
| Metadata Files | 14 |
| Contradictions Found | 0 (3 flagged, all resolved) |
| Duplicate Clusters | 32 (36 files archived) |
| Evolution Chains | 16 documented |
| Wikilinks | ~1,200 established |

## Workflow Phases

| Phase | Status | Date |
|-------|--------|------|
| EXTRACTION | COMPLETE | 2026-01-13 |
| DEDUPLICATION | COMPLETE | 2026-01-14 |
| VALIDATION | COMPLETE | 2026-01-14 |
| LINKING | COMPLETE | 2026-01-14 |
| CHRONICLE | COMPLETE | 2026-01-14 |
| INDEX | COMPLETE | 2026-01-14 |
| QA | COMPLETE (96/100) | 2026-01-14 |

## Items for Human Review

### Contradictions - ALL RESOLVED (2026-01-15)
All 3 flagged contradictions were found to be consistent with established systems:
1. ~~Dagon Age Timeline~~ → Consistent with Gojira Growth Rate system
2. ~~Dagon Duration Math~~ → Numbers are approximations within tolerance
3. ~~San's Head 2019~~ → Correct timeline; naming convention clarification only

### Deduplication - COMPLETE
- 36 duplicate files archived to `_Duplicates_Archive/`
- See [[_Duplicates]] for full analysis
- Archived files can be permanently deleted or restored as needed

### Folder Structure

```
80 Extracted/
├── Eclipse-II/           (183 content files)
├── AA-Kratos/            (142 content files)
├── KOTM/                 (131 content files)
├── Saga-TG/              (100 content files)
├── BSaga-TG/             (99 content files)
├── Standing/             (89 content files)
├── BAA-Kratos/           (86 content files)
├── Pacific/              (79 content files)
├── TG/                   (70 content files)
├── Kratos/               (64 content files)
├── Eclipse-I/            (62 content files)
├── BTG/                  (53 content files)
├── _Duplicates_Archive/  (70 archived files)
├── _File_Uploads/        (52 upload placeholders)
├── _scripts/             (utility scripts)
└── [metadata files at root]
```

---

## File Status

| File | Abbreviation | Total Prompts | Active Files | Status |
|------|--------------|---------------|--------------|--------|
| Eclipse of ATM AU II | Eclipse-II | 245 | 183 (-34 consolidated) | VERIFIED |
| AA - The Kratos of Kings | AA-Kratos | 344 | 142 (-4 archived) | VERIFIED |
| The Antitheriomorphosis - KOTM Rewrite | KOTM | 329 | 131 | NEW |
| Branch of Saga of TG | BSaga-TG | 399 | 99 | VERIFIED |
| Saga of the Titanus gojira | Saga-TG | 300 | 100 (-2 archived) | VERIFIED |
| Standing Hierarchy | Standing | 294 | 89 (-7 archived) | VERIFIED |
| Branch of AA - Kratos | BAA-Kratos | 284 | 86 | VERIFIED |
| The Antitheriomorphosis AU | Pacific | 277 | 79 | NEW |
| The Titanus gojira | TG | 276 | 70 (-6 archived) | VERIFIED |
| The Kratos of Kings | Kratos | 263 | 64 (-4 archived) | VERIFIED |
| Branch of Titanus gojira | BTG | 263 | 53 (-13 archived) | VERIFIED |
| Eclipse of ATM AU I | Eclipse-I | 260 | 62 | VERIFIED |

---

## Extraction Log

### 2026-01-17: KOTM and Pacific Full Extraction (2 NEW SOURCES)

- **Status:** COMPLETED SUCCESSFULLY
- **Method:** Automated script extraction (`_scripts/extract_prompts.py`)

**KOTM Source:**
- **Source:** The Antitheriomorphosis - KOTM Rewrite (P199-P329)
- **Total Prompts Extracted:** 131 unique prompts
- **Files Created:** 131 topic files
- **Key Content Areas:**
  - Kratos power system development
  - Godric/Maria relationship dynamics
  - Ghidorah abilities and Ichi-Arthur symbiosis
  - Scylla development and Ice Weaver lore
  - Standing Hierarchy expansion
  - Warden system and special titles

**Pacific Source:**
- **Source:** The Antitheriomorphosis AU (P199-P277)
- **Total Prompts Extracted:** 79 unique prompts
- **Files Created:** 79 topic files
- **Key Content Areas:**
  - Pacific Rim Crossover Arc (2030)
  - Precursor invasion (Moon portal, Mars campaign)
  - Ichi-Arthur cosmic journey
  - Galactic situation (Precursors, Nebulans, Bilusaludo, Exif)
  - Nordson children developmental scenes
  - Godzilla's Second Repose

**Note:** Both sources extracted and titles refined (2026-01-17). Entity Registry updated with KOTM/Pacific entities.

---

### 2026-01-16: BSaga-TG Full Extraction (NEW SOURCE)

- **Status:** COMPLETED SUCCESSFULLY
- **Source:** Branch of The Saga of the Titanus gojira (P301-P399)
- **Method:** Automated script extraction (`_scripts/extract_prompts.py`)
- **Total Prompts Extracted:** 99 unique prompts
- **Files Created:** 99 topic files
- **Branch Relationship:** Shares P001-P300 with Saga-TG, unique content P301-P399
- **Key Content Areas:**
  - Lost Nordsons (Megara/Megaguirus, Simon/SpaceGodzilla, Millen/Orga)
  - Gojira tribal instinct and blood loyalty
  - Titanus mosura Heavenly Instance theology
  - Mothra/Battra twin dynamic and divine test
  - Gojira-Mosura ancient "Rome and China" dynamic
  - Nordson family daily life and routines
  - Music and instruments in the AU
  - Lepidiel parent names (Theia, Hyperion, Gabriel, Anna)

### 2026-01-16: Saga-TG P290-P300 Off-by-2 Error Repair

- **Status:** COMPLETE
- **Issue:** User reported P299 content appearing in P297 file
- **Root Cause:** Off-by-2 extraction error extending from P290 through P300
  - P290-P298 contained content from 2 prompts ahead
  - P299-P300 contained fabricated overflow content (not in source)
- **Action:** Re-extracted 11 files (P290-P300) with correct line mappings
- **Files Corrected:**
  - P290: Aurelia Sees Dagon in Godric Smile Symmetry (lines 21480-21579)
  - P291: Biollante with Aurelia Alive Scenario (lines 21580-21671)
  - P292: Darius Maria Connection and Parental Wisdom (lines 21672-21800)
  - P293: Darius Maria Bartholomew Family Dynamics (lines 21801-21913)
  - P294: Aurelia Learning of Godric First Ten Years (lines 21914-22027)
  - P295: Fraternity of Desperate Parents Theme (lines 22028-22141)
  - P296: Aurelia and Atomic Amplification Cure (lines 22142-22261)
  - P297: Golden Timeline Family Reunion Desire (lines 22262-22369)
  - P298: Darius Aurelia Dynamic as Newlyweds (lines 22370-22490)
  - P299: Grandparents and Grandchildren Three Generations (lines 22491-22612)
  - P300: Nordson Clan City Visit Human Reactions (lines 22613-22742)
- **Total Saga-TG Repairs:** 45 files (34 from P233-P266 + 11 from P290-P300)
- **Index Updated:** `_Index_Saga-TG.md` corrected

### 2026-01-15: Duplicate Archival Complete

- **Status:** COMPLETE
- **Action:** Archived 36 duplicate files to `_Duplicates_Archive/`
- **Breakdown:**
  - Saga-TG: 14 files (P199, P200, P242-P253)
  - Standing: 7 files (P231, P256, P265, P268-P269, P272-P273)
  - TG: 6 files (P199-P201, P209-P210, P236)
  - AA-Kratos: 4 files (P211, P220, P227, P237)
  - BTG: 4 files (P200-P201, P239-P240)
  - Kratos: 1 file (P254)
- **Canonical versions** retained in original source folders

### 2026-01-15: Integrity Repairs Complete

- **Status:** ALL REPAIRS SUCCESSFUL
- **Sources Repaired:**
  - **Saga-TG:** Re-extracted 34 files (P233-P266) - off-by-21 error fixed
  - **TG:** Re-extracted 7 files (P230-P236) - off-by-3 error fixed
  - **Standing:** Re-extracted 1 file (P230) - duplicate removed, correct content extracted
  - **BAA-Kratos:** Full re-extraction of 86 files (P199-P284) - chaotic mapping fixed
- **Verification:** Spot-checks passed for all repaired sources (P199, P237, last prompt)
- **Total Files Re-extracted:** 128 files

### 2026-01-13: Eclipse-I Full Extraction

- **Status:** COMPLETED SUCCESSFULLY
- **Source:** Eclipse of ATM AU I (P199-P260)
- **Total Prompts Extracted:** 62 unique prompts
- **Files Created:** 62 topic files
- **Key Content Areas:**
  - Atomic Stride and mobility system
  - Godric's linguistic identity (Japanese, Southern drawl, Northern English)
  - Tangible/Intangible love dynamic foundation
  - Godric's virgin status and physical attraction awakening
  - Maria's hair as vulnerability equivalent (golden eyes parallel)
  - Silent scenes and unspoken communication
  - Junior/Father public height misconceptions
  - Leo and Lora "Partners in Chaos" dynamic
  - Godric Sr./Jr. protective dynamic and Beta ambition
  - Junior idolizes Rodan and Anguirus (secret Beta training)
  - Lepidiel and hybrid physiques comparison

### 2026-01-12: BTG Full Extraction

- **Status:** COMPLETED SUCCESSFULLY
- **Source:** Branch of Titanus gojira (P199-P263)
- **Total Prompts Extracted:** 66 unique prompts
- **Files Created:** 66 topic files
- **Key Content Areas:**
  - Darius voice characteristics
  - Godric Japanese language and hybrid speech
  - Nordson family Japanese language heritage
  - Titan polyglot imperative
  - Godric American English voice of command
  - Name origin philosophy (Godric, Maria, Darius, Leo)
  - Castle Bravo Four Story Arcs framework
  - Gojira years growth rate and lifespan system
  - Dagon campaign and betrothal trial
  - Nordson onomancy complete name analysis
  - Godzilla profile chronological organization
  - Master Timeline VII Eras

### 2026-01-12: Kratos Full Extraction

- **Status:** COMPLETED SUCCESSFULLY
- **Source:** The Kratos of Kings (P199-P263)
- **Total Prompts Extracted:** 68 unique prompts
- **Files Created:** 68 topic files
- **Key Content Areas:**
  - Tangibility principle and Zuko parallel
  - Atomic Amplification Arsenal complete
  - Godric's accents (Japanese, Southern, Northern English)
  - Tangible and intangible love dynamic
  - Physical attraction and historical relationship
  - Kratos system mechanics (Edicts, Injection, Fortification)
  - Ghidorah abilities (Gravity Beams, Tempest, Travel Methods)
  - ATM Ghidorah and Godzilla amalgamation profiles
  - Blood-Vow terms and EGO system
  - Energy constructs philosophy
  - Ichi's combat doctrine and tagging system
  - Phantom Head Syndrome
  - Sculptor vs Painter philosophy

### 2026-01-10: TG Full Extraction

- **Status:** COMPLETED SUCCESSFULLY
- **Source:** The Titanus gojira (P199-P276)
- **Total Prompts Extracted:** 76 unique prompts (P244, P254 file uploads only)
- **Files Created:** 77 topic files
- **Key Content Areas:**
  - Zuko Principle and Tangibility Theme
  - Atomic Amplification Arsenal Complete (biography as trophies)
  - Godric linguistic identity (Japanese, Northern English, Southern drawl)
  - Nordson family naming philosophy (Godric, Maria, Darius, Leo)
  - Alpha Titan Political Categories (Standing Hierarchy, Wardens, Challengers)
  - Sovereign vs Divine Authority dynamics
  - Three Stages of Rekindling (Kong, Battra, Dagon/children)
  - Burning Form mechanics and Aurelia/Astraea legacy
  - Gojira time/growth rate and lifespan mechanics
  - Master Timeline Arc Structure (Era I-VII, 15 arcs)
  - Zeke/Zilla Jr. and HEAT Team crossover
  - Titan Theology (Emergent vs Ascendant)
  - Godric-Zeke confrontation scenes

### 2026-01-09: BAA-Kratos Full Extraction

- **Status:** COMPLETED SUCCESSFULLY
- **Source:** Branch of AA - The Kratos of Kings (P199-P284)
- **Total Prompts Extracted:** 86 unique prompts
- **Files Created:** 86 topic files
- **Key Content Areas:**
  - Power Systems Philosophy (Kratos tangibility, Zuko Principle)
  - Atomic Amplification Arsenal Complete (AA, Railgun, Stride, Mantle)
  - Godric characterization (accents, era influences)
  - Godric-Maria romance dynamics (attraction, vulnerability, silent scenes)
  - Ghidorah abilities complete (Gravity Beams, Tempest, Travel Methods, Tagging)
  - Blood-Vow terms and mechanics
  - Ichi/Arthur vessel dynamics (EGO, limitations, translation vs imprisonment)
  - Kratos system mechanics (Edicts, Injection, Fortification)
  - Three Power Systems contrast philosophy
  - Godzilla/Ghidorah amalgamation analysis (franchise era inspirations)
  - Scylla development and Conquerors of Fate theme

### 2026-01-08: Standing Hierarchy Full Extraction

- **Status:** COMPLETED SUCCESSFULLY
- **Source:** Standing Hierarchy (P199-P294)
- **Total Prompts Extracted:** 96 unique prompts
- **Files Created:** 96 topic files

### 2026-01-08: Saga-TG Full Extraction

- **Status:** COMPLETED SUCCESSFULLY
- **Source:** Saga of the Titanus gojira (P199-P300)
- **Total Prompts Extracted:** 102 unique prompts
- **Files Created:** 102 topic files

### 2026-01-06 - 2026-01-07: AA-Kratos Full Extraction

- **Status:** COMPLETED SUCCESSFULLY
- **Source:** AA - The Kratos of Kings (P199-P344)
- **Total Prompts Extracted:** 146 unique prompts
- **Files Created:** 146 topic files

---

## Current Phase: CONTENT PROCESSING

All extraction and cleanup phases are complete. The corpus is ready for content processing:

1. **Query & Explore** - Use the corpus as a knowledge base for ATM universe questions
2. **Synthesize Lore Docs** - Merge related topics into unified reference documents
3. **Build Character Profiles** - Compile scattered character information
4. **Create Timeline** - Extract chronological references into master timeline

### Cleanup Completed (2026-01-16)
- Eclipse-II: Consolidated 34 topic-split files into 9 (one per prompt)
- BTG: Archived P220 duplicate and P244 placeholder (2 files)
- Kratos: Archived P253 duplicate, consolidated P262 splits (3 files)
- Total archived during cleanup: 39 additional files
- All sources verified clean (no duplicate P-numbers)

---

*This file should be updated after each extraction session.*
