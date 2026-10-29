
def selection_sort(items):
    n = len(items)

    for i in range(n):
        min_index = i

        # Find the smallest element in the unsorted portion
        for j in range(i + 1, n):
            if items[j] < items[min_index]:
                min_index = j

        # Swap only if the minimum is not already in place
        if min_index != i:
            items[i], items[min_index] = items[min_index], items[i]

    return items


# =========================
# TEST CASES
# =========================

def run_tests():
    print("========== TEST 1: EMPTY LIST ==========")
    numbers = []
    assert selection_sort(numbers) == []
    print("Test 1 passed!")

    print("\n========== TEST 2: SINGLE ELEMENT ==========")
    numbers = [7]
    assert selection_sort(numbers) == [7]
    print("Test 2 passed!")

    print("\n========== TEST 3: FIRST REQUIRED EXAMPLE ==========")
    numbers = [33, 1, 89, 2, 67, 245]
    assert selection_sort(numbers) == [1, 2, 33, 67, 89, 245]
    print("Test 3 passed!")

    print("\n========== TEST 4: SECOND REQUIRED EXAMPLE ==========")
    numbers = [5, 16, 99, 12, 567, 23, 15, 72, 3]
    assert selection_sort(numbers) == [3, 5, 12, 15, 16, 23, 72, 99, 567]
    print("Test 4 passed!")

    print("\n========== TEST 5: DUPLICATE VALUES ==========")
    numbers = [
        1, 4, 2, 8, 345, 123, 43, 32, 5643,
        63, 123, 43, 2, 55, 1, 234, 92
    ]
    expected = [
        1, 1, 2, 2, 4, 8, 32, 43, 43,
        55, 63, 92, 123, 123, 234, 345, 5643
    ]
    assert selection_sort(numbers) == expected
    print("Test 5 passed!")

    print("\n========== TEST 6: REVERSE ORDER ==========")
    numbers = [5, 4, 3, 2, 1]
    assert selection_sort(numbers) == [1, 2, 3, 4, 5]
    print("Test 6 passed!")

    print("\n========== TEST 7: IN-PLACE MODIFICATION ==========")
    numbers = [9, 3, 6, 1]
    original_id = id(numbers)

    result = selection_sort(numbers)

    assert result is numbers
    assert id(numbers) == original_id
    assert numbers == [1, 3, 6, 9]
    print("Test 7 passed!")

    print("\n========== TEST 8: ALREADY SORTED ==========")
    numbers = [1, 2, 3, 4, 5]
    assert selection_sort(numbers) == [1, 2, 3, 4, 5]
    print("Test 8 passed!")

    print("\n========== ALL TESTS PASSED! ==========")


if __name__ == "__main__":
    run_tests()
