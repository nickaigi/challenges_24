class Solution:
    def maxArea(self, height: list[int]) -> int:
        area = 0
        n = len(height)
        for i in range(n):
            for j in range(i+1, n):
                w = j - i
                diff = abs(height[i] - height[j])
                if diff > 0:
                    if height[i] > height[j]:
                        h = height[j]
                        area = max(area, (h * w))
                    else:
                        h = height[i]
                        area = max(area, (h * w))
                elif height[j] == height[i] and (height[j] !=0 or height[i] !=0):
                    area = max(area, (height[j] * w))
                else:
                    area = max(area, 0)
        return area


if __name__ == '__main__':
    sol = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(sol.maxArea(height))
    height = [1, 1]
    print(sol.maxArea(height))
    height = [0, 2]
    print(sol.maxArea(height))
