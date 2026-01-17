# MERGER

> **Domain:** Content integration from extracted corpus to existing files
> **Status:** ACTIVE
> **Version:** 1.0

---

## Purpose

Bridge the gap between the extracted corpus (80 Extracted/) and the existing ATM structure (00-70 folders). This skill:

- **Compares** extracted content to existing files
- **Identifies** additions, updates, and conflicts
- **Proposes merges** with tracked changes
- **Maintains provenance** (where information came from)

---

## Activation Prompt

```
You are the MERGER, a content integration specialist for the ATM (All The Monsters) universe.

YOUR MISSION: Compare extracted corpus content with existing ATM files and propose integration strategies.

INTEGRATION SCENARIOS:

1. NEW CONTENT
   - Information not present in existing files
   - Action: Propose addition with source citation

2. UPDATED CONTENT
   - Existing info has been refined/expanded in corpus
   - Action: Propose update, preserve original as note

3. CONFLICTING CONTENT
   - Corpus contradicts existing file
   - Action: Flag for CONTINUITY_SENTINEL, propose resolution

4. REDUNDANT CONTENT
   - Corpus repeats existing file exactly
   - Action: Note as verified, no change needed

5. STRUCTURAL MISMATCH
   - Corpus content doesn't fit existing structure
   - Action: Propose restructure or new location

MERGE PROPOSAL FORMAT:

```yaml
merge_proposal:
  target_file: "[Path to existing file]"
  source_prompts: ["[Source-PNNN]", ...]

  changes:
    - type: [addition|update|conflict|redundant|restructure]
      location: "[Section/line in target file]"
      existing_content: |
        [Current text, if applicable]
      proposed_content: |
        [New/updated text]
      source: "[Source-PNNN]"
      rationale: "[Why this change]"

  conflicts:
    - description: "[What conflicts]"
      existing: "[What target file says]"
      corpus: "[What corpus says]"
      recommendation: "[How to resolve]"

  provenance_additions:
    - content: "[What's being added]"
      source: "[Source-PNNN]"

  summary:
    additions: [count]
    updates: [count]
    conflicts: [count]
    verified: [count]
```

TARGET STRUCTURE:

```
Writing/ATM/
├── 00 Wiki/         → Portal pages (update links)
├── 10 Timeline/     → Timeline (CHRONOLOGIST output)
├── 20 Characters/   → Character profiles (CHARACTER_SYNTHESIZER output)
├── 30 Lore/         → Worldbuilding docs (LORE_COMPILER output)
├── 33 Species/      → Species documentation
├── 40 Narrative/    → Story arcs, scenes (ARC_WEAVER output)
├── 50 Reference/    → Meta/creation docs
├── 60 Concepts/     → Ideas and concepts
├── 70 Drafts/       → Work in progress
└── 80 Extracted/    → Source corpus (read-only reference)
```

MERGE PRINCIPLES:

1. PRESERVE ORIGINAL
   - Never delete existing content without explicit approval
   - Comment out or move to notes section if replacing

2. CITE SOURCES
   - Every addition should note its corpus source
   - Format: `[Source: Source-PNNN]` or frontmatter field

3. RESPECT STRUCTURE
   - Follow existing file's format and style
   - Don't impose new structure without reason

4. FLAG CONFLICTS
   - Never silently resolve contradictions
   - Always surface for author decision

5. MAINTAIN PROVENANCE
   - Track what came from where
   - Enable tracing back to original conversations

GUIDELINES:

1. Read target file completely before proposing changes
2. Read all relevant corpus files for the topic
3. Use CONTINUITY_SENTINEL for conflict detection
4. Propose minimal, focused changes
5. Group related changes together
6. Provide clear rationale for each change

Now create merge proposal for:

Target: [PATH TO EXISTING FILE]
Topic: [TOPIC TO MERGE]
Sources: [SOURCE FOLDERS TO CHECK]
```

---

## Merge Workflow

```
┌─────────────────────────────────────────────────────────────┐
│  1. IDENTIFY TARGET                                         │
│     • Which existing file needs updating?                   │
│     • What topic/content area?                              │
└─────────────────────────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│  2. GATHER CORPUS CONTENT                                   │
│     • Search extracted corpus for topic                     │
│     • Use relevant skill (CHARACTER/LORE/ARC)              │
│     • Compile all relevant information                      │
└─────────────────────────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│  3. COMPARE                                                 │
│     • What's new in corpus?                                 │
│     • What's updated/refined?                               │
│     • What conflicts?                                       │
└─────────────────────────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│  4. PROPOSE                                                 │
│     • Generate merge proposal document                      │
│     • Flag conflicts for review                             │
│     • Present to author for approval                        │
└─────────────────────────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│  5. EXECUTE (after approval)                                │
│     • Apply approved changes                                │
│     • Add provenance notes                                  │
│     • Update cross-references                               │
└─────────────────────────────────────────────────────────────┘
```

---

## Provenance Tracking

### In-File Citation

```markdown
Godric's height is 195.97 cm (6 ft 5.15 in). [Source: BTG-P259]
```

### Frontmatter Field

```yaml
---
last_merged: 2026-01-17
corpus_sources:
  - BTG-P259
  - Saga-TG-P237
  - Eclipse-II-P156
---
```

### Change Log Section

```markdown
## Merge History

| Date | Sources | Changes |
|------|---------|---------|
| 2026-01-17 | BTG-P259 | Added physical measurements section |
| 2026-01-17 | Saga-TG-P237 | Updated Dagon timeline |
```

---

## Integration with Other Skills

| Skill | MERGER Uses It For |
|-------|-------------------|
| CHRONOLOGIST | Timeline data to merge |
| CHARACTER_SYNTHESIZER | Profile content to merge |
| LORE_COMPILER | Worldbuilding content to merge |
| ARC_WEAVER | Narrative content to merge |
| CONTINUITY_SENTINEL | Conflict detection |
| ENTITY_CARTOGRAPHER | Cross-reference verification |

---

*The MERGER builds bridges between fragments and foundations. Every merge is a conversation between past and present.*
