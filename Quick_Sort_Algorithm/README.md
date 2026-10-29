# Quick Sort Algorithm ⚡

## Overview
The **Quick Sort Algorithm** is a Python implementation of a sorting algorithm that uses the **Divide and Conquer** strategy to arrange numbers in ascending order.

The function selects a pivot, separates the input values into three groups, and recursively sorts the smaller and larger values before combining the results.

## Features
- Sorts numbers in ascending order.
- Uses a recursive Divide and Conquer approach.
- Selects the first element as the pivot.
- Separates values into `less`, `equal`, and `greater` groups.
- Handles duplicate values correctly.
- Supports empty lists and lists containing a single element.
- Returns a new sorted list without modifying the original input list.

## How It Works
1. Checks whether the input list contains zero or one element.
2. Selects the first element as the pivot.
3. Iterates through the list and classifies each number:
   - `less`: numbers smaller than the pivot.
   - `equal`: numbers equal to the pivot.
   - `greater`: numbers greater than the pivot.
4. Recursively sorts the `less` and `greater` lists.
5. Combines the sorted groups into a new list.

## Example
```python
quick_sort([20, 3, 14, 1, 5])
```

Expected output:

```python
[1, 3, 5, 14, 20]
```

The function also handles duplicate values:

```python
quick_sort([4, 2, 4, 1, 2])
```

Expected output:

```python
[1, 2, 2, 4, 4]
```

## Test Cases
The project includes tests for:
- Empty lists.
- Lists containing one element.
- Unsorted lists of different sizes.
- Duplicate values.
- Lists in reverse order.
- Preserving the original input list.

The test suite uses Python's `assert` statements to verify the results.

## Concepts Practiced
- Sorting Algorithms
- Quick Sort
- Divide and Conquer
- Recursion
- List Comprehensions and List Operations
- Pivot Selection
- Handling Duplicate Values
- Automated Testing

## Complexity Analysis
For a list containing `n` elements:

- **Average Time Complexity:** O(n log n).
- **Worst-Case Time Complexity:** O(n²), which can occur when the pivot repeatedly produces highly unbalanced partitions.
- **Space Complexity:** Additional memory is required for the partition lists and recursive calls.

Because the implementation always chooses the first element as the pivot, already sorted or reverse-sorted lists can lead to worst-case behavior.

## Technologies Used
- Python 3

## Learning Outcomes
This project demonstrates how recursive partitioning can be used to sort data efficiently. It also provides practice with pivot selection, list manipulation, recursion, and testing whether a function preserves its input.

---

*Part of my Python practice projects, focused on algorithms, data structures, and problem-solving.*
