# ISBN Validator 📚

## Overview
The **ISBN Validator** is a Python project that checks whether an International Standard Book Number (ISBN) is valid. It supports both **ISBN-10** and **ISBN-13** formats by calculating the expected check digit and comparing it with the digit provided in the input.

ISBNs are unique identifiers used to identify books and other book-related publications.

## Features
- Supports ISBN-10 and ISBN-13 validation.
- Calculates check digits using the appropriate algorithm for each format.
- Handles the special `X` check digit used by ISBN-10.
- Checks whether the ISBN has the required number of characters.
- Accepts user input containing an ISBN and its length.
- Displays whether the ISBN is valid or invalid.

## How It Works
1. The user enters an ISBN and its length, separated by a comma.
2. The program checks whether the specified length is `10` or `13`.
3. It verifies that the ISBN contains the expected number of characters.
4. It separates the main digits from the final check digit.
5. It calculates the expected check digit using the appropriate algorithm.
6. It compares the calculated digit with the supplied digit and displays the result.

## Validation Algorithms

### ISBN-10
The program multiplies the first nine digits by weights from `10` down to `2`, then uses the sum to calculate the expected check digit. The check digit can be a number from `0` to `9`, or `X` when its value represents `10`.

### ISBN-13
The program multiplies the first twelve digits by alternating weights of `1` and `3`. It uses the resulting sum to calculate the final check digit.

## Example Input
```text
978030640615,13
```

The program calculates the expected ISBN-13 check digit and compares it with the final character supplied in the input.

## Concepts Practiced
- Python Functions
- Conditional Statements
- Loops and Arithmetic Operations
- Lists and List Comprehensions
- String Manipulation
- Input Parsing
- Check Digit Algorithms
- Modular Arithmetic

## Technologies Used
- Python 3

## Learning Outcomes
This project provides practical experience implementing validation algorithms, processing user input, working with strings and lists, and using mathematical operations to verify identifiers.

## Possible Improvements
- Validate that all ISBN characters are permitted before converting them to integers.
- Handle malformed input and invalid length values gracefully.
- Add automated test cases for valid and invalid ISBNs.
- Support ISBN-13 inputs that include hyphens by normalizing the input first.

---

*Part of my Python practice projects, focused on algorithm implementation, data validation, and problem-solving.*
