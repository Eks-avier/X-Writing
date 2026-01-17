# ATM Gemini Export - Branch Genealogy Map

> **Status:** EXTRACTION COMPLETE
> **Last Updated:** 2026-01-16

## Overview

All 9 conversation exports share a common trunk of **198 prompts** (extracted via Eclipse-II pilot). After P198, they diverge into different branches with unique content.

## Branch Tree

```
                        COMMON TRUNK (Prompts 1-198)
                        [Extracted from Eclipse-II]
                                    |
      +-----------------------------+-----------------------------+
      |                             |                             |
   KRATOS TRUNK                TITANUS TRUNK              ECLIPSE II BRANCH
   (Prompts 199-213)           (Prompts 199-202)          (Diverges at P199)
      |                             |                     [208 files]
      |                             |
      +--+--+                  +----+----+----+
      |  |  |                  |    |    |    |
     AA BAA TK               TG  STG  BTG  SH  EI
   [142][86][66]           [71][88][62][89][61]
```

## Source Reference

| Abbrev | Full Name | Prompts | Files | Status |
|--------|-----------|---------|-------|--------|
| Eclipse-II | The Eclipse of the ATM AU II | 245 | 208 | COMPLETE |
| AA-Kratos | AA - The Kratos of Kings | 344 | 142 | COMPLETE |
| Saga-TG | The Saga of the _Titanus gojira_ | 300 | 88 | COMPLETE (repaired) |
| Standing | Standing Hierarchy | 294 | 89 | COMPLETE (repaired) |
| BAA-Kratos | Branch of AA - The Kratos of Kings | 284 | 86 | COMPLETE (repaired) |
| TG | The _Titanus gojira_ | 276 | 71 | COMPLETE (repaired) |
| Kratos | The Kratos of Kings | 263 | 66 | COMPLETE |
| BTG | Branch of The _Titanus gojira_ | 263 | 62 | COMPLETE |
| Eclipse-I | The Eclipse of the ATM AU I | 260 | 61 | COMPLETE |

## Processing Status

- [x] Common trunk (P001-P198): Extracted via Eclipse-II
- [x] Kratos branch (AA-Kratos, BAA-Kratos, Kratos)
- [x] Titanus branch (TG, Saga-TG, BTG)
- [x] Standing branch
- [x] Eclipse branches (I and II)
- [x] Integrity audit and repairs (128 files re-extracted)
- [x] Duplicate detection and archival (36 files)

## Final Statistics

| Metric | Value |
|--------|-------|
| Total prompts across all files | 2,529 |
| Common trunk prompts | 198 |
| Active topic files | 873 |
| Archived duplicates | 36 |
| Sources repaired | 4 (Saga-TG, TG, Standing, BAA-Kratos) |
| Files re-extracted | 128 |

## Branch Overlap Analysis

The branch structure means significant content overlap exists:
- **P001-P198:** Identical across all 9 sources (extracted once from Eclipse-II)
- **P199-213:** Shared across Kratos trunk (AA, BAA, TK)
- **P199-202:** Shared across Titanus trunk (TG, STG, BTG, SH, EI)

This is why 2,529 prompts → 873 unique topic files (plus 36 archived duplicates within unique ranges).

---

See [[_MANIFESTO]] for complete extraction workflow documentation.
See [[_Duplicates]] for cross-source duplicate analysis.
