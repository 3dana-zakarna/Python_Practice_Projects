
def dfs_n_queens(n):
    if n < 1:
        return []

    solutions = []
    board = []

    def dfs(row):
        if row == n:
            solutions.append(board.copy())
            return

        for col in range(n):
            # Check whether this column or either diagonal is occupied
            safe = True

            for previous_row in range(row):
                previous_col = board[previous_row]

                if previous_col == col:
                    safe = False
                    break

                if abs(previous_col - col) == abs(previous_row - row):
                    safe = False
                    break

            if safe:
                board.append(col)
                dfs(row + 1)
                board.pop()

    dfs(0)
    return solutions


# =========================
# TEST CASES
# =========================

def run_tests():
    print("========== TEST 1: N = 1 ==========")
    assert dfs_n_queens(1) == [[0]]
    print("Test 1 passed!")

    print("\n========== TEST 2: N = 2 ==========")
    assert dfs_n_queens(2) == []
    print("Test 2 passed!")

    print("\n========== TEST 3: N = 3 ==========")
    assert dfs_n_queens(3) == []
    print("Test 3 passed!")

    print("\n========== TEST 4: N = 4 ==========")
    expected4 = [
        [1, 3, 0, 2],
        [2, 0, 3, 1]
    ]
    assert dfs_n_queens(4) == expected4
    print("Test 4 passed!")

    print("\n========== TEST 5: N = 5 ==========")
    expected5 = [
        [0, 2, 4, 1, 3],
        [0, 3, 1, 4, 2],
        [1, 3, 0, 2, 4],
        [1, 4, 2, 0, 3],
        [2, 0, 3, 1, 4],
        [2, 4, 1, 3, 0],
        [3, 0, 2, 4, 1],
        [3, 1, 4, 2, 0],
        [4, 1, 3, 0, 2],
        [4, 2, 0, 3, 1]
    ]
    assert dfs_n_queens(5) == expected5
    print("Test 5 passed!")

    print("\n========== TEST 6: N = 8 ==========")
    assert len(dfs_n_queens(8)) == 92
    print("Test 6 passed!")

    print("\n========== TEST 7: N = 0 ==========")
    assert dfs_n_queens(0) == []
    print("Test 7 passed!")

    print("\n========== TEST 8: NEGATIVE N ==========")
    assert dfs_n_queens(-3) == []
    print("Test 8 passed!")

    print("\n========== ALL TESTS PASSED! ==========")


if __name__ == "__main__":
    run_tests()
