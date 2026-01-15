class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        left = 0
        for right in range(n):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1


if __name__ == "__main__":
    sol = Solution()
    nums = [0, 1, 0, 3, 12]
    sol.moveZeroes(nums)
    assert [1, 3, 12, 0, 0] == nums
