# Square Root Calculator Using Bisection Method 🧮

## Overview
The **Square Root Bisection Calculator** is a Python project that approximates the square root of a non-negative number using the **Bisection Method**.

Instead of relying on Python's built-in square root functions, the program repeatedly narrows an interval until it reaches the required tolerance or the maximum number of iterations.

## Features
- Calculates approximate square roots using the Bisection Method.
- Supports integer and decimal inputs.
- Allows users to specify a tolerance level.
- Limits the number of iterations to avoid endless calculations.
- Handles zero and one as special cases.
- Raises a `ValueError` for negative inputs.
- Includes test cases for different inputs, precision levels, and convergence behavior.

## How It Works
1. Checks whether the target number is negative.
2. Returns the number directly if the target is `0` or `1`.
3. Initializes the lower and upper bounds of the search interval.
4. Calculates the midpoint of the interval.
5. Compares the square of the midpoint with the target:
   - If the midpoint's square is too small, the lower bound is updated.
   - Otherwise, the upper bound is updated.
6. Repeats the process until the interval width meets the tolerance.
7. Returns the approximate square root or `None` if the algorithm fails to converge within the iteration limit.

## Example
```python
square_root_bisection(81)
```

Expected result: approximately `9`.

Another example:

```python
square_root_bisection(0.25, tolerance=1e-7, max_iterations=50)
```

Expected result: approximately `0.5`.

## Test Cases
The project includes tests for:

- Square roots of `0` and `1`.
- Small decimal values.
- The square root of `0.25`.
- Perfect squares such as `81` and `225`.
- Different tolerance levels.
- Negative inputs and `ValueError` handling.
- Failure to converge within a limited number of iterations.

The tests use Python's `assert` statements to verify the results.

## Concepts Practiced
- Numerical Methods
- Bisection Algorithm
- Iterative Algorithms
- Conditional Statements and Loops
- Floating-Point Arithmetic
- Error Handling with `ValueError`
- Tolerance and Numerical Precision
- Automated Testing

## Complexity Analysis
- **Time Complexity:** O(k), where `k` is the number of iterations performed.
- **Space Complexity:** O(1), because the algorithm uses a constant amount of additional memory.

## Technologies Used
- Python 3

## Learning Outcomes
This project demonstrates how numerical algorithms can approximate mathematical solutions without relying on built-in square root functions. It also provides practical experience with convergence, precision, error handling, and testing numerical computations.

---

*Part of my Python practice projects, focused on algorithms, numerical computing, and problem-solving.*
