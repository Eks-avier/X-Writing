# Titan Species Documentation System

## 1. Core Philosophy

This system uses an atomic knowledge base approach for documenting Titan species in the Antitheriomorphosis universe. Key principles include:

- **Atomic Modularity**: Each aspect exists as a separate document
- **Hierarchical Organization**: Documents organized in logical “shells”
- **Standardized Metadata**: Consistent YAML frontmatter across documents
- **Rich Interlinking**: Robust connections between related documents
- **Dataview Integration**: Queries to gather and display cross-document information
- **Cross-Species Referencing**: Standardized connections between related species

## 2. Document Size Guidelines

| Document Type | Target Word Count | Max Word Count |
|---------------|-------------------|----------------|
| Hub Document | 500-750 words | 1,000 words |
| Biology Documents | 300-500 words | 750 words |
| Society Documents | 300-500 words | 750 words |
| History Documents | 300-500 words | 750 words |

## 3. Atomic Architecture

The knowledge base follows a nucleus-electron shell model:

- **Nucleus Document**: Central hub for navigation and species overview
- **Inner Shell**: Core biological aspects (evolution, physiology, abilities)
- **Middle Shell**: Societal and behavioral aspects
- **Outer Shell**: Historical and contextual aspects

## 4. File Structure

```
Species/
├── _Species-Index.md             # Master index of all species
├── Ascendant-Lines/              # Highest tier species  
│   ├── Titanus-Gojira/           # Example species folder
│   │   ├── _Titanus-Gojira.md    # Hub document
│   │   ├── Biology/              # Inner shell
│   │   ├── Society/              # Middle shell
│   │   └── History/              # Outer shell
│   └── [Other Ascendant Species]/
├── Emergent-Lines/               # Rising tier species
└── Supporting-Species/           # Lesser Titan species
```

## 5. Metadata Standards

### Hub Document Metadata

```yaml
---
title: "[Species Full Name]"
aliases: 
  - "[Common Name]"
  - "[Variant Names]"
species_classification: "[Ascendant/Emergent/Supporting]"
lineage_type: "[Species Family]"
status: "[Extinct/Endangered/Stable/Unknown]"
living_representatives:
  - "[[Representative Individual 1]]"
  - "[[Representative Individual 2]]"
core_abilities:
  - "[[Core Ability 1]]"
  - "[[Core Ability 2]]"
related_species:
  - "[[Related Species 1]]" 
  - "[[Related Species 2]]"
tags:
  - atm
  - atm/species/[species_tag]
  - atm/lineage/[lineage_tag]
  - atm/status/[status_tag]
created: YYYY-MM-DD
last_modified: YYYY-MM-DD
---
```

### Biology Document Metadata

```yaml
---
title: "[Species Name]: [Biological Aspect]"
parent: "[[_Species-Name]]"
component_type: "biology"
component_category: "[evolutionary/physiological/ability]"
related_components:
  - "[[Related Component 1]]"
  - "[[Related Component 2]]"
manifestations:
  - "[Example 1]"
  - "[Example 2]"
current_status: "[Active/Dormant/Evolved/Lost]"
tags:
  - atm
  - atm/species/[species_tag]
  - atm/biology/[aspect_tag]
created: YYYY-MM-DD
last_modified: YYYY-MM-DD
---
```

### Society Document Metadata

```yaml
---
title: "[Species Name]: [Social Aspect]"
parent: "[[_Species-Name]]"
component_type: "society"
component_category: "[social_structure/communication/behavior/faction]"
faction_name: "[For faction documents]"
territory: "[For faction documents]"
distinctive_traits:
  - "[Trait 1]"
  - "[Trait 2]"
related_components:
  - "[[Related Component 1]]"
  - "[[Related Component 2]]"
tags:
  - atm
  - atm/species/[species_tag]
  - atm/society/[aspect_tag]
created: YYYY-MM-DD
last_modified: YYYY-MM-DD
---
```

### History Document Metadata

```yaml
---
title: "[Species Name]: [Historical Aspect]"
parent: "[[_Species-Name]]"
component_type: "history"
component_category: "[timeline/extinction/relationship]"
time_period: "[Relevant time period]"
related_events:
  - "[[Event 1]]"
  - "[[Event 2]]"
related_species:
  - "[[Species 1]]"
  - "[[Species 2]]"
tags:
  - atm
  - atm/species/[species_tag]
  - atm/history/[aspect_tag]
created: YYYY-MM-DD
last_modified: YYYY-MM-DD
---
```

## 6. Document Templates

### Streamlined Hub Document Template

```markdown
# [Species Name]

## Introduction
[Single powerful paragraph capturing essence of species with atmospheric elements]

> [!quote] Monarch Classification
> "[Brief, focused observation about the species]"

## Core Characteristics
- **Physical Form**: [Concise description with key distinctive elements]
- **Evolutionary Status**: [Species classification with brief context]
- **Primary Abilities**: [Bulleted list with one-line descriptions]

## Biology
![[Biology/Evolutionary-Origins#Summary]]

## Society & Behavior
![[Society/Social-Structure#Summary]]

## Historical Significance
![[History/Current-Status#Summary]]

## Representatives
- **[[Representative 1]]**: [Brief description]
- **[[Representative 2]]**: [Brief description]

## Data Analysis
[Focused dataview queries]

## Related Species
- **[[Related Species 1]]**: [Nature of relationship]
- **[[Related Species 2]]**: [Nature of relationship]
```

### Biology Document Template

```markdown
# [Species Name]: [Biological Aspect]

## Summary {#summary}
[1 powerful paragraph summary that captures the key essence]

## Fundamental Mechanics
- **Origin**: [How this feature developed]
- **Function**: [Core purpose in concise terms]
- **Manifestation**: [How it physically manifests]

## Variations
| Variant | Description |
|---------|-------------|
| [Variant 1] | [Concise description] |
| [Variant 2] | [Concise description] |

## Evolutionary Significance
[Short paragraph on importance and impact]

> [!example] Notable Example
> [Brief specific instance highlighting this feature]

## Related Aspects
- [[Related Document 1]] - [Brief connection explanation]
- [[Related Document 2]] - [Brief connection explanation]

[Return to Hub Document]([[_Species-Name]])
```

### Society Document Template

```markdown
# [Species Name]: [Social Aspect]

## Summary {#summary}
[1 powerful paragraph summary capturing key aspects]

## Core Characteristics
- **Purpose**: [Function in species society]
- **Expression**: [How it manifests]
- **Evolution**: [How it developed over time]

## Behavioral Patterns
| Pattern | Manifestation |
|---------|---------------|
| [Pattern 1] | [Concise description] |
| [Pattern 2] | [Concise description] |

> [!note] Researcher Observation
> "[Brief, impactful observation]"

## Related Aspects
- [[Related Document 1]] - [Brief connection explanation]
- [[Related Document 2]] - [Brief connection explanation]

[Return to Hub Document]([[_Species-Name]])
```

### History Document Template

```markdown
# [Species Name]: [Historical Aspect]

## Summary {#summary}
[1 powerful paragraph summary that encapsulates key historical elements]

## Timeline Context
- **Period**: [When this occurred]
- **Location**: [Where this occurred]
- **Significance**: [Why it matters]

## Key Events
| Event | Impact |
|-------|--------|
| [Event 1] | [Concise description] |
| [Event 2] | [Concise description] |

> [!quote] Historical Record
> "[Brief, relevant quote from source]"

## Related Aspects
- [[Related Document 1]] - [Brief connection explanation]
- [[Related Document 2]] - [Brief connection explanation]

[Return to Hub Document]([[_Species-Name]])
```

## 7. Writing Style Guidelines

### Concision Strategies

1. **Strategic Atmospheric Writing**
   - One powerful, evocative paragraph rather than several
   - Place rich description in introduction, then shift to efficient delivery
   - Choose targeted sensory details rather than comprehensive description

2. **Information Density Techniques**
   - Convert narrative paragraphs to structured bullet points
   - Use tables for comparative information
   - Implement callout boxes for special information

3. **Stylistic Elements for Maximum Impact**
   - **Sensory Language**: Incorporate key sensory details
   - **Contrasting Scales**: Juxtapose cosmic scale with precise details
   - **Environmental Impact**: Describe effect on surroundings
   - **Implied History**: Let descriptions hint at deeper history

### Example: Concise But Atmospheric

**Preferred Style:**
> Titanus gojira's cellular structure evolved as nature's ultimate energy engine—dorsal plates capturing radiation like living solar arrays that illuminated in sequence before releasing their devastating atomic projection. This concentrated stream of superheated plasma varied between regional populations, with Northern variants producing focused, penetrating beams and Southern variants generating wider, heat-intensive projections.

## 8. Implementation Process

### Phase 1: Preparation

1. **Research and Structure**
   - Gather available information about the species
   - Set up hub document with complete metadata
   - Create folder structure for all shells
   - Prepare empty documents with appropriate metadata

### Phase 2: Content Development

1. **Write Summaries First**
   - Focus on the embedded summaries that will appear in hub document
   - Ensure these are self-contained while encouraging deeper reading

2. **Develop Core Content**
   - Expand each document with essential information
   - Use tables and bullet points for efficient information delivery
   - Add targeted atmospheric elements strategically

3. **Create Connections**
   - Document relationships with other species
   - Implement links between related documents
   - Create “Related Aspects” sections

### Phase 3: Integration

1. **Implement Queries**
   - Create dataview queries based on species characteristics
   - Generate representative lists with relevant metadata

2. **Final Review**
   - Verify consistent metadata implementation
   - Check all links and embeds function correctly
   - Ensure documents remain within word count guidelines
   - Add species to master index

## 9. Dataview Query Examples

### Hub Document Queries

```markdown
## Abilities Overview

```dataview
TABLE
  manifestations as "Manifestations",
  current_status as "Status"
FROM "Species/[Classification]/[Species-Name]/Biology"
WHERE component_category = "ability"
SORT file.name ASC
```

## Faction Analysis

```dataview
TABLE
  territory as "Territory",
  distinctive_traits as "Traits"
FROM "Species/[Classification]/[Species-Name]/Society"
WHERE component_category = "faction"
SORT file.name ASC
```

```

### Master Index Query

```markdown
## Ascendant Line Species

```dataview
TABLE
  status as "Status",
  living_representatives as "Representatives"
FROM "Species/Ascendant-Lines"
WHERE file.name startswith "_"
SORT file.name ASC
```

```

## 10. Special Considerations

### Ascendant Line Species
- Implement full shell structure
- Create detailed faction documentation where applicable
- Focus on distinctive abilities and evolutionary advantages

### Emergent Line Species
- Adapt shell structure based on complexity
- Focus on evolutionary trajectory and potential
- Emphasize relationship to Ascendant species

### Supporting Species
- Implement streamlined documentation
- Focus on ecological niche and relationship to dominant species

## 11. Implementation Checklist

- [ ] Hub Document with complete metadata
- [ ] Biology documents covering core aspects
- [ ] Society documents detailing social structure
- [ ] History documents covering key timeline events
- [ ] Cross-references between related documents
- [ ] Dataview queries implemented and functional
- [ ] Addition to master species index
```


