# Module 1 — AI-Powered File & Task Management

## 📚 Overview

This module teaches **effective AI collaboration** for everyday productivity tasks. Through three hands-on exercises, you'll learn how to craft prompts that get reliable, consistent results when organizing files, analyzing content, and prioritizing tasks.

---

## 🎯 Learning Outcomes

By completing this module, you will be able to:

1. **Write Effective Prompts**: Progress from vague to professional instructions
2. **Choose Prompt Strategies**: Know when to use outcome-focused vs. step-by-step prompts
3. **Define Classification Criteria**: Make your priorities explicit for consistent AI decisions
4. **Organize Information**: Structure files and tasks by purpose, not just type
5. **Handle Ambiguity**: Flag edge cases for human review instead of silent failures
6. **Create Audit Trails**: Generate summary reports for transparency and verification

---

## 📁 Exercise Structure

```
module-1/
├── README.md                      # This file - module overview
├── exercise-1.1-messy-downloads/  # Prompt iteration practice
├── exercise-1.2-photo-album/      # Prompt strategy comparison
└── exercise-1.3-inbox-zero/       # Priority-based classification
```

---

## 🗂️ Exercises

### Exercise 1.1 — The Messy Downloads Folder

**Theme:** Iterative Prompt Refinement  
**Time:** 30-45 minutes  
**Difficulty:** Beginner

A chaotic downloads folder with 35 mixed files teaches you to progressively refine prompts from vague to professional.

| Attempt | Prompt Style | Result |
|---------|--------------|--------|
| 1 | "Organize these files" | Simple type-based organization (scatters related files) |
| 2 | Add topic + naming specs | Better grouping, some inconsistencies remain |
| 3 | Professional specification | Topic-based folders, consistent naming, version tracking |

**Key Lessons:**
- Simple prompts get simple results
- Topic-based organization > type-based for findability
- Naming conventions matter for long-term maintainability
- Save your final prompt as a reusable template

📖 [Detailed Guide →](./exercise-1.1-messy-downloads/README.md)

---

### Exercise 1.2 — Photo Album Builder

**Theme:** Prompt Strategy Comparison  
**Time:** 45-60 minutes  
**Difficulty:** Intermediate

Sort 24 SVG images by orientation, flag duplicates, and create an HTML gallery using two different prompting approaches.

| Approach | Style | Best For |
|----------|-------|----------|
| A | Outcome-focused ("I want a gallery...") | Simple, familiar tasks |
| B | Step-by-step ("1. Examine each file...") | Complex, specific requirements |

**Key Lessons:**
- Match prompt style to task complexity
- AI can analyze file properties (dimensions, metadata)
- Duplicate detection requires multiple signals
- Visual output needs structure and labeling

📖 [Detailed Guide →](./exercise-1.2-photo-album/README.md)

---

### Exercise 1.3 — The Inbox Zero Challenge

**Theme:** Priority-Based Classification  
**Time:** 30-45 minutes  
**Difficulty:** Beginner to Intermediate

Triage 18 simulated emails into action categories (respond-today, this-week, read-later, archive, delete) based on YOUR priorities.

| Category | Timeframe | Count |
|----------|-----------|-------|
| respond-today | < 24 hours | 6 |
| this-week | 2-7 days | 4 |
| read-later | No action | 1 |
| archive | Keep records | 5 |
| delete | Remove | 2 |

**Key Lessons:**
- Priorities are personal — AI doesn't know them without explicit criteria
- Explicit criteria = consistent results
- Flag ambiguity for human review
- Action-oriented organization works best

📖 [Detailed Guide →](./exercise-1.3-inbox-zero/README.md)

---

## 🔗 Common Themes

All three exercises reinforce these core principles:

### 1. Explicit Criteria Matter
| Exercise | What Needs Explicit Criteria |
|----------|------------------------------|
| 1.1 | Organization structure, naming conventions, duplicate handling |
| 1.2 | Classification method, duplicate detection, gallery layout |
| 1.3 | Priority rules, urgency thresholds, edge case handling |

### 2. Iteration Improves Results
| Exercise | Iteration Pattern |
|----------|-------------------|
| 1.1 | Vague → Improved → Professional prompt |
| 1.2 | Outcome → Step-by-step comparison |
| 1.3 | Your priorities → Written rules → Consistent classification |

### 3. Audit Trails Build Trust
| Exercise | Audit Mechanism |
|----------|-----------------|
| 1.1 | README documenting structure and conventions |
| 1.2 | REPORT.md with statistics and duplicate flags |
| 1.3 | triage-summary.md with reasoning for each classification |

### 4. Ambiguity Should Be Flagged, Not Hidden
| Exercise | Ambiguous Cases |
|----------|-----------------|
| 1.1 | Files that don't fit any category → Misc folder |
| 1.2 | Near-duplicates → Flagged with badges |
| 1.3 | Borderline emails → Marked with ⚠ Ambiguous |

---

## 🛠️ Skills Developed

| Skill | Exercise 1.1 | Exercise 1.2 | Exercise 1.3 |
|-------|:------------:|:------------:|:------------:|
| Prompt Engineering | ✅ | ✅ | ✅ |
| File Management | ✅ | ✅ | ✅ |
| Classification Systems | ✅ | ✅ | ✅ |
| Critical Evaluation | ✅ | ✅ | ✅ |
| Documentation | ✅ | ✅ | ✅ |
| HTML/CSS | | ✅ | |
| Priority Assessment | | | ✅ |
| Decision Frameworks | | | ✅ |

---

## 🚀 Quick Start

### Recommended Order
1. **Start with 1.1** — Builds foundational prompt iteration skills
2. **Continue with 1.2** — Compares two prompting strategies
3. **Finish with 1.3** — Applies learning to priority-based decisions

### Prerequisites
- Basic computer file management
- Comfortable with text editors
- No programming experience required

### What You'll Need
- A text editor or IDE
- A terminal or file explorer
- An AI assistant (Claude, Cursor, etc.)

---

## 📖 Additional Resources

### Related Concepts
- **Information Architecture**: Organizing information for findability
- **Prompt Engineering**: Crafting effective AI instructions
- **GTD (Getting Things Done)**: Action-based task management
- **Eisenhower Matrix**: Urgent vs. Important framework
- **Inbox Zero**: Email management methodology

### Prompt Templates

**File Organization:**
```
Organize [FOLDER] into topic-based subfolders with:
- Numbered prefixes for sort order (01_, 02_, etc.)
- Consistent naming: lowercase, underscores, ISO dates
- Version tracking for duplicates (_v1, _v2)
- A summary report of all changes
```

**Multi-Step Tasks:**
```
1. [First step with clear criteria]
2. [Second step with clear criteria]
3. [Continue for each sub-task]
4. Generate a summary report with [specific fields]
```

**Classification/Triage:**
```
Classify [ITEMS] into: [CATEGORY 1], [CATEGORY 2], [CATEGORY 3]

Classification rules:
- [CATEGORY 1]: [Clear criteria]
- [CATEGORY 2]: [Clear criteria]

Requirements:
1. [Action for each item]
2. [Summary report format]
3. Flag ambiguous cases for review
```

---

## ✅ Module Completion Checklist

- [ ] Completed Exercise 1.1 (Messy Downloads)
- [ ] Completed Exercise 1.2 (Photo Album)
- [ ] Completed Exercise 1.3 (Inbox Zero)
- [ ] Reflected on prompt iteration patterns
- [ ] Saved reusable prompt templates
- [ ] Can explain when to use each prompt strategy

---

## 📊 Module Summary

| Aspect | Details |
|--------|---------|
| **Total Exercises** | 3 |
| **Estimated Time** | 1.5 - 2.5 hours |
| **Difficulty Range** | Beginner to Intermediate |
| **Core Skill** | AI Collaboration for Productivity |
| **Key Insight** | Explicit criteria + iteration = reliable results |

---

**Next Module:** Continue to Module 2 for advanced AI collaboration patterns.
