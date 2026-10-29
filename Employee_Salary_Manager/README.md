# Employee Salary Manager

## 📌 Project Overview

This project implements an **Employee Management System** in Python using Object-Oriented Programming (OOP).

The `Employee` class manages employee information, including names, career levels, and salaries. It uses properties and setter methods to validate attribute updates, enforce salary requirements, and control promotions through predefined career levels.

## ✨ Features

- **Employee Class:** Represents employees with names, career levels, and salaries.
- **Predefined Salary Structure:** Assigns base salaries according to employee levels.
- **Name Validation:** Ensures employee names are strings.
- **Career Level Validation:** Accepts only predefined levels: trainee, junior, mid-level, and senior.
- **Promotion System:** Allows employees to advance to higher levels while preventing demotions.
- **Salary Validation:** Ensures salaries are numeric and meet the minimum salary for the employee's current level.
- **Property-Based Access:** Uses getters and setters to control access to employee attributes.
- **Readable Object Representation:** Implements `__str__()` and `__repr__()` for displaying employee information.

## 🛠️ Technologies Used

- Python
- Object-Oriented Programming (OOP)
- Properties and Setters
- Dictionaries
- Exception Handling
- String Formatting

## 🧠 Concepts Demonstrated

- Classes and objects
- Class attributes and instance attributes
- Encapsulation
- The `@property` decorator
- Attribute validation
- Type checking with `isinstance()`
- Raising `TypeError` and `ValueError`
- Object string representations
- Business rules and promotion logic

## 💰 Career Levels and Base Salaries

| Career Level | Base Salary |
|---|---:|
| Trainee | $1,000 |
| Junior | $2,000 |
| Mid-level | $3,000 |
| Senior | $4,000 |

The salary structure is stored in a class-level dictionary, allowing the class to use a predefined minimum salary for each career level.

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Open a terminal in the project directory.
3. Run the Python file:

   ```bash
   python employee_salary.py
   ```

   Replace `employee_salary.py` with the actual name of your Python file if it differs.

## 🧪 Example Scenario

The program:

1. Creates an employee named Charlie Brown at the trainee level.
2. Displays the employee's information.
3. Prints the employee's base salary.
4. Promotes the employee to the junior level.

The program also prints messages when employee attributes or salary values are updated.

## 📚 Learning Objective

The goal of this project is to practice encapsulation, property-based validation, class attributes, and controlled state changes while modeling a simple employee salary and promotion system.

---

**Project Type:** Python OOP Practice  
**Language:** Python
