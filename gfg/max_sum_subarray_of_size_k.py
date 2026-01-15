class Solution:
    def maxSubarraySum(self, arr: list[int], k: int) -> float:
        max_sum = float("-inf")
        n = len(arr)
        left = 0
        right = k
        while right <= n:
            tot_sum = sum(arr[left:right])
            max_sum = max(max_sum, tot_sum)
            left = left + 1
            right = right + 1
        return max_sum


if __name__ == "__main__":
    sol = Solution()
    arr = [100, 200, 300, 400]
    k = 2
    assert sol.maxSubarraySum(arr, k) == 700
