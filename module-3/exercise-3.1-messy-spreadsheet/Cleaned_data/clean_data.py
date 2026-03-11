#!/usr/bin/env python3
"""Clean customer_data_messy.csv and generate changes log."""

import csv
import re
from datetime import datetime

INPUT_FILE = "customer_data_messy.csv"
OUTPUT_FILE = "customer_data_clean.csv"
CHANGES_LOG = "changes-log.md"

changes = []

def parse_date(date_str):
    """Parse various date formats and return YYYY-MM-DD."""
    date_str = date_str.strip().strip('"')
    if not date_str:
        return ""
    
    # Try various formats
    formats = [
        ("%Y-%m-%d", None),           # 2024-01-25, 2024-3-15
        ("%m/%d/%Y", None),           # 01/15/2024
        ("%b %d, %Y", None),          # Jan 20, 2024
        ("%B %d, %Y", None),          # February 1, 2024
        ("%b %d %Y", None),           # Feb 15 2024
        ("%B %d %Y", None),           # April 20 2024
    ]
    
    for fmt, _ in formats:
        try:
            dt = datetime.strptime(date_str, fmt)
            return dt.strftime("%Y-%m-%d")
        except ValueError:
            continue
    
    # Handle formats with single-digit month/day like 2024-3-15
    match = re.match(r"(\d{4})-(\d{1,2})-(\d{1,2})", date_str)
    if match:
        year, month, day = match.groups()
        return f"{year}-{int(month):02d}-{int(day):02d}"
    
    return date_str  # Return as-is if can't parse

def format_phone(phone_str):
    """Standardize phone numbers to (XXX) XXX-XXXX for US numbers."""
    phone_str = phone_str.strip()
    if not phone_str:
        return ""
    
    # Keep international numbers with country code
    if phone_str.startswith("+") and not phone_str.startswith("+1"):
        # International non-US: normalize dashes
        return re.sub(r"\s+", "-", phone_str)
    
    # Extract digits only
    digits = re.sub(r"\D", "", phone_str)
    
    # Handle US numbers (10 or 11 digits starting with 1)
    if len(digits) == 11 and digits.startswith("1"):
        digits = digits[1:]
    if len(digits) == 10:
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    
    return phone_str  # Return as-is if can't format

def title_case(name):
    """Convert name to title case."""
    if not name:
        return ""
    return name.strip().title()

def format_city(city):
    """Format city name to title case."""
    if not city:
        return ""
    return city.strip().title()

def main():
    rows = []
    seen_duplicates = set()
    
    with open(INPUT_FILE, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row_num, row in enumerate(reader, start=2):  # Start at 2 (header is row 1)
            original_row = row.copy()
            row_id = row["ID"]
            
            # Track changes for this row
            row_changes = []
            
            # 1. Standardize names (title case)
            old_first = row["First Name"]
            old_last = row["Last Name"]
            row["First Name"] = title_case(old_first)
            row["Last Name"] = title_case(old_last)
            
            if old_first != row["First Name"]:
                row_changes.append(f"First Name: '{old_first}' → '{row['First Name']}'")
            if old_last != row["Last Name"]:
                row_changes.append(f"Last Name: '{old_last}' → '{row['Last Name']}'")
            
            # 2. Standardize date
            old_date = row["Date Joined"]
            row["Date Joined"] = parse_date(old_date)
            if old_date != row["Date Joined"]:
                row_changes.append(f"Date Joined: '{old_date}' → '{row['Date Joined']}'")
            
            # 3. Format phone
            old_phone = row["Phone"]
            row["Phone"] = format_phone(old_phone)
            if old_phone != row["Phone"]:
                row_changes.append(f"Phone: '{old_phone}' → '{row['Phone']}'")
            
            # 4. Format city
            old_city = row["City"]
            row["City"] = format_city(old_city)
            if old_city != row["City"]:
                row_changes.append(f"City: '{old_city}' → '{row['City']}'")
            
            # 5. Check for duplicates (based on First Name, Last Name, Email, Phone, Date Joined)
            dup_key = (row["First Name"].lower(), row["Last Name"].lower(), 
                       row["Email"].lower(), row["Phone"], row["Date Joined"])
            
            is_duplicate = False
            if dup_key in seen_duplicates:
                is_duplicate = True
                row_changes.append("DUPLICATE REMOVED")
            else:
                seen_duplicates.add(dup_key)
            
            # 6. Flag missing critical info
            missing_flags = []
            if not row["Email"].strip():
                missing_flags.append("Email missing")
            if not row["Plan"].strip():
                missing_flags.append("Plan missing")
            
            if missing_flags:
                row_changes.append("⚠️ FLAGGED: " + ", ".join(missing_flags))
            
            # Also flag missing phone (non-critical but noted)
            if not row["Phone"].strip() and "⚠️ FLAGGED" not in str(row_changes):
                row_changes.append("⚠️ Note: Phone missing")
            
            if row_changes:
                changes.append({
                    "row": row_id,
                    "original": original_row,
                    "changes": row_changes,
                    "is_duplicate": is_duplicate
                })
            
            if not is_duplicate:
                rows.append(row)
    
    # Write clean CSV
    fieldnames = ["ID", "First Name", "Last Name", "Email", "Phone", "Date Joined", "City", "Plan", "Monthly Spend"]
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for i, row in enumerate(rows, start=1):
            row["ID"] = i  # Renumber IDs
            writer.writerow(row)
    
    # Write changes log
    with open(CHANGES_LOG, "w", encoding="utf-8") as f:
        f.write("# Data Cleaning Changes Log\n\n")
        f.write(f"**Source File:** `{INPUT_FILE}`\n\n")
        f.write(f"**Output File:** `{OUTPUT_FILE}`\n\n")
        f.write(f"**Original Rows:** 25\n")
        f.write(f"**Clean Rows:** {len(rows)}\n")
        f.write(f"**Duplicates Removed:** {25 - len(rows)}\n\n")
        
        f.write("---\n\n")
        f.write("## Summary of Changes\n\n")
        
        # Count change types
        date_changes = sum(1 for c in changes if any("Date Joined" in ch for ch in c["changes"]))
        name_changes = sum(1 for c in changes if any("First Name" in ch or "Last Name" in ch for ch in c["changes"]))
        phone_changes = sum(1 for c in changes if any("Phone:" in ch for ch in c["changes"]))
        city_changes = sum(1 for c in changes if any("City:" in ch for ch in c["changes"]))
        duplicates = sum(1 for c in changes if c["is_duplicate"])
        flagged = sum(1 for c in changes if any("⚠️ FLAGGED" in ch for ch in c["changes"]))
        
        f.write(f"| Change Type | Count |\n")
        f.write(f"|---------------|-------|\n")
        f.write(f"| Name capitalization | {name_changes} |\n")
        f.write(f"| Date standardization | {date_changes} |\n")
        f.write(f"| Phone formatting | {phone_changes} |\n")
        f.write(f"| City capitalization | {city_changes} |\n")
        f.write(f"| Duplicates removed | {duplicates} |\n")
        f.write(f"| Rows flagged (missing critical info) | {flagged} |\n\n")
        
        f.write("---\n\n")
        f.write("## Detailed Changes by Row\n\n")
        
        for change in changes:
            f.write(f"### Row {change['row']}\n\n")
            if change["is_duplicate"]:
                f.write("**Status:** ⛔ DUPLICATE REMOVED\n\n")
            f.write("**Original Data**:\n")
            f.write(f"- First Name: `{change['original']['First Name']}`\n")
            f.write(f"- Last Name: `{change['original']['Last Name']}`\n")
            f.write(f"- Email: `{change['original']['Email']}`\n")
            f.write(f"- Phone: `{change['original']['Phone']}`\n")
            f.write(f"- Date Joined: `{change['original']['Date Joined']}`\n")
            f.write(f"- City: `{change['original']['City']}`\n")
            f.write(f"- Plan: `{change['original']['Plan']}`\n")
            f.write(f"- Monthly Spend: `{change['original']['Monthly Spend']}`\n\n")
            
            f.write("**Changes Made**:\n")
            for ch in change["changes"]:
                f.write(f"- {ch}\n")
            f.write("\n---\n\n")
        
        f.write("## Rows with Missing Critical Information\n\n")
        f.write("These rows were retained but flagged for review:\n\n")
        f.write("| Row ID | Missing Field(s) |\n")
        f.write("|--------|------------------|\n")
        for change in changes:
            for ch in change["changes"]:
                if "⚠️ FLAGGED" in ch:
                    fields = ch.replace("⚠️ FLAGGED: ", "")
                    f.write(f"| {change['row']} | {fields} |\n")
                    break
    
    print(f"✓ Clean data written to: {OUTPUT_FILE}")
    print(f"✓ Changes log written to: {CHANGES_LOG}")
    print(f"✓ Total rows cleaned: {len(rows)}")
    print(f"✓ Duplicates removed: {25 - len(rows)}")

if __name__ == "__main__":
    main()
