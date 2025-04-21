# Obsidian Organization Guide

## Introduction

This guide provides a structured approach to organizing your Antitheriomorphosis AU project within Obsidian. Based on analysis of your project knowledge, this universe centers around transformed Titans in human form, complex magical systems (Primus, Soul, and Psionics), and the evolving relationships between characters like Battra, Mothra, and Godzilla. This organization system will help you maintain consistency, discover narrative connections, and enhance your world-building through structured documentation.

## File Structure

### Root Organization

```
/Antitheriomorphosis/
├── _Introduction/
│   ├── Universe Overview.md
│   ├── Terminology Glossary.md
│   └── Timeline.md
│
├── Magic System/
│   ├── Core Concepts/
│   ├── Mechanics/
│   ├── Applications/
│   └── History/
│
├── Titans/
│   ├── Godzilla/
│   ├── Mothra/
│   ├── Battra/
│   ├── Rodan/
│   ├── Kong/
│   └── Other Titans/
│
├── Organizations/
│   ├── Monarch/
│   ├── Keep Charlie/
│   └── Historical Organizations/
│
├── Locations/
│   ├── Castle Bravo/
│   ├── Monster Island/
│   ├── Keep Charlie/
│   └── Other Locations/
│
├── Concepts/
│   ├── Antitheriomorphosis/
│   ├── The Null/
│   ├── Divine Mandate/
│   └── Other Key Concepts/
│
├── Narratives/
│   ├── Character Scenes/
│   ├── Historical Events/
│   ├── Current Timeline/
│   └── Planned Arcs/
│
└── Reference Materials/
    ├── Maps of Content/
    ├── Relationship Charts/
    ├── Development Notes/
    └── Research/
```

### Magic System Subfolders

```
/Antitheriomorphosis/Magic System/Core Concepts/
├── Primus/
│   ├── Primus - Fundamental Force.md
│   ├── Raw Primus Manipulation.md
│   ├── Primus Ignition.md
│   └── Primus Structure and Behavior.md
│
├── Soul/
│   ├── Basics of Mortal Soul.md
│   ├── Soul Infusion Process.md
│   ├── Soul Resonance.md
│   └── Soul-Primus Interface.md
│
├── Psionics/
│   ├── Psionic Fundamentals.md
│   ├── Psychic-Sorcery Interface.md
│   ├── Psionic Awakening.md
│   └── Mental Visualization.md
│
└── Null Phenomenon/
    ├── Null Species Classification.md
    ├── Godzilla as Null.md
    └── Bypassing Null Status.md
```

### Titans Subfolders (Example for Battra)

```
/Antitheriomorphosis/Titans/Battra/
├── Battra - Profile Overview.md
├── Lord of the Mystic Arts.md
├── Magical Abilities/
│   ├── Unparalleled Sorcery.md
│   ├── Raw Primus Manipulation.md
│   ├── Pocket Universe Creation.md
│   └── Combat Abilities.md
│
├── History/
│   ├── Origins and Early Life.md
│   ├── Exile and Cosmic Journey.md
│   ├── Atlantean Incident.md
│   └── Current Status.md
│
├── Relationships/
│   ├── Mothra Relationship.md
│   ├── Godzilla Relationship.md
│   ├── Keep Charlie Students.md
│   └── Monarch Relationship.md
│
└── Forms/
    ├── Human Form.md
    ├── Titan Form.md
    └── Transformation Abilities.md
```

## Tag-Based Organization

All tags must be tagged with `#atm` tag to centralize everything.

### Primary Tag Categories

```
#atm/magic/core/primus
#atm/magic/core/soul
#atm/magic/core/psionics
#atm/magic/core/null

#atm/magic/mechanics/spellcasting
#atm/magic/mechanics/optimization
#atm/magic/mechanics/commitments
#atm/magic/mechanics/visualization
#atm/magic/mechanics/incantation
#atm/magic/mechanics/spatial

#atm/magic/history/divine-mandate
#atm/magic/history/atlantis
#atm/magic/history/origin

#atm/titans/godzilla
#atm/titans/mothra
#atm/titans/battra
#atm/titans/rodan
#atm/titans/kong

#atm/organizations/monarch
#atm/organizations/keep-charlie

#atm/locations/castle-bravo
#atm/locations/monster-island

#atm/concepts/antitheriomorphosis
#atm/concepts/commitments
#atm/concepts/the-null

#atm/relationships/mothra-godzilla
#atm/relationships/battra-mothra
#atm/relationships/godzilla-battra

#atm/narratives/pre-transformation
#atm/narratives/post-transformation
#atm/narratives/historical
```

### Tag Usage Guidelines

1. **Hierarchical Structure**: Always use the full hierarchical path (#antitheriomorphosis/titans/battra rather than just #battra)
2. **Consistent Application**: Apply tags consistently across related files to ensure Dataview queries work properly
3. **Multiple Tags**: Apply all relevant tags to each file; don't limit to just one category
4. **Cross-Referencing**: Include relationship tags when documenting character interactions
5. **Search Enhancement**: Consider how you might search for content when applying tags

## Templates and Metadata

### Character Profile Template

```markdown
---
title: "{{title}}"
aliases: ["{{aliases}}"]
tags: [#atm/titans/{{titan_name}}, {{additional_tags}}]
related: [{{related_documents}}]
category: "Titans/{{titan_name}}"
created: {{date}}
last_modified: {{date}}
status: "{{development_status}}"
---

# {{title}}

> *"{{character_quote}}"*

## Overview

{{A concise introduction to the character, capturing their essence and most important traits}}

## Basic Profile

### Human Form

> [!info] Human Identity
> 
> - **Human Name:** {{human_name}}
> - **Documented Age:** {{documented_age}} (Monarch records)
> - **Actual Age:** {{actual_age}}
> - **Race:** {{race}}
> - **Affiliation:** {{affiliations}}
> - **Status:** {{status}}
> - **Titles:** {{titles}}

### Titan Form

> [!info] Titan Identity
> 
> - **Species:** {{species}}
> - **Height:** {{height}}
> - **Weight:** {{weight}}
> - **Status:** {{titan_status}}

## Physical Appearance

### Human Form

#### Basic Traits

{{Description of human appearance and distinctive features}}

| Attribute       | Description                                           |
| --------------- | ----------------------------------------------------- |
| **Height**      | {{height_human}}                                      |
| **Weight**      | {{weight_human}}                                      |
| **Build**       | {{build_description}}                                 |
| **Hair**        | {{hair_description}}                                  |
| **Eyes**        | {{eyes_description}}                                  |
| **Skin**        | {{skin_description}}                                  |
| **Features**    | {{distinctive_features}}                              |

#### Movement and Presence

{{How the character carries themselves and their impact on surroundings}}

#### Power Manifestation

{{How their Titan abilities appear in human form}}

### Titan Form

{{Description of Titan appearance and distinctive features}}

### Clothing Preferences

{{Typical attire and styling choices}}

## Abilities & Powers

> [!quote] {{ability_quote}}
> {{ability_quote_text}}

### Core Abilities

{{List and description of primary powers and abilities}}

### Combat Abilities

{{Fighting style, techniques, and combat approach}}

### Weaknesses

{{Limitations and vulnerabilities}}

## Early Life & Formative Experiences

{{Background and key events that shaped the character}}

## Cultural Heritage

{{Species background, traditions, and identity}}

## Behavior, Mindset and Philosophy

{{Character's worldview, values, and psychological traits}}

## Notable Relationships

> [!info] Key Relationships
> {{Brief overview of relationship dynamics}}

### {{Relationship 1}}

{{Detailed exploration of this relationship}}

### {{Relationship 2}}

{{Detailed exploration of this relationship}}

## History

{{Significant events in character's timeline}}

> [!note] Major Events
> - {{event_1}}
> - {{event_2}}
> - {{event_3}}

## Personal Interests

{{Hobbies, preferences, and activities}}

## Character Arc

{{Current developmental trajectory}}

## Trivia

> [!tip] Interesting Facts
> - {{fact_1}}
> - {{fact_2}}
> - {{fact_3}}
```

### Magic System Template

```markdown
---
title: "{{title}}"
aliases: ["{{aliases}}"]
tags: [#atm/magic/{{magic_category}}/{{magic_subcategory}}, {{additional_tags}}]
related: [{{related_documents}}]
category: "Magic System/{{category_path}}"
created: {{date}}
last_modified: {{date}}
concept_type: "{{concept_type}}"
status: "{{development_status}}"
complexity: "{{complexity_level}}"
---

# {{title}}

## Definition & Nature

{{A concise definition of the magical concept and its fundamental characteristics}}

## Core Properties

- **{{Property 1}}**: {{Description with emphasis on how this property manifests}}
- **{{Property 2}}**: {{Description with emphasis on how this property manifests}}
- **{{Property 3}}**: {{Description with emphasis on how this property manifests}}
- **{{Property 4}}**: {{Description with emphasis on how this property manifests}}

## Mechanism of Action

{{Detailed explanation of how this concept operates within the magical framework}}

### Primary Functions

1. **{{Function 1}}**: {{How this function operates and its significance}}
2. **{{Function 2}}**: {{How this function operates and its significance}}
3. **{{Function 3}}**: {{How this function operates and its significance}}

### Limitations & Constraints

- {{Limitation 1}} - {{Explanation of how/why this limitation exists}}
- {{Limitation 2}} - {{Explanation of how/why this limitation exists}}
- {{Limitation 3}} - {{Explanation of how/why this limitation exists}}

## Relationship to Other Concepts

### {{Related Concept 1}}
{{Explanation of the relationship between concepts}}

### {{Related Concept 2}}
{{Explanation of the relationship between concepts}}

## Historical Context

{{Information about the discovery, development, or evolution of understanding}}

## Notable Practitioners

- **{{Practitioner 1}}**: {{Their unique approach or relationship to this concept}}
- **{{Practitioner 2}}**: {{Their unique approach or relationship to this concept}}

## Examples In Action

### Example 1: {{Title}}
{{Detailed example showing the concept in action}}

## Research Notes

{{Meta-commentary on areas for further development}}
```

### Narrative Scene Template

```markdown
---
title: "{{title}}"
aliases: ["{{aliases}}"]
tags: [#atm/narratives/{{narrative_type}}, {{character_tags}}, {{location_tags}}]
related: [{{related_documents}}]
characters: [{{primary_characters}}]
locations: [{{scene_locations}}]
created: {{date}}
last_modified: {{date}}
status: "{{status}}"
timeline_position: "{{timeline_position}}"
---

# {{title}}

## Setting
- **Location:** {{location}}
- **Time:** {{time_period}}
- **Context:** {{contextual_information}}

## Characters Present
- {{character_1}} - {{brief_role}}
- {{character_2}} - {{brief_role}}

## Narrative

{{narrative_content}}

## Connection Points

### Previous Events
- {{connection_to_previous_1}}
- {{connection_to_previous_2}}

### Future Implications
- {{future_implication_1}}
- {{future_implication_2}}

## Notes
{{additional_notes}}
```

## Dataview Integration

### Basic Query Syntax

```
```dataview
TABLE 
  property1 as "Display Name 1",
  property2 as "Display Name 2"
FROM #tag1 OR #tag2
WHERE condition
SORT property ASC/DESC
LIMIT number
```

```

### Essential Queries

#### List All Titan Profiles

```

```dataview
TABLE 
  title as "Character",
  file.folder as "Category",
  status as "Status"
FROM #atm/titans
SORT file.folder ASC, title ASC
```

```

#### Find Character Relationships

```

```dataview
TABLE
  file.link as "Relationship Document",
  created as "Created Date"
FROM #atm/relationships
WHERE contains(file.name, "Battra") OR contains(file.tags, "#atm/titans/battra")
SORT file.name ASC
```

```

#### Track Magic System Development

```

```dataview
TABLE
  status as "Status",
  complexity as "Complexity",
  file.folder as "Category"
FROM #atm/magic
GROUP BY status
```

```

#### Character Narrative Scenes

```

```dataview
TABLE
  title as "Scene",
  timeline_position as "Timeline",
  characters as "Characters"
FROM #atm/narratives
WHERE contains(characters, "Mothra") AND contains(characters, "Godzilla")
SORT timeline_position ASC
```

```

## Knowledge Dashboards

### Universe Overview Dashboard

Create a central dashboard file that provides navigation to key universe elements:

```markdown
# Antitheriomorphosis AU: Master Reference

## Core Concepts
- [[Antitheriomorphosis Phenomenon]] #atm/concepts/antitheriomorphosis
- [[The Divine Mandate Against Sorcery]] #atm/magic/history/divine-mandate
- [[The Null Phenomenon]] #atm/concepts/the-null

## Primary Characters
- [[Godzilla, the King of the Monsters]] #atm/titans/godzilla
- [[Mothra, the Queen of the Monsters]] #atm/titans/mothra
- [[Battra, the Lord of the Mystic Arts]] #atm/titans/battra
- [[Kong, King of the Hollow Earth]] #atm/titans/kong

## Magic System
- [[Primus, the Foundation of Magic]] #atm/magic/core/primus
- [[The Basics of the Mortal Soul]] #atm/magic/core/soul
- [[Commitments Overview]] #atm/magic/mechanics/commitments

## Organizations
- [[Monarch]] #atm/organizations/monarch
- [[Keep Charlie]] #atm/organizations/keep-charlie

## Key Relationships
- [[Mothra and Godzilla's Relationship]] #atm/relationships/mothra-godzilla
- [[The Divine Twins: Battra and Mothra]] #antitheriomorphosis/relationships/battra-mothra

## Timeline
- [[Atlantean Golden Age]] #atm/magic/history/atlantis
- [[The Xillien Invasion]] #atm/narratives/historical
- [[Post-Transformation Timeline]] #atm/narratives/post-transformation

## Current Development Focus
```dataview
TABLE
  status as "Status",
  file.folder as "Category"
FROM #atm
WHERE status = "development"
SORT file.mtime DESC
LIMIT 5
```

## Recent Updates

```dataview
TABLE
  file.mtime as "Last Modified"
FROM #atm
SORT file.mtime DESC
LIMIT 5
```

```

### Character-Specific Dashboards

Create specialized dashboards for your main characters:

#### Battra Dashboard

```markdown
# Battra, Lord of the Mystic Arts: Reference Dashboard

## Character Documents
```dataview
TABLE
  title as "Document",
  file.folder as "Category",
  status as "Status"
FROM #atm/titans/battra
SORT file.folder ASC, title ASC
```

## Magical Abilities

```dataview
TABLE
  title as "Ability",
  status as "Status"
FROM #atm/magic
WHERE contains(file.content, "Battra") AND contains(file.content, "ability")
SORT title ASC
```

## Relationships

```dataview
TABLE
  title as "Relationship",
  file.mtime as "Last Updated"
FROM #atm/relationships
WHERE contains(file.content, "Battra")
SORT title ASC
```

## Narrative Appearances

```dataview
TABLE
  title as "Scene",
  timeline_position as "Timeline"
FROM #atm/narratives
WHERE contains(characters, "Battra")
SORT timeline_position ASC
```

```

## Workflow Recommendations

### Initial Project Setup

1. **Create Folder Structure**: Set up the hierarchical folder organization
2. **Install Essential Plugins**: 
   - Dataview (for queries)
   - Templater (for templates)
   - Calendar (for timeline visualization)
   - Kanban (for development tracking)
   - Excalidraw (for relationship mapping)

3. **Set Up Templates**: Create your primary templates:
   - Character profiles
   - Magic system elements
   - Narrative scenes
   - Location descriptions

4. **Establish Key MOCs**: Create initial Maps of Content:
   - Universe overview
   - Character index
   - Magic system overview
   - Timeline reference

### Content Development Process

1. **Foundation First**: Begin with core structural elements
   - Document the Antitheriomorphosis phenomenon
   - Define the main Titan characters
   - Establish the magic system fundamentals

2. **Build Characters**: Develop detailed character profiles
   - Human and Titan forms
   - Abilities and powers
   - Background and history
   - Psychological profile

3. **Establish Relationships**: Document key relationships
   - Create relationship maps using Excalidraw
   - Document specific character dynamics
   - Capture relationship histories

4. **Expand World Elements**: Broaden your universe
   - Develop key locations
   - Build out organizations
   - Refine historical events

5. **Create Narratives**: Write character-focused scenes
   - Develop key character moments
   - Capture pivotal interactions
   - Create coherent narrative arcs

### Ongoing Maintenance

1. **Regular Reviews**: Schedule periodic reviews of story elements
2. **Consistency Checks**: Verify details remain consistent across documents
3. **Gap Analysis**: Use Dataview to identify underdeveloped areas
4. **Update Timeline**: Maintain chronological coherence as you develop

## Development Approach for Narrative Writers

For writers who focus primarily on narrative first (like you mentioned with your interest in immersive narratives and dynamic character interactions), consider this workflow:

1. **Scene-First Writing**:
   - Write your narrative scenes based on creative inspiration
   - Tag them with temporary markers (#needs-integration)
   - Focus on character voice and emotional authenticity

2. **Integration Phase**:
   - After writing, extract worldbuilding elements
   - Create or update relevant reference documents
   - Ensure consistency with existing materials
   - Remove temporary tags once integrated

3. **Cross-Referencing**:
   - Link narrative scenes to character profiles and concepts
   - Update character development notes based on scenes
   - Use dataview to track character arcs across multiple scenes

4. **Narrative Threading**:
   - Use dataview to create reading orders and story arcs
   - Develop dashboard views that show narrative progression
   - Track emotional arcs and character development

## Troubleshooting and Maintenance

### Common Issues

#### Handling Contradictions
- Create a dedicated "Canon Conflicts" note to track discrepancies
- Resolve contradictions by explicitly choosing a canonical version
- Update all related documents to reflect the resolution

#### Managing Complexity
- Create visual relationship maps for complex interconnections
- Use progressive disclosure in dashboards (collapsible sections)
- Develop summary documents for major concepts

#### Balancing Detail and Progress
- Create "stub" documents for planned content
- Use status tags (#stub, #needs-expansion, #complete)
- Prioritize depth for central elements, breadth for peripheral ones

### System Evolution

As your universe develops:

1. **Version Your Canon**: When significant changes occur, note version shifts
2. **Document Retcons**: When you need to revise established elements, explicitly note the changes
3. **Track Development**: Use the Kanban plugin to visualize project progress
4. **Reader's Guides**: Create reading pathways for different entry points to your universe

## Conclusion

This organizational system provides a framework for documenting, exploring, and developing your Antitheriomorphosis AU based on the rich foundation you've established. By combining hierarchical file organization, consistent tagging, powerful templates, and Dataview integration, you'll create a dynamic knowledge base that grows with your creative vision.

The structure respects the core elements of your universe—transformed Titans, complex magic systems, and evolving relationships—while accommodating narrative development and creative exploration. As your universe evolves, this organization will help maintain consistency while allowing for creative expansion.