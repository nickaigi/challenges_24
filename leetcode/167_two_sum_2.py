class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            s = numbers[left] + numbers[right]
            if s == target:
                return [left + 1, right + 1]
            if s < target:
                left += 1
            elif s > target:
                right -= 1
        return [-1, -1]


if __name__ == '__main__':
    numbers = [2, 7, 11, 15]
    target = 9
    sol = Solution()
    assert sol.twoSum(numbers, target) == [1, 2]
    numbers = [2, 3, 4]
    target = 6
    assert sol.twoSum(numbers, target) == [1, 3]
    numbers = [-1, 0]
    target = -1
    assert sol.twoSum(numbers, target) == [1, 2]
