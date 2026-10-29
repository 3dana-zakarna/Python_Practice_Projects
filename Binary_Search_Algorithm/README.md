# Binary Search Algorithm 🔍

## Overview
The **Binary Search Algorithm** is a Python project that searches for a target value in a sorted list by repeatedly dividing the search range in half.

In addition to searching for the target, the function records the values examined along the way, providing a simple way to visualize the search process.

## Features
- Searches for a target value in a sorted list.
- Uses an iterative binary search approach.
- Records the sequence of values examined during the search.
- Returns the search path when the target is found.
- Returns a message when the target is not found.
- Includes example calls for successful and unsuccessful searches.

## How It Works
1. Initializes the search boundaries using `low` and `high`.
2. Calculates the middle index of the current search range.
3. Records the value at the middle index.
4. Compares the middle value with the target:
   - If they match, the function returns the search path.
   - If the target is greater, the search continues in the right half.
   - If the target is smaller, the search continues in the left half.
5. Repeats until the target is found or the search range becomes empty.

## Example
```python
print(binary_search([1, 2, 3, 4, 5], 3))
```

Expected output:

```text
[3]
```

Another example:

```python
print(binary_search([1, 3, 5, 9, 14, 22], 10))
```

Since `10` is not in the list, the function returns an empty search path along with a message indicating that the value was not found.

## Concepts Practiced
- Searching Algorithms
- Binary Search
- Iterative Loops
- Conditional Statements
- List Indexing
- Tracking Algorithm Execution
- Algorithm Efficiency and Complexity

## Complexity Analysis
- **Time Complexity:** O(log n), because the search range is approximately halved in each iteration.
- **Space Complexity:** O(log n) for the recorded search path in the worst case.

## Important Note
Binary search requires the input list to be sorted in ascending order for the algorithm to work correctly.

## Technologies Used
- Python 3

## Learning Outcomes
This project demonstrates how binary search efficiently locates values in sorted data and how tracking intermediate steps can help explain an algorithm's behavior.

---

*Part of my Python practice projects, focused on algorithms, data structures, and problem-solving.*
