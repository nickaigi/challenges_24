class Solution:
    def search(self, nums: list[int], target: int) -> int:
        arr = sorted(nums)
        n = len(arr)
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return nums.index(arr[mid])
            if arr[mid] < target:
                left = mid + 1
            elif arr[mid] > target:
                right = mid - 1
        return -1


if __name__ == "__main__":
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0

    sol = Solution()

    assert sol.search(nums, target) == 4
    print("All Tests Passed")
