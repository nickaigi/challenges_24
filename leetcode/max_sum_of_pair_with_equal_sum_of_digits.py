"""
2342. Max Sum of a pair with equal sum of digits

You are given a 0-indexed array nums consisting of positive integers. You can choose two indices i and j, such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].

Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the conditions.


Example 1:

Input: nums = [18,43,36,13,7]
Output: 54
Explanation: The pairs (i, j) that satisfy the conditions are:
- (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
- (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.
So the maximum sum that we can obtain is 54.

Example 2:

Input: nums = [10,12,19,14]
Output: -1
Explanation: There are no two numbers that satisfy the conditions, so we return -1.


failing test:
input: nums = [279,169,463,252,94,455,423,315,288,64,494,337,409,283,283,477,248,8,89,166,188,186,128]

Output: 765  <--- wrong
Expected: 872

"""

from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        sums = {}
        max_sum = -1
        for i in range(len(nums)):
            sum_digits = 0
            for char in str(nums[i]):
                sum_digits += int(char)
            
            print(sum_digits)
            if sum_digits in sums:
                total = nums[i] + nums[sums[sum_digits]]
                if total > max_sum:
                    max_sum = total
            
            sums[sum_digits] = i
        return max_sum


if __name__ == '__main__':
    sol = Solution()
    nums = [279,169,463,252,94,455,423,315,288,64,494,337,409,283,283,477,248,8,89,166,188,186,128]

    assert sol.maximumSum(nums) == 872 
