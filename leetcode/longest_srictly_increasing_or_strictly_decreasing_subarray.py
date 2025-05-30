"""
3105 Longest strictly increase or strictly decreasing subarray


You are given an array of integers nums. Return the length of the longest subarray of nums which is either strictly increasing or strictly decreasing.

 

Example 1:

Input: nums = [1,4,3,3,2]

Output: 2

Explanation:

The strictly increasing subarrays of nums are [1], [2], [3], [3], [4], and [1,4].

The strictly decreasing subarrays of nums are [1], [2], [3], [3], [4], [3,2], and [4,3].

Hence, we return 2.

Example 2:

Input: nums = [3,3,3,3]

Output: 1

Explanation:

The strictly increasing subarrays of nums are [3], [3], [3], and [3].

The strictly decreasing subarrays of nums are [3], [3], [3], and [3].

Hence, we return 1.

Example 3:

Input: nums = [3,2,1]

Output: 3

Explanation:

The strictly increasing subarrays of nums are [3], [2], and [1].

The strictly decreasing subarrays of nums are [3], [2], [1], [3,2], [2,1], and [3,2,1].

Hence, we return 3.



"""
from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_length = 1
        inc_length = 1  # increasing length
        dec_length = 1  # decreasing length

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                dec_length += 1
                inc_length = 1  # reset increasing length
            elif nums[i] < nums[i - 1]:
                inc_length += 1
                dec_length = 1  # reset decreasing length
            else:
                # if elements are equal, reset both sequences
                inc_length = dec_length = 1
            # update max length considering both sequences
            max_length = max(max_length, inc_length, dec_length)
        return max_length
