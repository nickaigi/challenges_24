class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        pref = strs[0]
        pref_len = len(pref)

        for s in strs[1:]:
            while pref != s[0:pref_len]:
                pref_len -= 1
                if pref_len == 0:
                    return ""
                pref = pref[0:pref_len]
        return pref


if __name__ == "__main__":
    sol = Solution()
    words = ["flower", "flow", "flight"]
    assert sol.longestCommonPrefix(words) == "fl"
    print("All Tests Passed")
