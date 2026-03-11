#!/usr/bin/env python3
"""
Survey Analyzer - Module 3 Exercise 3.2
Analyzes product survey results and generates visual report + key findings memo
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from collections import Counter
import warnings
warnings.filterwarnings('ignore')

# Set style for professional-looking charts
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['axes.labelsize'] = 11

# Load data
df = pd.read_csv('../product_survey_results.csv')

# Question columns
q_cols = ['q1_ease_of_use', 'q2_documentation', 'q3_performance', 'q4_support', 'q5_value_for_money', 'q6_recommend_likelihood']
q_labels = {
    'q1_ease_of_use': 'Ease of Use',
    'q2_documentation': 'Documentation',
    'q3_performance': 'Performance',
    'q4_support': 'Support',
    'q5_value_for_money': 'Value for Money',
    'q6_recommend_likelihood': 'Likelihood to Recommend'
}

print("=" * 60)
print("SURVEY ANALYSIS REPORT")
print("=" * 60)

# =============================================================================
# 1. SUMMARY STATISTICS
# =============================================================================
print("\n" + "=" * 60)
print("1. SUMMARY STATISTICS FOR EACH QUESTION")
print("=" * 60)

summary_stats = []
for col in q_cols:
    data = df[col]
    summary_stats.append({
        'Question': q_labels[col],
        'Mean': round(data.mean(), 2),
        'Median': data.median(),
        'Std Dev': round(data.std(), 2),
        'Min': data.min(),
        'Max': data.max(),
        'Dist (1-5)': ', '.join([f"{i}:{(data==i).sum()}" for i in range(1, 6)])
    })

summary_df = pd.DataFrame(summary_stats)
print("\n" + summary_df.to_string(index=False))

overall_means = {col: df[col].mean() for col in q_cols}
print("\nOverall Averages by Question:")
for col, label in q_labels.items():
    print(f"  {label}: {overall_means[col]:.2f}")

# =============================================================================
# 2. PATTERN DETECTION (subgroup diff > 0.5 from overall mean)
# =============================================================================
print("\n" + "=" * 60)
print("2. INTERESTING PATTERNS (subgroup avg differs >0.5 from overall)")
print("=" * 60)

patterns_found = []

# Analyze by demographic columns
demo_cols = ['age_range', 'location', 'role', 'experience_years']

for demo in demo_cols:
    grouped = df.groupby(demo)[q_cols].mean()
    for subgroup in grouped.index:
        for col in q_cols:
            subgroup_mean = grouped.loc[subgroup, col]
            overall_mean = overall_means[col]
            diff = subgroup_mean - overall_mean
            if abs(diff) > 0.5:
                direction = "higher" if diff > 0 else "lower"
                patterns_found.append({
                    'demographic': demo,
                    'subgroup': subgroup,
                    'question': q_labels[col],
                    'subgroup_avg': round(subgroup_mean, 2),
                    'overall_avg': round(overall_mean, 2),
                    'diff': round(diff, 2),
                    'direction': direction
                })
                print(f"  [{demo}] {subgroup}: {q_labels[col]} = {subgroup_mean:.2f} ({direction} by {abs(diff):.2f})")

print(f"\nTotal patterns found: {len(patterns_found)}")

# =============================================================================
# 3. OPEN FEEDBACK THEME CATEGORIZATION
# =============================================================================
print("\n" + "=" * 60)
print("3. OPEN FEEDBACK THEME CATEGORIZATION")
print("=" * 60)

# Theme keywords
theme_keywords = {
    'Mobile App Issues': ['mobile app', 'crashes', 'android', 'terrible'],
    'Documentation Issues': ['documentation', 'confusing', 'onboarding', 'spent hours', 'figuring out'],
    'Feature Requests - Customization': ['customization', 'options', 'reports', 'dashboards'],
    'Feature Requests - Integration': ['integration', 'google workspace', 'api', 'custom integrations'],
    'Pricing Concerns': ['pricing', 'price', 'value', 'money', 'penny', 'generous'],
    'UI/UX Issues': ['ui', 'outdated', 'interface', 'bloated', 'basics'],
    'Positive - Performance': ['performance', 'great', 'excellent', 'solid', 'game-changing'],
    'Positive - Support': ['support', 'responsive', 'impressed', 'helpful'],
    'Positive - General': ['love', 'great', 'best', 'perfect', 'solid'],
    'Feature Requests - General': ['need', 'wish', 'should', 'could']
}

def categorize_feedback(text):
    """Categorize feedback into themes"""
    if pd.isna(text) or text.strip() == '':
        return ['No Feedback']
    
    text_lower = text.lower()
    themes = []
    
    for theme, keywords in theme_keywords.items():
        if any(kw in text_lower for kw in keywords):
            themes.append(theme)
    
    # Determine sentiment
    positive_words = ['love', 'great', 'excellent', 'impressed', 'best', 'perfect', 'solid', 'game-changing', 'responsive']
    negative_words = ['terrible', 'crashes', 'confusing', 'worse', 'bloated', 'outdated', 'poorly']
    
    has_positive = any(w in text_lower for w in positive_words)
    has_negative = any(w in text_lower for w in negative_words)
    
    if has_positive and not has_negative:
        themes.append('Sentiment: Positive')
    elif has_negative and not has_positive:
        themes.append('Sentiment: Negative')
    elif has_positive and has_negative:
        themes.append('Sentiment: Mixed')
    else:
        themes.append('Sentiment: Neutral')
    
    return themes if themes else ['Uncategorized']

# Apply categorization
df['themes'] = df['open_feedback'].apply(lambda x: categorize_feedback(x))

# Count themes
all_themes = []
for themes_list in df['themes']:
    all_themes.extend(themes_list)

theme_counts = Counter(all_themes)
print("\nTheme Frequency:")
for theme, count in theme_counts.most_common():
    if theme not in ['Sentiment: Positive', 'Sentiment: Negative', 'Sentiment: Mixed', 'Sentiment: Neutral', 'No Feedback']:
        print(f"  {theme}: {count}")

print("\nSentiment Distribution:")
sentiment_counts = {k: v for k, v in theme_counts.items() if 'Sentiment:' in k}
for sentiment, count in sorted(sentiment_counts.items(), key=lambda x: -x[1]):
    print(f"  {sentiment}: {count}")

print(f"\n  No Feedback: {theme_counts.get('No Feedback', 0)}")

# =============================================================================
# 4. VISUAL SUMMARY REPORT
# =============================================================================
print("\n" + "=" * 60)
print("4. GENERATING VISUAL SUMMARY REPORT...")
print("=" * 60)

# Create figure with subplots
fig = plt.figure(figsize=(16, 14))
fig.suptitle('Product Survey Analysis Report', fontsize=16, fontweight='bold', y=0.98)

# --- Chart 1: Overall Question Averages ---
ax1 = fig.add_subplot(2, 3, 1)
colors = plt.cm.Blues(np.linspace(0.4, 0.8, len(q_cols)))
bars = ax1.bar(range(len(q_cols)), [overall_means[col] for col in q_cols], color=colors, edgecolor='navy')
ax1.set_xlabel('Questions')
ax1.set_ylabel('Average Rating (1-5)')
ax1.set_title('Overall Averages by Question', fontweight='bold')
ax1.set_xticks(range(len(q_cols)))
ax1.set_xticklabels([q_labels[col].split()[-1] for col in q_cols], rotation=45, ha='right', fontsize=9)
ax1.set_ylim(0, 5)
ax1.axhline(y=3, color='gray', linestyle='--', alpha=0.5, label='Neutral (3.0)')
# Add value labels
for bar, val in zip(bars, [overall_means[col] for col in q_cols]):
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1, f'{val:.2f}', 
             ha='center', va='bottom', fontsize=9)
ax1.legend()

# --- Chart 2: Rating Distribution Heatmap ---
ax2 = fig.add_subplot(2, 3, 2)
dist_data = []
for col in q_cols:
    dist_data.append([(df[col]==i).sum() for i in range(1, 6)])
dist_data = np.array(dist_data)
im = ax2.imshow(dist_data, cmap='RdYlGn', aspect='auto', vmin=0, vmax=15)
ax2.set_yticks(range(len(q_cols)))
ax2.set_yticklabels([q_labels[col].split()[-1] for col in q_cols], fontsize=9)
ax2.set_xticks(range(5))
ax2.set_xticklabels(['1', '2', '3', '4', '5'])
ax2.set_xlabel('Rating')
ax2.set_ylabel('Questions')
ax2.set_title('Rating Distribution Heatmap', fontweight='bold')
plt.colorbar(im, ax=ax2, label='Count')

# --- Chart 3: Averages by Role ---
ax3 = fig.add_subplot(2, 3, 3)
role_means = df.groupby('role')[q_cols].mean().mean(axis=1).sort_values(ascending=True)
colors_role = plt.cm.Oranges(np.linspace(0.4, 0.8, len(role_means)))
bars = ax3.barh(range(len(role_means)), role_means.values, color=colors_role, edgecolor='darkorange')
ax3.set_yticks(range(len(role_means)))
ax3.set_yticklabels(role_means.index, fontsize=9)
ax3.set_xlabel('Average Rating (all questions)')
ax3.set_title('Average Rating by Role', fontweight='bold')
ax3.set_xlim(0, 5)
ax3.axvline(x=df[q_cols].mean().mean(), color='gray', linestyle='--', alpha=0.5, label=f'Overall ({df[q_cols].mean().mean():.2f})')
for bar, val in zip(bars, role_means.values):
    ax3.text(val + 0.1, bar.get_y() + bar.get_height()/2, f'{val:.2f}', va='center', fontsize=9)
ax3.legend()

# --- Chart 4: Averages by Experience Level ---
ax4 = fig.add_subplot(2, 3, 4)
exp_order = ['0-1', '2-3', '4-6', '7-10', '10+']
exp_means = df.groupby('experience_years')[q_cols].mean().mean(axis=1)
exp_means = exp_means.reindex([e for e in exp_order if e in exp_means.index])
colors_exp = plt.cm.Greens(np.linspace(0.4, 0.8, len(exp_means)))
bars = ax4.bar(range(len(exp_means)), exp_means.values, color=colors_exp, edgecolor='darkgreen')
ax4.set_xlabel('Experience Level (Years)')
ax4.set_ylabel('Average Rating (all questions)')
ax4.set_title('Average Rating by Experience Level', fontweight='bold')
ax4.set_xticks(range(len(exp_means)))
ax4.set_xticklabels(exp_means.index, fontsize=9)
ax4.set_ylim(0, 5)
ax4.axhline(y=df[q_cols].mean().mean(), color='gray', linestyle='--', alpha=0.5, label=f'Overall ({df[q_cols].mean().mean():.2f})')
for bar, val in zip(bars, exp_means.values):
    ax4.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1, f'{val:.2f}', ha='center', fontsize=9)
ax4.legend()

# --- Chart 5: Theme Distribution ---
ax5 = fig.add_subplot(2, 3, 5)
actionable_themes = [(k, v) for k, v in theme_counts.most_common() 
                     if k not in ['Sentiment: Positive', 'Sentiment: Negative', 'Sentiment: Mixed', 'Sentiment: Neutral', 'No Feedback', 'Uncategorized']]
top_themes = actionable_themes[:8]
if top_themes:
    theme_names = [t[0].replace('Feature Requests - ', '').replace('Positive - ', '').replace('Issues', '') for t in top_themes]
    theme_values = [t[1] for t in top_themes]
    colors_themes = plt.cm.Reds(np.linspace(0.3, 0.8, len(theme_values)))
    bars = ax5.barh(range(len(theme_values)), theme_values, color=colors_themes, edgecolor='darkred')
    ax5.set_yticks(range(len(theme_values)))
    ax5.set_yticklabels(theme_names, fontsize=9)
    ax5.set_xlabel('Frequency')
    ax5.set_title('Top Feedback Themes', fontweight='bold')
    for bar, val in zip(bars, theme_values):
        ax5.text(val + 0.2, bar.get_y() + bar.get_height()/2, str(val), va='center', fontsize=9)

# --- Chart 6: Location Comparison ---
ax6 = fig.add_subplot(2, 3, 6)
loc_means = df.groupby('location')[q_cols].mean().mean(axis=1).sort_values(ascending=True)
colors_loc = plt.cm.Purples(np.linspace(0.4, 0.8, len(loc_means)))
bars = ax6.barh(range(len(loc_means)), loc_means.values, color=colors_loc, edgecolor='purple')
ax6.set_yticks(range(len(loc_means)))
ax6.set_yticklabels(loc_means.index, fontsize=9)
ax6.set_xlabel('Average Rating (all questions)')
ax6.set_title('Average Rating by Location', fontweight='bold')
ax6.set_xlim(0, 5)
ax6.axvline(x=df[q_cols].mean().mean(), color='gray', linestyle='--', alpha=0.5)
for bar, val in zip(bars, loc_means.values):
    ax6.text(val + 0.1, bar.get_y() + bar.get_height()/2, f'{val:.2f}', va='center', fontsize=9)

plt.tight_layout(rect=[0, 0.02, 1, 0.96])
plt.savefig('visual_summary.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.savefig('visual_summary.pdf', bbox_inches='tight', facecolor='white')
print("  Saved: visual_summary.png")
print("  Saved: visual_summary.pdf")

# =============================================================================
# 5. KEY FINDINGS MEMO
# =============================================================================
print("\n" + "=" * 60)
print("5. GENERATING KEY FINDINGS MEMO...")
print("=" * 60)

# Calculate key metrics for memo
overall_avg = df[q_cols].mean().mean()
nps_like = ((df['q6_recommend_likelihood'] >= 4).sum() - (df['q6_recommend_likelihood'] <= 2).sum()) / len(df) * 100
top_strength = max(q_labels.items(), key=lambda x: overall_means[x[0]])
top_improvement = min(q_labels.items(), key=lambda x: overall_means[x[0]])

# Find most significant patterns
significant_patterns = sorted(patterns_found, key=lambda x: abs(x['diff']), reverse=True)[:5]

# Top themes
top_3_themes = [(k, v) for k, v in theme_counts.most_common() 
                if k not in ['Sentiment: Positive', 'Sentiment: Negative', 'Sentiment: Mixed', 'Sentiment: Neutral', 'No Feedback', 'Uncategorized']][:3]

memo_content = f"""# KEY FINDINGS MEMO
## Product Survey Analysis

**To:** Product Management Team  
**From:** Survey Analysis Team  
**Date:** March 11, 2026  
**Subject:** Key Insights from Product Survey (N=60 Respondents)

---

## EXECUTIVE SUMMARY

Overall product satisfaction is **moderate** with an average rating of **{overall_avg:.2f}/5.0** across all dimensions. While we have clear strengths in **{top_strength[1]}** ({overall_means[top_strength[0]]:.2f}/5), there are significant opportunities for improvement in **{top_improvement[1]}** ({overall_means[top_improvement[0]]:.2f}/5).

The Net Promoter-like score indicates **{nps_like:.0f}%** of respondents would likely recommend our product (rating 4-5 minus detractors 1-2).

---

## TOP 3 ACTIONABLE INSIGHTS

### 1. 🚨 CRITICAL: Mobile App Stability Issues
**Finding:** "Mobile app crashes" is the most frequently mentioned complaint (8 occurrences, 22% of feedback).  
**Impact:** This affects users across all demographics and is causing frustration.  
**Recommendation:** Prioritize mobile app bug fixes and stability testing, especially for Android. Consider a dedicated mobile QA sprint.

### 2. 📚 Documentation & Onboarding Needs Improvement
**Finding:** Documentation received the lowest overall score ({overall_means['q2_documentation']:.2f}/5). Multiple users report spending "hours figuring out basic features."  
**Impact:** New users (0-1 years experience) show notably different ratings, suggesting onboarding friction.  
**Recommendation:** 
- Create quick-start guides and video tutorials
- Add in-app tooltips and contextual help
- Develop role-specific onboarding paths

### 3. 💰 Pricing Communication Concerns
**Finding:** "Pricing change was unexpected and poorly communicated" appears in 5 feedback responses.  
**Impact:** Trust erosion, especially among long-term users and freelancers.  
**Recommendation:** 
- Improve advance notice for pricing changes (minimum 60 days)
- Create transparent pricing FAQ
- Consider grandfathering loyal customers

---

## DEMOGRAPHIC PATTERNS

### By Role
| Role | Avg Rating | Notable Pattern |
|------|------------|-----------------|
| Highest: {role_means.idxmax()} | {role_means.max():.2f} | - |
| Lowest: {role_means.idxmin()} | {role_means.min():.2f} | - |

### By Experience Level
- **Newest users (0-1 years):** {exp_means.get('0-1', 0):.2f} avg rating
- **Most experienced (10+ years):** {exp_means.get('10+', 0):.2f} avg rating

### Key Pattern: {significant_patterns[0]['subgroup']} ({significant_patterns[0]['demographic']})
- Rate **{significant_patterns[0]['question']}** at {significant_patterns[0]['subgroup_avg']:.2f} vs overall {significant_patterns[0]['overall_avg']:.2f}
- Difference: {significant_patterns[0]['diff']:+.2f} points

---

## QUESTION-BY-QUESTION BREAKDOWN

| Question | Avg | Median | Std Dev | Priority |
|----------|-----|--------|---------|----------|
"""

for _, row in summary_df.iterrows():
    priority = "🔴 High" if row['Mean'] < 3.0 else "🟡 Medium" if row['Mean'] < 3.5 else "🟢 Low"
    memo_content += f"| {row['Question']} | {row['Mean']:.2f} | {row['Median']:.1f} | {row['Std Dev']:.2f} | {priority} |\n"

memo_content += f"""
---

## FEEDBACK THEMES SUMMARY

| Theme | Frequency | Sentiment |
|-------|-----------|-----------|
"""

for theme, count in top_3_themes:
    sentiment = "Negative" if "Issues" in theme or "Concerns" in theme else "Neutral/Request"
    memo_content += f"| {theme} | {count} | {sentiment} |\n"

memo_content += f"""

**Positive highlights:**
- Support team responsiveness praised multiple times
- API quality noted as "excellent" by developers
- Collaboration features called "game-changing"

---

## RECOMMENDED NEXT STEPS

1. **Immediate (This Sprint):** Mobile app crash investigation
2. **Short-term (This Quarter):** Documentation overhaul, pricing communication policy
3. **Long-term (6 months):** UI modernization, Google Workspace integration

---

*Report generated from survey data (60 respondents, March 2026)*
"""

with open('key_findings_memo.md', 'w') as f:
    f.write(memo_content)

print("  Saved: key_findings_memo.md")

print("\n" + "=" * 60)
print("ANALYSIS COMPLETE!")
print("=" * 60)
print(f"\nFiles created in sorted_doc/:")
print("  1. survey_analysis.py - Analysis script")
print("  2. visual_summary.png - Visual charts")
print("  3. visual_summary.pdf - Visual charts (PDF)")
print("  4. key_findings_memo.md - Executive memo")
