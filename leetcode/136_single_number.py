from typing import List
from collections import Counter


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_map = Counter(nums)  # {Num: Frequency}
        for k in hash_map:
            if hash_map[k] == 1:
                return k
