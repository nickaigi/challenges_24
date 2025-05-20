from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in nums:
            heapq.heappush(heap, i)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]


if __name__ == '__main__':
    sol = Solution()
    nums = [3,2,1,5,6,4]
    k = 2
    assert sol.findKthLargest(nums, k) == 5
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    assert sol.findKthLargest(nums, k) == 4
