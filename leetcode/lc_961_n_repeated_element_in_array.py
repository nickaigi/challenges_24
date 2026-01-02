from typing import List
from collections import Counter


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        data = Counter(nums)
        for k in data:
            if data[k] > 1:
                return k
