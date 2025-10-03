
class Solution:
    def maxArea(self, height: list[int]) -> int:
        area = 1
        n = len(height)
        for i in range(n):
            for j in range(i+1, n):
                w = j - i
                diff = abs(height[i] - height[j])
                if diff > 0:
                    if height[i] > height[j]:
                        h = height[i] - height[j]
                        area = max(area, (h * w))
                    else:
                        h = height[j] - height[i]
                        area = max(area, (h * w))
        return area


if __name__ == '__main__':
    sol = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(sol.maxArea(height))
    height = [1, 1]
    print(sol.maxArea(height))
