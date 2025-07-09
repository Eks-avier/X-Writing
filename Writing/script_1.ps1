<#
.SYNOPSIS
    Creates the complete folder structure for the Antitheriomorphosis Universe Obsidian vault.

.DESCRIPTION
    This script scaffolds the entire directory tree as designed, allowing for a clean,
    organized start to the world-building project. It prompts the user for a base
    location, then creates all necessary parent and sub-folders.

.NOTES
    Author: Gemini (based on our collaborative design)
    Version: 1.0
    PowerShell Version Requirement: 7.0 or higher
#>

# --- SCRIPT CONFIGURATION ---
# Define the name of the main project folder.
$mainFolderName = "Antitheriomorphosis Universe"

# --- USER INTERACTION ---
# Clear the screen for a better user experience.
Clear-Host

# Get the current location where the script is being run.
$currentPath = Get-Location

Write-Host "Antitheriomorphosis Universe Vault Scaffolding Script" -ForegroundColor Yellow
Write-Host "----------------------------------------------------" -ForegroundColor Yellow
Write-Host
Write-Host "This script will create the main project folder in the following location:"
Write-Host "$currentPath" -ForegroundColor Cyan
Write-Host
# Prompt the user to either accept the current path or provide a new one.
$inputPath = Read-Host "Press ENTER to accept this location, or provide a new full path (e.g., D:\Projects)"

# Set the base path based on user input. If no input, use the current path.
if ([string]::IsNullOrWhiteSpace($inputPath)) {
  $basePath = $currentPath
  Write-Host "Using current directory as the base." -ForegroundColor Green
}
else {
  $basePath = $inputPath
  Write-Host "Using custom path: $basePath" -ForegroundColor Green
}

# Construct the full path for the main project folder.
$projectRoot = Join-Path -Path $basePath -ChildPath $mainFolderName
Write-Host "Full project root will be: $projectRoot" -ForegroundColor Cyan
Write-Host

# --- FOLDER STRUCTURE DEFINITION ---
# Define the entire folder structure as an array of strings.
# These paths are relative to the main project folder.
$folderStructure = @(
  "00 - ATLAS (Core Lore)/Power Systems/_components",
  "00 - ATLAS (Core Lore)/World History & Timeline",
  "00 - ATLAS (Core Lore)/Society & Culture/_components",
  "00 - ATLAS (Core Lore)/Species Profiles",
  "00 - ATLAS (Core Lore)/Locations & Organizations",

  "10 - CHARACTERS/Godzilla (Godric Nordson)/_source_notes",
  "10 - CHARACTERS/Mothra (Maria Lepidiel)",
  "10 - CHARACTERS/Dagon (Darius Nordson)",
  "10 - CHARACTERS/Kong (Kevin King)",
  "10 - CHARACTERS/Rodan (Roman Volcario)",
  "10 - CHARACTERS/Anguirus (Alexios Peltast)",
  "10 - CHARACTERS/Battra (Bartholomew Lepidiel)",
  "10 - CHARACTERS/Barb (The Turncoat Parasite)",

  "20 - NARRATIVE (Story Arcs)/The First Arc (Awakening)",
  "20 - NARRATIVE (Story Arcs)/Xilien Invasion Arc",
  "20 - NARRATIVE (Story Arcs)/Keystone Arc",
  "20 - NARRATIVE (Story Arcs)/Blue House at Maple Street Arc",
  "20 - NARRATIVE (Story Arcs)/Dagon Resurrection Arc"
)

# --- FOLDER CREATION LOGIC ---
Write-Host
Write-Host "Beginning folder creation..." -ForegroundColor Yellow
Write-Host "----------------------------" -ForegroundColor Yellow

# Create the main project root folder first.
try {
  # Check if the directory already exists to provide a more informative message.
  if (-not (Test-Path -Path $projectRoot)) {
    New-Item -Path $projectRoot -ItemType Directory -Force | Out-Null
    Write-Host "[CREATED] Root Folder: $projectRoot" -ForegroundColor Green
  }
  else {
    Write-Host "[EXISTS] Root Folder: $projectRoot" -ForegroundColor Gray
  }

  # Loop through each defined folder path in our structure array.
  foreach ($folder in $folderStructure) {
    # Combine the project root with the relative folder path.
    $targetPath = Join-Path -Path $projectRoot -ChildPath $folder

    # The -Force switch on New-Item will create any necessary parent directories.
    # This is more efficient than checking for each parent folder individually.
    New-Item -Path $targetPath -ItemType Directory -Force | Out-Null
    Write-Host "  [CREATED] Sub-Folder: $folder" -ForegroundColor White
  }

  Write-Host
  Write-Host "✅ Folder structure created successfully!" -ForegroundColor Green
  Write-Host "You can now open '$projectRoot' as a vault in Obsidian." -ForegroundColor Cyan
}
catch {
  # If any error occurs (e.g., permissions issue), display it.
  Write-Host
  Write-Host "❌ An error occurred:" -ForegroundColor Red
  Write-Host $_.Exception.Message -ForegroundColor Red
}
