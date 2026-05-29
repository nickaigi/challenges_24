def reverse_digits(num: int) -> int:
    result = 0
    while num != 0:
        temp = divmod(num, 10)  # (num // 10, num % 10)
        digit = temp[1]
        result = (result * 10) + digit
        num = temp[0]
    return result


if __name__ == "__main__":
    assert reverse_digits(183) == 381
    print("All Tests Passed")
