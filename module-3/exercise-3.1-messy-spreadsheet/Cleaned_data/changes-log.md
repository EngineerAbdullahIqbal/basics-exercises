# Data Cleaning Changes Log

**Source File:** `customer_data_messy.csv`

**Output File:** `customer_data_clean.csv`

**Original Rows:** 25
**Clean Rows:** 22
**Duplicates Removed:** 3

---

## Summary of Changes

| Change Type | Count |
|---------------|-------|
| Name capitalization | 12 |
| Date standardization | 18 |
| Phone formatting | 15 |
| City capitalization | 3 |
| Duplicates removed | 3 |
| Rows flagged (missing critical info) | 2 |

---

## Detailed Changes by Row

### Row 1

**Original Data**:
- First Name: `john`
- Last Name: `smith`
- Email: `john.smith@email.com`
- Phone: `(555) 123-4567`
- Date Joined: `01/15/2024`
- City: `New York`
- Plan: `pro`
- Monthly Spend: `49.99`

**Changes Made**:
- First Name: 'john' → 'John'
- Last Name: 'smith' → 'Smith'
- Date Joined: '01/15/2024' → '2024-01-15'

---

### Row 2

**Original Data**:
- First Name: `JANE`
- Last Name: `DOE`
- Email: `jane.doe@email.com`
- Phone: `555.234.5678`
- Date Joined: `Jan 20, 2024`
- City: `los angeles`
- Plan: `free`
- Monthly Spend: `0`

**Changes Made**:
- First Name: 'JANE' → 'Jane'
- Last Name: 'DOE' → 'Doe'
- Date Joined: 'Jan 20, 2024' → '2024-01-20'
- Phone: '555.234.5678' → '(555) 234-5678'
- City: 'los angeles' → 'Los Angeles'

---

### Row 3

**Original Data**:
- First Name: `Bob`
- Last Name: `Jones`
- Email: `bob.jones@email.com`
- Phone: `+1-555-345-6789`
- Date Joined: `2024-01-25`
- City: `Chicago`
- Plan: `pro`
- Monthly Spend: `49.99`

**Changes Made**:
- Phone: '+1-555-345-6789' → '(555) 345-6789'

---

### Row 4

**Original Data**:
- First Name: `alice`
- Last Name: `WILLIAMS`
- Email: `alice.w@email.com`
- Phone: `5554567890`
- Date Joined: `February 1, 2024`
- City: `Houston`
- Plan: `enterprise`
- Monthly Spend: `199.99`

**Changes Made**:
- First Name: 'alice' → 'Alice'
- Last Name: 'WILLIAMS' → 'Williams'
- Date Joined: 'February 1, 2024' → '2024-02-01'
- Phone: '5554567890' → '(555) 456-7890'

---

### Row 5

**Status:** ⛔ DUPLICATE REMOVED

**Original Data**:
- First Name: `John`
- Last Name: `Smith`
- Email: `john.smith@email.com`
- Phone: `(555) 123-4567`
- Date Joined: `01/15/2024`
- City: `New York`
- Plan: `pro`
- Monthly Spend: `49.99`

**Changes Made**:
- Date Joined: '01/15/2024' → '2024-01-15'
- DUPLICATE REMOVED

---

### Row 6

**Original Data**:
- First Name: `Charlie`
- Last Name: `Brown`
- Email: `charlie.b@email.com`
- Phone: ``
- Date Joined: `2024-02-10`
- City: `Phoenix`
- Plan: `pro`
- Monthly Spend: `49.99`

**Changes Made**:
- ⚠️ Note: Phone missing

---

### Row 7

**Original Data**:
- First Name: `DIANA`
- Last Name: `prince`
- Email: `diana.p@email.com`
- Phone: `555 678 9012`
- Date Joined: `Feb 15 2024`
- City: ``
- Plan: `free`
- Monthly Spend: `0`

**Changes Made**:
- First Name: 'DIANA' → 'Diana'
- Last Name: 'prince' → 'Prince'
- Date Joined: 'Feb 15 2024' → '2024-02-15'
- Phone: '555 678 9012' → '(555) 678-9012'

---

### Row 8

**Original Data**:
- First Name: `edward`
- Last Name: `Norton`
- Email: `edward.n@email.com`
- Phone: `(555)789-0123`
- Date Joined: `02/20/2024`
- City: `San Antonio`
- Plan: `pro`
- Monthly Spend: `49.99`

**Changes Made**:
- First Name: 'edward' → 'Edward'
- Date Joined: '02/20/2024' → '2024-02-20'
- Phone: '(555)789-0123' → '(555) 789-0123'

---

### Row 10

**Original Data**:
- First Name: `George`
- Last Name: ``
- Email: `george@email.com`
- Phone: `555-890-1234`
- Date Joined: `March 5, 2024`
- City: `Dallas`
- Plan: `free`
- Monthly Spend: ``

**Changes Made**:
- Date Joined: 'March 5, 2024' → '2024-03-05'
- Phone: '555-890-1234' → '(555) 890-1234'

---

### Row 11

**Original Data**:
- First Name: `hannah`
- Last Name: `Lee`
- Email: ``
- Phone: `555.901.2345`
- Date Joined: `03/10/2024`
- City: `San Jose`
- Plan: `pro`
- Monthly Spend: `49.99`

**Changes Made**:
- First Name: 'hannah' → 'Hannah'
- Date Joined: '03/10/2024' → '2024-03-10'
- Phone: '555.901.2345' → '(555) 901-2345'
- ⚠️ FLAGGED: Email missing

---

### Row 12

**Original Data**:
- First Name: `IVAN`
- Last Name: `PETROV`
- Email: `ivan.p@email.com`
- Phone: `+7-555-012-3456`
- Date Joined: `2024-3-15`
- City: `Moscow`
- Plan: `pro`
- Monthly Spend: `49.99`

**Changes Made**:
- First Name: 'IVAN' → 'Ivan'
- Last Name: 'PETROV' → 'Petrov'
- Date Joined: '2024-3-15' → '2024-03-15'

---

### Row 13

**Status:** ⛔ DUPLICATE REMOVED

**Original Data**:
- First Name: `jane`
- Last Name: `doe`
- Email: `jane.doe@email.com`
- Phone: `555.234.5678`
- Date Joined: `Jan 20, 2024`
- City: `Los Angeles`
- Plan: `free`
- Monthly Spend: `0`

**Changes Made**:
- First Name: 'jane' → 'Jane'
- Last Name: 'doe' → 'Doe'
- Date Joined: 'Jan 20, 2024' → '2024-01-20'
- Phone: '555.234.5678' → '(555) 234-5678'
- DUPLICATE REMOVED

---

### Row 14

**Original Data**:
- First Name: `Kevin`
- Last Name: `Park`
- Email: `kevin.p@email.com`
- Phone: `(555) 123 4567`
- Date Joined: `03/25/2024`
- City: `Austin`
- Plan: `enterprise`
- Monthly Spend: `199.99`

**Changes Made**:
- Date Joined: '03/25/2024' → '2024-03-25'
- Phone: '(555) 123 4567' → '(555) 123-4567'

---

### Row 15

**Original Data**:
- First Name: `Luna`
- Last Name: `Garcia`
- Email: `luna.g@email.com`
- Phone: ``
- Date Joined: `April 1, 2024`
- City: ``
- Plan: `pro`
- Monthly Spend: `49.99`

**Changes Made**:
- Date Joined: 'April 1, 2024' → '2024-04-01'
- ⚠️ Note: Phone missing

---

### Row 16

**Original Data**:
- First Name: `Mike`
- Last Name: `Johnson`
- Email: `mike.j@email.com`
- Phone: `555-234-5678`
- Date Joined: `2024-04-05`
- City: `Seattle`
- Plan: `free`
- Monthly Spend: `0`

**Changes Made**:
- Phone: '555-234-5678' → '(555) 234-5678'

---

### Row 17

**Original Data**:
- First Name: `nina`
- Last Name: `WILLIAMS`
- Email: `nina.w@email.com`
- Phone: `(555)345-6789`
- Date Joined: `04/10/2024`
- City: `denver`
- Plan: `pro`
- Monthly Spend: ``

**Changes Made**:
- First Name: 'nina' → 'Nina'
- Last Name: 'WILLIAMS' → 'Williams'
- Date Joined: '04/10/2024' → '2024-04-10'
- Phone: '(555)345-6789' → '(555) 345-6789'
- City: 'denver' → 'Denver'

---

### Row 18

**Original Data**:
- First Name: `Oscar`
- Last Name: `Martinez`
- Email: `oscar.m@email.com`
- Phone: `+1 555 456 7890`
- Date Joined: `2024-04-15`
- City: `Portland`
- Plan: `enterprise`
- Monthly Spend: `199.99`

**Changes Made**:
- Phone: '+1 555 456 7890' → '(555) 456-7890'

---

### Row 19

**Status:** ⛔ DUPLICATE REMOVED

**Original Data**:
- First Name: `bob`
- Last Name: `jones`
- Email: `bob.jones@email.com`
- Phone: `+1-555-345-6789`
- Date Joined: `2024-01-25`
- City: `chicago`
- Plan: `pro`
- Monthly Spend: `49.99`

**Changes Made**:
- First Name: 'bob' → 'Bob'
- Last Name: 'jones' → 'Jones'
- Phone: '+1-555-345-6789' → '(555) 345-6789'
- City: 'chicago' → 'Chicago'
- DUPLICATE REMOVED

---

### Row 20

**Original Data**:
- First Name: `Priya`
- Last Name: `Sharma`
- Email: `priya.s@email.com`
- Phone: `+91-555-567-8901`
- Date Joined: `April 20 2024`
- City: `Mumbai`
- Plan: `pro`
- Monthly Spend: `49.99`

**Changes Made**:
- Date Joined: 'April 20 2024' → '2024-04-20'

---

### Row 21

**Original Data**:
- First Name: `Quinn`
- Last Name: `O'Brien`
- Email: `quinn.ob@email.com`
- Phone: `5556789012`
- Date Joined: `2024-05-01`
- City: `Boston`
- Plan: ``
- Monthly Spend: `49.99`

**Changes Made**:
- Phone: '5556789012' → '(555) 678-9012'
- ⚠️ FLAGGED: Plan missing

---

### Row 22

**Original Data**:
- First Name: `Rachel`
- Last Name: `Kim`
- Email: `rachel.k@email.com`
- Phone: `(555) 789-0123`
- Date Joined: `05/05/2024`
- City: `Atlanta`
- Plan: `pro`
- Monthly Spend: `49.99`

**Changes Made**:
- Date Joined: '05/05/2024' → '2024-05-05'

---

### Row 23

**Original Data**:
- First Name: `SAM`
- Last Name: `taylor`
- Email: `sam.t@email.com`
- Phone: ``
- Date Joined: `May 10, 2024`
- City: `Miami`
- Plan: `free`
- Monthly Spend: `0`

**Changes Made**:
- First Name: 'SAM' → 'Sam'
- Last Name: 'taylor' → 'Taylor'
- Date Joined: 'May 10, 2024' → '2024-05-10'
- ⚠️ Note: Phone missing

---

### Row 24

**Original Data**:
- First Name: `Tara`
- Last Name: `Singh`
- Email: `tara.s@email.com`
- Phone: `+91-555-890-1234`
- Date Joined: `2024-5-15`
- City: `Delhi`
- Plan: `enterprise`
- Monthly Spend: `199.99`

**Changes Made**:
- Date Joined: '2024-5-15' → '2024-05-15'

---

### Row 25

**Original Data**:
- First Name: `uma`
- Last Name: `CHEN`
- Email: `uma.c@email.com`
- Phone: `555 901 2345`
- Date Joined: `05/20/2024`
- City: ``
- Plan: `pro`
- Monthly Spend: `49.99`

**Changes Made**:
- First Name: 'uma' → 'Uma'
- Last Name: 'CHEN' → 'Chen'
- Date Joined: '05/20/2024' → '2024-05-20'
- Phone: '555 901 2345' → '(555) 901-2345'

---

## Rows with Missing Critical Information

These rows were retained but flagged for review:

| Row ID | Missing Field(s) |
|--------|------------------|
| 11 | Email missing |
| 21 | Plan missing |
