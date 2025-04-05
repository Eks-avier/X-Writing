# Antitheriomorphosis Universe Document Integration Instructions

## Overview

The following instructions will guide you in implementing a cohesive atomic knowledge base for the Antitheriomorphosis universe, specifically addressing the integration of character profiles, species information, and cultural heritage documents for Godzilla and the *Titanus gojira* species.

## Document Architecture & File Structure

### Primary Structure

Implement the following file structure to organize your atomic knowledge base:

```
ATM/
├── Species/
│   └── Titanus-Gojira/
│       ├── _Titanus-Gojira.md                 # Hub document for species
│       ├── Core/                              # Biological aspects
│       │   ├── Evolutionary-Origins.md
│       │   ├── Limitless-Adaptation.md
│       │   ├── Energy-Domination.md
│       │   ├── Ascendant-Line.md
│       │   └── Reproductive-Biology.md
│       ├── Societal/                          # Cultural & social aspects
│       │   ├── Factions/                      # Faction subfolder
│       │   │   ├── Northern-Faction.md        # Physical & biological traits
│       │   │   ├── Northern-Culture.md        # Cultural & social practices
│       │   │   ├── Southern-Faction.md
│       │   │   ├── Southern-Culture.md
│       │   │   ├── Eastern-Faction.md
│       │   │   ├── Eastern-Culture.md
│       │   │   ├── Western-Faction.md
│       │   │   └── Western-Culture.md
│       │   ├── Hierarchy-of-Priorities.md
│       │   └── Energy-Communication.md
│       └── Historical/                        # Historical aspects
│           ├── Decline-and-Extinction.md
│           ├── MUTO-Relationship.md
│           ├── Current-Status.md
│           └── Titanus-Zilla-Relationship.md
└── Titans/
    └── Godzilla/
        ├── _Godzilla.md                       # Hub document for character
        ├── Identity/
        │   ├── Identity-Core.md
        │   ├── Physical-Appearance.md
        │   ├── Psychological-Profile.md
        │   └── Cultural-Heritage.md           # Links to relevant species documents
        ├── Energy-Domination/
        │   └── [...energy technique documents]
        ├── Physical-Capabilities/
        │   └── [...physical ability documents]
        ├── History/
        │   └── [...historical documents]
        ├── Relationships/
        │   └── [...relationship documents]
        └── Authority/
            └── [...authority documents]
```

## Document Naming & Content Guidelines

### 1. Standardized Naming Convention

All document filenames should:
- Use PascalCase for multi-word names (e.g., `Northern-Faction.md`)
- Include contextual prefixes when needed
- Use descriptive, specific names

### 2. Content Division Guidelines

When dividing content between related documents:

#### Species Faction Documents:

- **`Northern-Faction.md`**: Focus exclusively on:
  - Physical characteristics
  - Biological adaptations
  - Environmental specializations
  - Territorial range
  - Physiological traits
  - Combat adaptations specific to biology
- **`Northern-Culture.md`**: Focus exclusively on:
  - Social structures
  - Family organization
  - Betrothal and bonding practices
  - Communication styles
  - Naming conventions
  - Cultural rituals
  - Value systems

## YAML Frontmatter Standardization

### 1. Species Documents

#### Species Hub Document:

```yaml
---
title: "Titanus gojira"
alias: 
  - "Gojira" 
  - "Northern Gojira"
  - "Southern Gojira"
  - "Eastern Gojira"
  - "Western Gojira"
component_type: "species"
component_category: "titan_biology"
related_entities:
  - "[[Godzilla]]"
  - "[[Titanus zilla]]"
  - "[[MUTO]]"
species_status: "Near-extinct"
last_pure_member: "[[Godzilla]]"
core_abilities:
  - "[[Limitless Adaptation]]"
  - "[[Energy Domination]]"
tags:
  - atm
  - atm/species/titanus_gojira
  - atm/species/classification/ascendant_line
created: 2025-04-03
last_modified: 2025-04-03
---
```

#### Faction Document:

```yaml
---
title: "Titanus gojira: Northern Faction"
parent: "[[Titanus Gojira]]"
component_type: "faction"
component_category: "regional_variation"
faction_name: "Northern Gojira"
territory: "Northern hemisphere polar regions extending into boreal forests and cold oceans"
extinction_timeframe: "Latest surviving faction"
distinctive_traits:
  - "White dorsal fins with crystalline structure"
  - "Cooler-toned scales with silvery undertones"
  - "Broader build with enhanced insulation"
  - "Superior energy conservation"
  - "Strict hierarchical organization"
related_documents:
  - "[[Northern Culture]]": "Cultural practices and social structures"
  - "[[Southern Faction]]": "Contrasting adaptations and philosophy"
  - "[[Eastern Faction]]": "Historical territorial disputes"
  - "[[Western Faction]]": "Occasional cooperative hunting"
  - "[[Godzilla]]": "Last surviving member"
tags:
  - atm
  - atm/species/titanus_gojira
  - atm/faction/northern
created: 2025-04-03
last_modified: 2025-04-03
---
```

#### Culture Document:

```yaml
---
title: "Northern Titanus gojira: Cultural Profile"
parent: "[[Titanus Gojira Species Profile]]"
component_type: "culture"
component_category: "titan_culture"
related_entities:
  - "[[Godzilla]]"
  - "[[Dagon, the Last Northern Patriarch]]"
faction: "Northern"
territory: "Northern Hemisphere"
cultural_emphasis: "Family bonds"
distinctive_traits:
  - "Whiter dorsal fins"
  - "Cooler-toned scales"
  - "Cold environment adaptation"
  - "Familial prioritization"
tags:
  - atm
  - atm/culture/northern_gojira
  - atm/titan/northern_faction
created: 2025-04-03
last_modified: 2025-04-03
---
```

### 2. Character Documents

#### Character Hub Document:

```yaml
---
title: "Godzilla"
aliases: ["Godric Nordson", "Alpha Paramount", "King of the Monsters"]
tags:
  - atm
  - atm/titans/godzilla
  - atm/concepts/the-null
  - atm/hierarchical/alpha
related:
  - "[[Mothra]]"
  - "[[Kong]]"
  - "[[Anguirus]]"
  - "[[Atomic Amplification]]"
category: "Titans/Godzilla"
species: "Titanus gojira"
faction: "The Null"
status: "Active"
relationships:
  - "[[Mothra]]: Alpha Divine, romantic partner"
  - "[[Kong]]: Alpha Sovereign, respected ally"
  - "[[Anguirus]]: Beta Tier, closest friend"
  - "[[Rodan]]: Beta Tier, loyal lieutenant"
  - "[[Battra]]: Lord of Mystic Arts, complicated history"
traits: ["disciplined", "adaptable", "reserved", "protective", "relentless"]
created: 2025-04-03
last_modified: 2025-04-03
---
```

#### Character Heritage Document:

```yaml
---
title: "Godzilla: Cultural Heritage"
parent: "[[Godzilla]]"
component_type: "identity"
component_category: "cultural_background"
related_aspects:
  - "[[Titanus gojira Species Profile]]"
  - "[[Northern Titanus gojira Cultural Profile]]"
  - "[[Physical Appearance]]"
  - "[[Psychological Profile]]"
  - "[[Hierarchical Position]]"
evolution_points:
  - "Early Years": "Limited cultural education from Dagon focused on survival"
  - "Rise to Alpha": "Carried Northern values into leadership style"
  - "Post-Antitheriomorphosis": "Adaptation of heritage to human form"
  - "Current Status": "Selective preservation and sharing of cultural knowledge"
knowledge_completeness: "Partial"
cultural_continuation: "Active preservation"
heritage_expression_rating: 8.7
tags:
  - atm
  - atm/titans/godzilla
  - atm/identity/cultural
  - atm/northern_heritage
created: 2025-04-03
last_modified: 2025-04-03
---
```

## Document Content Structure

### 1. All Documents Must Include:

1. **Summary Section**:

   ```markdown
   ## Summary 
   
   [1-2 paragraph concise summary of the document content that can stand alone when embedded elsewhere]
   ```

2. **Related Documents Section**:

   ```markdown
   ## Related Aspects
   
   - [[Related Document 1]] - [Brief explanation of relationship]
   - [[Related Document 2]] - [Brief explanation of relationship]
   ```

3. **Return Link**:

   ```markdown
   [Return to Hub Document]([[_Titanus-Gojira]])
   ```

### 2. Faction and Culture Document Structures

#### Northern-Faction.md Structure:

```markdown
# Northern Faction

## Summary {#summary}

[Brief overview of Northern faction biological traits and physical characteristics]

## Territory & Environment

[Details about geographical range and environmental adaptations]

## Physical Characteristics

[Detailed description of distinctive physical traits]

## Energy Conservation Systems

[Information about biological energy management]

## Combat Adaptations

[Description of biological combat specializations]

## Related Aspects

- [[Northern Culture]] - Social structures and practices built upon these biological foundations
- [[Godzilla Cultural Heritage]] - How these traits manifest in the last survivor
- [[Energy Communication]] - Biological basis for Northern communication efficiency
- [[Southern Faction]] - Contrasting adaptations and physiological approaches

[Return to Hub Document]([[_Titanus-Gojira]])
```

#### Northern-Culture.md Structure:

```markdown
# Northern Titanus Gojira

## Summary {#summary}

[Brief overview of Northern cultural practices and social organization]

## Social Structure

[Details about family units, hierarchy, and social organization]

## Territory and Domain Division

[Information about how territories were divided and managed]

## Betrothal and Bonding Practices

[Description of mating rituals and partnership formation]

## Naming Conventions

[Explanation of naming traditions and significance]

## Related Aspects

- [[Northern Faction]] - The biological traits underlying cultural practices
- [[Godzilla Cultural Heritage]] - Northern cultural elements preserved by the last survivor
- [[Southern Culture]] - Contrasting cultural approaches and values
- [[Hierarchy of Priorities]] - How Northern values influenced species-wide priorities

[Return to Hub Document]([[_Titanus-Gojira]])
```

## Cross-Referencing Implementation

### 1. Bidirectional References

When referencing related documents, always:
- Explain the relationship between documents
- Use consistent terminology for relationships
- Ensure references are bidirectional (both documents reference each other)

Example:
- In Northern-Faction.md:

  ```markdown
  - [[Northern Culture]] - Social structures and practices built upon these biological foundations
  ```

- In Northern-Culture.md:

  ```markdown
  - [[Northern Faction]] - The biological traits underlying cultural practices
  ```

### 2. Use Embed Blocks in Hub Documents

In hub documents, embed summaries from relevant documents:

```markdown
## Northern Gojira Overview

![[Northern-Faction#summary]]

For details on social structures and cultural practices, see [[Northern-Culture]].
```

### 3. Consistent Callout Formatting

Use Obsidian callout blocks consistently:

```markdown
> [!note] Cultural Influence
> This physical adaptation directly influenced the development of Northern cultural practices regarding territory division. See [[Northern Culture#Territory and Domain Division]].
```

## Integration with Character Profile

### 1. Godzilla's Cultural Heritage Document

This document should:
- Link to relevant species and cultural documents
- Focus on how species/cultural traits manifest in Godzilla specifically
- Note how these traits have evolved in the last survivor
- Describe which cultural practices Godzilla maintains
- Explain how cultural heritage influences current behavior

### 2. Embedding Information Flow

Character Profile → Cultural Heritage → Species Culture → Species Biology

Each level should reference the level beneath it while focusing on increasingly specific aspects.

## Implementation Sequence

Follow this order to efficiently implement the knowledge base:

1. **Create Hub Documents**:
   - _Titanus-Gojira.md
   - _Godzilla.md

2. **Create Core Species Documents**:
   - Faction documents (Northern-Faction.md, etc.)
   - Culture documents (Northern-Culture.md, etc.)

3. **Create Character-Specific Documents**:
   - Identity documents (including Cultural-Heritage.md)
   - Ability documents
   - Relationship documents

4. **Implement Cross-References**:
   - Add bidirectional references between related documents
   - Implement embed blocks in hub documents
   - Add callouts highlighting connections

5. **Review for Consistency**:
   - Check all document names follow conventions
   - Verify YAML frontmatter standardization
   - Ensure content separation is maintained
   - Test all links and embeds

## Content Migration Guidelines

When redistributing existing content:

1. **Preserve Rich Description**:
   - Maintain the evocative, atmospheric writing style
   - Keep all sensory details and vivid descriptions
   - Preserve the sense of ancient cosmic significance

2. **Maintain Factual Consistency**:
   - Ensure dates, capabilities, and relationships remain consistent
   - Check that territorial descriptions match across documents
   - Verify that species history maintains continuity

3. **Resolve Contradictions**:
   - When contradictions exist, default to the most detailed source
   - Document resolution decisions in a separate note for future reference
   - Standardize terminology for concepts that appear in multiple documents

## Writing Style Guidelines

Maintain the rich, atmospheric writing style established in existing documents:

1. **Sensory Language**: Incorporate all senses in descriptions
2. **Contrasting Scales**: Juxtapose cosmic scale with intimate details
3. **Rhythmic Phrasing**: Use sentence structure to reflect controlled power
4. **Environmental Impact**: Describe how presence affects surroundings
5. **Implied History**: Let descriptions hint at deeper history without explicit exposition

## Final Output Requirements

The completed knowledge base should:

1. Contain all files specified in the file structure
2. Maintain all information from the original documents
3. Feature rich interlinking between documents
4. Include working dataview queries in hub documents
5. Implement consistent formatting throughout
6. Maintain the original tone and descriptive quality
7. Provide clear navigation paths between documents
8. Resolve all contradictions between source materials
9. Separate biological from cultural content appropriately
10. Link character traits to species characteristics where relevant