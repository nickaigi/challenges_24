class Solution:
    def triangleNumber(self, nums: list[int]) -> int:

        def binary_search(nums: list[int], l: int, r: int, x: int) -> int:
            while r >= l and r < len(nums):
                mid = (l + r) // 2
                if nums[mid] >= x:
                    r = mid - 1
                else:
                    l = mid + 1
            return l

        count = 0
        nums.sort()
        for i in range(0, len(nums) - 2):
            k = i + 2
            j = i + 1
            while j < len(nums) - 1 and nums[i] != 0:
                k = binary_search(nums, k, len(nums) - 1, nums[i] + nums[j])
                count += k - j - 1
                j += 1
        return count
