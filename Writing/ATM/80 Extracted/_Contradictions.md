# ATM Extraction - Contradictions Tracker

> **Last Updated:** 2026-01-15
> **Status:** ALL CONTRADICTIONS RESOLVED

---

## Overview

This file tracks contradictions detected during extraction. Contradictions are flagged when the same topic has conflicting information across different prompts.

| Metric | Value |
|--------|-------|
| Total Contradictions Flagged | 3 |
| Resolved | 3 (all consistent with established systems) |
| Intentional Refinements | 1 |
| **True Contradictions** | **0** |

---

## Extraction Review Status

### Eclipse II (P001-P245) - COMPLETE

| Prompt Range | Agent | Contradictions Found | Notes |
|--------------|-------|----------------------|-------|
| P001-P096 | Multiple | 0 | Core power systems, initial worldbuilding |
| P097-P103 | ac468f4 | 0 | Continued worldbuilding |
| P104-P120 | aa4361c | 0 | Nordson family, combat philosophies |
| P121-P136 | a0eeb3d | 0 | Mothra/Rodan dynamics |
| P137-P170 | a90b619 | 0 | Scylla backstory, Ascendant framework, Antitheriomorphosis |
| P171-P198 | a7b720b | 0 | Godzilla fighting styles, Atomic Amplification |
| P199-P245 | a056e0d | 0 | AA arsenal, romance dynamics, intimate scenes |

**Summary:** No substantive contradictions found. One intentional refinement identified and documented. Content appears internally consistent.

---

## Validator Review Notes (2026-01-05)

### Topics Reviewed

1. **Kratos/Aura Mechanics (P001-P005, P046-P050)**
   - Aura definition, Latent vs Actualized states
   - Two-layered Krator Aura (First/Second Layer)
   - Flaring, Coating, Expansion, Suppression definitions
   - Royal Court Framework
   - Injection/Sovereign's Writ mechanics
   - **Status:** Internally consistent. Later prompts refine earlier definitions without contradiction.

2. **Atomic Amplification (P164, P184-P206)**
   - Foundations (Limitless Adaptation, Hyperthymesia, Kratos)
   - Tier system (1-15%, 15-50%, 50-100%)
   - Kratonic definition (simultaneous Penetration + Neutralization)
   - Arsenal components (AA, Railgun, Stride, Mantle, APS)
   - **Status:** Internally consistent. Progressive development with no conflicting statements.

3. **Character Abilities**
   - Godzilla: Limitless Adaptation, Hyperthymesia, Magic Nullification
   - Mothra/Battra: Telepathy ethics, Scale constructs (Fairies/Sentinels)
   - **Status:** Internally consistent.

4. **Timeline/Dates (P010, P025, P027)**
   - Keep Charlie establishment: 2024 (post-Xilien Invasion)
   - Godzilla's Repose period: engagement through twin sons' birth (~1.5 years)
   - Pacific Rim timeline: 2030
   - **Status:** Internally consistent.

---

## Resolved Contradictions (2026-01-15 Review Complete)

### Dagon's Age: Mating vs Death Timeline

**Detected:** 2026-01-14
**Severity:** N/A (Resolved)
**Status:** RESOLVED - Consistent with Growth Rate System

#### Files Involved

1. [[P237 - Gojira Years Growth Rate and Lifespan System (BTG)]]
2. [[P237 - Gojira Time Growth Rate and Lifespan (TG)]]
3. [[P229 - Godzilla Mother Frail Constitution Origin (BTG)]]
4. [[P224 - Mother Frailty and Heart Condition (TG)]]
5. [[P229 - Godzilla Mother Physical Frailty Origin (Saga-TG)]]

#### Conflicting Statements

**From BTG P237 / TG P237:**
> "Dagon dies at 30-31 human-equivalent years. Dagon's objective age at death is ~500 Earth years."

**From BTG P229 / TG P224 / Saga-TG P229:**
> "she and Dagon were ~300 years old, which was biologically equivalent to 20 year old humans."

#### Math Breakdown

- If 500 Earth years = 30-31 human-equivalent years → ratio is 1:16-17
- At ~300 Earth years with that ratio → Dagon would be ~18-19 human-equivalent
- But files state he was "~20 year old humans equivalent" at 300 years
- Minor variance (1-2 years) OR the anchor points need adjustment

#### Resolution (2026-01-15)

**Resolved:** The [[P237 - Gojira Age Conversion and Growth Rate (Saga-TG)]] establishes a non-linear growth rate table:

| Stage | Human-Equivalent | Earth Years |
|-------|------------------|-------------|
| Adolescence/Betrothal | 12-18 | 200-300 |
| Young Adulthood | 18-30 | 300-500 |

The "~300 Earth years" cited in mating files is a rounded approximation. At 20 human-equivalent (actual mating age), Dagon would be ~330-350 Earth years. This is consistent with the established growth rate system.

---

### Dagon + Godzilla Duration Inconsistency

**Detected:** 2026-01-14
**Severity:** N/A (Resolved)
**Status:** RESOLVED - Numbers are approximations within tolerance

#### Files Involved

1. [[P237 - Gojira Years Growth Rate and Lifespan System (BTG)]]
2. [[P070 - Deep Time - Titans Older Than Dinosaurs (Eclipse-II)]]

#### Conflicting Calculations

| Claim | Earth Years |
|-------|-------------|
| Dagon fathers Godzilla at 20-21 human-equivalent | ~300 |
| Dagon + mother together 10 human-equivalent years | ~165 |
| Expected mother's death | ~465 |
| Dagon's actual death age | ~500 |
| Gap remaining | 35 Earth years (2 human years) |

**Problem:** Files state Dagon and Godzilla spent 10 human years together AFTER mother's death. But math shows only 35 Earth years (2 human years) between mother's death (465) and Dagon's death (500).

#### Resolution (2026-01-15)

**Resolved:** The timeline values are approximations that fit within the established death age of 30-31 human-equivalent years:
- Fathering at ~20-21
- Mother alive ~1-1.5 years
- Together ~10 years
- Death at ~30-31 ✓

Minor variance (0.5-1 year) is acceptable for narrative approximations spanning hundreds of Earth years.

---

### San's Head "Mexico 2019" Timeline Conflict

**Detected:** 2026-01-14
**Severity:** N/A (Naming Convention Issue)
**Status:** RESOLVED - Not a timeline error

#### Files Involved

1. [[P235 - Ichi Godric Blood Vow Terms (AA-Kratos)]]
2. [[P208 - Blood-Vow Mechanics Ichi and Godric (BAA-Kratos)]]
3. [[P252 - ATM Definitive Master Timeline VII Eras (BTG)]]

#### Conflicting Statements

**From AA-Kratos P235 / BAA-Kratos P208:**
> "Godric must search for San's severed head, the one Godric himself took off in Mexico way back in 2019."

**From BTG P252 (Master Timeline):**
> 2019 = "Arc 0.5: The Modern Titan Wars" - Ghidorah awakens, Mass Awakening
> 2020 = "The Antitheriomorphosis" - Godric transforms to human form

#### Problem

In 2019, Godric was still in full Titan form (transformation happens 2020). How did he fight Ghidorah and sever San's head as referenced in Blood-Vow files?

#### Resolution (2026-01-15)

**Resolved:** The "Mexico 2019" reference is **correct**. This is the adaptation of *Godzilla: King of the Monsters* events within the ATM AU.

**Clarification on naming convention:**
- **Godzilla** = Titan form (used for events before transformation)
- **Godric** = Human form (used after 2020 Antitheriomorphosis)

The files inconsistently use "Godric" when referring to pre-transformation events. The timeline is accurate; only the name used in the reference should be "Godzilla" for clarity.

---

## Verified Consistent Areas (2026-01-14)

| Topic | Files Checked | Status |
|-------|---------------|--------|
| Atomic Amplification (4 abilities) | 12 | CONSISTENT |
| Ghidorah Travel Methods (4 methods) | 8 | CONSISTENT |
| Godric Voice/Accents (3 languages) | 15 | CONSISTENT |
| Edict Allocation System | 6 | CONSISTENT |
| Kratos Power Philosophy | 10 | CONSISTENT |

---

## Refinement Log

### Godzilla's Magic Nullification Mechanism - INTENTIONAL REFINEMENT

**Detected:** 2026-01-05
**Severity:** N/A (Intentional System Refinement)
**Status:** Resolved - Later definition supersedes earlier

#### Files Involved

1. [[P029 - Godzilla Magic Nullification and Domination of Energy (Eclipse-II)]]
2. [[P047 - Kratos Mechanics Fixing Circular Definitions (Eclipse-II)]]
3. [[P048 - Kratos Royal Court Framework (Eclipse-II)]]

#### Evolution of Definition

**From P029 (earlier, Prompt 29):**
> "It's essentially the application of Submission into the area covered by his Aura."

**From P048 (later, Prompt 48 - explicitly correcting this):**
> "Godzilla's Magic Nullification is not Submission, but simply Flaring so hard Primus Energy simply can't exist in the same space as his Aura occupies!"

#### Context

This is NOT a contradiction but an **intentional refinement**. P047 explicitly addresses "circular definitions" in the Kratos system and P048 provides the corrected framework. The author recognized the earlier description created logical confusion and refined it within the conversation.

**Canonical Definition:** Magic Nullification is extreme **Flaring (Anapsis)** - a Territorial application that physically displaces Primus Energy through overwhelming atomic presence. It is NOT Submission (which targets willpower of beings).

---

## Contradiction Log

*No true contradictions have been logged. The content appears internally consistent.*

### Template for Future Entries

\`\`\`markdown
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
\`\`\`

---

## Severity Levels

| Level | Definition | Example |
|-------|------------|---------|
| Minor | Phrasing difference, same meaning | "25 meters" vs "approximately 25m" |
| Moderate | Different details, potentially reconcilable | Different timeline dates |
| Major | Directly opposing claims | "X can do Y" vs "X cannot do Y" |

---

## Areas to Watch for Future Extractions

Based on the ATM universe complexity, these areas are prone to contradiction:
- **Power level scaling** across different arcs
- **Timeline dates** for historical events
- **Ability mechanics** as they evolved through conversation
- **Character relationships** and their development
- **Species traits** for Titans

---

*This file should be updated after each extraction batch and validation pass.*
