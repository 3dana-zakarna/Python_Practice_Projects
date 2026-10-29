
def dfs(adj_matrix, start_node):
    visited = []
    stack = [start_node]

    while stack:
        current = stack.pop()

        if current not in visited:
            visited.append(current)

            # Visit connected neighbors
            for neighbor in range(len(adj_matrix) - 1, -1, -1):
                if adj_matrix[current][neighbor] == 1 and neighbor not in visited:
                    stack.append(neighbor)

    return visited


# =========================
# TEST CASES
# =========================

def run_tests():
    print("========== TEST 1 ==========")
    graph1 = [
        [0, 1, 0, 0],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [0, 0, 1, 0]
    ]

    result = dfs(graph1, 1)
    assert result == [1, 0, 2, 3]
    print("Test 1 passed!", result)

    print("\n========== TEST 2 ==========")
    result = dfs(graph1, 3)
    assert result == [3, 2, 1, 0]
    print("Test 2 passed!", result)

    print("\n========== TEST 3: ISOLATED NODE ==========")
    graph2 = [
        [0, 1, 0, 0],
        [1, 0, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0]
    ]

    result = dfs(graph2, 3)
    assert result == [3]
    print("Test 3 passed!", result)

    print("\n========== TEST 4: DISCONNECTED COMPONENT ==========")
    graph3 = [
        [0, 1, 0, 0],
        [1, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 0]
    ]

    result = dfs(graph3, 3)
    assert result == [3, 2]
    print("Test 4 passed!", result)

    print("\n========== TEST 5 ==========")
    result = dfs(graph3, 0)
    assert result == [0, 1]
    print("Test 5 passed!", result)

    print("\n========== TEST 6: SINGLE NODE ==========")
    result = dfs([[0]], 0)
    assert result == [0]
    print("Test 6 passed!", result)

    print("\n========== ALL TESTS PASSED! ==========")


if __name__ == "__main__":
    run_tests()
