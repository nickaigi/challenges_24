class Solution:
    def minElement(self, nums: list[int]) -> int:
        ans = 37  # every element in nums is at most 10^4 so 36 = 4 * 9
        for num in nums:
            dig = 0
            while num > 0:
                dig += num % 10
                num //= 10
            ans = min(ans, dig)
        return ans


if __name__ == "__main__":
    sol = Solution()
    nums = [10, 12, 13, 14]
    assert sol.minElement(nums) == 1

    nums = [1, 2, 3, 4]
    assert sol.minElement(nums) == 1

    nums = [999, 19, 199]
    assert sol.minElement(nums) == 10
    print("All Tests Passed")
