# Session & Rate Limit Tracker

> **Purpose:** Track rate limit status across sessions to maximize extraction efficiency.
> **Last Updated:** 2026-01-07

---

## Current Session Status

| Metric | Value |
|--------|-------|
| Session Start | 2026-01-07 |
| Agents Launched | 5 |
| Rate Limits Hit | 3 |
| Last Limit Hit | ~2026-01-07 07:00 (Asia/Shanghai) |
| Expected Reset | ~5 hours after limit |

---

## Rate Limit Patterns Observed

### Timing (Asia/Shanghai Timezone)
- Limits typically reset every ~5 hours
- Observed reset times: 9am, 2pm, 7pm, 12am
- Each agent consumes significant quota (300k-500k tokens per extraction batch)

### Capacity Guidelines
| Action | Token Cost (approx) | Safe Per Session |
|--------|---------------------|------------------|
| Single file read | 1-5k | Unlimited |
| Grep/search | <1k | Unlimited |
| Extraction agent (10 prompts) | 50-100k | 3-4 agents |
| Extraction agent (25 prompts) | 150-250k | 2 agents |
| Extraction agent (50 prompts) | 300-400k | 1-2 agents |

### Best Practices
1. **Batch size:** 15-25 prompts per agent is optimal
2. **Parallelization:** Max 3 agents at once to avoid mass rate limits
3. **Monitoring:** Check agent status before launching more
4. **Partial progress:** Agents often make significant progress before hitting limits
5. **Sequential fallback:** If limits are frequent, use single-agent sequential processing

---

## Agent Launch Protocol

### Before Launching Agents
1. Check this file for recent rate limit history
2. Estimate tokens needed for planned work
3. If 2+ agents hit limits in last hour, wait or reduce parallelization

### During Extraction
1. Launch agents in batches of 2-3
2. Monitor with non-blocking TaskOutput
3. Note agent IDs for potential resume
4. If agent hits limit, record time and expected reset

### After Rate Limit
1. Update this file with limit timestamp
2. Calculate expected reset (~5 hours)
3. Save agent IDs for resume
4. Document partial progress achieved

---

## Rate Limit History

### 2026-01-06 - 2026-01-07 (AA-Kratos Extraction)

| Time (Asia/Shanghai) | Event | Recovery |
|---------------------|-------|----------|
| ~Jan 6 afternoon | 3 agents hit limit after P199-P270 | Wait for reset |
| ~Jan 6 evening | Resumed, extracted P271-P328 | Partial before limit |
| ~Jan 7 morning | Final push P329-P344 | Complete |
| ~Jan 7 07:00 | Title standardization agent hit limit | Wait for reset |
| ~Jan 7 12:00 | Resumed, completed title standardization | Success |

---

## Session Handoff Checklist

When rate limit forces session end:

- [ ] Update `_Progress.md` with current status
- [ ] Update this file with rate limit timestamp
- [ ] Note any agent IDs for resume (in format: `aXXXXXX`)
- [ ] Document what was partially completed
- [ ] Calculate expected reset time

When resuming after rate limit:

- [ ] Read `_Progress.md` for overall status
- [ ] Read this file for rate limit context
- [ ] Check if previous agents can be resumed
- [ ] Plan work within expected quota

---

## Quick Reference

### Remaining Extraction Work
| Source | Unique Prompts | Est. Agents | Est. Tokens |
|--------|---------------|-------------|-------------|
| Saga-TG | 102 | 4-5 | 400-500k |
| Standing | 96 | 4-5 | 400-500k |
| BAA-Kratos | 70 | 3-4 | 300-400k |
| TG | 74 | 3-4 | 300-400k |
| Kratos | 49 | 2-3 | 200-300k |
| BTG | 61 | 3 | 250-300k |
| Eclipse-I | 46 | 2-3 | 200-250k |

### Post-Extraction Phases
| Phase | Est. Tokens | Notes |
|-------|-------------|-------|
| QA Validation | 50-100k | Quick scan of all files |
| Contradiction Detection | 100-200k | Cross-file comparison |
| Wikilink Addition | 100-150k | Entity recognition |
| Evolution Chains | 50-100k | Topic grouping |
| Index Generation | 20-50k | Catalog all files |

---

*Update this file whenever rate limits are encountered or sessions change.*
