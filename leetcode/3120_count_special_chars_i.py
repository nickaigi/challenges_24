class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count = 0
        seen = set(word)

        for i in range(26):
            c = chr(i + ord("a"))
            if c in seen and c.upper() in seen:
                count += 1
        return count


if __name__ == "__main__":
    sol = Solution()
    word = "aaAbcBC"
    assert sol.numberOfSpecialChars(word) == 3

    word = "abBCab"
    assert sol.numberOfSpecialChars(word) == 1
    print("All Tests Passed")
