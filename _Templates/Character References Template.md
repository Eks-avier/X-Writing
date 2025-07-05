<%*
// Basic file information
let fileName = tp.file.title;
let creationDate = tp.file.creation_date("YYYY-MM-DD");
let modificationDate = tp.file.last_modified_date("YYYY-MM-DD");

// Status can be "draft", "complete", or "revision"
let status = "draft";

// Optional prompt for alias - for characters with multiple names
let alias = await tp.system.prompt("Enter character aliases (comma separated)", "");
let aliases = alias ? alias.split(",").map(item => item.trim()) : [];

// Optional prompt for character type
let charType = await tp.system.prompt("Enter character type (protagonist, antagonist, supporting, etc.)", "");

// Generate YAML frontmatter
-%>
---
aliases: <% aliases.length > 0 ? aliases.map(a => `\n  - ${a}`).join('') : '[]' %>
tags:
  - character
  - reference
  - character/<% charType.toLowerCase() %>
status: <% status %>
created: <% creationDate %>
modified: <% modificationDate %>
File: <% tp.file.folder() %>/<% tp.file.title %>.md

---

# **<% fileName %>**

> *“[Signature quote or statement that captures character essence]”*

## Overview

[Two to three paragraphs introducing the character's fundamental nature, role in the narrative, and most distinctive qualities. This should provide enough context for someone unfamiliar with your world to understand who this character is and why they matter.]

## Basic Profile

### Identification

> [!info] Basic Information
> - **Full Name**: [Character's complete name]
> - **Age**: [Actual and/or apparent age]
> - **Race/Species**: [Character's race or species]
> - **Affiliation**: [Primary group, faction, or organizational ties]
> - **Status**: [Active, deceased, missing, etc.]
> - **Title(s)**: [Official or informal titles]

## Physical Appearance

### Basic Traits

[One paragraph describing overall physical presence and immediate visual impression]

| Attribute       | Description                                                           |
| --------------- | --------------------------------------------------------------------- |
| **Height**      | [Height in appropriate units]                                         |
| **Build**       | [Body type and general physical condition]                            |
| **Hair**        | [Color, style, distinctive features]                                  |
| **Eyes**        | [Color, shape, notable qualities]                                     |
| **Skin**        | [Complexion, notable markings or features]                            |
| **Features**    | [Distinctive facial or bodily characteristics]                        |
| **Movement**    | [How they carry themselves, distinctive movement patterns]            |

### Distinctive Characteristics

- [Unusual physical trait or feature]
- [Characteristic mannerisms or gestures]
- [Distinctive voice qualities or speech patterns]
- [Unique physical capabilities or limitations]

## Abilities & Powers

> [!quote] [Ability Theme]
> “[Quote about their abilities or powers from another character or themselves]”

### Core Abilities

- [Primary ability/power and its significance]
- [Secondary ability/power and its significance]
- [Notable skills or trained capabilities]
- [Unique knowledge or expertise]

### Limitations

- [Physical or mental limitations]
- [Power restrictions or weaknesses]
- [Situational vulnerabilities]
- [Self-imposed restrictions]

## Personality & Psychology

### Core Traits

- **[Primary Trait]**: [Description with brief example]
- **[Secondary Trait]**: [Description with brief example]
- **[Contradictory Trait]**: [Description with brief example]
- **[Hidden Trait]**: [Description with brief example]

### Motivations

- **Primary Motivation**: [What drives them above all else]
- **Secondary Motivation**: [Important but lesser driving force]
- **Desires**: [What they actively want or seek]
- **Fears**: [What terrifies or concerns them most]

### Values & Beliefs

- **Core Value**: [What they hold most sacred]
- **Philosophical Outlook**: [General worldview or philosophy]
- **Moral Framework**: [How they determine right from wrong]
- **Religious/Spiritual Views**: [Beliefs about higher powers or cosmic order]

## Notable Relationships

> [!info] Key Relationships
> [Brief overview of relationship dynamics and patterns]

### [Relationship 1 - Name]

- **Nature**: [Relationship type - friend, enemy, mentor, etc.]
- **History**: [Brief history of their connection]
- **Dynamic**: [Current state of relationship]
- **Significance**: [Why this relationship matters to the character]

### [Relationship 2 - Name]

- **Nature**: [Relationship type - friend, enemy, mentor, etc.]
- **History**: [Brief history of their connection]
- **Dynamic**: [Current state of relationship]
- **Significance**: [Why this relationship matters to the character]

## Background & History

### Origin

- [Birth or creation circumstances]
- [Early formative experiences]
- [Cultural and familial context]
- [Initial trajectory or expectations]

### Key Life Events

- **[Event 1]**: [Description and impact]
- **[Event 2]**: [Description and impact]
- **[Event 3]**: [Description and impact]

## Role in Narrative

### Function

- **Archetypal Role**: [Hero, Mentor, Trickster, etc.]
- **Plot Function**: [How they drive or affect the plot]
- **Thematic Representation**: [What themes they embody or explore]

### Character Arc

- **Starting Point**: [Initial state or position]
- **Transformation**: [How they change throughout the narrative]
- **Resolution/Current State**: [Where their journey leads]

## Additional Notes

### Cultural Context

- [Relevant cultural background information]
- [How culture influences their perspective]
- [Cultural practices or traditions they observe]

### Symbolic Significance

- [What the character symbolizes in the narrative]
- [Visual or thematic motifs associated with them]
- [Mythological or literary parallels]

## Quotations

> “[Memorable quote that reveals character]”

> “[Meaningful quote that shows growth or conflict]”

> “[Quote that demonstrates relationship with another character]”

## Narrative Appearances

- [Story/Chapter/Scene where they first appear]
- [Major stories/chapters/scenes featuring them]
- [Significant off-screen developments]

## See Also

- [[Related Character 1]] - [Brief description of connection]
- [[Related Character 2]] - [Brief description of connection]
- [[Related Location]] - [Character's connection to this place]
- [[Related Event]] - [Character's involvement in this event]
- [[Related Concept]] - [Character's connection to this concept]

## Supplementary Materials

- [[SUP_Character_Name_Backstory]] - Detailed exploration of character history
- [[SUP_Character_Name_Relationships]] - In-depth analysis of key relationships
- [[SUP_Character_Name_Development]] - Character evolution across narrative
- [[SUP_Character_Name_Abilities]] - Comprehensive breakdown of powers and skills

## Trivia

> [!tip] Interesting Facts
> - [Behind-the-scenes detail or development note]
> - [Unusual character trait or habit not mentioned elsewhere]
> - [Character inspiration or reference point]
> - [Planned developments or potential futures]