class Solution:
    def pushZerosToEnd(self, arr: list[int]) -> list[int]:
        left = 0
        n = len(arr)
        for right in range(n):
            if arr[right] != 0:
                arr[right], arr[left] = arr[left], arr[right]
                left += 1
        return arr


if __name__ == "__main__":
    sol = Solution()
    arr = [1, 2, 0, 4, 3, 0, 5, 0]
    print(f"Before: {arr} -> after {sol.pushZerosToEnd(arr)}")

    arr = [10, 20, 30]
    print(f"Before: {arr} -> after {sol.pushZerosToEnd(arr)}")

    arr = [0, 0]
    print(f"Before: {arr} -> after {sol.pushZerosToEnd(arr)}")
