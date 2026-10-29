# Merge Sort Algorithm 🔢

## Overview
The **Merge Sort Algorithm** is a Python implementation of a sorting algorithm that follows the **Divide and Conquer** approach. It divides an array into smaller subarrays, sorts them recursively, and merges them back together in ascending order.

The algorithm modifies the original array by placing the sorted elements back into it.

## Features
- Sorts an array in ascending order.
- Uses the Divide and Conquer strategy.
- Recursively splits the array into smaller parts.
- Merges sorted subarrays into a single sorted array.
- Handles empty arrays and arrays containing a single element.
- Demonstrates sorting with an example list of integers.

## How It Works
1. Checks whether the array contains zero or one element. If so, it is already sorted.
2. Divides the array into left and right halves.
3. Recursively sorts each half.
4. Compares elements from both halves.
5. Places the smaller element into the original array.
6. Copies any remaining elements from either half.
7. Continues until the original array is sorted.

## Example
The project starts with the following array:

```python
numbers = [4, 10, 6, 14, 2, 1, 8, 5]
```

After calling `merge_sort(numbers)`, the array becomes:

```python
[1, 2, 4, 5, 6, 8, 10, 14]
```

**Note:** The function sorts the list in place and returns `None`.

## Concepts Practiced
- Sorting Algorithms
- Merge Sort
- Divide and Conquer
- Recursion
- List Slicing
- Array Indexing
- Loops and Conditional Statements
- Merging Sorted Sequences

## Complexity Analysis
For an array containing `n` elements:

- **Time Complexity:** O(n log n) in the best, average, and worst cases.
- **Space Complexity:** O(n) for the temporary subarrays created during the recursive process.

## Technologies Used
- Python 3

## Learning Outcomes
This project demonstrates how recursion and the Divide and Conquer strategy can be used to implement an efficient sorting algorithm. It also provides practice with list manipulation, index tracking, and merging sorted data.

---

*Part of my Python practice projects, focused on algorithms, data structures, and problem-solving.*
