class Solution:
    def removeAnagrams(self, words: list[str]) -> list[str]:
        res = set()
        for w in words:
            if ''.join(sorted(w)) not in res:
                res.add(w)
        return list(res)


if __name__ == '__main__':
    words = ['abba','baba','bbaa','cd','cd']
    sol = Solution()
    print(sol.removeAnagrams(words))
