class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
        return False


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    sol = Solution()
    print(sol.containsDuplicate(nums))
    nums = [1,2,3,4]
    print(sol.containsDuplicate(nums))
    nums = [1,1,1,3,3,4,3,2,4,2]
    print(sol.containsDuplicate(nums))
