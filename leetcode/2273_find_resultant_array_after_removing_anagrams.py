class Solution:
    def removeAnagrams(self, words: list[str]) -> list[str]:
        res = [words[0]]
        n = len(words)

        def compare(word1: str, word2: str) -> bool:
            freq = [0] * 26
            for ch in word1:
                freq[ord(ch) - ord('a')] += 1

            for ch in word2:
                freq[ord(ch) - ord('a')] -= 1
            return all(x == 0 for x in freq)

        for i in range(1, n):
            if compare(words[i], words[i-1]):
                continue
            res.append(words[i])
        return res


if __name__ == '__main__':
    words = ['abba','baba','bbaa','cd','cd']
    sol = Solution()
    print(sol.removeAnagrams(words))
