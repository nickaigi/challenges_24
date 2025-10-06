from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams_dict =  defaultdict(list) # mapping charCount to list of anagrams
        for s in strs:
            count = [0] * 26   # a ... z
            for c in s:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            anagrams_dict[key].append(s)

        return list(anagrams_dict.values())
