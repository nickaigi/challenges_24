class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        res = []
        for i in spells:
            count = 0
            for p in potions:
                if i * p >= success:
                    count += 1
            res.append(count)
        return res


if __name__ == '__main__':
    sol = Solution()
    spells = [5, 1, 3]
    potions = [1, 2, 3, 4, 5]
    success = 7
    ans = sol.successfulPairs(spells, potions, success)
    print(f'Answer: {ans=}')
    assert ans == [4, 0, 3]

    spells = [3, 1, 2]
    potions = [8, 5, 8]
    success = 16
    ans = sol.successfulPairs(spells, potions, success)
    print(f'Answer: {ans=}')
    assert ans == [2, 0, 2]
