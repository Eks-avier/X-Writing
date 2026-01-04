# ATM Extraction - Contradictions Tracker

> **Last Updated:** 2026-01-05
> **Status:** Initial review complete - Eclipse II full extraction

---

## Overview

This file tracks contradictions detected during extraction. Contradictions are flagged when the same topic has conflicting information across different prompts.

| Metric | Value |
|--------|-------|
| Total Contradictions Found | 0 |
| Pending Review | 0 |
| Resolved | 0 |

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

**Summary:** No contradictions flagged during Eclipse II extraction. Content appears internally consistent.

---

## Contradiction Log

*No contradictions have been logged yet.*

### Template for Future Entries

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
