
def adjacency_list_to_matrix(adjacency_list):
    # Determine the number of nodes
    n = len(adjacency_list)

    # Create an n x n matrix filled with zeros
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    # Set 1 for every existing edge
    for node, neighbors in adjacency_list.items():
        for neighbor in neighbors:
            matrix[node][neighbor] = 1

    # Print each row
    for row in matrix:
        print(row)

    # Return the adjacency matrix
    return matrix


# =========================
# TEST CASES
# =========================

def run_tests():
    print("========== TEST 1 ==========")
    graph1 = {
        0: [1, 2],
        1: [2],
        2: [0, 3],
        3: [2]
    }

    expected1 = [
        [0, 1, 1, 0],
        [0, 0, 1, 0],
        [1, 0, 0, 1],
        [0, 0, 1, 0]
    ]

    assert adjacency_list_to_matrix(graph1) == expected1
    print("Test 1 passed!")

    print("\n========== TEST 2 ==========")
    graph2 = {
        0: [1],
        1: [0]
    }

    expected2 = [
        [0, 1],
        [1, 0]
    ]

    assert adjacency_list_to_matrix(graph2) == expected2
    print("Test 2 passed!")

    print("\n========== TEST 3 ==========")
    graph3 = {
        0: [],
        1: [],
        2: []
    }

    expected3 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    assert adjacency_list_to_matrix(graph3) == expected3
    print("Test 3 passed!")

    print("\n========== TEST 4: DIRECTED GRAPH ==========")
    graph4 = {
        0: [2],
        1: [],
        2: [1]
    }

    expected4 = [
        [0, 0, 1],
        [0, 0, 0],
        [0, 1, 0]
    ]

    assert adjacency_list_to_matrix(graph4) == expected4
    print("Test 4 passed!")

    print("\n========== ALL TESTS PASSED! ==========")


if __name__ == "__main__":
    run_tests()
