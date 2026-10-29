# Medical Records Validator

## 📌 Project Overview

This project implements a **Medical Records Validation System** in Python to check the structure and data types of medical records and define validation rules for individual patient fields.

The system works with a collection of patient records containing identifiers, ages, genders, diagnoses, medications, and visit IDs. It uses Python's built-in data structures and regular expressions to support data validation.

## ✨ Features

- **Medical Records Dataset:** Stores sample patient records using dictionaries.
- **Patient ID Validation:** Checks patient identifiers against a regular expression pattern.
- **Age Validation:** Ensures that the age is an integer and at least 18.
- **Gender Validation:** Accepts `male` and `female`, regardless of capitalization.
- **Diagnosis Validation:** Allows diagnosis values to be strings or `None`.
- **Medication Validation:** Checks that medications are stored in a list containing strings.
- **Visit ID Validation:** Checks visit identifiers against a regular expression pattern.
- **Structure Validation:** Verifies that the input is a list or tuple containing dictionaries with the expected keys.
- **Error Messages:** Reports invalid input formats and record structures.

## 🛠️ Technologies Used

- Python
- Regular Expressions (`re`)
- Dictionaries and Lists
- Sets and Tuples
- Functions
- Data Validation

## 🧠 Concepts Demonstrated

- Input validation
- Data type checking with `isinstance()`
- Pattern matching with regular expressions
- Dictionary key validation
- Iterating through collections
- List comprehensions
- Boolean logic and conditional statements
- Handling structured data

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Open a terminal in the project directory.
3. Run the Python file:

   ```bash
   python medical_records_validator.py
   ```

   Replace `medical_records_validator.py` with the actual name of your Python file if it differs.

## 📋 Medical Record Fields

| Field | Validation Rule |
|---|---|
| `patient_id` | String matching a patient ID pattern such as `P1001` |
| `age` | Integer greater than or equal to 18 |
| `gender` | String containing `male` or `female` |
| `diagnosis` | String or `None` |
| `medications` | List containing only strings |
| `last_visit_id` | String matching a visit ID pattern such as `V2301` |

## 📚 Learning Objective

The goal of this project is to practice validating structured data, checking input formats, applying regular expressions, and building reusable validation functions in Python.

**Note:** This project is for programming practice and does not replace professional medical data validation or healthcare privacy and security requirements.

---

**Project Type:** Python Data Validation Practice  
**Language:** Python
