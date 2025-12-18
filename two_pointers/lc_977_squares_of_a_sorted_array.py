"""
Given an integer array nums sorted in non-decreasing order return an array of
the squares of each number in non-decreasing order

Example 1:
input: nums = [-4, -10, 0, 3, 10]
output: [0, 1, 9, 16, 100]

Explanation: After squaring, the array becomes [16, 1, 0, 9, 100]
After sorting, it becomes [0, 1, 9, 16, 100]
"""

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        left = 0
        right = len(nums) - 1
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                res.append(nums[left] ** 2)
                left += 1
            else:
                res.append(nums[right] ** 2)
                right -= 1
        res.reverse()  # reverse inplace
        return res


if __name__ == "__main__":
    sol = Solution()
    nums: List[int] = [-4, -1, 0, 3, 10]
    ans = sol.sortedSquares(nums)
    assert [0, 1, 9, 16, 100] == ans
