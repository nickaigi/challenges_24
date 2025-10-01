class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        longest = 0

        for n in num_set:
            if (n - 1) not in num_set:
                # we are at a number that starts a sequence
                len = 1
                while (n + len) in num_set:
                    len += 1
                longest = max(len, longest)
        return longest


if __name__ == '__main__':
    nums = [100,4,200,1,3,2]
    print(Solution().longestConsecutive(nums))
