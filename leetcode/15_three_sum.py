class Solution:
    def threeSum(self, nums: list[int]):
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    res.append([
                        nums[i], nums[j], nums[k]
                    ])
                    j += 1

                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
        return res


if __name__ == '__main__':
    sol = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    res = list(sol.threeSum(nums=nums))
    print(res)
    #assert res == [[-1,-1,2],[-1,0,1]]
