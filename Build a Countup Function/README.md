# Recursive Count Up

## Description
A Python program that uses recursion to generate a list of consecutive integers from 1 up to a given number. The function returns an empty list when the input is less than 1.

## Features
- Generates a sequence of numbers from 1 to the specified number.
- Uses recursion instead of traditional iteration to build the list.
- Handles zero and negative numbers by returning an empty list.
- Returns the numbers in ascending order.
- Includes test cases to verify the function's behavior for different inputs.

## Concepts Used
- Python Functions
- Recursion
- Lists and List Methods
- Conditional Statements
- Return Values
- Assertions and Testing
- Program Entry Point (`if __name__ == "__main__"`)

## How It Works
The `countup()` function calls itself with a number one less than the current number until it reaches a value less than 1. It then builds the list by appending each number as the recursive calls return.

## Example

```python
countup(5)
```

Output:

```text
[1, 2, 3, 4, 5]
```

Another example:

```python
countup(0)
```

Output:

```text
[]
```

## How to Run
1. Make sure Python 3 is installed.
2. Save the program in a `.py` file.
3. Run the file using:

   ```bash
   python countup.py
   ```

The program executes the included test cases and displays the results.

## Purpose
This project demonstrates how recursion can solve a simple counting problem and how assertions can be used to test function correctness.

**Language:** Python 3
