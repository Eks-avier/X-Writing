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

### Primary Tag Categories (Example Format)

```yaml
tags:
  - #atm/magic/core/primus
  - #atm/magic/core/soul
  - #atm/magic/core/psionics
  - #atm/magic/core/null

  - #atm/magic/mechanics/spellcasting
  - #atm/magic/mechanics/optimization
  - #atm/magic/mechanics/commitments
  - #atm/magic/mechanics/visualization
  - #atm/magic/mechanics/incantation
  - #atm/magic/mechanics/spatial

  - #atm/magic/history/divine-mandate
  - #atm/magic/history/atlantis
  - #atm/magic/history/origin

  - #atm/titans/godzilla
  - #atm/titans/mothra
  - #atm/titans/battra
  - #atm/titans/rodan
  - #atm/titans/kong

  - #atm/organizations/monarch
  - #atm/organizations/keep-charlie

  - #atm/locations/castle-bravo
  - #atm/locations/monster-island

  - #atm/concepts/antitheriomorphosis
  - #atm/concepts/commitments
  - #atm/concepts/the-null

  - #atm/relationships/mothra-godzilla
  - #atm/relationships/battra-mothra
  - #atm/relationships/godzilla-battra

  - #atm/narratives/pre-transformation
  - #atm/narratives/post-transformation
  - #atm/narratives/historical
```

### Tag Usage Guidelines

1.  **Base Tag**: Always include the `#atm` tag in your frontmatter list for global categorization.
2.  **Hierarchical Structure**: Always use the full hierarchical path (e.g., `#atm/titans/battra` rather than just `#battra`) for specific categorization.
3.  **Consistent Application**: Apply tags consistently across related files to ensure Dataview queries work properly.
4.  **Multiple Tags**: Apply all relevant tags to each file; don't limit to just one category.
5.  **Cross-Referencing**: Include relationship tags when documenting character interactions.
6.  **Search Enhancement**: Consider how you might search for content when applying tags.

## Templates and Metadata

### Character Profile Template

```markdown
---
title: "{{title}}"
aliases: ["{{aliases}}"]
tags:
  - #atm
  - #atm/titans/{{titan_name}}
  # Add specific character tags like #atm/titans/battra if not using templater for titan_name
  # Add additional descriptive tags below
  - {{additional_tags}}
related: [{{related_documents}}]
category: "Titans/{{titan_name}}"
created: {{date}}
last_modified: {{date}}
status: "{{development_status}}" # e.g., draft, development, complete
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
> - **Race:** {{race}} # e.g., Human (Transformed Titan), Atlantean, etc.
> - **Affiliation:** {{affiliations}} # e.g., Monarch, Keep Charlie, Independent
> - **Status:** {{status}} # e.g., Active, Dormant, Deceased
> - **Titles:** {{titles}} # e.g., King of the Monsters, Lord of the Mystic Arts

### Titan Form

> [!info] Titan Identity
>
> - **Species:** {{species}} # e.g., Titanus Gojira, Titanus Mosura, Titanus Battra
> - **Height:** {{height}}
> - **Weight:** {{weight}}
> - **Status:** {{titan_status}} # e.g., Active, Alpha, Subordinate

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

{{How their Titan abilities appear subtly or overtly in human form}}

### Titan Form

{{Description of Titan appearance and distinctive features}}

### Clothing Preferences

{{Typical attire and styling choices}}

## Abilities & Powers

> [!quote] {{ability_quote}}
> {{ability_quote_text}}

### Core Abilities

{{List and description of primary powers and abilities derived from their Titan nature or magical skills}}

### Combat Abilities

{{Fighting style, techniques, and combat approach}}

### Weaknesses

{{Limitations and vulnerabilities, both physical and psychological}}

## Early Life & Formative Experiences

{{Background and key events that shaped the character before and after transformation}}

## Cultural Heritage

{{Species background, traditions, and identity associated with their Titan lineage}}

## Behavior, Mindset and Philosophy

{{Character's worldview, values, motivations, and psychological traits}}

## Notable Relationships

> [!info] Key Relationships
> {{Brief overview of relationship dynamics}}

### [[{{Relationship 1 Link}}]]
{{Detailed exploration of this relationship}}

### [[{{Relationship 2 Link}}]]
{{Detailed exploration of this relationship}}

## History

{{Significant events in character's timeline}}

> [!note] Major Events
> - {{event_1}}
> - {{event_2}}
> - {{event_3}}

## Personal Interests

{{Hobbies, preferences, and activities outside of main duties/conflicts}}

## Character Arc

{{Current developmental trajectory and potential future development}}

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
tags:
  - #atm
  - #atm/magic/{{magic_category}}/{{magic_subcategory}}
  # Add additional descriptive tags below
  - {{additional_tags}}
related: [{{related_documents}}]
category: "Magic System/{{category_path}}"
created: {{date}}
last_modified: {{date}}
concept_type: "{{concept_type}}" # e.g., Core Force, Mechanic, Phenomenon
status: "{{development_status}}" # e.g., brainstorming, defined, refined
complexity: "{{complexity_level}}" # e.g., low, medium, high
---

# {{title}}

## Definition & Nature

{{A concise definition of the magical concept and its fundamental characteristics within the Antitheriomorphosis universe}}

## Core Properties

- **{{Property 1}}**: {{Description with emphasis on how this property manifests}}
- **{{Property 2}}**: {{Description with emphasis on how this property manifests}}
- **{{Property 3}}**: {{Description with emphasis on how this property manifests}}
- **{{Property 4}}**: {{Description with emphasis on how this property manifests}}

## Mechanism of Action

{{Detailed explanation of how this concept operates within the magical framework (Primus, Soul, Psionics interface)}}

### Primary Functions

1.  **{{Function 1}}**: {{How this function operates and its significance}}
2.  **{{Function 2}}**: {{How this function operates and its significance}}
3.  **{{Function 3}}**: {{How this function operates and its significance}}

### Limitations & Constraints

- {{Limitation 1}} - {{Explanation of how/why this limitation exists, e.g., Null interference, Soul capacity, Commitment cost}}
- {{Limitation 2}} - {{Explanation of how/why this limitation exists}}
- {{Limitation 3}} - {{Explanation of how/why this limitation exists}}

## Relationship to Other Concepts

### [[{{Related Concept 1 Link}}]]
{{Explanation of the interaction or dependency between concepts}}

### [[{{Related Concept 2 Link}}]]
{{Explanation of the interaction or dependency between concepts}}

## Historical Context

{{Information about the discovery, development, or evolution of understanding this concept, potentially linking to Atlantis, Divine Mandate, etc.}}

## Notable Practitioners / Manifestations

- **{{Practitioner/Example 1}}**: {{Their unique approach, mastery, or relationship to this concept (e.g., Battra's unparalleled sorcery)}}
- **{{Practitioner/Example 2}}**: {{Their unique approach, mastery, or relationship to this concept}}

## Examples In Action

### Example 1: {{Title}}
{{Detailed example showing the concept in action, perhaps linking to a specific scene or event}}

## Research Notes

{{Meta-commentary on areas for further development, inconsistencies, or open questions}}
```

### Narrative Scene Template

```markdown
---
title: "{{title}}"
aliases: ["{{aliases}}"]
tags:
  - #atm
  - #atm/narratives/{{narrative_type}} # e.g., character-scene, historical-event, planned-arc
  # Add specific character tags like #atm/titans/battra if present
  # Add specific location tags like #atm/locations/keep-charlie if relevant
  - {{character_tags}}
  - {{location_tags}}
related: [{{related_documents}}] # Links to concepts, characters, locations involved
characters: [{{primary_characters}}] # List of character names (linkable: [[Battra]], [[Mothra]])
locations: [{{scene_locations}}] # List of locations (linkable: [[Keep Charlie]], [[Castle Bravo]])
created: {{date}}
last_modified: {{date}}
status: "{{status}}" # e.g., idea, draft, first-pass, final
timeline_position: "{{timeline_position}}" # e.g., Post-Transformation Year 2, Atlantean Era, Specific Date
---

# {{title}}

## Setting
- **Location:** [[{{location}}]]
- **Time:** {{time_period}}
- **Context:** {{contextual_information leading into the scene}}

## Characters Present
- [[{{character_1}}]] - {{brief_role or state in scene}}
- [[{{character_2}}]] - {{brief_role or state in scene}}
- (Add more as needed)

## Narrative

{{Paste or write the scene content here. Use standard markdown formatting.}}

## Connection Points

### Previous Events
- Links to or brief description of preceding scenes/events: [[{{Previous Scene Link}}]]
- {{connection_to_previous_2}}

### Future Implications
- How this scene sets up future events or character development: [[{{Future Arc Link}}]]?
- {{future_implication_2}}

## Notes
{{Any additional author notes, questions about the scene, continuity checks needed, etc.}}
```

## Dataview Integration

### Basic Query Syntax

```dataview
TABLE 
  property1 as "Display Name 1",
  property2 as "Display Name 2"
FROM #tag1 OR #tag2
WHERE condition
SORT property ASC/DESC
LIMIT number
```

*(Dataview queries remain the same as they query based on tags existing, not the specific format within the YAML block)*

### Essential Queries

#### List All Titan Profiles

```dataview
TABLE 
  title as "Character",
  file.folder as "Category",
  status as "Status"
FROM #atm/titans AND -"Templates" /* Exclude template files if they exist */
SORT file.folder ASC, title ASC
```

#### Find Character Relationships

```dataview
TABLE
  file.link as "Relationship Document",
  created as "Created Date"
FROM #atm/relationships AND -"Templates"
WHERE contains(file.name, "Battra") OR contains(file.tags, "#atm/titans/battra")
SORT file.name ASC
```

*Note: This query finds relationship *files* specifically tagged or named. You might need to adjust if relationship info is embedded within character profiles.*

#### Track Magic System Development

```dataview
TABLE
  status as "Status",
  complexity as "Complexity",
  file.folder as "Category"
FROM #atm/magic AND -"Templates"
WHERE status != null /* Only show files where status is set */
GROUP BY status
```

#### Character Narrative Scenes

```dataview
TABLE
  title as "Scene",
  timeline_position as "Timeline",
  characters as "Characters"
FROM #atm/narratives AND -"Templates"
WHERE contains(characters, "[[Mothra]]") AND contains(characters, "[[Godzilla]]") /* Assumes linked character names in YAML */
SORT timeline_position ASC
```

*Note: Ensure character names in the template's `characters` field are consistently formatted, ideally as links like `[[Mothra]]`.*

## Knowledge Dashboards

*(Dashboard structure remains the same, relying on the tags and links defined)*

### Universe Overview Dashboard

```markdown
# Antitheriomorphosis AU: Master Reference

## Core Concepts
- [[Universe Overview]] `="_Introduction/Universe Overview"`
- [[Antitheriomorphosis Phenomenon]] `#atm/concepts/antitheriomorphosis`
- [[The Divine Mandate Against Sorcery]] `#atm/magic/history/divine-mandate`
- [[The Null Phenomenon]] `#atm/concepts/the-null`

## Primary Characters
- [[Godzilla - Profile Overview]] `#atm/titans/godzilla`
- [[Mothra - Profile Overview]] `#atm/titans/mothra`
- [[Battra - Profile Overview]] `#atm/titans/battra`
- [[Kong - Profile Overview]] `#atm/titans/kong`

## Magic System
- [[Primus - Fundamental Force]] `#atm/magic/core/primus`
- [[Basics of Mortal Soul]] `#atm/magic/core/soul`
- [[Commitments Overview]] `#atm/magic/mechanics/commitments` *(Assuming you create this overview note)*

## Organizations
- [[Monarch]] `#atm/organizations/monarch` *(Create Monarch profile note)*
- [[Keep Charlie]] `#atm/organizations/keep-charlie` *(Create Keep Charlie profile note)*

## Key Relationships
- [[Mothra Relationship]] `#atm/relationships/mothra-godzilla` *(Example name, adjust to your actual file)*
- [[Battra Relationship]] `#atm/relationships/battra-mothra` *(Example name, adjust to your actual file)*

## Timeline
- [[Timeline]] `="_Introduction/Timeline"`
- [[Atlantean Incident]] `#atm/magic/history/atlantis` *(Example name, adjust to your actual file)*
- [[Historical Events]] `#atm/narratives/historical` *(Link to a narrative MOC or specific event)*
- [[Current Timeline]] `#atm/narratives/current-timeline` *(Link to a narrative MOC or specific event)*

## Current Development Focus
```dataview
TABLE
  status as "Status",
  file.folder as "Category"
FROM #atm AND -"Templates"
WHERE status = "development" OR status = "draft" OR status = "brainstorming"
SORT file.mtime DESC
LIMIT 10
```

## Recent Updates

```dataview
TABLE
  file.mtime as "Last Modified"
FROM #atm AND -"Templates"
SORT file.mtime DESC
LIMIT 10
```

```

### Character-Specific Dashboards

#### Battra Dashboard

```markdown
# Battra, Lord of the Mystic Arts: Reference Dashboard

## Character Documents
```dataview
TABLE
  title as "Document",
  file.folder as "Category",
  status as "Status"
FROM #atm/titans/battra AND -"Templates"
SORT file.folder ASC, title ASC
```

## Magical Abilities & Concepts Mentioning Battra

```dataview
LIST
FROM #atm/magic AND -"Templates"
WHERE contains(file.content, "Battra") 
SORT title ASC
```

*Note: `file.content` search can be slow on large vaults.*

## Relationships Involving Battra

```dataview
LIST
FROM #atm/relationships AND -"Templates"
WHERE contains(file.name, "Battra") OR contains(file.content, "Battra")
SORT title ASC
```

## Narrative Appearances

```dataview
TABLE
  title as "Scene",
  timeline_position as "Timeline"
FROM #atm/narratives AND -"Templates"
WHERE contains(characters, "[[Battra]]") /* Assumes linked name in YAML */
SORT timeline_position ASC
```

```

## Workflow Recommendations

*(Workflow recommendations remain the same)*

### Initial Project Setup

1.  **Create Folder Structure**: Set up the hierarchical folder organization.
2.  **Install Essential Plugins**:
    *   Dataview (for queries)
    *   Templater (for templates)
    *   Calendar (for timeline visualization)
    *   Kanban (for development tracking)
    *   Excalidraw (for relationship mapping)
3.  **Set Up Templates**: Create your primary templates using the updated format above.
4.  **Establish Key MOCs**: Create initial Maps of Content (like the dashboards).

### Content Development Process

*(Process remains the same)*

### Ongoing Maintenance

*(Maintenance remains the same)*

## Development Approach for Narrative Writers

*(Approach remains the same)*

## Troubleshooting and Maintenance

*(Troubleshooting remains the same)*

### Common Issues

#### Handling Contradictions
- Create a dedicated "Canon Conflicts" note to track discrepancies.
- Resolve contradictions by explicitly choosing a canonical version.
- Update all related documents to reflect the resolution.

#### Managing Complexity
- Create visual relationship maps for complex interconnections (Excalidraw).
- Use progressive disclosure in dashboards (collapsible sections).
- Develop summary documents (MOCs) for major concepts.

#### Balancing Detail and Progress
- Create "stub" documents for planned content.
- Use status tags/metadata (`#stub`, `status: draft`).
- Prioritize depth for central elements, breadth for peripheral ones.

### System Evolution

*(Evolution guidance remains the same)*

## Conclusion

This organizational system provides a framework for documenting, exploring, and developing your Antitheriomorphosis AU based on the rich foundation you've established. By combining hierarchical file organization, consistent tagging (including the base `#atm` tag), powerful templates, and Dataview integration, you'll create a dynamic knowledge base that grows with your creative vision.

The structure respects the core elements of your universe—transformed Titans, complex magic systems, and evolving relationships—while accommodating narrative development and creative exploration. As your universe evolves, this organization will help maintain consistency while allowing for creative expansion.