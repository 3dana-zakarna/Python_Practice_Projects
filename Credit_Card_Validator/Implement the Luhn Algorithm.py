
def verify_card_number(card_number):
    # Remove spaces and dashes
    card_number = card_number.replace(" ", "").replace("-", "")

    # Check that the input contains only digits
    if not card_number or not card_number.isdigit():
        return "INVALID!"

    # Convert the string into a list of integers
    digits = [int(digit) for digit in card_number]

    # Starting from the right, double every other digit,
    # excluding the rightmost check digit
    for i in range(len(digits) - 2, -1, -2):
        digits[i] *= 2

        # Subtract 9 if the result is greater than 9
        if digits[i] > 9:
            digits[i] -= 9

    # Sum all digits and check whether the total is divisible by 10
    if sum(digits) % 10 == 0:
        return "VALID!"

    return "INVALID!"


# =========================
# TEST CASES
# =========================

def run_tests():
    print("========== TEST 1: VALID NUMBER ==========")
    assert verify_card_number("453914889") == "VALID!"
    print("Test 1 passed!")

    print("\n========== TEST 2: VALID NUMBER WITH DASHES ==========")
    assert verify_card_number("4111-1111-1111-1111") == "VALID!"
    print("Test 2 passed!")

    print("\n========== TEST 3: INVALID NUMBER ==========")
    assert verify_card_number("453914881") == "INVALID!"
    print("Test 3 passed!")

    print("\n========== TEST 4: NUMBER WITH SPACES ==========")
    assert verify_card_number("1234 5678 9012 3456") == "INVALID!"
    print("Test 4 passed!")

    print("\n========== TEST 5: VALID NUMBER WITH SPACES ==========")
    assert verify_card_number("4111 1111 1111 1111") == "VALID!"
    print("Test 5 passed!")

    print("\n========== TEST 6: EMPTY INPUT ==========")
    assert verify_card_number("") == "INVALID!"
    print("Test 6 passed!")

    print("\n========== TEST 7: NON-DIGIT CHARACTERS ==========")
    assert verify_card_number("abcd1234") == "INVALID!"
    print("Test 7 passed!")

    print("\n========== TEST 8: DISPLAY RESULTS ==========")
    print("453914889:", verify_card_number("453914889"))
    print("4111-1111-1111-1111:",
          verify_card_number("4111-1111-1111-1111"))
    print("1234 5678 9012 3456:",
          verify_card_number("1234 5678 9012 3456"))

    print("\n========== ALL TESTS PASSED! ==========")


if __name__ == "__main__":
    run_tests()
