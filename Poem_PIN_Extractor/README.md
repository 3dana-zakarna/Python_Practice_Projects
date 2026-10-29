# Poem PIN Extractor

## 📌 Project Overview

This project implements a simple text-processing algorithm in Python that extracts numeric secret codes from poems.

The program analyzes each poem line by line and generates a digit for every line based on the number of characters in a specific word. The selected word depends on the line's position within the poem.

The resulting digits are combined to create a PIN-like code for each poem.

## ⚙️ How It Works

The `pin_extractor(poems)` function follows these steps:

1. Receives a list of poems as input.
2. Splits each poem into individual lines.
3. Splits each line into words.
4. Uses the line's index to select the corresponding word.
5. Counts the characters in the selected word and adds the count to the secret code.
6. Adds `0` when the selected word does not exist on a particular line.
7. Stores the generated code for each poem and returns a list of codes.

## ✨ Features

- Processes multiple poems in a single function call.
- Extracts numeric codes using word lengths.
- Uses line positions to determine which words are analyzed.
- Handles lines that do not contain enough words by appending `0`.
- Returns a list containing one generated code per poem.
- Demonstrates string manipulation, loops, indexing, and conditional logic.

## 🧪 Example

The project defines three sample poems and passes them to the function:

```python
print(pin_extractor([poem, poem2, poem3]))
```

The function returns a list of strings, with each string representing the code extracted from one poem.

Each digit corresponds to the character count of the selected word on a line, or `0` if that word is unavailable.

## 🛠️ Technologies Used

- **Language:** Python 3
- **Concepts:** String manipulation, lists, nested loops, `split()`, `enumerate()`, indexing, conditional statements, and character counting.

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Save the code in a Python file, such as `pin_extractor.py`.
3. Run the file from your terminal:

   ```bash
   python pin_extractor.py
   ```

The program processes the sample poems and prints their extracted codes.

## 🎯 Learning Objectives

This project demonstrates an understanding of:

- Processing multiline strings.
- Splitting text into lines and words.
- Using indexes to select elements.
- Counting characters in strings.
- Building numeric codes from text.
- Handling missing elements with conditional logic.
- Processing collections of text using loops.

## ⚠️ Note

This is an educational text-processing project. The generated codes are based on word lengths and should not be considered secure PINs for authentication or sensitive information.

---

**Project Type:** Text Processing  
**Language:** Python 3
