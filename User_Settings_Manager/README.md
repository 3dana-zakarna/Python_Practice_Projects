# User Settings Manager

## 📌 Project Overview

This project implements a simple **User Settings Management System** in Python using a dictionary to store and manage user preferences.

It provides functions to add new settings, update existing values, delete settings, and display all currently stored preferences. Setting names and values are converted to lowercase to maintain consistent formatting.

## ✨ Features

- **Add Settings:** Adds a new setting if its key does not already exist.
- **Update Settings:** Changes the value of an existing setting.
- **Delete Settings:** Removes a setting by its key.
- **View Settings:** Displays all settings in a readable format.
- **Duplicate Prevention:** Prevents adding a setting with a key that already exists.
- **Missing-Key Handling:** Returns informative messages when a setting cannot be updated or deleted because it does not exist.
- **Case Normalization:** Converts setting keys and values to lowercase for consistent storage.
- **Empty Dictionary Handling:** Displays a message when no settings are available.

## 🛠️ Technologies Used

- Python
- Dictionaries
- Functions
- Conditional Statements
- String Methods
- Dictionary Iteration

## 🧠 Concepts Demonstrated

- Key-value data storage
- Dictionary manipulation
- Adding, updating, and deleting entries
- Function parameters and return values
- Conditional logic
- String normalization with `lower()`
- Formatting output with f-strings
- Handling missing and duplicate keys

## ⚙️ Available Functions

| Function | Description |
|---|---|
| `add_setting(settings, setting)` | Adds a new setting if its key is not already present. |
| `update_setting(settings, setting)` | Updates an existing setting's value. |
| `delete_setting(settings, key)` | Deletes a setting using its key. |
| `view_settings(settings)` | Returns a formatted summary of all settings. |

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Open a terminal in the project directory.
3. Run the Python file:

   ```bash
   python user_settings.py
   ```

   Replace `user_settings.py` with the actual name of your Python file if it differs.

## 🧪 Example Scenario

The program starts with these settings:

- `theme`: `dark`
- `language`: `english`
- `notifications`: `enabled`

It then adds a volume setting, updates the theme to light, deletes the language setting, and displays the remaining preferences.

## 📚 Learning Objective

The goal of this project is to practice dictionary operations, reusable functions, conditional logic, and string manipulation while building a simple settings management system.

---

**Project Type:** Python Fundamentals Practice  
**Language:** Python
