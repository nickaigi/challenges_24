class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix)  # rows
        n = len(matrix[0])  # cols
        t = m * n  # total number of elements in matrix

        l = 0  # left
        r = t - 1  # right

        while l <= r:
            m = (l + r) // 2
            i = m // n  # row
            j = m % n  # col

            mid_num = matrix[i][j] 

            if target == mid_num:
                return True
            elif target < mid_num:
                r = m - 1
            else:
                l = m + 1

        return False
