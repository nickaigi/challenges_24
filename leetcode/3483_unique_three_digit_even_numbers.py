class Solution:
    def totalNumbers(self, digits: list[int]) -> int:
        n = len(digits)
        visited = [False] * 1000
        count = 0

        for i in range(n):
            if digits[i] == 0:
                continue
            for j in range(n):
                if j == i:
                    continue
                for k in range(n):
                    if k == i or k == j or digits[k] % 2 != 0:
                        continue
                    num = digits[i] * 100 + digits[j] * 10 + digits[k]
                    if not visited[num]:
                        visited[num] = True
                        count += 1
        return count


if __name__ == "__main__":
    sol = Solution()
    assert sol.totalNumbers([1, 2, 3, 4]) == 12
    assert sol.totalNumbers([0, 2, 2]) == 2
    assert sol.totalNumbers([6, 6, 6]) == 1
    print("All tests passed")
