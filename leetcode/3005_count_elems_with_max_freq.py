class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        freqs = {}
        for num in nums:
            if num in freqs:
                freqs[num] += 1
            else:
                freqs[num] = 1

        max_freq = 0
        for freq in freqs.values():
            max_freq = max(max_freq, freq)

        freq_of_max_freq = 0
        for freq in freqs.values():
            if freq == max_freq:
                freq_of_max_freq += 1

        return freq_of_max_freq * max_freq
