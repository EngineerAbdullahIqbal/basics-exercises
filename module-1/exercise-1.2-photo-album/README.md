# Exercise 1.2 — Photo Album Builder

## 📚 What We Learned

This exercise teaches **prompting strategies comparison** by asking you to write instructions two different ways and analyze which produces better results for multi-step tasks.

---

## 🎯 Learning Objectives

By completing this exercise, you will learn:

1. **Outcome vs. Process Prompting**: When to specify the result vs. the steps
2. **Multi-Step Task Decomposition**: Breaking complex tasks into sub-tasks
3. **File Analysis**: Examining file properties (dimensions, metadata) for classification
4. **Duplicate Detection**: Identifying similar files by name patterns and file sizes
5. **HTML Generation**: Creating visual galleries from file collections
6. **Report Writing**: Summarizing findings in structured formats

---

## 📁 Exercise Structure

```
photo-album/
├── INSTRUCTIONS.md          # Original exercise instructions
├── photos/                  # Source images (24 SVG files)
│   ├── landscape/           # Sorted: 14 landscape images
│   └── portrait/            # Sorted: 10 portrait images
├── gallery.html             # Generated HTML gallery
├── REPORT.md                # Analysis report
└── README.md                # This file - learning guide
```

---

## 🎨 The Two-Approach Challenge

### Approach A: Outcome-Focused Prompt
```
"I want a photo gallery organized by orientation with duplicates flagged."
```

**What This Does:**
- Tells the AI **WHAT** you want, not **HOW** to do it
- Lets the AI decide the implementation approach
- Works well for simple, well-understood tasks

**Potential Issues:**
- AI might make assumptions about your preferences
- May skip steps you considered important
- Results vary based on AI's interpretation

---

### Approach B: Step-by-Step Prompt
```
"1. Examine each SVG file and read its width/height attributes
2. Sort into two folders: landscape (width ≥ height) and portrait (height > width)
3. Compare filenames and file sizes to identify potential duplicates
4. Create an HTML page with thumbnail grid layout
5. Add badges to mark duplicate images
6. Write a summary report with statistics"
```

**What This Does:**
- Specifies **exact steps** to follow
- Reduces ambiguity and assumptions
- Ensures all requirements are addressed

**Potential Issues:**
- More verbose to write
- May constrain AI's problem-solving creativity
- Time-consuming for simple tasks

---

## 📊 Results Comparison

| Aspect | Approach A (Outcome) | Approach B (Steps) |
|--------|---------------------|-------------------|
| **Accuracy** | Good | Excellent |
| **Completeness** | May miss details | All steps covered |
| **Creativity** | AI chooses approach | Follows your method |
| **Speed** | Faster to prompt | More setup time |
| **Best For** | Simple, familiar tasks | Complex, specific requirements |

---

## 🔍 Task Breakdown

### Sub-Task 1: Orientation Detection
**Method:** Read SVG `width` and `height` attributes

```
Landscape: width ≥ height (e.g., 800×600)
Portrait: height > width (e.g., 600×800)
```

**Files Sorted:**
- **Landscape:** 14 files (autumn_forest.svg, mountain_view.svg, etc.)
- **Portrait:** 10 files (portrait_ali.svg, cat_sitting.svg, etc.)

---

### Sub-Task 2: Duplicate Detection
**Methods Used:**

| Method | Example | Detection |
|--------|---------|-----------|
| **Filename patterns** | `cat_sitting.svg` vs `cat_sitting_2.svg` | `_2`, `_copy`, `_edited` suffixes |
| **File size comparison** | 607 bytes vs 620 bytes | Similar sizes suggest same content |

**Duplicates Found:**
1. `cat_sitting.svg` ↔ `cat_sitting_2.svg`
2. `portrait_ali.svg` ↔ `portrait_ali_edited.svg`
3. `sunset_beach.svg` ↔ `sunset_beach_copy.svg`

---

### Sub-Task 3: HTML Gallery Generation
**Features Implemented:**
- CSS Grid layout with responsive thumbnails
- 200×200px thumbnail display
- Filename labels on hover
- Duplicate badges (red flag icon)
- Summary statistics section
- Clean, modern styling

---

### Sub-Task 4: Summary Report
**Statistics Generated:**

| Metric | Count |
|--------|-------|
| Total Images | 24 |
| Landscape | 14 |
| Portrait | 10 |
| Duplicate Pairs | 3 |

---

## 💡 Key Takeaways

### 1. Match Prompt Style to Task Complexity
- **Simple tasks** → Outcome-focused prompts are faster
- **Complex tasks** → Step-by-step ensures nothing is missed

### 2. AI Can Analyze File Properties
SVG files contain metadata (width, height) that AI can read and use for classification — not just filename patterns.

### 3. Duplicate Detection Requires Multiple Signals
- Filename patterns alone miss renamed copies
- File size comparison catches near-duplicates
- Combining methods increases accuracy

### 4. Visual Output Needs Structure
HTML galleries require:
- Consistent image sizing
- Clear labeling
- Visual indicators for special cases (duplicates)
- Responsive layout for different screens

### 5. Reports Provide Accountability
A summary report lets you:
- Verify all files were processed
- Quick-check statistics
- Document decisions made

---

## 🛠️ Skills Developed

| Skill | Application |
|-------|-------------|
| **Prompt Strategy** | Choosing outcome vs. process prompts |
| **File Analysis** | Reading metadata for classification |
| **Pattern Recognition** | Identifying duplicates by name/size |
| **HTML/CSS** | Creating visual galleries |
| **Data Summarization** | Generating statistics and reports |
| **Critical Evaluation** | Comparing two approaches |

---

## 🚀 Apply This Learning

### When to Use Outcome-Focused Prompts:
```
"Create a contact form with validation"
"Summarize this article in 3 bullet points"
"Find all TODO comments in my code"
```

### When to Use Step-by-Step Prompts:
```
"1. Parse the CSV file
2. Filter rows where status = 'active'
3. Group by department
4. Calculate average salary per department
5. Export as JSON with specific schema"
```

### Hybrid Approach (Best of Both):
```
"I need a photo gallery organized by orientation (outcome).
Please: examine dimensions, sort into folders, flag duplicates, 
and create an HTML page (key steps)."
```

---

## 📖 Related Concepts

- **Task Decomposition**: Breaking complex problems into smaller steps
- **Classification Algorithms**: Sorting items by properties
- **Duplicate Detection**: Fuzzy matching, similarity scoring
- **Information Visualization**: Presenting data in accessible formats
- **Prompt Engineering**: Outcome vs. process specification

---

## ✅ Completion Checklist

- [ ] Wrote Approach A prompt (outcome-focused)
- [ ] Wrote Approach B prompt (step-by-step)
- [ ] Compared results from both approaches
- [ ] Images sorted by orientation (landscape/portrait)
- [ ] Duplicates identified and flagged
- [ ] HTML gallery created and working
- [ ] Summary report generated
- [ ] Reflected on which approach worked better and why

---

## 🤔 Reflection Questions

1. Which approach gave you better results? Why?
2. Did the AI make any assumptions you didn't expect?
3. What would you add to your prompt next time?
4. When would you use each approach in real work?

---

**Time Estimate:** 45-60 minutes  
**Difficulty:** Intermediate  
**Prerequisites:** Basic file management, HTML familiarity helpful but not required
