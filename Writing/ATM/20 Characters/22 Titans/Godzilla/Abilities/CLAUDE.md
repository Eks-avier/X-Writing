# CLAUDE.md - Godzilla Abilities Folder

## Overview

This folder documents Godric Nordson's (Godzilla's) combat abilities in human form. All files are **canonical** and use the standardized frontmatter system.

## Terminology Framework

### Kratos Vs “Domination of Energy”

These are **distinct concepts** with an in-universe relationship:

| Term | Type | Usage |
|------|------|-------|
| **Kratos** | Formal power system | The canonical framework for Titan abilities based on willpower |
| **Domination of Energy** | In-universe theory | Battra's initial classification attempt before Kratos was formalized |

**Important:** “Domination of Energy” is NOT deprecated. It represents Battra's working theory during his fight with Godzilla. The narrative sidepiece (70 Drafts) preserves this as valid in-universe scientific discovery. However, formal ability documentation should use **Kratos terminology**.

### Kratonic Terminology Reference

All ability files should use the proper Greek terms when discussing Kratonic mechanics:

**Personal Coating (Epichrisis):**
* **Fortification (Stereosis)** - Reinforcing structural integrity
  * Internal: Sovereign's Vessel (body enhancement)
  * External: Sovereign's Touch / “Structural Infusion” (object reinforcement)
* **Neutralization (Exoudeterosis)** - Dissolving incoming attacks
* **Penetration (Diatresis)** - Bypassing defenses

**Territorial Aura:**
* **Flaring (Anapsis)** - Intensifying environmental effects
* **Submission (Proskynesis)** - Will domination
* **Expansion (Ektasis)** - Enlarging Aura radius
* **Suppression (Kryptis)** - Concealment

**Hybrid:**
* **Injection** (Sovereign's Writ) - Penetration + Neutralization combined

### Atomic Amplification Definition

Per BAA-Kratos-P210, Atomic Amplification is:
> “The simultaneous and sustained application of both Personal Coating techniques… a master-level feat requiring a Kraton to maintain two opposing intents across their entire body at once: Neutralization (The Royal Armor) and Penetration (The Sceptered Strike).”

Also includes **Fortification (Stereosis)** for physical enhancement.

## Source References

### Primary Sources (80 Extracted)

* **AA-Kratos**: P199-P344 (142 files) - Original Kratos development
* **BAA-Kratos**: P199-P284 (86 files) - Branch conversation refinements

### Key Source Files

| Topic | Source |
|-------|--------|
| Structural Infusion = Fortification | AA-Kratos-P219 |
| Atomic Amplification definition | BAA-Kratos-P210 |
| Arsenal overview | AA-Kratos-P200, P280, P307 |
| Stride variants | BAA-Kratos-P211-214 |
| Electromagnetic foundation | AA-Kratos-P302, P304, P316-P320 |
| Elektromagneton nature | AA-Kratos-P302, P316-P320 |
| Mother Prime EMP strategy | AA-Kratos-P319 |

### Lore Integration

* **30 Lore/31 Power Systems/Krátos/** - Canonical Kratos documentation (see [[Krátos, the Power of Will]])
* [[Appendix_D_Glossary|30 Lore/Krátos/Appendix_D_Glossary]] - Definitive term reference
* [[Domination of Energy]] - Species-level biological trait (distinct from Battra's theory)
* [[elektromagneton-nature]] - Godric's personal awakening to his EM nature (Abilities perspective)

## Foundational Layer

The `_foundations/` folder serves **two purposes**:
1. **Personal Foundations**: Godric's ontological bedrock—his Holariston Polykrator nature
2. **Species Staging**: Temporary home for species-level ability documentation until Species Profile overhaul

### Architecture

```
_foundations/
├── CLAUDE.md                    # Hub explaining the dual-purpose layer
│
├── [SPECIES-LEVEL ABILITIES]    # Staging for Species Profile overhaul
│   ├── atomic-breath/           # First Kratonic application (any gojira)
│   ├── nuclear-pulse/           # EM-carried shockwave (any gojira)
│   ├── burning-form-potential/  # Why near-impossible (species truth)
│   ├── predatory-arsenal/       # Bite, Death Roll (species biology)
│   └── combat-doctrines/        # One-Shot, Attrition, faction styles
│
├── [PERSONAL FOUNDATIONS]       # Godric's journey with his nature
│   ├── dual-nature-overview.md  # Summary + links to species docs
│   ├── pyrenikon-mastery/       # Godric's PERSONAL nuclear journey
│   └── elektromagneton-awakening/ # Godric's PERSONAL EM awakening
```

### Key Distinction: Three Layers

| Layer | Location | Contains | Example |
|-------|----------|----------|---------|
| **Species Forces** | `_species-reference/` | What ALL gojira ARE | "Gojira can absorb electricity" |
| **Species Abilities** | `_foundations/` (staging) | What ALL gojira CAN DO | "Any gojira can fire atomic breath" |
| **Character** | `_foundations/` + `Abilities/` | Godric's specific achievements | "How Godric discovered his EM side" |

### Species-Level Documentation

> [!note] Temporary Locations
> - **Force definitions** → `_species-reference/` (adjacent to Abilities)
> - **Ability documentation** → `_foundations/` (this folder)
> Both will migrate to `30 Lore/33 Species/Titanus Gojira/` when Species Profile is overhauled.

| Document | Location | Content |
|----------|----------|---------|
| [[Holariston Dual-Nature]] | `_species-reference/` | Dual-force classification |
| [[Pyrenikon]] | `_species-reference/` | Nuclear force—"The Wild" |
| [[Elektromagneton]] | `_species-reference/` | EM force—"The Order" |
| [[_foundations/atomic-breath/CLAUDE\|Atomic Breath]] | `_foundations/` | First Kratonic application |
| [[_foundations/nuclear-pulse/CLAUDE\|Nuclear Pulse]] | `_foundations/` | EM-carried shockwave |
| [[_foundations/burning-form-potential/CLAUDE\|Burning Form Potential]] | `_foundations/` | Why 99.9% fail |
| [[_foundations/predatory-arsenal/CLAUDE\|Predatory Arsenal]] | `_foundations/` | Bite, Death Roll |
| [[_foundations/combat-doctrines/CLAUDE\|Combat Doctrines]] | `_foundations/` | One-Shot, Attrition, Faction styles |

---

## Atomic Topic Folders

Some ability topics use an **atomic folder architecture** instead of single files. This enables:
- Pure separation of content types (mechanics, narrative, thematic, trivia)
- Atomic files for precise linking
- In-universe trivia creates relationship web between characters
- Numbered prefixes ensure consistent ordering

### Folder Structure Pattern

```
[topic]/
├── CLAUDE.md            # Documents folder contents, links to all subfiles
├── 01-mechanics/        # What it does, how it works
├── 02-narrative/        # Story significance, character development
├── 03-thematic/         # Themes, symbolism, meaning
└── 04-trivia/
    ├── in-universe/     # Inspiration from other characters (linkable)
    └── out-of-universe/ # Meta-references, real-life inspirations
```

### Migrated Topics

| Folder | Purpose | Status |
|--------|---------|--------|
| [[_foundations/CLAUDE\|_foundations/]] | Species staging + Personal foundations | Complete |
| [[aerial-combat-doctrine/CLAUDE\|aerial-combat-doctrine/]] | Aerial mobility doctrine | Complete |
| [[atomic-amplification/CLAUDE\|atomic-amplification/]] | Root technique | Complete |
| [[atomic-stride/CLAUDE\|atomic-stride/]] | Mobility technique (Trophy of Humility) | Complete |
| [[atomic-mantle/CLAUDE\|atomic-mantle/]] | Protection technique (Trophy of Love) | Complete |
| [[innate-abilities/CLAUDE\|innate-abilities/]] | Personal use of species abilities | **NEW** |
| [[atomic-railgun/CLAUDE\|atomic-railgun/]] | Precision finisher (Trophy of Intellect) | **NEW** |
| [[burning-form/CLAUDE\|burning-form/]] | Ultimate state achievement | **NEW** |

> **Note:** Legacy single-file versions are documented in [[_Archive/CLAUDE|_Archive/CLAUDE.md]]. Use the folder structure for all new work.

---

## File Inventory

### Active Atomic Folders (Use These)

| Folder | Purpose | Trophy |
|--------|---------|--------|
| [[_foundations/CLAUDE\|_foundations/]] | Species staging + Personal foundations | — |
| [[aerial-combat-doctrine/CLAUDE\|aerial-combat-doctrine/]] | Aerial mobility doctrine | — |
| [[atomic-amplification/CLAUDE\|atomic-amplification/]] | Root technique | — |
| [[atomic-stride/CLAUDE\|atomic-stride/]] | Mobility technique | Trophy of Humility |
| [[atomic-mantle/CLAUDE\|atomic-mantle/]] | Protection technique | Trophy of Love |
| [[innate-abilities/CLAUDE\|innate-abilities/]] | Personal use of species abilities | — |
| [[atomic-railgun/CLAUDE\|atomic-railgun/]] | Precision finisher | Trophy of Intellect |
| [[burning-form/CLAUDE\|burning-form/]] | Ultimate state achievement | — |
| [[Writing/ATM/20 Characters/22 Titans/Godzilla/Abilities/supernatural-interactions/CLAUDE\|supernatural-interactions/]] | Psychic/Magic interactions | — |
| [[kratos-mastery/CLAUDE\|kratos-mastery/]] | Complete Kratonic mastery documentation | — |
| [[godric-energy-limitations/CLAUDE\|godric-energy-limitations/]] | Energy systems & psychological limitations | — |
| [[fighting-style-evolution/CLAUDE\|fighting-style-evolution/]] | Martial arts evolution & combat philosophy | — |
| [[zone-state-breakthrough/CLAUDE\|zone-state-breakthrough/]] | Flow state / Symphonia achievement | — |

### Active Single Files

| File | Nature | Notes |
|------|--------|-------|
| [[abilities-overview]] | Hub document | Overview linking to folders |

### Archived Files

Legacy files that have been superseded by atomic folders are now physically located in `_Archive/`. See [[_Archive/CLAUDE|_Archive/CLAUDE.md]] for the full list and migration documentation.

---

## Consistency Guidelines

1. **Use Greek terms** when discussing Kratonic mechanics (Stereosis, Epichrisis, etc.)
2. **Distinguish** between:
   * Biological traits (Limitless Adaptation, species-level energy control)
   * Kratonic techniques (Atomic Amplification, Fortification, etc.)
3. **“Structural Infusion”** = colloquial name for External Fortification
4. **First-person files** (like [[atomic-stride/02-narrative/godrics-working-notes|godrics-working-notes]]) can use informal terminology as Godric's voice
5. Reference **source files** when adding new content

## Vignette-Style Files

Certain files in this folder are **profiles that double as vignettes** — narrative documents written in Godric's first-person voice rather than objective documentation.

**Current vignette-style files:**
* [[atomic-stride/02-narrative/godrics-working-notes|godrics-working-notes]] — Godric's personal notes on refining a technique (located in `atomic-stride/02-narrative/`)

**Key characteristics:**
* Written in **first-person perspective** (Godric's voice)
* "Open to ideas" placeholders are **intentionally authentic** — his actual working notes, not incomplete documentation
* These capture his **thought process at a specific moment** in his martial development
* The "IN DEVELOPMENT" header is his **in-universe status label**, not a meta-documentation flag

**Important:** These files should NOT be "fixed" or "completed" with corpus solutions. The ambiguity and open questions are part of the narrative authenticity — they represent techniques Godric is actively figuring out.

## Trophy Narrative Framework

Per AA-Kratos P200 and P280, Godric's combat techniques carry **narrative significance beyond their tactical utility**:

> "Each ability is not a random power-up, but a **trophy**, a hard-won memento of a pivotal relationship and a crucial stage in his personal growth."

This framework connects combat development to character development. When writing about or expanding technique files, reference these trophy assignments:

| Technique | Trophy Title | Represents | Documentation |
|-----------|--------------|------------|---------------|
| **Atomic Railgun** | Trophy of Intellect | [[Madison Russell\|Madison's]] influence — analytical thinking | [[atomic-railgun/CLAUDE\|atomic-railgun/]] |
| **Atomic Stride** | Trophy of Humility | [[Kong\|Kong's]] martial philosophy — learning from others | [[atomic-stride/CLAUDE\|atomic-stride/]] |
| **Atomic Mantle** | Trophy of Love | [[Maria Lepidiel\|Maria]]/Mothra — protection priorities | [[atomic-mantle/CLAUDE\|atomic-mantle/]] |

**Application:** When documenting technique development or writing scenes involving these abilities, consider the underlying relationship and growth they represent. The techniques are not just combat tools but **character markers** that show who shaped Godric and how.

**Related:** The [[_foundations/elektromagneton-awakening/CLAUDE|Elektromagneton Awakening]] folder documents Godric's journey with his EM nature. Notably, **Barb's revelation** (teaching Godric about his EM nature) was essential to unlocking the Atomic Railgun—see [[atomic-railgun/04-trivia/in-universe/barb-foundation|Barb Foundation]].

## Updates

When modifying files:
1. Check source material in 80 Extracted for canonical terminology
2. Verify against 30 Lore/Kratos documentation
3. Maintain consistency with Greek term usage
4. Update frontmatter `source` field if adding corpus content
