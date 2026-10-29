# Tower of Hanoi Solver

## 📌 Project Overview

This project implements a recursive solution to the **Tower of Hanoi puzzle** using Python.

The Tower of Hanoi is a classic mathematical puzzle consisting of three rods and a stack of disks of different sizes. The objective is to move all disks from the source rod to the target rod while following a set of rules.

The program simulates the disk movements and records the state of all three rods after each move.

## ⚙️ How It Works

The `hanoi_solver(n)` function:

1. Initializes three rods, placing all disks on the source rod in descending order.
2. Creates a list to store the states of the rods throughout the solution.
3. Uses a recursive helper function named `solve()` to move the disks.
4. Moves one disk directly when the base case is reached.
5. Recursively moves smaller disks to the auxiliary rod, transfers the largest remaining disk, and then moves the smaller disks onto the target rod.
6. Returns all recorded rod states as a single string, with each state on a separate line.

## 📏 Rules of the Puzzle

The solution follows three fundamental rules:

- Only one disk can be moved at a time.
- Only the top disk of a rod can be moved.
- A larger disk cannot be placed on top of a smaller disk.

## ✨ Features

- Solves the Tower of Hanoi puzzle using recursion.
- Simulates disk movements across three rods.
- Records the state of the rods after every move.
- Uses a recursive base case to terminate the process.
- Returns the complete sequence of rod states as a string.

## 🧪 Example

Calling the function with three disks:

```python
print(hanoi_solver(3))
```

The initial state is:

```text
[3, 2, 1] [] []
```

The solution records the rod configuration after each disk movement, ending with all disks on the target rod:

```text
[] [] [3, 2, 1]
```

Each recorded line represents the state of the three rods at a particular step.

## ⏱️ Time and Space Complexity

Let \(n\) represent the number of disks.

| Complexity | Value |
|---|---|
| Time complexity | O(2ⁿ) |
| Auxiliary recursion space | O(n) |
| Space including recorded moves | O(n × 2ⁿ) |

The puzzle requires \(2^n - 1\) moves for \(n\) disks. Because the program stores the state of all three rods after each move, its total storage requirement grows exponentially.

## 🛠️ Technologies Used

- **Language:** Python 3
- **Concepts:** Recursion, lists, nested functions, stack-based disk movement, algorithm analysis, and state tracking.

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Save the code in a Python file, such as `hanoi_solver.py`.
3. Import the function or call it from your program:

   ```python
   print(hanoi_solver(3))
   ```

The function returns a string containing the recorded states of the rods.

## 🎯 Learning Objectives

This project demonstrates an understanding of:

- Recursive problem-solving.
- Base cases and recursive calls.
- Breaking a complex problem into smaller subproblems.
- Manipulating lists using `pop()` and `append()`.
- Tracking state changes throughout an algorithm.
- Analyzing exponential time complexity.

---

**Project Type:** Recursive Algorithm  
**Language:** Python 3
