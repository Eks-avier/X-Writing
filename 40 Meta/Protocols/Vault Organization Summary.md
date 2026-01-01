# Vault Organization Summary

> *Documentation of the X-Writing vault reorganization conducted January 2026.*

---

## Overview

This vault underwent a comprehensive reorganization to implement **Johnny.Decimal numbering** throughout, with a parallel **wiki layer** for reader-friendly navigation. The goal was dual-purpose organization: efficient for authoring, discoverable for reading/sharing.

---

## Phase 1: Non-Fanfiction Content

### Before
Scattered folders at vault root:
- `Journal/`, `College/`, `Curiosity/` - unorganized
- 9 Notepad files loose at root
- `_Archive/`, `_Templates/` with unclear purpose
- Mixed content without consistent structure

### After: Johnny.Decimal Structure
```
X-Writing/
├── 10 Personal/
│   ├── Journal/        (7 entries)
│   └── Finance/        (Spending.md)
├── 20 Academic/
│   ├── College/        (Quarter folders + essays)
│   └── Languages/      (German vocab, Filipino essay)
├── 30 Learning/
│   └── Programming/    (C++, STL, project notes)
├── 40 Meta/
│   ├── Notepads/       (10 consolidated notepad files)
│   ├── Protocols/      (Linking protocol, THIS FILE)
│   └── Diagrams/       (Excalidraw, screenshots)
├── _Templates/         (Unchanged - Obsidian templates)
└── Writing/            (Phase 2)
```

### Files Moved
| From | To |
|------|-----|
| `Journal/*` | `10 Personal/Journal/` |
| `Spending.md` | `10 Personal/Finance/` |
| `College/*` | `20 Academic/College/` |
| `German Vocabulary*.txt`, `Filipino Essay.md` | `20 Academic/Languages/` |
| `Curiosity/*` | `30 Learning/Programming/` |
| `Notepad*.md` (9 files) | `40 Meta/Notepads/` |
| `New Linking Protocol.md` | `40 Meta/Protocols/` |
| `Excalidraw/*`, `CSS125*.png` | `40 Meta/Diagrams/` |

### Fanfiction-Adjacent Content
Moved to `Writing/`:
- `Claude Conversations/` → `Writing/Claude Conversations/`
- `Tags/` → `Writing/Tags/`
- `_Archive/Fiction/` → `Writing/Archive/`

---

## Phase 2: Writing/ATM Reorganization

### Before
- 215 files with inconsistent organization
- 18 loose root files (concepts, frameworks)
- "Messy" subfolders with 48 unorganized research files
- `Titans/` folder contained lore, not characters
- Empty placeholder folders (`ATM - Medieval AU/`, `Antitheriomorphosis Universe/`)
- Duplicate files

### After: Johnny.Decimal Structure
```
Writing/ATM/
├── 00 Wiki/                    (NEW - Portal layer)
│   ├── Index.md
│   ├── Portal - Characters.md
│   ├── Portal - Titans.md
│   ├── Portal - Humans.md
│   ├── Portal - Power Systems.md
│   ├── Portal - World.md
│   └── Portal - Story.md
├── 10 Characters/
│   ├── 11 Humans/              (12 profiles)
│   └── 12 Titans/              (78 files)
│       ├── Godzilla III/
│       │   └── Research/       (Suborganized from Messy/)
│       │       ├── Abilities/
│       │       ├── Appearance/
│       │       ├── Relationships/
│       │       └── Psychology/
│       ├── Mothra/
│       │   └── Research/       (Suborganized from Messy/)
│       └── [Other Titans]
├── 20 Lore/
│   ├── 21 Power Systems/       (38 files)
│   ├── 22 Hierarchy/           (11 files)
│   └── 23 Species/             (15 files)
├── 30 Narrative/
│   ├── 31 Story Arcs/          (15 files)
│   └── 32 Chapters/            (2 files)
├── 40 Reference/
│   ├── 41 Creation Instructions/ (9 files)
│   ├── 42 Settings/            (2 files)
│   └── 43 Canvases/            (12 files)
├── 50 Concepts/                (19 files - formerly loose)
└── 60 Drafts/                  (13 files - formerly Unrefined/)
```

### Major Changes

#### Messy Folders → Research Subfolders
**Godzilla III/Messy/** (33 files) reorganized:
- `Research/Abilities/` - Atomic powers, energy mechanics
- `Research/Appearance/` - Design philosophy, clothing, physical details
- `Research/Relationships/` - Trinity dynamics, family, romance
- `Research/Psychology/` - Memory, senses, personality

**Mothra/Messy/** (15 files) reorganized:
- `Research/Abilities/` - Scales, psionics, divine powers
- `Research/Appearance/` - Ethereal details, measurements
- `Research/Relationships/` - Romance, family dynamics

#### Lore Separation
`Titans/` folder previously mixed character profiles with lore. Now:
- Character profiles → `10 Characters/12 Titans/`
- Hierarchy documentation → `20 Lore/22 Hierarchy/`
- Species biology → `20 Lore/23 Species/`

#### Archived Content
- `Extracted from Gemini AI/` (8.3MB) → `Writing/Archive/Gemini AI Exports/`

#### Deleted
- `ATM - Medieval AU/` (empty)
- `Antitheriomorphosis Universe/` (empty template)
- `script_1.ps1`, `script_2.ps1` (loose scripts)

---

## Phase 3: Wiki Portal Layer

### Purpose
A parallel navigation system for **reader-friendly discovery** without reorganizing files. Portals link INTO the J.D. structure using `[[wikilinks]]`.

### Structure
```
00 Wiki/
├── Index.md                 - Main homepage, universe overview
├── Portal - Characters.md   - All characters hub
├── Portal - Titans.md       - Titan deep dive
├── Portal - Humans.md       - Human characters
├── Portal - Power Systems.md - Krátos, Magic, Psionics
├── Portal - World.md        - Hierarchy, species, locations
└── Portal - Story.md        - Narrative arcs, timeline
```

### Usage
- **Author mode**: Navigate via numbered folders (10-60)
- **Reader mode**: Start at `00 Wiki/Index.md`, browse via portals
- **Publishing**: Portal pages work excellently with Obsidian Publish

---

## File Counts

### Final Vault Structure
| Location | Files |
|----------|-------|
| `10 Personal/` | 8 |
| `20 Academic/` | 23 |
| `30 Learning/` | 3 |
| `40 Meta/` | 14 |
| `Writing/ATM/10 Characters/` | 90 |
| `Writing/ATM/20 Lore/` | 64 |
| `Writing/ATM/30 Narrative/` | 17 |
| `Writing/ATM/40 Reference/` | 23 |
| `Writing/ATM/50 Concepts/` | 19 |
| `Writing/ATM/60 Drafts/` | 13 |
| `Writing/ATM/00 Wiki/` | 7 |
| `Writing/Archive/` | 32 |

---

## Johnny.Decimal Numbering Convention

### Vault Root (Non-Fanfiction)
- **10** Personal
- **20** Academic
- **30** Learning
- **40** Meta

### Writing/ATM (Fanfiction)
- **00** Wiki (Portal layer)
- **10** Characters (11 Humans, 12 Titans)
- **20** Lore (21 Power Systems, 22 Hierarchy, 23 Species)
- **30** Narrative (31 Story Arcs, 32 Chapters)
- **40** Reference (41 Creation Instructions, 42 Settings, 43 Canvases)
- **50** Concepts
- **60** Drafts

---

## Benefits Achieved

1. **Dual-purpose structure** - J.D. for authoring, portals for reading
2. **Consistent numbering** - Easy to find files by category
3. **No lost content** - All files preserved, just reorganized
4. **Scalable** - Room to grow in each category
5. **Publishable** - Wiki layer ready for Obsidian Publish
6. **Research organized** - Messy folders now themed and navigable

---

## Maintenance Notes

- When adding new content, place in appropriate numbered folder
- Update relevant portal pages when adding significant new entries
- Keep `60 Drafts/` for work-in-progress; move to proper location when finalized
- Portals should be updated periodically to reflect new content

---

*Reorganization completed January 1, 2026*
