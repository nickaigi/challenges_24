"""
Given an m x n matrix, return all elements of the matrix in spiral order.
"""


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        m, n = len(matrix), len(matrix[0])
        ans: list[int] = []
        return ans


if __name__ == "__main__":
    sol = Solution()
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    assert sol.spiralOrder(matrix) == [1, 2, 3, 6, 9, 8, 7, 4, 5]

    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]

    assert sol.spiralOrder(matrix) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    print("All Tests Passed")
