# Magic System - Core Concepts

<%*
// Core Concept Template for Monsterverse AU Magic System
// For use with Templater plugin in Obsidian

// Get the file title or prompt for one
let title = tp.file.title;
if (title === "Untitled" || title === "New File") {
    title = await tp.system.prompt("Enter the concept title");
    await tp.file.rename(title);
}

// Prompt for other metadata
let aliases = await tp.system.prompt("Enter aliases (comma-separated)", "");
let primaryTag = await tp.system.prompt("Enter primary tag (e.g., magic/core/primus)", "magic/core/");
let secondaryTags = await tp.system.prompt("Enter secondary tags (comma-separated)", "magic/");
let relatedDocs = await tp.system.prompt("Enter related documents (comma-separated)", "");
let categoryPath = await tp.system.prompt("Enter category path (e.g., Core Concepts/Primus)", "Core Concepts/");
let complexity = await tp.system.prompt("Enter complexity (basic, intermediate, advanced, master)", "basic");
let status = await tp.system.prompt("Enter status (draft, development, review, complete)", "draft");

// Format date
let now = tp.date.now("YYYY-MM-DD");

// Create YAML frontmatter
tR += "---\n";
tR += `title: "${title}"\n`;
tR += `aliases: [${aliases}]\n`;
tR += `tags: [${primaryTag}, ${secondaryTags}]\n`;
tR += `related: [${relatedDocs}]\n`;
tR += `category: "${categoryPath}"\n`;
tR += `created: ${now}\n`;
tR += `last_modified: ${now}\n`;
tR += `concept_type: "core"\n`;
tR += `status: "${status}"\n`;
tR += `complexity: "${complexity}"\n`;
tR += "---\n\n";

// Create the document structure
tR += `# ${title}\n\n`;

tR += "## Definition & Fundamental Nature\n\n";
tR += "<!-- A concise definition of the concept and its most fundamental characteristics. -->\n\n";

tR += "## Core Properties\n\n";
tR += "- **Property 1**: <!-- Description with emphasis on how this property manifests and its significance -->\n";
tR += "- **Property 2**: <!-- Description with emphasis on how this property manifests and its significance -->\n";
tR += "- **Property 3**: <!-- Description with emphasis on how this property manifests and its significance -->\n";
tR += "- **Property 4**: <!-- Description with emphasis on how this property manifests and its significance -->\n\n";

tR += "## Mechanism of Action\n\n";
tR += "<!-- Detailed explanation of how this concept operates within the magical framework. -->\n\n";

tR += "### Primary Functions\n\n";
tR += "1. **Function 1**: <!-- How this function operates and its significance -->\n";
tR += "2. **Function 2**: <!-- How this function operates and its significance -->\n";
tR += "3. **Function 3**: <!-- How this function operates and its significance -->\n\n";

tR += "### Limitations & Constraints\n\n";
tR += "- Limitation 1 - <!-- Explanation of how/why this limitation exists -->\n";
tR += "- Limitation 2 - <!-- Explanation of how/why this limitation exists -->\n";
tR += "- Limitation 3 - <!-- Explanation of how/why this limitation exists -->\n\n";

tR += "## Relationship to Other Core Concepts\n\n";

tR += "### Related Concept 1\n";
tR += "<!-- Explanation of the relationship between concepts -->\n\n";

tR += "### Related Concept 2\n";
tR += "<!-- Explanation of the relationship between concepts -->\n\n";

tR += "## Historical Context\n\n";
tR += "<!-- Information about the discovery, development, or evolution of understanding regarding this concept. -->\n\n";

tR += "## Practitioners & Applications\n\n";

tR += "### Notable Users\n";
tR += "- **User/Group 1**: <!-- Their unique approach or relationship to this concept -->\n";
tR += "- **User/Group 2**: <!-- Their unique approach or relationship to this concept -->\n\n";

tR += "### Practical Applications\n";
tR += "1. **Application Area 1**: <!-- How this concept is applied in this context -->\n";
tR += "2. **Application Area 2**: <!-- How this concept is applied in this context -->\n\n";

tR += "## Examples & Case Studies\n\n";

tR += "### Example 1: <!-- Title -->\n";
tR += "<!-- Detailed example showing the concept in action -->\n\n";

tR += "## Research & Development Notes\n\n";
tR += "<!-- Meta-commentary on areas for further development -->\n";
%>