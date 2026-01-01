# **New Linking Protocol: Concise & Intentional Referencing**

From this point forward, all links within character profiles and related documents will adhere to the following rules:

1.  **One Link Per Concept Per File:** Each unique concept or term will only be linked *once* within any given `.md` file, at its very first instance or definition. Subsequent mentions of the same concept within that file will *not* be linked.
2.  **Placement at First Instance/Definition:** The link should be placed directly on the first occurrence where the concept is introduced or clearly defined.
3.  **Clarity and Intentionality:** Every link must serve a clear purpose: to define a new term, elaborate on a core concept, or provide crucial context from an external file.

#### **Obsidian.md Linking Syntax Guide:**

Here are the specific syntaxes we will use for different linking scenarios:

1.  **Linking to a Heading within the *Same* File:**
    *   **Purpose:** To cross-reference a concept or detail that is explained or elaborated upon elsewhere in the *current* document.
    *   **Syntax:** `[[#Heading Name]]` or `[[#Heading Name|Link Alias]]`
    *   **Example:** If you're in Section I and want to refer to "Nomothete" defined in Section III, and "Nomothete" is a `#### Heading` under "III.C," you'd use:
        *   `[[#1. Nomothete (Ultimate Mastery Level)|Nomothete]]`
    *   **Note:** As you requested, no need to include parent sections in the link itself (e.g., `III C Nomothete` is not required). Just the heading name is sufficient.

2.  **Linking to a Heading in an *External* File:**
    *   **Purpose:** To cross-reference a concept or detail that is explained or elaborated upon in a *different* document. This is common for linking to power system definitions, historical events, or related character profiles.
    *   **Syntax:** `[[Filename#Heading Name]]` or `[[Filename#Heading Name|Link Alias]]`
    *   **Example:** To link to the "Antitheriomorphosis" concept defined in the `Antitheriomorphosis.md` file, under its main heading:
        *   `[[Antitheriomorphosis.md#Antitheriomorphosis]]` or `[[Antitheriomorphosis.md#Antitheriomorphosis|Antitheriomorphosis]]`
    *   **Example 2:** To link to "Mother Prime" defined in the `Barb, the Turncoat Parasite.md` file under the heading "Origin & Transformation":
        *   `[[Barb, the Turncoat Parasite.md#Origin & Transformation|Mother Prime]]`

3.  **Linking to a Specific *Block* (Paragraph or List Item) within *Any* File:**
    *   **Purpose:** To link to a very specific piece of content (a sentence, a paragraph, a list item) that doesn't have its own heading. This is useful for citing specific facts or quotes that are embedded deeply within a larger section.
    *   **How to Use:**
        *   **Step 1: Create a Block ID:** Go to the target paragraph or list item in the source file. At the end of the paragraph (or the list item), add ` ^your-unique-id ` (a space, a caret, then a unique ID).
            *   *Example (in the source file):* `His final words, witnessed by Barb, expressed profound love and regret. ^dagon-final-words`
        *   **Step 2: Link to the Block ID:**
            *   **Syntax (same file):** `[[#^your-unique-id]]` or `[[#^your-unique-id|Link Alias]]`
            *   **Syntax (external file):** `[[Filename#^your-unique-id]]` or `[[Filename#^your-unique-id|Link Alias]]`
    *   **Example (linking from another file):** To link to Dagon's final words about his son from the example above:
        *   `[[godzilla_dagon_relationship.md#^dagon-final-words|Dagon's final words]]`
