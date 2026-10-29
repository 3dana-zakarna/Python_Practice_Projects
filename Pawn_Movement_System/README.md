# Pawn Movement System

## 📌 Project Overview

This project implements a simple movement system in Python inspired by chess pieces. It uses **Object-Oriented Programming (OOP)** and abstract classes to define player movement behavior.

The `Player` class provides shared functionality for tracking positions, making random moves, and recording movement history. The `Pawn` class extends this functionality by defining its available moves and unlocking diagonal movement when it levels up.

## ✨ Features

- **Abstract Player Class:** Defines the common structure and behavior for player objects.
- **Pawn Class:** Implements a pawn-like character with horizontal and vertical movement.
- **Random Movement:** Selects a move randomly from the available moves.
- **Position Tracking:** Maintains the player's current coordinates on a 2D grid.
- **Path History:** Records every position visited during movement.
- **Level-Up Mechanism:** Unlocks four diagonal moves when the pawn levels up.
- **Automated Tests:** Uses assertions to verify initialization, movement, level progression, path tracking, and abstract class behavior.

## 🛠️ Technologies Used

- Python
- Object-Oriented Programming (OOP)
- Abstract Base Classes (`ABC`)
- Abstract Methods
- Random Module
- Tuples and Lists
- Assertions and Testing

## 🧠 Concepts Demonstrated

- Abstraction and inheritance
- Implementing abstract methods
- Overriding methods in child classes
- Representing 2D coordinates using tuples
- Random selection with `random.choice()`
- Tracking state changes
- Extending available actions through level progression
- Testing class behavior with assertions

## 🎮 Movement System

The pawn begins at coordinate `(0, 0)` with four available moves:

| Direction | Coordinate Change |
|---|---|
| Up | `(0, 1)` |
| Down | `(0, -1)` |
| Left | `(-1, 0)` |
| Right | `(1, 0)` |

After leveling up, the pawn gains four diagonal moves:

- Up-left: `(-1, 1)`
- Up-right: `(1, 1)`
- Down-left: `(-1, -1)`
- Down-right: `(1, -1)`

Each move updates the current position and appends the new coordinates to the movement history.

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Open a terminal in the project directory.
3. Run the Python file:

   ```bash
   python pawn_movement.py
   ```

   Replace `pawn_movement.py` with the actual name of your Python file if it differs.

## 🧪 Test Coverage

The built-in tests verify:

1. Initial position, available moves, and path history
2. Random movement and position tracking
3. Level-up behavior and diagonal movement
4. Multiple moves and path length
5. The abstract nature of the `Player` class

If all assertions pass, the program prints a message confirming that all tests passed.

## 📚 Learning Objective

The goal of this project is to understand how abstract classes and inheritance can structure related behaviors, while practicing coordinate-based movement, state tracking, random actions, and automated testing.

---

**Project Type:** Python OOP and Data Structures Practice  
**Language:** Python
