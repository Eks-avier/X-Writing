# PowerShell Script to Create the Antitheriomorphosis Universe Directory Structure
# This script will create a nested folder structure for organizing your project files.

# Define the base path for the main project folder
$basePath = ".\Antitheriomorphosis Universe"

# Create the main project folder if it doesn't exist
New-Item -Path $basePath -ItemType Directory -Force | Out-Null

# Define the top-level directories
$topLevelDirs = @(
    "0_META",
    "1_CHARACTERS",
    "2_LORE_&_CONCEPTS",
    "3_NARRATIVE_ARCS",
    "4_GROUPS_&_ORGANIZATIONS",
    "5_LOCATIONS",
    "6_SPECIES"
)

# Create the top-level directories
foreach ($dir in $topLevelDirs) {
    New-Item -Path (Join-Path $basePath $dir) -ItemType Directory -Force | Out-Null
}

# --- Create Subdirectories ---

# META
New-Item -Path (Join-Path $basePath "0_META\design-philosophies") -ItemType Directory -Force | Out-Null
New-Item -Path (Join-Path $basePath "0_META\scratchpad") -ItemType Directory -Force | Out-Null

# CHARACTERS
New-Item -Path (Join-Path $basePath "1_CHARACTERS\Humans") -ItemType Directory -Force | Out-Null
New-Item -Path (Join-Path $basePath "1_CHARACTERS\Titans") -ItemType Directory -Force | Out-Null
New-Item -Path (Join-Path $basePath "1_CHARACTERS\_templates") -ItemType Directory -Force | Out-Null

# LORE & CONCEPTS
New-Item -Path (Join-Path $basePath "2_LORE_&_CONCEPTS\Power_Systems") -ItemType Directory -Force | Out-Null
New-Item -Path (Join-Path $basePath "2_LORE_&_CONCEPTS\Power_Systems\Kratos") -ItemType Directory -Force | Out-Null
New-Item -Path (Join-Path $basePath "2_LORE_&_CONCEPTS\Power_Systems\Magic") -ItemType Directory -Force | Out-Null
New-Item -Path (Join-Path $basePath "2_LORE_&_CONCEPTS\Power_Systems\Psionics") -ItemType Directory -Force | Out-Null
New-Item -Path (Join-Path $basePath "2_LORE_&_CONCEPTS\Titan_Hierarchy") -ItemType Directory -Force | Out-Null
New-Item -Path (Join-Path $basePath "2_LORE_&_CONCEPTS\World_History") -ItemType Directory -Force | Out-Null

# NARRATIVE ARCS
New-Item -Path (Join-Path $basePath "3_NARRATIVE_ARCS\Main_Story") -ItemType Directory -Force | Out-Null
New-Item -Path (Join-Path $basePath "3_NARRATIVE_ARCS\Main_Story\01_The_Awakening_Arc") -ItemType Directory -Force | Out-Null
New-Item -Path (Join-Path $basePath "3_NARRATIVE_ARCS\Main_Story\02_Keystone_Arc") -ItemType Directory -Force | Out-Null
New-Item -Path (Join-Path $basePath "3_NARRATIVE_ARCS\Main_Story\03_Xilien_Invasion_Arc") -ItemType Directory -Force | Out-Null
New-Item -Path (Join-Path $basePath "3_NARRATIVE_ARCS\Side_Stories_&_Vignettes") -ItemType Directory -Force | Out-Null

# GROUPS & ORGANIZATIONS
New-Item -Path (Join-Path $basePath "4_GROUPS_&_ORGANIZATIONS\Monarch") -ItemType Directory -Force | Out-Null

# SPECIES
New-Item -Path (Join-Path $basePath "6_SPECIES\Titanus_gojira") -ItemType Directory -Force | Out-Null
New-Item -Path (Join-Path $basePath "6_SPECIES\Titanus_mosura") -ItemType Directory -Force | Out-Null

Write-Host "Directory structure for 'Antitheriomorphosis Universe' created successfully."
