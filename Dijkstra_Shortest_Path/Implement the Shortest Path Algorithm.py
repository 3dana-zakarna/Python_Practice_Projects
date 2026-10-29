
INF = float('inf')

adj_matrix = [
    [0, 5, 3, INF, 11, INF],
    [5, 0, 1, INF, INF, 2],
    [3, 1, 0, 1, 5, INF],
    [INF, INF, 1, 0, 9, 3],
    [11, INF, 5, 9, 0, INF],
    [INF, 2, INF, 3, INF, 0],
]


def shortest_path(matrix, start_node, target_node=None):
    n = len(matrix)

    distances = [INF] * n
    distances[start_node] = 0

    paths = [[node] for node in range(n)]
    paths[start_node] = [start_node]

    visited = [False] * n

    for _ in range(n):
        min_distance = INF
        current = -1

        for node_no in range(n):
            if not visited[node_no] and distances[node_no] < min_distance:
                min_distance = distances[node_no]
                current = node_no

        if current == -1:
            break

        visited[current] = True

        for node_no in range(n):
            distance = matrix[current][node_no]

            if distance != INF and not visited[node_no]:
                new_distance = distances[current] + distance

                if new_distance < distances[node_no]:
                    distances[node_no] = new_distance
                    paths[node_no] = paths[current] + [node_no]

    targets = [target_node] if target_node is not None else range(n)

    for node_no in targets:
        if node_no == start_node or distances[node_no] == INF:
            continue

        path = ' -> '.join(str(node) for node in paths[node_no])

        print(
            f'\n{start_node}-{node_no} distance: {distances[node_no]}'
            f'\nPath: {path}'
        )

    return distances, paths


# =========================
# TEST CASES
# =========================

def run_tests():

    print("========== TEST 1: START NODE 0 ==========")
    distances, paths = shortest_path(adj_matrix, 0)

    assert distances == [0, 4, 3, 4, 8, 6]
    assert paths[0] == [0]
    assert paths[1] == [0, 2, 1]
    assert paths[2] == [0, 2]
    assert paths[3] == [0, 2, 3]
    assert paths[4] == [0, 2, 4]
    assert paths[5] == [0, 2, 1, 5]

    print("Test 1 passed!")

    print("\n========== TEST 2: SPECIFIC TARGET ==========")
    distances, paths = shortest_path(adj_matrix, 0, 5)

    assert distances[5] == 6
    assert paths[5] == [0, 2, 1, 5]

    print("Test 2 passed!")

    print("\n========== TEST 3: SAME START AND TARGET ==========")
    distances, paths = shortest_path(adj_matrix, 2, 2)

    assert distances[2] == 0
    assert paths[2] == [2]

    print("Test 3 passed!")

    print("\n========== TEST 4: START NODE 5 ==========")
    distances, paths = shortest_path(adj_matrix, 5)

    assert distances == [6, 2, 3, 3, 8, 0]
    assert paths[0] == [5, 1, 2, 0]
    assert paths[1] == [5, 1]
    assert paths[2] == [5, 1, 2]
    assert paths[3] == [5, 3]
    assert paths[4] == [5, 1, 2, 4]
    assert paths[5] == [5]

    print("Test 4 passed!")

    print("\n========== TEST 5: DISCONNECTED GRAPH ==========")
    disconnected_matrix = [
        [0, 2, INF],
        [2, 0, INF],
        [INF, INF, 0]
    ]

    distances, paths = shortest_path(disconnected_matrix, 0)

    assert distances[0] == 0
    assert distances[1] == 2
    assert distances[2] == INF

    print("Test 5 passed!")

    print("\n========== TEST 6: SINGLE NODE ==========")
    single_node_matrix = [[0]]

    distances, paths = shortest_path(single_node_matrix, 0)

    assert distances == [0]
    assert paths == [[0]]

    print("Test 6 passed!")

    print("\n========== ALL TESTS PASSED! ==========")


if __name__ == "__main__":
    run_tests()


