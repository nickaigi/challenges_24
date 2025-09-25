class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        """
        Find the minimum path sum from top to bottom of a triangle.
        Each step can move to adjacent numbers on the row below.

        Args:
            triangle: A triangle array where triangle[i][j] represents
                the element at row i and position j
        Returns:
            the minimum path sum from top to bottom
        """
        # Get the number of rows in the triangle
        num_rows = len(triangle)

        # initialize DP table with dimensions (num_rows + 1) x (num_rows + 1)
        # dp[i][j] represents the minimum path sum from position (i, j) to the bottom
        # Extra row and column are added to handle boundary cases
        dp = [[0] * (num_rows + 1) for _ in range(num_rows + 1)]

        # build the DP table from bottom to top
        # start from the second-to-last row and move upward
        for row in range(num_rows -1, -1, -1):
            # for each position in the current row
            for col in range(row + 1):
                # calculate minimum path sum from current position
                # chose the minimum between going down-left or down-right
                # add the current element's value to the minimum path sum below
                dp[row][col] = min(dp[row + 1][col], dp[row + 1][col + 1]) + triangle[row][col]
        # the top element contains the minimum path sum for the entire triangle
        return dp[0][0]
