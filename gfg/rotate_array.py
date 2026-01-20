class Solution:
    # Function to rotate an array by d elements in counter-clockwise direction.
    def rotateArr_one(self, arr: list[int], d: int) -> None:
        """
        Brute force approach
        """
        n = len(arr)
        for _ in range(d):
            temp = arr[0]
            for j in range(1, n):
                arr[j - 1] = arr[j]
            arr[n - 1] = temp
        print(arr)


if __name__ == "__main__":
    sol = Solution()
    arr = [1, 2, 3, 4, 5]
    d = 2
    print(arr)
    sol.rotateArr_one(arr, d)
    assert arr == [3, 4, 5, 1, 2]
