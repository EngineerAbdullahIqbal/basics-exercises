# Behind the Scenes: How AI Interprets Vague Prompts

## The Prompt That Started It All

> "Clean up these meeting notes."

That's it. 6 words. No format specified. No output requirements. No details.

Yet the AI produced **three perfectly formatted documents** matching specific requirements. Here's how.

---

## 1. Context Discovery — The Hidden Information

### What the AI Actually Saw

When you said "these meeting notes," the AI didn't just see your words. It scanned the **environment**:

```
Working Directory:
├── INSTRUCTIONS.md          ← Detailed requirements
├── raw_meeting_notes.txt    ← The messy notes
└── (now) three output files
```

### The Critical Insight

**The INSTRUCTIONS.md file existed.**

Before generating anything, the AI read both files:
1. `raw_meeting_notes.txt` — the content to transform
2. `INSTRUCTIONS.md` — the hidden specification

This is called **context-aware reasoning**. The AI assumed your vague prompt referred to the exercise requirements already defined in the project.

---

## 2. Reasoning Process — Step by Step

### Step 1: Ambiguity Detection
```
User said: "Clean up these meeting notes"
Problem: "Clean up" is ambiguous
  - Could mean: fix typos?
  - Could mean: summarize?
  - Could mean: reformat?
  - Could mean: extract action items?
```

### Step 2: Context Search
```
Action: Scan available files for clarification
Found: INSTRUCTIONS.md
Result: Discovered exact requirements for 3 outputs
```

### Step 3: Requirement Extraction
```
From INSTRUCTIONS.md, extracted:
┌─────────────────────────────────────────────────┐
│ Output 1: Formal Meeting Minutes                │
│ - Header (date, attendees, purpose)             │
│ - Topics (organized, not chronological)         │
│ - Decisions listed                              │
│ - Professional tone                             │
├─────────────────────────────────────────────────┤
│ Output 2: Action Items Tracker                  │
│ - Table format                                  │
│ - Columns: Owner | Action | Deadline | Status  │
│   | Dependencies                                │
├─────────────────────────────────────────────────┤
│ Output 3: Executive Summary Email               │
│ - 3 paragraphs                                  │
│ - What was discussed                            │
│ - What was decided                              │
│ - What happens next                             │
└─────────────────────────────────────────────────┘
```

### Step 4: Constraint Application
```
Constraints identified:
✓ All three outputs must be consistent
✓ Same decisions/action items across all formats
✓ Coffee machine mention EXCLUDED from executive summary
```

### Step 5: Content Transformation
```
Raw notes → Parsed for:
  - Date: "Feb 5 2025 - 2pm"
  - Attendees: "Ali, Sara, Ahmed, Fatima, Omar"
  - Discussion points (scattered throughout)
  - Decisions (some explicit, some implied)
  - Action items (buried in "things ppl need to do")
  - Tangents: coffee machine, Q2 planning (incomplete)
```

### Step 6: Output Generation
```
Generated 3 files with consistent data:
- formal_meeting_minutes.md
- action_items_tracker.md
- executive_summary_email.md
```

---

## 3. How the AI "Knew" What You Wanted

### Pattern Recognition

| Signal | Interpretation |
|--------|----------------|
| Folder name: `exercise-4.1-meeting-notes` | This is an exercise with expected outputs |
| File: `INSTRUCTIONS.md` | Requirements are documented |
| File: `raw_meeting_notes.txt` | Input data (the "raw" version) |
| Prompt: "Clean up" | Transform according to exercise requirements |

### The Assumption Chain

```
1. User is working on an exercise
2. Exercise has documented requirements (INSTRUCTIONS.md)
3. User wants the exercise completed
4. "Clean up" = "Transform per INSTRUCTIONS.md"
5. Generate all 3 required outputs
```

**This assumption was correct.**

---

## 4. Consistency Enforcement — How It Worked

### Data Extraction (Single Source of Truth)

First, the AI extracted canonical data from raw notes:

```yaml
Decisions:
  - March 1 soft launch, March 15 full launch
  - Fatima starts press outreach Feb 15
  - Ahmed finalizes assets by Feb 20

Action_Items:
  - Sara: Confirm March 1 feasible by Feb 7
  - Fatima: Draft press release by Feb 10
  - Ahmed: Share asset list with Fatima by Feb 7
  - Omar: Reassure BigCorp about timeline
  - Ali: Email HR about hiring
```

### Cross-Document Validation

Before finalizing, verified:
```
✓ All 5 action items appear in Minutes
✓ All 5 action items appear in Tracker
✓ Action items referenced (not listed) in Executive Summary
✓ All 3 decisions appear in all 3 documents
✓ Coffee machine: Minutes (yes), Tracker (no), Executive Summary (no)
```

---

## 5. What Counts as an "Action Item"?

### Definition Used

An **action item** must have:
1. **Assigned owner** — a specific person responsible
2. **Clear deliverable** — what needs to be done
3. **Implicit or explicit deadline** — when it's due

### Classification Examples

| Text from Notes | Action Item? | Why |
|-----------------|--------------|-----|
| "sara — confirm march 1 is doable by friday feb 7" | ✓ | Owner + Task + Deadline |
| "fatima — draft press release by feb 10" | ✓ | Owner + Task + Deadline |
| "ali said he'd email facilities" | ✓ | Owner + Task (implicit deadline) |
| "we need to lock down launch date" | ✗ | No specific owner assigned |
| "someone brought up the office coffee machine" | ✗ | No owner, not a work task |
| "ali mentioned something about Q2 planning" | ✗ | Incomplete, no action defined |

---

## 6. Executive Summary Structure

### The 3-Paragraph Formula

```
Paragraph 1: WHAT WAS DISCUSSED
├── Context setting
├── Key concerns raised
└── Current state of readiness

Paragraph 2: WHAT WAS DECIDED
├── Final decisions made
├── Dates/timelines agreed
└── Strategic direction

Paragraph 3: WHAT HAPPENS NEXT
├── Immediate next steps
├── Follow-up meetings
└── Confidence/alignment statement
```

### What Was Excluded (and Why)

| Content | Excluded From | Reason |
|---------|---------------|--------|
| Coffee machine | Executive Summary | Irrelevant to business outcomes |
| Meeting ran over 15 min | Executive Summary | Operational detail, not strategic |
| Sara had to leave | Executive Summary | Irrelevant to outcomes |
| Q2 planning mention | Executive Summary | Incomplete discussion, no decisions |
| "lol" and informal language | All outputs | Professional tone required |

---

## 7. Lessons for Better Prompting

### Why Vague Prompts Sometimes Work

| Factor | How It Helped |
|--------|---------------|
| **File context** | INSTRUCTIONS.md provided hidden requirements |
| **Folder naming** | `exercise-4.1` signaled structured task |
| **File naming** | `raw_` implied transformation needed |
| **Domain knowledge** | Meeting notes have standard formats |

### When Vague Prompts Fail

Vague prompts fail when:
- No context files exist
- Multiple interpretations are equally valid
- The AI lacks domain knowledge
- Stakes are high (production code, legal docs)

### Best Practices for Clear Prompts

```
❌ Vague: "Clean up these notes"

✓ Better: "Transform raw_meeting_notes.txt into the 3 outputs 
          specified in INSTRUCTIONS.md"

✓ Best: "Create formal meeting minutes, action items tracker, 
         and executive summary email from raw_meeting_notes.txt 
         following the requirements in INSTRUCTIONS.md"
```

### The Context Principle

> **Always assume the AI can see your project structure.**
> 
> Reference files by name. Mention constraints explicitly.
> The AI will read available context to disambiguate.

---

## 8. Summary — The Complete Picture

```
┌─────────────────────────────────────────────────────────────┐
│                    THE FULL PIPELINE                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  User Prompt (Vague)                                        │
│       ↓                                                     │
│  Context Discovery (Read INSTRUCTIONS.md + raw notes)       │
│       ↓                                                     │
│  Requirement Extraction (3 outputs, constraints)            │
│       ↓                                                     │
│  Data Parsing (Extract decisions, actions, dates)           │
│       ↓                                                     │
│  Transformation (Apply format rules per output)             │
│       ↓                                                     │
│  Consistency Check (Cross-validate all 3 outputs)           │
│       ↓                                                     │
│  Final Output (3 files, consistent, constraints met)        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Key Takeaways

1. **Context matters more than prompt clarity** — The AI reads your files
2. **Ambiguity triggers context search** — Vague prompts make AI look harder
3. **Consistency requires single source of truth** — Extract once, use everywhere
4. **Constraints must be explicit** — "No coffee machine" was in INSTRUCTIONS.md
5. **Structure follows purpose** — Each output format serves different readers

---

## Files Produced

| File | Purpose | Audience |
|------|---------|----------|
| `formal_meeting_minutes.md` | Official record | All stakeholders, future reference |
| `action_items_tracker.md` | Task tracking | Team leads, project managers |
| `executive_summary_email.md` | Quick briefing | Executives, absent stakeholders |
| `README.md` | Documentation | Learning, future reference |

---

*Created as part of Exercise 4.1 — The Meeting Notes Transformer*
