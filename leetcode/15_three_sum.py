"""
Copied from Gregg Hogg: https://youtu.be/8IjCNFIo8YI?si=yPNkVmuS83mIcR_V

Time: O(n^2)
Space: O(n)
"""
from typing import List


class Solution:

    def threeSum(self, nums: List[int]):
        data = {}  # num : idx
        n = len(nums)
        s = set()

        for i, num in enumerate(nums):
            data[num] = i

        for i in range(n):
            for j in range(i + 1, n):
                # we want
                # 0 = nums[i] + nums[j] + desired
                # OR 
                # -nums[i] - nums[j] = desired
                # desired = -nums[i] - nums[j]
                desired = -nums[i] - nums[j]
                if desired in data and data[desired] != i and data[desired] != j:
                    s.add(tuple(
                        sorted([ nums[i], nums[j], nums[desired]]))
                    )
        return s


if __name__ == '__main__':
    sol = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    res = list(sol.threeSum(nums=nums))
    print(res)
    #assert res == [[-1,-1,2],[-1,0,1]]
