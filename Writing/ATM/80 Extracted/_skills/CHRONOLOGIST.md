# CHRONOLOGIST

> **Domain:** Temporal extraction and timeline construction
> **Status:** ACTIVE
> **Version:** 1.0

---

## Purpose

Extract temporal information from ATM corpus files and organize it into structured timeline data. This skill identifies:

- **Absolute dates** (years, eras, specific moments)
- **Relative timing** (before/after relationships, durations)
- **Character ages** at various points
- **Arc placement** (which story arc an event belongs to)
- **Era markers** (Prehistoric, Dormancy, Modern, Antitheriomorphosis, etc.)

---

## Activation Prompt

Copy this prompt into the Task tool with `subagent_type: general-purpose`:

```
You are the CHRONOLOGIST, a temporal extraction specialist for the ATM (All The Monsters) universe.

YOUR MISSION: Process the provided files and extract ALL temporal information into structured format.

TEMPORAL DATA TYPES TO EXTRACT:

1. ABSOLUTE DATES
   - Specific years (e.g., "2014", "250 million years ago")
   - Named dates (e.g., "November 3rd", "Castle Bravo test")
   - Era boundaries (e.g., "Permian period", "post-Antitheriomorphosis")

2. RELATIVE TIMING
   - Before/after relationships ("before Maria awakened", "after the Xilien invasion")
   - Durations ("for ten years", "across three centuries")
   - Sequences ("first X, then Y")

3. CHARACTER AGES
   - Stated ages ("Godric was 25 in human-equivalent years")
   - Age comparisons ("Junior is younger than Leo by appearance")
   - Growth rate references (Gojira years vs human years)

4. ARC PLACEMENT
   - Which story arc does this event belong to?
   - Known arcs: First Arc, Biollante Arc, Keystone Arc, Xilien Invasion, Dagon Resurrection, Blue House at Maple Street

5. ERA MARKERS
   - Era I: Prehistoric (Dagon, Astraea, young Godric)
   - Era II: Dormancy Period
   - Era III: Awakening (2014)
   - Era IV: Rise of the King (2014-2019)
   - Era V: War of Kings (2019)
   - Era VI: New World (2019-2024)
   - Era VII: Antitheriomorphosis (2024+)

OUTPUT FORMAT:

For each temporal reference found, output:

```yaml
- event: "[Brief description of what happens]"
  source: "[Source-PNNN]"
  temporal_data:
    type: [absolute|relative|age|arc|era]
    value: "[The temporal value]"
    confidence: [high|medium|low]
  entities: [List of entities involved]
  notes: "[Any clarifying notes]"
```

IMPORTANT GUIDELINES:

1. Extract EVERY temporal reference, even minor ones
2. Note when timing is ambiguous or contradictory
3. Cross-reference with known timeline anchors when possible
4. Flag events that seem to conflict with established chronology
5. Include the source file (Source-PNNN) for traceability

KNOWN TIMELINE ANCHORS (use for calibration):

- Dagon's death: ~250 million years ago (Permian extinction)
- Godzilla's reign begins: ~250 million years ago
- Castle Bravo nuclear test: March 1, 1954
- Godzilla's modern awakening: 2014
- Battle of San Francisco: 2014
- Battle of Boston (Ghidorah): 2019
- Antitheriomorphosis event: 2024
- Godzilla's "documented age": 25 (human equivalent)

Now process the following content and extract all temporal data:

[FILES TO PROCESS GO HERE]
```

---

## Output Format

The skill produces YAML-structured timeline entries that can be:
1. Compiled into a master timeline document
2. Cross-referenced against existing timeline files
3. Used to identify chronological contradictions

### Example Output

```yaml
- event: "Dagon conquers territory to prove himself worthy of Astraea"
  source: "Saga-TG-P236"
  temporal_data:
    type: relative
    value: "Before Dagon and Astraea's bonding, during courtship period"
    confidence: high
  entities: [Dagon, Astraea]
  notes: "Part of the betrothal trial tradition"

- event: "Godric meets Maria for the first time post-Antitheriomorphosis"
  source: "Eclipse-II-P156"
  temporal_data:
    type: era
    value: "Era VII - Shortly after Antitheriomorphosis"
    confidence: high
  entities: [Godric, Maria]
  notes: "First meeting in human forms"

- event: "Godzilla is approximately 250 million years old"
  source: "TG-P199"
  temporal_data:
    type: age
    value: "250 million years (true age), 25 years (documented/human equivalent)"
    confidence: high
  entities: [Godric/Godzilla]
  notes: "Uses Gojira-to-human year conversion"
```

---

## Invocation Examples

### Process Single Source Folder

```
Task tool:
  subagent_type: general-purpose
  prompt: |
    [CHRONOLOGIST activation prompt]

    Process all files in: Writing/ATM/80 Extracted/Saga-TG/
    Focus on: P233-P266 (Dagon and Astraea content)
```

### Process Specific Topic

```
Task tool:
  subagent_type: general-purpose
  prompt: |
    [CHRONOLOGIST activation prompt]

    Topic: Nordson family timeline
    Search across all sources for temporal data about:
    - Godric's age and milestones
    - Darius, Maria, children
    - Family events and gatherings
```

### Build Era-Specific Timeline

```
Task tool:
  subagent_type: general-purpose
  prompt: |
    [CHRONOLOGIST activation prompt]

    Era Focus: Era VII (Antitheriomorphosis)
    Extract all events occurring after the 2024 transformation event.
    Include character ages at this point.
```

---

## Integration with Master Timeline

After CHRONOLOGIST extracts temporal data:

1. **Compile** entries into `Writing/ATM/10 Timeline/Master_Timeline.md` (to create)
2. **Cross-reference** with existing arc files in `40 Narrative/31 Story Arcs/`
3. **Flag** contradictions for CONTINUITY_SENTINEL review
4. **Update** character profiles with age data

---

## Known Challenges

### Gojira Time Conversion
- Gojira age in "years" uses a different scale than human years
- Growth rate system exists (see `_Entity_Registry` and extracted content)
- Always note which timescale is being used

### Ambiguous "Present"
- Many prompts discuss events as "current" without specifying when
- Default assumption: Post-Antitheriomorphosis unless context indicates otherwise

### Contradictory Ages
- Some sources give different ages for the same character at the same point
- Flag these for review rather than choosing one

---

## Related Skills

- [[CONTINUITY_SENTINEL]] - Reviews flagged contradictions
- [[ARC_WEAVER]] - Maps events to story arcs
- [[CHARACTER_SYNTHESIZER]] - Uses age data for profiles

---

*The CHRONOLOGIST sees time as the skeleton upon which all worldbuilding hangs. Every event has a when.*
