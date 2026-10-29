# Fibonacci Number Calculator 🧮

## Overview
The **Fibonacci Number Calculator** is a Python project that calculates the nth number in the Fibonacci sequence using an iterative dynamic programming approach.

Each number in the sequence is calculated by adding the two preceding numbers, starting with `0` and `1`.

## Features
- Calculates the nth Fibonacci number.
- Uses an iterative approach instead of recursion.
- Stores previously calculated values in a list.
- Includes automated test cases using Python's `assert` statements.
- Tests multiple inputs, including small values and larger indices.

## Fibonacci Sequence
The Fibonacci sequence begins as follows:

```text
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
```

For example, the 10th Fibonacci number is `55`, using zero-based indexing.

## How It Works
1. Initializes a list with the first two Fibonacci numbers: `[0, 1]`.
2. Returns the corresponding value directly when `n` is less than `2`.
3. Iterates from index `2` to `n`.
4. Calculates each new number by adding the two previous numbers.
5. Appends each result to the sequence.
6. Returns the number at index `n`.

## Test Cases
The project includes tests for the following inputs:

| Input (`n`) | Expected Output |
|---:|---:|
| 0 | 0 |
| 1 | 1 |
| 2 | 1 |
| 3 | 2 |
| 5 | 5 |
| 10 | 55 |
| 15 | 610 |

The test suite uses `assert` statements to verify the results and prints a success message when each test passes.

## Concepts Practiced
- Python Functions
- Lists and Indexing
- Loops and Conditional Statements
- Dynamic Programming
- Algorithm Implementation
- Automated Testing with `assert`
- Time and Space Complexity Analysis

## Complexity Analysis
- **Time Complexity:** O(n), because the function calculates each Fibonacci number up to the requested index once.
- **Space Complexity:** O(n), because the list stores all calculated Fibonacci numbers.

## Technologies Used
- Python 3

## Learning Outcomes
This project demonstrates how dynamic programming can solve a problem efficiently by reusing previously calculated results. It also provides practice in algorithm design, sequence generation, and testing program correctness.

---

*Part of my Python practice projects, focused on strengthening programming fundamentals and algorithmic problem-solving skills.*
