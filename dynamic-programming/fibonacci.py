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
    r0, r1 = 0, 1
    res = -1

    for i in range(2, n + 1):
        res = r0 + r1
        r0, r1 = r1, res

    return res


def main():
    print(fib_memo(10))
    print(fib(10))


if __name__ == "__main__":
    main()
