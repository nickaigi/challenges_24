import math


def is_prime(num: int) -> bool:
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True


if __name__ == "__main__":
    assert is_prime(11)
    assert not is_prime(12)
    print("All Tests Passed")
