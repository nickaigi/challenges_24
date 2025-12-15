from typing import List


class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        res = 1
        prev = 1
        for i in range(1, n):
            if prices[i] == prices[i - 1] - 1:
                prev += 1
            else:
                prev = 1
            res += prev
        return res


if __name__ == '__main__':
    sol = Solution()

    prices: List[int] = [3, 2, 1, 4]
    assert 7 == sol.getDescentPeriods(prices)

    prices = [8, 6, 7, 7]
    assert 4 == sol.getDescentPeriods(prices)

    prices = [1]
    assert 1 == sol.getDescentPeriods(prices)
