class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        cur = str(n)

        while cur not in seen:
            seen.add(cur)
            summ = 0
            for digit in cur:
                digit = int(digit)
                summ += digit**2

            if summ == 1:
                return True
            cur = str(summ)
        return False


if __name__ == "__main__":
    sol = Solution()
    n = 19
    assert sol.isHappy(n) is True
