class Solution:
    def minimumDeletions(self, nums: list[int]) -> int:
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        left = min(min_idx, max_idx)
        right = max(min_idx, max_idx)
        n = len(nums)

        return min(right + 1, n - left, left + 1 + n - right)


if __name__ == "__main__":
    sol = Solution()
    assert sol.minimumDeletions([2, 10, 7, 5, 4, 1, 8, 6]) == 5
    assert sol.minimumDeletions([0, -4, 19, 1, 8, -2, -3, 5]) == 3
    assert sol.minimumDeletions([101]) == 1
    print("All Tests Passed")
