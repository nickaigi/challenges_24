class Solution:
    def hasIncreasingSubarrays(self, nums: list[int], k: int) -> bool:
        return False


if __name__ == '__main__':
    nums = [2, 5, 7, 8, 9, 2, 3, 4, 3, 1]
    k = 3

    sol = Solution()
    assert sol.hasIncreasingSubarrays(nums, k) == True
