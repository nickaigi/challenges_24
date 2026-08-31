# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        def check(r1: TreeNode | None, r2: TreeNode | None):
            if not r1 and not r2:
                return True

            if not r1 or not r2:
                return False

            if r1.val != r2.val:
                return False
            return check(r1.left, r2.left) and check(r1.right, r2.right)

        return check(p, q)
