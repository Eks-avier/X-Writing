# Titanus Gojira: Atomic Knowledge Base Implementation Instructions

## Overview

These instructions will guide you in transforming the monolithic “Titanus Gojira.md” species profile into an interconnected atomic knowledge base using Obsidian's capabilities. The atomic model divides content into specialized documents while maintaining connections through a hub-and-spoke architecture.

## Core Architecture

Implement a nucleus-electron shell model with:

1. **Nucleus Document**: Central hub for navigation and overview
2. **Inner Shell**: Core biological aspects (evolution, abilities)
3. **Middle Shell**: Societal aspects (factions, communication)
4. **Outer Shell**: Historical aspects (decline, legacy)

## File Structure

Create the following folder and file structure:

```
Species/Titanus-Gojira/
├── _Titanus Gojira.md             # Nucleus document
├── Core/                              # Inner Shell
│   ├── Evolutionary Origins.md
│   ├── Limitless Adaptation.md
│   ├── Energy Domination.md
│   ├── Ascendant Line.md
│   └── Reproductive Biology.md
├── Societal/                          # Middle Shell
│   ├── Factional Overview.md
│   ├── Northern Faction.md
│   ├── Southern Faction.md
│   ├── Eastern Faction.md
│   ├── Western Faction.md
│   ├── Hierarchy of Priorities.md
│   └── Energy Communication.md
└── Historical/                        # Outer Shell
    ├── Decline and Extinction.md
    ├── MUTO Relationship.md
    ├── Current Status.md
    ├── Godzilla Legacy.md
    └── Titanus Zilla Relationship.md
```

## Metadata Requirements

### Hub Document Metadata

```yaml
---
title: "Titanus gojira"
alias: 
  - "Gojira" 
  - "Northern Gojira"
  - "Southern Gojira"
  - "Eastern Gojira"
  - "Western Gojira"
component_type: species
component_category: titan_biology
related_entities:
  - "[[Godzilla]]"
  - "[[Titanus zilla]]"
  - "[[Titanus jinshin-mushi|MUTO]]"
species_status: Near-extinct
last_pure_member: "[[Godzilla]]"
core_abilities:
  - "[[Limitless Adaptation]]"
  - "[[Domination of Energy]]"
tags:
  - atm
  - atm/species/titanus_gojira
  - atm/species/classification/ascendant_line
---
```

### Core Document Metadata

```yaml
---
title: "Titanus gojira: [Aspect Name]"
parent: "[[Titanus Gojira]]"
component_type: [ability/biological/evolutionary]
component_category: [appropriate category]
related_abilities:
  - "[[Related Ability 1]]"
  - "[[Related Ability 2]]"
ability_manifestations: [for ability documents]
ability_status: [Current status]
tags:
  - atm
  - atm/species/titanus_gojira
  - atm/[appropriate tag category]
---
```

### Societal Document Metadata

```yaml
---
title: "Titanus gojira: [Faction/Aspect Name]"
parent: "[[Titanus Gojira]]"
component_type: [faction/communication/hierarchy]
component_category: [appropriate category]
faction_name: [for faction documents]
territory: [for faction documents]
extinction_timeframe: [for faction documents]
distinctive_traits: [list for faction documents]
related_factions: [for faction documents]
tags:
  - atm
  - atm/species/titanus_gojira
  - atm/[appropriate tag category]
---
```

### Historical Document Metadata

```yaml
---
title: "Titanus gojira: [Historical Aspect]"
parent: "[[Titanus Gojira]]"
component_type: historical
component_category: [appropriate category]
species_status: [for extinction documents]
extinction_cause: [for extinction documents]
extinction_timeframe: [for extinction documents]
related_documents:
  - "[[Related Document 1]]"
  - "[[Related Document 2]]"
tags:
  - atm
  - atm/species/titanus_gojira
  - atm/history/[appropriate tag]
---
```

## Implementation Process

### Phase 1: Create Framework (Complete First)

1. **Create Hub Document**
   * Implement `_Titanus-Gojira-Hub.md` with complete metadata
   * Include introduction section from original document
   * Create skeleton structure with section headings
   * Add placeholder dataview queries

2. **Create All Document Files**
   * Create all files in the structure with proper naming conventions
   * Add metadata headers to each document
   * Include document title as first heading

### Phase 2: Content Division (Complete Second)

1. **Distribute Content by Topic**
   * Analyze original document to identify logical content divisions
   * Extract content blocks and place in appropriate documents
   * Maintain original tone, style, and descriptive quality
   * Identify and preserve all quotes, examples, and callouts

2. **Maintain Completeness**
   * Ensure no content from original is lost in the division process
   * Check extracted sections for context that might need to be included
   * Add transitional text where needed for coherence

3. **Implement Structural Elements**
   * Create consistent section headings within each document
   * Implement bullet lists, tables, and callout blocks
   * Add summary sections at the beginning of each document

### Phase 3: Connections & Enhancement (Complete Last)

1. **Create Cross-References**
   * Add links between related documents
   * Implement bidirectional linking
   * Create embed blocks for key content in hub document
   * Add “Related Documents” sections with contextual descriptions

2. **Implement Dataview Queries**
   * Add the following queries to the hub document:

```markdown
## Factional Analysis

```dataview
TABLE
  territory as "Territory",
  distinctive_traits as "Distinctive Traits"
FROM "Species/Titanus Gojira/Societal"
WHERE contains(file.name, "Faction") AND file.name != "Factional Overview"
SORT file.name ASC
```

## Core Abilities

```dataview
TABLE
  ability_manifestations as "Manifestations",
  ability_status as "Current Status"
FROM "Species/Titanus Gojira/Core"
WHERE component_type = "ability"
```

## Extinction Timeline

```dataview
TABLE WITHOUT ID
  file.name as "Faction",
  extinction_timeframe as "Extinction Period",
  row.extinction_cause as "Primary Cause"
FROM "Species/Titanus Gojira/Societal"
WHERE contains(file.name, "Faction") AND file.name != "Factional Overview"
FLATTEN "Specialized MUTO parasitism" as extinction_cause
SORT extinction_timeframe ASC
```

```

3. **Add Navigation Elements**
   * Create "Back to Hub" links at the end of each document
   * Add "Related Documents" sections
   * Implement consistent section navigation

## Document Templates

### Hub Document Template

```markdown
# Titanus Gojira

## Introduction

The *Titanus gojira* emerged from Earth's primordial oceans as living dynamos—beings of extraordinary power whose very cells converted radiation into usable energy with an efficiency no other species has matched.

> [!quote] Monarch Field Notes
> "The skeletal and tissue samples from *Titanus gojira* specimens reveal cellular structures unlike anything in Earth's current biosphere—radiation conversion mechanisms so efficient they border on theoretical impossibility."

## Species Overview

![[Species/Titanus Gojira/Core/Evolutionary Origins#Summary]]

## Core Abilities

- **[[Limitless Adaptation]]**: Unprecedented capacity for biological evolution within a single lifespan
- **[[Energy Domination]]**: Universal control over all forms of energy, far beyond elemental affinity

## Factional Divisions

The species developed four distinct regional variations:

- **[[Northern Faction|Northern Gojira]]**: Adapted to arctic environments with superior energy conservation
- **[[Southern Faction|Southern Gojira]]**: Adapted to volcanic regions with superior heat manipulation
- **[[Eastern Faction|Eastern Gojira]]**: Adapted to coastal environments with superior aquatic capabilities
- **[[Western Faction|Western Gojira]]**: Adapted to diverse continental environments with superior versatility

[Dataview Queries Will Be Placed Here]

## Current Status

![[Species/Titanus-Gojira/Historical/Current-Status#Summary]]

## Related Entities

- [[Godzilla, the King of the Monsters|Godzilla]] - Last pure member of the species
- [[Titanus zilla]] - Hybrid descendant with partial genetic legacy
- [[Titanus jinshin-mushi|MUTO]] - Specialized parasite evolved to target the species
```

### Core Document Template

```markdown
# [Aspect Name]

## Summary

[1-2 paragraph summary that encapsulates the key aspects of this topic]

## [Main Section 1]

[Detailed content with rich description maintaining the original tone]

### [Subsection 1.1]

[Content with examples, details, and references]

### [Subsection 1.2]

[Content with examples, details, and references]

## [Main Section 2]

[Content organization following logical progression]

> [!example] [Example Title]
> [Example content preserved from original document]

## Related Aspects

- [[Related Document 1]] - [Brief explanation of relationship]
- [[Related Document 2]] - [Brief explanation of relationship]

[Return to Hub Document](_Titanus-Gojira-Hub.md)
```

## Content Creation Guidelines

### 1. Preserve Descriptive Quality

* Maintain the rich, evocative language from the original document
* Keep the sense of ancient cosmic significance in descriptions
* Preserve all quotes, examples, and special callouts
* Ensure the writing conveys the weight and power of the species

### 2. Implement Formatting Consistently

* Use level 1 heading (`#`) only for document title
* Use level 2 headings (`##`) for major sections
* Use level 3 headings (`###`) for subsections
* Use bullet lists for trait collections
* Use numbered lists for sequential processes
* Use tables for comparative information
* Use blockquotes for quotes from characters or sources
* Use callout blocks for examples, important notes, and warnings

### 3. Create Effective Summaries

* Begin each document with a 1-2 paragraph summary section
* Create block reference targets for these summaries using heading ID: `## Summary {#summary}`
* These summaries will be embedded in the hub document
* Summaries should stand alone while encouraging further reading

### 4. Implement Cross-References Properly

* Use wiki-style links for all references to other documents
* When first mentioning another document in the text, create a link
* Add a “Related Aspects” section at the end of each document
* Include contextual descriptions for why documents are related

## Topic-Specific Instructions

### Core Abilities Documentation

* Create separate documents for each core ability (Limitless Adaptation, Energy Domination)
* Explain the fundamental mechanisms in detail
* Compare species-wide expression versus Godzilla's refined version
* Document how the abilities manifested differently across factions
* Include specific examples of ability applications

### Factional Documentation

* Create consistent structure across faction documents
* Include common sections: Territory, Physical Characteristics, Cultural Emphasis, Energy Application
* Use comparative language to highlight differences between factions
* Create connections to current characters where relevant (especially Godzilla's Northern heritage)

### Extinction Documentation

* Create clear timeline of progressive factional extinction
* Document specific causes for each faction's decline
* Connect to MUTO evolution and specialized predation
* Explore theoretical versus actual extinction causes
* Create connection to current status and Titanus zilla relationship

## Final Output Requirements

The completed knowledge base should:

1. Contain all files specified in the file structure
2. Maintain all information from the original document
3. Feature rich interlinking between documents
4. Include working dataview queries in the hub document
5. Implement consistent formatting throughout
6. Maintain the original tone and descriptive quality
7. Provide clear navigation paths between documents

This atomic approach transforms the monolithic species profile into an interconnected knowledge network that enhances discoverability, comprehension, and future expandability.