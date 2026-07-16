class Solution:
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x: x[0])
        res = 0
        for i in range(1, len(points)):
            res = max(res, points[i][0] - points[i - 1][0])
        return res


if __name__ == "__main__":
    sol = Solution()
    points = [[8, 7], [9, 9], [7, 4], [9, 7]]

    assert sol.maxWidthOfVerticalArea(points) == 1
    points = [[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]]
    assert sol.maxWidthOfVerticalArea(points) == 3
