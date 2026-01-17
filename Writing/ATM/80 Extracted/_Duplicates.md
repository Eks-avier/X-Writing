# Duplicate File Analysis

> **Generated:** 2026-01-15 (Post-Repair Rescan)
> **Updated:** 2026-01-16 (Pre-Content Processing Cleanup)
> **Total Files Analyzed:** 943 active
> **Sources Analyzed:** 10 (including BSaga-TG branch)
> **Duplicate Clusters Found:** 32
> **Status:** ARCHIVED
> **Files Archived:** 75 total (36 duplicates + 39 cleanup consolidations)
> **Archive Location:** `_Duplicates_Archive/`

---

## Summary

This document catalogs duplicate content across the 10 extracted source conversations, updated after the 2026-01-15 integrity repairs (128 files re-extracted).

### 2026-01-16 Pre-Content Processing Cleanup

Consolidated topic-split files to standard "one file per prompt":

**Eclipse-II (34 → 9 files archived):**
- P001: 4 topic-splits → 1 consolidated (Kratos Power System Introduction and Philosophy)
- P002: 5 topic-splits → 1 consolidated (Aura Mechanics and Willpower Dependency)
- P003: 5 topic-splits → 1 consolidated (Krator Terminology and Progression Paths)
- P004: 4 topic-splits → 1 consolidated (Coating Epichrisis and Energy Costs)
- P005: 8 topic-splits → 1 consolidated (Three Power Systems Linguistic Theming)
- P011: 2 topic-splits → 1 consolidated (Sorcery Division Backstories and Battra)
- P012: 2 topic-splits → 1 consolidated (Battra Finding Dorianne Scene)
- P013: 2 topic-splits → 1 consolidated (Narrative Structure and Godzillas Role)
- P094: 2 topic-splits → 1 consolidated (Junior Combat Style and Leo Flight Mechanics)

**BTG (2 files archived):**
- P220: Duplicate archived (kept "Naming Vignette Scene Leo and Junior" with Dagon entity)
- P244: Placeholder archived (file upload only, no content)

**Kratos (3 files archived):**
- P253: Duplicate archived (kept "Ichi's Tagging Combat System" with apostrophe)
- P262: 2 topic-splits → 1 consolidated (Kratonic Disdain and Sculptor vs Painter Philosophy)

### Branch Source Note

**BSaga-TG** is a continuation branch of Saga-TG:
- **Shared Content (P001-P300):** BSaga-TG inherits prompts P001-P300 from its parent Saga-TG. These are intentional shared content from the same conversation lineage, NOT duplicates requiring archival.
- **Unique Content (P301-P399):** The 99 files in this range are unique to BSaga-TG with no duplicates detected across other sources.
- **Duplicate Policy:** Only the unique P301-P399 range was scanned for cross-source duplicates. The shared P001-P300 content is already covered by Saga-TG extractions.

### Key Patterns

1. **Saga-TG ↔ BTG**: High overlap in P239-P253 (Godzilla profile content)
2. **AA-Kratos ↔ Kratos**: Power system mechanics (Edicts, Ghidorah abilities)
3. **AA-Kratos ↔ Standing**: Scylla development content (P265-P273)
4. **TG ↔ BTG ↔ Saga-TG**: Voice/linguistics content (P200, P201, P209)

---

## Duplicate Clusters

### P199 - Zuko Principle and Tangibility Theme
**Classification:** NEAR-DUPLICATE (3 files)
**Canonical:** AA-Kratos
**Files:**
- `AA-Kratos/P199 - Zuko Principle and Tangibility Theme (AA-Kratos).md` ← KEEP
- `Saga-TG/P199 - Zuko Principle and Tangibility Theme (Saga-TG).md` ← DELETE
- `TG/P199 - Zuko Principle and Tangibility Theme (TG).md` ← DELETE

---

### P200 - Atomic Amplification Arsenal Complete
**Classification:** NEAR-DUPLICATE (4 files)
**Canonical:** Kratos
**Files:**
- `Kratos/P200 - Atomic Amplification Arsenal Complete (Kratos).md` ← KEEP
- `Saga-TG/P200 - Atomic Amplification Arsenal Complete (Saga-TG).md` ← DELETE
- `TG/P200 - Atomic Amplification Arsenal Complete (TG).md` ← DELETE
- `BTG/P200 - Atomic Amplification Arsenal Complete (BTG).md` ← DELETE

---

### P201 - Godric Japanese Accent Origin
**Classification:** NEAR-DUPLICATE (3 files)
**Canonical:** AA-Kratos
**Files:**
- `AA-Kratos/P201 - Godric Japanese Accent Origin (AA-Kratos).md` ← KEEP
- `TG/P201 - Godric Japanese Accent Origin (TG).md` ← DELETE
- `BTG/P201 - Godric Japanese Accent Origin (BTG).md` ← DELETE

---

### P209 - Godric American English Voice of Command
**Classification:** VERBATIM (2 files)
**Canonical:** BTG
**Files:**
- `BTG/P209 - Godric American English Voice of Command (BTG).md` ← KEEP
- `TG/P209 - Godric American English Voice of Command (TG).md` ← DELETE

---

### P210 - Voice Actor Challenge and Telepathic Translation
**Classification:** VERBATIM (2 files)
**Canonical:** Saga-TG
**Files:**
- `Saga-TG/P210 - Voice Actor Challenge and Telepathic Translation (Saga-TG).md` ← KEEP
- `TG/P210 - Voice Actor Challenge and Telepathic Translation (TG).md` ← DELETE

---

### P211 - Atomic Resonance and Structural Infusion
**Classification:** VERBATIM (2 files)
**Canonical:** Kratos
**Files:**
- `Kratos/P211 - Atomic Resonance and Structural Infusion Clarification (Kratos).md` ← KEEP
- `AA-Kratos/P211 - Atomic Resonance and Structural Infusion (AA-Kratos).md` ← DELETE

---

### P220 - Edict Allocation Points System
**Classification:** VERBATIM (2 files)
**Canonical:** Kratos
**Files:**
- `Kratos/P220 - Edict Allocation Points System (Kratos).md` ← KEEP
- `AA-Kratos/P220 - Edict Allocation Points System (AA-Kratos).md` ← DELETE

---

### P227 - Ghidorah Tempest AOE Ability
**Classification:** VERBATIM (2 files)
**Canonical:** Kratos
**Files:**
- `Kratos/P227 - Ghidorah Tempest AOE Ability (Kratos).md` ← KEEP
- `AA-Kratos/P227 - Ghidorah Tempest AOE Ability (AA-Kratos).md` ← DELETE

---

### P231 - Ghidorah Cosmic Travel Methods
**Classification:** VERBATIM (2 files)
**Canonical:** Kratos
**Files:**
- `Kratos/P231 - Ghidorah Cosmic Travel Methods (Kratos).md` ← KEEP
- `Standing/P231 - Ghidorah Cosmic Travel Methods (Standing).md` ← DELETE

---

### P236 - Dagon Territorial Conquest for Courtship
**Classification:** VERBATIM (2 files)
**Canonical:** Saga-TG
**Files:**
- `Saga-TG/P236 - Dagon Territorial Conquest for Courtship (Saga-TG).md` ← KEEP
- `TG/P236 - Dagon Territorial Conquest for Courtship (TG).md` ← DELETE

---

### P237 - Translation vs Imprisonment Dichotomy
**Classification:** VERBATIM (2 files)
**Canonical:** Kratos
**Files:**
- `Kratos/P237 - Translation vs Imprisonment Dichotomy (Kratos).md` ← KEEP
- `AA-Kratos/P237 - Translation vs Imprisonment Dichotomy (AA-Kratos).md` ← DELETE

---

### P239 - Godzilla Mother Agency and Final Choice
**Classification:** VERBATIM (2 files)
**Canonical:** Saga-TG
**Files:**
- `Saga-TG/P239 - Godzilla Mother Agency and Final Choice (Saga-TG).md` ← KEEP
- `BTG/P239 - Godzilla Mother Agency and Final Sacrifice (BTG).md` ← DELETE

---

### P240 - Godzilla Inherited Tragedy Orphan Wound
**Classification:** VERBATIM (2 files)
**Canonical:** Saga-TG
**Files:**
- `Saga-TG/P240 - Godzilla Inherited Tragedy Orphan Wound (Saga-TG).md` ← KEEP
- `BTG/P240 - Godzilla Inherited Tragedy Orphan Wound (BTG).md` ← DELETE

---

### P242 - Aurelia Nordson Naming and Letter Synergy
**Classification:** VERBATIM (2 files)
**Canonical:** BTG
**Files:**
- `BTG/P242 - Aurelia Nordson Naming and Letter Synergy (BTG).md` ← KEEP
- `Saga-TG/P242 - Aurelia Nordson Naming and Letter Synergy (Saga-TG).md` ← DELETE

---

### P243 - Nordson Onomancy Complete Name Analysis
**Classification:** VERBATIM (2 files)
**Canonical:** BTG
**Files:**
- `BTG/P243 - Nordson Onomancy Complete Name Analysis (BTG).md` ← KEEP
- `Saga-TG/P243 - Nordson Onomancy Complete Name Analysis (Saga-TG).md` ← DELETE

---

### P244 - User Uploaded File Reference
**Classification:** VERBATIM (2 files)
**Canonical:** BTG
**Files:**
- `BTG/P244 - User Uploaded File Reference (BTG).md` ← KEEP
- `Saga-TG/P244 - User Uploaded File Reference (Saga-TG).md` ← DELETE

---

### P245 - Godzilla Profile Rewrite Strategy
**Classification:** VERBATIM (2 files)
**Canonical:** BTG
**Files:**
- `BTG/P245 - Godzilla Profile Rewrite Strategy (BTG).md` ← KEEP
- `Saga-TG/P245 - Godzilla Profile Rewrite Strategy (Saga-TG).md` ← DELETE

---

### P246 - Chronological Profile and Arc Organization
**Classification:** VERBATIM (2 files)
**Canonical:** BTG
**Files:**
- `BTG/P246 - Chronological Profile and Arc Organization (BTG).md` ← KEEP
- `Saga-TG/P246 - Chronological Profile and Arc Organization (Saga-TG).md` ← DELETE

---

### P247 - Meadowvale Timeline and Grand Opening Arc
**Classification:** VERBATIM (2 files)
**Canonical:** BTG
**Files:**
- `BTG/P247 - Meadowvale Timeline and Grand Opening Arc (BTG).md` ← KEEP
- `Saga-TG/P247 - Meadowvale Timeline and Grand Opening Arc (Saga-TG).md` ← DELETE

---

### P248 - Gaius Helena Goddard Cover Names
**Classification:** VERBATIM (2 files)
**Canonical:** BTG
**Files:**
- `BTG/P248 - Gaius Helena Goddard Cover Names (BTG).md` ← KEEP
- `Saga-TG/P248 - Gaius Helena Goddard Cover Names (Saga-TG).md` ← DELETE

---

### P249 - Goddard Identity Demotion Psychology
**Classification:** VERBATIM (2 files)
**Canonical:** BTG
**Files:**
- `BTG/P249 - Goddard Identity Demotion Psychology (BTG).md` ← KEEP
- `Saga-TG/P249 - Goddard Identity Demotion Psychology (Saga-TG).md` ← DELETE

---

### P250 - Titan Relational Maturity and Immortality
**Classification:** VERBATIM (2 files)
**Canonical:** BTG
**Files:**
- `BTG/P250 - Titan Relational Maturity and Immortality (BTG).md` ← KEEP
- `Saga-TG/P250 - Titan Relational Maturity and Immortality (Saga-TG).md` ← DELETE

---

### P251 - Human Side Characters and Keep Charlie Phases
**Classification:** VERBATIM (2 files)
**Canonical:** BTG
**Files:**
- `BTG/P251 - Human Side Characters and Keep Charlie Phases (BTG).md` ← KEEP
- `Saga-TG/P251 - Human Side Characters and Keep Charlie Phases (Saga-TG).md` ← DELETE

---

### P252 - ATM Definitive Master Timeline VII Eras
**Classification:** VERBATIM (2 files)
**Canonical:** BTG
**Files:**
- `BTG/P252 - ATM Definitive Master Timeline VII Eras (BTG).md` ← KEEP
- `Saga-TG/P252 - ATM Definitive Master Timeline VII Eras (Saga-TG).md` ← DELETE

---

### P253 - Godzilla Profile Pruning and Focus
**Classification:** VERBATIM (2 files)
**Canonical:** BTG
**Files:**
- `BTG/P253 - Godzilla Profile Pruning and Focus (BTG).md` ← KEEP
- `Saga-TG/P253 - Godzilla Profile Pruning and Focus (Saga-TG).md` ← DELETE

---

### P254 - Electrogravitational Warfare Synergy
**Classification:** VERBATIM (2 files)
**Canonical:** AA-Kratos
**Files:**
- `AA-Kratos/P254 - Electrogravitational Warfare Synergy (AA-Kratos).md` ← KEEP
- `Kratos/P254 - Electrogravitational Warfare Synergy (Kratos).md` ← DELETE

---

### P256 - Inverted Arcs Control vs Effort
**Classification:** VERBATIM (2 files)
**Canonical:** Kratos
**Files:**
- `Kratos/P256 - Inverted Arcs Control vs Effort (Kratos).md` ← KEEP
- `Standing/P256 - Inverted Arcs Control vs Effort (Standing).md` ← DELETE

---

### P265 - Kratos Revelations from Ghidorah
**Classification:** VERBATIM (2 files)
**Canonical:** AA-Kratos
**Files:**
- `AA-Kratos/P265 - Kratos Revelations from Ghidorah (AA-Kratos).md` ← KEEP
- `Standing/P265 - Kratos Revelations from Ghidorah (Standing).md` ← DELETE

---

### P268 - Scylla Development Approach
**Classification:** VERBATIM (2 files)
**Canonical:** AA-Kratos
**Files:**
- `AA-Kratos/P268 - Scylla Development Approach (AA-Kratos).md` ← KEEP
- `Standing/P268 - Scylla Development Approach (Standing).md` ← DELETE

---

### P269 - Hydrokinesis and Psychokinetic Metrics
**Classification:** VERBATIM (2 files)
**Canonical:** AA-Kratos
**Files:**
- `AA-Kratos/P269 - Hydrokinesis and Psychokinetic Metrics (AA-Kratos).md` ← KEEP
- `Standing/P269 - Hydrokinesis and Psychokinetic Metrics (Standing).md` ← DELETE

---

### P272 - Scylla Power Set Overview
**Classification:** VERBATIM (2 files)
**Canonical:** AA-Kratos
**Files:**
- `AA-Kratos/P272 - Scylla Power Set Overview (AA-Kratos).md` ← KEEP
- `Standing/P272 - Scylla Power Set Overview (Standing).md` ← DELETE

---

### P273 - Scylla Kratonic Abilities
**Classification:** VERBATIM (2 files)
**Canonical:** AA-Kratos
**Files:**
- `AA-Kratos/P273 - Scylla Kratonic Abilities (AA-Kratos).md` ← KEEP
- `Standing/P273 - Scylla Kratonic Abilities (Standing).md` ← DELETE

---

## Archival Summary

| Source | Files Archived | Prompt Numbers |
|--------|----------------|----------------|
| Saga-TG | 14 files | P199, P200, P242-P253 |
| TG | 6 files | P199, P200, P201, P209, P210, P236 |
| BTG | 4 files | P200, P201, P239, P240 |
| AA-Kratos | 4 files | P211, P220, P227, P237 |
| Standing | 7 files | P231, P256, P265, P268, P269, P272, P273 |
| Kratos | 1 file | P254 |
| BSaga-TG | 0 files | (No duplicates - unique P301-P399 content) |

**Total Duplicates Archived:** 36 files → `_Duplicates_Archive/`
**Canonical Versions Kept:** 32 files in original locations

---

## Canonical Version Selection Criteria

1. Most complete/detailed content
2. Cleanest extraction (no artifacts)
3. Source with longest prompt range (more context)
4. Preference order: AA-Kratos > Kratos > BSaga-TG > BTG > Saga-TG > TG > Standing > Eclipse-I

> **Note:** BSaga-TG is ranked above Saga-TG in preference order because it contains the continuation (P301-P399) with more recent context.

---

## Archival Complete

**Archived on:** 2026-01-15

All 36 duplicate files have been moved to `_Duplicates_Archive/` preserving the source folder structure:

```
_Duplicates_Archive/
├── Saga-TG/    (14 files)
├── TG/         (6 files)
├── BTG/        (4 files)
├── AA-Kratos/  (4 files)
├── Standing/   (7 files)
├── Kratos/     (1 file)
└── BSaga-TG/   (0 files - no duplicates detected)
```

Files can be permanently deleted after user review, or restored if any were misidentified.

> **BSaga-TG Note:** This branch source shares P001-P300 with parent Saga-TG (intentional lineage, not duplicates). Only unique content P301-P399 was scanned for cross-source duplicates; none were found.

---

*Updated: 2026-01-16 (Added BSaga-TG branch source)*
