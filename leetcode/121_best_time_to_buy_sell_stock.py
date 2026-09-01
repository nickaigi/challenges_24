class Solution:
    def maxProfit_bruteforce(self, prices: list[int]) -> int:
        """
        Time: O(n^2)
        Space: O(1)
        """
        max_profit = float("-inf")
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]

                if profit > 0:
                    max_profit = max(max_profit, profit)
        return int(max_profit if max_profit > float("-inf") else 0)

    def maxProfit(self, prices: list[int]) -> int:
        min_price = float("inf")
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price

            profit = price - min_price

            if profit > max_profit:
                max_profit = profit

        return max_profit
