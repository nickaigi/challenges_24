class Solution:
    def countCommas(self, n: int) -> int:
        return max(n - 999, 0)


if __name__ == "__main__":
    sol = Solution()
    assert sol.countCommas(1002) == 3
    assert sol.countCommas(998) == 0
