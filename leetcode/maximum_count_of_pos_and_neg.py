from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg, pos = 0, 0
        for i in nums:
            if i < 0:
                neg += 1
            elif i > 0:
                pos += 1
        return max(neg, pos)


if __name__ == '__main__':
    sol = Solution()
    nums_one = [-2, -1, -1, 1, 2, 3]
    nums_two = [-3, -2, -1, 0, 0, 1, 2]
    nums_three = [5, 20, 66, 1314]

    assert sol.maximumCount(nums_one) == 3
    assert sol.maximumCount(nums_two) == 3
    assert sol.maximumCount(nums_three) == 3
