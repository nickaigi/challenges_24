from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        ans = 0
        max_sum = float("-inf")
        level = 0
        queue = deque([root])
        while queue:
            level += 1
            sum_at_current_level = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    sum_at_current_level += node.val

                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            if max_sum < sum_at_current_level:
                max_sum = sum_at_current_level
                ans = level
        return ans
