# Rectangle and Square Calculator

## 📌 Project Overview

This project implements a geometric shape calculator in Python using **Object-Oriented Programming (OOP)**.

It defines a `Rectangle` class with methods for calculating geometric properties and generating text-based pictures. A `Square` class inherits from `Rectangle` and maintains equal width and height when its dimensions are updated.

## ✨ Features

- **Rectangle Class:** Represents rectangles using width and height.
- **Square Class:** Inherits from `Rectangle` and maintains equal side lengths.
- **Area Calculation:** Calculates the area of a shape.
- **Perimeter Calculation:** Computes the total distance around a shape.
- **Diagonal Calculation:** Uses the Pythagorean theorem to calculate the diagonal.
- **Text-Based Pictures:** Generates a rectangle or square using asterisks.
- **Dimension Updates:** Supports changing rectangle dimensions and square side lengths.
- **Shape-Fitting Calculation:** Determines how many copies of another shape can fit inside a rectangle using whole-number division.
- **Automated Tests:** Uses assertions to verify calculations and class behavior.

## 🛠️ Technologies Used

- Python
- Object-Oriented Programming (OOP)
- Inheritance
- The `math` Module
- Loops and Conditional Statements
- Assertions and Testing

## 🧠 Concepts Demonstrated

- Classes and objects
- Inheritance and method overriding
- Constructors and instance attributes
- Geometric calculations
- The Pythagorean theorem
- Integer division
- String formatting
- Generating text-based patterns
- Automated testing with assertions

## 📐 Available Methods

### Rectangle

| Method | Description |
|---|---|
| `set_width(width)` | Updates the rectangle's width. |
| `set_height(height)` | Updates the rectangle's height. |
| `get_area()` | Returns the area. |
| `get_perimeter()` | Returns the perimeter. |
| `get_diagonal()` | Returns the diagonal length. |
| `get_picture()` | Generates a text-based picture. |
| `get_amount_inside(shape)` | Calculates how many whole shapes fit inside the rectangle. |

### Square

The `Square` class inherits the rectangle's calculation and picture methods and adds `set_side(side)` to update both dimensions simultaneously. Its overridden dimension setters also keep the width and height equal.

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Open a terminal in the project directory.
3. Run the Python file:

   ```bash
   python rectangle_square.py
   ```

   Replace `rectangle_square.py` with the actual name of your Python file if it differs.

## 🧪 Test Coverage

The built-in tests verify:

1. Rectangle area, perimeter, and diagonal
2. Updating rectangle dimensions
3. Text-based picture generation
4. Square dimensions and calculations
5. Maintaining equal square sides after updates
6. Calculating how many shapes fit inside a rectangle

If all assertions pass, the program prints a message confirming that all tests passed.

## 📚 Learning Objective

The goal of this project is to practice object-oriented design, inheritance, method overriding, geometric calculations, and testing while modeling real-world shapes in Python.

---

**Project Type:** Python OOP and Geometry Practice  
**Language:** Python
