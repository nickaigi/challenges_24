class Solution:
    def hasIncreasingSubarrays(self, nums: list[int], k: int) -> bool:
        n = len(nums)
        current, prev_current, ans = 1, 0, 0
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                current += 1
            else:
                prev_current, current = current, 1
            ans = max(ans, min(prev_current, current))
            ans = max(ans, current // 2)
        return ans >= k


if __name__ == '__main__':
    nums = [2, 5, 7, 8, 9, 2, 3, 4, 3, 1]
    k = 3

    sol = Solution()
    assert sol.hasIncreasingSubarrays(nums, k) == True
