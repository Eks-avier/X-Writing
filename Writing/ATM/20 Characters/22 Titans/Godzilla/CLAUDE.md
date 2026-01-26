# CLAUDE.md - Godzilla/Godric Nordson Profile

## Overview

This folder contains the **atomic profile** for Godric Nordson (Godzilla) - broken into category subfolders rather than a single monolithic document. All files use era-aware frontmatter for temporal filtering via the Hub Base.

## Folder Structure

| Folder | Contents | Atomization Status |
|--------|----------|--------------------|
| `Abilities/` | Atomic Amplification, combat arsenal, Kratos mastery | ✓ Fully atomized |
| `Appearance/` | Physical design, measurements, uncanny perfection | ✓ Fully atomized (5 folders + clothing) |
| `Biology/` | Limitless Adaptation, immortality, seasonal cycles | Flat files |
| `History/` | Timeline events, origin, Serizawa sacrifice | Flat files |
| `Identity/` | Names, titles, standing, lineage | ✓ Enhanced with corpus integration |
| `Lifestyle/` | Daily routines, grooming, leisure, education | ✓ Fully atomized (5 folders) |
| `Possessions/` | Territories, artifacts, vehicles, finances | ✓ Fully atomized (4 folders) |
| `Psychology/` | Hyperthymesia, linguistic identity, personality | Flat files |
| `_foundations/` | Species-wide traits (applies to all *Titanus gojira*) | ✓ Complete |
| `_Relationships/` | Maria, Dagon, Madison, family bonds | Flat files (external location) |
| `_Archive/` | Original monolith, audit reports | - |

## Hub Base

The `_Hub.base` aggregator provides 10 views:
- All Atoms
- Current (Era VII)
- Pre-Transformation (Era VI)
- Historical (Era I-V)
- Relationships
- By Category
- Canonical Only
- Needs Review
- By Source
- Archived

---

## Corpus Source Reference

### Priority Sources by Category

| Category | Primary Sources | Authority |
|----------|-----------------|-----------|
| **Abilities** | AA-Kratos P274-P282, Eclipse-II P163-P199 | DEFINITIVE |
| **Biology** | BSaga-TG P369, P389, Eclipse-II P163 | DEFINITIVE |
| **Psychology** | BSaga-TG P369, Eclipse-II P071, P180 | DEFINITIVE |
| **Appearance** | BSaga-TG P350, Eclipse-II P232-P242 | DEFINITIVE |
| **Identity** | Saga-TG P241-P242, P219 | DEFINITIVE |
| **Lifestyle** | BSaga-TG P341-P343, P368, P388 | DEFINITIVE |
| **Relationships** | BSaga-TG P323, AA-Kratos P204-P208 | DEFINITIVE |
| **History** | Eclipse-II P070-P073, Saga-TG P228-P294 | SUBSTANTIAL |
| **Linguistic** | AA-Kratos P201-P203, Saga-TG P206-P212 | DEFINITIVE |

### Key Source Files

| Topic | Best Source |
|-------|-------------|
| Atomic Amplification profile | AA-Kratos P274-P282 |
| Limitless Adaptation | Eclipse-II P163 |
| Hyperthymesia & memory | BSaga-TG P369, Eclipse-II P071 |
| Biological immortality | BSaga-TG P389 |
| Uncanny Perfection design | BSaga-TG P350 |
| Madison Russell relationship | BSaga-TG P323 |
| Maria/Mothra relationship | AA-Kratos P204-P208 |
| Dagon relationship | Eclipse-II P071, P073 |
| Martial arts repertoire | Eclipse-II P183, P187 |
| Japanese accent origin | AA-Kratos P201 |
| English accent variants | AA-Kratos P202-P203 |
| Mother (Astraea/Aurelia) naming | Saga-TG P241-P242 |
| Leo Aurelius connection | Saga-TG P219 |
| Antitheriomorphosis naming convention | Saga-TG P241 |

### Authority Levels

- **DEFINITIVE**: Use as primary authority
- **SUBSTANTIAL**: Use for supporting detail
- **PARTIAL**: Use for specific quotes/details only

### Evolution Chains

These show how topics developed across corpus files:

| Topic | Chain |
|-------|-------|
| Atomic Amplification | Eclipse-II P164→P184→P185→P197→AA-Kratos P200→P210→P218→P274-P282 |
| Fighting Style | Eclipse-II P165→P170→P174→P183→P187 |
| Romance Foundation | Eclipse-II P210-P214→AA-Kratos P204-P208→P335-P338 |

---

## Maintenance Guidelines

### When Adding New Content

1. **Check corpus sources** - Use the reference tables above to find authoritative files
2. **Verify canonicity** - Use canon-checker skill before propagating content
3. **Apply frontmatter** - All atoms need era-aware frontmatter with `status: canonical`
4. **Update Hub Base** - Ensure new atoms appear in appropriate views

### Ongoing Tasks

- [ ] Periodic review of "Needs Review" Hub Base view
- [ ] Sync check when monolith is updated
- [ ] Cross-reference with `30 Lore/` power system updates
- [ ] Cross-Titan links as other profiles are consolidated

### Optional Enhancements

- **Relationship Expansion**: Dedicated atoms for Kong, Anguirus, Rodan (currently in `found-family-bonds.md`)
- **Visual Canvas**: `.canvas` file mapping atom relationships
- **Era VI Content**: Pre-transformation atoms as that era develops

---

## Supporting Documents

| Document | Location | Purpose |
|----------|----------|---------|
| Original Monolith | `_Archive/Godzilla Profile.md` | 23K-word source reference |
| Monolith Audit | `_Archive/Monolith_Audit_Report.md` | Line-by-line comparison |
| Extraction Script | `_scripts/atomize_monolith.py` | Reproducible extraction |
| Abilities CLAUDE | `Abilities/CLAUDE.md` | Kratos terminology guide |

---

## Content Authority

| Source Type | Authority For |
|-------------|---------------|
| **Corpus** (`80 Extracted/`) | Narrative context, thematic quotes |
| **Monolith** (`_Archive/`) | Mathematical measurements, wardrobe specs, grooming protocols |
| **Lore** (`30 Lore/`) | Power system terminology (Kratos, etc.) |

---

## Lore Framework Integration

All profile files should link to relevant lore documentation when appropriate:

### Hierarchy & Standing (Identity files)
- [[The Titan Hierarchy]] — Complete three-axis hierarchy system
- [[The Standing System]] — Standing tier definitions (Alpha → Denizen)
- [[The Lineage System]] — Ascendant vs Emergent classification
- [[The Alpha Tier]] — Alpha Paramount, Divine, Sovereign positions

### Power Systems (Abilities, Psychology files)
- [[Krátos, the Power of Will]] — Primary hub document
- [[Appendix_D_Glossary]] — Greek terminology reference
- [[Part_VI_Character_Applications]] — Character-specific Krátos applications
- [[Appendix_B_Combat_Philosophies]] — Combat philosophy framework

### Timeline (History files)
- [[Master_Timeline.md]] — Era definitions, age calculations, event sequencing

### Species Documentation
- [[Titanus Gojira]] — Species encyclopedia
- [[_foundations/species-traits]] — Species-wide traits

---

## Metrics

- **Total atoms**: ~84 files
- **Hub Base views**: 10
- **Corpus references**: 280+ files mapped
- **Consolidation status**: Complete (2026-01-18); Clothing consolidated to Appearance/ (2026-01-21)
