# Project Management Tool Comparison — Iteration Analysis

**Exercise 2.1:** Comparison Matrix  
**Date:** March 11, 2026  
**Scenario:** 8-person startup selecting a project management tool (Trello, Asana, Notion, Linear)

---

## Overview

This directory contains **three iterations** of the same comparison task, each with different prompt quality and output depth. This analysis compares the prompts, methodologies, and results across all versions.

| Iteration | Folder | Prompt Quality | Output Quality |
|-----------|--------|----------------|----------------|
| **V1 (Vague)** | `Vauge_prompt_response/` | Low | Medium |
| **V2 (Better)** | `Second_better_camparision/` | Medium | Good |
| **V3 (Current)** | `working/tool-selection/` | High | Excellent |

---

## Prompt Comparison

### V1: Vague Prompt (Original)

**Characteristics:**
- ❌ No specific constraints mentioned
- ❌ No budget or team size specified
- ❌ No timeline or growth considerations
- ❌ Generic "compare these tools" request

**Result:** Generic comparison without actionable context.

---

### V2: Better Prompt (Second Iteration)

**Characteristics:**
- ✅ Included budget ($15/user/month)
- ✅ Mentioned team size (8 people)
- ✅ Noted mixed technical ability
- ✅ Listed integrations needed (Slack, Google Workspace)
- ✅ Included growth projection (25 users)

**Result:** More targeted comparison with relevant criteria.

---

### V3: Current Prompt (Final Iteration)

**Characteristics:**
- ✅ All V2 constraints PLUS:
- ✅ Explicit priority weights (High/Medium/Low)
- ✅ Exact column structure specified
- ✅ Scoring scale defined (1-5)
- ✅ Weighted total score requirement
- ✅ Color-coding specification for decision matrix
- ✅ Structured memo format with exact sections
- ✅ 2-week timeline constraint

**Result:** Precise, actionable output matching exact business needs.

---

## Criteria & Scoring Comparison

### V1: Vague Prompt Response

| Criteria | Scoring Method |
|----------|----------------|
| Price, Free tier, Learning curve, Mobile, Integrations, Reporting, Scalability, Visibility | Winner column only (no weighted scoring) |

**Issues:**
- No weights assigned to criteria
- No numerical scoring (just "Winner" labels)
- Inconsistent evaluation depth

---

### V2: Better Prompt Response

| Criteria | Weight | Scoring |
|----------|--------|---------|
| Price, Learning curve, Visibility, Integrations, Reporting, Scalability, Mobile | High/Medium/Low | 1-5 scale with weighted average |

**Improvements:**
- Added weights
- Numerical scoring (1-5)
- Weighted final score (Asana: 4.6, Trello: 4.1, Notion: 3.9, Linear: 3.5)

---

### V3: Current Prompt Response

| Criteria | Weight | Weight Value | Scoring Method |
|----------|--------|--------------|----------------|
| Price per user | High | 3 | 1-5 per tool |
| Learning curve | High | 3 | 1-5 per tool |
| Slack + Google integration | High | 3 | 1-5 per tool |
| Mobile app quality | Medium | 2 | 1-5 per tool |
| Reporting / visibility | Medium | 2 | 1-5 per tool |
| Scalability to 25 users | Medium | 2 | 1-5 per tool |
| Free tier usefulness | Low | 1 | 1-5 per tool |

**Final Weighted Scores:**
| Tool | Score |
|------|-------|
| Asana | **64** |
| Trello | **58** |
| Notion | **57** |
| Linear | **49** |

**Improvements:**
- Explicit weight values (High=3, Medium=2, Low=1)
- Color-coded decision matrix (Green/Yellow/Red)
- Separate spreadsheet tabs (raw scores + visual matrix)

---

## Output Files Comparison

### V1: Vague Prompt

| File | Format | Quality |
|------|--------|---------|
| `scenario-A-comparison.csv` | CSV | Basic table, winner column only |
| `scenario-A-detailed-comparison.md` | Markdown | Long-form, good detail but unstructured |

**Issues:**
- No weighted scoring
- Memo embedded in comparison doc (not separate)
- No visual decision matrix

---

### V2: Better Prompt

| File | Format | Quality |
|------|--------|---------|
| `scenario-A-comparison-matrix.csv` | CSV | Detailed with pricing, features, scores |
| `scenario-A-recommendation-memo.md` | Markdown | Structured memo with timeline |

**Improvements:**
- Separate memo file
- Implementation timeline included
- Budget breakdown ($87.92/month)
- Clear "Why Not the Others" section

---

### V3: Current Prompt

| File | Format | Quality |
|------|--------|---------|
| `tool-comparison.xlsx` | Excel | Two sheets: scores + color-coded matrix |
| `recommendation-memo.md` | Markdown | Structured per exact specifications |
| `tool-comparison.csv` | CSV | Backup format |

**Improvements:**
- Excel with formatting (bold headers, borders)
- Color-coded cells (Green=4-5, Yellow=3, Red=1-2)
- Legend and summary rankings
- Memo follows exact 4-section structure requested

---

## Recommendation Quality Comparison

### All Three Agree: **Asana Wins**

| Iteration | Winner | Score | Key Reason |
|-----------|--------|-------|------------|
| V1 | Asana | 9/10 | Best for mixed tech-savviness |
| V2 | Asana | 4.6/5 | Superior visibility & integrations |
| V3 | Asana | 64 pts | Workload visibility (5/5), Integrations (5/5), Scalability (5/5) |

---

## Key Differences in Recommendations

### V1 (Vague)
- Generic reasoning
- No specific mitigation strategies
- Basic implementation timeline

### V2 (Better)
- Budget breakdown included
- 2-week implementation plan with specific tasks
- "Why Not the Others" comparison table

### V3 (Current)
- **Mitigation strategy for weakness** (onboarding plan with 3 steps)
- **Runner-up section** with "when to choose instead" guidance
- **Decision deadline** calculated (March 25, 2026)
- **Next steps** with evaluation metrics

---

## Scoring Accuracy Check

| Tool | V2 Score | V3 Score | Difference | Notes |
|------|----------|----------|------------|-------|
| Asana | 4.6/5 | 64 pts | Consistent | Both rate highest |
| Trello | 4.1/5 | 58 pts | Consistent | Both rate 2nd |
| Notion | 3.9/5 | 57 pts | Consistent | Close to Trello |
| Linear | 3.5/5 | 49 pts | Consistent | Both rate lowest |

**Observation:** Despite different scoring methods, rankings are identical across iterations.

---

## What Improved Across Iterations

### Prompt Specificity
| Aspect | V1 | V2 | V3 |
|--------|----|----|----|
| Budget specified | ❌ | ✅ | ✅ |
| Team size | ❌ | ✅ | ✅ |
| Timeline | ❌ | ❌ | ✅ (2 weeks) |
| Priority weights | ❌ | ⚠️ (mentioned) | ✅ (explicit values) |
| Output format | ❌ | ⚠️ | ✅ (exact columns) |
| Visual requirements | ❌ | ❌ | ✅ (color-coding) |

---

### Output Quality
| Aspect | V1 | V2 | V3 |
|--------|----|----|----|
| Weighted scoring | ❌ | ✅ | ✅ |
| Color-coding | ❌ | ❌ | ✅ |
| Separate memo | ❌ | ✅ | ✅ |
| Mitigation strategies | ❌ | ❌ | ✅ |
| Runner-up analysis | ⚠️ | ✅ | ✅ (with conditions) |
| Actionable next steps | ⚠️ | ✅ | ✅ (with metrics) |

---

## Lessons Learned

### 1. Prompt Engineering Matters
- **Vague prompt** → Generic output requiring manual refinement
- **Specific prompt** → Ready-to-use deliverables

### 2. Weights Change Decisions
- V1 had no weights → all criteria treated equally
- V3's explicit weights (High=3, Medium=2, Low=1) made scoring transparent and defensible

### 3. Visual Communication
- V3's color-coded matrix allows stakeholders to grasp results in seconds
- Green/Yellow/Red is universal language for "Good/Caution/Poor"

### 4. Mitigation > Weakness
- V3 didn't just list Asana's weakness (learning curve)
- Provided 3-step mitigation plan with timeline

### 5. Runner-Up Context
- V3 answered "When would I choose the runner-up?"
- This helps stakeholders understand trade-offs

---

## File Structure

```
module-2/exercise-2.1-comparison-matrix/
├── Vauge_prompt_response/          # Iteration 1 (Low specificity)
│   ├── scenario-A-comparison.csv
│   └── scenario-A-detailed-comparison.md
├── Second_better_camparision/      # Iteration 2 (Medium specificity)
│   ├── scenario-A-comparison-matrix.csv
│   └── scenario-A-recommendation-memo.md
└── working/tool-selection/         # Iteration 3 (High specificity)
    ├── tool-comparison.xlsx        # Color-coded matrix
    ├── tool-comparison.csv         # CSV backup
    └── recommendation-memo.md      # Structured memo
```

---

## Final Recommendation

**Use Iteration 3 (V3) deliverables for actual decision-making because:**

1. ✅ **Transparent methodology** — weights and scoring are explicit
2. ✅ **Visual communication** — color-coded matrix for quick stakeholder review
3. ✅ **Actionable mitigation** — addresses weaknesses with concrete steps
4. ✅ **Decision context** — explains when runner-up would be preferable
5. ✅ **Timeline awareness** — includes decision deadline and evaluation metrics

---

## How to Use This Analysis

| Audience | Recommended File |
|----------|------------------|
| **Stakeholders** | `working/tool-selection/recommendation-memo.md` (1-page summary) |
| **Analysts** | `working/tool-selection/tool-comparison.xlsx` (detailed matrix) |
| **Learning** | This README (understand prompt → output relationship) |

---

*Analysis completed for Exercise 2.1 — Comparison Matrix*
