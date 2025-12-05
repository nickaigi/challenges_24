class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        ops = 0
        while num1 and num2:
            ops += num1 // num2
            num1 %= num2
            num1, num2 = num2, num1
        return ops


if __name__ == '__main__':
    sol = Solution()

    num1 = 2
    num2 = 3
    assert 3 == sol.countOperations(num1, num2)

    num1 = 10
    num2 = 10
    assert 1 == sol.countOperations(num1, num2)
