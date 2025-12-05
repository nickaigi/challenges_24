class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        return len(nums) - 1 if total_sum % 2 == 0 else 0



if __name__ == "__main__":
    sol = Solution()
    nums = [10, 10, 3, 7, 6]
    assert 4 == sol.countPartitions(nums)
    nums = [1, 2, 2]
    assert 0 == sol.countPartitions(nums)
    nums = [2, 4, 6, 8]
    assert 3 == sol.countPartitions(nums)
