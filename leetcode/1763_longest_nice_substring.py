class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return ""

        res = ""
        for i in range(n):
            lower_set = set()
            upper_set = set()

            for j in range(i, n):
                curr = s[j]
                if curr.islower():
                    lower_set.add(curr)
                else:
                    upper_set.add(curr)

                nice = True

                for c in lower_set:
                    if c.upper() not in upper_set:
                        nice = False
                        break
                for c in upper_set:
                    if c.lower() not in lower_set:
                        nice = False
                        break
                if nice and (j - i + 1) > len(res):
                    res = s[i : j + 1]

        return res


if __name__ == "__main__":
    sol = Solution()
    assert sol.longestNiceSubstring("YazaAay") == "aAa"
    assert sol.longestNiceSubstring("Bb") == "Bb"
    assert sol.longestNiceSubstring("c") == ""
    print("All Tests Passed")
