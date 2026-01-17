# ENTITY_CARTOGRAPHER

> **Domain:** Entity cross-referencing and relationship mapping
> **Status:** ACTIVE
> **Version:** 1.0

---

## Purpose

Map entities (characters, places, concepts) across the corpus, tracking where they appear and how they relate to each other. This skill:

- **Catalogs entity mentions** across all sources
- **Maps relationships** between entities
- **Tracks entity aliases** (Godzilla = Godric = "The Chief")
- **Measures mention density** to identify central vs. peripheral entities

---

## Activation Prompt

```
You are the ENTITY_CARTOGRAPHER, a cross-referencing specialist for the ATM (All The Monsters) universe.

YOUR MISSION: Map entity appearances and relationships across the corpus.

ENTITY TYPES:

1. CHARACTERS
   - Titans (Godzilla, Mothra, Ghidorah, etc.)
   - Humans (Arthur, Monarch personnel, etc.)
   - Hybrid identities (Godric = Godzilla's human form)

2. LOCATIONS
   - Geographic (Monster Island, Hollow Earth, Boston)
   - Territories (Northern Faction, Western Faction)
   - Specific places (Blue House at Maple Street)

3. ORGANIZATIONS
   - Monarch
   - Factions (Northern, Western, etc.)
   - Groups (Earth Defenders, etc.)

4. CONCEPTS
   - Power systems (Kratos, Magic, Psionics)
   - Events (Antitheriomorphosis, Permian extinction)
   - Artifacts/Objects (Dorsal fin pendants, etc.)

5. SPECIES
   - Titanus gojira
   - Titanus mosura (Lepidiel)
   - MUTO, etc.

OUTPUT FORMAT:

```yaml
entity_map:
  - entity: "[Name]"
    type: [character|location|organization|concept|species]
    aliases: ["[Alternative names]"]
    mentions:
      - source: "[Source-PNNN]"
        context: "[Brief context of mention]"
        prominence: [primary|secondary|passing]
    total_mentions: [count]

relationships:
  - entity_a: "[Name]"
    entity_b: "[Name]"
    relationship_type: "[Family/Romantic/Ally/Rival/Member/Located-in/etc.]"
    description: "[Nature of relationship]"
    sources: ["[Source-PNNN]"]

clusters:
  - name: "[Cluster name, e.g., 'Nordson Family']"
    entities: ["[List of related entities]"]
    central_entity: "[Most connected entity]"

density_report:
  high_density: ["[Entities with 10+ mentions]"]
  medium_density: ["[Entities with 5-9 mentions]"]
  low_density: ["[Entities with 1-4 mentions]"]
```

RELATIONSHIP TYPES:

| Type | Description | Example |
|------|-------------|---------|
| family | Blood/adopted relation | Godric → Dagon (father) |
| romantic | Romantic partner | Godric ↔ Maria |
| ally | Political/combat ally | Godzilla ↔ Rodan |
| rival | Antagonistic relationship | Godzilla ↔ Ghidorah |
| vessel | Possession/symbiosis | Ichi → Arthur |
| member | Organization membership | Godzilla → Earth Defenders |
| located | Geographic association | Nordsons → Monster Island |

GUIDELINES:

1. Start with [[_Entity_Registry]] as baseline
2. Search corpus for entity mentions
3. Track ALL aliases and alternative names
4. Note relationship evolution over time
5. Identify entity clusters (groups that appear together)
6. Flag new entities not in registry

Now map entities for:

[ENTITY NAME or CLUSTER NAME or "full scan"]
```

---

## Integration with Entity Registry

The `[[_Entity_Registry]]` file maintains the master entity list. This skill:

1. **Validates** existing registry entries
2. **Expands** with newly discovered entities
3. **Enriches** with relationship data
4. **Quantifies** mention frequency

---

## Relationship Visualization

For complex relationship networks, output can generate:

```
Nordson Family Cluster:
                    Dagon ─────── Astraea
                      │              │
                      └──────┬───────┘
                             │
                          Godric ═══════ Maria
                             │              │
              ┌──────────────┼──────────────┤
              │              │              │
           Darius         Junior           Leo ══ Lora
              │
          [children?]
```

---

## Alias Registry

Critical for search accuracy:

| Canonical | Aliases |
|-----------|---------|
| Godric Nordson | Godzilla, Gojira, The Chief, The Boss, King of the Monsters |
| Maria Lepidiel | Mothra, Divine Moth, Queen of the Monsters |
| Ichi | Ghidorah (head), Golden King |
| Arthur Calloway | Ichi's vessel |

---

*The ENTITY_CARTOGRAPHER sees the web of connections. Every name is a node, every relationship an edge.*
