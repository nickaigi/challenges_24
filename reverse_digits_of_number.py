def reverse_digits(num: int) -> int:
    result = 0
    while num != 0:
        digit = num % 10  # grab the last digit
        num = num // 10  # chop off the last digit
        result = (result * 10) + digit
    return result


if __name__ == "__main__":
    assert reverse_digits(183) == 381
    assert reverse_digits(6789) == 9876
    print("All Tests Passed")
