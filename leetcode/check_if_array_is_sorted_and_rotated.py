"""
1752. Check if Array Is Sorted and Rotated


Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

There may be duplicates in the original array.

Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: true
Explanation: [1,2,3,4,5] is the original sorted array.
You can rotate the array by x = 3 positions to begin on the the element of value 3: [3,4,5,1,2].
Example 2:

Input: nums = [2,1,3,4]
Output: false
Explanation: There is no sorted array once rotated that can make nums.
Example 3:

Input: nums = [1,2,3]
Output: true
Explanation: [1,2,3] is the original sorted array.
You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.
"""


def check(nums):
    n = len(nums)
    count = 0
    
    # Traverse the array to count the number of places where nums[i] > nums[i+1]
    for i in range(n - 1):
        if nums[i] > nums[i + 1]:
            count += 1
            if count > 1:
                return False
    
    # If no rotation point, it's already sorted
    if count == 0:
        return True
    
    # Check if the array is sorted when rotated at the identified point
    # The last element should be less than or equal to the first element
    return nums[-1] <= nums[0]

if __name__ == '__main__':
    # Test cases
    print(check([3, 4, 5, 1, 2]))  # Output: True
    print(check([2, 1, 3, 4]))      # Output: False
    print(check([1, 2, 3]))         # Output: True
    print(check([1, 1, 1]))         # Output: True
    print(check([1, 3, 2]))         # Output: False
