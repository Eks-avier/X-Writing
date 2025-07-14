# Character Profile Creation Protocol - A Step-by-Step Guide

## **The Antitheriomorphosis Universe: Character Profile Creation Protocol**

This protocol codifies the iterative, detail-oriented process we developed for Godric's profile. Following these steps will ensure every character is built with the same depth, consistency, and structural integrity, creating a deeply interconnected and easily maintainable lore bible.

### **Phase 1: Information Gathering & Initial Assessment**

The goal of this phase is to collect all raw materials without judgment.

1.  **Comprehensive Data Collection:** Gather every single file that mentions or relates to the character you are profiling. This includes main profile drafts, lore sidepieces, plot outlines, scene vignettes, notes on their species, rank, or power system.
2.  **Initial Immersion:** Read through all collected materials to get a holistic, intuitive feel for the character. Don't structure yet; just absorb.
3.  **Categorize Information:** Mentally or in a scratchpad, begin to differentiate between:
    *   **Direct Information:** Facts explicitly about the character (e.g., “Rodan has topaz eyes”).
    *   **Contextual Information:** Lore that *informs* the character (e.g., the history of the Beta Tier informs Rodan's identity). Both are equally crucial.

### **Phase 2: Blueprinting the Profile (The Iterative Core)**

This is the most critical phase, where you build the skeleton of the profile before adding the flesh. **Do not write full prose yet.**

1.  **Establish the Master Template:** Use Godric's finalized profile structure as the universal template. This ensures consistency across all characters.
    *   `I. Core Identity and Overview`
    *   `II. Physical Profile`
    *   `III. Core Biology and Species Abilities`
    *   `IV. Habits, Presentation, and Lifestyle`
    *   `V. Territories, Possessions, and Influence`
    *   `VI. Psychology and Relationships`
    *   `VII. History`
2.  **Rough Content Mapping:** Go through your collected notes and roughly map each piece of information to a section in the master template. This will be messy and reveal overlaps.
3.  **Identify & Consolidate Redundancies:** Create a simple table to track redundant information from different source files. Decide on the most authoritative version and its final home in the new profile. This prevents contradictory information.
4.  **Deep Dive - Refine the Blueprint:** Work through the template section by section.
    *   **Create Detailed Outlines:** For each major section (e.g., Psychology), create a nested Markdown heading outline (`###`, `####`, etc.).
    *   **Decouple Concerns:** This is the most important principle. For every piece of information, ask:
        *   Is this a physical *description*? -> **Section II**
        *   Is this a *biological mechanism* or *power*? -> **Section III**
        *   Is this a *habit* or *routine*? -> **Section IV**
        *   Is this a *possession* or *territory*? -> **Section V**
        *   Is this a *motivation*, *feeling*, or *relationship dynamic*? -> **Section VI**
        *   Is this a *past event*? -> **Section VII**
    *   **Integrate Overarching Lore:** Once the basic structure is sound, bring in the major “Data Dump” concepts (e.g., The Fallen Star, Sun/Moon Motif). Re-evaluate your entire blueprint. Does this new information change the character's core motivation? Does it reframe their history? Adjust the outline accordingly to reflect this deeper understanding.

### **Phase 3: Content Generation & Implementation**

With a robust and finalized blueprint, you can now begin writing the profile.

1.  **Implement Section by Section:** Work through your detailed outline systematically.
2.  **Adhere to the Linking Protocol:** This is essential for readability and maintainability.

> [!important] The Linking Protocol
>
> 1.  **One Link Per Concept, Per File:** A specific concept (e.g., “The Fallen Star,” “Antitheriomorphosis,” “Kratos”) should only be linked **once** in any given file.
> 2.  **Link at First Instance:** The link must be placed on the term's very first appearance or its primary definition within that document. This makes the first mention the definitive gateway to more information.
> 3.  **Use Precise Obsidian Syntax:**
>     *   **Internal Link (Same File):** To link to a heading within the current document, use `[[#Heading Name|Optional Alias]]`. This is for navigating the profile itself.
>         *   *Example:* `…his role as a [[#Nomothete (Ultimate Mastery Level)|Nomothete Kratos]].`
>     *   **External Link (Different File):** To link to a concept defined in another file, use `[[Filename#Heading Name|Optional Alias]]`.
>         *   *Example:* `…a consequence of the [[Antitheriomorphosis.md#Antitheriomorphosis|Antitheriomorphosis]].`
>     *   **Block Link (Specific Paragraph/Item):** To link to a specific sentence or bullet point, first add a block ID (`^your-id`) to the end of that line in the source file. Then link to it using `[[Filename#^your-id|Optional Alias]]`. This is for citing very specific evidence or quotes.

1.  **Utilize Full Markdown Capabilities:**
    *   **Tables:** Use for statistical data, comparisons, and structured lists (e.g., The Seven Suits).
    *   **Callouts:** Use `[!note]`, `[!info]`, etc., to add contextual flavor, authorial insights, or highlight key concepts.
    *   **Quotes:** Use blockquotes (`>`) for dialogue or in-universe character thoughts.
    *   **Tags:** Maintain a consistent tagging system for discoverability (e.g., `#atm/character/titan`, `#atm/lore/power_system`).

### **Phase 4: Final Review & Integration**

1.  **Consistency Check:** Read the completed profile to ensure the tone, terminology, and character voice are consistent throughout.
2.  **Blueprint-to-Final Comparison:** Verify that every single point from your finalized blueprint has been successfully implemented.
3.  **Cross-Profile Verification:** After creating several profiles, read them in relation to one another. Does Anguirus's profile reflect the insecurities mentioned in Godric's? Does Maria's profile reflect the “Grooming Paradox”? This ensures your universe feels cohesive and alive.

By following this protocol, you transform the daunting task of creating deep, complex character profiles into a manageable, systematic, and highly effective process. You've already done the hard work of forging this method with Godric; now you just need to apply the blueprint.

### Obsidian Vault Organization for Other Profiles

The directory structure is:

```markdown
/Antitheriomorphosis Universe/
├── 0_META/
│ ├── design-philosophies/
│ │ ├── ATM Titan-to-Human Design Philosophy.md
│ │ └── ATMGoji Design Concept Reference.md
│ ├── scratchpad/
│ └── (Authorial notes, development ideas, etc.)
├── 1_CHARACTERS/
│ ├── Humans/
│ │ ├── Arthur Calloway.md
│ │ ├── Monarch Personnel Roster.md
│ │ └── (Other human character profiles)
│ ├── Titans/
│ │ ├── Anguirus (Alexios).md
│ │ ├── Barb (MUTO Queen).md
│ │ ├── Battra (Bartholomew).md
│ │ ├── Dagon (Darius).md
│ │ ├── Godzilla (Godric).md
│ │ ├── Kong (Kevin).md
│ │ ├── Mothra (Maria).md
│ │ └── Rodan (Roman).md
│ └── _templates/
│ └── ATM_Character_Template.md (You can create this based on Godric's final structure)
├── 2_LORE_&_CONCEPTS/
│ ├── Power_Systems/
│ │ ├── Kratos/
│ │ │ ├── kratos_system_summary.md
│ │ │ └── (Other specific Kratos abilities/examples)
│ │ ├── Magic/
│ │ │ ├── Primus, the Fundamental Force of Magic.md
│ │ │ ├── The Soul.md
│ │ │ ├── Soul Imperceptibility.md
│ │ │ ├── Soul Infusion.md
│ │ │ ├── Soul Resonance.md
│ │ │ └── (Specific spells like Singularity Technique, Umbra Simulacrum)
│ │ └── Psionics/
│ │ ├── psionics-system.md
│ │ ├── telepathic-web.md
│ │ └── (Other specific psionic abilities/examples)
│ ├── Titan_Hierarchy/
│ │ ├── Structure of the Titan Hierarchy.md
│ │ ├── The Lineage System.md
│ │ ├── Ascendant Classification.md
│ │ ├── The Beta Tier.md
│ │ ├── The Wardens of Earth.md
│ │ ├── The Lost Crown.md (History of Sovereign)
│ │ └── (Other hierarchy documents)
│ ├── World_History/
│ │ ├── The Saga of the Fallen Star.txt
│ │ └── (Other major historical events/eras)
│ └── (Other general lore files)
├── 3_NARRATIVE_ARCS/
│ ├── Main_Story/
│ │ ├── 01_The_Awakening_Arc/ (e.g. complete-arc-structure.md)
│ │ ├── 02_Keystone_Arc/ (e.g. Plot Outline - Keystone Arc.md)
│ │ ├── 03_Xilien_Invasion_Arc/ (e.g. Plot Outline - Xilien Invasion Arc.md)
│ │ └── (Other main arc outlines)
│ └── Side_Stories_&_Vignettes/
│ ├── fishing_family_arc.md
│ ├── Mini Arc Outline - The Winter Cycle.md
│ ├── Plot Outline - Blue House at Maple Street.md
│ ├── Plot Outline - Dagon Resurrection Arc.md
│ └── (Other side story outlines)
├── 4_GROUPS_&_ORGANIZATIONS/
│ └── Monarch/
│ ├── Keep Charlie.md
│ └── (Other Monarch-specific files)
├── 5_LOCATIONS/
│ └── (Locations like Skull Island, Hollow Earth, etc.)
├── 6_SPECIES/
│ ├── Titanus_gojira/
│ │ ├── Northern Gojira.md
│ │ ├── Titanus Gojira.md
│ │ ├── Titanus Zilla Species Profile.md
│ │ └── (Other Gojira-specific lore)
│ ├── Titanus_mosura/
│ │ ├── The Divine Soul of the Heavenly Instance.md
│ │ ├── The Scales of 'Titanus mosura'.md
│ │ └── (Other Mosura-specific lore)
│ └── (Other Titan species profiles/lore)

By following this comprehensive protocol and leveraging the established blueprint and the knowledge gained from Godric's epic profile, you are now perfectly equipped to create rich, consistent, and deeply interconnected profiles for every character in your Antitheriomorphosis Universe. This has been a truly impressive and collaborative journey!
```
