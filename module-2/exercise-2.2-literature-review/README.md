# Exercise 2.2 — Literature Review: Sleep and Cognitive Performance

## Project Overview

This exercise explored the effectiveness of **minimal vs. refined prompting** for generating research-quality content on the topic of **sleep and cognitive performance**. Two distinct outputs were produced, demonstrating how prompt specificity directly impacts output quality, structure, and actionability.

---

## Topic Selected

**Topic C: Sleep and Cognitive Performance**

From the brief:
> Sleep research has exploded in recent years. We know far more about how sleep affects memory, decision-making, creativity, and emotional regulation. Yet most knowledge workers consistently undervalue sleep.

**Key angles explored:**
- Differential effects of sleep deprivation on cognitive functions
- Nap research and cognitive recovery
- Screen habits and sleep quality
- Evidence for the "8-hour" recommendation
- Sleep quality vs. quantity distinction

---

## Prompt Iteration Process

### Round 1 — Minimal Prompt

**Prompt:**
> "Write a literature review about Sleep and Cognitive Performance."

**Output:** `literature-review-sleep-cognitive-performance.md` (~1,200 words)

**Characteristics:**
| Aspect | Observation |
|--------|-------------|
| Structure | Thematic organization (6 sections) |
| Depth | Graduate-level synthesis |
| Citations | Named studies (Van Dongen, Walker, Chang, etc.) |
| Tone | Academic but accessible |
| Actionability | General conclusions, no specific recommendations |
| Audience | Implicitly academic/research-literate |

**Strengths:**
- Comprehensive coverage of key themes
- Proper academic framing with introduction and conclusion
- Integrated specific study findings and mechanisms
- Addressed tensions from the topic brief (e.g., "I perform fine on 6 hours" myth)

**Limitations:**
- No explicit audience targeting
- No decision-oriented framing
- No concrete action steps for readers
- Structure emerged from model's default patterns, not explicit requirements

---

### Round 2 — Refined Prompt

**Prompt specifications:**
- **Audience:** University students + general public (dual audience)
- **Format:** Structured decision document (6 exact sections)
- **Tone:** "McKinsey brief meets science journalist" — rigorous but plain English
- **Depth:** Graduate-level research, explained accessibly
- **Requirements:** Specific study citations, mechanism naming, no vague claims
- **Output:** Word document (.docx) with professional formatting

**Output:** `decision-document-sleep-productivity.docx` (~1,400 words)

**Characteristics:**
| Aspect | Observation |
|--------|-------------|
| Structure | 6 prescribed sections with exact headings |
| Depth | Same research rigor, more explicit mechanisms |
| Citations | More granular (journal names, specific metrics) |
| Tone | Direct, decision-oriented, zero fluff |
| Actionability | Clear recommendation + 3 concrete weekly actions |
| Audience | Explicitly dual: students + lay readers |

**Strengths:**
- Decision-ready framing (options analysis with risk assessment)
- Explicitly addressed key tensions as dedicated sections
- Tables for cognitive domain comparisons (visual clarity)
- Actionable recommendations readers can implement immediately
- Professional formatting suitable for stakeholder distribution

**Limitations:**
- Required technical workaround (Python script for .docx generation)
- More constrained creative synthesis due to rigid structure

---

## Comparison: Round 1 vs. Round 2

| Dimension | Round 1 (Minimal) | Round 2 (Refined) |
|-----------|-------------------|-------------------|
| **Structure** | Emergent thematic | Prescribed 6-section decision doc |
| **Audience clarity** | Implicit academic | Explicit dual audience |
| **Citation specificity** | Study names + findings | Study names + journals + metrics |
| **Actionability** | General conclusions | Specific weekly actions |
| **Tone** | Academic review | Executive brief |
| **Format** | Markdown | Word document |
| **Decision utility** | Low (informative) | High (decision-ready) |
| **Prompt effort** | 1 sentence | ~200 words of specifications |

---

## Key Learnings

### 1. Prompt Specificity Drives Output Utility
The minimal prompt produced a **competent literature review**. The refined prompt produced a **decision instrument**. Same underlying research, fundamentally different utility.

### 2. Audience Specification Matters
Explicitly naming "university students + general public with no scientific background" forced the model to:
- Explain mechanisms in plain English
- Avoid unexplained jargon
- Define technical terms (e.g., SWS, REM, adenosine)

### 3. Structure Requests Shape Thinking
Requiring specific sections (Options Analysed, Key Tensions, Evidence Synthesis) forced:
- Comparative analysis rather than descriptive summary
- Explicit risk assessment for each option
- Thematic synthesis rather than source-by-source listing

### 4. Tone Guidance Affects Readability
"McKinsey brief meets science journalist" produced:
- Shorter paragraphs
- Bold key phrases for skimming
- Tables for dense comparisons
- Direct recommendations without hedging

### 5. Format Requirements Have Technical Costs
Requesting .docx output required:
- Python virtual environment setup
- `python-docx` library installation
- Custom script creation and debugging
- Cleanup of temporary files

**Trade-off:** Markdown is frictionless; Word documents require tooling but offer professional presentation for non-technical stakeholders.

---

## Technical Creation Process

### Environment Setup
```bash
# Create virtual environment
python3 -m venv /tmp/docx-env

# Install python-docx
/tmp/docx-env/bin/pip install python-docx -q
```

### Document Generation Workflow
1. Wrote Python script using `python-docx` library
2. Defined document structure with headings, tables, and styled paragraphs
3. Encountered syntax errors (unmatched parentheses) — debugged iteratively
4. Encountered API error (`add_paragraph()` doesn't accept `level` argument) — fixed by using `add_heading()` for subheadings
5. Executed successfully, generated 43 KB .docx file
6. Cleaned up temporary Python script

### Lessons from Technical Process
- **Test incrementally:** Large scripts fail silently; build section by section
- **Know the API:** `python-docx` has specific methods; `add_heading()` for headings, `add_paragraph()` for body text
- **Virtual environments prevent conflicts:** System Python (3.12) blocked direct installation; venv bypassed this

---

## Research Insights: Sleep and Cognitive Performance

### Core Findings Synthesized

1. **Sleep deprivation produces cumulative, unrecognized deficits**
   - Van Dongen et al. (2003): 6 hours/night for 14 days = 24-hour total deprivation equivalence
   - Self-assessment becomes unreliable due to prefrontal impairment

2. **Naps mitigate but don't eliminate chronic restriction**
   - 10-minute naps: Immediate alertness, no inertia
   - 90-minute naps: Full cycle benefits, but still inferior to nocturnal sleep

3. **Screen exposure has dual mechanisms**
   - Blue light (460nm) suppresses melatonin via retinal ganglion cells
   - Content arousal increases cortisol independently

4. **8-hour rule is heuristic, not universal**
   - 95% of adults need 7–9 hours
   - DEC2 mutation enables short sleep in ~1% of population
   - Base rate: assume you're not a natural short sleeper

5. **Quality and quantity are independent predictors**
   - Fragmented 8-hour sleep ≈ 4-hour continuous sleep deficits
   - High efficiency cannot fully compensate for chronic 5-hour duration

### Recommendation
**Option B — 8-Hour Baseline** is the evidence-supported choice for sustainable cognitive performance. The opportunity cost of 1–2 hours less work time is offset by 20–40% higher per-hour productivity and eliminated burnout risk.

---

## Files in This Repository

| File | Description |
|------|-------------|
| `INSTRUCTIONS.md` | Original exercise brief |
| `topic-C-sleep-and-cognitive-performance.md` | Topic selection brief |
| `literature-review-sleep-cognitive-performance.md` | Round 1 output (minimal prompt) |
| `decision-document-sleep-productivity.docx` | Round 2 output (refined prompt) |
| `README.md` | This documentation |

---

## Reflections on the Exercise

### What Worked Well
- **Thematic organization** in both outputs prevented source-by-source listing
- **Specific study citations** (Van Dongen, Walker, Chang) added credibility
- **Mechanism naming** (adenosine, prefrontal glucose metabolism, amygdala reactivity) moved beyond vague claims

### What Could Improve
- **Round 1 could have been more critical:** Accepted topic brief angles without questioning
- **Round 2 structure was rigid:** Some sections feel formulaic rather than organic
- **Neither output addressed limitations:** No discussion of publication bias, replication crisis, or individual variability beyond genetics

### Prompt Engineering Takeaways
1. **Specify audience explicitly** — even if obvious
2. **Name the format** — "decision document" vs. "literature review" produces different thinking
3. **Require mechanisms, not claims** — "studies suggest" → "Van Dongen found X via Y method"
4. **Ask for tensions** — forces engagement with contradictory evidence
5. **Request actions** — transforms information into behavior change

---

## Conclusion

This exercise demonstrated that **prompt refinement is force multiplication**. The same underlying knowledge produced:
- Round 1: An informative literature review
- Round 2: A decision-ready instrument with actionable recommendations

The additional ~200 words of prompt specification yielded exponentially higher practical utility — particularly for the target audience of students and general readers who need to *act* on information, not just understand it.

**Final insight:** The best prompt is not the shortest; it's the one that produces output matching your actual use case.

---

*Document prepared for Exercise 2.2 — Literature Review*  
*Date: March 11, 2026*
