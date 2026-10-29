# N-Queens Solver Using DFS ♟️

## Overview
The **N-Queens Solver** is a Python project that finds all valid ways to place `N` queens on an `N × N` chessboard so that no two queens attack each other.

The solution uses **Depth-First Search (DFS)** combined with **backtracking** to explore possible queen placements and reject configurations that violate the rules.

## Features
- Finds all valid solutions for a given board size.
- Uses DFS and recursive backtracking.
- Prevents queens from sharing the same column or diagonal.
- Represents each solution as a list of column positions.
- Handles board sizes with no valid solutions.
- Includes test cases for multiple board sizes.

## How It Works
1. Starts with the first row of the chessboard.
2. Tries placing a queen in each column of the current row.
3. Checks whether the position conflicts with any previously placed queen.
4. If the position is safe, adds the queen and recursively processes the next row.
5. If a conflict occurs or a branch is completed, backtracks and tries another position.
6. When queens have been placed in all `N` rows, saves a copy of the solution.
7. Returns all valid solutions after exploring the search space.

## Solution Representation
Each solution is represented as a list in which the index represents the row and the value represents the queen's column.

For example:

```python id="x6j8pv"
[1, 3, 0, 2]
```

This represents one valid solution for a 4 × 4 chessboard.

## Example
```python id="n0pm44"
dfs_n_queens(4)
```

Expected output:

```python id="1mvhkc"
[
    [1, 3, 0, 2],
    [2, 0, 3, 1]
]
```

The 4-Queens problem has two valid solutions.

## Test Cases
The project tests the following board sizes:

| Board Size (`N`) | Number of Solutions |
|---:|---:|
| 1 | 1 |
| 2 | 0 |
| 3 | 0 |
| 4 | 2 |
| 5 | 10 |
| 8 | 92 |
| 0 | 0 |
| -3 | 0 |

The test suite uses Python's `assert` statements to verify the expected solutions and solution counts.

## Concepts Practiced
- Depth-First Search (DFS)
- Recursive Algorithms
- Backtracking
- Constraint Checking
- Lists and List Operations
- Nested Functions
- Absolute Differences and Diagonal Detection
- Automated Testing

## Complexity Analysis
The N-Queens problem has a rapidly growing search space as the board size increases.

- **Time Complexity:** Exponential in the general case, as the algorithm explores possible queen placements while pruning invalid configurations.
- **Space Complexity:** O(N) for the current board and recursion stack, excluding the storage required for all returned solutions.

## Technologies Used
- Python 3

## Learning Outcomes
This project demonstrates how DFS and backtracking can solve constraint-satisfaction problems. It provides practical experience with recursion, search-space pruning, and systematically generating all valid configurations.

---

*Part of my Python practice projects, focused on algorithms, recursion, and problem-solving.*
