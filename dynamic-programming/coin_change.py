"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:
    coins = [1, 2, 5]   amount = 11
    output: 3
    Explanation 11 = 5 + 5 + 1

Example 2:
    coins = [2]   amount = 3
    output: -1

Example 3:
    coins = [1]   amount = 0
    output: 0
"""


def coin_change_memo(coins: list[int], amount: int) -> int:
    """
    Top Down with Memoization
    Time: O(coins * amount)
    Space: O(amount)
    """
    coins.sort()
    memo: dict[int, int | float] = {0: 0}

    def min_coin(amt) -> int | float:
        if amt in memo:
            return memo[amt]

        min_ = float("inf")
        for coin in coins:
            diff = amt - coin
            if diff < 0:
                break
            min_ = min(min_, 1 + min_coin(diff))

        memo[amt] = min_
        return min_

    result = min_coin(amount)
    if result < float("inf"):
        return result  # type: ignore
    else:
        return -1


def coin_change(coins: list[int], amount: int) -> int:
    coins.sort()
    dp: list[int | float] = [0] * (amount + 1)
    for i in range(1, amount + 1):
        min_ = float("inf")
        for coin in coins:
            diff = i - coin
            if diff < 0:
                break
            min_ = min(min_, dp[diff] + 1)
        dp[i] = min_

    if dp[amount] < float("inf"):
        return dp[amount]  # type: ignore
    else:
        return -1


def coin_change_dp(coins: list[int], amount: int) -> int:
    dp = [amount + 1] * (amount + 1)

    # base case: 0 coins are needed to make an amount of 0
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], 1 + dp[i - coin])
    return dp[amount] if dp[amount] != amount + 1 else -1


def coin_change_greedy(coins: list[int], amount: int) -> int:
    """
    Fails these tests:
        assert coin_change_greedy([1, 21, 25], 63) == 3
        assert coin_chagreedy_sol([1, 5, 21, 25], 63) == 3
    correct answer should be 3, using three 21 cent coins
    """
    num_coins = 0
    coins.sort()
    coins.reverse()

    for c in coins:
        num_coins = num_coins + (amount // c)
        amount = amount % c
    return num_coins


if __name__ == "__main__":
    assert coin_change([1, 2, 5], 11) == 3
    assert coin_change([1, 5, 10, 25], 63) == 6
    assert coin_change([1, 21, 25], 63) == 3
    assert coin_change([1, 5, 21, 25], 63) == 3
    assert coin_change([1], 0) == 0
    print("All Tests passed")
