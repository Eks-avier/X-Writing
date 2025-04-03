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

---

<?xml version="1.0" encoding="UTF-8"?>
<TitanSpeciesDocumentationSystem>
    <Version>1.0</Version>
    <Project>Antitheriomorphosis Universe Titan Species Documentation</Project>

    <Section id="1" title="Core Philosophy">
        <Description>This system uses an atomic knowledge base approach for documenting Titan species in the Antitheriomorphosis universe.</Description>
        <Principles>
            <Principle name="Atomic Modularity">Each aspect exists as a separate document.</Principle>
            <Principle name="Hierarchical Organization">Documents organized in logical "shells".</Principle>
            <Principle name="Standardized Metadata">Consistent YAML frontmatter across documents.</Principle>
            <Principle name="Rich Interlinking">Robust connections between related documents.</Principle>
            <Principle name="Dataview Integration">Queries to gather and display cross-document information.</Principle>
            <Principle name="Cross-Species Referencing">Standardized connections between related species.</Principle>
        </Principles>
    </Section>

    <Section id="2" title="Document Size Guidelines">
        <GuidelinesTable>
            <Headers>
                <Header>Document Type</Header>
                <Header>Target Word Count</Header>
                <Header>Max Word Count</Header>
            </Headers>
            <Row>
                <Cell>Hub Document</Cell>
                <Cell>500-750 words</Cell>
                <Cell>1,000 words</Cell>
            </Row>
            <Row>
                <Cell>Biology Documents</Cell>
                <Cell>300-500 words</Cell>
                <Cell>750 words</Cell>
            </Row>
            <Row>
                <Cell>Society Documents</Cell>
                <Cell>300-500 words</Cell>
                <Cell>750 words</Cell>
            </Row>
            <Row>
                <Cell>History Documents</Cell>
                <Cell>300-500 words</Cell>
                <Cell>750 words</Cell>
            </Row>
        </GuidelinesTable>
    </Section>

    <Section id="3" title="Atomic Architecture">
        <Description>The knowledge base follows a nucleus-electron shell model:</Description>
        <ShellModel>
            <Level name="Nucleus Document">Central hub for navigation and species overview.</Level>
            <Level name="Inner Shell">Core biological aspects (evolution, physiology, abilities).</Level>
            <Level name="Middle Shell">Societal and behavioral aspects.</Level>
            <Level name="Outer Shell">Historical and contextual aspects.</Level>
        </ShellModel>
    </Section>

    <Section id="4" title="File Structure">
        <StructureDescription>Example file structure:</StructureDescription>
        <CodeBlock type="filesystem">
            <![CDATA[
Species/
├── _Species-Index.md             # Master index of all species
├── Ascendant-Lines/              # Highest tier species
│   ├── Titanus-Gojira/           # Example species folder
│   │   ├── _Titanus-Gojira.md    # Hub document
│   │   ├── Biology/              # Inner shell
│   │   ├── Society/              # Middle shell
│ │   └── History/ # Outer shell
│ └── [Other Ascendant Species]/
├── Emergent-Lines/ # Rising tier species
└── Supporting-Species/ # Lesser Titan species
            ]]>
        </CodeBlock>
    </Section>

    <Section id="5" title="Metadata Standards">
        <Metadata type="Hub Document">
            <Description>Metadata for the main species hub document.</Description>
            <CodeBlock type="yaml">
                <![CDATA[
---
title: “[Species Full Name]”
aliases:
  - “[Common Name]”
  - “[Variant Names]”
species_classification: “[Ascendant/Emergent/Supporting]”
lineage_type: “[Species Family]”
status: “[Extinct/Endangered/Stable/Unknown]”
living_representatives:
  - “[[Representative Individual 1]]”
  - “[[Representative Individual 2]]”
core_abilities:
  - “[[Core Ability 1]]”
  - “[[Core Ability 2]]”
related_species:
  - “[[Related Species 1]]”
  - “[[Related Species 2]]”
tags:
  - atm
  - atm/species/[species_tag]
  - atm/lineage/[lineage_tag]
  - atm/status/[status_tag]
created: YYYY-MM-DD
last_modified: YYYY-MM-DD
---
                ]]>
            </CodeBlock>
        </Metadata>
        <Metadata type="Biology Document">
            <Description>Metadata for individual biological aspect documents.</Description>
            <CodeBlock type="yaml">
                <![CDATA[
---
title: “[Species Name]: [Biological Aspect]”
parent: “[[_Species-Name]]”
component_type: “biology”
component_category: “[evolutionary/physiological/ability]”
related_components:
  - “[[Related Component 1]]”
  - “[[Related Component 2]]”
manifestations:
  - “[Example 1]”
  - “[Example 2]”
current_status: “[Active/Dormant/Evolved/Lost]”
tags:
  - atm
  - atm/species/[species_tag]
  - atm/biology/[aspect_tag]
created: YYYY-MM-DD
last_modified: YYYY-MM-DD
---
                ]]>
            </CodeBlock>
        </Metadata>
        <Metadata type="Society Document">
            <Description>Metadata for individual societal aspect documents.</Description>
            <CodeBlock type="yaml">
                <![CDATA[
---
title: “[Species Name]: [Social Aspect]”
parent: “[[_Species-Name]]”
component_type: “society”
component_category: “[social_structure/communication/behavior/faction]”
faction_name: “[For faction documents]”
territory: “[For faction documents]”
distinctive_traits:
  - “[Trait 1]”
  - “[Trait 2]”
related_components:
  - “[[Related Component 1]]”
  - “[[Related Component 2]]”
tags:
  - atm
  - atm/species/[species_tag]
  - atm/society/[aspect_tag]
created: YYYY-MM-DD
last_modified: YYYY-MM-DD
---
                ]]>
            </CodeBlock>
        </Metadata>
        <Metadata type="History Document">
            <Description>Metadata for individual historical aspect documents.</Description>
            <CodeBlock type="yaml">
                <![CDATA[
---
title: “[Species Name]: [Historical Aspect]”
parent: “[[_Species-Name]]”
component_type: “history”
component_category: “[timeline/extinction/relationship]”
time_period: “[Relevant time period]”
related_events:
  - “[[Event 1]]”
  - “[[Event 2]]”
related_species:
  - “[[Species 1]]”
  - “[[Species 2]]”
tags:
  - atm
  - atm/species/[species_tag]
  - atm/history/[aspect_tag]
created: YYYY-MM-DD
last_modified: YYYY-MM-DD
---
                ]]>
            </CodeBlock>
        </Metadata>
    </Section>

    <Section id="6" title="Document Templates">
        <Template type="Streamlined Hub Document">
            <CodeBlock type="markdown">
                <![CDATA[

# [Species Name]

## Introduction

[Single powerful paragraph capturing essence of species with atmospheric elements]

> [!quote] Monarch Classification
> “[Brief, focused observation about the species]”

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
                ]]>
            </CodeBlock>
        </Template>
        <Template type="Biology Document">
             <CodeBlock type="markdown">
                 <![CDATA[

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
                 ]]>
             </CodeBlock>
        </Template>
        <Template type="Society Document">
             <CodeBlock type="markdown">
                 <![CDATA[

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
> “[Brief, impactful observation]”

## Related Aspects

- [[Related Document 1]] - [Brief connection explanation]
- [[Related Document 2]] - [Brief connection explanation]

[Return to Hub Document]([[_Species-Name]])
                 ]]>
             </CodeBlock>
        </Template>
        <Template type="History Document">
             <CodeBlock type="markdown">
                 <![CDATA[

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
> “[Brief, relevant quote from source]”

## Related Aspects

- [[Related Document 1]] - [Brief connection explanation]
- [[Related Document 2]] - [Brief connection explanation]

[Return to Hub Document]([[_Species-Name]])
                 ]]>
             </CodeBlock>
        </Template>
    </Section>

    <Section id="7" title="Writing Style Guidelines">
        <ConcisionStrategies>
            <Title>Concision Strategies</Title>
            <Strategy number="1" name="Strategic Atmospheric Writing">
                <Item>One powerful, evocative paragraph rather than several.</Item>
                <Item>Place rich description in introduction, then shift to efficient delivery.</Item>
                <Item>Choose targeted sensory details rather than comprehensive description.</Item>
            </Strategy>
            <Strategy number="2" name="Information Density Techniques">
                <Item>Convert narrative paragraphs to structured bullet points.</Item>
                <Item>Use tables for comparative information.</Item>
                <Item>Implement callout boxes for special information.</Item>
            </Strategy>
            <Strategy number="3" name="Stylistic Elements for Maximum Impact">
                <Item name="Sensory Language">Incorporate key sensory details.</Item>
                <Item name="Contrasting Scales">Juxtapose cosmic scale with precise details.</Item>
                <Item name="Environmental Impact">Describe effect on surroundings.</Item>
                <Item name="Implied History">Let descriptions hint at deeper history.</Item>
            </Strategy>
        </ConcisionStrategies>
        <Example name="Concise But Atmospheric">
            <Title>Example: Concise But Atmospheric</Title>
            <PreferredStyle>
                <![CDATA[
Titanus gojira's cellular structure evolved as nature's ultimate energy engine—dorsal plates capturing radiation like living solar arrays that illuminated in sequence before releasing their devastating atomic projection. This concentrated stream of superheated plasma varied between regional populations, with Northern variants producing focused, penetrating beams and Southern variants generating wider, heat-intensive projections.
                ]]>
            </PreferredStyle>
        </Example>
    </Section>

    <Section id="8" title="Implementation Process">
        <Phase number="1" title="Preparation">
            <Step number="1" title="Research and Structure">
                <SubStep>Gather available information about the species.</SubStep>
                <SubStep>Set up hub document with complete metadata.</SubStep>
                <SubStep>Create folder structure for all shells.</SubStep>
                <SubStep>Prepare empty documents with appropriate metadata.</SubStep>
            </Step>
        </Phase>
        <Phase number="2" title="Content Development">
            <Step number="1" title="Write Summaries First">
                <SubStep>Focus on the embedded summaries that will appear in hub document.</SubStep>
                <SubStep>Ensure these are self-contained while encouraging deeper reading.</SubStep>
            </Step>
            <Step number="2" title="Develop Core Content">
                <SubStep>Expand each document with essential information.</SubStep>
                <SubStep>Use tables and bullet points for efficient information delivery.</SubStep>
                <SubStep>Add targeted atmospheric elements strategically.</SubStep>
            </Step>
            <Step number="3" title="Create Connections">
                <SubStep>Document relationships with other species.</SubStep>
                <SubStep>Implement links between related documents.</SubStep>
                <SubStep>Create "Related Aspects" sections.</SubStep>
            </Step>
        </Phase>
        <Phase number="3" title="Integration">
            <Step number="1" title="Implement Queries">
                <SubStep>Create dataview queries based on species characteristics.</SubStep>
                <SubStep>Generate representative lists with relevant metadata.</SubStep>
            </Step>
            <Step number="2" title="Final Review">
                <SubStep>Verify consistent metadata implementation.</SubStep>
                <SubStep>Check all links and embeds function correctly.</SubStep>
                <SubStep>Ensure documents remain within word count guidelines.</SubStep>
                <SubStep>Add species to master index.</SubStep>
            </Step>
        </Phase>
    </Section>

    <Section id="9" title="Dataview Query Examples">
        <Example type="Hub Document">
            <Query title="Abilities Overview">
                <CodeBlock type="dataview">
                    <![CDATA[

```dataview
TABLE
  manifestations as "Manifestations",
  current_status as "Status"
FROM "Species/[Classification]/[Species-Name]/Biology"
WHERE component_category = "ability"
SORT file.name ASC

    

IGNORE_WHEN_COPYING_START
Use code with caution.Xml
IGNORE_WHEN_COPYING_END

      
]]>
            </CodeBlock>
        </Query>
        <Query title="Faction Analysis">
            <CodeBlock type="dataview">
                <![CDATA[
TABLE
  territory as "Territory",
  distinctive_traits as "Traits"
FROM "Species/[Classification]/[Species-Name]/Society"
WHERE component_category = "faction"
SORT file.name ASC

    

IGNORE_WHEN_COPYING_START
Use code with caution.Dataview
IGNORE_WHEN_COPYING_END

      
]]>
            </CodeBlock>
        </Query>
    </Example>
    <Example type="Master Index">
         <Query title="Ascendant Line Species">
             <CodeBlock type="dataview">
                 <![CDATA[

    

IGNORE_WHEN_COPYING_START
Use code with caution.
IGNORE_WHEN_COPYING_END

      
TABLE
  status as "Status",
  living_representatives as "Representatives"
FROM "Species/Ascendant-Lines"
WHERE file.name startswith "_"
SORT file.name ASC

    

IGNORE_WHEN_COPYING_START
Use code with caution.Dataview
IGNORE_WHEN_COPYING_END

      
]]>
             </CodeBlock>
         </Query>
    </Example>
</Section>

<Section id="10" title="Special Considerations">
    <SpeciesType name="Ascendant Line Species">
        <Guideline>Implement full shell structure.</Guideline>
        <Guideline>Create detailed faction documentation where applicable.</Guideline>
        <Guideline>Focus on distinctive abilities and evolutionary advantages.</Guideline>
    </SpeciesType>
    <SpeciesType name="Emergent Line Species">
        <Guideline>Adapt shell structure based on complexity.</Guideline>
        <Guideline>Focus on evolutionary trajectory and potential.</Guideline>
        <Guideline>Emphasize relationship to Ascendant species.</Guideline>
    </SpeciesType>
    <SpeciesType name="Supporting Species">
        <Guideline>Implement streamlined documentation.</Guideline>
        <Guideline>Focus on ecological niche and relationship to dominant species.</Guideline>
    </SpeciesType>
</Section>

<Section id="11" title="Implementation Checklist">
    <Checklist>
        <Item>Hub Document with complete metadata</Item>
        <Item>Biology documents covering core aspects</Item>
        <Item>Society documents detailing social structure</Item>
        <Item>History documents covering key timeline events</Item>
        <Item>Cross-references between related documents</Item>
        <Item>Dataview queries implemented and functional</Item>
        <Item>Addition to master species index</Item>
    </Checklist>
</Section>

    

IGNORE_WHEN_COPYING_START
Use code with caution.
IGNORE_WHEN_COPYING_END
</TitanSpeciesDocumentationSystem>