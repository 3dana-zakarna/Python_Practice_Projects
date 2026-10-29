# Generate Parentheses 🔢

## Overview
The **Generate Parentheses** project is a Python program that generates all valid combinations of parentheses for a given number of pairs.

It uses a **Breadth-First Search (BFS)** approach to build combinations incrementally while ensuring that every generated sequence follows the rules for valid parentheses.

## Features
- Generates all valid combinations of parentheses for a specified number of pairs.
- Uses a queue-based BFS algorithm.
- Ensures that closing parentheses never exceed opening parentheses.
- Validates input types and values.
- Handles invalid inputs, including negative numbers, floats, strings, and Boolean values.
- Includes automated test cases for different input scenarios.

## How It Works
1. Initializes a queue with an empty string and counters for opening and closing parentheses.
2. Removes the next state from the front of the queue.
3. Adds an opening parenthesis if fewer than the required number have been used.
4. Adds a closing parenthesis only when it will keep the sequence valid.
5. Continues until each sequence contains exactly twice the requested number of characters.
6. Collects and returns all valid combinations.

## Example
```python
gen_parentheses(3)
```

Expected output:

```python
["((()))", "(()())", "(())()", "()(())", "()()()"]
```

For two pairs, the function generates:

```python
["(())", "()()"]
```

## Input Validation
The function checks that:
- The input is an integer.
- Boolean values are rejected even though `bool` is a subclass of `int` in Python.
- The number of pairs is at least `1`.

Invalid inputs return descriptive error messages.

## Test Cases
The project includes tests for:
- One pair of parentheses.
- Two pairs of parentheses.
- Three pairs of parentheses.
- Zero and negative values.
- Floating-point and string inputs.
- Boolean input.

The tests use Python's `assert` statements to verify the expected results.

## Concepts Practiced
- Breadth-First Search (BFS)
- Queue-Based Algorithms
- Combinatorial Generation
- Strings and Tuples
- Lists and State Tracking
- Conditional Logic
- Input Validation
- Automated Testing

## Complexity Analysis
The number of valid combinations is given by the Catalan numbers. For `n` pairs, the number of combinations grows approximately as \(4^n / (n^{3/2}\sqrt{\pi})\).

The algorithm stores intermediate states in a queue and generates valid combinations incrementally. Its time and space requirements grow rapidly as the number of pairs increases.

## Technologies Used
- Python 3

## Learning Outcomes
This project demonstrates how BFS can systematically explore possible states while enforcing constraints. It also provides practice with queue operations, combinatorial problems, algorithm design, and input validation.

---

*Part of my Python practice projects, focused on algorithms, data structures, and problem-solving.*
