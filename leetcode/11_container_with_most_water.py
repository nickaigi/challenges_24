class Solution:
    def maxArea(self, height: list[int]) -> int:
        area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            area = max(area, (right - left) * min(height[left], height[right]))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return area


if __name__ == '__main__':
    sol = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(sol.maxArea(height))
    height = [1, 1]
    print(sol.maxArea(height))
    height = [0, 2]
    print(sol.maxArea(height))
