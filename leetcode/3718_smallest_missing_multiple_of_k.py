class Solution:
    def missing_multiple(self, nums: list[int], k: int) -> int:
        seen = set(nums)
        ans = k

        while ans in seen:
            ans += k

        return ans


if __name__ == "__main__":
    sol = Solution()

    assert sol.missing_multiple([8, 2, 3, 4, 6], 2) == 10
    assert sol.missing_multiple([3, 29, 3, 51], 3) == 6
    print("All Tests Passed")
