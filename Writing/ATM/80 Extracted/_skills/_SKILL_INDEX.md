# ATM Content Processing Skills

> **Purpose:** Specialized prompt templates for processing the ATM extracted corpus.
> **Usage:** Read a skill file, then invoke via Task tool with `subagent_type: general-purpose`.

---

## Available Skills

| Skill | Domain | Status | Description |
|-------|--------|--------|-------------|
| [[CHRONOLOGIST]] | Timeline | ACTIVE | Extract temporal data, build chronology |
| [[CONTINUITY_SENTINEL]] | Canon | ACTIVE | Detect contradictions, track revisions |
| [[CHARACTER_SYNTHESIZER]] | Profiles | ACTIVE | Compile character information |
| [[LORE_COMPILER]] | Worldbuilding | ACTIVE | Build system reference docs |
| [[ARC_WEAVER]] | Narrative | ACTIVE | Scene inventory, plot mapping |
| [[ENTITY_CARTOGRAPHER]] | Cross-ref | ACTIVE | Entity relationships, mentions |
| [[THEME_ANALYST]] | Themes | ACTIVE | Thematic patterns, symbolism |
| [[MERGER]] | Integration | ACTIVE | Flow extracted into existing |

---

## Skill File Format

Each skill file contains:

```markdown
# [SKILL_NAME]

## Purpose
What this skill does.

## Activation Prompt
The prompt to copy into Task tool.

## Output Format
What the skill produces.

## Examples
Sample invocations and results.
```

---

## Invocation Pattern

### Via Task Tool (Recommended)

```
Use Task tool:
  subagent_type: general-purpose
  prompt: [Copy activation prompt from skill file]
```

### Via Project Agent

All skills have corresponding `.claude/agents/` definitions for automatic invocation.

| Skill | Agent File | Auto-Invokes When |
|-------|------------|-------------------|
| CHRONOLOGIST | `chronologist.md` | Processing temporal content |
| CONTINUITY_SENTINEL | `continuity-sentinel.md` | Checking for contradictions |
| CHARACTER_SYNTHESIZER | `character-synthesizer.md` | Building character profiles |
| LORE_COMPILER | `lore-compiler.md` | Compiling worldbuilding docs |
| ARC_WEAVER | `arc-weaver.md` | Mapping narrative structure |
| ENTITY_CARTOGRAPHER | `entity-cartographer.md` | Cross-referencing entities |
| THEME_ANALYST | `theme-analyst.md` | Analyzing themes/symbols |
| MERGER | `merger.md` | Integrating content |

---

## Orchestration Workflows

### Timeline-First Processing

1. Run CHRONOLOGIST on source folder
2. Build master timeline anchors
3. Process remaining content with temporal context

### Full Source Processing

1. CHRONOLOGIST - Extract temporal data
2. ENTITY_CARTOGRAPHER - Map entities
3. CONTINUITY_SENTINEL - Check for conflicts
4. MERGER - Propose integrations

---

## Output Locations

| Skill Output | Target Location |
|--------------|-----------------|
| Timeline entries | `Writing/ATM/10 Timeline/` (to create) |
| Character updates | `Writing/ATM/20 Characters/` |
| Lore additions | `Writing/ATM/30 Lore/` |
| Narrative mapping | `Writing/ATM/40 Narrative/` |

---

*Skills are prompt templates, not executable code. They guide Claude instances toward consistent, structured output.*
