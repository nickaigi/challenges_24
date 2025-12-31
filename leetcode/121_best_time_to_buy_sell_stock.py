from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        price_to_buy = float("inf")
        max_profit = 0.0
        for price in prices:
            if price < price_to_buy:
                price_to_buy = price
            else:
                max_profit = max(max_profit, price - price_to_buy)
        return int(max_profit)
