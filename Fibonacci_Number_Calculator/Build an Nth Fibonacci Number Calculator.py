
def fibonacci(n):
    sequence = [0, 1]

    if n < 2:
        return sequence[n]

    for i in range(2, n + 1):
        next_number = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_number)

    return sequence[n]


# =========================
# TEST CASES
# =========================

def run_tests():
    print("========== TEST 1: N = 0 ==========")
    assert fibonacci(0) == 0
    print("Test 1 passed!")

    print("\n========== TEST 2: N = 1 ==========")
    assert fibonacci(1) == 1
    print("Test 2 passed!")

    print("\n========== TEST 3: N = 2 ==========")
    assert fibonacci(2) == 1
    print("Test 3 passed!")

    print("\n========== TEST 4: N = 3 ==========")
    assert fibonacci(3) == 2
    print("Test 4 passed!")

    print("\n========== TEST 5: N = 5 ==========")
    assert fibonacci(5) == 5
    print("Test 5 passed!")

    print("\n========== TEST 6: N = 10 ==========")
    assert fibonacci(10) == 55
    print("Test 6 passed!")

    print("\n========== TEST 7: N = 15 ==========")
    assert fibonacci(15) == 610
    print("Test 7 passed!")

    print("\n========== ALL TESTS PASSED! ==========")


if __name__ == "__main__":
    run_tests()
