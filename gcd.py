# Given two positive integers a and b, find the GCD of the two numbers

def gcd(a: int, b: int) -> int:
    if a == 0:
        return b
    if b == 0:
        return a

    # base case
    if a == b:
        return a

    if a > b:
        return gcd(a - b, b)
    return gcd(b - a, a)


if __name__ == '__main__':
    a, b = 36, 60

    print(f'The GCD({a}, {b}) is {gcd(a, b)}')
