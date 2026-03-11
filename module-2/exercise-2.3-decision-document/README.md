# Exercise 2.3 — Decision Document Comparison Guide

> **A beginner's guide to comparing AI-assisted decision documents and understanding the decision-making process.**

---

## 📋 Table of Contents

- [Overview](#overview)
- [What's in This Exercise](#whats-in-this-exercise)
- [Files Included](#files-included)
- [How to Compare Both Results](#how-to-compare-both-results)
- [Evaluation Criteria](#evaluation-criteria)
- [Decision Quality Checklist](#decision-quality-checklist)
- [For Beginners: Understanding Decision Documents](#for-beginners-understanding-decision-documents)
- [Key Takeaways](#key-takeaways)

---

## Overview

This exercise demonstrates how to create a **structured decision document** for a real career transition scenario: moving from web development into AI/ML engineering.

We generated **two versions** of the decision document:

| Version | Format | Purpose |
|---------|--------|---------|
| **Version A** | Markdown (`.md`) | Comprehensive reference document with detailed analysis |
| **Version B** | Word (`.docx`) | Polished, formal document ready for stakeholder presentation |

---

## What's in This Exercise

### The Decision Question

> Given $30,000 in savings, $2,500/month in fixed obligations, a supportive-but-risk-conscious partner, and 7 years of senior web development experience at $95K — which transition path into AI/ML engineering maximises long-term career and financial outcomes while keeping short-term financial risk within acceptable bounds?

### The Three Options Analysed

1. **Option 1: Full Career Pause** — Quit job, 6-month intensive bootcamp ($15K + lost income)
2. **Option 2: Gradual Transition** — Keep job, study 10-15 hrs/week for 12-18 months
3. **Option 3: AI-Adjacent Bridge Role** — Move into product role using existing web skills while learning AI on the job

---

## Files Included

```
exercise-2.3-decision-document/
├── README.md                              # This guide
├── INSTRUCTIONS.md                        # Original exercise instructions
├── decision-A-build-vs-buy.md             # Example decision document (reference)
├── decision-B-career-pivot.md             # Example decision document (reference)
├── decision-C-team-restructure.md         # Example decision document (reference)
├── decision-D-web-to-ai-ml-transition.md  # ✅ Our Markdown version (Version A)
├── Career-Transition-Decision-Document.docx # ✅ Our Word version (Version B)
└── generate_decision_doc.py               # Python script that generated the Word doc
```

---

## How to Compare Both Results

### Step 1: Read Both Documents

Open both files and read them completely:

```bash
# View Markdown version (any text editor or browser)
open decision-D-web-to-ai-ml-transition.md

# Open Word version (requires Microsoft Word or compatible viewer)
open Career-Transition-Decision-Document.docx
```

### Step 2: Check Structure Alignment

Both documents should contain the **same 7 sections**:

| # | Section | Markdown | Word |
|---|---------|----------|------|
| 1 | Decision Statement | ✅ | ✅ |
| 2 | Context & Background | ✅ | ✅ |
| 3 | Assumptions & Constraints | ✅ | ✅ |
| 4 | Three Options Analysed | ✅ | ✅ |
| 5 | Risk Assessment | ✅ | ✅ |
| 6 | Recommended Path | ✅ | ✅ |
| 7 | Next Steps | ✅ | ✅ |

### Step 3: Compare Content Depth

| Aspect | Markdown Version | Word Version |
|--------|------------------|--------------|
| **Detail Level** | More comprehensive, additional resources | Focused, executive-friendly |
| **Formatting** | Simple markdown headers | Professional styling, colours |
| **Tables** | Basic markdown tables | Colour-coded risk matrix |
| **Length** | ~4000 words (detailed) | ~2500 words (concise) |
| **Best For** | Personal reference, deep dive | Stakeholder presentation, printing |

### Step 4: Evaluate Decision Quality

Use the criteria below to assess whether both documents produce a **sound, defensible decision**.

---

## Evaluation Criteria

### 1. Decision Framing ✓

- [ ] Is the decision question **specific** (not vague)?
- [ ] Does it include **constraints** in the framing?
- [ ] Is it **actionable** (can be answered with analysis)?

**Good Example:**
> "Given constraints A, B, and C, which approach to X maximizes Y while minimizing Z?"

**Bad Example:**
> "Should I switch careers?"

### 2. Options Analysis ✓

- [ ] Are **2-3 distinct options** presented?
- [ ] Does each option include **realistic costs** (financial + opportunity)?
- [ ] Are **pros and cons** balanced (not biased toward one option)?
- [ ] Is there **evidence** supporting claims (not just opinions)?

### 3. Risk Assessment ✓

- [ ] Are **multiple risk dimensions** considered?
- [ ] Is risk **quantified or rated** (LOW/MEDIUM/HIGH)?
- [ ] Are risks **specific to each option** (not generic)?

### 4. Recommendation Quality ✓

- [ ] Is there **one clear recommendation** (not "it depends")?
- [ ] Is the rationale **grounded in stated constraints**?
- [ ] Does it **address stakeholder concerns** (e.g., partner's risk tolerance)?

### 5. Actionability ✓

- [ ] Are next steps **concrete** (not vague)?
- [ ] Does each action have an **owner** and **deadline**?
- [ ] Are there **5-7 specific actions** (not just "research more")?

---

## Decision Quality Checklist

Use this checklist to score both documents:

| Criterion | Markdown Score (1-5) | Word Score (1-5) | Notes |
|-----------|---------------------|------------------|-------|
| Decision framing is clear and specific | ⬜ | ⬜ | |
| Options are distinct and realistic | ⬜ | ⬜ | |
| Financial analysis is accurate | ⬜ | ⬜ | |
| Risk assessment is comprehensive | ⬜ | ⬜ | |
| Recommendation is clear and justified | ⬜ | ⬜ | |
| Next steps are actionable | ⬜ | ⬜ | |
| Addresses stakeholder concerns | ⬜ | ⬜ | |
| Professional presentation | ⬜ | ⬜ | |
| **Total** | **__/40** | **__/40** | |

**Scoring Guide:**
- 5 = Exceeds expectations
- 4 = Meets expectations fully
- 3 = Adequate but could improve
- 2 = Missing key elements
- 1 = Poor or absent

---

## For Beginners: Understanding Decision Documents

### What is a Decision Document?

A **decision document** is a structured written analysis that helps you (and stakeholders) make informed choices. It forces you to:

1. **Think clearly** before acting
2. **Document your reasoning** for future reference
3. **Communicate your decision** to others (manager, partner, team)
4. **Defend your choice** with evidence, not intuition

### Why Use This Format?

| Benefit | Explanation |
|---------|-------------|
| **Reduces bias** | Forces you to analyse multiple options, not just your preferred one |
| **Creates accountability** | Written record of why you chose a path |
| **Enables review** | Can revisit in 6 months to see if decision was sound |
| **Builds consensus** | Stakeholders can see your reasoning process |

### The 7-Section Structure Explained

```
┌─────────────────────────────────────────────────────────┐
│  1. DECISION STATEMENT                                  │
│     "What exact question are we answering?"             │
├─────────────────────────────────────────────────────────┤
│  2. CONTEXT & BACKGROUND                                │
│     "What situation are we in? What's relevant history?"│
├─────────────────────────────────────────────────────────┤
│  3. ASSUMPTIONS & CONSTRAINTS                           │
│     "What are the hard limits we must work within?"     │
├─────────────────────────────────────────────────────────┤
│  4. OPTIONS ANALYSED                                    │
│     "What are our realistic choices? Full analysis."    │
├─────────────────────────────────────────────────────────┤
│  5. RISK ASSESSMENT                                     │
│     "What could go wrong with each option?"             │
├─────────────────────────────────────────────────────────┤
│  6. RECOMMENDATION                                      │
│     "Which option do we choose and why?"                │
├─────────────────────────────────────────────────────────┤
│  7. NEXT STEPS                                          │
│     "What specific actions do we take now?"             │
└─────────────────────────────────────────────────────────┘
```

### Common Mistakes to Avoid

| Mistake | Why It's Bad | Fix |
|---------|--------------|-----|
| Vague decision question | Can't answer "should I be happy?" | Frame as "which option maximizes X given Y" |
| Only one option analysed | Not a decision, just justification | Always include 2-3 realistic alternatives |
| Ignoring constraints | Decision may be impossible to execute | List hard constraints upfront (money, time, people) |
| Hedging recommendation | Doesn't help anyone decide | Pick ONE option and defend it |
| Vague next steps | Decision never gets implemented | Specific actions with owners and deadlines |

---

## Key Takeaways

### For This Specific Decision

✅ **Recommended Path:** Gradual transition (Option 2) with bridge role elements (Option 3)

✅ **Why:** Maintains $95K income, respects partner's risk tolerance, preserves $30K savings, keeps options open

✅ **Timeline:** 12-18 months part-time study + active pursuit of AI-adjacent opportunities

### For Decision-Making Generally

1. **Frame the decision well** — A good question leads to a good answer
2. **Analyse multiple options** — Never decide between "do it" vs "don't do it"
3. **Quantify risks** — Use ratings or numbers, not just descriptions
4. **Address stakeholders** — Consider who else is affected and their concerns
5. **Make it actionable** — A decision without next steps is just thinking

---

## Further Resources

### Decision-Making Frameworks

- [WRAP Process](https://www.heathbrothers.com/) — *Decisive* by Chip & Dan Heath
- [Pros-Cons-Risks Framework](https://www.mindtools.com/) — MindTools
- [Decision Matrix Analysis](https://www.businessballs.com/) — BusinessBalls

### Career Transition Resources

- [Andrew Ng's ML Course](https://www.coursera.org/learn/machine-learning) — Foundational
- [Fast.ai](https://www.fast.ai/) — Practical deep learning
- [Hugging Face](https://huggingface.co/) — AI models and community

---

## About This Exercise

**Module:** 2 — Decision Making & Documentation  
**Exercise:** 2.3 — The Decision Document  
**Skill Focus:** Framing decisions clearly, structured analysis, stakeholder communication

**Learning Objectives:**
- [x] Frame a decision question precisely
- [x] Analyse multiple options with evidence
- [x] Assess risks across multiple dimensions
- [x] Make a clear recommendation grounded in constraints
- [x] Create actionable next steps with ownership

---

*Created: March 2026*  
*For: Digita FTEs Training Program*
