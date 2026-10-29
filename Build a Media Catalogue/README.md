# Media Catalogue System

## 📌 Project Overview

This project implements a **Media Catalogue System** in Python using Object-Oriented Programming (OOP).

It manages different types of media content, including movies and TV series. The system uses inheritance to share common movie attributes with TV series, validates input data, and applies custom exceptions to handle invalid media items.

## ✨ Features

- **Movie Class:** Stores movie details, including title, release year, director, and duration.
- **TVSeries Class:** Inherits from `Movie` and adds seasons and total episode information.
- **Media Catalogue:** Stores and organizes movie and TV series objects.
- **Input Validation:** Checks titles, release years, directors, durations, seasons, and episode counts.
- **Custom Exceptions:** Defines a `MediaError` exception for invalid media items.
- **Media Filtering:** Retrieves movies and TV series separately.
- **Readable Output:** Uses custom string representations to display media information.

## 🛠️ Technologies Used

- Python
- Object-Oriented Programming (OOP)
- Inheritance
- Custom Exceptions
- List Comprehensions
- Type Checking
- Exception Handling

## 🧠 Concepts Demonstrated

- Classes and objects
- Parent and child classes
- Method overriding
- Constructor validation
- Custom exception classes
- Polymorphism and inheritance
- Filtering collections of objects
- String representation with `__str__()`

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Open a terminal in the project directory.
3. Run the Python file:

   ```bash
   python media_catalogue.py
   ```

   Replace `media_catalogue.py` with the actual name of your Python file if it differs.

## 🎬 Example Media Items

The example program creates and adds the following items to the catalogue:

| Type | Title | Year |
|---|---|---:|
| Movie | The Matrix | 1999 |
| Movie | Inception | 2010 |
| TV Series | Scrubs | 2001 |
| TV Series | Breaking Bad | 2008 |

The program then prints the catalogue's contents.

## 📚 Learning Objective

The goal of this project is to practice designing an object-oriented system that manages related data types through inheritance, validates input, handles errors, and organizes objects in a collection.

---

**Project Type:** Python OOP Practice  
**Language:** Python
