
def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    if square_target < 0:
        raise ValueError(
            "Square root of negative number is not defined in real numbers"
        )

    if square_target == 0 or square_target == 1:
        print(f"The square root of {square_target} is {square_target}")
        return square_target

    low = 0
    high = max(1, square_target)

    for _ in range(max_iterations):
        midpoint = (low + high) / 2

        if high - low <= tolerance:
            print(
                f"The square root of {square_target} is approximately {midpoint}"
            )
            return midpoint

        if midpoint * midpoint < square_target:
            low = midpoint
        else:
            high = midpoint

    print(f"Failed to converge within {max_iterations} iterations")
    return None


# =========================
# TEST CASES
# =========================

def run_tests():
    print("TEST 1: ZERO")
    assert square_root_bisection(0) == 0

    print("\nTEST 2: ONE")
    assert square_root_bisection(1) == 1

    print("\nTEST 3: SMALL DECIMAL")
    result = square_root_bisection(0.001, 1e-7, 50)
    assert 0.03162267660168379 <= result <= 0.031622876601683794

    print("\nTEST 4: 0.25")
    result = square_root_bisection(0.25, 1e-7, 50)
    assert 0.4999999 <= result <= 0.5000001

    print("\nTEST 5: 81")
    result = square_root_bisection(81, 1e-3, 50)
    assert 8.999 <= result <= 9.001

    print("\nTEST 6: 225 WITH TOLERANCE 1e-3")
    result = square_root_bisection(225, 1e-3, 100)
    assert 14.999 <= result <= 15.001

    print("\nTEST 7: 225 WITH TOLERANCE 1e-5")
    result = square_root_bisection(225, 1e-5, 100)
    assert 14.99999 <= result <= 15.00001

    print("\nTEST 8: 225 WITH TOLERANCE 1e-7")
    result = square_root_bisection(225, 1e-7, 100)
    assert 14.9999999 <= result <= 15.0000001

    print("\nTEST 9: NEGATIVE NUMBER")
    try:
        square_root_bisection(-4)
        assert False, "Expected ValueError"
    except ValueError as error:
        assert str(error) == (
            "Square root of negative number is not defined in real numbers"
        )
        print("Negative number test passed!")

    print("\nTEST 10: FAILURE TO CONVERGE")
    result = square_root_bisection(225, 1e-7, 10)
    assert result is None

    print("\nALL TESTS PASSED!")


if __name__ == "__main__":
    run_tests()

