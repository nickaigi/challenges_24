"""
322. Coin Change


You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:

Input: coins = [2], amount = 3
Output: -1

Example 3:

Input: coins = [1], amount = 0
Output: 0
"""

def coin_change(coins: list[int], amount: int) -> int | float:
    # Top Down DP (Memoization)
    # Time: O(coins * amount)
    # Space: O(amount)

    coins.sort()
    memo = {0: 0}

    def min_coins(amt):
        if amt in memo:
            return memo[amt]
        minn = float('inf')  # inifinity
        for coin in coins:
            diff = amt - coin
            if diff < 0:
                # since our coins are sorted in ascending order, there is no
                # need to continue iterating over the coins sinc ethe diff will
                # continue getting larger.
                break
            minn = min(minn, 1 + min_coins(diff))
        memo[amt] = minn
        return minn

    result = min_coins(amount)
    if result < float('inf'):
        return result
    else:
        return -1


if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 11
    assert coin_change(coins=coins, amount=amount) == 3

    coins = [2]
    amount = 3
    assert coin_change(coins=coins, amount=amount) == -1

    coins = [1]
    amount = 0
    assert coin_change(coins=coins, amount=amount) == 0
