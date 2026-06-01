def sum_of_digits(num: int) -> int:
    total = 0
    while num != 0:
        digit = num % 10  # grab the last digit
        num = num // 10  # chop the last digit
        total += digit
    return total


if __name__ == "__main__":
    assert sum_of_digits(183) == 12
    assert sum_of_digits(11) == 2
    assert sum_of_digits(100) == 1
    assert sum_of_digits(123) == 6
    print("All Tests Passed")
