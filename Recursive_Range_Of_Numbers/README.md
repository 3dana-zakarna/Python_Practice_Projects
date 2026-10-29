# Recursive Range of Numbers

## 📌 Project Overview

This project implements a recursive function in Python that generates a list of consecutive integers between a starting number and an ending number, including both endpoints.

Instead of using a loop, the function applies **recursion** to build the list by calling itself with an incremented starting number until it reaches the ending number.

## ✨ Features

- **Recursive Function:** Generates a sequence of integers using recursive calls.
- **Inclusive Range:** Includes both the starting and ending numbers.
- **Base Case:** Stops recursion when the starting number equals the ending number.
- **List Generation:** Returns the complete sequence as a Python list.
- **Negative Number Support:** Handles ranges containing negative numbers and zero.
- **Automated Tests:** Uses assertions to verify the function's behavior across different input ranges.

## 🛠️ Technologies Used

- Python
- Recursion
- Lists
- Functions
- Assertions and Testing

## 🧠 Concepts Demonstrated

- Recursive function calls
- Base cases and recursive cases
- Building lists recursively
- List insertion with `insert()`
- Handling positive, zero, and negative integers
- Testing function output with assertions

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Open a terminal in the project directory.
3. Run the Python file:

   ```bash
   python recursive_range.py
   ```

   Replace `recursive_range.py` with the actual name of your Python file if it differs.

## 🧪 Test Coverage

The built-in tests verify:

1. Generating a normal range of numbers
2. Handling identical start and end values
3. Generating a range containing two consecutive numbers
4. Handling ranges starting at zero
5. Supporting negative numbers
6. Returning a list
7. Printing sample function results

If all assertions pass, the program prints a message confirming that all tests passed.

## 📚 Learning Objective

The goal of this project is to understand recursion, identify base cases, build sequences through recursive calls, and test functions with different numerical inputs.

---

**Project Type:** Python Recursion Practice  
**Language:** Python
