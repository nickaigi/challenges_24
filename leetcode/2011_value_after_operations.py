class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        res = 0
        for op in operations:
            if op in {"++X", "X++"}:
                res += 1
            elif op in {"--X", "X--"}:
                res -= 1
        return res


if __name__ == '__main__':
    operations: list[str] = ["--X", "X++", "X++"]
    sol = Solution()
    assert sol.finalValueAfterOperations(operations) == 1
    operations = ["++X", "++X", "X++"]
    assert sol.finalValueAfterOperations(operations) == 3
