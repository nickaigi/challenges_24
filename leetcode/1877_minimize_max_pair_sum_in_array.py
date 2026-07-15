class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        nums.sort()
        max_sum = 0
        for i in range(len(nums) // 2):  # we only need to go to the middle of the list
            max_sum = max(max_sum, nums[i] + nums[len(nums) - 1 - i])
        return max_sum


if __name__ == "__main__":
    sol = Solution()
    nums = [3, 5, 2, 3]
    assert sol.minPairSum(nums) == 7
    nums = [3, 5, 4, 2, 4, 6]
    assert sol.minPairSum(nums) == 8
