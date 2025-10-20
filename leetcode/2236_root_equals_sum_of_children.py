# Definition for a binary tree node.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val: int = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right


class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        if root and root.left and root.right:
            return root.val == root.left.val + root.right.val
        return False


if __name__ == '__main__':
    a = TreeNode(10)
    b = TreeNode(4)
    c = TreeNode(6)
    a.left = b
    a.right = c

    sol = Solution()
    assert sol.checkTree(a) == True
