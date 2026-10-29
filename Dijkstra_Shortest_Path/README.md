# Dijkstra's Shortest Path Algorithm

## 📌 Project Overview

This project implements **Dijkstra's algorithm** in Python to find the shortest paths from a starting node to other nodes in a weighted graph.

The graph is represented using an adjacency matrix, where each value represents the distance between two nodes. The value `float('inf')` indicates that no direct edge exists between two nodes.

The algorithm calculates the shortest distances and records the corresponding paths.

## ⚙️ How It Works

The `shortest_path(matrix, start_node, target_node=None)` function:

1. Initializes all distances to infinity, except the starting node, whose distance is zero.
2. Selects the unvisited node with the smallest known distance.
3. Examines its neighboring nodes and updates their distances when a shorter path is found.
4. Tracks the shortest path to each reachable node.
5. Repeats the process until all reachable nodes have been visited or no reachable unvisited nodes remain.
6. Prints the paths and distances for the requested target or all reachable destinations.

The function returns two lists:

- `distances`: The shortest known distance from the starting node to each node.
- `paths`: The sequence of nodes representing each shortest path.

## ✨ Features

- Finds shortest paths in a weighted graph.
- Supports finding paths to all nodes or a specific target.
- Tracks both distances and complete paths.
- Handles disconnected graphs.
- Supports graphs containing a single node.
- Handles cases where the starting node and target node are the same.
- Includes automated tests using Python assertions.

## 🗺️ Graph Representation

The project uses an adjacency matrix to represent a weighted graph.

Example:

```python
[
    [0, 5, 3],
    [5, 0, 1],
    [3, 1, 0]
]
```

Each row and column represents a node. A value of `0` on the diagonal represents the distance from a node to itself, while other values represent edge weights.

In this project, `float('inf')` represents the absence of a direct connection.

## 🧪 Test Cases

The project includes six test scenarios:

1. **Starting Node 0:** Verifies shortest distances and paths to all nodes.
2. **Specific Target:** Finds the shortest path from node 0 to node 5.
3. **Same Start and Target:** Confirms that the distance to the starting node is zero.
4. **Starting Node 5:** Tests shortest paths from a different starting point.
5. **Disconnected Graph:** Verifies that unreachable nodes retain an infinite distance.
6. **Single Node:** Tests the algorithm on a graph containing only one node.

## ⏱️ Time and Space Complexity

Let \(V\) represent the number of vertices.

| Complexity | Value |
|---|---|
| Time complexity | O(V²) |
| Space complexity | O(V²) |

The time complexity is \(O(V^2)\) because the algorithm searches for the nearest unvisited node and examines possible neighbors using nested loops.

The space complexity is \(O(V^2)\) because the adjacency matrix requires quadratic space. The distance, visited, and path-tracking structures require additional space.

## 🛠️ Technologies Used

- **Language:** Python 3
- **Data Structure:** Adjacency matrix
- **Algorithm:** Dijkstra's shortest path algorithm
- **Concepts:** Graph theory, weighted graphs, greedy algorithms, path reconstruction, and automated testing.

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Open a terminal in the project directory.
3. Run the Python file:

   ```bash
   python dijkstra_shortest_path.py
   ```

   Replace `dijkstra_shortest_path.py` with the actual filename if it is different.

The program executes the test cases and prints the shortest distances and paths.

## ⚠️ Important Note

Dijkstra's algorithm assumes that all edge weights are non-negative. It is not suitable for graphs containing negative-weight edges.

## 🎯 Learning Objectives

This project demonstrates an understanding of:

- Graph representation using adjacency matrices.
- Greedy algorithm design.
- Shortest-path calculations.
- Distance updates and path reconstruction.
- Handling unreachable nodes.
- Time and space complexity analysis.
- Testing graph algorithms with different scenarios.

---

**Project Type:** Graph Algorithm Implementation  
**Language:** Python 3
