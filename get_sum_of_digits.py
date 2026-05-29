def sum_of_digits(num: int) -> int:
    total = 0
    while num != 0:
        temp = divmod(num, 10)  # (num//10, num % 10)
        digit = temp[1]
        total += digit
        num = temp[0]
    return total


if __name__ == "__main__":
    assert sum_of_digits(183) == 12
    assert sum_of_digits(11) == 2
    assert sum_of_digits(100) == 1
    assert sum_of_digits(123) == 6
    print("All Tests Passed")
