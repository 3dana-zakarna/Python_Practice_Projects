
def countup(number):
    if number < 1:
        return []
    count_list = countup(number - 1)
    count_list.append(number)
    return count_list


# =========================
# TEST CASES
# =========================

def run_tests():
    print("========== TEST 1: POSITIVE NUMBER ==========")
    assert countup(5) == [1, 2, 3, 4, 5]
    print("Test 1 passed!")

    print("\n========== TEST 2: NUMBER 1 ==========")
    assert countup(1) == [1]
    print("Test 2 passed!")

    print("\n========== TEST 3: ZERO ==========")
    assert countup(0) == []
    print("Test 3 passed!")

    print("\n========== TEST 4: NEGATIVE NUMBER ==========")
    assert countup(-3) == []
    print("Test 4 passed!")

    print("\n========== TEST 5: NUMBER 10 ==========")
    assert countup(10) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Test 5 passed!")

    print("\n========== TEST 6: RETURN TYPE ==========")
    assert isinstance(countup(3), list)
    print("Test 6 passed!")

    print("\n========== TEST 7: ORIGINAL LIST ORDER ==========")
    result = countup(4)
    assert result == sorted(result)
    print("Test 7 passed!")

    print("\n========== ALL TESTS PASSED! ==========")


if __name__ == "__main__":
    run_tests()


