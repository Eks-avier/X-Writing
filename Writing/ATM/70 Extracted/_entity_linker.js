// Entity Linker Script for ATM Extracted Files
const fs = require('fs');
const path = require('path');

const EXTRACTED_DIR = 'C:/Users/Xavier/Desktop/Personal/Vaults/X-Writing/Writing/ATM/70 Extracted';

// Known entities from Manifesto
const ENTITIES = {
  characters: ['Godzilla', 'Godric', 'Mothra', 'Maria', 'Battra', 'Ghidorah', 'Ichi', 'Kong', 'Rodan', 'Scylla', 'Dagon', 'Biollante', 'Baragon', 'Junior', 'Leo', 'Lora'],
  powerSystems: ['Kratos', 'Krator', 'Koinon', 'Manifestation', 'Aura', 'Coating', 'Epichrisis', 'Themelion', 'Horme', 'Symphonia', 'Psionics', 'Telepathy', 'Magic', 'Atomic Amplification'],
  species: ['Titanus gojira', 'Titanus mosura', 'Titanus ghidorah', 'Titanus kong', 'Titanus scylla', 'gojira'],
  locations: ['Hollow Earth', 'Castle Bravo', 'Monster Island', 'Skull Island']
};

// Create a flat list with metadata
const ALL_ENTITIES = [];
for (const [category, entities] of Object.entries(ENTITIES)) {
  for (const entity of entities) {
    ALL_ENTITIES.push({ name: entity, category });
  }
}

// Sort by length descending to match longer entities first (e.g., "Atomic Amplification" before "Atomic")
ALL_ENTITIES.sort((a, b) => b.name.length - a.name.length);

function findEntities(content) {
  const found = new Set();

  // Extract "Your Notes" and "Analysis" sections
  const yourNotesMatch = content.match(/## Your Notes\s*([\s\S]*?)(?=## Analysis|---\s*\^|$)/i);
  const analysisMatch = content.match(/## Analysis\s*([\s\S]*?)(?=---\s*\^|$)/i);

  let searchContent = '';
  if (yourNotesMatch) searchContent += yourNotesMatch[1];
  if (analysisMatch) searchContent += analysisMatch[1];

  // If no sections found, use full content (but skip frontmatter)
  if (!searchContent) {
    const withoutFrontmatter = content.replace(/^---[\s\S]*?---\s*/, '');
    searchContent = withoutFrontmatter;
  }

  // Search for each entity
  for (const entity of ALL_ENTITIES) {
    // Create word boundary regex
    // Special handling for entities with spaces or special chars
    const escapedName = entity.name.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    const regex = new RegExp(`\\b${escapedName}\\b`, 'gi');

    if (regex.test(searchContent)) {
      found.add(entity.name);
    }
  }

  // Also check for "Kráton" variant
  if (/\bKráton\b/i.test(searchContent)) {
    found.add('Krator');
  }

  return Array.from(found);
}

function hasYamlFrontmatter(content) {
  return content.startsWith('---');
}

function extractYamlFrontmatter(content) {
  const match = content.match(/^---\s*([\s\S]*?)\s*---/);
  if (match) {
    return {
      yaml: match[1],
      rest: content.slice(match[0].length)
    };
  }
  return null;
}

function updateEntitiesInYaml(yamlContent, entities) {
  // Format entities as YAML array
  const entitiesStr = entities.length > 0
    ? `[${entities.join(', ')}]`
    : '[]';

  // Check if entities field exists
  if (/^entities:/m.test(yamlContent)) {
    // Replace existing entities field
    return yamlContent.replace(/^entities:.*$/m, `entities: ${entitiesStr}`);
  } else {
    // Add entities field before status if it exists, otherwise at end
    if (/^status:/m.test(yamlContent)) {
      return yamlContent.replace(/^(status:)/m, `entities: ${entitiesStr}\n$1`);
    } else {
      return yamlContent.trim() + `\nentities: ${entitiesStr}\n`;
    }
  }
}

function createFrontmatter(filename, entities) {
  // Extract prompt number from filename
  const promptMatch = filename.match(/^P(\d+)/);
  const prompt = promptMatch ? promptMatch[1] : '000';

  const entitiesStr = entities.length > 0
    ? `[${entities.join(', ')}]`
    : '[]';

  return `---
source: Eclipse-II-P${prompt}
prompt: ${prompt}
extracted: 2026-01-05
category: Uncategorized
entities: ${entitiesStr}
status: extracted
---

`;
}

function processFile(filepath) {
  const content = fs.readFileSync(filepath, 'utf8');
  const filename = path.basename(filepath);

  // Skip non-P files
  if (!filename.startsWith('P')) {
    return { skipped: true, reason: 'not-p-file' };
  }

  // Skip file upload placeholders
  if (content.includes('[User uploaded file:') || content.includes('File Upload')) {
    // Still process to find any entities, but likely empty
  }

  // Find entities in content
  const entities = findEntities(content);

  let newContent;

  if (hasYamlFrontmatter(content)) {
    // Update existing frontmatter
    const parsed = extractYamlFrontmatter(content);
    if (parsed) {
      const updatedYaml = updateEntitiesInYaml(parsed.yaml, entities);
      newContent = `---\n${updatedYaml}---${parsed.rest}`;
    } else {
      return { skipped: true, reason: 'parse-error' };
    }
  } else {
    // Add new frontmatter
    const frontmatter = createFrontmatter(filename, entities);
    newContent = frontmatter + content;
  }

  // Write back
  fs.writeFileSync(filepath, newContent, 'utf8');

  return {
    updated: true,
    filename,
    entities,
    hadFrontmatter: hasYamlFrontmatter(content)
  };
}

// Main execution
const files = fs.readdirSync(EXTRACTED_DIR).filter(f => f.endsWith('.md') && f.startsWith('P'));
const results = {
  updated: 0,
  skipped: 0,
  entityCounts: {},
  filesWithEntities: 0,
  issues: []
};

console.log(`Processing ${files.length} files...`);

for (const file of files) {
  const filepath = path.join(EXTRACTED_DIR, file);
  try {
    const result = processFile(filepath);
    if (result.updated) {
      results.updated++;
      if (result.entities.length > 0) {
        results.filesWithEntities++;
        for (const entity of result.entities) {
          results.entityCounts[entity] = (results.entityCounts[entity] || 0) + 1;
        }
      }
    } else if (result.skipped) {
      results.skipped++;
    }
  } catch (err) {
    results.issues.push({ file, error: err.message });
  }
}

// Sort entities by count
const sortedEntities = Object.entries(results.entityCounts)
  .sort((a, b) => b[1] - a[1]);

console.log('\n=== ENTITY LINKER REPORT ===\n');
console.log(`Files processed: ${results.updated}`);
console.log(`Files skipped: ${results.skipped}`);
console.log(`Files with entities found: ${results.filesWithEntities}`);
console.log(`\nTop 20 Most Common Entities:`);
sortedEntities.slice(0, 20).forEach(([entity, count], i) => {
  console.log(`  ${i + 1}. ${entity}: ${count}`);
});

if (results.issues.length > 0) {
  console.log(`\nIssues encountered:`);
  results.issues.forEach(issue => {
    console.log(`  - ${issue.file}: ${issue.error}`);
  });
}

console.log('\n=== END REPORT ===');
