# Adjacency List to Adjacency Matrix

## 📌 Project Overview

This project implements a graph representation converter in Python that transforms an **adjacency list into an adjacency matrix**.

The program creates a square matrix initialized with zeros, then marks each existing edge with `1`. It supports directed graphs and can represent graphs with isolated nodes or no edges.

## ✨ Features

- **Graph Conversion:** Converts an adjacency list into an adjacency matrix.
- **Automatic Matrix Creation:** Builds an \(n \times n\) matrix based on the number of nodes.
- **Edge Representation:** Uses `1` to indicate an existing edge and `0` to indicate the absence of an edge.
- **Directed Graph Support:** Represents edges according to their specified direction.
- **Isolated Node Support:** Handles graphs whose nodes have no connections.
- **Matrix Display:** Prints each row of the resulting adjacency matrix.
- **Return Value:** Returns the generated matrix for further use.
- **Automated Tests:** Uses assertions to verify conversion results across different graph structures.

## 🛠️ Technologies Used

- Python
- Dictionaries
- Lists and Nested Lists
- Loops
- Graph Data Structures
- Assertions and Testing

## 🧠 Concepts Demonstrated

- Graph representations
- Adjacency lists and adjacency matrices
- Directed edges
- Nested list creation
- Iterating through dictionaries and lists
- Matrix indexing
- Converting between data structures
- Testing algorithms with assertions

## 🔗 How Graph Conversion Works

1. Determine the number of nodes in the graph.
2. Create a square matrix filled with zeros.
3. Iterate through each node and its neighbors.
4. Set the corresponding matrix entry to `1` for every edge.
5. Print and return the completed matrix.

For an edge from node `0` to node `2`, the matrix entry at `matrix[0][2]` becomes `1`. In a directed graph, the reverse entry is not automatically set.

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Open a terminal in the project directory.
3. Run the Python file:

   ```bash
   python adjacency_list_to_matrix.py
   ```

   Replace `adjacency_list_to_matrix.py` with the actual name of your Python file if it differs.

## 🧪 Test Coverage

The built-in tests verify:

1. Converting a graph with multiple edges
2. Converting a simple graph with bidirectional connections
3. Handling a graph with no edges
4. Correctly representing a directed graph

If all assertions pass, the program prints a message confirming that all tests passed.

## 📚 Learning Objective

The goal of this project is to understand common graph representations, practice nested list manipulation, and learn how edge direction affects the structure of an adjacency matrix.

---

**Project Type:** Python Graph Algorithms Practice  
**Language:** Python
