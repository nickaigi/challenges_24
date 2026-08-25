class Solution:
    def merge(self, intervals: list[list[int]]) -> list[int]:
        """
        Time: O(n log n) because sorting is n log n
        Space: O(log n)
        """
        merged = []
        intervals.sort(key=lambda x: x[0])

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged


if __name__ == "__main__":
    sol = Solution()
    data = [
        [1, 3],
        [2, 6],
        [8, 10],
        [15, 18],
    ]
    assert sol.merge(data) == [[1, 6], [8, 10], [15, 18]]
    assert sol.merge([[1, 4], [4, 5]]) == [[1, 5]]
    assert sol.merge([[4, 7], [1, 4]]) == [[1, 7]]
    print("All Tests Passed")
