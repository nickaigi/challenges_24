class Solution:
    def subarraysum(self, nums: list[int], k: int) -> int:
        count = 0
        curr_sum = 0
        prefix_sums = {0: 1}

        for num in nums:
            curr_sum += num
            diff = curr_sum - k

            count += prefix_sums.get(diff, 0)
            prefix_sums[curr_sum] = 1 + prefix_sums.get(curr_sum, 0)
        return count

    def subarraysum_brute_force(self, nums: list[int], k: int) -> int:
        """
        Brute Force, O(n^2)
        """
        count = 0
        for i in range(len(nums)):
            curr_sum = 0
            for j in range(i, len(nums)):
                curr_sum += nums[j]
                if curr_sum == k:
                    count += 1
        return count


if __name__ == "__main__":
    sol = Solution()
    assert sol.subarraysum([1, 1, 1], 2) == 2
    assert sol.subarraysum([1, 2, 3], 3) == 2
    print("All Tests Passed")
