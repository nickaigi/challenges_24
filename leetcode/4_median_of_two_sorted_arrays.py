class Solution:
    def findMedianSortedArrays_one(self, nums1: list[int], nums2: list[int]) -> float:
        """
        Time complexity:
            O((m + n)log(m + n))
        Does not meet the requirment of O(log(m + n))
        """
        merged = sorted(nums1 + nums2)
        length = len(merged)

        # check if the length is even or odd
        if length % 2 == 0:
            # if even, return the average of the two middle elements
            return (merged[(length // 2) - 1] + merged[(length // 2)]) / 2
        # if odd, return the middle element
        return merged[length // 2]


if __name__ == "__main__":
    sol = Solution()

    assert sol.findMedianSortedArrays_one([1, 3], [2]) == 2
    assert sol.findMedianSortedArrays_one([1, 2], [3, 4]) == 2.5
    print("All Tests Passed")
