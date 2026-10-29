
def range_of_numbers(start_num, end_num):
    if start_num == end_num:
        return [start_num]

    count_list = range_of_numbers(start_num + 1, end_num)
    count_list.insert(0, start_num)
    return count_list


# =========================
# TEST CASES
# =========================

def run_tests():
    print("========== TEST 1: NORMAL RANGE ==========")
    assert range_of_numbers(3, 9) == [3, 4, 5, 6, 7, 8, 9]
    print("Test 1 passed!")

    print("\n========== TEST 2: SAME START AND END ==========")
    assert range_of_numbers(5, 5) == [5]
    print("Test 2 passed!")

    print("\n========== TEST 3: TWO CONSECUTIVE NUMBERS ==========")
    assert range_of_numbers(4, 5) == [4, 5]
    print("Test 3 passed!")

    print("\n========== TEST 4: RANGE STARTING AT ZERO ==========")
    assert range_of_numbers(0, 4) == [0, 1, 2, 3, 4]
    print("Test 4 passed!")

    print("\n========== TEST 5: NEGATIVE NUMBERS ==========")
    assert range_of_numbers(-3, 2) == [-3, -2, -1, 0, 1, 2]
    print("Test 5 passed!")

    print("\n========== TEST 6: RETURN TYPE ==========")
    assert isinstance(range_of_numbers(2, 6), list)
    print("Test 6 passed!")

    print("\n========== TEST 7: PRINT OUTPUT ==========")
    print(range_of_numbers(3, 9))
    print(range_of_numbers(5, 5))
    print("Test 7 passed!")

    print("\n========== ALL TESTS PASSED! ==========")


if __name__ == "__main__":
    run_tests()
