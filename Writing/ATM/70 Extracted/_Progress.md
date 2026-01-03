# Extraction Progress

> **Last Updated:** 2026-01-03 05:00
> **Current Phase:** Pilot Extraction (Eclipse II) - PAUSED DUE TO RATE LIMIT
> **Next Instance:** Continue from Prompt 6

---

## Overall Status

| Metric | Value |
|--------|-------|
| Source Files | 9 |
| Total Prompts | 2,529 |
| Common Trunk | 198 prompts (shared by all files) |
| Unique Content | ~945 prompts (~37%) |

| Progress | Count |
|----------|-------|
| Files Processed | 1 / 9 (in progress) |
| Prompts Extracted | 5 / 245 (Eclipse II) |
| Topics Generated | 26 |
| Metadata Files | 3 |
| Rate Limit Hit | Yes - parallel agents terminated |

---

## RESUME INSTRUCTIONS FOR NEXT CLAUDE INSTANCE

### Step 1: Read the Manifesto
```
C:\Users\Xavier\Desktop\Personal\Vaults\X-Writing\Writing\ATM\70 Extracted\_MANIFESTO.md
```

### Step 2: Continue Eclipse II Extraction

**Current State:** Only prompts 1-5 completed (26 files)
**Remaining:** Prompts 6-245 (240 prompts)

**Recommended approach:** Process in chunks of 10-20 prompts to avoid rate limits

**Next chunk to process:**
- File: `Formatted_With_Thoughts - The Eclipse of the ATM AU II.md`
- Prompts: 6-25 (20 prompts)
- Use the Extractor agent template from manifesto

### Step 3: Update This File
After each successful chunk, update this progress file with:
- Prompts completed
- Files created
- Any issues

---

## File Status

| File | Abbreviation | Total Prompts | Prompts Done | Status | Next Prompt |
|------|--------------|---------------|--------------|--------|-------------|
| Eclipse of ATM AU II | `Eclipse-II` | 245 | 5 | **IN PROGRESS** | P006 |
| AA - The Kratos of Kings | `AA-Kratos` | 344 | 0 | Pending | P214* |
| Saga of the _Titanus gojira_ | `Saga-TG` | 300 | 0 | Pending | P203* |
| Standing Hierarchy | `Standing` | 294 | 0 | Pending | P203* |
| Branch of AA - Kratos | `BAA-Kratos` | 284 | 0 | Pending | P214* |
| The _Titanus gojira_ | `TG` | 276 | 0 | Pending | P203* |
| The Kratos of Kings | `Kratos` | 263 | 0 | Pending | P214* |
| Branch of _Titanus gojira_ | `BTG` | 263 | 0 | Pending | P203* |
| Eclipse of ATM AU I | `Eclipse-I` | 260 | 0 | Pending | P214* |

*Skip common trunk (P001-P198) - already extracted via Eclipse II

---

## Extraction Log

### 2026-01-03

#### Session 1: Initial Setup
- Created output directory `70 Extracted`
- Completed branch analysis - all 9 files share common trunk (P001-P198)
- Created `_MANIFESTO.md` with full workflow documentation
- Created `_Branch_Map.md` with genealogy visualization

#### Session 1: Pilot Extraction (P001-P005)
- **Status:** COMPLETED
- **Files Created:** 26
- **Prompts:** 1-5
- **Topics by Prompt:**
  - P001: 4 files (Krátos comparative analysis)
  - P002: 5 files (Aura mechanics)
  - P003: 5 files (Hellenic terms, Aura shape)
  - P004: 4 files (Aura techniques)
  - P005: 8 files (Philosophical theming)

#### Session 1: Parallel Extraction Attempt (P006-P245)
- **Status:** RATE LIMITED - agents terminated before completion
- **Files Created:** 0 from this batch
- **Note:** Launched 9 parallel agents, all hit rate limit
- **Recovery:** Next instance should process sequentially or in smaller batches

---

## Files Generated (26 topic files + 3 metadata)

### Metadata Files
1. `_MANIFESTO.md` - Complete workflow documentation
2. `_Branch_Map.md` - Branch genealogy
3. `_Progress.md` - This file

### Topic Files from P001-P005

**Prompt 1 (4 files):**
- Kratos Overall Impression and Core Strengths (Eclipse-II-P001).md
- Kratos Distinctions from Other Power Systems (Eclipse-II-P001).md
- Cross-System Dynamics and Balance (Eclipse-II-P001).md
- Kratos Character Examples and Excellence (Eclipse-II-P001).md

**Prompt 2 (5 files):**
- Aura Definition and Latent Properties (Eclipse-II-P002).md
- Aura Irrepressibility and Thresholds (Eclipse-II-P002).md
- Aura Willpower Awareness and Sensory Extension (Eclipse-II-P002).md
- Aura Willpower Dependency and Conscious Control (Eclipse-II-P002).md
- Aura Actualized - Coating Flaring Expansion (Eclipse-II-P002).md

**Prompt 3 (5 files):**
- Hellenic Plural Forms for Kraton (Eclipse-II-P003).md
- Aura Shape - Spherical vs Circular (Eclipse-II-P003).md
- Krator Aura Threshold - First and Second Layer (Eclipse-II-P003).md
- Flaring Revised Definition (Eclipse-II-P003).md
- Koinon vs Krator Progression Paths (Eclipse-II-P003).md

**Prompt 4 (4 files):**
- Hellenic Terms for Aura Techniques (Eclipse-II-P004).md
- Aura Two Axes - Intensity and Spatial Management (Eclipse-II-P004).md
- Aura Energy Costs and Consequences (Eclipse-II-P004).md
- Coating - Epichrisis Definition (Eclipse-II-P004).md

**Prompt 5 (8 files):**
- Linguistic Theming of Power Systems (Eclipse-II-P005).md
- Magic Core Metaphor - Scholar Orator Showman (Eclipse-II-P005).md
- Psionics Core Metaphor - Artist and Ethicist (Eclipse-II-P005).md
- Kratos Core Metaphor - The Ruler (Eclipse-II-P005).md
- Mothra Telepathy Ethics (Eclipse-II-P005).md
- Battra Telepathy Pragmatism (Eclipse-II-P005).md
- Battra Irony - Ethics in Magic vs Psionics (Eclipse-II-P005).md
- Mothra and Battra Twin Symbology (Eclipse-II-P005).md

---

## Lessons Learned

1. **Avoid aggressive parallelization** - 9 agents hit rate limits
2. **Recommended chunk size:** 10-20 prompts per agent
3. **Consider sequential processing** for reliability over speed

---

*This file should be updated after each extraction session.*
