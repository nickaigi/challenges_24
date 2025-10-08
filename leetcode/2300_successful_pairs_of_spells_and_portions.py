class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        """
        O(nlogm + mlogm)
        Sort potions and Binary search
        """
        potions.sort()
        res = []

        for s in spells:
            # bin search
            l, r = 0, len(potions) - 1
            idx = len(potions) # find weakest potion that works

            while l <= r:
                mid = (l + r) // 2
                if s * potions[mid] >= success:
                    r = mid - 1
                    idx = mid
                else:
                    l = mid + 1
            res.append(len(potions) - idx)

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
