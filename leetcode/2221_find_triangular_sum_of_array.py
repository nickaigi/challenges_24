class Solution:
    def triangularSum(self, nums: list[int]) -> int:
        while len(nums) > 1:
            new_nums = []
            for i in range(len(nums) - 1):
                new_nums.append((nums[i] + nums[i + 1]) % 10)
            nums = new_nums
        return nums[0]


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    print(Solution().triangularSum(nums=nums))
