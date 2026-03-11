# Exercise 3.2 — Survey Analyzer

## Overview

This project analyzes 60 product survey responses to extract actionable insights about a software product. The analysis covers summary statistics, demographic patterns, open-feedback themes, and generates visual reports.

---

## What You Have

- **`product_survey_results.csv`** — 60 survey responses containing:
  - **Demographics**: age range, location, role, experience level
  - **6 Likert-scale questions** (1-5): ease of use, documentation, performance, support, value for money, likelihood to recommend
  - **Open-text feedback**: qualitative comments (some rows have it, some don't)

---

## What This Project Does

1. **Summary Statistics** — Calculates mean, median, standard deviation, and distribution for each survey question
2. **Pattern Detection** — Finds demographic subgroups whose ratings differ by more than 0.5 points from the overall average
3. **Theme Categorization** — Automatically categorizes open-text feedback into themes (positive, negative, feature requests, etc.)
4. **Visual Report** — Generates 6 charts showing key metrics and patterns
5. **Executive Memo** — Produces a 1-page summary suitable for non-technical managers

---

## Files Structure

```
exercise-3.2-survey-analyzer/
├── INSTRUCTIONS.md              # Original exercise instructions
├── product_survey_results.csv   # Source survey data (60 responses)
├── README.md                    # This file
└── sorted_doc/                  # Analysis outputs
    ├── survey_analysis.py       # Main analysis script
    ├── visual_summary.png       # Visual charts (PNG)
    ├── visual_summary.pdf       # Visual charts (PDF)
    └── key_findings_memo.md     # Executive summary memo
```

---

## Running the Analysis (Step-by-Step for Beginners)

Follow these steps to run the survey analysis:

### Step 1: Navigate to the Project Directory

Open your terminal and go to the exercise folder:

```bash
cd /path/to/exercise-3.2-survey-analyzer
```

### Step 2: Go to the `sorted_doc` Directory

```bash
cd sorted_doc
```

### Step 3: Create a Python Virtual Environment

A virtual environment keeps dependencies isolated from your system Python:

```bash
python3 -m venv venv
```

### Step 4: Activate the Virtual Environment

**On Linux/Mac:**
```bash
source venv/bin/activate
```

**On Windows:**
```bash
venv\Scripts\activate
```

You should see `(venv)` appear at the start of your terminal prompt.

### Step 5: Install Required Packages

Install the Python libraries needed for analysis:

```bash
pip install pandas numpy matplotlib
```

This installs:
- **pandas** — Data manipulation and analysis
- **numpy** — Numerical computing
- **matplotlib** — Chart generation

### Step 6: Run the Analysis Script

```bash
python survey_analysis.py
```

### Step 7: View the Results

After the script completes, you'll see:
- Console output with statistics and patterns
- Generated files in the `sorted_doc/` folder:
  - `visual_summary.png` — Charts image
  - `visual_summary.pdf` — Charts PDF
  - `key_findings_memo.md` — Executive memo

Open the memo in any markdown viewer or text editor to read the findings.

### Step 8: Deactivate the Virtual Environment (Optional)

When you're done:

```bash
deactivate
```

---

## Quick Command Summary

Copy and paste all commands at once:

```bash
cd /path/to/exercise-3.2-survey-analyzer/sorted_doc
python3 -m venv venv
source venv/bin/activate
pip install pandas numpy matplotlib
python survey_analysis.py
deactivate
```

---

## Output Files Explained

### `visual_summary.png` / `visual_summary.pdf`

Contains 6 charts:
1. **Overall Averages by Question** — Bar chart showing mean ratings
2. **Rating Distribution Heatmap** — How many 1s, 2s, 3s, 4s, 5s per question
3. **Average Rating by Role** — Comparison across job roles
4. **Average Rating by Experience Level** — Comparison across experience levels
5. **Top Feedback Themes** — Most common themes from open feedback
6. **Average Rating by Location** — Comparison across geographic regions

### `key_findings_memo.md`

A 1-page executive summary including:
- Overall satisfaction score
- Top 3 actionable insights
- Demographic patterns
- Question-by-question breakdown
- Recommended next steps

---

## Key Findings (Summary)

| Metric | Value |
|--------|-------|
| Overall Average | 3.27/5.0 |
| Highest-Rated Question | Ease of Use (3.37) |
| Lowest-Rated Question | Documentation (3.17) |
| Net Promoter-like Score | 20% |
| Patterns Detected | 36 |

### Top 3 Actionable Insights

1. **Mobile App Stability** — 8 users reported crashes (especially Android)
2. **Documentation Gaps** — Users spend hours figuring out basic features
3. **Pricing Communication** — Changes were poorly communicated to users

---

## Troubleshooting

### Error: `ModuleNotFoundError: No module named 'pandas'`

You haven't installed the required packages. Run:

```bash
pip install pandas numpy matplotlib
```

### Error: `externally-managed-environment`

Your system Python is protected. Use a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
pip install pandas numpy matplotlib
```

### Error: `python: command not found`

Try `python3` instead of `python`:

```bash
python3 -m venv venv
source venv/bin/activate
./venv/bin/pip install pandas numpy matplotlib
./venv/bin/python survey_analysis.py
```

---

## For Advanced Users

You can modify `survey_analysis.py` to:
- Change the pattern detection threshold (currently >0.5)
- Add new demographic comparisons
- Customize theme keywords for better categorization
- Export data to Excel or other formats

---

## License

This exercise is part of the Digita-FTEs basics training program.
