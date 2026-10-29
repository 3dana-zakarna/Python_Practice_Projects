
def quick_sort(list_of_numbers):
    if len(list_of_numbers) <= 1:
        return list_of_numbers.copy()

    pivot = list_of_numbers[0]

    less = []
    equal = []
    greater = []

    for number in list_of_numbers:
        if number < pivot:
            less.append(number)
        elif number == pivot:
            equal.append(number)
        else:
            greater.append(number)

    return quick_sort(less) + equal + quick_sort(greater)


# =========================
# TEST CASES
# =========================

def run_tests():
    print("========== TEST 1: EMPTY LIST ==========")
    assert quick_sort([]) == []
    print("Test 1 passed!")

    print("\n========== TEST 2: SINGLE ELEMENT ==========")
    assert quick_sort([7]) == [7]
    print("Test 2 passed!")

    print("\n========== TEST 3: NORMAL LIST ==========")
    assert quick_sort([20, 3, 14, 1, 5]) == [1, 3, 5, 14, 20]
    print("Test 3 passed!")

    print("\n========== TEST 4: DIFFERENT NUMBERS ==========")
    assert quick_sort([83, 4, 24, 2]) == [2, 4, 24, 83]
    print("Test 4 passed!")

    print("\n========== TEST 5: SIX ELEMENTS ==========")
    assert quick_sort([4, 42, 16, 23, 15, 8]) == [4, 8, 15, 16, 23, 42]
    print("Test 5 passed!")

    print("\n========== TEST 6: DUPLICATE VALUES ==========")
    assert quick_sort(
        [87, 11, 23, 18, 18, 23, 11, 56, 87, 56]
    ) == [11, 11, 18, 18, 23, 23, 56, 56, 87, 87]
    print("Test 6 passed!")

    print("\n========== TEST 7: ORIGINAL LIST UNCHANGED ==========")
    original = [5, 2, 8, 1, 3]
    original_copy = original.copy()

    result = quick_sort(original)

    assert original == original_copy
    assert result == [1, 2, 3, 5, 8]
    print("Test 7 passed!")

    print("\n========== TEST 8: REVERSE ORDER ==========")
    assert quick_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    print("Test 8 passed!")

    print("\n========== ALL TESTS PASSED! ==========")


if __name__ == "__main__":
    run_tests()
