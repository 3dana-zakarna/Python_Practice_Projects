
def gen_parentheses(pairs):
    if not isinstance(pairs, int) or isinstance(pairs, bool):
        return 'The number of pairs should be an integer'

    if pairs < 1:
        return 'The number of pairs should be at least 1'

    queue = [('', 0, 0)]
    result = []

    while queue:
        current, opens_used, closes_used = queue.pop(0)

        if len(current) == 2 * pairs:
            result.append(current)
        else:
            if opens_used < pairs:
                queue.append((current + '(', opens_used + 1, closes_used))

            if closes_used < opens_used:
                queue.append((current + ')', opens_used, closes_used + 1))

    return result


# =========================
# TEST CASES
# =========================

def run_tests():
    print("========== TEST 1: ONE PAIR ==========")
    assert gen_parentheses(1) == ["()"]
    print("Test 1 passed!")

    print("\n========== TEST 2: TWO PAIRS ==========")
    assert gen_parentheses(2) == ["(())", "()()"]
    print("Test 2 passed!")

    print("\n========== TEST 3: THREE PAIRS ==========")
    expected3 = ["((()))", "(()())", "(())()", "()(())", "()()()"]
    assert gen_parentheses(3) == expected3
    print("Test 3 passed!")

    print("\n========== TEST 4: ZERO PAIRS ==========")
    assert gen_parentheses(0) == "The number of pairs should be at least 1"
    print("Test 4 passed!")

    print("\n========== TEST 5: NEGATIVE PAIRS ==========")
    assert gen_parentheses(-2) == "The number of pairs should be at least 1"
    print("Test 5 passed!")

    print("\n========== TEST 6: FLOAT INPUT ==========")
    assert gen_parentheses(2.5) == "The number of pairs should be an integer"
    print("Test 6 passed!")

    print("\n========== TEST 7: STRING INPUT ==========")
    assert gen_parentheses("3") == "The number of pairs should be an integer"
    print("Test 7 passed!")

    print("\n========== TEST 8: BOOLEAN INPUT ==========")
    assert gen_parentheses(True) == "The number of pairs should be an integer"
    print("Test 8 passed!")

    print("\n========== ALL TESTS PASSED! ==========")


if __name__ == "__main__":
    run_tests()
