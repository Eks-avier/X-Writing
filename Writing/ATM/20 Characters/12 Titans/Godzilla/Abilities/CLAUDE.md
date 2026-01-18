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

The `_foundations/` folder documents Godric's **ontological bedrock**—his Holariston Polykrator nature as dual wielder of Pyrenikon (nuclear) and Elektromagneton (electromagnetic) forces.

### Architecture

```
_foundations/
├── CLAUDE.md                    # Hub explaining the foundations layer
├── dual-nature-overview.md      # Summary + links to species docs
├── pyrenikon-mastery/           # Godric's PERSONAL nuclear journey
│   ├── 01-inheritance/          # Mother's heart, father's body
│   ├── 02-applications/         # Breath, Pulse, Burning Form
│   └── 03-thematic/             # "The Wild Contained"
└── elektromagneton-awakening/   # Godric's PERSONAL EM awakening
    ├── 01-dormancy/             # 250 million years of unconscious use
    ├── 02-awakening/            # Barb, Battra, Symphonia
    ├── 03-applications/         # Railgun, Mantle, Aura integration
    └── 04-thematic/             # "The Order Mastered"
```

### Key Distinction: Species vs. Character

| Layer | Location | Contains |
|-------|----------|----------|
| **Species Profile** | 30 Lore/33 Species/Titanus Gojira/ | What ALL gojira are |
| **Foundations** | Abilities/_foundations/ | Godric's *personal relationship* with his nature |
| **Techniques** | Abilities/ (other folders) | Specific abilities built on that foundation |

### Species-Level Documentation

The following files in `30 Lore/33 Species/Titanus Gojira/1_Biology/` document universal gojira traits:

| Document | Content |
|----------|---------|
| [[Holariston Dual-Nature]] | Hub explaining dual-force classification |
| [[Pyrenikon]] | Nuclear force—"The Wild," culturally celebrated |
| [[Elektromagneton]] | EM force—"The Order," culturally ignored |

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

| Folder | Files | Status |
|--------|-------|--------|
| [[_foundations/CLAUDE\|_foundations/]] | 17 files | Complete |
| [[aerial-combat-doctrine/CLAUDE\|aerial-combat-doctrine/]] | 15 files | Complete |
| [[atomic-amplification/CLAUDE\|atomic-amplification/]] | 24 files | Complete |
| [[atomic-stride/CLAUDE\|atomic-stride/]] | 15 files | Complete |
| [[atomic-mantle/CLAUDE\|atomic-mantle/]] | 12 files | Complete |

> **Note:** Original single-file versions are retained temporarily during transition. The `elektromagneton-nature.md` file is being superseded by the `_foundations/elektromagneton-awakening/` folder structure.

---

## File Inventory

| File | Nature | Greek Terms |
|------|--------|-------------|
| [[abilities-overview]] | Hub document | Has terms |
| [[aerial-combat-doctrine]] | Aerial mobility (legacy file) | Has terms |
| [[aerial-combat-doctrine/CLAUDE\|aerial-combat-doctrine/]] | Aerial mobility (atomic folder) | Has terms |
| [[atomic-amplification]] | Main AA reference (legacy file) | Has terms |
| [[atomic-amplification/CLAUDE\|atomic-amplification/]] | Root technique (atomic folder) | Has terms |
| [[atomic-amplification-energy-domination]] | Theoretical perspective | Has terms |
| [[atomic-breath-evolution]] | Breath adaptation | Has terms |
| [[atomic-railgun-development]] | Railgun technique | Has terms |
| [[atomic-stride-development]] | First-person narrative (Godric's POV)* | Has terms |
| [[atomic-stride-mantle]] | Technical reference (legacy file) | Has terms |
| [[atomic-stride/CLAUDE\|atomic-stride/]] | Mobility technique (atomic folder) | Has terms |
| [[atomic-mantle/CLAUDE\|atomic-mantle/]] | Protection technique (atomic folder) | Has terms |
| [[burning-form]] | Ultimate state | Has terms |
| [[_foundations/CLAUDE\|_foundations/]] | **Foundational layer** — dual-nature documentation | Has terms |
| [[elektromagneton-nature]] | EM nature (legacy file — see `_foundations/elektromagneton-awakening/`) | Has terms |
| [[fighting-style-evolution]] | Combat philosophy | Has terms |
| [[godric-energy-limitations]] | Limitations analysis | Has terms |
| [[godric-supernatural-interactions]] | Psychic/Magic interactions | Has terms |
| [[kratos-mastery]] | Kratonic techniques | Has terms |
| [[primal-arsenal]] | Innate Gojira abilities & Phantom Tail | Has terms |
| [[zone-state-breakthrough]] | Krator awakening / Zone state | Has terms |

> **\*** [[atomic-stride-development]] is intentionally written in **Godric's first-person voice**. The “IN DEVELOPMENT” header is his **in-universe status label**, not a meta-documentation flag. This represents his personal notes on a technique he's actively refining.

## Consistency Guidelines

1. **Use Greek terms** when discussing Kratonic mechanics (Stereosis, Epichrisis, etc.)
2. **Distinguish** between:
   * Biological traits (Limitless Adaptation, species-level energy control)
   * Kratonic techniques (Atomic Amplification, Fortification, etc.)
3. **“Structural Infusion”** = colloquial name for External Fortification
4. **First-person files** (like [[atomic-stride-development]]) can use informal terminology as Godric's voice
5. Reference **source files** when adding new content

## Vignette-Style Files

Certain files in this folder are **profiles that double as vignettes** — narrative documents written in Godric's first-person voice rather than objective documentation.

**Current vignette-style files:**
* [[atomic-stride-development]] — Godric's personal notes on refining a technique

**Key characteristics:**
* Written in **first-person perspective** (Godric's voice)
* “Open to ideas” placeholders are **intentionally authentic** — his actual working notes, not incomplete documentation
* These capture his **thought process at a specific moment** in his martial development
* The “IN DEVELOPMENT” header is his **in-universe status label**, not a meta-documentation flag

**Important:** These files should NOT be “fixed” or “completed” with corpus solutions. The ambiguity and open questions are part of the narrative authenticity — they represent techniques Godric is actively figuring out.

## Trophy Narrative Framework

Per AA-Kratos P200 and P280, Godric's combat techniques carry **narrative significance beyond their tactical utility**:

> “Each ability is not a random power-up, but a **trophy**, a hard-won memento of a pivotal relationship and a crucial stage in his personal growth.”

This framework connects combat development to character development. When writing about or expanding technique files, reference these trophy assignments:

| Technique | Trophy Title | Represents |
|-----------|--------------|------------|
| [[atomic-railgun-development|Atomic Railgun]] | Trophy of Intellect | [[Madison Russell|Madison's]] influence — human analytical thinking, scientific approach |
| [[atomic-stride/CLAUDE|Atomic Stride]] | Trophy of Humility | [[Kong|Kong's]] martial philosophy — learning from others, adapting fighting styles |
| [[atomic-mantle/CLAUDE|Atomic Mantle]] | Trophy of Love | [[Maria Lepidiel|Maria]]/[[Mothra Profile|Mothra]] — protection and care for others, defensive priorities |

**Application:** When documenting technique development or writing scenes involving these abilities, consider the underlying relationship and growth they represent. The techniques are not just combat tools but **character markers** that show who shaped Godric and how.

**Related:** The [[elektromagneton-nature|Elektromagneton Nature]] file documents the foundational biological trait that enables many of these techniques. Notably, **Barb's revelation** (teaching Godric about his EM nature) was essential to unlocking the Atomic Railgun—making the MUTO turncoat an unlikely architect of his ultimate evolution.

## Updates

When modifying files:
1. Check source material in 80 Extracted for canonical terminology
2. Verify against 30 Lore/Kratos documentation
3. Maintain consistency with Greek term usage
4. Update frontmatter `source` field if adding corpus content
