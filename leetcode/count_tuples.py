"""
1726. Tuple with Same Product

Given an array nums of distinct positive integers, return the number of tuples (a, b, c, d) such that a * b = c * d where a, b, c, and d are elements of nums, and a != b != c != d.

Example 1:

Input: nums = [2,3,4,6]
Output: 8
Explanation: There are 8 valid tuples:
(2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
(3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)

Example 2:

Input: nums = [1,2,4,5,10]
Output: 16
Explanation: There are 16 valid tuples:
(1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
(2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
(2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,5,4)
(4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,
"""

from collections import defaultdict


def countTuples(nums):
    # Create a frequency map for all possible products of pairs
    product_count = defaultdict(int)
    n = len(nums)
    
    # Iterate through all unique pairs (a, b) where a != b
    for i in range(n):
        for j in range(i + 1, n):
            product = nums[i] * nums[j]
            product_count[product] += 1
    
    # Calculate the total number of valid tuples
    total = 0
    for count in product_count.values():
        if count >= 2:
            # For each product with at least 2 pairs, calculate the number of valid tuples
            # Each pair can be arranged in 2 ways (a,b or b,a), and there are count such pairs
            # So the total tuples for this product is count * (count - 1) * 4
            total += count * (count - 1) * 4
    
    return total


if __name__ == '__main__':
    # Example usage:
    nums1 = [2, 3, 4, 6]
    nums2 = [1, 2, 4, 5, 10]

    print(countTuples(nums1))  # Output: 8
    print(countTuples(nums2))  # Output: 16
