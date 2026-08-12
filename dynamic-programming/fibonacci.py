def fib_recursive(n: int) -> int:
    if n <= 1:
        return n
    return fib_recursive(n - 2) + fib_recursive(n - 1)


def fib_memo(n: int) -> int:
    """Bottom up Tabulation"""
    memo = [0] * (n + 1)

    memo[0], memo[1] = 0, 1

    for i in range(2, n + 1):
        memo[i] = memo[i - 2] + memo[i - 1]

    return memo[n]


def fib(n: int) -> int:
    a, b = 0, 1

    for i in range(n):
        a, b = b, a + b
    return a


def main():
    print(fib_memo(100))
    print(fib(100))


if __name__ == "__main__":
    main()
