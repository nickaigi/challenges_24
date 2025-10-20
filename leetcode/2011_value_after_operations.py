class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        return sum(1 if op[1] == '+' else -1 for op in operations)


if __name__ == '__main__':
    operations: list[str] = ["--X", "X++", "X++"]
    sol = Solution()
    assert sol.finalValueAfterOperations(operations) == 1
    operations = ["++X", "++X", "X++"]
    assert sol.finalValueAfterOperations(operations) == 3
