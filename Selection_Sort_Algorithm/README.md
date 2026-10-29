# Selection Sort Algorithm

## 📌 Project Overview

This project implements the **Selection Sort algorithm** in Python to sort a list of elements in ascending order. It repeatedly finds the smallest element in the unsorted portion of the list and swaps it into its correct position.

The project includes test cases covering different input scenarios to verify the algorithm's correctness.

## ⚙️ How It Works

The `selection_sort(items)` function:

1. Iterates through the list to identify the current position.
2. Searches the remaining unsorted portion for the smallest element.
3. Swaps the smallest element with the element at the current position when necessary.
4. Repeats the process until the list is sorted.
5. Returns the sorted list.

**Important:** The algorithm modifies the original list in place and returns the same list object.

## ✨ Features

- Sorts elements in ascending order.
- Handles empty lists and single-element lists.
- Supports duplicate values.
- Works with reverse-sorted and already-sorted lists.
- Modifies the original list instead of creating a new one.
- Includes automated tests using Python assertions.

## 🧪 Test Cases

The project tests the following scenarios:

- Empty list.
- Single-element list.
- Unsorted lists with different values.
- Lists containing duplicate elements.
- Reverse-sorted list.
- In-place modification verification.
- Already-sorted list.

## ⏱️ Time and Space Complexity

| Complexity | Value |
|---|---|
| Best-case time | O(n²) |
| Average-case time | O(n²) |
| Worst-case time | O(n²) |
| Auxiliary space | O(1) |

Selection Sort uses constant auxiliary space because it sorts the list in place. Its time complexity remains quadratic regardless of the initial ordering of the elements.

## 🛠️ Technologies Used

- **Language:** Python 3
- **Concepts:** Sorting algorithms, nested loops, list manipulation, swapping, algorithm analysis, and unit testing with assertions.

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Open a terminal in the project directory.
3. Run the Python file:

   ```bash
   python selection_sort.py
   ```

   Replace `selection_sort.py` with the actual name of your Python file if it is different.

The program runs all test cases and prints a success message when they pass.

## 🎯 Learning Objectives

This project demonstrates an understanding of:

- The Selection Sort algorithm.
- Finding minimum values in an unsorted sequence.
- Swapping elements in a list.
- In-place sorting.
- Time and space complexity analysis.
- Testing algorithms against multiple edge cases.

---

**Project Type:** Algorithm Implementation  
**Language:** Python 3
