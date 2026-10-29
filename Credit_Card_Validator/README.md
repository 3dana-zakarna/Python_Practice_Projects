# Credit Card Number Validator 💳

## Overview
The **Credit Card Number Validator** is a Python project that verifies whether a numeric card number satisfies the **Luhn algorithm**, a checksum algorithm commonly used to validate identification numbers, including many payment card numbers.

The program normalizes the input by removing spaces and hyphens, checks that the remaining characters are digits, and calculates the checksum to determine whether the number passes validation.

## Features
- Validates numeric card numbers using the Luhn algorithm.
- Accepts numbers containing spaces or hyphens.
- Rejects empty input and non-digit characters.
- Calculates the checksum by doubling alternating digits.
- Subtracts `9` from doubled digits greater than `9`.
- Returns `"VALID!"` or `"INVALID!"`.
- Includes test cases for valid and invalid inputs.

## How It Works
1. Removes spaces and hyphens from the input.
2. Checks whether the input is non-empty and contains only digits.
3. Converts the string into a list of integers.
4. Starting from the right, doubles every other digit, excluding the rightmost digit.
5. Subtracts `9` from any doubled digit greater than `9`.
6. Adds all the digits together.
7. If the total is divisible by `10`, the number passes the Luhn check.

## Example
```python
verify_card_number("4111-1111-1111-1111")
```

Expected output:

```text
VALID!
```

Another example:

```python
verify_card_number("453914881")
```

Expected output:

```text
INVALID!
```

## Test Cases
The project includes tests for:
- A number that passes the Luhn check.
- Valid-looking input containing hyphens.
- An invalid number.
- Inputs containing spaces.
- Empty input.
- Non-digit characters.
- Displaying validation results.

The test suite uses Python's `assert` statements to check expected results.

## Concepts Practiced
- String Manipulation
- Input Validation
- Lists and List Comprehensions
- Loops and Conditional Statements
- Integer Conversion
- Checksum Algorithms
- The Luhn Algorithm
- Automated Testing

## Complexity Analysis
For an input containing `n` digits:

- **Time Complexity:** O(n), because the algorithm processes the input a constant number of times.
- **Space Complexity:** O(n), because it stores the digits in a list.

## Technologies Used
- Python 3

## Important Note
Passing the Luhn check does **not** prove that a card exists, is active, or is authorized for transactions. This project performs checksum validation only and does not process payments or access financial accounts.

## Learning Outcomes
This project demonstrates how checksum algorithms can validate structured numeric input. It also provides practice with string processing, input validation, arithmetic operations, and automated testing.

---

*Part of my Python practice projects, focused on algorithms, validation, and problem-solving.*
