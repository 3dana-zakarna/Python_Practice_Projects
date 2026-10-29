# Depth-First Search (DFS) 🔎

## Overview
The **Depth-First Search (DFS)** project is a Python implementation of a graph traversal algorithm. It explores a graph by following connected nodes as deeply as possible before returning to explore other available paths.

The graph is represented using an **adjacency matrix**, and the algorithm uses an explicit stack to manage the traversal process.

## Features
- Traverses graphs using the DFS algorithm.
- Represents graphs with an adjacency matrix.
- Uses an iterative approach with a stack.
- Tracks visited nodes to avoid processing the same node multiple times.
- Supports isolated nodes and disconnected graph components.
- Includes test cases for different graph structures.

## How It Works
1. Initializes a list of visited nodes and a stack containing the starting node.
2. Removes the top node from the stack.
3. If the node has not been visited, adds it to the visited list.
4. Checks its connected neighbors using the adjacency matrix.
5. Adds unvisited neighbors to the stack.
6. Repeats until the stack is empty.
7. Returns the nodes in traversal order.

## Example
```python id="n8grm4"
graph = [
    [0, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 0]
]

print(dfs(graph, 1))
```

Expected output:

```text id="0qft6h"
[1, 0, 2, 3]
```

## Test Cases
The project includes tests for:
- Traversal from different starting nodes.
- An isolated node.
- Disconnected graph components.
- A graph containing a single node.

The test suite uses Python's `assert` statements to verify the expected traversal order.

## Concepts Practiced
- Graph Theory
- Depth-First Search (DFS)
- Adjacency Matrices
- Stack-Based Algorithms
- Lists and Loops
- Conditional Statements
- Graph Connectivity
- Automated Testing

## Complexity Analysis
For a graph with \(V\) vertices represented by an adjacency matrix:

- **Time Complexity:** O(V²) in the worst case, because the algorithm scans the matrix row for each visited vertex.
- **Space Complexity:** O(V) for the stack and visited-node list, excluding the adjacency matrix.

## Technologies Used
- Python 3

## Learning Outcomes
This project demonstrates how graph traversal works and how a stack can be used to explore connected nodes iteratively. It also provides practice with adjacency matrices, visited-node tracking, and handling different graph structures.

---

*Part of my Python practice projects, focused on algorithms, data structures, and problem-solving.*
