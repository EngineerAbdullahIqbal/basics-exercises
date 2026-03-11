# Exercise 3.1: The Messy Spreadsheet

## Learning Objective

This exercise teaches **data cleaning fundamentals**—a critical skill for anyone working with real-world data. You'll learn to identify, document, and fix common data quality issues while maintaining an audit trail.

---

## 📁 Files

| File | Description |
|------|-------------|
| `customer_data_messy.csv` | Original dataset with 25 rows of messy customer data |
| `customer_data_clean.csv` | Cleaned output (22 rows after deduplication) |
| `changes-log.md` | Detailed audit trail of every transformation |
| `clean_data.py` | Python script that performs the cleaning |
| `README.md` | This file—learning guide and implementation reference |

---

## 🚨 Common Data Quality Issues

Real-world data is **never** clean. Here are the issues you'll encounter:

### 1. Inconsistent Date Formats
```
❌ 01/15/2024      (MM/DD/YYYY)
❌ Jan 20, 2024    (Month DD, YYYY)
❌ February 1, 2024 (Full month name)
❌ Feb 15 2024     (No comma)
❌ 2024-3-15       (Single-digit month)
✅ 2024-01-15      (ISO 8601 standard)
```

**Why it matters:** Date parsing errors, sorting issues, and filtering bugs.

---

### 2. Inconsistent Name Casing
```
❌ john smith      (all lowercase)
❌ JANE DOE        (all uppercase)
❌ Bob JONES       (mixed)
✅ John Smith      (title case)
```

**Why it matters:** Duplicate detection fails, reports look unprofessional.

---

### 3. Phone Number Variations
```
❌ (555) 123-4567
❌ 555.234.5678
❌ 5554567890
❌ +1-555-345-6789
❌ 555 678 9012
✅ (555) 234-5678  (standardized US format)
✅ +92-300-1234567 (international preserved)
```

**Why it matters:** Validation fails, duplicate customers appear different.

---

### 4. Missing Values
```
❌ (empty email field)
❌ (empty city field)
❌ (empty plan field)
```

**Why it matters:** Analytics break, marketing campaigns fail, revenue tracking incomplete.

---

### 5. Duplicate Records
```
Row 1: John Smith, john.smith@email.com, 2024-01-15
Row 5: John Smith, john.smith@email.com, 2024-01-15  ← Exact duplicate!
```

**Why it matters:** Inflated metrics, double-counting revenue, confused customers.

---

## 🔧 Implementation Guide

### Step 1: Read the Data

```python
import csv

with open("customer_data_messy.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["First Name"], row["Last Name"])
```

---

### Step 2: Define Transformation Functions

```python
from datetime import datetime
import re

def parse_date(date_str):
    """Convert various date formats to YYYY-MM-DD."""
    date_str = date_str.strip().strip('"')
    
    formats = [
        "%Y-%m-%d",      # 2024-01-25
        "%m/%d/%Y",      # 01/15/2024
        "%b %d, %Y",     # Jan 20, 2024
        "%B %d, %Y",     # February 1, 2024
        "%b %d %Y",      # Feb 15 2024
    ]
    
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue
    
    return date_str  # Return as-is if unparseable


def title_case(name):
    """Convert name to Title Case."""
    return name.strip().title() if name else ""


def format_phone(phone_str):
    """Standardize US phone numbers to (XXX) XXX-XXXX."""
    phone_str = phone_str.strip()
    if not phone_str:
        return ""
    
    # Keep international numbers
    if phone_str.startswith("+") and not phone_str.startswith("+1"):
        return re.sub(r"\s+", "-", phone_str)
    
    # Extract digits only
    digits = re.sub(r"\D", "", phone_str)
    
    # Handle 10-digit US numbers
    if len(digits) == 11 and digits.startswith("1"):
        digits = digits[1:]
    if len(digits) == 10:
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    
    return phone_str
```

---

### Step 3: Detect Duplicates

```python
seen = set()
duplicates = []

for row in rows:
    # Create a unique key from identifying fields
    dup_key = (
        row["First Name"].lower(),
        row["Last Name"].lower(),
        row["Email"].lower(),
        row["Phone"],
        row["Date Joined"]
    )
    
    if dup_key in seen:
        duplicates.append(row["ID"])
    else:
        seen.add(dup_key)

print(f"Duplicate rows: {duplicates}")
```

---

### Step 4: Flag Missing Critical Data

```python
def check_missing(row):
    """Return list of missing critical fields."""
    missing = []
    
    if not row["Email"].strip():
        missing.append("Email")
    if not row["Plan"].strip():
        missing.append("Plan")
    
    return missing

# Usage
for row in rows:
    missing = check_missing(row)
    if missing:
        print(f"Row {row['ID']}: Missing {', '.join(missing)}")
```

---

### Step 5: Log Every Change

```python
changes_log = []

def log_change(row_id, field, old_value, new_value):
    changes_log.append({
        "row": row_id,
        "field": field,
        "before": old_value,
        "after": new_value
    })

# Example usage
old_name = row["First Name"]
row["First Name"] = title_case(old_name)
if old_name != row["First Name"]:
    log_change(row["ID"], "First Name", old_name, row["First Name"])
```

---

### Step 6: Write Clean Output

```python
fieldnames = ["ID", "First Name", "Last Name", "Email", "Phone", 
              "Date Joined", "City", "Plan", "Monthly Spend"]

with open("customer_data_clean.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    
    for i, row in enumerate(clean_rows, start=1):
        row["ID"] = i  # Renumber sequentially
        writer.writerow(row)
```

---

## 📊 Before & After Comparison

### Before (Messy)
```csv
ID,First Name,Last Name,Email,Phone,Date Joined,City,Plan,Monthly Spend
1,john,smith,john.smith@email.com,(555) 123-4567,01/15/2024,New York,pro,49.99
2,JANE,DOE,jane.doe@email.com,555.234.5678,"Jan 20, 2024",los angeles,free,0
```

### After (Clean)
```csv
ID,First Name,Last Name,Email,Phone,Date Joined,City,Plan,Monthly Spend
1,John,Smith,john.smith@email.com,(555) 123-4567,2024-01-15,New York,pro,49.99
2,Jane,Doe,jane.doe@email.com,(555) 234-5678,2024-01-20,Los Angeles,free,0
```

---

## 🎯 Key Takeaways

1. **Always preview before changing** — Document issues before applying fixes
2. **Keep an audit trail** — Log every transformation for accountability
3. **Standardize early** — Consistent formats prevent downstream bugs
4. **Flag, don't delete** — Mark missing data instead of removing rows
5. **Test incrementally** — Verify each transformation step

---

## 🛠️ Extend This Exercise

Try these challenges to deepen your understanding:

| Challenge | Difficulty |
|-----------|------------|
| Add email validation (check @ symbol, domain) | ⭐ Easy |
| Detect near-duplicates (same name, different email) | ⭐⭐ Medium |
| Impute missing cities based on phone area code | ⭐⭐⭐ Hard |
| Export to multiple formats (JSON, Excel, Parquet) | ⭐⭐ Medium |
| Add unit tests for each transformation function | ⭐⭐ Medium |

---

## 📚 Further Reading

- [Data Cleaning Best Practices](https://en.wikipedia.org/wiki/Data_cleansing)
- [Python CSV Module Documentation](https://docs.python.org/3/library/csv.html)
- [ISO 8601 Date Standard](https://en.wikipedia.org/wiki/ISO_8601)
- [Pandas for Data Cleaning](https://pandas.pydata.org/docs/user_guide/cleaning.html)

---

## ✅ Checklist for Data Cleaning Projects

- [ ] Read and inspect raw data
- [ ] Document all issues found
- [ ] Get approval before making changes
- [ ] Write transformation functions
- [ ] Detect and remove duplicates
- [ ] Flag missing critical values
- [ ] Log every change made
- [ ] Export clean dataset
- [ ] Export changes log
- [ ] Verify output integrity

---

**Exercise Source:** Digital FTEs Program — Module 3: Data Fundamentals
