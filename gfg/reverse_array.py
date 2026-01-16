class Solution:
    def reverseArray(self, arr: list[int]) -> None:
        # code here
        n = len(arr)
        left, right = 0, n - 1
        while left < right:
            arr[right], arr[left] = arr[left], arr[right]
            left += 1
            right -= 1


if __name__ == "__main__":
    sol = Solution()
    arr = [1, 4, 3, 2, 6, 5]
    sol.reverseArray(arr)
    assert [5, 6, 2, 3, 4, 1] == arr

    arr = [4, 5, 2]
    sol.reverseArray(arr)
    assert [2, 5, 4] == arr

    arr = [1]
    sol.reverseArray(arr)
    assert [1] == arr
