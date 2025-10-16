"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
The remaining elements of nums are not important as well as the size of nums.

Return k.
"""

from typing import List


class Solution:
    def removeElement_old(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

    def removeElement(self, nums: List[int], val: int) -> int:
        # T O(n)
        # space O(1)
        i = 0
        n = len(nums)

        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]
            else:
                i += 1
        return n


if __name__ == '__main__':
    sol = Solution()
    nums = [3, 2, 2, 3]
    val = 3
    assert sol.removeElement(nums, val) == 2
