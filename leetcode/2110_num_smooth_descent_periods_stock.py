from typing import List


class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        res = 0
        n = len(prices)
        for i in range(n):
            res += 1
            j = i + 1
            while j < n:
                if prices[j - 1] - prices[j] == 1:
                    res += 1
                    j += 1
                else:
                    break
        return res


if __name__ == '__main__':
    sol = Solution()

    prices: List[int] = [3, 2, 1, 4]
    assert 7 == sol.getDescentPeriods(prices)

    prices = [8, 6, 7, 7]
    assert 4 == sol.getDescentPeriods(prices)

    prices = [1]
    assert 1 == sol.getDescentPeriods(prices)
