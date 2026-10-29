# Hash Table Implementation

## 📌 Project Overview

This project implements a basic **Hash Table** in Python to store, retrieve, update, and remove key-value pairs efficiently.

It demonstrates how a hash function maps string keys to numerical hash values and how collisions can be handled by storing multiple keys within the same hash bucket.

## ✨ Features

- **Hash Function:** Calculates a hash value by summing the Unicode code points of each character in a string.
- **Add Items:** Stores key-value pairs in the hash table.
- **Lookup Items:** Retrieves values using their keys.
- **Update Existing Keys:** Replaces the value associated with an existing key.
- **Remove Items:** Deletes a key-value pair from the collection.
- **Collision Handling:** Stores multiple keys with the same hash value in a shared bucket.
- **Automated Tests:** Uses assertions to verify the expected behavior of the hash table.

## 🛠️ Technologies Used

- Python
- Dictionaries
- Hashing concepts
- Object-Oriented Programming (OOP)
- Assertions and testing

## 🧠 Concepts Demonstrated

- Hash functions and key-value storage
- Hash collisions and collision handling
- Dictionary-based data structures
- Class methods and object initialization
- Adding, updating, retrieving, and deleting data
- Unit-testing fundamentals

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Open a terminal in the project directory.
3. Run the Python file:

   ```bash
   python hash_table.py
   ```

   Replace `hash_table.py` with the actual name of your Python file if it differs.

## 🧪 Test Coverage

The built-in tests check:

1. Hash table initialization
2. Hash function results
3. Adding and looking up key-value pairs
4. Handling missing keys
5. Updating existing values
6. Removing existing keys
7. Removing nonexistent keys
8. Handling hash collisions without mixing up values

If all assertions pass, the program prints a message confirming that all tests passed.

## 📚 Learning Objective

The goal of this project is to understand the fundamental behavior of hash tables, including how keys are mapped to hash values and how collisions can be managed using buckets.

---

**Project Type:** Python Data Structures Practice  
**Language:** Python
