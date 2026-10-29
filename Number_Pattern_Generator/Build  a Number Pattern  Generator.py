
def number_pattern(n):
    if not isinstance(n, int) or isinstance(n, bool):
        return "Argument must be an integer value."

    if n < 1:
        return "Argument must be an integer greater than 0."

    pattern = ""
    for i in range(1, n + 1):
        if i > 1:
            pattern += " "
        pattern += str(i)

    return pattern
print(number_pattern(4))


print(number_pattern(12))


print(number_pattern(0))


print(number_pattern(3.5))
